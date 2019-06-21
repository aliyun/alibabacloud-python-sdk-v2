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

import logging
import os
import tempfile

import mock

from alibabacloud.clients.ecs_20140526 import EcsClient
from base import SDKTestBase


class AlibabaLoggerTest(SDKTestBase):

    def test_no_retry(self):
        client = EcsClient(self.client_config, self.init_credentials_provider())
        tempdir = tempfile.mkdtemp()

        temp_file = os.path.join(tempdir, 'file_logger')

        client.add_rotating_file_log_handler(log_level=logging.DEBUG, path=temp_file)
        context = client.describe_instances()
        self.assertTrue(os.path.isfile(temp_file))
        with open(temp_file) as logfile:
            s = logfile.read()
        self.assertTrue('alibabacloud-' in s)
        self.assertTrue('DEBUG' in s)

    @mock.patch('logging.getLogger')
    @mock.patch('logging.Formatter')
    def test_stream_logger(self, formatter, get_logger):
        client = EcsClient(self.client_config, self.init_credentials_provider())
        client.add_stream_log_handler(logger_name='foo.bar', log_level=40, format_string='foo')
        get_logger.assert_called_with('foo.bar')
        get_logger.return_value.setLevel.assert_called_with(logging.ERROR)
        formatter.assert_called_with('foo')
