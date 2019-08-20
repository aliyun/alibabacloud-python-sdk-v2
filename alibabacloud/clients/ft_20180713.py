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

from alibabacloud.client import AlibabaCloudClient
from alibabacloud.request import APIRequest
from alibabacloud.utils.parameter_validation import verify_params


class FtClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Ft'
        self.api_version = '2018-07-13'
        self.location_service_code = 'ft'
        self.location_endpoint_type = 'openAPI'

    def batch_audit_test01(self, name=None, batch_audit_test01=None):
        api_request = APIRequest('BatchAuditTest01', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name, "BatchAuditTest01": batch_audit_test01}
        return self._handle_request(api_request).result

    def ft_ip_flow_control(self, name=None):
        api_request = APIRequest('FtIpFlowControl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name}
        return self._handle_request(api_request).result

    def ft_dynamic_address_dubbo(self, int_value=None, string_value=None):
        api_request = APIRequest('FtDynamicAddressDubbo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"IntValue": int_value, "StringValue": string_value}
        return self._handle_request(api_request).result

    def ft_dynamic_address_hsf(self,):
        api_request = APIRequest('FtDynamicAddressHsf', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def ft_flow_special(self, name=None):
        api_request = APIRequest('FtFlowSpecial', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name}
        return self._handle_request(api_request).result

    def ft_api_alias_api(self, name=None):
        api_request = APIRequest('FTApiAliasApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name}
        return self._handle_request(api_request).result

    def ft_eagle_eye(self, name=None):
        api_request = APIRequest('FtEagleEye', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name}
        return self._handle_request(api_request).result

    def ft_param_list(self, list_of_disk=None, name=None):
        api_request = APIRequest('FtParamList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Disk": list_of_disk, "Name": name}
        repeat_info = {"Disk": ('Disk', 'list', 'dict', [('Size', 'list', 'str', None),
                                                         ('Type', 'list', 'str', None),
                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def ft_gated_launch_policy4(self, is_gated_launch=None):
        api_request = APIRequest('FtGatedLaunchPolicy4', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"IsGatedLaunch": is_gated_launch}
        return self._handle_request(api_request).result
