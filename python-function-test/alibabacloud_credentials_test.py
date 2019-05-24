# Copyright 2019 Alibaba Cloud Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import mock

from alibabacloud.client import ClientConfig, AlibabaCloudClient, get_merged_client_config
from alibabacloud.credentials import AccessKeyCredentials
from alibabacloud.credentials.provider import RamRoleCredentialsProvider, StaticCredentialsProvider, \
    DefaultChainedCredentialsProvider, ProfileCredentialsProvider, \
    InstanceProfileCredentialsProvider
from alibabacloud.exceptions import ServerException, ClientException
from alibabacloud.request import APIRequest
from alibabacloud.utils import ini_helper
from alibabacloud.vendored import requests
from base import SDKTestBase, MyServer

role_name = {u'Code': u'Success', u'LastUpdated': u'2019-04-09T10:41:31Z',
             u'AccessKeyId': u'STS.NHLK9qYbdbKgs4oYTRXqjLSdX',
             u'AccessKeySecret': u'J94mBKoeEUzDGwgUUsdXcf8hdbDm9Pht4A4R9vKParVT',
             u'Expiration': u'2019-04-09T16:41:31Z',
             u'SecurityToken': u'CAISigJ1q6Ft5B2yfSjIr4'
                               u'v5AIPFtL1F1YmMcRLevVQHVP5Go5bPujz2IHlFeXBoCekes/8'
                               u'yn29S6vwalrRtTtpfTEmBbI569s0M9hGjPZSQsM+n5qVUk5+1'
                               u'BjBe3ZEEFIqADd/iRfbxJ92PCTmd5AIRrJL+cTK9JS/HVbSCl'
                               u'Z9gaPkOQwC8dkAoLdxKJwxk2qR4XDmrQpTLCBPxhXfKB0dFox'
                               u'd1jXgFiZ6y2cqB8BHT/jaYo603392gcsj+NJc1ZssjA47oh7R'
                               u'MG/CfgHIK2X9j77xriaFIwzDDs+yGDkNZixf8aLOFr4Q3fFYh'
                               u'O/NnQPEe8KKkj5t1sffJnoHtzBJAIexOTzRtjFVtcH5xchqAA'
                               u'U8ECYWEiFKZtXwEpMnJUW4UXeXgzhMYDCeoLzrwQxcDwxpVEH'
                               u'KfA1zt+i/yAOXhJ1EgWwDPjyIeeFiR5VypJaHstnq/P0Jv/Uq'
                               u'ZAOS88KwDNLMHAc34HwmPNUnlsWc95B40ys91qtyHxQa1Jjjs'
                               u'LgE/S/5WyUQslQmuQI6e/rnT'}


