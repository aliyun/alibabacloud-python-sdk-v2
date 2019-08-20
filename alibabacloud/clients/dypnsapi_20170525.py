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


class DypnsapiClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Dypnsapi'
        self.api_version = '2017-05-25'
        self.location_service_code = 'dypnsapi'
        self.location_endpoint_type = 'openAPI'

    def get_mobile(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            access_token=None,
            out_id=None,
            owner_id=None):
        api_request = APIRequest('GetMobile', 'POST', 'https', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "AccessToken": access_token,
            "OutId": out_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_verify_scheme(
            self,
            resource_owner_id=None,
            pack_name=None,
            app_name=None,
            resource_owner_account=None,
            scheme_name=None,
            bundle_id=None,
            os_type=None,
            owner_id=None,
            pack_sign=None):
        api_request = APIRequest('CreateVerifyScheme', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PackName": pack_name,
            "AppName": app_name,
            "ResourceOwnerAccount": resource_owner_account,
            "SchemeName": scheme_name,
            "BundleId": bundle_id,
            "OsType": os_type,
            "OwnerId": owner_id,
            "PackSign": pack_sign}
        return self._handle_request(api_request).result

    def verify_mobile(
            self,
            resource_owner_id=None,
            access_code=None,
            resource_owner_account=None,
            phone_number=None,
            out_id=None,
            owner_id=None):
        api_request = APIRequest('VerifyMobile', 'POST', 'https', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccessCode": access_code,
            "ResourceOwnerAccount": resource_owner_account,
            "PhoneNumber": phone_number,
            "OutId": out_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def twice_tel_verify(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            phone_number=None,
            owner_id=None,
            since=None):
        api_request = APIRequest('TwiceTelVerify', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PhoneNumber": phone_number,
            "OwnerId": owner_id,
            "Since": since}
        return self._handle_request(api_request).result
