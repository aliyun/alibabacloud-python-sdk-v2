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


class CdnClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Cdn'
        self.api_version = '2014-11-11'
        self.location_service_code = 'None'
        self.location_endpoint_type = 'openAPI'

    def describe_l2_vips_by_dynamic_domain(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeL2VipsByDynamicDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
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

    def describe_cdn_user_quota(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeCdnUserQuota', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
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

    def describe_fc_trigger(self, trigger_arn=None, owner_id=None):
        api_request = APIRequest('DescribeFCTrigger', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TriggerARN": trigger_arn, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_fc_trigger(self, trigger_arn=None, owner_id=None):
        api_request = APIRequest('DeleteFCTrigger', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TriggerARN": trigger_arn, "OwnerId": owner_id}
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

    def describe_domain_certificate_info(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeDomainCertificateInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
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

    def describe_domain_cname(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeDomainCname', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_user_custom_log_config(self, owner_id=None):
        api_request = APIRequest('DescribeUserCustomLogConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id}
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

    def describe_domain_slow_ratio(
            self,
            start_time=None,
            page_number=None,
            page_size=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainSlowRatio', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "PageNumber": page_number,
            "PageSize": page_size,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
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

    def describe_domain_custom_log_config(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeDomainCustomLogConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_custom_log_config(self, owner_id=None, config_id=None):
        api_request = APIRequest('DescribeCustomLogConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "ConfigId": config_id}
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

    def set_user_green_manager_config(
            self,
            security_token=None,
            quota=None,
            owner_id=None,
            ratio=None):
        api_request = APIRequest('SetUserGreenManagerConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "Quota": quota,
            "OwnerId": owner_id,
            "Ratio": ratio}
        return self._handle_request(api_request).result

    def set_domain_green_manager_config(self, domain_name=None, owner_id=None, enable=None):
        api_request = APIRequest('SetDomainGreenManagerConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id, "Enable": enable}
        return self._handle_request(api_request).result

    def set_https_option_config(
            self,
            security_token=None,
            domain_name=None,
            http2=None,
            owner_id=None):
        api_request = APIRequest('SetHttpsOptionConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "Http2": http2,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_l2_oss_key_config(
            self,
            security_token=None,
            domain_name=None,
            owner_id=None,
            private_oss_auth=None):
        api_request = APIRequest('SetL2OssKeyConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "PrivateOssAuth": private_oss_auth}
        return self._handle_request(api_request).result

    def describe_live_stream_bit_rate_data(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DescribeLiveStreamBitRateData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_domain_average_response_time(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_type=None,
            out_string=None,
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
            "OutString": out_string,
            "TimeMerge": time_merge,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def set_ip_black_list_config(
            self,
            security_token=None,
            domain_name=None,
            owner_id=None,
            block_ips=None):
        api_request = APIRequest('SetIpBlackListConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "BlockIps": block_ips}
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

    def set_remove_query_string_config(
            self,
            keep_oss_args=None,
            security_token=None,
            domain_name=None,
            ali_remove_args=None,
            owner_id=None):
        api_request = APIRequest('SetRemoveQueryStringConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "KeepOssArgs": keep_oss_args,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "AliRemoveArgs": ali_remove_args,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_user_customer_labels(self, uid=None, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeUserCustomerLabels', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Uid": uid, "SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_dynamic_config(
            self,
            dynamic_origin=None,
            static_type=None,
            security_token=None,
            static_uri=None,
            domain_name=None,
            static_path=None,
            dynamic_cache_control=None,
            owner_id=None):
        api_request = APIRequest('SetDynamicConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DynamicOrigin": dynamic_origin,
            "StaticType": static_type,
            "SecurityToken": security_token,
            "StaticUri": static_uri,
            "DomainName": domain_name,
            "StaticPath": static_path,
            "DynamicCacheControl": dynamic_cache_control,
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

    def describe_live_pull_stream_config(
            self,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeLivePullStreamConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domains_by_source(self, sources=None, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeDomainsBySource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Sources": sources,
            "SecurityToken": security_token,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_live_domain_mapping(
            self,
            pull_domain=None,
            security_token=None,
            push_domain=None,
            owner_id=None):
        api_request = APIRequest('DeleteLiveDomainMapping', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PullDomain": pull_domain,
            "SecurityToken": security_token,
            "PushDomain": push_domain,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_live_domain_mapping(
            self,
            pull_domain=None,
            security_token=None,
            push_domain=None,
            owner_id=None):
        api_request = APIRequest('AddLiveDomainMapping', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PullDomain": pull_domain,
            "SecurityToken": security_token,
            "PushDomain": push_domain,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_l2_vips_by_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeL2VipsByDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_http_error_page_config(
            self,
            security_token=None,
            domain_name=None,
            page_url=None,
            owner_id=None,
            error_code=None):
        api_request = APIRequest('SetHttpErrorPageConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "PageUrl": page_url,
            "OwnerId": owner_id,
            "ErrorCode": error_code}
        return self._handle_request(api_request).result

    def delete_specific_config(
            self,
            security_token=None,
            function_name=None,
            config_id=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteSpecificConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "FunctionName": function_name,
            "ConfigId": config_id,
            "DomainName": domain_name,
            "OwnerId": owner_id}
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

    def update_live_app_snapshot_config(
            self,
            time_interval=None,
            oss_bucket=None,
            app_name=None,
            security_token=None,
            domain_name=None,
            oss_endpoint=None,
            sequence_oss_object=None,
            overwrite_oss_object=None,
            owner_id=None):
        api_request = APIRequest('UpdateLiveAppSnapshotConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TimeInterval": time_interval,
            "OssBucket": oss_bucket,
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OssEndpoint": oss_endpoint,
            "SequenceOssObject": sequence_oss_object,
            "OverwriteOssObject": overwrite_oss_object,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_stream_snapshot_info(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            limit=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DescribeLiveStreamSnapshotInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "Limit": limit,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_live_snapshot_config(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            page_size=None,
            owner_id=None,
            page_num=None,
            stream_name=None,
            order=None):
        api_request = APIRequest('DescribeLiveSnapshotConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "StreamName": stream_name,
            "Order": order}
        return self._handle_request(api_request).result

    def delete_live_app_snapshot_config(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteLiveAppSnapshotConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_live_app_snapshot_config(
            self,
            time_interval=None,
            oss_bucket=None,
            app_name=None,
            security_token=None,
            domain_name=None,
            oss_endpoint=None,
            sequence_oss_object=None,
            overwrite_oss_object=None,
            owner_id=None):
        api_request = APIRequest('AddLiveAppSnapshotConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TimeInterval": time_interval,
            "OssBucket": oss_bucket,
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OssEndpoint": oss_endpoint,
            "SequenceOssObject": sequence_oss_object,
            "OverwriteOssObject": overwrite_oss_object,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_mix_streams_service(
            self,
            security_token=None,
            main_domain_name=None,
            mix_stream_name=None,
            mix_domain_name=None,
            owner_id=None,
            main_app_name=None,
            mix_app_name=None,
            main_stream_name=None):
        api_request = APIRequest('StopMixStreamsService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "MainDomainName": main_domain_name,
            "MixStreamName": mix_stream_name,
            "MixDomainName": mix_domain_name,
            "OwnerId": owner_id,
            "MainAppName": main_app_name,
            "MixAppName": mix_app_name,
            "MainStreamName": main_stream_name}
        return self._handle_request(api_request).result

    def start_mix_streams_service(
            self,
            mix_type=None,
            security_token=None,
            main_domain_name=None,
            mix_stream_name=None,
            mix_template=None,
            mix_domain_name=None,
            owner_id=None,
            main_app_name=None,
            mix_app_name=None,
            main_stream_name=None):
        api_request = APIRequest('StartMixStreamsService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MixType": mix_type,
            "SecurityToken": security_token,
            "MainDomainName": main_domain_name,
            "MixStreamName": mix_stream_name,
            "MixTemplate": mix_template,
            "MixDomainName": mix_domain_name,
            "OwnerId": owner_id,
            "MainAppName": main_app_name,
            "MixAppName": mix_app_name,
            "MainStreamName": main_stream_name}
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

    def describe_live_streams_frame_rate_and_bit_rate_data(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest(
            'DescribeLiveStreamsFrameRateAndBitRateData',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_live_stream_record_index_files(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DescribeLiveStreamRecordIndexFiles',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_live_stream_record_index_file(
            self,
            record_id=None,
            app_name=None,
            security_token=None,
            domain_name=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DescribeLiveStreamRecordIndexFile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RecordId": record_id,
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_live_stream_record_content(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DescribeLiveStreamRecordContent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_live_record_config(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeLiveRecordConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_live_app_record_config(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteLiveAppRecordConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_live_stream_record_index_files(
            self,
            oss_bucket=None,
            app_name=None,
            security_token=None,
            domain_name=None,
            oss_endpoint=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None,
            oss_object=None):
        api_request = APIRequest('CreateLiveStreamRecordIndexFiles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OssBucket": oss_bucket,
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OssEndpoint": oss_endpoint,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name,
            "OssObject": oss_object}
        return self._handle_request(api_request).result

    def add_live_app_record_config(
            self,
            oss_bucket=None,
            app_name=None,
            security_token=None,
            domain_name=None,
            oss_endpoint=None,
            oss_object_prefix=None,
            owner_id=None):
        api_request = APIRequest('AddLiveAppRecordConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OssBucket": oss_bucket,
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OssEndpoint": oss_endpoint,
            "OssObjectPrefix": oss_object_prefix,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_forward_scheme_config(
            self,
            scheme_origin=None,
            scheme_origin_port=None,
            security_token=None,
            enable=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('SetForwardSchemeConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SchemeOrigin": scheme_origin,
            "SchemeOriginPort": scheme_origin_port,
            "SecurityToken": security_token,
            "Enable": enable,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_user_configs(self, security_token=None, owner_id=None, config=None):
        api_request = APIRequest('DescribeUserConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "OwnerId": owner_id,
            "Config": config}
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

    def describe_cdn_region_and_isp(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeCdnRegionAndIsp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_stream_transcode_info(
            self,
            security_token=None,
            owner_id=None,
            domain_transcode_name=None):
        api_request = APIRequest('DescribeLiveStreamTranscodeInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "OwnerId": owner_id,
            "DomainTranscodeName": domain_transcode_name}
        return self._handle_request(api_request).result

    def delete_live_stream_transcode(
            self,
            template=None,
            app=None,
            security_token=None,
            owner_account=None,
            domain=None,
            owner_id=None):
        api_request = APIRequest('DeleteLiveStreamTranscode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Template": template,
            "App": app,
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "Domain": domain,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_live_stream_transcode(
            self,
            template=None,
            app=None,
            security_token=None,
            owner_account=None,
            domain=None,
            record=None,
            owner_id=None,
            snapshot=None):
        api_request = APIRequest('AddLiveStreamTranscode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Template": template,
            "App": app,
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "Domain": domain,
            "Record": record,
            "OwnerId": owner_id,
            "Snapshot": snapshot}
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

    def describe_cdn_types(self, security_token=None, owner_account=None, owner_id=None):
        api_request = APIRequest('DescribeCdnTypes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
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

    def modify_cdn_domain(
            self,
            top_level_domain=None,
            source_port=None,
            resource_group_id=None,
            priorities=None,
            sources=None,
            security_token=None,
            domain_name=None,
            source_type=None,
            owner_id=None):
        api_request = APIRequest('ModifyCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "SourcePort": source_port,
            "ResourceGroupId": resource_group_id,
            "Priorities": priorities,
            "Sources": sources,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "SourceType": source_type,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_video_seek_config(
            self,
            security_token=None,
            enable=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('SetVideoSeekConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "Enable": enable,
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

    def set_range_config(self, security_token=None, enable=None, domain_name=None, owner_id=None):
        api_request = APIRequest('SetRangeConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "Enable": enable,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_path_cache_expired_config(
            self,
            security_token=None,
            domain_name=None,
            weight=None,
            cache_content=None,
            owner_id=None,
            ttl=None):
        api_request = APIRequest('SetPathCacheExpiredConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "Weight": weight,
            "CacheContent": cache_content,
            "OwnerId": owner_id,
            "TTL": ttl}
        return self._handle_request(api_request).result

    def set_page_compress_config(
            self,
            security_token=None,
            enable=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('SetPageCompressConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "Enable": enable,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_optimize_config(
            self,
            security_token=None,
            enable=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('SetOptimizeConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "Enable": enable,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_ignore_query_string_config(
            self,
            keep_oss_args=None,
            hash_key_args=None,
            security_token=None,
            enable=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('SetIgnoreQueryStringConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "KeepOssArgs": keep_oss_args,
            "HashKeyArgs": hash_key_args,
            "SecurityToken": security_token,
            "Enable": enable,
            "DomainName": domain_name,
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

    def modify_path_cache_expired_config(
            self,
            security_token=None,
            config_id=None,
            domain_name=None,
            weight=None,
            cache_content=None,
            owner_id=None,
            ttl=None):
        api_request = APIRequest('ModifyPathCacheExpiredConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ConfigID": config_id,
            "DomainName": domain_name,
            "Weight": weight,
            "CacheContent": cache_content,
            "OwnerId": owner_id,
            "TTL": ttl}
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

    def describe_refresh_quota(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeRefreshQuota', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_ip_info(self, security_token=None, ip=None, owner_id=None):
        api_request = APIRequest('DescribeIpInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "IP": ip, "OwnerId": owner_id}
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

    def describe_domain_top_url_visit(
            self,
            security_token=None,
            domain_name=None,
            sort_by=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainTopUrlVisit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "SortBy": sort_by,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_top_refer_visit(
            self,
            security_token=None,
            domain_name=None,
            sort_by=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainTopReferVisit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "SortBy": sort_by,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_src_flow_data(
            self,
            start_time=None,
            fix_time_gap=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainSrcFlowData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "FixTimeGap": fix_time_gap,
            "TimeMerge": time_merge,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_domain_src_bps_data(
            self,
            start_time=None,
            fix_time_gap=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainSrcBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "FixTimeGap": fix_time_gap,
            "TimeMerge": time_merge,
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

    def describe_domain_qps_data(
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
        api_request = APIRequest('DescribeDomainQpsData', 'GET', 'http', 'RPC', 'query')
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

    def describe_domain_http_code_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            time_merge=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeDomainHttpCodeData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "TimeMerge": time_merge,
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

    def describe_domain_flow_data(
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
        api_request = APIRequest('DescribeDomainFlowData', 'GET', 'http', 'RPC', 'query')
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

    def describe_domain_configs(
            self,
            security_token=None,
            domain_name=None,
            config_list=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "ConfigList": config_list,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_cc_data(
            self,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainCCData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_cc_attack_info(
            self,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDomainCCAttackInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_domain_bps_data(
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
        api_request = APIRequest('DescribeDomainBpsData', 'GET', 'http', 'RPC', 'query')
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

    def delete_http_header_config(
            self,
            security_token=None,
            config_id=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteHttpHeaderConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ConfigID": config_id,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_cache_expired_config(
            self,
            cache_type=None,
            security_token=None,
            config_id=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteCacheExpiredConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CacheType": cache_type,
            "SecurityToken": security_token,
            "ConfigID": config_id,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_live_streams_notify_url_config(
            self,
            security_token=None,
            domain_name=None,
            notify_url=None,
            owner_id=None):
        api_request = APIRequest('SetLiveStreamsNotifyUrlConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "NotifyUrl": notify_url,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_stream_online_user_num(
            self,
            app_name=None,
            security_token=None,
            hls_switch=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DescribeLiveStreamOnlineUserNum', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "HlsSwitch": hls_switch,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def resume_live_stream(
            self,
            app_name=None,
            security_token=None,
            live_stream_type=None,
            domain_name=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('ResumeLiveStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "LiveStreamType": live_stream_type,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def forbid_live_stream(
            self,
            resume_time=None,
            app_name=None,
            security_token=None,
            live_stream_type=None,
            domain_name=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('ForbidLiveStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResumeTime": resume_time,
            "AppName": app_name,
            "SecurityToken": security_token,
            "LiveStreamType": live_stream_type,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_live_streams_publish_list(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            page_size=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None,
            page_number=None):
        api_request = APIRequest('DescribeLiveStreamsPublishList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_live_streams_online_list(
            self,
            stream_type=None,
            app_name=None,
            security_token=None,
            domain_name=None,
            page_size=None,
            owner_id=None,
            page_num=None):
        api_request = APIRequest('DescribeLiveStreamsOnlineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StreamType": stream_type,
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNum": page_num}
        return self._handle_request(api_request).result

    def describe_live_streams_control_history(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveStreamsControlHistory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_streams_block_list(
            self,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveStreamsBlockList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cdn_domain_logs(
            self,
            security_token=None,
            domain_name=None,
            page_size=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            log_day=None):
        api_request = APIRequest('DescribeCdnDomainLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "LogDay": log_day}
        return self._handle_request(api_request).result

    def describe_cdn_domain_detail(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeCdnDomainDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_cdn_domain(
            self,
            resource_group_id=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_cdn_domain(
            self,
            top_level_domain=None,
            sources=None,
            owner_account=None,
            domain_name=None,
            owner_id=None,
            resource_group_id=None,
            source_port=None,
            priorities=None,
            security_token=None,
            cdn_type=None,
            scope=None,
            source_type=None,
            check_url=None,
            region=None):
        api_request = APIRequest('AddCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "Sources": sources,
            "OwnerAccount": owner_account,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "ResourceGroupId": resource_group_id,
            "SourcePort": source_port,
            "Priorities": priorities,
            "SecurityToken": security_token,
            "CdnType": cdn_type,
            "Scope": scope,
            "SourceType": source_type,
            "CheckUrl": check_url,
            "Region": region}
        return self._handle_request(api_request).result

    def push_object_cache(self, area=None, security_token=None, object_path=None, owner_id=None):
        api_request = APIRequest('PushObjectCache', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Area": area,
            "SecurityToken": security_token,
            "ObjectPath": object_path,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def open_cdn_service(self, security_token=None, internet_charge_type=None, owner_id=None):
        api_request = APIRequest('OpenCdnService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "InternetChargeType": internet_charge_type,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_cdn_service(self, security_token=None, internet_charge_type=None, owner_id=None):
        api_request = APIRequest('ModifyCdnService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "InternetChargeType": internet_charge_type,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_user_domains(
            self,
            func_filter=None,
            sources=None,
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
            page_size=None):
        api_request = APIRequest('DescribeUserDomains', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FuncFilter": func_filter,
            "Sources": sources,
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
            "PageSize": page_size}
        return self._handle_request(api_request).result

    def describe_refresh_tasks(
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
        api_request = APIRequest('DescribeRefreshTasks', 'GET', 'http', 'RPC', 'query')
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

    def describe_cdn_service(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeCdnService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cdn_monitor_data(
            self,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeCdnMonitorData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def stop_cdn_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('StopCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_cdn_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('StartCdnDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
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
