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


class DcdnClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'dcdn'
        self.api_version = '2018-01-15'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def modify_dcdn_domain_schdm_by_property(self, property_=None, domain_name=None, owner_id=None):
        api_request = APIRequest('ModifyDCdnDomainSchdmByProperty', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Property": property_,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_ipa_bps_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            fix_time_gap=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDcdnDomainIpaBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "FixTimeGap": fix_time_gap,
            "TimeMerge": time_merge,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_ipa_traffic_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            fix_time_gap=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDcdnDomainIpaTrafficData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "FixTimeGap": fix_time_gap,
            "TimeMerge": time_merge,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_dcdn_ipa_service(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeDcdnIpaService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_dcdn_ipa_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('StopDcdnIpaDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_ipa_domain_detail(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeDcdnIpaDomainDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_dcdn_ipa_domain(
            self,
            resource_group_id=None,
            security_token=None,
            owner_account=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteDcdnIpaDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_dcdn_ipa_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('StartDcdnIpaDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_user_dcdn_ipa_status(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeUserDcdnIpaStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_dcdn_ipa_domain(
            self,
            top_level_domain=None,
            resource_group_id=None,
            sources=None,
            security_token=None,
            owner_account=None,
            scope=None,
            domain_name=None,
            owner_id=None,
            check_url=None):
        api_request = APIRequest('AddDcdnIpaDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "ResourceGroupId": resource_group_id,
            "Sources": sources,
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "Scope": scope,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "CheckUrl": check_url}
        return self._handle_request(api_request).result

    def batch_set_dcdn_ipa_domain_configs(
            self,
            functions=None,
            security_token=None,
            domain_names=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('BatchSetDcdnIpaDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Functions": functions,
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_dcdn_ipa_domain(
            self,
            top_level_domain=None,
            resource_group_id=None,
            sources=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('UpdateDcdnIpaDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "ResourceGroupId": resource_group_id,
            "Sources": sources,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_ipa_domain_configs(
            self,
            function_names=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnIpaDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FunctionNames": function_names,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_ipa_user_domains(
            self,
            func_filter=None,
            check_domain_show=None,
            resource_group_id=None,
            security_token=None,
            page_size=None,
            domain_name=None,
            owner_id=None,
            func_id=None,
            page_number=None,
            domain_status=None,
            domain_search_type=None):
        api_request = APIRequest('DescribeDcdnIpaUserDomains', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FuncFilter": func_filter,
            "CheckDomainShow": check_domain_show,
            "ResourceGroupId": resource_group_id,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "FuncId": func_id,
            "PageNumber": page_number,
            "DomainStatus": domain_status,
            "DomainSearchType": domain_search_type}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_real_time_bps_data(
            self,
            location_name_en=None,
            isp_name_en=None,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainRealTimeBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "IspNameEn": isp_name_en,
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_real_time_byte_hit_rate_data(
            self, start_time=None, domain_name=None, end_time=None, owner_id=None):
        api_request = APIRequest(
            'DescribeDcdnDomainRealTimeByteHitRateData',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_real_time_http_code_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainRealTimeHttpCodeData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_real_time_qps_data(
            self,
            location_name_en=None,
            isp_name_en=None,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainRealTimeQpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "IspNameEn": isp_name_en,
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_real_time_req_hit_rate_data(
            self, start_time=None, domain_name=None, end_time=None, owner_id=None):
        api_request = APIRequest(
            'DescribeDcdnDomainRealTimeReqHitRateData',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_real_time_src_bps_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainRealTimeSrcBpsData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_real_time_src_traffic_data(
            self, start_time=None, domain_name=None, end_time=None, owner_id=None):
        api_request = APIRequest(
            'DescribeDcdnDomainRealTimeSrcTrafficData',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_uv_data(
            self,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainUvData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_pv_data(
            self,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainPvData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_websocket_http_code_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest(
            'DescribeDcdnDomainWebsocketHttpCodeData',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_websocket_bps_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            fix_time_gap=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDcdnDomainWebsocketBpsData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "FixTimeGap": fix_time_gap,
            "TimeMerge": time_merge,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_websocket_traffic_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            fix_time_gap=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDcdnDomainWebsocketTrafficData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "FixTimeGap": fix_time_gap,
            "TimeMerge": time_merge,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_top_url_visit(
            self,
            security_token=None,
            domain_name=None,
            sort_by=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainTopUrlVisit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "SortBy": sort_by,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_top_refer_visit(
            self,
            security_token=None,
            domain_name=None,
            sort_by=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainTopReferVisit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "SortBy": sort_by,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_region_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainRegionData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_isp_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainIspData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_top_domains_by_flow(
            self,
            start_time=None,
            limit=None,
            product=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnTopDomainsByFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Limit": limit,
            "Product": product,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_user_quota(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeDcdnUserQuota', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_certificate_info(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainCertificateInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_traffic_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            fix_time_gap=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDcdnDomainTrafficData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "FixTimeGap": fix_time_gap,
            "TimeMerge": time_merge,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_qps_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            fix_time_gap=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDcdnDomainQpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "FixTimeGap": fix_time_gap,
            "TimeMerge": time_merge,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_origin_traffic_data(
            self,
            start_time=None,
            fix_time_gap=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDcdnDomainOriginTrafficData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "FixTimeGap": fix_time_gap,
            "TimeMerge": time_merge,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_origin_bps_data(
            self,
            start_time=None,
            fix_time_gap=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDcdnDomainOriginBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "FixTimeGap": fix_time_gap,
            "TimeMerge": time_merge,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_log(
            self,
            start_time=None,
            page_number=None,
            page_size=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "PageNumber": page_number,
            "PageSize": page_size,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_http_code_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDcdnDomainHttpCodeData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_hit_rate_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDcdnDomainHitRateData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_cname(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainCname', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_bps_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            fix_time_gap=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDcdnDomainBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "FixTimeGap": fix_time_gap,
            "TimeMerge": time_merge,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def preload_dcdn_object_caches(
            self,
            area=None,
            security_token=None,
            object_path=None,
            owner_id=None):
        api_request = APIRequest('PreloadDcdnObjectCaches', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Area": area,
            "SecurityToken": security_token,
            "ObjectPath": object_path,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_dcdn_specific_config(
            self,
            security_token=None,
            config_id=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteDcdnSpecificConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ConfigId": config_id,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_user_domains(
            self,
            func_filter=None,
            check_domain_show=None,
            resource_group_id=None,
            security_token=None,
            page_size=None,
            domain_name=None,
            owner_id=None,
            func_id=None,
            page_number=None,
            domain_status=None,
            domain_search_type=None):
        api_request = APIRequest('DescribeDcdnUserDomains', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FuncFilter": func_filter,
            "CheckDomainShow": check_domain_show,
            "ResourceGroupId": resource_group_id,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "FuncId": func_id,
            "PageNumber": page_number,
            "DomainStatus": domain_status,
            "DomainSearchType": domain_search_type}
        return self._handle_request(api_request).result

    def batch_start_dcdn_domain(self, security_token=None, domain_names=None, owner_id=None):
        api_request = APIRequest('BatchStartDcdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_detail(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_user_dcdn_status(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeUserDcdnStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_dcdn_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('StartDcdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_refresh_tasks(
            self,
            object_path=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            resource_group_id=None,
            security_token=None,
            page_size=None,
            object_type=None,
            task_id=None,
            status=None):
        api_request = APIRequest('DescribeDcdnRefreshTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ObjectPath": object_path,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "ResourceGroupId": resource_group_id,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "ObjectType": object_type,
            "TaskId": task_id,
            "Status": status}
        return self._handle_request(api_request).result

    def batch_stop_dcdn_domain(self, security_token=None, domain_names=None, owner_id=None):
        api_request = APIRequest('BatchStopDcdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_dcdn_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('StopDcdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_dcdn_domain(
            self,
            top_level_domain=None,
            resource_group_id=None,
            sources=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('UpdateDcdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "ResourceGroupId": resource_group_id,
            "Sources": sources,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_service(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeDcdnService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def refresh_dcdn_object_caches(
            self,
            security_token=None,
            object_path=None,
            owner_id=None,
            object_type=None):
        api_request = APIRequest('RefreshDcdnObjectCaches', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ObjectPath": object_path,
            "OwnerId": owner_id,
            "ObjectType": object_type}
        return self._handle_request(api_request).result

    def describe_dcdn_domain_configs(
            self,
            function_names=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeDcdnDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FunctionNames": function_names,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_user_resource_package(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeDcdnUserResourcePackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_refresh_quota(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeDcdnRefreshQuota', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_set_dcdn_domain_configs(
            self,
            functions=None,
            security_token=None,
            domain_names=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('BatchSetDcdnDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Functions": functions,
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_dcdn_domain_certificate(
            self,
            force_set=None,
            security_token=None,
            cert_type=None,
            ssl_pub=None,
            cert_name=None,
            ssl_protocol=None,
            domain_name=None,
            owner_id=None,
            region=None,
            ssl_pri=None):
        api_request = APIRequest('SetDcdnDomainCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ForceSet": force_set,
            "SecurityToken": security_token,
            "CertType": cert_type,
            "SSLPub": ssl_pub,
            "CertName": cert_name,
            "SSLProtocol": ssl_protocol,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "Region": region,
            "SSLPri": ssl_pri}
        return self._handle_request(api_request).result

    def add_dcdn_domain(
            self,
            top_level_domain=None,
            resource_group_id=None,
            sources=None,
            security_token=None,
            owner_account=None,
            scope=None,
            domain_name=None,
            owner_id=None,
            check_url=None):
        api_request = APIRequest('AddDcdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "ResourceGroupId": resource_group_id,
            "Sources": sources,
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "Scope": scope,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "CheckUrl": check_url}
        return self._handle_request(api_request).result

    def delete_dcdn_domain(
            self,
            resource_group_id=None,
            security_token=None,
            owner_account=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteDcdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_certificate_detail(self, security_token=None, cert_name=None, owner_id=None):
        api_request = APIRequest('DescribeDcdnCertificateDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "CertName": cert_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dcdn_certificate_list(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeDcdnCertificateList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_delete_dcdn_domain_configs(
            self,
            function_names=None,
            security_token=None,
            domain_names=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('BatchDeleteDcdnDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FunctionNames": function_names,
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result
