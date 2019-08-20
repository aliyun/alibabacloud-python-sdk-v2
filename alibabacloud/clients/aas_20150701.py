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


class AasClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Aas'
        self.api_version = '2015-07-01'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def check_mfa_bind(self,):
        api_request = APIRequest('CheckMfaBind', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def verify_account_login_token(self, login_token=None):
        api_request = APIRequest('VerifyAccountLoginToken', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"LoginToken": login_token}
        return self._handle_request(api_request).result

    def generate_account_login_token(self, target_pk=None):
        api_request = APIRequest('GenerateAccountLoginToken', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TargetPk": target_pk}
        return self._handle_request(api_request).result

    def create_intl_aliyun_account(self, nationality_code=None):
        api_request = APIRequest('CreateIntlAliyunAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"NationalityCode": nationality_code}
        return self._handle_request(api_request).result

    def create_short_term_access_key_for_account(
            self, expire_time=None, is_mfa_present=None, pk=None):
        api_request = APIRequest('CreateShortTermAccessKeyForAccount',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ExpireTime": expire_time, "IsMfaPresent": is_mfa_present, "PK": pk}
        return self._handle_request(api_request).result

    def get_aliyun_account_with_bind_taobao_hid(self, havana_id=None):
        api_request = APIRequest('GetAliyunAccountWithBindTaobaoHid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"HavanaId": havana_id}
        return self._handle_request(api_request).result

    def get_aliyun_account_with_bind_hid(self, inner_account_hid=None):
        api_request = APIRequest('GetAliyunAccountWithBindHid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InnerAccountHid": inner_account_hid}
        return self._handle_request(api_request).result

    def create_aliyun_account_with_bind_hid(self, inner_account_hid=None):
        api_request = APIRequest('CreateAliyunAccountWithBindHid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InnerAccountHid": inner_account_hid}
        return self._handle_request(api_request).result

    def update_status_for_account(self, account_status=None, pk=None):
        api_request = APIRequest('UpdateStatusForAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AccountStatus": account_status, "PK": pk}
        return self._handle_request(api_request).result

    def list_aliyun_account(self, marker=None, max_items=None):
        api_request = APIRequest('ListAliyunAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Marker": marker, "MaxItems": max_items}
        return self._handle_request(api_request).result

    def get_short_term_access_key_for_account(self, expire_time=None, is_mfa_present=None, pk=None):
        api_request = APIRequest('GetShortTermAccessKeyForAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ExpireTime": expire_time, "IsMfaPresent": is_mfa_present, "PK": pk}
        return self._handle_request(api_request).result

    def delete_access_key_for_account(self, ak_id=None, pk=None):
        api_request = APIRequest('DeleteAccessKeyForAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AKId": ak_id, "PK": pk}
        return self._handle_request(api_request).result

    def create_aliyun_account(self, aliyun_id=None):
        api_request = APIRequest('CreateAliyunAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AliyunId": aliyun_id}
        return self._handle_request(api_request).result

    def create_access_key_for_account(self, ak_secret=None, pk=None):
        api_request = APIRequest('CreateAccessKeyForAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AKSecret": ak_secret, "PK": pk}
        return self._handle_request(api_request).result

    def update_password_for_account(self, pk=None, new_password=None):
        api_request = APIRequest('UpdatePasswordForAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PK": pk, "NewPassword": new_password}
        return self._handle_request(api_request).result

    def update_access_key_status_for_account(self, ak_status=None, ak_id=None, pk=None):
        api_request = APIRequest('UpdateAccessKeyStatusForAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AKStatus": ak_status, "AKId": ak_id, "PK": pk}
        return self._handle_request(api_request).result

    def list_access_keys_for_account(self, ak_type=None, ak_status=None, pk=None):
        api_request = APIRequest('ListAccessKeysForAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AKType": ak_type, "AKStatus": ak_status, "PK": pk}
        return self._handle_request(api_request).result

    def get_basic_info_for_account(self, aliyun_id=None):
        api_request = APIRequest('GetBasicInfoForAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AliyunId": aliyun_id}
        return self._handle_request(api_request).result
