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
import shutil
import tempfile
import time

from mock import patch

from alibabacloud import get_client
from alibabacloud.exceptions import HttpErrorException
from alibabacloud.request import APIRequest
from base import SDKTestBase


class ConfigFileTest(SDKTestBase):

    def setUp(self):
        super(ConfigFileTest, self).setUp()
        self.tempdir = tempfile.mkdtemp()
        self.credentials_file = os.path.join(self.tempdir, 'config.ini')
        os.environ['ALIBABA_CLOUD_CONFIG_FILE'] = self.credentials_file

    def tearDown(self):
        shutil.rmtree(self.tempdir)
        if os.environ.get('ALIBABA_CLOUD_CONFIG_FILE') is not None:
            os.environ.pop('ALIBABA_CLOUD_CONFIG_FILE')

    def write_config(self, credential):
        with open(self.credentials_file, 'w') as f:
            f.write(credential)

    def test_client_file(self):
        config_file = (
            '[default]\n'
            'region_id = us-west-1\n'
            'endpoint = somewhere.you.will.never.get\n'
            'max_retry_times = 2\n'
            'http_port = 8080\n'
            'https_port = 8081\n'
            'connection_timeout = 2\n'
            'read_timeout = 5\n'
        )
        self.write_config(config_file)
        client = get_client('ecs', access_key_id=self.access_key_id,
                            access_key_secret=self.access_key_secret,
                            region_id='hangzhou', endpoint='123')
        self.assertEqual(client.config.region_id, 'hangzhou')
        self.assertEqual(client.config.endpoint, '123')
        self.assertEqual(client.config.max_retry_times, '2')
        self.assertEqual(client.config.http_port, '8080')
        self.assertEqual(client.config.https_port, '8081')
        self.assertEqual(client.config.connection_timeout, '2')
        self.assertEqual(client.config.read_timeout, '5')
        os.environ.pop('ALIBABA_CLOUD_CONFIG_FILE')

    def test_file_region_id(self):
        config_file = (
            '[default]\n'
            'region_id = us-west-1\n'
            'endpoint = somewhere.you.will.never.get\n'
        )
        self.write_config(config_file)
        client = get_client('ecs', access_key_id=self.access_key_id,
                            access_key_secret=self.access_key_secret)
        self.assertEqual(client.config.region_id, 'us-west-1')
        self.assertEqual(client.config.endpoint, 'somewhere.you.will.never.get')
        self.assertEqual(client.config.max_retry_times, 3)
        self.assertEqual(client.config.http_port, 80)
        self.assertEqual(client.config.https_port, 443)
        self.assertEqual(client.config.connection_timeout, None)
        self.assertEqual(client.config.read_timeout, None)
        os.environ.pop('ALIBABA_CLOUD_CONFIG_FILE')

    def test_file_retry(self):

        config_file = (
            '[default]\n'
            'max_retry_times = 2\n'
            'endpoint = somewhere.you.will.never.get\n'
            'region_id = us-west-1\n'
        )
        self.write_config(config_file)

        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC')
        client = get_client('ecs', credentials_provider=self.init_credentials_provider())
        globals()["_test_compute_delay"] = []

        def record_sleep(delay):
            global _test_compute_delay
            _test_compute_delay.append(delay)

        from alibabacloud.handlers.api_protocol_handler import APIProtocolHandler
        from alibabacloud.handlers.credentials_handler import CredentialsHandler
        from alibabacloud.handlers.signer_handler import SignerHandler
        from alibabacloud.handlers.timeout_config_reader import TimeoutConfigReader
        from alibabacloud.handlers.endpoint_handler import EndpointHandler
        from alibabacloud.handlers.retry_handler import RetryHandler
        from alibabacloud.handlers.server_error_handler import ServerErrorHandler
        from alibabacloud.handlers.http_handler import HttpHandler
        DEFAULT_HANDLERS = [
            RetryHandler(),
            APIProtocolHandler(),
            CredentialsHandler(),
            SignerHandler(),
            TimeoutConfigReader(),
            EndpointHandler(),
            ServerErrorHandler(),
            HttpHandler(),
        ]

        client.handlers = DEFAULT_HANDLERS

        with patch.object(time, "sleep", wraps=record_sleep) as monkey:
            try:
                client._handle_request(api_request)
                assert False
            except HttpErrorException as e:
                self.assertTrue("Max retries exceeded with url" in e.error_message)
        self.assertEqual(2, monkey.call_count)
        self.assertEqual(2, len(_test_compute_delay))

        os.environ.pop('ALIBABA_CLOUD_CONFIG_FILE')
