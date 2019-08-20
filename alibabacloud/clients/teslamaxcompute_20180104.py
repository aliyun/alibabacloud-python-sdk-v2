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


class TeslaMaxComputeClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'TeslaMaxCompute'
        self.api_version = '2018-01-04'
        self.location_service_code = 'teslamaxcompute'
        self.location_endpoint_type = 'openAPI'

    def query_customer_sale_info(self, region_name=None):
        api_request = APIRequest('QueryCustomerSaleInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionName": region_name}
        return self._handle_request(api_request).result

    def get_cluster_instance(
            self,
            cluster=None,
            page_size=None,
            page_num=None,
            region=None,
            status=None):
        api_request = APIRequest('GetClusterInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Cluster": cluster,
            "PageSize": page_size,
            "PageNum": page_num,
            "Region": region,
            "Status": status}
        return self._handle_request(api_request).result

    def get_instances_status_count(self, cluster=None, quota_id=None, region=None, quota_name=None):
        api_request = APIRequest('GetInstancesStatusCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Cluster": cluster,
            "QuotaId": quota_id,
            "Region": region,
            "QuotaName": quota_name}
        return self._handle_request(api_request).result

    def get_project_instance(
            self,
            page_size=None,
            project=None,
            page_num=None,
            region=None,
            status=None):
        api_request = APIRequest('GetProjectInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "Project": project,
            "PageNum": page_num,
            "Region": region,
            "Status": status}
        return self._handle_request(api_request).result

    def get_quota_history_info(
            self,
            cluster=None,
            end_time=None,
            start_time=None,
            region=None,
            quota_name=None):
        api_request = APIRequest('GetQuotaHistoryInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Cluster": cluster,
            "EndTime": end_time,
            "StartTime": start_time,
            "Region": region,
            "QuotaName": quota_name}
        return self._handle_request(api_request).result

    def get_quota_instance(
            self,
            cluster=None,
            page_size=None,
            quota_id=None,
            page_num=None,
            region=None,
            quota_name=None,
            status=None):
        api_request = APIRequest('GetQuotaInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Cluster": cluster,
            "PageSize": page_size,
            "QuotaId": quota_id,
            "PageNum": page_num,
            "Region": region,
            "QuotaName": quota_name,
            "Status": status}
        return self._handle_request(api_request).result

    def get_user_instance(self, page_size=None, page_num=None, region=None, user=None, status=None):
        api_request = APIRequest('GetUserInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "PageNum": page_num,
            "Region": region,
            "User": user,
            "Status": status}
        return self._handle_request(api_request).result
