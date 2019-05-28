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

from alibabacloud.vendored import six
from base import TestCase
from alibabacloud.client import ClientConfig, AlibabaCloudClient
from alibabacloud.exceptions import ServerException
from alibabacloud.handlers.credentials_handler import CredentialsHandler
from alibabacloud.handlers.endpoint_handler import EndpointHandler
from alibabacloud.handlers.http_handler import HttpHandler
from alibabacloud.handlers.api_protocol_handler import APIProtocolHandler
from alibabacloud.handlers.retry_handler import RetryHandler
from alibabacloud.handlers.server_error_handler import ServerErrorHandler
from alibabacloud.handlers.signer_handler import SignerHandler
from alibabacloud.handlers.timeout_config_reader import TimeoutConfigReader
from alibabacloud.request import APIRequest
from alibabacloud.vendored.requests import Response
from mock import patch

from alibabacloud.clients.ecs_20140526 import EcsClient
from alibabacloud.clients.rds_20140815 import RdsClient
from alibabacloud.clients.ram_20150501 import RamClient
from alibabacloud.clients.slb_20140515 import SlbClient
from alibabacloud.clients.vpc_20160428 import VpcClient
from alibabacloud.clients.cdn_20141111 import CdnClient as cdn_old
from alibabacloud.clients.cdn_20180510 import CdnClient as cdn_new

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


class APIRequestTest(TestCase):

    def _init_client_config(self):
        self.access_key_id = os.environ.get("ACCESS_KEY_ID")
        self.access_key_secret = os.environ.get("ACCESS_KEY_SECRET")
        self.region_id = os.environ.get("REGION_ID")
        client_config = ClientConfig(access_key_id=self.access_key_id,
                                          access_key_secret=self.access_key_secret,
                                          region_id="cn-hangzhou")
        return client_config

    def test_request_with_ecs(self):
        client_config = self._init_client_config()
        ecs_client = EcsClient(client_config)
        delete_version = ["1.0.1", ]

        try:
            context = ecs_client.delete_launch_template_version(delete_version=delete_version)
            assert False
        except ServerException as e:
            self.assertEqual(e.http_status, 400)
            self.assertEqual(e.error_code, "InvalidParameter")
            self.assertEqual(e.error_message, 'The specified parameter "DeleteVersion.1" is not valid.')

    def test_request_with_rds(self):
        client_config = self._init_client_config()
        client = RdsClient(client_config)
        result = client.describe_db_instances()
        self.assertTrue(result.get("Items"))

    def test_request_with_cdn(self):
        client_config = self._init_client_config()
        client = cdn_old(client_config)
        response = client.describe_cdn_types()
        self.assertTrue(response.get("CdnTypes"))

    def test_request_with_cdn_new(self):
        client_config = self._init_client_config()
        client = cdn_new(client_config)
        result = client.describe_cdn_certificate_detail(cert_name="sdk-test")
        self.assertTrue(result.get("RequestId"))

    def test_request_with_slb(self):
        client_config = self._init_client_config()

        client = SlbClient(client_config)
        result = client.describe_access_control_lists()
        self.assertTrue(result.get("Acls"))

    def test_request_with_ram(self):
        client_config = self._init_client_config()

        client = RamClient(client_config)
        response = client.list_access_keys()
        self.assertTrue(response.get("AccessKeys"))

    def test_request_with_vpc(self):
        client_config = self._init_client_config()

        client = VpcClient(client_config)
        result = client.describe_access_points()
        self.assertTrue(result.get("AccessPointSet"))

    def test_request_with_listkeys(self):
        client_config = self._init_client_config()

        client = AlibabaCloudClient(client_config, None)
        client.product_code = "Kms"
        client.api_version = "2016-01-20"
        client.location_service_code = 'kms'
        client.location_endpoint_type = "openAPI"
        api_request = APIRequest('ListKeys', 'GET', 'https', 'RPC')
        context = client._handle_request(api_request)
        response = context.result
        self.assertTrue(response.get("PageNumber"))

    def test_request_with_body_unicode(self):

        def _handle_request(context):
            context.retry_flag = False
            context.http_response = Response()
            context.http_response.status_code = 400
            context.http_response.headers = {}
            context.http_response._content = test_unicode

        client_config = self._init_client_config()

        client = EcsClient(client_config, None)

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
                    self.assertEqual(e.error_message, 'ServerResponseBody: '+test_unicode)
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

        client_config = self._init_client_config()
        client = EcsClient(client_config, None)

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
