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
from alibabacloud.exceptions import ServerException
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

test_unicode = "\u007b\u0026\u0071\u0075\u006f\u0074\u003b\u006e\u0061\u006d" \
               "\u0065\u0026\u0071\u0075\u006f\u0074\u003b\u0020\u003a\u0020" \
               "\u0026\u0071\u0075\u006f\u0074\u003b\u0063\u006c\u006f\u0075" \
               "\u0064\u0026\u0071\u0075\u006f\u0074\u003b\u007d"

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

from alibabacloud import get_client


class APIRequestTest(SDKTestBase):

    def _init_client(self, service_name, api_version=None):
        client = get_client(service_name=service_name, api_version=api_version,
                            region_id=self.region_id,
                            access_key_id=self.access_key_id,
                            access_key_secret=self.access_key_secret,
                            config=self.init_client_config())
        return client

    def test_request_with_ecs(self):
        ecs_client = self._init_client('ecs')
        delete_version = ["1.0.1", ]

        try:
            context = ecs_client.delete_launch_template_version(
                list_of_delete_version=delete_version)
            assert False
        except ServerException as e:
            self.assertEqual(e.http_status, 400)
            self.assertEqual(e.error_code, "InvalidParameter")
            self.assertEqual(e.error_message,
                             'The specified parameter "DeleteVersion.1" is not valid.')

    def test_request_with_rds(self):
        rds_client = self._init_client('rds')
        result = rds_client.describe_db_instances()
        self.assertTrue(result.get("Items"))

    def test_request_with_cdn(self):
        cdn_client = self._init_client('cdn', '2014-11-11')
        response = cdn_client.describe_cdn_types()
        self.assertTrue(response.get("CdnTypes"))

    def test_request_with_cdn_new(self):
        client_new = self._init_client('cdn')
        result = client_new.describe_cdn_certificate_detail(cert_name="sdk-test")
        self.assertTrue(result.get("RequestId"))

    def test_request_with_slb(self):
        client = self._init_client('slb')
        result = client.describe_access_control_lists()
        self.assertTrue(result.get("Acls"))

    def test_request_with_ram(self):
        client = self._init_client('ram')
        response = client.list_access_keys()
        self.assertTrue(response.get("AccessKeys"))

    def test_request_with_vpc(self):
        client = self._init_client('vpc')

        result = client.describe_access_points()
        self.assertTrue(result.get("AccessPointSet"))

    def test_request_with_listkeys(self):

        client = AlibabaCloudClient(self.client_config,
                                    credentials_provider=self.init_credentials_provider())
        client.product_code = "Kms"
        client.api_version = "2016-01-20"
        client.location_service_code = 'kms'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('ListKeys', 'GET', 'https', 'RPC')
        try:
            context = client._handle_request(api_request)
        except ServerException as e:
            self.assertEqual(e.http_status, 403)
        else:
            response = context.result
            self.assertTrue(response.get("PageNumber"))

    def test_request_with_body_unicode(self):

        def _handle_request(context):
            context.retry_flag = False
            context.http_response = Response()
            context.http_response.status_code = 400
            context.http_response.headers = {}
            context.http_response._content = test_unicode

        client = self._init_client('ecs')

        client.handlers = DEFAULT_HANDLERS

        with patch.object(http_handler, "handle_request", wraps=_handle_request):
            try:
                client.describe_regions()
                assert False
            except ServerException as e:
                self.assertEqual(400, e.http_status)
                self.assertEqual("Ecs", e.service_name)
                self.assertEqual("ecs-cn-hangzhou.aliyuncs.com", e.endpoint)
                self.assertEqual("SDK.UnknownServerError", e.error_code)
                if six.PY2:
                    self.assertEqual(e.error_message, 'ServerResponseBody: ' + test_unicode)
                else:
                    self.assertEqual("ServerResponseBody: {&quot;name&quot; : &quot;cloud&quot;}",
                                     e.error_message)

    def test_request_with_body_escape(self):
        def _handle_request(context):
            context.retry_flag = False
            context.http_response = Response()
            context.http_response.status_code = 400
            context.http_response.headers = {}
            context.http_response._content = "{\"Message\": \"Some message\"}"

        client = self._init_client('ecs')

        client.handlers = DEFAULT_HANDLERS

        with patch.object(http_handler, "handle_request", wraps=_handle_request):
            try:
                client.describe_regions()
                assert False
            except ServerException as e:
                self.assertEqual(400, e.http_status)
                self.assertEqual("Ecs", e.service_name)
                self.assertEqual("ecs-cn-hangzhou.aliyuncs.com", e.endpoint)
                self.assertEqual("SDK.UnknownServerError", e.error_code)
                self.assertEqual("Some message", e.error_message)
