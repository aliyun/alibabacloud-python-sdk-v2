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


class SasapiClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Sas-api'
        self.api_version = '2017-07-05'
        self.location_service_code = 'sas-api'
        self.location_endpoint_type = 'openAPI'

    def describe_total_and_rate_line(self, source_ip=None, api_type=None):
        api_request = APIRequest('DescribeTotalAndRateLine', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "ApiType": api_type}
        return self._handle_request(api_request).result

    def describe_threat_type_lines(self, source_ip=None, api_type=None):
        api_request = APIRequest('DescribeThreatTypeLines', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "ApiType": api_type}
        return self._handle_request(api_request).result

    def describe_per_date_data(self, source_ip=None, api_type=None):
        api_request = APIRequest('DescribePerDateData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "ApiType": api_type}
        return self._handle_request(api_request).result

    def describe_account_profile_by_key(self, source_ip=None, keyword=None):
        api_request = APIRequest('DescribeAccountProfileByKey', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Keyword": keyword}
        return self._handle_request(api_request).result

    def describe_threat_distribute(
            self,
            end_date=None,
            source_ip=None,
            hit_day=None,
            start_date=None,
            api_type=None):
        api_request = APIRequest('DescribeThreatDistribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndDate": end_date,
            "SourceIp": source_ip,
            "HitDay": hit_day,
            "StartDate": start_date,
            "ApiType": api_type}
        return self._handle_request(api_request).result

    def describe_hit_rate_pie(
            self,
            end_date=None,
            source_ip=None,
            start_date=None,
            hit_day=None,
            api_type=None):
        api_request = APIRequest('DescribeHitRatePie', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndDate": end_date,
            "SourceIp": source_ip,
            "StartDate": start_date,
            "HitDay": hit_day,
            "ApiType": api_type}
        return self._handle_request(api_request).result

    def describe_hit_rate_column(
            self,
            end_date=None,
            source_ip=None,
            hit_day=None,
            start_date=None,
            api_type=None):
        api_request = APIRequest('DescribeHitRateColumn', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndDate": end_date,
            "SourceIp": source_ip,
            "HitDay": hit_day,
            "StartDate": start_date,
            "ApiType": api_type}
        return self._handle_request(api_request).result

    def describe_account_profile_by_key_word(self, source_ip=None, keyword=None):
        api_request = APIRequest('DescribeAccountProfileByKeyWord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Keyword": keyword}
        return self._handle_request(api_request).result

    def get_account_profile(
            self,
            device_id_md5=None,
            carrier=None,
            os=None,
            phone=None,
            request_url=None,
            ip=None,
            user_agent=None,
            connection_type=None,
            sens_type=None,
            device_type=None,
            access_timestamp=None,
            business_type=None):
        api_request = APIRequest('GetAccountProfile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DeviceIdMd5": device_id_md5,
            "Carrier": carrier,
            "Os": os,
            "Phone": phone,
            "RequestUrl": request_url,
            "Ip": ip,
            "UserAgent": user_agent,
            "ConnectionType": connection_type,
            "SensType": sens_type,
            "DeviceType": device_type,
            "AccessTimestamp": access_timestamp,
            "BusinessType": business_type}
        return self._handle_request(api_request).result

    def get_instance_count(self, owner_id=None):
        api_request = APIRequest('GetInstanceCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_phone_profile(self, phone=None, sens_type=None, data_version=None, business_type=None):
        api_request = APIRequest('GetPhoneProfile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Phone": phone,
            "SensType": sens_type,
            "DataVersion": data_version,
            "BusinessType": business_type}
        return self._handle_request(api_request).result

    def get_ip_profile(
            self,
            device_id_md5=None,
            carrier=None,
            os=None,
            request_url=None,
            ip=None,
            user_agent=None,
            connection_type=None,
            sens_type=None,
            device_type=None,
            business_type=None):
        api_request = APIRequest('GetIpProfile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DeviceIdMd5": device_id_md5,
            "Carrier": carrier,
            "Os": os,
            "RequestUrl": request_url,
            "Ip": ip,
            "UserAgent": user_agent,
            "ConnectionType": connection_type,
            "SensType": sens_type,
            "DeviceType": device_type,
            "BusinessType": business_type}
        return self._handle_request(api_request).result
