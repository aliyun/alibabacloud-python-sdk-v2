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


class ScdnClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'scdn'
        self.api_version = '2017-11-15'
        self.location_service_code = 'scdn'
        self.location_endpoint_type = 'openAPI'

    def describe_scdn_domain_real_time_src_traffic_data(
            self, start_time=None, domain_name=None, end_time=None, owner_id=None):
        api_request = APIRequest(
            'DescribeScdnDomainRealTimeSrcTrafficData',
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

    def describe_scdn_domain_real_time_src_bps_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainRealTimeSrcBpsData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_real_time_req_hit_rate_data(
            self, start_time=None, domain_name=None, end_time=None, owner_id=None):
        api_request = APIRequest(
            'DescribeScdnDomainRealTimeReqHitRateData',
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

    def describe_scdn_domain_real_time_qps_data(
            self,
            location_name_en=None,
            isp_name_en=None,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainRealTimeQpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "IspNameEn": isp_name_en,
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_real_time_http_code_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainRealTimeHttpCodeData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_real_time_byte_hit_rate_data(
            self, start_time=None, domain_name=None, end_time=None, owner_id=None):
        api_request = APIRequest(
            'DescribeScdnDomainRealTimeByteHitRateData',
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

    def describe_scdn_domain_real_time_bps_data(
            self,
            location_name_en=None,
            isp_name_en=None,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainRealTimeBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "IspNameEn": isp_name_en,
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_top_domains_by_flow(
            self,
            start_time=None,
            limit=None,
            product=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnTopDomainsByFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Limit": limit,
            "Product": product,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_real_time_traffic_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainRealTimeTrafficData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_top_url_visit(
            self,
            security_token=None,
            domain_name=None,
            sort_by=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainTopUrlVisit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "SortBy": sort_by,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_top_refer_visit(
            self,
            security_token=None,
            domain_name=None,
            sort_by=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainTopReferVisit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "SortBy": sort_by,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_region_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainRegionData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_update_scdn_domain(
            self,
            top_level_domain=None,
            resource_group_id=None,
            sources=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('BatchUpdateScdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "ResourceGroupId": resource_group_id,
            "Sources": sources,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def open_scdn_service(
            self,
            end_date=None,
            security_token=None,
            bandwidth=None,
            domain_count=None,
            owner_id=None,
            protect_type=None,
            start_date=None,
            elastic_protection=None,
            ddo_sbasic=None,
            cc_protection=None):
        api_request = APIRequest('OpenScdnService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndDate": end_date,
            "SecurityToken": security_token,
            "Bandwidth": bandwidth,
            "DomainCount": domain_count,
            "OwnerId": owner_id,
            "ProtectType": protect_type,
            "StartDate": start_date,
            "ElasticProtection": elastic_protection,
            "DDoSBasic": ddo_sbasic,
            "CcProtection": cc_protection}
        return self._handle_request(api_request).result

    def set_domain_server_certificate(
            self,
            security_token=None,
            ssl_pub=None,
            cert_name=None,
            ssl_protocol=None,
            domain_name=None,
            owner_id=None,
            region=None,
            ssl_pri=None):
        api_request = APIRequest('SetDomainServerCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "SSLPub": ssl_pub,
            "CertName": cert_name,
            "SSLProtocol": ssl_protocol,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "Region": region,
            "SSLPri": ssl_pri}
        return self._handle_request(api_request).result

    def describe_scdn_domain_uv_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainUvData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_ip_info(self, security_token=None, ip=None, owner_id=None):
        api_request = APIRequest('DescribeScdnIpInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "IP": ip, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_pv_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainPvData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_isp_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainIspData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_cname(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeScdnDomainCname', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_log(
            self,
            start_time=None,
            page_number=None,
            page_size=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "PageNumber": page_number,
            "PageSize": page_size,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_user_quota(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeScdnUserQuota', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_certificate_info(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeScdnDomainCertificateInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_http_code_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeScdnDomainHttpCodeData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_scdn_domain_hit_rate_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeScdnDomainHitRateData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def preload_scdn_object_caches(
            self,
            area=None,
            security_token=None,
            object_path=None,
            owner_id=None):
        api_request = APIRequest('PreloadScdnObjectCaches', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Area": area,
            "SecurityToken": security_token,
            "ObjectPath": object_path,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_certificate_detail(self, security_token=None, cert_name=None, owner_id=None):
        api_request = APIRequest('DescribeScdnCertificateDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "CertName": cert_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_scdn_domain_certificate(
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
        api_request = APIRequest('SetScdnDomainCertificate', 'GET', 'http', 'RPC', 'query')
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

    def describe_scdn_refresh_tasks(
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
        api_request = APIRequest('DescribeScdnRefreshTasks', 'GET', 'http', 'RPC', 'query')
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

    def refresh_scdn_object_caches(
            self,
            security_token=None,
            object_path=None,
            owner_id=None,
            object_type=None):
        api_request = APIRequest('RefreshScdnObjectCaches', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ObjectPath": object_path,
            "OwnerId": owner_id,
            "ObjectType": object_type}
        return self._handle_request(api_request).result

    def batch_set_scdn_domain_configs(
            self,
            functions=None,
            security_token=None,
            domain_names=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('BatchSetScdnDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Functions": functions,
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_certificate_list(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeScdnCertificateList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_configs(
            self,
            function_names=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeScdnDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FunctionNames": function_names,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_refresh_quota(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeScdnRefreshQuota', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_delete_scdn_domain_configs(
            self,
            function_names=None,
            security_token=None,
            domain_names=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('BatchDeleteScdnDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FunctionNames": function_names,
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_user_domains(
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
        api_request = APIRequest('DescribeScdnUserDomains', 'GET', 'http', 'RPC', 'query')
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

    def describe_scdn_domain_traffic_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeScdnDomainTrafficData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_scdn_domain_qps_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeScdnDomainQpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_scdn_domain_origin_traffic_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeScdnDomainOriginTrafficData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_scdn_domain_origin_bps_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeScdnDomainOriginBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_scdn_domain_bps_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeScdnDomainBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def update_scdn_domain(
            self,
            resource_group_id=None,
            sources=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('UpdateScdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "Sources": sources,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_scdn_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('StopScdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_scdn_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('StartScdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_service(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeScdnService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scdn_domain_detail(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeScdnDomainDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_scdn_domain(
            self,
            resource_group_id=None,
            security_token=None,
            owner_account=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteScdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def check_scdn_service(self, security_token=None, owner_id=None):
        api_request = APIRequest('CheckScdnService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_scdn_domain(
            self,
            resource_group_id=None,
            sources=None,
            security_token=None,
            owner_account=None,
            scope=None,
            domain_name=None,
            owner_id=None,
            check_url=None):
        api_request = APIRequest('AddScdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "Sources": sources,
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "Scope": scope,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "CheckUrl": check_url}
        return self._handle_request(api_request).result
