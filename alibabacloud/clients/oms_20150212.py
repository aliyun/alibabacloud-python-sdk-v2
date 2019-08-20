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


class OmsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Oms'
        self.api_version = '2015-02-12'
        self.location_service_code = 'oms'
        self.location_endpoint_type = 'openAPI'

    def get_data_open_config(
            self,
            data_type=None,
            product_name=None,
            table_name=None,
            site_bid=None):
        api_request = APIRequest('GetDataOpenConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataType": data_type,
            "ProductName": product_name,
            "TableName": table_name,
            "SiteBid": site_bid}
        return self._handle_request(api_request).result

    def get_product_define(self, data_type=None, product_name=None, site_bid=None):
        api_request = APIRequest('GetProductDefine', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataType": data_type,
            "ProductName": product_name,
            "siteBid": site_bid}
        return self._handle_request(api_request).result

    def get_user_data(
            self,
            data_type=None,
            next_token=None,
            owner_account=None,
            product_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            table_name=None,
            max_result=None):
        api_request = APIRequest('GetUserData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataType": data_type,
            "NextToken": next_token,
            "OwnerAccount": owner_account,
            "ProductName": product_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "TableName": table_name,
            "MaxResult": max_result}
        return self._handle_request(api_request).result
