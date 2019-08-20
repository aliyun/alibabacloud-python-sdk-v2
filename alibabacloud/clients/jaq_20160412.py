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


class JaqClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'jaq'
        self.api_version = '2016-04-12'
        self.location_service_code = 'jaq'
        self.location_endpoint_type = 'openAPI'

    def scan_vuln(self, ext_param=None, app_info=None):
        api_request = APIRequest('ScanVuln', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ExtParam": ext_param, "AppInfo": app_info}
        return self._handle_request(api_request).result

    def scan_malware(self, ext_param=None, app_info=None):
        api_request = APIRequest('ScanMalware', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ExtParam": ext_param, "AppInfo": app_info}
        return self._handle_request(api_request).result

    def scan_fake(self, ext_param=None, app_info=None):
        api_request = APIRequest('ScanFake', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ExtParam": ext_param, "AppInfo": app_info}
        return self._handle_request(api_request).result

    def get_risk_summary(self, item_id=None):
        api_request = APIRequest('GetRiskSummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ItemId": item_id}
        return self._handle_request(api_request).result

    def get_risk_detail4_batch(self, item_id=None, country=None, language=None):
        api_request = APIRequest('GetRiskDetail4Batch', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ItemId": item_id, "Country": country, "Language": language}
        return self._handle_request(api_request).result

    def get_risk_detail(self, item_id=None, country=None, language=None):
        api_request = APIRequest('GetRiskDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ItemId": item_id, "Country": country, "Language": language}
        return self._handle_request(api_request).result

    def diy_shield(self, channel=None, app_info=None, enhance=None):
        api_request = APIRequest('DiyShield', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Channel": channel, "AppInfo": app_info, "Enhance": enhance}
        return self._handle_request(api_request).result

    def batch_scan_plugin(self, app_info_batch=None):
        api_request = APIRequest('BatchScanPlugin', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AppInfoBatch": app_info_batch}
        return self._handle_request(api_request).result

    def batch_scan_malware(self, app_info_batch=None):
        api_request = APIRequest('BatchScanMalware', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AppInfoBatch": app_info_batch}
        return self._handle_request(api_request).result

    def shield(self, channel=None, app_info=None):
        api_request = APIRequest('Shield', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Channel": channel, "AppInfo": app_info}
        return self._handle_request(api_request).result

    def get_shield_result(self, item_id=None):
        api_request = APIRequest('GetShieldResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ItemId": item_id}
        return self._handle_request(api_request).result
