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


class CdnClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Cdn'
        self.api_version = '2018-05-10'
        self.location_service_code = 'cdn'
        self.location_endpoint_type = 'openAPI'

    def describe_domain_qps_data_by_layer(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            layer=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainQpsDataByLayer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "Layer": layer,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def delete_specific_staging_config(
            self,
            security_token=None,
            config_id=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteSpecificStagingConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ConfigId": config_id,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_cdn_domain_schdm_by_property(self, domain_name=None, owner_id=None, property_=None):
        api_request = APIRequest('ModifyCdnDomainSchdmByProperty', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "Property": property_}
        return self._handle_request(api_request).result

    def describe_cdn_https_domain_list(
            self,
            page_number=None,
            page_size=None,
            keyword=None,
            owner_id=None):
        api_request = APIRequest('DescribeCdnHttpsDomainList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageNumber": page_number,
            "PageSize": page_size,
            "Keyword": keyword,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cdn_domain_by_certificate(self, owner_id=None, ssl_pub=None):
        api_request = APIRequest('DescribeCdnDomainByCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "SSLPub": ssl_pub}
        return self._handle_request(api_request).result

    def tag_resources(
            self,
            region_id=None,
            list_of_tag=None,
            list_of_resource_id=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('TagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "Tag": list_of_tag,
            "ResourceId": list_of_resource_id,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       "ResourceId": ('ResourceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_user_tags(self, owner_id=None):
        api_request = APIRequest('DescribeUserTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_tag_resources(
            self,
            region_id=None,
            scope=None,
            list_of_tag=None,
            list_of_resource_id=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('DescribeTagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "Scope": scope,
            "Tag": list_of_tag,
            "ResourceId": list_of_resource_id,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       "ResourceId": ('ResourceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def untag_resources(
            self,
            region_id=None,
            list_of_resource_id=None,
            owner_id=None,
            resource_type=None,
            list_of_tag_key=None):
        api_request = APIRequest('UntagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "ResourceId": list_of_resource_id,
            "OwnerId": owner_id,
            "ResourceType": resource_type,
            "TagKey": list_of_tag_key}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "TagKey": ('TagKey', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def batch_set_cdn_domain_server_certificate(
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
        api_request = APIRequest('BatchSetCdnDomainServerCertificate',
                                 'GET', 'http', 'RPC', 'query')
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

    def delete_usage_detail_data_export_task(self, owner_id=None, task_id=None):
        api_request = APIRequest('DeleteUsageDetailDataExportTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "TaskId": task_id}
        return self._handle_request(api_request).result

    def delete_user_usage_data_export_task(self, owner_id=None, task_id=None):
        api_request = APIRequest('DeleteUserUsageDataExportTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "TaskId": task_id}
        return self._handle_request(api_request).result

    def describe_realtime_delivery_acc(
            self,
            project=None,
            start_time=None,
            end_time=None,
            owner_id=None,
            interval=None,
            log_store=None):
        api_request = APIRequest('DescribeRealtimeDeliveryAcc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Project": project,
            "StartTime": start_time,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval,
            "LogStore": log_store}
        return self._handle_request(api_request).result

    def list_fc_trigger(self, event_meta_version=None, owner_id=None, event_meta_name=None):
        api_request = APIRequest('ListFCTrigger', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EventMetaVersion": event_meta_version,
            "OwnerId": owner_id,
            "EventMetaName": event_meta_name}
        return self._handle_request(api_request).result

    def describe_cdn_certificate_detail(self, security_token=None, cert_name=None, owner_id=None):
        api_request = APIRequest('DescribeCdnCertificateDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "CertName": cert_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_req_auth_config(
            self,
            key1=None,
            key2=None,
            auth_remote_desc=None,
            security_token=None,
            domain_name=None,
            owner_id=None,
            time_out=None,
            auth_type=None):
        api_request = APIRequest('SetReqAuthConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Key1": key1,
            "Key2": key2,
            "AuthRemoteDesc": auth_remote_desc,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "TimeOut": time_out,
            "AuthType": auth_type}
        return self._handle_request(api_request).result

    def update_fc_trigger(
            self,
            notes=None,
            trigger_arn=None,
            source_arn=None,
            owner_id=None,
            role_arn=None,
            function_arn=None):
        api_request = APIRequest('UpdateFCTrigger', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "Notes": notes,
            "TriggerARN": trigger_arn,
            "SourceARN": source_arn,
            "OwnerId": owner_id,
            "RoleARN": role_arn,
            "FunctionARN": function_arn}
        return self._handle_request(api_request).result

    def set_waiting_room_config(
            self,
            wait_url=None,
            wait_uri=None,
            max_time_wait=None,
            domain_name=None,
            allow_pct=None,
            gap_time=None,
            owner_id=None):
        api_request = APIRequest('SetWaitingRoomConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WaitUrl": wait_url,
            "WaitUri": wait_uri,
            "MaxTimeWait": max_time_wait,
            "DomainName": domain_name,
            "AllowPct": allow_pct,
            "GapTime": gap_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_waf_config(self, enable=None, domain_name=None, owner_id=None, config_id=None):
        api_request = APIRequest('SetWafConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Enable": enable,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ConfigId": config_id}
        return self._handle_request(api_request).result

    def set_video_seek_config(self, enable=None, domain_name=None, owner_id=None, config_id=None):
        api_request = APIRequest('SetVideoSeekConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Enable": enable,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ConfigId": config_id}
        return self._handle_request(api_request).result

    def set_remove_query_string_config(
            self,
            ali_remove_args=None,
            keep_oss_args=None,
            domain_name=None,
            owner_id=None,
            config_id=None):
        api_request = APIRequest('SetRemoveQueryStringConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AliRemoveArgs": ali_remove_args,
            "KeepOssArgs": keep_oss_args,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ConfigId": config_id}
        return self._handle_request(api_request).result

    def set_range_config(self, enable=None, domain_name=None, owner_id=None, config_id=None):
        api_request = APIRequest('SetRangeConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Enable": enable,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ConfigId": config_id}
        return self._handle_request(api_request).result

    def set_page_compress_config(
            self,
            enable=None,
            domain_name=None,
            owner_id=None,
            config_id=None):
        api_request = APIRequest('SetPageCompressConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Enable": enable,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ConfigId": config_id}
        return self._handle_request(api_request).result

    def set_optimize_config(self, enable=None, domain_name=None, owner_id=None, config_id=None):
        api_request = APIRequest('SetOptimizeConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Enable": enable,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ConfigId": config_id}
        return self._handle_request(api_request).result

    def set_l2_oss_key_config(
            self,
            domain_name=None,
            owner_id=None,
            config_id=None,
            private_oss_auth=None):
        api_request = APIRequest('SetL2OssKeyConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ConfigId": config_id,
            "PrivateOssAuth": private_oss_auth}
        return self._handle_request(api_request).result

    def set_ip_black_list_config(
            self,
            block_ips=None,
            domain_name=None,
            owner_id=None,
            config_id=None):
        api_request = APIRequest('SetIpBlackListConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BlockIps": block_ips,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ConfigId": config_id}
        return self._handle_request(api_request).result

    def set_ignore_query_string_config(
            self,
            enable=None,
            keep_oss_args=None,
            domain_name=None,
            owner_id=None,
            hash_key_args=None,
            config_id=None):
        api_request = APIRequest('SetIgnoreQueryStringConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Enable": enable,
            "KeepOssArgs": keep_oss_args,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "HashKeyArgs": hash_key_args,
            "ConfigId": config_id}
        return self._handle_request(api_request).result

    def set_https_option_config(self, http2=None, domain_name=None, owner_id=None, config_id=None):
        api_request = APIRequest('SetHttpsOptionConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Http2": http2,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ConfigId": config_id}
        return self._handle_request(api_request).result

    def set_http_error_page_config(
            self,
            page_url=None,
            error_code=None,
            domain_name=None,
            owner_id=None,
            config_id=None):
        api_request = APIRequest('SetHttpErrorPageConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageUrl": page_url,
            "ErrorCode": error_code,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ConfigId": config_id}
        return self._handle_request(api_request).result

    def set_forward_scheme_config(
            self,
            scheme_origin_port=None,
            enable=None,
            scheme_origin=None,
            domain_name=None,
            owner_id=None,
            config_id=None):
        api_request = APIRequest('SetForwardSchemeConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SchemeOriginPort": scheme_origin_port,
            "Enable": enable,
            "SchemeOrigin": scheme_origin,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ConfigId": config_id}
        return self._handle_request(api_request).result

    def set_file_cache_expired_config(
            self,
            security_token=None,
            domain_name=None,
            weight=None,
            cache_content=None,
            owner_id=None,
            ttl=None):
        api_request = APIRequest('SetFileCacheExpiredConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "Weight": weight,
            "CacheContent": cache_content,
            "OwnerId": owner_id,
            "TTL": ttl}
        return self._handle_request(api_request).result

    def set_domain_green_manager_config(self, enable=None, domain_name=None, owner_id=None):
        api_request = APIRequest('SetDomainGreenManagerConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Enable": enable, "DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_user_custom_log_config(self, owner_id=None, config_id=None, tag=None):
        api_request = APIRequest('ModifyUserCustomLogConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "ConfigId": config_id, "Tag": tag}
        return self._handle_request(api_request).result

    def modify_domain_custom_log_config(self, domain_name=None, owner_id=None, config_id=None):
        api_request = APIRequest('ModifyDomainCustomLogConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ConfigId": config_id}
        return self._handle_request(api_request).result

    def list_domains_by_log_config_id(self, owner_id=None, config_id=None):
        api_request = APIRequest('ListDomainsByLogConfigId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "ConfigId": config_id}
        return self._handle_request(api_request).result

    def describe_user_usage_detail_data_export_task(
            self, page_number=None, page_size=None, owner_id=None):
        api_request = APIRequest('DescribeUserUsageDetailDataExportTask',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageNumber": page_number,
            "PageSize": page_size,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_user_usage_data_export_task(self, page_number=None, page_size=None, owner_id=None):
        api_request = APIRequest('DescribeUserUsageDataExportTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageNumber": page_number,
            "PageSize": page_size,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_top_domains_by_flow(
            self,
            start_time=None,
            limit=None,
            product=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeTopDomainsByFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Limit": limit,
            "Product": product,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_fc_trigger(self, trigger_arn=None, owner_id=None):
        api_request = APIRequest('DescribeFCTrigger', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TriggerARN": trigger_arn, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_usage_data(
            self,
            start_time=None,
            data_protocol=None,
            area=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            field=None,
            interval=None):
        api_request = APIRequest('DescribeDomainUsageData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DataProtocol": data_protocol,
            "Area": area,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Field": field,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_domain_traffic_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainTrafficData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_domain_src_traffic_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainSrcTrafficData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_domain_src_bps_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainSrcBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_domain_req_hit_rate_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainReqHitRateData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_domain_region_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainRegionData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_real_time_src_traffic_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainRealTimeSrcTrafficData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_real_time_src_bps_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainRealTimeSrcBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_real_time_req_hit_rate_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainRealTimeReqHitRateData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_real_time_qps_data(
            self,
            location_name_en=None,
            isp_name_en=None,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainRealTimeQpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "IspNameEn": isp_name_en,
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_real_time_http_code_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainRealTimeHttpCodeData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_real_time_byte_hit_rate_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainRealTimeByteHitRateData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_real_time_bps_data(
            self,
            location_name_en=None,
            isp_name_en=None,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainRealTimeBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "IspNameEn": isp_name_en,
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_qps_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainQpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_domain_path_data(
            self,
            start_time=None,
            page_number=None,
            path=None,
            page_size=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainPathData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "PageNumber": page_number,
            "Path": path,
            "PageSize": page_size,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_http_code_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainHttpCodeData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_domain_hit_rate_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainHitRateData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_domain_custom_log_config(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeDomainCustomLogConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_cname(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeDomainCname', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_certificate_info(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeDomainCertificateInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_bps_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_custom_log_config(self, owner_id=None, config_id=None):
        api_request = APIRequest('DescribeCustomLogConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "ConfigId": config_id}
        return self._handle_request(api_request).result

    def describe_cdn_domain_logs(
            self,
            start_time=None,
            page_number=None,
            page_size=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeCdnDomainLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "PageNumber": page_number,
            "PageSize": page_size,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_fc_trigger(self, trigger_arn=None, owner_id=None):
        api_request = APIRequest('DeleteFCTrigger', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TriggerARN": trigger_arn, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_user_usage_data_export_task(
            self,
            task_name=None,
            language=None,
            start_time=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('CreateUserUsageDataExportTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TaskName": task_name,
            "Language": language,
            "StartTime": start_time,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_usage_detail_data_export_task(
            self,
            domain_names=None,
            task_name=None,
            language=None,
            start_time=None,
            type_=None,
            group=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('CreateUsageDetailDataExportTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainNames": domain_names,
            "TaskName": task_name,
            "Language": language,
            "StartTime": start_time,
            "Type": type_,
            "Group": group,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_fc_trigger(
            self,
            notes=None,
            event_meta_version=None,
            trigger_arn=None,
            source_arn=None,
            owner_id=None,
            role_arn=None,
            event_meta_name=None,
            function_arn=None):
        api_request = APIRequest('AddFCTrigger', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "Notes": notes,
            "EventMetaVersion": event_meta_version,
            "TriggerARN": trigger_arn,
            "SourceARN": source_arn,
            "OwnerId": owner_id,
            "RoleARN": role_arn,
            "EventMetaName": event_meta_name,
            "FunctionARN": function_arn}
        return self._handle_request(api_request).result

    def start_cdn_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('StartCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_add_cdn_domain(
            self,
            top_level_domain=None,
            resource_group_id=None,
            sources=None,
            security_token=None,
            cdn_type=None,
            owner_account=None,
            scope=None,
            domain_name=None,
            owner_id=None,
            check_url=None):
        api_request = APIRequest('BatchAddCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "ResourceGroupId": resource_group_id,
            "Sources": sources,
            "SecurityToken": security_token,
            "CdnType": cdn_type,
            "OwnerAccount": owner_account,
            "Scope": scope,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "CheckUrl": check_url}
        return self._handle_request(api_request).result

    def batch_set_cdn_domain_config(
            self,
            functions=None,
            security_token=None,
            domain_names=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('BatchSetCdnDomainConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Functions": functions,
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cdn_user_resource_package(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeCdnUserResourcePackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_average_response_time(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_type=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainAverageResponseTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainType": domain_type,
            "TimeMerge": time_merge,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def batch_start_cdn_domain(self, security_token=None, domain_names=None, owner_id=None):
        api_request = APIRequest('BatchStartCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_file_cache_expired_config(
            self,
            security_token=None,
            config_id=None,
            domain_name=None,
            weight=None,
            cache_content=None,
            owner_id=None,
            ttl=None):
        api_request = APIRequest('ModifyFileCacheExpiredConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ConfigID": config_id,
            "DomainName": domain_name,
            "Weight": weight,
            "CacheContent": cache_content,
            "OwnerId": owner_id,
            "TTL": ttl}
        return self._handle_request(api_request).result

    def describe_ip_info(self, security_token=None, ip=None, owner_id=None):
        api_request = APIRequest('DescribeIpInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "IP": ip, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_file_size_proportion_data(
            self,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainFileSizeProportionData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_http_header_config(
            self,
            header_value=None,
            security_token=None,
            config_id=None,
            domain_name=None,
            header_key=None,
            owner_id=None):
        api_request = APIRequest('SetHttpHeaderConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HeaderValue": header_value,
            "SecurityToken": security_token,
            "ConfigId": config_id,
            "DomainName": domain_name,
            "HeaderKey": header_key,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_update_cdn_domain(
            self,
            top_level_domain=None,
            resource_group_id=None,
            sources=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('BatchUpdateCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "ResourceGroupId": resource_group_id,
            "Sources": sources,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_pv_data(
            self,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainPvData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cdn_user_quota(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeCdnUserQuota', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_delete_cdn_domain_config(
            self,
            function_names=None,
            security_token=None,
            domain_names=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('BatchDeleteCdnDomainConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FunctionNames": function_names,
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_refresh_quota(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeRefreshQuota', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_domain_server_certificate(
            self,
            private_key=None,
            force_set=None,
            server_certificate_status=None,
            server_certificate=None,
            security_token=None,
            cert_type=None,
            cert_name=None,
            domain_name=None,
            owner_id=None,
            region=None):
        api_request = APIRequest('SetDomainServerCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PrivateKey": private_key,
            "ForceSet": force_set,
            "ServerCertificateStatus": server_certificate_status,
            "ServerCertificate": server_certificate,
            "SecurityToken": security_token,
            "CertType": cert_type,
            "CertName": cert_name,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "Region": region}
        return self._handle_request(api_request).result

    def delete_specific_config(
            self,
            security_token=None,
            config_id=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteSpecificConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ConfigId": config_id,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_source_host_config(
            self,
            security_token=None,
            enable=None,
            domain_name=None,
            owner_id=None,
            back_src_domain=None):
        api_request = APIRequest('SetSourceHostConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "Enable": enable,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "BackSrcDomain": back_src_domain}
        return self._handle_request(api_request).result

    def describe_cdn_region_and_isp(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeCdnRegionAndIsp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def open_cdn_service(self, security_token=None, internet_charge_type=None, owner_id=None):
        api_request = APIRequest('OpenCdnService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "InternetChargeType": internet_charge_type,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_top_refer_visit(
            self,
            start_time=None,
            percent=None,
            domain_name=None,
            owner_id=None,
            sort_by=None):
        api_request = APIRequest('DescribeDomainTopReferVisit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Percent": percent,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "SortBy": sort_by}
        return self._handle_request(api_request).result

    def set_cc_config(
            self,
            allow_ips=None,
            security_token=None,
            domain_name=None,
            owner_id=None,
            block_ips=None):
        api_request = APIRequest('SetCcConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AllowIps": allow_ips,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "BlockIps": block_ips}
        return self._handle_request(api_request).result

    def describe_l2_vips_by_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeL2VipsByDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cdn_certificate_list(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeCdnCertificateList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_cdn_domain(
            self,
            resource_group_id=None,
            security_token=None,
            owner_account=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def push_object_cache(self, area=None, security_token=None, object_path=None, owner_id=None):
        api_request = APIRequest('PushObjectCache', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Area": area,
            "SecurityToken": security_token,
            "ObjectPath": object_path,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_cdn_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('StopCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_uv_data(
            self,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainUvData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_stop_cdn_domain(self, security_token=None, domain_names=None, owner_id=None):
        api_request = APIRequest('BatchStopCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_cdn_service(self, security_token=None, internet_charge_type=None, owner_id=None):
        api_request = APIRequest('ModifyCdnService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "InternetChargeType": internet_charge_type,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cdn_service(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeCdnService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_cdn_domain(
            self,
            top_level_domain=None,
            resource_group_id=None,
            sources=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('ModifyCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "ResourceGroupId": resource_group_id,
            "Sources": sources,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cdn_domain_configs(
            self,
            function_names=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeCdnDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FunctionNames": function_names,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_refresh_tasks(
            self,
            resource_group_id=None,
            security_token=None,
            object_path=None,
            domain_name=None,
            page_size=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            object_type=None,
            task_id=None,
            page_number=None,
            status=None):
        api_request = APIRequest('DescribeRefreshTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SecurityToken": security_token,
            "ObjectPath": object_path,
            "DomainName": domain_name,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "ObjectType": object_type,
            "TaskId": task_id,
            "PageNumber": page_number,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_cdn_domain_detail(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeCdnDomainDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_user_domains(
            self,
            func_filter=None,
            domain_name=None,
            owner_id=None,
            func_id=None,
            page_number=None,
            domain_status=None,
            domain_search_type=None,
            check_domain_show=None,
            resource_group_id=None,
            security_token=None,
            cdn_type=None,
            page_size=None,
            list_of_tag=None):
        api_request = APIRequest('DescribeUserDomains', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FuncFilter": func_filter,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "FuncId": func_id,
            "PageNumber": page_number,
            "DomainStatus": domain_status,
            "DomainSearchType": domain_search_type,
            "CheckDomainShow": check_domain_show,
            "ResourceGroupId": resource_group_id,
            "SecurityToken": security_token,
            "CdnType": cdn_type,
            "PageSize": page_size,
            "Tag": list_of_tag}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def set_ip_allow_list_config(
            self,
            allow_ips=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('SetIpAllowListConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AllowIps": allow_ips,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_cdn_domain(
            self,
            top_level_domain=None,
            resource_group_id=None,
            sources=None,
            security_token=None,
            cdn_type=None,
            owner_account=None,
            scope=None,
            domain_name=None,
            owner_id=None,
            check_url=None):
        api_request = APIRequest('AddCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "ResourceGroupId": resource_group_id,
            "Sources": sources,
            "SecurityToken": security_token,
            "CdnType": cdn_type,
            "OwnerAccount": owner_account,
            "Scope": scope,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "CheckUrl": check_url}
        return self._handle_request(api_request).result

    def refresh_object_caches(
            self,
            security_token=None,
            object_path=None,
            owner_id=None,
            object_type=None):
        api_request = APIRequest('RefreshObjectCaches', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ObjectPath": object_path,
            "OwnerId": owner_id,
            "ObjectType": object_type}
        return self._handle_request(api_request).result

    def describe_cdn_types(self, security_token=None, owner_account=None, owner_id=None):
        api_request = APIRequest('DescribeCdnTypes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_range_data_by_locate_and_isp_service(
            self,
            domain_names=None,
            location_names=None,
            start_time=None,
            isp_names=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeRangeDataByLocateAndIspService',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainNames": domain_names,
            "LocationNames": location_names,
            "StartTime": start_time,
            "IspNames": isp_names,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_error_page_config(
            self,
            page_type=None,
            security_token=None,
            domain_name=None,
            custom_page_url=None,
            owner_id=None):
        api_request = APIRequest('SetErrorPageConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageType": page_type,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "CustomPageUrl": custom_page_url,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_req_header_config(
            self,
            security_token=None,
            config_id=None,
            domain_name=None,
            owner_id=None,
            value=None,
            key=None):
        api_request = APIRequest('SetReqHeaderConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ConfigId": config_id,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "Value": value,
            "Key": key}
        return self._handle_request(api_request).result

    def describe_domain_bps_data_by_time_stamp(
            self,
            location_names=None,
            isp_names=None,
            domain_name=None,
            owner_id=None,
            time_point=None):
        api_request = APIRequest('DescribeDomainBpsDataByTimeStamp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNames": location_names,
            "IspNames": isp_names,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "TimePoint": time_point}
        return self._handle_request(api_request).result

    def set_referer_config(
            self,
            refer_list=None,
            security_token=None,
            domain_name=None,
            refer_type=None,
            disable_ast=None,
            owner_id=None,
            allow_empty=None):
        api_request = APIRequest('SetRefererConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ReferList": refer_list,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "ReferType": refer_type,
            "DisableAst": disable_ast,
            "OwnerId": owner_id,
            "AllowEmpty": allow_empty}
        return self._handle_request(api_request).result

    def set_force_redirect_config(
            self,
            security_token=None,
            domain_name=None,
            redirect_type=None,
            owner_id=None):
        api_request = APIRequest('SetForceRedirectConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "RedirectType": redirect_type,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_isp_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainISPData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_user_configs(self, security_token=None, owner_id=None, config=None):
        api_request = APIRequest('DescribeUserConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "OwnerId": owner_id,
            "Config": config}
        return self._handle_request(api_request).result

    def modify_http_header_config(
            self,
            header_value=None,
            security_token=None,
            config_id=None,
            domain_name=None,
            header_key=None,
            owner_id=None):
        api_request = APIRequest('ModifyHttpHeaderConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HeaderValue": header_value,
            "SecurityToken": security_token,
            "ConfigID": config_id,
            "DomainName": domain_name,
            "HeaderKey": header_key,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domains_by_source(self, sources=None, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeDomainsBySource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Sources": sources,
            "SecurityToken": security_token,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_top_url_visit(
            self,
            start_time=None,
            percent=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            sort_by=None):
        api_request = APIRequest('DescribeDomainTopUrlVisit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Percent": percent,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "SortBy": sort_by}
        return self._handle_request(api_request).result

    def describe_domains_usage_by_day(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainsUsageByDay', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_src_http_code_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainSrcHttpCodeData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_domain_max95_bps_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainMax95BpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result
