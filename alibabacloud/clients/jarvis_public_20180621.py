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


class JarvispublicClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'jarvis-public'
        self.api_version = '2018-06-21'
        self.location_service_code = 'jarvis-public'
        self.location_endpoint_type = 'openAPI'

    def describe_count_attack_event(
            self,
            source_ip=None,
            server_ip_list=None,
            page_size=None,
            end_time=None,
            current_page=None,
            start_time=None,
            lang=None,
            region=None,
            product_type=None):
        api_request = APIRequest('DescribeCountAttackEvent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ServerIpList": server_ip_list,
            "PageSize": page_size,
            "EndTime": end_time,
            "CurrentPage": current_page,
            "StartTime": start_time,
            "Lang": lang,
            "Region": region,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def describe_attack_event(
            self,
            source_ip=None,
            server_ip_list=None,
            page_size=None,
            end_time=None,
            current_page=None,
            start_time=None,
            lang=None,
            region=None,
            product_type=None):
        api_request = APIRequest('DescribeAttackEvent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ServerIpList": server_ip_list,
            "PageSize": page_size,
            "EndTime": end_time,
            "CurrentPage": current_page,
            "StartTime": start_time,
            "Lang": lang,
            "Region": region,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def describe_attacked_ip(
            self,
            source_ip=None,
            server_ip_list=None,
            page_size=None,
            end_time=None,
            current_page=None,
            start_time=None,
            lang=None,
            region=None,
            product_type=None):
        api_request = APIRequest('DescribeAttackedIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ServerIpList": server_ip_list,
            "PageSize": page_size,
            "EndTime": end_time,
            "CurrentPage": current_page,
            "StartTime": start_time,
            "Lang": lang,
            "Region": region,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def describe_phone_info(self, source_ip=None, phone_num=None, lang=None, source_code=None):
        api_request = APIRequest('DescribePhoneInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "phoneNum": phone_num,
            "Lang": lang,
            "sourceCode": source_code}
        return self._handle_request(api_request).result
