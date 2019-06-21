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

from alibabacloud.clients.ecs_20140526 import EcsClient
from base import SDKTestBase


class AlibabaCloudTest(SDKTestBase):

    def test_config_enable_default(self):
        config = self.client_config
        self.assertEqual(config.enable_https, True)
        self.assertEqual(config.enable_retry, True)
        self.assertEqual(config.enable_http_debug, False)
        client = EcsClient(config, self.init_credentials_provider())
        self.assertEqual(client.config.enable_https, True)
        self.assertEqual(client.config.enable_retry, True)
        self.assertEqual(client.config.enable_http_debug, False)

    def test_config_enable_custom(self):
        config = self.client_config
        config.enable_http_debug = True
        config.enable_https = False
        config.enable_retry = False
        client = EcsClient(config, self.init_credentials_provider())
        self.assertEqual(client.config.enable_https, False)
        self.assertEqual(client.config.enable_retry, False)
        self.assertEqual(client.config.enable_http_debug, True)

    def test_config_from_env(self):
        config = self.client_config
        os.environ.setdefault('HTTPS_PROXY', 'https://alibabacloud-sdk.com')
        os.environ.setdefault('HTTP_PROXY', 'http://alibabacloud-sdk.com')
        os.environ.setdefault('DEBUG', 'sdk')

        client = EcsClient(config, self.init_credentials_provider())
        self.assertEqual(client.config.enable_http_debug, False)
        os.environ.pop('HTTPS_PROXY')
        os.environ.pop('HTTP_PROXY')
        os.environ.pop('DEBUG')
