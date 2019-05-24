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

from alibabacloud.client import ClientConfig
from base import TestCase
from alibabacloud.clients.ecs_20140526 import EcsClient


class AlibabaCloudTest(TestCase):

    def _prepare_config_var(self):
        self.access_key_id = os.environ.get("ACCESS_KEY_ID")
        self.access_key_secret = os.environ.get("ACCESS_KEY_SECRET")
        self.region_id = os.environ.get("REGION_ID")
        client_config = ClientConfig(access_key_id=self.access_key_id,
                                          access_key_secret=self.access_key_secret,
                                          region_id="cn-hangzhou")
        return client_config

    def test_config_enable_default(self):
        config = self._prepare_config_var()
        self.assertEqual(config.enable_https, None)
        self.assertEqual(config.enable_retry, None)
        self.assertEqual(config.enable_http_debug, None)
        self.assertEqual(config.enable_stream_logger, None)
        client = EcsClient(config)
        self.assertEqual(client.config.enable_https, True)
        self.assertEqual(client.config.enable_retry, True)
        self.assertEqual(client.config.enable_http_debug, False)
        self.assertEqual(client.config.enable_stream_logger, None)

    def test_config_enable_custom(self):
        config = self._prepare_config_var()
        config.enable_http_debug = True
        config.enable_stream_logger = False
        config.enable_https = False
        config.enable_retry = False
        client = EcsClient(config)
        self.assertEqual(client.config.enable_https, False)
        self.assertEqual(client.config.enable_retry, False)
        self.assertEqual(client.config.enable_http_debug, True)
        self.assertEqual(client.config.enable_stream_logger, False)

    def test_config_from_env(self):
        config = self._prepare_config_var()
        os.environ.setdefault('HTTPS_PROXY', 'https://alibabacloud-sdk.com')
        os.environ.setdefault('HTTP_PROXY', 'http://alibabacloud-sdk.com')
        os.environ.setdefault('DEBUG', 'sdk')

        client = EcsClient(config)
        self.assertEqual(client.config.enable_http_debug, True)
        os.environ.pop('HTTPS_PROXY')
        os.environ.pop('HTTP_PROXY')
        os.environ.pop('DEBUG')
