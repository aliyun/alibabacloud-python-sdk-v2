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

from alibabacloud.clients.ecs_20140526 import EcsClient
from alibabacloud.exceptions import HttpErrorException
from alibabacloud.request import APIRequest
from base import SDKTestBase


class TimeoutTest(SDKTestBase):

    def test_no_retry(self):
        config = self.client_config
        config.enable_retry = False
        config.endpoint = 'somewhere.you.never'
        client = EcsClient(config, self.init_credentials_provider())

        with patch.object(client, "_handle_request",
                          wraps=client._handle_request) as monkey:
            try:
                context = client.describe_instances()
                assert False
            except HttpErrorException as e:
                self.assertTrue(e.error_message.startswith(
                    "HTTPConnectionPool(host='somewhere.you.never', port=80): "
                    "Max retries exceeded with url: /"))

        self.assertEqual(1, monkey.call_count)

    def test_default_timeout(self):
        config = self.client_config
        config.connection_timeout = None
        config.enable_retry = False
        client = EcsClient(config, self.init_credentials_provider())
        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC')
        context = client._handle_request(api_request, _raise_exception=False)

        self.assertEqual((5, 10), context.http_request.timeout)

    def test_client_customized_timeout(self):
        config = self.client_config
        config.read_timeout = 7
        config.connection_timeout = 8
        client = EcsClient(config, self.init_credentials_provider())
        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC')
        context = client._handle_request(api_request, _raise_exception=False)
        self.assertEqual((8, 7), context.http_request.timeout)

    def test_read_timeout_priority(self):
        # read config
        config = self.client_config
        config.connection_timeout = None
        config.read_timeout = 20
        client = EcsClient(config, self.init_credentials_provider())
        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC')
        context = client._handle_request(api_request, _raise_exception=False)
        self.assertEqual((5, 20), context.http_request.timeout)
        # read file
        config = self.client_config
        config.read_timeout = None
        client = EcsClient(config, self.init_credentials_provider())
        api_request = APIRequest('RunInstances', 'GET', 'http', 'RPC')
        context = client._handle_request(api_request, _raise_exception=False)
        self.assertEqual((5, 86), context.http_request.timeout)

    def test_connect_timeout_priority(self):
        # read config
        config = self.client_config
        config.connection_timeout = "20"
        client = EcsClient(config, self.init_credentials_provider())
        api_request = APIRequest('RunInstances', 'GET', 'http', 'RPC')
        context = client._handle_request(api_request, _raise_exception=False)
        self.assertEqual((20.0, 86), context.http_request.timeout)
        # read file
        config = self.client_config
        config.connection_timeout = None
        client = EcsClient(config, self.init_credentials_provider())
        context = client._handle_request(api_request, _raise_exception=False)
        self.assertEqual((5, 86), context.http_request.timeout)
