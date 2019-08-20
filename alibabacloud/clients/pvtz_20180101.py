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


class PvtzClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'pvtz'
        self.api_version = '2018-01-01'
        self.location_service_code = 'pvtz'
        self.location_endpoint_type = 'openAPI'

    def set_proxy_pattern(self, proxy_pattern=None, user_client_ip=None, zone_id=None, lang=None):
        api_request = APIRequest('SetProxyPattern', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProxyPattern": proxy_pattern,
            "UserClientIp": user_client_ip,
            "ZoneId": zone_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_statistic_summary(self, user_client_ip=None, lang=None):
        api_request = APIRequest('DescribeStatisticSummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UserClientIp": user_client_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_request_graph(
            self,
            vpc_id=None,
            user_client_ip=None,
            zone_id=None,
            lang=None,
            start_timestamp=None,
            end_timestamp=None):
        api_request = APIRequest('DescribeRequestGraph', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VpcId": vpc_id,
            "UserClientIp": user_client_ip,
            "ZoneId": zone_id,
            "Lang": lang,
            "StartTimestamp": start_timestamp,
            "EndTimestamp": end_timestamp}
        return self._handle_request(api_request).result

    def describe_zone_vpc_tree(self, user_client_ip=None, lang=None):
        api_request = APIRequest('DescribeZoneVpcTree', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UserClientIp": user_client_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def add_zone_record(
            self,
            rr=None,
            user_client_ip=None,
            zone_id=None,
            lang=None,
            type_=None,
            priority=None,
            ttl=None,
            value=None):
        api_request = APIRequest('AddZoneRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Rr": rr,
            "UserClientIp": user_client_ip,
            "ZoneId": zone_id,
            "Lang": lang,
            "Type": type_,
            "Priority": priority,
            "Ttl": ttl,
            "Value": value}
        return self._handle_request(api_request).result

    def delete_zone_record(self, record_id=None, user_client_ip=None, lang=None):
        api_request = APIRequest('DeleteZoneRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RecordId": record_id, "UserClientIp": user_client_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def check_zone_name(self, user_client_ip=None, lang=None, zone_name=None):
        api_request = APIRequest('CheckZoneName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UserClientIp": user_client_ip, "Lang": lang, "ZoneName": zone_name}
        return self._handle_request(api_request).result

    def add_zone(
            self,
            proxy_pattern=None,
            resource_group_id=None,
            user_client_ip=None,
            lang=None,
            zone_name=None):
        api_request = APIRequest('AddZone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProxyPattern": proxy_pattern,
            "ResourceGroupId": resource_group_id,
            "UserClientIp": user_client_ip,
            "Lang": lang,
            "ZoneName": zone_name}
        return self._handle_request(api_request).result

    def delete_zone(self, user_client_ip=None, zone_id=None, lang=None):
        api_request = APIRequest('DeleteZone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UserClientIp": user_client_ip, "ZoneId": zone_id, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_zones(
            self,
            query_vpc_id=None,
            resource_group_id=None,
            page_size=None,
            user_client_ip=None,
            search_mode=None,
            lang=None,
            keyword=None,
            page_number=None,
            query_region_id=None):
        api_request = APIRequest('DescribeZones', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "QueryVpcId": query_vpc_id,
            "ResourceGroupId": resource_group_id,
            "PageSize": page_size,
            "UserClientIp": user_client_ip,
            "SearchMode": search_mode,
            "Lang": lang,
            "Keyword": keyword,
            "PageNumber": page_number,
            "QueryRegionId": query_region_id}
        return self._handle_request(api_request).result

    def update_zone_remark(self, user_client_ip=None, zone_id=None, remark=None, lang=None):
        api_request = APIRequest('UpdateZoneRemark', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "ZoneId": zone_id,
            "Remark": remark,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_zone_info(self, user_client_ip=None, zone_id=None, lang=None):
        api_request = APIRequest('DescribeZoneInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UserClientIp": user_client_ip, "ZoneId": zone_id, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_regions(self, user_client_ip=None, accept_language=None, lang=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "AcceptLanguage": accept_language,
            "Lang": lang}
        return self._handle_request(api_request).result

    def bind_zone_vpc(self, user_client_ip=None, zone_id=None, lang=None, list_of_vpcs=None):
        api_request = APIRequest('BindZoneVpc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "ZoneId": zone_id,
            "Lang": lang,
            "Vpcs": list_of_vpcs}
        repeat_info = {"Vpcs": ('Vpcs', 'list', 'dict', [('RegionId', 'str', None, None),
                                                         ('VpcId', 'str', None, None),
                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def update_zone_record(
            self,
            rr=None,
            record_id=None,
            user_client_ip=None,
            lang=None,
            type_=None,
            priority=None,
            ttl=None,
            value=None):
        api_request = APIRequest('UpdateZoneRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Rr": rr,
            "RecordId": record_id,
            "UserClientIp": user_client_ip,
            "Lang": lang,
            "Type": type_,
            "Priority": priority,
            "Ttl": ttl,
            "Value": value}
        return self._handle_request(api_request).result

    def set_zone_record_status(self, record_id=None, user_client_ip=None, lang=None, status=None):
        api_request = APIRequest('SetZoneRecordStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RecordId": record_id,
            "UserClientIp": user_client_ip,
            "Lang": lang,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_zone_records(
            self,
            page_size=None,
            user_client_ip=None,
            zone_id=None,
            search_mode=None,
            tag=None,
            lang=None,
            keyword=None,
            page_number=None):
        api_request = APIRequest('DescribeZoneRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "UserClientIp": user_client_ip,
            "ZoneId": zone_id,
            "SearchMode": search_mode,
            "Tag": tag,
            "Lang": lang,
            "Keyword": keyword,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_change_logs(
            self,
            entity_type=None,
            page_size=None,
            user_client_ip=None,
            zone_id=None,
            keyword=None,
            lang=None,
            start_timestamp=None,
            page_number=None,
            end_timestamp=None):
        api_request = APIRequest('DescribeChangeLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EntityType": entity_type,
            "PageSize": page_size,
            "UserClientIp": user_client_ip,
            "ZoneId": zone_id,
            "Keyword": keyword,
            "Lang": lang,
            "StartTimestamp": start_timestamp,
            "PageNumber": page_number,
            "EndTimestamp": end_timestamp}
        return self._handle_request(api_request).result

    def describe_user_service_status(self, user_client_ip=None, lang=None):
        api_request = APIRequest('DescribeUserServiceStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UserClientIp": user_client_ip, "Lang": lang}
        return self._handle_request(api_request).result
