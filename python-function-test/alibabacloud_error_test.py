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

from mock import patch

from alibabacloud.client import AlibabaCloudClient
from alibabacloud.clients.ecs_20140526 import EcsClient
from alibabacloud.exceptions import ServerException, InvalidRegionIDException, HttpErrorException
from alibabacloud.handlers.api_protocol_handler import APIProtocolHandler
from alibabacloud.handlers.credentials_handler import CredentialsHandler
from alibabacloud.handlers.endpoint_handler import EndpointHandler
from alibabacloud.handlers.http_handler import HttpHandler
from alibabacloud.handlers.retry_handler import RetryHandler
from alibabacloud.handlers.server_error_handler import ServerErrorHandler
from alibabacloud.handlers.signer_handler import SignerHandler
from alibabacloud.handlers.timeout_config_reader import TimeoutConfigReader
from alibabacloud.request import APIRequest
from alibabacloud.vendored import six
from alibabacloud.vendored.requests import Response
from base import SDKTestBase

http_handler = HttpHandler()
DEFAULT_HANDLERS = [
    RetryHandler(),
    APIProtocolHandler(),
    CredentialsHandler(),
    SignerHandler(),
    TimeoutConfigReader(),
    EndpointHandler(),
    http_handler,
    ServerErrorHandler(),
]


class ErrorTest(SDKTestBase):

    def test_server_unreachable(self):
        client_config = self.client_config
        client_config.region_id = 'cn-abc'
        client = AlibabaCloudClient(client_config, self.init_credentials_provider())
        client.product_code = "Ecs"
        client.api_version = "2014-05-26"
        client.location_service_code = 'ecs'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC')
        try:
            client._handle_request(api_request)
            assert False
        except InvalidRegionIDException as e:
            self.assertTrue(e.error_message.startswith(
                "No such region 'cn-abc'. Please check your region ID."))

    def test_server_error_normal(self):
        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())
        try:
            ecs_client.delete_instance(instance_id="blah")
            assert False
        except ServerException as e:
            self.assertEqual("InvalidInstanceId.NotFound", e.error_code)
            self.assertEqual("The specified InstanceId does not exist.",
                             e.error_message)

    def test_server_timeout(self):
        self.client_config.read_timeout = 0.001
        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())

        try:
            ecs_client.create_instance(image_id="coreos_1745_7_0_64_30G_alibase_20180705.vhd",
                                       instance_type="ecs.cn-hangzhou.invalid",
                                       system_disk_category="cloud_ssd")
            assert False
        except HttpErrorException as e:
            self.assertEqual("HTTPConnectionPool(host='ecs-cn-hangzhou.aliyuncs.com',"
                             " port=80): Read timed out. (read timeout=0.001)",
                             e.error_message)

    def test_server_error_with_a_bad_json(self):

        def _handle_request(context):
            context.retry_flag = False
            context.http_response = Response()
            context.http_response.status_code = 400
            context.http_response.headers = {}
            context.http_response._content = b"bad-json"

        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())

        ecs_client.handlers = DEFAULT_HANDLERS

        with patch.object(http_handler, "handle_request", wraps=_handle_request):
            try:
                ecs_client.delete_instance()
                assert False
            except ServerException as e:
                self.assertEqual(400, e.http_status)
                self.assertEqual("Ecs", e.service_name)
                self.assertEqual("ecs-cn-hangzhou.aliyuncs.com", e.endpoint)
                self.assertEqual("SDK.UnknownServerError", e.error_code)
                if six.PY2:
                    self.assertEqual('ServerResponseBody: bad-json', e.error_message)
                else:
                    self.assertEqual("ServerResponseBody: b'bad-json'", e.error_message)

    def test_server_error_with_valid_json_no_code_or_message(self):
        # test valid json format but no Code or Message
        def _handle_request(context):
            context.retry_flag = False
            context.http_response = Response()
            context.http_response.status_code = 400
            context.http_response.headers = {}
            context.http_response._content = b"""{"key" : "this is a valid json string"}"""

        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())

        ecs_client.handlers = DEFAULT_HANDLERS
        with patch.object(http_handler, "handle_request", wraps=_handle_request):
            try:
                ecs_client.describe_instances()
                assert False
            except ServerException as e:
                self.assertEqual(400, e.http_status)
                self.assertEqual("Ecs", e.service_name)
                self.assertEqual("ecs-cn-hangzhou.aliyuncs.com", e.endpoint)
                self.assertEqual("SDK.UnknownServerError", e.error_code)
                if six.PY2:
                    self.assertEqual(
                        'ServerResponseBody: {"key" : "this is a valid json string"}',
                        e.error_message)
                else:
                    self.assertEqual(
                        """ServerResponseBody: b'{"key" : "this is a valid json string"}'""",
                        e.error_message)

    def test_missing_code_in_response(self):
        # test missing Code in response
        def _handle_request(context):
            context.retry_flag = False
            context.http_response = Response()
            context.http_response.status_code = 400
            context.http_response.headers = {}
            context.http_response._content = b"{\"Message\": \"Some message\"}"

        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())

        ecs_client.handlers = DEFAULT_HANDLERS

        with patch.object(http_handler, "handle_request", wraps=_handle_request):
            try:
                ecs_client.describe_instances()
                assert False
            except ServerException as e:
                self.assertEqual(400, e.http_status)
                self.assertEqual("Ecs", e.service_name)
                self.assertEqual("ecs-cn-hangzhou.aliyuncs.com", e.endpoint)
                self.assertEqual("SDK.UnknownServerError", e.error_code)
                if six.PY2:
                    self.assertEqual("Some message", e.error_message)
                else:
                    self.assertEqual("""Some message""", e.error_message)

    def test_missing_message_in_response(self):
        # test missing message in response
        def _handle_request(context):
            context.retry_flag = False
            context.http_response = Response()
            context.http_response.status_code = 400
            context.http_response.headers = {}
            context.http_response._content = b"{\"Message\": \"Some message\"}"

        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())

        ecs_client.handlers = DEFAULT_HANDLERS
        with patch.object(http_handler, "handle_request", wraps=_handle_request):
            try:
                ecs_client.describe_regions()
                assert False
            except ServerException as e:
                self.assertEqual(400, e.http_status)
                self.assertEqual("Ecs", e.service_name)
                self.assertEqual("ecs-cn-hangzhou.aliyuncs.com", e.endpoint)
                self.assertEqual("SDK.UnknownServerError", e.error_code)
                self.assertEqual("""Some message""", e.error_message)

    def test_missing_message_in_response2(self):
        # test missing Code in response
        def _handle_request(context):
            context.retry_flag = False
            context.http_response = Response()
            context.http_response.status_code = 400
            context.http_response.headers = {}
            context.http_response._content = b"{\"Code\": \"YouMessedSomethingUp\"}"

        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())

        ecs_client.handlers = DEFAULT_HANDLERS

        with patch.object(http_handler, "handle_request", wraps=_handle_request):
            try:
                ecs_client.describe_regions()
                assert False
            except ServerException as e:
                self.assertEqual(400, e.http_status)
                self.assertEqual("Ecs", e.service_name)
                self.assertEqual("ecs-cn-hangzhou.aliyuncs.com", e.endpoint)
                self.assertEqual("YouMessedSomethingUp", e.error_code)
                if six.PY2:
                    self.assertEqual('ServerResponseBody: {"Code": "YouMessedSomethingUp"}',
                                     e.error_message)
                else:
                    self.assertEqual("""ServerResponseBody: b'{"Code": "YouMessedSomethingUp"}'""",
                                     e.error_message)