class CredentialsTest(SDKTestBase):

    def test_call_request_with_client_env_priority(self):
        self._create_default_ram_user()
        # self._attach_default_policy()
        self._create_access_key()
        self._create_default_ram_role()

        client_config = ClientConfig(region_id=self.region_id)
        ram_role_arn_credential = RamRoleCredentialsProvider(
            client_config,
            AccessKeyCredentials(self.ram_user_access_key_id,
                                 self.ram_user_access_key_secret),
            self.ram_role_arn,
            "alice_test")
        client = AlibabaCloudClient(client_config, ram_role_arn_credential)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')

        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = self.access_key_secret

        response = client._handle_request(api_request)
        response_credential = response.http_request.credentials
        self.assertTrue(response_credential.access_key_id.startswith("STS."))
        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_request_with_env_config_priority(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = self.access_key_secret

        client_config = ClientConfig(region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        response = client._handle_request(api_request)

        env_credential_id = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_ID")
        env_credential_secret = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
        response_key_id = response.http_request.credentials.access_key_id
        response_key_secret = response.http_request.credentials.access_key_secret
        self.assertEqual(env_credential_id, response_key_id)
        self.assertEqual(env_credential_secret, response_key_secret)

        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_request_with_env_role_name_priority(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = self.access_key_secret
        os.environ["ALIBABA_CLOUD_ROLE_NAME"] = self.default_ram_role_name

        client_config = ClientConfig(region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        response = client._handle_request(api_request)

        env_credential_id = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_ID")
        env_credential_secret = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
        response_key_id = response.http_request.credentials.access_key_id
        response_key_secret = response.http_request.credentials.access_key_secret
        self.assertEqual(env_credential_id, response_key_id)
        self.assertEqual(env_credential_secret, response_key_secret)

        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_request_with_config_role_name_priority(self):
        os.environ["ALIBABA_CLOUD_ROLE_NAME"] = self.default_ram_role_name

        client_config = ClientConfig(region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        response = client._handle_request(api_request)

        response_key_id = response.http_request.credentials.access_key_id
        self.assertFalse(response_key_id.startswith("TST."))

        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_rpc_request_with_introduction_ak(self):
        client_config = ClientConfig(access_key_id=self.access_key_id,
                                     access_key_secret=self.access_key_secret,
                                     region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        response = client._handle_request(api_request)
        response_credentials = response.http_request.credentials
        from alibabacloud.credentials import AccessKeyCredentials
        self.assertEqual(type(response_credentials), AccessKeyCredentials)

        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_introduction_ak(self):
        client_config = ClientConfig(access_key_id=self.access_key_id,
                                     access_key_secret=self.access_key_secret,
                                     region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "ROS"
        client.product_version = "2015-09-01"
        client.location_service_code = 'ros'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeResourceTypes', 'GET', 'https', 'ROA')
        api_request.uri_pattern = '/resource_types'
        api_request.path_params = None
        response = client._handle_request(api_request)
        response_credentials = response.http_request.credentials
        from alibabacloud.credentials import AccessKeyCredentials
        self.assertEqual(type(response_credentials), AccessKeyCredentials)

        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_call_rpc_request_with_sts_token(self):
        self._create_default_ram_user()
        # self._attach_default_policy()
        self._create_access_key()
        self._create_default_ram_role()

        acs_client = ClientConfig(region_id=self.region_id)
        ram_role_arn_credential = RamRoleCredentialsProvider(
            acs_client,
            AccessKeyCredentials(self.ram_user_access_key_id,
                                 self.ram_user_access_key_secret),
            self.ram_role_arn,
            "alice_test")
        client = AlibabaCloudClient(acs_client, ram_role_arn_credential)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        response = client._handle_request(api_request)

        response_credentials = response.http_request.credentials
        self.assertTrue(response_credentials.access_key_id.startswith("STS."))

        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_ram_role(self):
        self._create_default_ram_user()
        # self._attach_default_policy()
        self._create_access_key()
        self._create_default_ram_role()

        roa_client = ClientConfig(region_id=self.region_id)
        ram_role_arn_credential = RamRoleCredentialsProvider(
            roa_client,
            AccessKeyCredentials(self.ram_user_access_key_id,
                                 self.ram_user_access_key_secret),
            self.ram_role_arn,
            "alice_test")
        client = AlibabaCloudClient(roa_client, ram_role_arn_credential)
        client.product_code = "ROS"
        client.product_version = "2015-09-01"
        client.location_service_code = 'ros'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeResourceTypes', 'GET', 'https', 'ROA')
        api_request.uri_pattern = '/resource_types'
        api_request.path_params = None
        response = client._handle_request(api_request)

        response_credentials = response.http_request.credentials
        self.assertTrue(response_credentials.access_key_id.startswith("STS."))

        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_call_rpc_request_with_env_ak(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = self.access_key_secret

        client_config = ClientConfig(region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        response = client._handle_request(api_request)
        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_env_ak(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_SECRET"] = self.access_key_secret

        client_config = ClientConfig(access_key_id=self.access_key_id,
                                     access_key_secret=self.access_key_secret,
                                     region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "ROS"
        client.product_version = "2015-09-01"
        client.location_service_code = 'ros'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeResourceTypes', 'GET', 'https', 'ROA')
        api_request.uri_pattern = '/resource_types'
        api_request.path_params = None
        response = client._handle_request(api_request)
        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    @mock.patch("alibabacloud.credentials.provider.InstanceProfileCredentialsProvider")
    def test_call_rpc_request_with_role_name(self, InstanceProfileCredentialsProvider):
        with MyServer() as f:
            os.environ["ALIBABA_CLOUD_ROLE_NAME"] = self.default_ram_role_name
            InstanceProfileCredentialsProvider.rotate_credentials.return_value = \
                requests.get(url="http://localhost:51352")
            InstanceProfileCredentialsProvider.rotate_credentials. \
                return_value = role_name
            self.assertTrue(InstanceProfileCredentialsProvider.rotate_credentials)

    def test_call_rpc_request_with_config_default(self):
        client_config = ClientConfig(region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        response = client._handle_request(api_request)
        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("Regions"))
        self.assertTrue(ret.get("RequestId"))

    def test_call_roa_request_with_config_default(self):
        client_config = ClientConfig(region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "ROS"
        client.product_version = "2015-09-01"
        client.location_service_code = 'ros'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeResourceTypes', 'GET', 'https', 'ROA')
        api_request.uri_pattern = '/resource_types'
        api_request.path_params = None
        response = client._handle_request(api_request)
        response = response.http_response.content
        ret = self.get_dict_response(response)
        self.assertTrue(ret.get("ResourceTypes"))

    def test_call_rpc_request_with_key_error(self):
        client_config = ClientConfig(access_key_id="BadAccessKeyId",
                                     access_key_secret=self.access_key_secret,
                                     region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        with self.assertRaises(ServerException) as e:
            client._handle_request(api_request)
        self.assertEqual(e.exception.service_name, "Ecs")
        self.assertEqual(e.exception.http_status, 404)
        self.assertEqual(e.exception.endpoint, "ecs-cn-hangzhou.aliyuncs.com")
        self.assertEqual(e.exception.error_code, "InvalidAccessKeyId.NotFound")
        self.assertEqual(e.exception.error_message, "Specified access key is not found.")

    def test_call_roa_request_with_key_error(self):
        client_config = ClientConfig(access_key_id="BadAccessKeyId",
                                     access_key_secret=self.access_key_secret,
                                     region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "ROS"
        client.product_version = "2015-09-01"
        client.location_service_code = 'ros'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeResourceTypes', 'GET', 'https', 'ROA')
        with self.assertRaises(ServerException) as e:
            client._handle_request(api_request)
        self.assertEqual(e.exception.service_name, "ROS")
        self.assertEqual(e.exception.http_status, 404)
        self.assertEqual(e.exception.endpoint, "ros.aliyuncs.com")
        self.assertEqual(e.exception.error_code, "InvalidAction.NotFound")
        self.assertEqual(e.exception.error_message,
                         "Specified api is not found, please check your url and method.")

    def test_call_rpc_request_with_secret_error(self):
        client_config = ClientConfig(access_key_id=self.access_key_id,
                                     access_key_secret="BadAccessKeySecret",
                                     region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "Ecs"
        client.product_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        with self.assertRaises(ServerException) as e:
            client._handle_request(api_request)
        self.assertEqual(e.exception.service_name, "Ecs")
        self.assertEqual(e.exception.http_status, 400)
        self.assertEqual(e.exception.endpoint, "ecs-cn-hangzhou.aliyuncs.com")
        self.assertEqual(e.exception.error_code, "InvalidAccessKeySecret")
        self.assertEqual(e.exception.error_message,
                         "The AccessKeySecret is incorrect. "
                         "Please check your AccessKeyId and AccessKeySecret.")

    def test_call_roa_request_with_secret_error(self):
        client_config = ClientConfig(access_key_id=self.access_key_id,
                                     access_key_secret="BadAccessKeySecret",
                                     region_id=self.region_id)
        client = AlibabaCloudClient(client_config, None)
        client.product_code = "ROS"
        client.product_version = "2015-09-01"
        client.location_service_code = 'ros'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeResourceTypes', 'GET', 'https', 'ROA')
        with self.assertRaises(ServerException) as e:
            client._handle_request(api_request)
        self.assertEqual(e.exception.service_name, "ROS")
        self.assertEqual(e.exception.http_status, 404)
        self.assertEqual(e.exception.endpoint, "ros.aliyuncs.com")
        self.assertEqual(e.exception.error_code, "InvalidAction.NotFound")
        self.assertEqual(e.exception.error_message,
                         "Specified api is not found, please check your url and method.")

    def test_call_request_with_env_error(self):
        os.environ["ALIBABA_CLOUD_ACCESS_KEY_ID"] = self.access_key_id
        os.environ.pop("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
        client_config = ClientConfig(region_id=self.region_id)
        with self.assertRaises(ClientException) as e:
            DefaultChainedCredentialsProvider(client_config)
        self.assertEqual(e.exception.error_message,
                         "Environment variable ALIBABA_CLOUD_ACCESS_KEY_SECRET cannot be empty.")

    def test_local_file_default_config_with_path_error(self):
        os.environ.setdefault('ALIBABA_CLOUD_CREDENTIALS_FILE', 'abc')
        client_config = ClientConfig(region_id=self.region_id)
        with self.assertRaises(ClientException) as e:
            DefaultChainedCredentialsProvider(client_config)
        self.assertEqual(e.exception.error_message, "Failed to find config file for SDK: abc")
        os.environ.pop("ALIBABA_CLOUD_CREDENTIALS_FILE")

    def test_local_file_default_config_with_none_error(self):
        client_config = ClientConfig(region_id=self.region_id)
        with self.assertRaises(ClientException) as e:
            DefaultChainedCredentialsProvider(client_config, profile_name="abc")
        self.assertEqual(e.exception.error_message, "Can not find valid credentials provider.")

    def test_local_file_default_config_with_provider_pair_error(self):
        client_config = ClientConfig(region_id=self.region_id)
        with self.assertRaises(ClientException) as e:
            DefaultChainedCredentialsProvider(client_config, profile_name="client4")
        self.assertEqual(e.exception.error_message, "RSA Key Pair credentials are not supported.")
