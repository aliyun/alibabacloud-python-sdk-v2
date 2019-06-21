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
from alibabacloud import get_client
from alibabacloud.client import AlibabaCloudClient
from alibabacloud.client import ClientConfig
from alibabacloud.credentials import AccessKeyCredentials
from alibabacloud.credentials.provider import RamRoleCredentialsProvider
from alibabacloud.exceptions import ServerException, InvalidRegionIDException
from alibabacloud.request import APIRequest
from base import SDKTestBase


class ROSClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None):
        AlibabaCloudClient.__init__(self, client_config, credentials_provider)
        self.product_code = 'ROS'
        self.api_version = '2015-09-01'
        self.location_service_code = 'ros'
        self.location_endpoint_type = 'openAPI'

    def describe_resource_types(self, support_status=None):
        api_request = APIRequest('DescribeResourceTypes', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/resource_types'
        api_request._params = {"SupportStatus": support_status}
        return self._handle_request(api_request).result


class CloudLevelTest(SDKTestBase):

    def _init_client(self, service_name, api_version=None, region_id='cn-hangzhou'):
        client = get_client(service_name=service_name, api_version=api_version,
                            region_id=region_id,
                            access_key_id=self.access_key_id,
                            access_key_secret=self.access_key_secret,
                            config=self.init_client_config())
        return client

    def test_rpc_with_regions_request(self):

        ecs_client = self._init_client('ecs')
        response = ecs_client.describe_regions()
        self.assertTrue(response.get("Regions"))
        self.assertTrue(response.get("RequestId"))

    def test_roa_with_resource_types_request(self):

        ros_client = ROSClient(self.client_config,
                               credentials_provider=self.init_credentials_provider())
        response = ros_client.describe_resource_types()
        self.assertTrue(response.get("ResourceTypes"))

    def test_rpc_assume_role_request_with_sts_token(self):
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
        client.api_version = "2014-05-26"
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

    def test_roa_assume_role_request_with_sts_token(self):
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
        client.api_version = "2015-09-01"
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

    def test_rpc_regions_request_with_error(self):
        self.client_config.region_id = 'abc'
        ecs_client = get_client(service_name='ecs',
                                access_key_id=self.access_key_id,
                                access_key_secret=self.access_key_secret,
                                config=self.client_config)

        with self.assertRaises(InvalidRegionIDException) as e:
            ecs_client.describe_regions()
        self.assertEqual(e.exception.error_message, "No such region 'abc'."
                                                    " Please check your region ID.")

    def test_rpc_regions_request_with_unicode(self):
        ecs_client = self._init_client('ecs')
        try:
            ecs_client.describe_regions(owner_account="&#111;&#119;&#110;&#101;")
            assert False

        except ServerException as e:
            self.assertEqual(e.error_code, "InvalidParameter.OwnerAccount")
            self.assertEqual(e.error_message, "OwnerAccount is Invalid.")

    def test_roa_regions_types_request_with_unicode(self):
        ros_client = ROSClient(self.client_config,
                               credentials_provider=self.init_credentials_provider())

        response = ros_client.describe_resource_types(support_status='&#114;&#101;')
        self.assertTrue(response.get("ResourceTypes") == [])

    def test_rpc_regions_request_with_query(self):
        ecs_client = self._init_client('ecs')

        with self.assertRaises(ServerException) as e:
            ecs_client.describe_regions(owner_account="owner&account")

        self.assertEqual(e.exception.error_code, "InvalidParameter.OwnerAccount")
        self.assertEqual(e.exception.error_message, "OwnerAccount is Invalid.")

    def test_roa_regions_types_request_with_query(self):

        ros_client = ROSClient(self.client_config,
                               credentials_provider=self.init_credentials_provider())
        response = ros_client.describe_resource_types(support_status='resource&types;')
        self.assertTrue(response.get("ResourceTypes") == [])
