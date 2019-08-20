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


class JarvisClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'jarvis'
        self.api_version = '2018-02-06'
        self.location_service_code = 'jarvis'
        self.location_endpoint_type = 'openAPI'

    def modify_ip_white_baseline(
            self,
            resource_owner_id=None,
            src_ip=None,
            source_ip=None,
            remark=None,
            id_=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('ModifyIpWhiteBaseline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SrcIp": src_ip,
            "SourceIp": source_ip,
            "Remark": remark,
            "Id": id_,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_ip_white_baseline(
            self,
            src_ip=None,
            source_ip=None,
            page_size=None,
            current_page=None,
            remark=None,
            lang=None,
            source_code=None,
            status=None):
        api_request = APIRequest('DescribeIpWhiteBaseline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcIp": src_ip,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Remark": remark,
            "Lang": lang,
            "SourceCode": source_code,
            "Status": status}
        return self._handle_request(api_request).result

    def delete_ip_white_baseline(
            self,
            resource_owner_id=None,
            source_ip=None,
            wbl_ip_list=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('DeleteIpWhiteBaseline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "WblIpList": wbl_ip_list,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def create_ip_white_baseline(
            self,
            resource_owner_id=None,
            src_ip=None,
            source_ip=None,
            remark=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('CreateIpWhiteBaseline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SrcIp": src_ip,
            "SourceIp": source_ip,
            "Remark": remark,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def modify_uid_white_baseline(
            self,
            resource_owner_id=None,
            source_ip=None,
            remark=None,
            id_=None,
            lang=None,
            src_uid=None,
            source_code=None):
        api_request = APIRequest('ModifyUidWhiteBaseline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "Remark": remark,
            "Id": id_,
            "Lang": lang,
            "SrcUid": src_uid,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_uid_white_baseline(
            self,
            source_ip=None,
            page_size=None,
            current_page=None,
            remark=None,
            lang=None,
            src_uid=None,
            source_code=None,
            status=None):
        api_request = APIRequest('DescribeUidWhiteBaseline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Remark": remark,
            "Lang": lang,
            "SrcUid": src_uid,
            "SourceCode": source_code,
            "Status": status}
        return self._handle_request(api_request).result

    def delete_uid_white_baseline(
            self,
            resource_owner_id=None,
            wbl_uid_list=None,
            source_ip=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('DeleteUidWhiteBaseline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "WblUidList": wbl_uid_list,
            "SourceIp": source_ip,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def create_uid_white_baseline(
            self,
            resource_owner_id=None,
            source_ip=None,
            remark=None,
            lang=None,
            src_uid=None,
            source_code=None):
        api_request = APIRequest('CreateUidWhiteBaseline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "Remark": remark,
            "Lang": lang,
            "SrcUid": src_uid,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def delete_white_list_db_item_conditional(
            self,
            src_ip=None,
            source_ip=None,
            query_product=None,
            dst_ip=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('DeleteWhiteListDbItemConditional', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcIP": src_ip,
            "SourceIp": source_ip,
            "queryProduct": query_product,
            "DstIP": dst_ip,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def delete_white_list_conditional(
            self,
            src_ip=None,
            source_ip=None,
            query_product=None,
            dst_ip=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('DeleteWhiteListConditional', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcIP": src_ip,
            "SourceIp": source_ip,
            "queryProduct": query_product,
            "DstIP": dst_ip,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_cdn_certify(self, source_ip=None, lang=None, source_code=None):
        api_request = APIRequest('DescribeCdnCertify', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "SourceCode": source_code}
        return self._handle_request(api_request).result

    def create_all_ecs_white_list(
            self,
            resource_owner_id=None,
            src_ip=None,
            source_ip=None,
            source_code=None):
        api_request = APIRequest('CreateAllEcsWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SrcIP": src_ip,
            "SourceIp": source_ip,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_special_ecs(self, target_ip=None, source_ip=None, lang=None, source_code=None):
        api_request = APIRequest('DescribeSpecialEcs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TargetIp": target_ip,
            "SourceIp": source_ip,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_ecs_list_page(
            self,
            source_ip=None,
            page_size=None,
            current_page=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('DescribeEcsListPage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_console_access_white_list(
            self,
            src_ip=None,
            source_ip=None,
            page_size=None,
            query_product=None,
            current_page=None,
            white_list_type=None,
            dst_ip=None,
            lang=None,
            status=None,
            source_code=None):
        api_request = APIRequest('DescribeConsoleAccessWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcIP": src_ip,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "queryProduct": query_product,
            "CurrentPage": current_page,
            "WhiteListType": white_list_type,
            "DstIP": dst_ip,
            "Lang": lang,
            "Status": status,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def create_console_access_white_list(
            self,
            note=None,
            resource_owner_id=None,
            src_ip=None,
            source_ip=None,
            dst_port=None,
            instance_id_list=None,
            live_time=None,
            product_name=None,
            white_list_type=None,
            instance_info_list=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('CreateConsoleAccessWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Note": note,
            "ResourceOwnerId": resource_owner_id,
            "SrcIP": src_ip,
            "SourceIp": source_ip,
            "DstPort": dst_port,
            "InstanceIdList": instance_id_list,
            "LiveTime": live_time,
            "ProductName": product_name,
            "WhiteListType": white_list_type,
            "InstanceInfoList": instance_info_list,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def delete_console_access_white_list(
            self,
            source_ip=None,
            lang=None,
            disable_whitelist=None,
            source_code=None):
        api_request = APIRequest('DeleteConsoleAccessWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Lang": lang,
            "DisableWhitelist": disable_whitelist,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def delete_cdn_ip(
            self,
            item_id=None,
            resource_owner_id=None,
            source_ip=None,
            cdn_ip=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('DeleteCdnIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ItemId": item_id,
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "CdnIp": cdn_ip,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def create_cdn_ip(
            self,
            cdn_ip_list=None,
            resource_owner_id=None,
            source_ip=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('CreateCdnIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CdnIpList": cdn_ip_list,
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_cdn_ip_list(
            self,
            src_ip=None,
            source_ip=None,
            wl_state=None,
            page_size=None,
            current_page=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('DescribeCdnIpList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcIP": src_ip,
            "SourceIp": source_ip,
            "WlState": wl_state,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def delete_cdn_subscription(
            self,
            source_ip=None,
            lang=None,
            cdn_uid_list=None,
            source_code=None):
        api_request = APIRequest('DeleteCdnSubscription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Lang": lang,
            "CdnUidList": cdn_uid_list,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def create_cdn_subscription(
            self,
            resource_owner_id=None,
            source_ip=None,
            lang=None,
            cdn_uid_list=None,
            source_code=None):
        api_request = APIRequest('CreateCdnSubscription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "Lang": lang,
            "CdnUidList": cdn_uid_list,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_cdn_subscription(
            self,
            source_ip=None,
            subscription_state=None,
            page_size=None,
            current_page=None,
            lang=None,
            vendor_name=None,
            source_code=None):
        api_request = APIRequest('DescribeCdnSubscription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "SubscriptionState": subscription_state,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang,
            "VendorName": vendor_name,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_cdn_vendor(
            self,
            source_ip=None,
            page_size=None,
            current_page=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('DescribeCdnVendor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_access_white_list_slb_list(self, source_ip=None, lang=None, source_code=None):
        api_request = APIRequest('DescribeAccessWhiteListSlbList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_access_white_list_eip_list(self, source_ip=None, lang=None, source_code=None):
        api_request = APIRequest('DescribeAccessWhiteListEipList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_punish_list(
            self,
            src_ip=None,
            source_ip=None,
            page_size=None,
            current_page=None,
            punish_status=None,
            lang=None,
            src_uid=None,
            source_code=None):
        api_request = APIRequest('DescribePunishList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcIP": src_ip,
            "SourceIp": source_ip,
            "pageSize": page_size,
            "currentPage": current_page,
            "PunishStatus": punish_status,
            "Lang": lang,
            "srcUid": src_uid,
            "sourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_risk_list_detail(
            self,
            risk_type=None,
            source_ip=None,
            page_size=None,
            query_product=None,
            current_page=None,
            risk_describe=None,
            lang=None,
            src_uid=None,
            source_code=None,
            query_region_id=None,
            status=None):
        api_request = APIRequest('DescribeRiskListDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "riskType": risk_type,
            "SourceIp": source_ip,
            "pageSize": page_size,
            "queryProduct": query_product,
            "currentPage": current_page,
            "riskDescribe": risk_describe,
            "Lang": lang,
            "srcUid": src_uid,
            "sourceCode": source_code,
            "queryRegionId": query_region_id,
            "status": status}
        return self._handle_request(api_request).result

    def describe_ddos_defense_info(self, source_ip=None, lang=None, src_uid=None, source_code=None):
        api_request = APIRequest('DescribeDdosDefenseInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Lang": lang,
            "srcUid": src_uid,
            "sourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_phone_info(self, source_ip=None, phone_num=None, lang=None, source_code=None):
        api_request = APIRequest('DescribePhoneInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "phoneNum": phone_num,
            "Lang": lang,
            "sourceCode": source_code}
        return self._handle_request(api_request).result

    def delete_uid_white_list_group(
            self,
            group_id_list=None,
            source_ip=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('DeleteUidWhiteListGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GroupIdList": group_id_list,
            "SourceIp": source_ip,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def modify_uid_white_list_auto_share(
            self,
            source_ip=None,
            auto_config=None,
            product_name=None,
            white_list_type=None,
            lang=None,
            src_uid=None,
            source_code=None):
        api_request = APIRequest('ModifyUidWhiteListAutoShare', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "AutoConfig": auto_config,
            "ProductName": product_name,
            "WhiteListType": white_list_type,
            "Lang": lang,
            "SrcUid": src_uid,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def create_uid_white_list_group(
            self,
            note=None,
            resource_owner_id=None,
            source_ip=None,
            dst_port=None,
            instance_id_list=None,
            live_time=None,
            product_name=None,
            white_list_type=None,
            lang=None,
            src_uid=None,
            source_code=None):
        api_request = APIRequest('CreateUidWhiteListGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Note": note,
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "DstPort": dst_port,
            "InstanceIdList": instance_id_list,
            "LiveTime": live_time,
            "ProductName": product_name,
            "WhiteListType": white_list_type,
            "Lang": lang,
            "SrcUid": src_uid,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_uid_white_list_group(
            self,
            source_ip=None,
            page_size=None,
            current_page=None,
            white_list_type=None,
            dst_ip=None,
            lang=None,
            src_uid=None,
            status=None,
            source_code=None):
        api_request = APIRequest('DescribeUidWhiteListGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "WhiteListType": white_list_type,
            "DstIP": dst_ip,
            "Lang": lang,
            "SrcUid": src_uid,
            "Status": status,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_risk_trend(
            self,
            source_ip=None,
            query_product=None,
            lang=None,
            peroid=None,
            source_code=None,
            query_region_id=None):
        api_request = APIRequest('DescribeRiskTrend', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "QueryProduct": query_product,
            "Lang": lang,
            "Peroid": peroid,
            "SourceCode": source_code,
            "QueryRegionId": query_region_id}
        return self._handle_request(api_request).result

    def modify_access_white_list_auto_share(
            self,
            src_ip=None,
            source_ip=None,
            auto_config=None,
            product_name=None,
            white_list_type=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('ModifyAccessWhiteListAutoShare', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcIP": src_ip,
            "SourceIp": source_ip,
            "AutoConfig": auto_config,
            "ProductName": product_name,
            "WhiteListType": white_list_type,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_uid_gc_level(self, source_ip=None, lang=None, source_code=None):
        api_request = APIRequest('DescribeUidGcLevel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_reset_record_query_count(self, source_ip=None, lang=None, source_code=None):
        api_request = APIRequest('DescribeResetRecordQueryCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_reset_record_list(
            self,
            src_ip=None,
            period=None,
            source_ip=None,
            page_size=None,
            current_page=None,
            dst_ip=None,
            region=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('DescribeResetRecordList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcIP": src_ip,
            "Period": period,
            "SourceIp": source_ip,
            "pageSize": page_size,
            "currentPage": current_page,
            "DstIP": dst_ip,
            "Region": region,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_cpmc_punish_list(
            self,
            src_ip=None,
            source_ip=None,
            page_size=None,
            punish_type=None,
            current_page=None,
            punish_status=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('DescribeCpmcPunishList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcIP": src_ip,
            "SourceIp": source_ip,
            "pageSize": page_size,
            "PunishType": punish_type,
            "currentPage": current_page,
            "PunishStatus": punish_status,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_access_white_list_group(
            self,
            src_ip=None,
            source_ip=None,
            page_size=None,
            query_product=None,
            current_page=None,
            white_list_type=None,
            dst_ip=None,
            lang=None,
            status=None,
            source_code=None):
        api_request = APIRequest('DescribeAccessWhiteListGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcIP": src_ip,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "queryProduct": query_product,
            "CurrentPage": current_page,
            "WhiteListType": white_list_type,
            "DstIP": dst_ip,
            "Lang": lang,
            "Status": status,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def describe_access_whitelist_ecs_list(self, source_ip=None, lang=None, source_code=None):
        api_request = APIRequest('DescribeAccessWhitelistEcsList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "SourceCode": source_code}
        return self._handle_request(api_request).result

    def delete_access_white_list_group(
            self,
            group_id_list=None,
            source_ip=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('DeleteAccessWhiteListGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GroupIdList": group_id_list,
            "SourceIp": source_ip,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def create_cpmc_punish_feed_back(
            self,
            feed_back=None,
            src_ip=None,
            source_ip=None,
            dst_port=None,
            protocol_name=None,
            src_port=None,
            punish_type=None,
            gmt_create=None,
            dst_ip=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('CreateCpmcPunishFeedBack', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FeedBack": feed_back,
            "SrcIP": src_ip,
            "SourceIp": source_ip,
            "DstPort": dst_port,
            "ProtocolName": protocol_name,
            "SrcPort": src_port,
            "PunishType": punish_type,
            "GmtCreate": gmt_create,
            "DstIP": dst_ip,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result

    def create_access_white_list_group(
            self,
            note=None,
            resource_owner_id=None,
            src_ip=None,
            source_ip=None,
            dst_port=None,
            instance_id_list=None,
            live_time=None,
            product_name=None,
            white_list_type=None,
            instance_info_list=None,
            lang=None,
            source_code=None):
        api_request = APIRequest('CreateAccessWhiteListGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Note": note,
            "ResourceOwnerId": resource_owner_id,
            "SrcIP": src_ip,
            "SourceIp": source_ip,
            "DstPort": dst_port,
            "InstanceIdList": instance_id_list,
            "LiveTime": live_time,
            "ProductName": product_name,
            "WhiteListType": white_list_type,
            "InstanceInfoList": instance_info_list,
            "Lang": lang,
            "SourceCode": source_code}
        return self._handle_request(api_request).result
