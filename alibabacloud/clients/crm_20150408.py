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


class CrmClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Crm'
        self.api_version = '2015-04-08'
        self.location_service_code = 'crm'
        self.location_endpoint_type = 'openAPI'

    def delete_label_for_bid(self, label_series=None, pk=None, label=None):
        api_request = APIRequest('DeleteLabelForBid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"LabelSeries": label_series, "PK": pk, "Label": label}
        return self._handle_request(api_request).result

    def check_label_for_bid(self, label_series=None, pk=None, label=None):
        api_request = APIRequest('CheckLabelForBid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"LabelSeries": label_series, "PK": pk, "Label": label}
        return self._handle_request(api_request).result

    def add_label_for_bid(self, label_series=None, end_time=None, pk=None, label=None):
        api_request = APIRequest('AddLabelForBid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LabelSeries": label_series,
            "EndTime": end_time,
            "PK": pk,
            "Label": label}
        return self._handle_request(api_request).result

    def get_aliyun_pk_by_aliyun_id(self, aliyun_id=None):
        api_request = APIRequest('GetAliyunPkByAliyunId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AliyunId": aliyun_id}
        return self._handle_request(api_request).result

    def batch_get_aliyun_id_by_aliyun_pk(self, list_of_pk_list=None):
        api_request = APIRequest('BatchGetAliyunIdByAliyunPk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PkList": list_of_pk_list}
        repeat_info = {"PkList": ('PkList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def remove_identity_certified_for_bid_user(self, bid_type=None, pk=None):
        api_request = APIRequest('RemoveIdentityCertifiedForBidUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BidType": bid_type, "PK": pk}
        return self._handle_request(api_request).result

    def query_bid_user_certified_info(self, bid_type=None, pk=None):
        api_request = APIRequest('QueryBidUserCertifiedInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BidType": bid_type, "PK": pk}
        return self._handle_request(api_request).result

    def add_identity_certified_for_bid_user(
            self,
            bid_type=None,
            license_number=None,
            license_type=None,
            phone=None,
            name=None,
            pk=None,
            is_enterprise=None):
        api_request = APIRequest('AddIdentityCertifiedForBidUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BidType": bid_type,
            "LicenseNumber": license_number,
            "LicenseType": license_type,
            "Phone": phone,
            "Name": name,
            "PK": pk,
            "IsEnterprise": is_enterprise}
        return self._handle_request(api_request).result

    def delete_label(
            self,
            label_series=None,
            organization=None,
            pk=None,
            label_name=None,
            user_name=None):
        api_request = APIRequest('DeleteLabel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LabelSeries": label_series,
            "Organization": organization,
            "PK": pk,
            "LabelName": label_name,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def check_label(self, label_series=None, pk=None, label_name=None):
        api_request = APIRequest('CheckLabel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"LabelSeries": label_series, "PK": pk, "LabelName": label_name}
        return self._handle_request(api_request).result

    def add_label(
            self,
            label_series=None,
            organization=None,
            end_time=None,
            pk=None,
            label_name=None,
            user_name=None):
        api_request = APIRequest('AddLabel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LabelSeries": label_series,
            "Organization": organization,
            "EndTime": end_time,
            "PK": pk,
            "LabelName": label_name,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def query_customer_label(self, label_series=None):
        api_request = APIRequest('QueryCustomerLabel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"LabelSeries": label_series}
        return self._handle_request(api_request).result
