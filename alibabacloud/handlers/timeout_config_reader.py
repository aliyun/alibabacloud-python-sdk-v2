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

import jmespath

from alibabacloud.exceptions import ClientException, ParamTypeInvalidException
from alibabacloud.handlers import RequestHandler
from alibabacloud.utils import load_json_from_data_dir

DEFAULT_READ_TIMEOUT = 10
DEFAULT_CONNECTION_TIMEOUT = 5
_api_timeout_config_data = load_json_from_data_dir._load_json_from_data_dir("timeout_config.json")


class TimeoutConfigReader(RequestHandler):
    def handle_request(self, context):
        context.http_request.timeout = (self._connection_timeout(context.config.connection_timeout),
                                        self._read_timeout(context))

    @staticmethod
    def _valid_timeout_value(timeout, name):
        if isinstance(timeout, int) or isinstance(timeout, float):
            if timeout > 0:
                return timeout
            raise ParamTypeInvalidException(param=name, param_type='positive integer')
        elif isinstance(timeout, str) and timeout.isdigit():
            if float(timeout) > 0:
                return float(timeout)
            raise ParamTypeInvalidException(param=name, param_type='positive integer')
        raise ParamTypeInvalidException(param=name, param_type='float or int or str')

    def _connection_timeout(self, connection_timeout):
        connection_timeout = self._valid_timeout_value(connection_timeout, 'connection_timeout') \
            if connection_timeout else None

        return connection_timeout or DEFAULT_CONNECTION_TIMEOUT

    def _read_timeout(self, context):
        read_timeout = self._valid_timeout_value(context.config.read_timeout, 'read_timeout') \
            if context.config.read_timeout else None
        file_read_timeout = None
        product_code = context.client.product_code
        api_version = context.client.api_version
        action_name = context.api_request.action_name
        if product_code is not None and api_version is not None \
                and action_name is not None:
            path = '"{0}"."{1}"."{2}"'.format(product_code.lower(), api_version,
                                              action_name)
            file_read_timeout = jmespath.search(path, _api_timeout_config_data)
        return read_timeout or file_read_timeout or DEFAULT_READ_TIMEOUT
