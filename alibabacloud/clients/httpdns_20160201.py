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


class HttpdnsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Httpdns'
        self.api_version = '2016-02-01'
        self.location_service_code = 'httpdns'
        self.location_endpoint_type = 'openAPI'

    def get_resolve_count_summary(self, granularity=None, time_span=None):
        api_request = APIRequest('GetResolveCountSummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Granularity": granularity, "TimeSpan": time_span}
        return self._handle_request(api_request).result

    def list_domains(self, page_size=None, page_number=None):
        api_request = APIRequest('ListDomains', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_resolve_statistics(
            self,
            granularity=None,
            protocol_name=None,
            domain_name=None,
            time_span=None):
        api_request = APIRequest('GetResolveStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Granularity": granularity,
            "ProtocolName": protocol_name,
            "DomainName": domain_name,
            "TimeSpan": time_span}
        return self._handle_request(api_request).result

    def get_account_info(self,):
        api_request = APIRequest('GetAccountInfo', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def describe_domains(self, account_id=None, page_size=None, page_number=None):
        api_request = APIRequest('DescribeDomains', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccountId": account_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_domain(self, account_id=None, domain_name=None):
        api_request = APIRequest('DeleteDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AccountId": account_id, "DomainName": domain_name}
        return self._handle_request(api_request).result

    def add_domain(self, account_id=None, domain_name=None):
        api_request = APIRequest('AddDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AccountId": account_id, "DomainName": domain_name}
        return self._handle_request(api_request).result
