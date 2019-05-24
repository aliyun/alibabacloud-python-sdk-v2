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


class openanalyticsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None):
        AlibabaCloudClient.__init__(self, client_config, credentials_provider)
        self.product_code = 'openanalytics'
        self.product_version = '2018-03-01'
        self.location_service_code = 'openanalytics'
        self.location_endpoint_type = 'openAPI'

    def get_product_status(
        self,
        product_code=None,
        product_access_key=None,
        target_uid=None,
        target_arn_role=None,
    ):
        api_request = APIRequest(
            'GetProductStatus', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "ProductCode": product_code,
            "ProductAccessKey": product_access_key,
            "TargetUid": target_uid,
            "TargetArnRole": target_arn_role,
        }
        return self._handle_request(api_request).result

    def close_product_account(
        self,
        product_code=None,
        product_access_key=None,
        target_uid=None,
        target_arn_role=None,
    ):
        api_request = APIRequest(
            'CloseProductAccount',
            'GET',
            'http',
            'RPC',
            'body')
        api_request._params = {
            "ProductCode": product_code,
            "ProductAccessKey": product_access_key,
            "TargetUid": target_uid,
            "TargetArnRole": target_arn_role,
        }
        return self._handle_request(api_request).result

    def get_region_status(self, target_uid=None,):
        api_request = APIRequest(
            'GetRegionStatus', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"TargetUid": target_uid, }
        return self._handle_request(api_request).result

    def open_product_account(
        self,
        product_code=None,
        product_access_key=None,
        target_uid=None,
        target_arn_role=None,
    ):
        api_request = APIRequest(
            'OpenProductAccount',
            'GET',
            'http',
            'RPC',
            'body')
        api_request._params = {
            "ProductCode": product_code,
            "ProductAccessKey": product_access_key,
            "TargetUid": target_uid,
            "TargetArnRole": target_arn_role,
        }
        return self._handle_request(api_request).result

    def get_allow_ip(self, user_id=None, network_type=None,):
        api_request = APIRequest('GetAllowIP', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "UserID": user_id, "NetworkType": network_type, }
        return self._handle_request(api_request).result

    def describe_region_list(self,):
        api_request = APIRequest(
            'DescribeRegionList', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def get_end_point_by_domain(self, user_id=None, domain_url=None,):
        api_request = APIRequest(
            'GetEndPointByDomain',
            'GET',
            'http',
            'RPC',
            'body')
        api_request._params = {"UserID": user_id, "DomainURL": domain_url, }
        return self._handle_request(api_request).result

    def query_end_point_list(self, user_id=None,):
        api_request = APIRequest(
            'QueryEndPointList', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"UserID": user_id, }
        return self._handle_request(api_request).result

    def set_allow_ip(
        self,
        user_id=None,
        network_type=None,
        allow_ip=None,
        append=None,
    ):
        api_request = APIRequest('SetAllowIP', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "UserID": user_id,
            "NetworkType": network_type,
            "AllowIP": allow_ip,
            "Append": append,
        }
        return self._handle_request(api_request).result
