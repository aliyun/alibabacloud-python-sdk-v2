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


class SasClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Sas'
        self.api_version = '2018-12-03'
        self.location_service_code = 'sas'
        self.location_endpoint_type = 'openAPI'

    def describe_property_count(self, source_ip=None, uuid_list=None, type_=None):
        api_request = APIRequest('DescribePropertyCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "UuidList": uuid_list, "Type": type_}
        return self._handle_request(api_request).result

    def describe_property_user_item(
            self,
            source_ip=None,
            page_size=None,
            current_page=None,
            user=None,
            force_flush=None):
        api_request = APIRequest('DescribePropertyUserItem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "User": user,
            "ForceFlush": force_flush}
        return self._handle_request(api_request).result

    def describe_property_user_detail(
            self,
            source_ip=None,
            page_size=None,
            remark=None,
            is_root=None,
            current_page=None,
            user=None,
            uuid=None):
        api_request = APIRequest('DescribePropertyUserDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "Remark": remark,
            "IsRoot": is_root,
            "CurrentPage": current_page,
            "User": user,
            "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_property_software_item(
            self,
            source_ip=None,
            name=None,
            page_size=None,
            current_page=None,
            force_flush=None):
        api_request = APIRequest('DescribePropertySoftwareItem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Name": name,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "ForceFlush": force_flush}
        return self._handle_request(api_request).result

    def describe_property_software_detail(
            self,
            path=None,
            source_ip=None,
            software_version=None,
            name=None,
            page_size=None,
            remark=None,
            current_page=None,
            uuid=None):
        api_request = APIRequest('DescribePropertySoftwareDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Path": path,
            "SourceIp": source_ip,
            "SoftwareVersion": software_version,
            "Name": name,
            "PageSize": page_size,
            "Remark": remark,
            "CurrentPage": current_page,
            "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_property_proc_item(
            self,
            source_ip=None,
            name=None,
            page_size=None,
            current_page=None,
            force_flush=None):
        api_request = APIRequest('DescribePropertyProcItem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Name": name,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "ForceFlush": force_flush}
        return self._handle_request(api_request).result

    def describe_property_proc_detail(
            self,
            cmdline=None,
            source_ip=None,
            name=None,
            page_size=None,
            remark=None,
            current_page=None,
            user=None,
            uuid=None):
        api_request = APIRequest('DescribePropertyProcDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Cmdline": cmdline,
            "SourceIp": source_ip,
            "Name": name,
            "PageSize": page_size,
            "Remark": remark,
            "CurrentPage": current_page,
            "User": user,
            "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_property_port_item(
            self,
            source_ip=None,
            port=None,
            page_size=None,
            current_page=None,
            force_flush=None):
        api_request = APIRequest('DescribePropertyPortItem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Port": port,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "ForceFlush": force_flush}
        return self._handle_request(api_request).result

    def describe_property_port_detail(
            self,
            source_ip=None,
            port=None,
            page_size=None,
            remark=None,
            current_page=None,
            proc_name=None,
            uuid=None):
        api_request = APIRequest('DescribePropertyPortDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Port": port,
            "PageSize": page_size,
            "Remark": remark,
            "CurrentPage": current_page,
            "ProcName": proc_name,
            "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_user_layout_authorization(self, resource_owner_id=None, source_ip=None, lang=None):
        api_request = APIRequest('DescribeUserLayoutAuthorization', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_cloud_product_field_statistics(self, source_ip=None):
        api_request = APIRequest('DescribeCloudProductFieldStatistics',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_domain_detail(self, source_ip=None, domain_name=None):
        api_request = APIRequest('DescribeDomainDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "DomainName": domain_name}
        return self._handle_request(api_request).result

    def describe_domain_list(
            self,
            source_ip=None,
            domain_type=None,
            page_size=None,
            current_page=None,
            fuzzy_domain=None):
        api_request = APIRequest('DescribeDomainList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "DomainType": domain_type,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "FuzzyDomain": fuzzy_domain}
        return self._handle_request(api_request).result

    def describe_domain_count(self, source_ip=None):
        api_request = APIRequest('DescribeDomainCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def modify_tag_with_uuid(
            self,
            source_ip=None,
            tag_id=None,
            uuid_list=None,
            machine_types=None,
            tag_list=None):
        api_request = APIRequest('ModifyTagWithUuid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "TagId": tag_id,
            "UuidList": uuid_list,
            "MachineTypes": machine_types,
            "TagList": tag_list}
        return self._handle_request(api_request).result

    def describe_grouped_tags(self, source_ip=None, machine_types=None):
        api_request = APIRequest('DescribeGroupedTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "MachineTypes": machine_types}
        return self._handle_request(api_request).result

    def describe_field_statistics(self, source_ip=None, machine_types=None):
        api_request = APIRequest('DescribeFieldStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "MachineTypes": machine_types}
        return self._handle_request(api_request).result

    def describe_instance_statistics(self, source_ip=None, from_=None, lang=None, uuid=None):
        api_request = APIRequest('DescribeInstanceStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_, "Lang": lang, "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_all_groups(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeAllGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def create_or_update_asset_group(
            self,
            source_ip=None,
            group_id=None,
            group_name=None,
            uuids=None):
        api_request = APIRequest('CreateOrUpdateAssetGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "GroupId": group_id,
            "GroupName": group_name,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def modify_group_property(self, source_ip=None, data=None):
        api_request = APIRequest('ModifyGroupProperty', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Data": data}
        return self._handle_request(api_request).result

    def delete_group(self, source_ip=None, group_id=None):
        api_request = APIRequest('DeleteGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "GroupId": group_id}
        return self._handle_request(api_request).result

    def describe_risk_check_item_result(
            self,
            item_id=None,
            resource_owner_id=None,
            source_ip=None,
            page_size=None,
            current_page=None,
            lang=None):
        api_request = APIRequest('DescribeRiskCheckItemResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ItemId": item_id,
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang}
        return self._handle_request(api_request).result

    def modify_push_all_task(self, source_ip=None, tasks=None, uuids=None):
        api_request = APIRequest('ModifyPushAllTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Tasks": tasks, "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_check_warning_detail(self, source_ip=None, lang=None, check_warning_id=None):
        api_request = APIRequest('DescribeCheckWarningDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Lang": lang,
            "CheckWarningId": check_warning_id}
        return self._handle_request(api_request).result

    def describe_check_warnings(
            self,
            source_ip=None,
            page_size=None,
            current_page=None,
            lang=None,
            risk_id=None,
            uuid=None):
        api_request = APIRequest('DescribeCheckWarnings', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang,
            "RiskId": risk_id,
            "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_warning_machines(
            self,
            source_ip=None,
            page_size=None,
            machine_name=None,
            strategy_id=None,
            current_page=None,
            lang=None,
            risk_id=None,
            uuids=None):
        api_request = APIRequest('DescribeWarningMachines', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "MachineName": machine_name,
            "StrategyId": strategy_id,
            "CurrentPage": current_page,
            "Lang": lang,
            "RiskId": risk_id,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_check_warning_summary(
            self,
            risk_name=None,
            source_ip=None,
            risk_status=None,
            page_size=None,
            strategy_id=None,
            current_page=None,
            lang=None,
            type_name=None,
            status=None,
            uuids=None):
        api_request = APIRequest('DescribeCheckWarningSummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RiskName": risk_name,
            "SourceIp": source_ip,
            "RiskStatus": risk_status,
            "PageSize": page_size,
            "StrategyId": strategy_id,
            "CurrentPage": current_page,
            "Lang": lang,
            "TypeName": type_name,
            "Status": status,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_stratety(self, source_ip=None, strategy_ids=None, lang=None):
        api_request = APIRequest('DescribeStratety', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "StrategyIds": strategy_ids, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_strategy_exec_detail(self, source_ip=None, strategy_id=None):
        api_request = APIRequest('DescribeStrategyExecDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "StrategyId": strategy_id}
        return self._handle_request(api_request).result

    def modify_operate_vul(
            self,
            reason=None,
            source_ip=None,
            operate_type=None,
            type_=None,
            info=None):
        api_request = APIRequest('ModifyOperateVul', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Reason": reason,
            "SourceIp": source_ip,
            "OperateType": operate_type,
            "Type": type_,
            "Info": info}
        return self._handle_request(api_request).result

    def modify_emg_vul_submit(self, source_ip=None, name=None, user_agreement=None, lang=None):
        api_request = APIRequest('ModifyEmgVulSubmit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Name": name,
            "UserAgreement": user_agreement,
            "Lang": lang}
        return self._handle_request(api_request).result

    def modify_delete_vul_whitelist(self, source_ip=None, whitelist=None):
        api_request = APIRequest('ModifyDeleteVulWhitelist', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Whitelist": whitelist}
        return self._handle_request(api_request).result

    def modify_concern_necessity(self, source_ip=None, lang=None, concern_necessity=None):
        api_request = APIRequest('ModifyConcernNecessity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Lang": lang,
            "ConcernNecessity": concern_necessity}
        return self._handle_request(api_request).result

    def modify_auto_del_config(self, source_ip=None, days=None):
        api_request = APIRequest('ModifyAutoDelConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Days": days}
        return self._handle_request(api_request).result

    def describe_vul_whitelist(self, source_ip=None, page_size=None, current_page=None):
        api_request = APIRequest('DescribeVulWhitelist', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page}
        return self._handle_request(api_request).result

    def describe_vul_list(
            self,
            alias_name=None,
            source_ip=None,
            page_size=None,
            remark=None,
            dealed=None,
            current_page=None,
            lang=None,
            type_=None,
            necessity=None,
            uuids=None):
        api_request = APIRequest('DescribeVulList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AliasName": alias_name,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "Remark": remark,
            "Dealed": dealed,
            "CurrentPage": current_page,
            "Lang": lang,
            "Type": type_,
            "Necessity": necessity,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_vul_details(
            self,
            alias_name=None,
            source_ip=None,
            name=None,
            lang=None,
            type_=None):
        api_request = APIRequest('DescribeVulDetails', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AliasName": alias_name,
            "SourceIp": source_ip,
            "Name": name,
            "Lang": lang,
            "Type": type_}
        return self._handle_request(api_request).result

    def describe_grouped_vul(
            self,
            alias_name=None,
            source_ip=None,
            page_size=None,
            dealed=None,
            current_page=None,
            lang=None,
            type_=None,
            necessity=None,
            uuids=None):
        api_request = APIRequest('DescribeGroupedVul', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AliasName": alias_name,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "Dealed": dealed,
            "CurrentPage": current_page,
            "Lang": lang,
            "Type": type_,
            "Necessity": necessity,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_emg_vul_group(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeEmgVulGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_concern_necessity(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeConcernNecessity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_auto_del_config(self, source_ip=None):
        api_request = APIRequest('DescribeAutoDelConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def modify_create_vul_whitelist(self, reason=None, source_ip=None, whitelist=None):
        api_request = APIRequest('ModifyCreateVulWhitelist', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Reason": reason, "SourceIp": source_ip, "Whitelist": whitelist}
        return self._handle_request(api_request).result

    def start_baseline_security_check(
            self,
            resource_owner_id=None,
            list_of_assets=None,
            source_ip=None,
            list_of_item_ids=None,
            lang=None,
            type_=None):
        api_request = APIRequest('StartBaselineSecurityCheck', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Assets": list_of_assets,
            "SourceIp": source_ip,
            "ItemIds": list_of_item_ids,
            "Lang": lang,
            "Type": type_}
        repeat_info = {"Assets": ('Assets', 'list', 'str', None),
                       "ItemIds": ('ItemIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_security_check_schedule_config(
            self,
            resource_owner_id=None,
            source_ip=None,
            days_of_week=None,
            end_time=None,
            start_time=None,
            lang=None):
        api_request = APIRequest('ModifySecurityCheckScheduleConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "DaysOfWeek": days_of_week,
            "EndTime": end_time,
            "StartTime": start_time,
            "Lang": lang}
        return self._handle_request(api_request).result

    def modify_risk_single_result_status(
            self,
            resource_owner_id=None,
            source_ip=None,
            list_of_ids=None,
            lang=None,
            task_id=None,
            status=None):
        api_request = APIRequest('ModifyRiskSingleResultStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "Ids": list_of_ids,
            "Lang": lang,
            "TaskId": task_id,
            "Status": status}
        repeat_info = {"Ids": ('Ids', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_risk_check_status(
            self,
            item_id=None,
            resource_owner_id=None,
            source_ip=None,
            lang=None,
            task_id=None,
            status=None):
        api_request = APIRequest('ModifyRiskCheckStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ItemId": item_id,
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "Lang": lang,
            "TaskId": task_id,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_user_baseline_authorization(
            self, resource_owner_id=None, source_ip=None, lang=None):
        api_request = APIRequest('DescribeUserBaselineAuthorization', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_security_check_schedule_config(
            self, resource_owner_id=None, source_ip=None, lang=None):
        api_request = APIRequest('DescribeSecurityCheckScheduleConfig',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_risk_item_type(self, resource_owner_id=None, source_ip=None, lang=None):
        api_request = APIRequest('DescribeRiskItemType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_risk_check_summary(self, resource_owner_id=None, source_ip=None, lang=None):
        api_request = APIRequest('DescribeRiskCheckSummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_risk_check_result(
            self,
            resource_owner_id=None,
            source_ip=None,
            group_id=None,
            list_of_item_ids=None,
            name=None,
            page_size=None,
            current_page=None,
            lang=None,
            risk_level=None,
            status=None):
        api_request = APIRequest('DescribeRiskCheckResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "GroupId": group_id,
            "ItemIds": list_of_item_ids,
            "Name": name,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang,
            "RiskLevel": risk_level,
            "Status": status}
        repeat_info = {"ItemIds": ('ItemIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_susp_events(
            self,
            alarm_unique_info=None,
            source_ip=None,
            name=None,
            page_size=None,
            dealed=None,
            remark=None,
            current_page=None,
            from_=None,
            lang=None,
            levels=None,
            parent_event_types=None):
        api_request = APIRequest('DescribeSuspEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AlarmUniqueInfo": alarm_unique_info,
            "SourceIp": source_ip,
            "Name": name,
            "PageSize": page_size,
            "Dealed": dealed,
            "Remark": remark,
            "CurrentPage": current_page,
            "From": from_,
            "Lang": lang,
            "Levels": levels,
            "ParentEventTypes": parent_event_types}
        return self._handle_request(api_request).result

    def describe_susp_event_detail(
            self,
            suspicious_event_id=None,
            source_ip=None,
            from_=None,
            lang=None):
        api_request = APIRequest('DescribeSuspEventDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SuspiciousEventId": suspicious_event_id,
            "SourceIp": source_ip,
            "From": from_,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_alarm_event_list(
            self,
            alarm_event_name=None,
            source_ip=None,
            page_size=None,
            alarm_event_type=None,
            dealed=None,
            from_=None,
            remark=None,
            current_page=None,
            lang=None,
            levels=None):
        api_request = APIRequest('DescribeAlarmEventList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AlarmEventName": alarm_event_name,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "AlarmEventType": alarm_event_type,
            "Dealed": dealed,
            "From": from_,
            "Remark": remark,
            "CurrentPage": current_page,
            "Lang": lang,
            "Levels": levels}
        return self._handle_request(api_request).result

    def describe_alarm_event_detail(
            self,
            alarm_unique_info=None,
            source_ip=None,
            from_=None,
            lang=None):
        api_request = APIRequest('DescribeAlarmEventDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AlarmUniqueInfo": alarm_unique_info,
            "SourceIp": source_ip,
            "From": from_,
            "Lang": lang}
        return self._handle_request(api_request).result
