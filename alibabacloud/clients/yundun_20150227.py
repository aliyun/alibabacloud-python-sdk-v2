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


class YundunClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Yundun'
        self.api_version = '2015-02-27'
        self.location_service_code = 'yundun'
        self.location_endpoint_type = 'openAPI'

    def web_attack_num(self,):
        api_request = APIRequest('WebAttackNum', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def todayqps_by_region(self,):
        api_request = APIRequest('TodayqpsByRegion', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def today_malware_num(self,):
        api_request = APIRequest('TodayMalwareNum', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def today_crack_intercept(self,):
        api_request = APIRequest('TodayCrackIntercept', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def today_backdoor(self,):
        api_request = APIRequest('TodayBackdoor', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def today_allpps(self,):
        api_request = APIRequest('TodayAllpps', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def today_allkbps(self,):
        api_request = APIRequest('TodayAllkbps', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def today_aegis_online_rate(self,):
        api_request = APIRequest('TodayAegisOnlineRate', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def current_ddos_attack_num(self,):
        api_request = APIRequest('CurrentDdosAttackNum', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def all_malware_num(self,):
        api_request = APIRequest('AllMalwareNum', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result
