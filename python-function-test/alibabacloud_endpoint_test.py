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
import json

from mock import patch

from alibabacloud.client import AlibabaCloudClient
from alibabacloud.clients.ecs_20140526 import EcsClient
from alibabacloud.endpoint.chained_endpoint_resolver import ChainedEndpointResolver
from alibabacloud.endpoint.default_endpoint_resolver import DefaultEndpointResolver
from alibabacloud.endpoint.local_config_global_endpoint_resolver import \
    LocalConfigGlobalEndpointResolver
from alibabacloud.endpoint.local_config_regional_endpoint_resolver import \
    LocalConfigRegionalEndpointResolver
from alibabacloud.endpoint.location_service_endpoint_resolver import LocationServiceEndpointResolver
from alibabacloud.endpoint.resolver_endpoint_request import ResolveEndpointRequest
from alibabacloud.endpoint.user_customized_endpoint_resolver import UserCustomizedEndpointResolver
from alibabacloud.exceptions import ServerException, NoSuchEndpointException, \
    InvalidRegionIDException, HttpErrorException, InvalidProductCodeException
from alibabacloud.request import APIRequest
from base import SDKTestBase


class EndpointTest(SDKTestBase):

    def setUp(self):
        SDKTestBase.setUp(self)
        DefaultEndpointResolver.predefined_endpoint_resolver = UserCustomizedEndpointResolver()

    def init_env(self, config, credentials_provider, test_local_config=None):
        resolver_chain = []

        self._user_customized_endpoint_resolver = UserCustomizedEndpointResolver()
        if test_local_config is None:
            self._local_config_regional_endpoint_resolver = LocalConfigRegionalEndpointResolver()
            self._local_config_global_endpoint_resolver = LocalConfigGlobalEndpointResolver()
        else:
            self._local_config_regional_endpoint_resolver = \
                LocalConfigRegionalEndpointResolver(test_local_config)
            self._local_config_global_endpoint_resolver = \
                LocalConfigGlobalEndpointResolver(test_local_config)
            # FIXME client
        self._location_service_endpoint_resolver = \
            LocationServiceEndpointResolver(config, credentials_provider)

        resolver_chain.append(self._user_customized_endpoint_resolver)
        resolver_chain.append(self._local_config_regional_endpoint_resolver)
        resolver_chain.append(self._local_config_global_endpoint_resolver)
        resolver_chain.append(self._location_service_endpoint_resolver)

        self._endpoint_resolver = ChainedEndpointResolver(resolver_chain)

    def resolve(self, region_id, product_code, location_service_code=None,
                endpoint_type=None):
        request = ResolveEndpointRequest(region_id, product_code,
                                         location_service_code, endpoint_type)
        return self._endpoint_resolver.resolve(request)

    def resolve_request(self, region_id, product_code, location_service_code=None,
                        endpoint_type=None):
        request = ResolveEndpointRequest(region_id, product_code,
                                         location_service_code, endpoint_type)
        return request

    def temp_client(self, product, version=None, endpoint_type=None, location_service_code=None):

        client_config = self.client_config

        class TempClient(AlibabaCloudClient):
            def __init__(_self):
                AlibabaCloudClient.__init__(_self, client_config, self.init_credentials_provider())
                self.product_code = product
                self.location_service_code = location_service_code
                self.api_version = version
                self.location_endpoint_type = endpoint_type

        return TempClient()

    def test_products_with_location_service(self):
        client = AlibabaCloudClient(self.client_config, self.init_credentials_provider())
        client.product_code = "Ecs"
        client.api_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        response = client._handle_request(api_request)

    def test_products_without_location_service(self):
        from alibabacloud.clients.ram_20150501 import RamClient
        client = RamClient(client_config=self.client_config,
                           credentials_provider=self.init_credentials_provider())
        response = client.list_access_keys()
        self.assertTrue(response.get('RequestId'))

    def test_regional_endpoint_comes_from_local_config(self):
        test_config = """
            {
                "regional_endpoints" : {
                    "abc" : {
                        "mars-ningbo" : "ecs.mars-ningbo.aliyuncs.com"
                    }
                }
            }
        """
        temp_client = self.temp_client('abc')
        self.init_env(temp_client.config, temp_client.credentials_provider, test_config)

        self.assertEqual(
            "ecs.mars-ningbo.aliyuncs.com",
            self.resolve("mars-ningbo", "abc")
        )

    def test_global_endpoint_comes_from_local_config(self):
        test_config = """
            {
                "regional_endpoints" : {
                    "abc" : {
                        "mars-ningbo" : "ecs.mars-ningbo.aliyuncs.com"
                    }
                },
                "global_endpoints" : {
                    "abc" : "ecs.mars.aliyuncs.com"
                },
                "regions" : ["mars-ningbo", "mars-hangzhou", "mars-shanghai"]
            }
        """
        temp_client = self.temp_client('abc')
        self.init_env(temp_client, temp_client.credentials_provider, test_config)

        self.assertEqual(
            "ecs.mars-ningbo.aliyuncs.com",
            self.resolve("mars-ningbo", "abc")
        )
        self.assertEqual(
            "ecs.mars.aliyuncs.com",
            self.resolve("mars-hangzhou", "abc")
        )
        self.assertEqual(
            "ecs.mars.aliyuncs.com",
            self.resolve("mars-shanghai", "abc")
        )

    def test_endpoint_comes_from_location_service(self):
        temp_client = self.temp_client('ECS', None, None, 'ecs')
        self.init_env(temp_client.config,
                      temp_client.credentials_provider, "{}")  # empty local config

        from alibabacloud.clients.ecs_20140526 import EcsClient
        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())
        ecs_client.describe_regions()

        ecs_client.endpoint_resolver = DefaultEndpointResolver(
            ecs_client.config, ecs_client.credentials_provider)
        with patch.object(
                self._location_service_endpoint_resolver,
                '_call_location_service',
                wraps=self._location_service_endpoint_resolver._call_location_service
        ) as monkey:
            for i in range(3):
                self.assertEqual(
                    "ecs-cn-hangzhou.aliyuncs.com",
                    ecs_client.endpoint_resolver.resolve(
                        self.resolve_request("cn-hangzhou", "ecs", "ecs", None))
                )

        self.assertEqual(0, monkey.call_count)

    def test_location_service_miss(self):
        temp_client = self.temp_client("Ram", None, 'openAPI', 'ram')
        self.init_env(temp_client.config,
                      temp_client.credentials_provider, "{}")  # empty local config

        with patch.object(
                self._location_service_endpoint_resolver,
                '_call_location_service',
                wraps=self._location_service_endpoint_resolver._call_location_service
        ) as monkey:

            self.assertEqual(0, monkey.call_count)
            # No openAPI data
            for i in range(3):
                try:
                    self.resolve("cn-hangzhou", "Ram", "ram", "openAPI")
                    assert False
                except NoSuchEndpointException as e:
                    self.assertTrue(e.error_message.startswith(
                        "No endpoint in the region 'cn-hangzhou' for product 'Ram'."
                    ))

            self.assertEqual(1, monkey.call_count)

            # Bad region ID
            for i in range(3):
                try:
                    self.resolve("mars", "Ram", "ram", "openAPI")
                    assert False
                except InvalidRegionIDException as e:
                    self.assertEqual(
                        "No such region 'mars'. Please check your region ID.",
                        e.error_message)

            self.assertEqual(2, monkey.call_count)
            # Bad region ID with another product
            try:
                self.resolve("mars", "Ecs", "ecs", "openAPI")
                assert False
            except InvalidRegionIDException as e:
                self.assertEqual("No such region 'mars'. Please check your region ID.",
                                 e.error_message)

            self.assertEqual(2, monkey.call_count)

            # Bad product code
            for i in range(3):
                try:
                    self.resolve("cn-hangzhou", "InvalidProductCode",
                                 "InvalidProductCode", "openAPI")
                    assert False
                except InvalidProductCodeException as e:
                    self.assertTrue(e.error_message.startswith(
                        "No endpoint for product 'InvalidProductCode'.\n"
                        "Please check the product code, "
                        "or set an endpoint for your request explicitly.\n"
                    ))

            # Bad product code with another region ID
            try:
                self.resolve("cn-beijing", "InvalidProductCode", "InvalidProductCode", "openAPI")
                assert False
            except InvalidProductCodeException as e:
                self.assertTrue(e.error_message.startswith(
                    "No endpoint for product 'InvalidProductCode'.\n"
                    "Please check the product code, "
                    "or set an endpoint for your request explicitly.\n")
                )
            self.assertEqual(3, monkey.call_count)

    def test_try_to_get_endpoint_with_invalid_region_id(self):
        temp_client = self.temp_client('ecs')
        self.init_env(temp_client.config, temp_client.credentials_provider)
        try:
            self.resolve("mars", "Ecs")
            assert False
        except InvalidRegionIDException as e:
            self.assertEqual(
                "No such region 'mars'. Please check your region ID.",
                e.error_message)

    def test_try_to_get_endpoint_with_invalid_product_code(self):
        temp_client = self.temp_client('InvalidProductCode')

        self.init_env(temp_client.config, temp_client.credentials_provider)
        try:
            self.resolve("cn-beijing", "InvalidProductCode")
            assert False
        except InvalidProductCodeException as e:
            self.assertTrue(e.error_message.startswith(
                "No endpoint for product 'InvalidProductCode'.\n"
                "Please check the product code, "
                "or set an endpoint for your request explicitly.\n")
            )

    def test_inner_api_endpoint(self):
        temp_client = self.temp_client('Ram', endpoint_type='innerAPI', location_service_code='ram')

        self.init_env(temp_client.config, temp_client.credentials_provider)
        self.assertEqual(
            "ram-share.aliyuncs.com",
            self.resolve("cn-hangzhou", "Ram", "ram", "innerAPI")
        )

    def test_get_inner_api_endpoint_bypass_local_config(self):
        test_config = """
            {
                "regional_endpoints" : {
                    "ram" : {
                        "cn-hangzhou" : "ram.mars-ningbo.aliyuncs.com"
                    }
                },
                "global_endpoints" : {
                    "ram" : "ram.mars.aliyuncs.com"
                }
            }
        """
        temp_client = self.temp_client('Ram', None, 'innerAPI', 'ram')
        self.init_env(temp_client.config, temp_client.credentials_provider, test_config)
        self.assertEqual(
            "ram-share.aliyuncs.com",
            self.resolve("cn-hangzhou", "Ram", "ram", "innerAPI")
        )

    def test_get_inner_api_endpoint_by_manually_adding(self):
        temp_client = self.temp_client('Ram', '2015-06-12', 'innerAPI')
        self.init_env(temp_client, temp_client.credentials_provider)
        self._user_customized_endpoint_resolver.put_endpoint_entry(
            "cn-hangzhou",
            "Ram",
            "ram.cn-hangzhou.endpoint-test.exception.com"
        )
        self.assertEqual(
            "ram.cn-hangzhou.endpoint-test.exception.com",
            self.resolve("cn-hangzhou", "Ram", "ram", "innerAPI")
        )

    def test_can_not_connect_location_service(self):
        temp_client = self.temp_client("Ecs", None, 'innerAPI', 'ecs')

        self.init_env(temp_client.config, temp_client.credentials_provider)
        self._location_service_endpoint_resolver.set_location_service_endpoint(
            "location-on-mars.aliyuncs.com")
        try:
            self.resolve("cn-hangzhou", "Ecs", "ecs", "innerAPI")
            assert False
        except HttpErrorException as e:
            self.assertTrue(e.error_message.startswith(
                "HTTPSConnectionPool(host='location-on-mars.aliyuncs.com', port=443):"
                " Max retries exceeded with url"))

    def test_invalid_access_key_id(self):
        def my_credentials_provider():
            from alibabacloud.credentials import AccessKeyCredentials

            credentials = AccessKeyCredentials('BadAccessKeyId',
                                               self.access_key_secret)
            from alibabacloud.credentials.provider import StaticCredentialsProvider
            credentials_provider = StaticCredentialsProvider(credentials)
            return credentials_provider

        self.init_env(self.client_config, my_credentials_provider(), None)
        try:
            self.resolve("cn-hangzhou", "Ecs", "ecs", "innerAPI")
            assert False
        except ServerException as e:
            self.assertEqual(e.error_code, 'InvalidAccessKeyId.NotFound')
            self.assertEqual(e.error_message, 'Specified access key is not found.')

    def test_invalid_access_key_secret(self):
        def my_credentials_provider():
            from alibabacloud.credentials import AccessKeyCredentials

            credentials = AccessKeyCredentials(self.access_key_id,
                                               'BadAccessKeySecret')
            from alibabacloud.credentials.provider import StaticCredentialsProvider
            credentials_provider = StaticCredentialsProvider(credentials)
            return credentials_provider

        self.init_env(self.client_config, my_credentials_provider(), None)
        try:
            self.resolve("cn-hangzhou", "Ecs", "ecs", "innerAPI")
            assert False
        except ServerException as e:
            self.assertEqual(e.error_code, 'InvalidAccessKeySecret')
            self.assertEqual(e.error_message,
                             'The AccessKeySecret is incorrect. '
                             'Please check your AccessKeyId and AccessKeySecret.')

    def test_call_rpc_request_with_client(self):
        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())
        response = ecs_client.describe_regions()
        self.assertTrue(response.get('RequestId'))

    def test_call_roa_request_with_client(self):
        client = AlibabaCloudClient(self.client_config, self.init_credentials_provider())
        client.product_code = "ROS"
        client.api_version = "2015-09-01"
        client.location_service_code = 'ros'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeResourceTypes', 'GET', 'https', 'ROA')
        api_request.uri_pattern = '/stacks/[StackName]/[StackId]/resources'
        api_request.path_params = None
        api_request._params = {"StackId": "StackId", "StackName": "StackName"}

        try:
            response = client._handle_request(api_request)
            assert False
        except ServerException as e:
            self.assertEqual("InvalidUrl", e.error_code)
            self.assertTrue(e.error_message.startswith("Request url is invalid"))

    def test_location_service_code_not_equals_product_code(self):
        client = AlibabaCloudClient(self.client_config, self.init_credentials_provider())
        client.product_code = "CloudAPI"
        client.api_version = "2016-07-14"
        client.location_service_code = 'apigateway'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeApis', 'GET', 'https', 'RPC')
        context = client._handle_request(api_request)
        response = json.loads(str(context.http_response.text))
        self.assertTrue(response.get('RequestId'))

    def test_location_service_code_not_equals_product_code2(self):
        # The product changed from api_gateway to edas
        temp_client = self.temp_client('Edas', '2017-08-01', 'openAPI', 'BindSlb')
        self.init_env(temp_client.config, temp_client.credentials_provider, "{}")
        client = AlibabaCloudClient(self.client_config, self.init_credentials_provider())
        client.product_code = "CloudAPI"
        client.api_version = "2016-07-14"
        client.location_service_code = 'apigateway'
        client.location_endpoint_type = "openAPI"
        client._endpoint_resolver = self._endpoint_resolver

        with patch.object(
                self._location_service_endpoint_resolver,
                '_call_location_service',
                wraps=self._location_service_endpoint_resolver._call_location_service
        ) as monkey:
            for i in range(3):
                api_request = APIRequest('DescribeApis', 'GET', 'https', 'RPC')
                response = client._handle_request(api_request)
        self.assertEqual(0, monkey.call_count)

        client._endpoint_resolver = self._endpoint_resolver

    def test_doc_help_sample(self):
        self.client_config.endpoint = "ecs-cn-hangzhou.aliyuncs.com"
        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())
        response = ecs_client.describe_instances()
        self.assertTrue(response.get('RequestId'))

    def test_r_kvstore(self):
        temp_client = self.temp_client("R-kvstore")
        resolver = DefaultEndpointResolver(temp_client, temp_client.credentials_provider)
        request = ResolveEndpointRequest("cn-hangzhou", "R-kvstore", None, None)
        self.assertEqual("r-kvstore.aliyuncs.com", resolver.resolve(request))

    def test_dts_regions(self):
        temp_client = self.temp_client("dts")
        resolver = DefaultEndpointResolver(temp_client.config, temp_client.credentials_provider)
        request = ResolveEndpointRequest("cn-chengdu", "dts", None, None)

        expected_message = "No endpoint in the region 'cn-chengdu' for product 'dts'.\n" \
                           "You can set an endpoint for your request explicitly.\n" \
                           "Or you can use the other available regions: ap-southeast-1 " \
                           "cn-beijing cn-hangzhou cn-hongkong cn-huhehaote cn-qingdao " \
                           "cn-shanghai cn-shenzhen cn-zhangjiakou\n" \
                           "See https://www.alibabacloud.com/help/doc-detail/92074.htm\n"
        try:
            resolver.resolve(request)
            assert False
        except NoSuchEndpointException as e:
            self.assertEqual(expected_message, e.error_message)

    def test_bssopenapi_resolve(self):
        temp_client = self.temp_client("BssOpenApi")
        resolver = DefaultEndpointResolver(temp_client.config, temp_client.credentials_provider)
        request = ResolveEndpointRequest("cn-hangzhou", "BssOpenApi", None, None)
        self.assertEqual("business.aliyuncs.com", resolver.resolve(request))

        request = ResolveEndpointRequest("eu-west-1", "BssOpenApi", None, None)
        self.assertEqual("business.ap-southeast-1.aliyuncs.com", resolver.resolve(request))

    def test_faas_resolve(self):
        temp_client = self.temp_client("faas")
        resolver = DefaultEndpointResolver(temp_client.config, temp_client.credentials_provider)
        request = ResolveEndpointRequest("cn-hangzhou", "faas", None, None)
        self.assertEqual("faas.cn-hangzhou.aliyuncs.com", resolver.resolve(request))

        client = AlibabaCloudClient(self.client_config, self.init_credentials_provider())
        client.product_code = "faas"
        client.api_version = "2017-08-24"
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeLoadTaskStatus', 'POST', 'https', 'RPC')
        api_request._params = {"FpgaUUID": "blah", "InstanceId": "blah", "RoleArn": "blah"}

        try:
            client._handle_request(api_request)
            assert False
        except ServerException as e:
            self.assertEqual(e.error_code, "EntityNotExist.RoleError")
            self.assertEqual(e.error_message, "The specified Role not exists")
