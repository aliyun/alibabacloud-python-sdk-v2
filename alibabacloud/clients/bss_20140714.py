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


class BssClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Bss'
        self.api_version = '2014-07-14'
        self.location_service_code = 'bss'
        self.location_endpoint_type = 'openAPI'

    def open_callback(self, param_str=None):
        api_request = APIRequest('OpenCallback', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"paramStr": param_str}
        return self._handle_request(api_request).result

    def query_for_css_order(self, param_str=None):
        api_request = APIRequest('QueryForCssOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"paramStr": param_str}
        return self._handle_request(api_request).result

    def create_order(self, param_str=None):
        api_request = APIRequest('CreateOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"paramStr": param_str}
        return self._handle_request(api_request).result

    def vno_pay_call_back_notify(self, param_str=None):
        api_request = APIRequest('VnoPayCallBackNotify', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"paramStr": param_str}
        return self._handle_request(api_request).result

    def vno_batch_refund_order(self, param_str=None):
        api_request = APIRequest('VnoBatchRefundOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"paramStr": param_str}
        return self._handle_request(api_request).result

    def subscription_create_order_api(self, product_code=None, owner_id=None):
        api_request = APIRequest('SubscriptionCreateOrderApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"productCode": product_code, "ownerId": owner_id}
        return self._handle_request(api_request).result

    def set_resource_business_status(
            self,
            business_status=None,
            resource_owner_id=None,
            resource_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('SetResourceBusinessStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BusinessStatus": business_status,
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        return self._handle_request(api_request).result

    def describe_coupon_list(
            self,
            start_delivery_time=None,
            page_size=None,
            end_delivery_time=None,
            page_num=None,
            status=None):
        api_request = APIRequest('DescribeCouponList', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "StartDeliveryTime": start_delivery_time,
            "PageSize": page_size,
            "EndDeliveryTime": end_delivery_time,
            "PageNum": page_num,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_coupon_detail(self, coupon_number=None):
        api_request = APIRequest('DescribeCouponDetail', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"CouponNumber": coupon_number}
        return self._handle_request(api_request).result

    def describe_cash_detail(self,):
        api_request = APIRequest('DescribeCashDetail', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result
