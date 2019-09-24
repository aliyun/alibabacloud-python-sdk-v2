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


class AegisClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'aegis'
        self.api_version = '2016-11-11'
        self.location_service_code = 'vipaegis'
        self.location_endpoint_type = 'openAPI'

    def describe_accesskey_run_info(self, source_ip=None):
        api_request = APIRequest('DescribeAccesskeyRunInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def modify_access_key_leak_inst_run(self, source_ip=None):
        api_request = APIRequest('ModifyAccessKeyLeakInstRun', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def modify_access_key_leak_deal(self, source_ip=None, remark=None, id_=None, type_=None):
        api_request = APIRequest('ModifyAccessKeyLeakDeal', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Remark": remark, "Id": id_, "Type": type_}
        return self._handle_request(api_request).result

    def describe_access_key_leak_detail(self, source_ip=None, id_=None):
        api_request = APIRequest('DescribeAccessKeyLeakDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Id": id_}
        return self._handle_request(api_request).result

    def describe_accesskey_leak_list(
            self,
            source_ip=None,
            query=None,
            page_size=None,
            start_ts=None,
            current_page=None,
            status=None):
        api_request = APIRequest('DescribeAccesskeyLeakList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Query": query,
            "PageSize": page_size,
            "StartTs": start_ts,
            "CurrentPage": current_page,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_check_warning_count(
            self,
            source_ip=None,
            lang=None,
            risk_id=None,
            check_id=None,
            status=None):
        api_request = APIRequest('DescribeCheckWarningCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Lang": lang,
            "RiskId": risk_id,
            "CheckId": check_id,
            "Status": status}
        return self._handle_request(api_request).result

    def send_customize_report(self, source_ip=None, report_id=None, lang=None):
        api_request = APIRequest('SendCustomizeReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "ReportId": report_id, "Lang": lang}
        return self._handle_request(api_request).result

    def copy_customize_report_config(self, source_ip=None, report_id=None, lang=None):
        api_request = APIRequest('CopyCustomizeReportConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "ReportId": report_id, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_chart_data(
            self,
            time_end=None,
            range_unit=None,
            source_ip=None,
            char_id=None,
            lang=None,
            time_start=None):
        api_request = APIRequest('DescribeChartData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TimeEnd": time_end,
            "RangeUnit": range_unit,
            "SourceIp": source_ip,
            "CharId": char_id,
            "Lang": lang,
            "TimeStart": time_start}
        return self._handle_request(api_request).result

    def describe_chart_list(self, source_ip=None, project_code=None, lang=None):
        api_request = APIRequest('DescribeChartList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "ProjectCode": project_code, "Lang": lang}
        return self._handle_request(api_request).result

    def update_customize_report_status(
            self,
            source_ip=None,
            report_id=None,
            lang=None,
            report_status=None):
        api_request = APIRequest('UpdateCustomizeReportStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ReportId": report_id,
            "Lang": lang,
            "ReportStatus": report_status}
        return self._handle_request(api_request).result

    def save_customize_report_config(
            self,
            report_send_type=None,
            report_type=None,
            source_ip=None,
            report_id=None,
            report_end_date=None,
            report_start_date=None,
            recipients=None,
            report_lang=None,
            lang=None,
            title=None,
            send_time=None,
            report_status=None):
        api_request = APIRequest('SaveCustomizeReportConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ReportSendType": report_send_type,
            "ReportType": report_type,
            "SourceIp": source_ip,
            "ReportId": report_id,
            "ReportEndDate": report_end_date,
            "ReportStartDate": report_start_date,
            "Recipients": recipients,
            "ReportLang": report_lang,
            "Lang": lang,
            "Title": title,
            "SendTime": send_time,
            "ReportStatus": report_status}
        return self._handle_request(api_request).result

    def operation_customize_report_chart(
            self,
            source_ip=None,
            report_id=None,
            chart_ids=None,
            lang=None):
        api_request = APIRequest('OperationCustomizeReportChart', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ReportId": report_id,
            "ChartIds": chart_ids,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_customize_report_list(
            self,
            report_type=None,
            source_ip=None,
            lang=None,
            report_status=None,
            title=None):
        api_request = APIRequest('DescribeCustomizeReportList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ReportType": report_type,
            "SourceIp": source_ip,
            "Lang": lang,
            "ReportStatus": report_status,
            "Title": title}
        return self._handle_request(api_request).result

    def describe_customize_report_config_detail(self, source_ip=None, report_id=None, lang=None):
        api_request = APIRequest('DescribeCustomizeReportConfigDetail',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "ReportId": report_id, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_customize_report_chart_list(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeCustomizeReportChartList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_customize_report_chart_data(
            self,
            source_ip=None,
            report_id=None,
            chart_ids=None,
            lang=None):
        api_request = APIRequest('DescribeCustomizeReportChartData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ReportId": report_id,
            "ChartIds": chart_ids,
            "Lang": lang}
        return self._handle_request(api_request).result

    def delete_customize_report(self, source_ip=None, report_id=None, lang=None):
        api_request = APIRequest('DeleteCustomizeReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "ReportId": report_id, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_supervison_info(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeSupervisonInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_webshell_list(
            self,
            source_ip=None,
            group_id=None,
            page_size=None,
            current_page=None,
            dealed=None,
            remark=None,
            tag=None,
            status=None):
        api_request = APIRequest('DescribeWebshellList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "GroupId": group_id,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Dealed": dealed,
            "Remark": remark,
            "Tag": tag,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_vul_statistics(
            self,
            end_modify_time_patch=None,
            remark_patch=None,
            source_ip=None,
            end_find_time_patch=None,
            start_modify_time_patch=None,
            start_find_time_patch=None,
            from_=None,
            distribution=None,
            uuid=None):
        api_request = APIRequest('DescribeVulStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndModifyTimePatch": end_modify_time_patch,
            "RemarkPatch": remark_patch,
            "SourceIp": source_ip,
            "EndFindTimePatch": end_find_time_patch,
            "StartModifyTimePatch": start_modify_time_patch,
            "StartFindTimePatch": start_find_time_patch,
            "From": from_,
            "Distribution": distribution,
            "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_host_statistics(self, source_ip=None, from_=None):
        api_request = APIRequest('DescribeHostStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_}
        return self._handle_request(api_request).result

    def describe_entity_list(
            self,
            os=None,
            tag_id_list=None,
            group_id=None,
            health=None,
            current_page=None,
            remark=None,
            trojan=None,
            suspicious=None,
            region_no=None,
            patch=None,
            source_ip=None,
            page_size=None,
            from_=None,
            account=None,
            status=None):
        api_request = APIRequest('DescribeEntityList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Os": os,
            "TagIdList": tag_id_list,
            "GroupId": group_id,
            "Health": health,
            "CurrentPage": current_page,
            "Remark": remark,
            "Trojan": trojan,
            "Suspicious": suspicious,
            "RegionNo": region_no,
            "Patch": patch,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "From": from_,
            "Account": account,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_latest_actions(
            self,
            source_ip=None,
            page_size=None,
            from_=None,
            current_page=None,
            secure_token=None):
        api_request = APIRequest('DescribeLatestActions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "From": from_,
            "CurrentPage": current_page,
            "SecureToken": secure_token}
        return self._handle_request(api_request).result

    def add_event_process(
            self,
            source_ip=None,
            warning_type=None,
            suspicious_event_ids=None,
            from_=None,
            lang=None):
        api_request = APIRequest('AddEventProcess', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "WarningType": warning_type,
            "SuspiciousEventIds": suspicious_event_ids,
            "From": from_,
            "Lang": lang}
        return self._handle_request(api_request).result

    def delete_susp_event_node(self, source_ip=None, note_id=None):
        api_request = APIRequest('DeleteSuspEventNode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "NoteId": note_id}
        return self._handle_request(api_request).result

    def create_susp_event_note(self, event_id=None, note=None, source_ip=None):
        api_request = APIRequest('CreateSuspEventNote', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"EventId": event_id, "Note": note, "SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_screen_cloud_hc_risk(self, source_ip=None):
        api_request = APIRequest('DescribeScreenCloudHcRisk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_screen_top_request_and_flow(self, source_ip=None):
        api_request = APIRequest('DescribeScreenTopRequestAndFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_screen_emer_risk(self, source_ip=None):
        api_request = APIRequest('DescribeScreenEmerRisk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_screen_biz_stat_simple_query_result(
            self,
            range_unit=None,
            source_ip=None,
            end_time=None,
            start_time=None,
            custom_query=None,
            range_value=None):
        api_request = APIRequest('DescribeScreenBizStatSimpleQueryResult',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RangeUnit": range_unit,
            "SourceIp": source_ip,
            "EndTime": end_time,
            "StartTime": start_time,
            "CustomQuery": custom_query,
            "RangeValue": range_value}
        return self._handle_request(api_request).result

    def describe_screen_city_monitor_data(self, screen_id=None, date_type=None, source_ip=None):
        api_request = APIRequest('DescribeScreenCityMonitorData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ScreenId": screen_id, "DateType": date_type, "SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_biz_stat_simple_query_result(
            self,
            source_ip=None,
            end_time=None,
            start_time=None,
            custom_time_range=None,
            custom_query=None):
        api_request = APIRequest('DescribeBizStatSimpleQueryResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "EndTime": end_time,
            "StartTime": start_time,
            "CustomTimeRange": custom_time_range,
            "CustomQuery": custom_query}
        return self._handle_request(api_request).result

    def describe_screen_request_top_type(self, source_ip=None, type_=None):
        api_request = APIRequest('DescribeScreenRequestTopType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Type": type_}
        return self._handle_request(api_request).result

    def describe_screen_flow_request_count(self, source_ip=None):
        api_request = APIRequest('DescribeScreenFlowRequestCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_screen_oss_upload_info(self, source_ip=None):
        api_request = APIRequest('DescribeScreenOssUploadInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_screen_data_map(self, source_ip=None):
        api_request = APIRequest('DescribeScreenDataMap', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_screen_titles(self, source_ip=None):
        api_request = APIRequest('DescribeScreenTitles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def create_screen_setting(
            self,
            screen_data_map=None,
            screen_default=None,
            logo_power=None,
            monitor_url=None,
            source_ip=None,
            id_=None,
            title=None,
            logo_url=None):
        api_request = APIRequest('CreateScreenSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ScreenDataMap": screen_data_map,
            "ScreenDefault": screen_default,
            "LogoPower": logo_power,
            "MonitorUrl": monitor_url,
            "SourceIp": source_ip,
            "Id": id_,
            "Title": title,
            "LogoUrl": logo_url}
        return self._handle_request(api_request).result

    def describe_gray_func(self, condition=None, source_ip=None):
        api_request = APIRequest('DescribeGrayFunc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Condition": condition, "SourceIp": source_ip}
        return self._handle_request(api_request).result

    def modify_refresh_process_info(self, source_ip=None, uuid=None):
        api_request = APIRequest('ModifyRefreshProcessInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_vul_related_process(self, source_ip=None, id_=None, ppid=None):
        api_request = APIRequest('DescribeVulRelatedProcess', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Id": id_, "Ppid": ppid}
        return self._handle_request(api_request).result

    def update_white_list_strategy_relation(
            self,
            source_ip=None,
            process_method=None,
            strategy_id=None,
            lang=None,
            type_=None,
            uuid=None,
            status=None):
        api_request = APIRequest('UpdateWhiteListStrategyRelation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ProcessMethod": process_method,
            "StrategyId": strategy_id,
            "Lang": lang,
            "Type": type_,
            "Uuid": uuid,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_white_list_strategy_uuid_count(
            self, source_ip=None, strategy_id=None, lang=None, type_=None):
        api_request = APIRequest('DescribeWhiteListStrategyUuidCount',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "StrategyId": strategy_id,
            "Lang": lang,
            "Type": type_}
        return self._handle_request(api_request).result

    def describe_white_list_strategy_list(self, source_ip=None, strategy_ids=None, lang=None):
        api_request = APIRequest('DescribeWhiteListStrategyList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "StrategyIds": strategy_ids, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_white_list_strategy_count(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeWhiteListStrategyCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_white_list_effective_assets(
            self,
            source_ip=None,
            page_size=None,
            remark=None,
            strategy_id=None,
            current_page=None,
            lang=None,
            need_statistics=None):
        api_request = APIRequest('DescribeWhiteListEffectiveAssets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "Remark": remark,
            "StrategyId": strategy_id,
            "CurrentPage": current_page,
            "Lang": lang,
            "NeedStatistics": need_statistics}
        return self._handle_request(api_request).result

    def update_white_list_process_status(
            self,
            process_ids=None,
            source_ip=None,
            strategy_id=None,
            lang=None,
            status=None):
        api_request = APIRequest('UpdateWhiteListProcessStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProcessIds": process_ids,
            "SourceIp": source_ip,
            "StrategyId": strategy_id,
            "Lang": lang,
            "Status": status}
        return self._handle_request(api_request).result

    def update_white_list_strategy_status(
            self,
            source_ip=None,
            strategy_ids=None,
            lang=None,
            status=None):
        api_request = APIRequest('UpdateWhiteListStrategyStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "StrategyIds": strategy_ids,
            "Lang": lang,
            "Status": status}
        return self._handle_request(api_request).result

    def save_white_list_strategy_assets(
            self,
            operations=None,
            relation_type=None,
            source_ip=None,
            strategy_id=None,
            lang=None):
        api_request = APIRequest('SaveWhiteListStrategyAssets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Operations": operations,
            "RelationType": relation_type,
            "SourceIp": source_ip,
            "StrategyId": strategy_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def save_white_list_strategy(
            self,
            strategy_name=None,
            source_ip=None,
            study_time=None,
            strategy_id=None,
            lang=None):
        api_request = APIRequest('SaveWhiteListStrategy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StrategyName": strategy_name,
            "SourceIp": source_ip,
            "StudyTime": study_time,
            "StrategyId": strategy_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_white_list_strategy_statistics(
            self,
            source_ip=None,
            page_size=None,
            strategy_ids=None,
            current_page=None,
            lang=None):
        api_request = APIRequest('DescribeWhiteListStrategyStatistics',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "StrategyIds": strategy_ids,
            "CurrentPage": current_page,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_white_list_process(
            self,
            source_ip=None,
            process_name=None,
            page_size=None,
            process_type=None,
            order_by=None,
            strategy_id=None,
            current_page=None,
            lang=None,
            desc=None):
        api_request = APIRequest('DescribeWhiteListProcess', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ProcessName": process_name,
            "PageSize": page_size,
            "ProcessType": process_type,
            "OrderBy": order_by,
            "StrategyId": strategy_id,
            "CurrentPage": current_page,
            "Lang": lang,
            "Desc": desc}
        return self._handle_request(api_request).result

    def describe_white_list_authorize(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeWhiteListAuthorize', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_white_list_asset(
            self,
            source_ip=None,
            last_max_id=None,
            page_size=None,
            strategy_id=None,
            lang=None,
            type_=None):
        api_request = APIRequest('DescribeWhiteListAsset', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "LastMaxId": last_max_id,
            "PageSize": page_size,
            "StrategyId": strategy_id,
            "Lang": lang,
            "Type": type_}
        return self._handle_request(api_request).result

    def auto_upgrade_to_sas_advanced_version(self, source_ip=None):
        api_request = APIRequest('AutoUpgradeToSasAdvancedVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_can_upgrade_sas(self, source_ip=None):
        api_request = APIRequest('DescribeCanUpgradeSas', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_can_try_sas(self, source_ip=None):
        api_request = APIRequest('DescribeCanTrySas', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_agent_install_status(self, source_ip=None, lang=None, uuids=None):
        api_request = APIRequest('DescribeAgentInstallStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "Uuids": uuids}
        return self._handle_request(api_request).result

    def operate_agent_client_install(
            self,
            source_ip=None,
            instance_ids=None,
            lang=None,
            uuids=None):
        api_request = APIRequest('OperateAgentClientInstall', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "InstanceIds": instance_ids,
            "Lang": lang,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_ecs_sts_status(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeEcsStsStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def open_sas_trial(self, source_ip=None, buy_version=None):
        api_request = APIRequest('OpenSasTrial', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "BuyVersion": buy_version}
        return self._handle_request(api_request).result

    def can_try_sas(self, source_ip=None):
        api_request = APIRequest('CanTrySas', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def modify_clear_logstore_storage(self, source_ip=None, from_=None, lang=None):
        api_request = APIRequest('ModifyClearLogstoreStorage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_logstore_storage(self, source_ip=None, from_=None, lang=None):
        api_request = APIRequest('DescribeLogstoreStorage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_, "Lang": lang}
        return self._handle_request(api_request).result

    def modify_web_lock_operate_events(self, source_ip=None, operation=None, event_ids=None):
        api_request = APIRequest('ModifyWebLockOperateEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Operation": operation, "EventIds": event_ids}
        return self._handle_request(api_request).result

    def describe_sls_project(self, source_ip=None, region_no=None):
        api_request = APIRequest('DescribeSlsProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "RegionNo": region_no}
        return self._handle_request(api_request).result

    def describe_analysis_shipper_status(self, source_ip=None):
        api_request = APIRequest('DescribeAnalysisShipperStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def execute_rule_engine_actual_time(self, source_ip=None, rule_id=None, message=None):
        api_request = APIRequest('ExecuteRuleEngineActualTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "RuleId": rule_id, "Message": message}
        return self._handle_request(api_request).result

    def describe_topic_list(self, source_ip=None):
        api_request = APIRequest('DescribeTopicList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_analysis_curve(self, source_ip=None, start_time_stamp=None, end_time_stamp=None):
        api_request = APIRequest('DescribeAnalysisCurve', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "StartTimeStamp": start_time_stamp,
            "EndTimeStamp": end_time_stamp}
        return self._handle_request(api_request).result

    def describe_analysis_statistics(self, source_ip=None):
        api_request = APIRequest('DescribeAnalysisStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_analysis_sls_index(self, source_ip=None):
        api_request = APIRequest('DescribeAnalysisSlsIndex', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_analysis_histograms(self, source_ip=None, query=None, from_=None, to=None):
        api_request = APIRequest('DescribeAnalysisHistograms', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Query": query, "From": from_, "To": to}
        return self._handle_request(api_request).result

    def describe_analysis_logs(
            self,
            source_ip=None,
            query=None,
            page_size=None,
            from_=None,
            current_page=None,
            to=None,
            reverse=None):
        api_request = APIRequest('DescribeAnalysisLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Query": query,
            "PageSize": page_size,
            "From": from_,
            "CurrentPage": current_page,
            "To": to,
            "Reverse": reverse}
        return self._handle_request(api_request).result

    def describe_join_rule_list(
            self,
            warn_level=None,
            source_ip=None,
            page_size=None,
            remark=None,
            current_page=None):
        api_request = APIRequest('DescribeJoinRuleList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WarnLevel": warn_level,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "remark": remark,
            "CurrentPage": current_page}
        return self._handle_request(api_request).result

    def operate_result(self, source_ip=None, ids=None, status=None):
        api_request = APIRequest('OperateResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Ids": ids, "Status": status}
        return self._handle_request(api_request).result

    def describe_result_list(
            self,
            source_ip=None,
            page_size=None,
            end_time=None,
            rule_name=None,
            remark=None,
            uuid_list=None,
            dealed=None,
            current_page=None,
            start_time=None):
        api_request = APIRequest('DescribeResultList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "EndTime": end_time,
            "RuleName": rule_name,
            "Remark": remark,
            "UuidList": uuid_list,
            "Dealed": dealed,
            "CurrentPage": current_page,
            "StartTime": start_time}
        return self._handle_request(api_request).result

    def describe_ding_talk(self, rule_action_name=None, source_ip=None):
        api_request = APIRequest('DescribeDingTalk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RuleActionName": rule_action_name, "SourceIp": source_ip}
        return self._handle_request(api_request).result

    def delete_ding_talk(self, source_ip=None, ids=None):
        api_request = APIRequest('DeleteDingTalk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Ids": ids}
        return self._handle_request(api_request).result

    def create_or_update_ding_talk(
            self,
            rule_action_name=None,
            source_ip=None,
            send_url=None,
            id_=None,
            interval_time=None):
        api_request = APIRequest('CreateOrUpdateDingTalk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RuleActionName": rule_action_name,
            "SourceIp": source_ip,
            "SendUrl": send_url,
            "Id": id_,
            "IntervalTime": interval_time}
        return self._handle_request(api_request).result

    def delete_join_rule(self, source_ip=None, ids=None):
        api_request = APIRequest('DeleteJoinRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Ids": ids}
        return self._handle_request(api_request).result

    def create_or_update_join_rule(
            self,
            warn_level=None,
            data_source_id2=None,
            data_source_id1=None,
            time_window=None,
            description=None,
            rule_name=None,
            expression2=None,
            expression1=None,
            source_ip=None,
            statistics_rules=None,
            join_relation=None,
            rule_id=None,
            actions=None):
        api_request = APIRequest('CreateOrUpdateJoinRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WarnLevel": warn_level,
            "DataSourceId2": data_source_id2,
            "DataSourceId1": data_source_id1,
            "TimeWindow": time_window,
            "Description": description,
            "RuleName": rule_name,
            "Expression2": expression2,
            "Expression1": expression1,
            "SourceIp": source_ip,
            "StatisticsRules": statistics_rules,
            "JoinRelation": join_relation,
            "RuleId": rule_id,
            "Actions": actions}
        return self._handle_request(api_request).result

    def create_or_update_data_source(
            self,
            project_name=None,
            config_type=None,
            source_ip=None,
            log_store_name=None,
            datasource_description=None,
            fields=None,
            region_no=None):
        api_request = APIRequest('CreateOrUpdateDataSource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProjectName": project_name,
            "ConfigType": config_type,
            "SourceIp": source_ip,
            "LogStoreName": log_store_name,
            "DatasourceDescription": datasource_description,
            "Fields": fields,
            "RegionNo": region_no}
        return self._handle_request(api_request).result

    def set_datasource_status(
            self,
            project_name=None,
            source_ip=None,
            log_store_name=None,
            status=None,
            region_no=None):
        api_request = APIRequest('SetDatasourceStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProjectName": project_name,
            "SourceIp": source_ip,
            "LogStoreName": log_store_name,
            "Status": status,
            "RegionNo": region_no}
        return self._handle_request(api_request).result

    def describe_meta_data(
            self,
            project_name=None,
            source_ip=None,
            log_store_name=None,
            region_no=None):
        api_request = APIRequest('DescribeMetaData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProjectName": project_name,
            "SourceIp": source_ip,
            "LogStoreName": log_store_name,
            "RegionNo": region_no}
        return self._handle_request(api_request).result

    def create_log_query(self, source_ip=None, query_name=None, conditions=None, query_detail=None):
        api_request = APIRequest('CreateLogQuery', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "QueryName": query_name,
            "Conditions": conditions,
            "QueryDetail": query_detail}
        return self._handle_request(api_request).result

    def download_log(self, source_ip=None, query=None, end_time=None, start_time=None):
        api_request = APIRequest('DownloadLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Query": query,
            "EndTime": end_time,
            "StartTime": start_time}
        return self._handle_request(api_request).result

    def describe_log_query(self, source_ip=None):
        api_request = APIRequest('DescribeLogQuery', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def delete_log_query(self, source_ip=None, query_name=None):
        api_request = APIRequest('DeleteLogQuery', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "QueryName": query_name}
        return self._handle_request(api_request).result

    def describe_histogram(self, source_ip=None, query=None, end_time=None, start_time=None):
        api_request = APIRequest('DescribeHistogram', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Query": query,
            "EndTime": end_time,
            "StartTime": start_time}
        return self._handle_request(api_request).result

    def describe_filter_fields(self, source_ip=None, query=None):
        api_request = APIRequest('DescribeFilterFields', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Query": query}
        return self._handle_request(api_request).result

    def describe_log_items(
            self,
            login_offset=None,
            process_snapshot_offset=None,
            port_snapshot_offset=None,
            query=None,
            end_time=None,
            current_page=None,
            network_offset=None,
            start_time=None,
            account_snapshot_offset=None,
            process_offset=None,
            source_ip=None,
            crack_offset=None,
            page_size=None):
        api_request = APIRequest('DescribeLogItems', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LoginOffset": login_offset,
            "ProcessSnapshotOffset": process_snapshot_offset,
            "PortSnapshotOffset": port_snapshot_offset,
            "Query": query,
            "EndTime": end_time,
            "CurrentPage": current_page,
            "NetworkOffset": network_offset,
            "StartTime": start_time,
            "AccountSnapshotOffset": account_snapshot_offset,
            "ProcessOffset": process_offset,
            "SourceIp": source_ip,
            "CrackOffset": crack_offset,
            "PageSize": page_size}
        return self._handle_request(api_request).result

    def describe_log_info(
            self,
            source_ip=None,
            query=None,
            page_size=None,
            end_time=None,
            current_page=None,
            start_time=None):
        api_request = APIRequest('DescribeLogInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Query": query,
            "PageSize": page_size,
            "EndTime": end_time,
            "CurrentPage": current_page,
            "StartTime": start_time}
        return self._handle_request(api_request).result

    def describe_secure_suggestion(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeSecureSuggestion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_defence_thread(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeDefenceThread', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def ignore_hc_check_warnings(
            self,
            reason=None,
            source_ip=None,
            check_warning_ids=None,
            check_ids=None,
            risk_id=None,
            type_=None):
        api_request = APIRequest('IgnoreHcCheckWarnings', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Reason": reason,
            "SourceIp": source_ip,
            "CheckWarningIds": check_warning_ids,
            "CheckIds": check_ids,
            "RiskId": risk_id,
            "Type": type_}
        return self._handle_request(api_request).result

    def validate_hc_warnings(self, risk_ids=None, source_ip=None, uuids=None):
        api_request = APIRequest('ValidateHcWarnings', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RiskIds": risk_ids, "SourceIp": source_ip, "Uuids": uuids}
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

    def describe_strategy_process(self, source_ip=None, strategy_id=None):
        api_request = APIRequest('DescribeStrategyProcess', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "StrategyId": strategy_id}
        return self._handle_request(api_request).result

    def describe_group_struct(self, source_ip=None, tag_id_list=None, remark=None):
        api_request = APIRequest('DescribeGroupStruct', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "tagIdList": tag_id_list, "remark": remark}
        return self._handle_request(api_request).result

    def describe_trace_info_node_list(
            self,
            source_ip=None,
            vertex_id=None,
            start_type=None,
            page_size=None,
            from_=None,
            page=None,
            lang=None,
            type_=None,
            uuid=None,
            incident_time=None):
        api_request = APIRequest('DescribeTraceInfoNodeList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "VertexId": vertex_id,
            "StartType": start_type,
            "PageSize": page_size,
            "From": from_,
            "Page": page,
            "Lang": lang,
            "Type": type_,
            "Uuid": uuid,
            "IncidentTime": incident_time}
        return self._handle_request(api_request).result

    def describe_trace_info_node(
            self,
            source_ip=None,
            vertex_id=None,
            from_=None,
            lang=None,
            type_=None,
            incident_time=None,
            uuid=None,
            event_name=None):
        api_request = APIRequest('DescribeTraceInfoNode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "VertexId": vertex_id,
            "From": from_,
            "Lang": lang,
            "Type": type_,
            "IncidentTime": incident_time,
            "Uuid": uuid,
            "EventName": event_name}
        return self._handle_request(api_request).result

    def describe_trace_info_detail(
            self,
            source_ip=None,
            vertex_id=None,
            from_=None,
            lang=None,
            type_=None,
            uuid=None,
            incident_time=None):
        api_request = APIRequest('DescribeTraceInfoDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "VertexId": vertex_id,
            "From": from_,
            "Lang": lang,
            "Type": type_,
            "Uuid": uuid,
            "IncidentTime": incident_time}
        return self._handle_request(api_request).result

    def describe_statistics(self, source_ip=None, from_=None):
        api_request = APIRequest('DescribeStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_}
        return self._handle_request(api_request).result

    def modify_save_vul_batch(
            self,
            batch_name=None,
            alias_name=None,
            status_list=None,
            source_ip=None,
            level=None,
            resource=None,
            name=None,
            dealed=None,
            remark=None,
            type_=None,
            necessity=None,
            uuids=None):
        api_request = APIRequest('ModifySaveVulBatch', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BatchName": batch_name,
            "AliasName": alias_name,
            "StatusList": status_list,
            "SourceIp": source_ip,
            "Level": level,
            "Resource": resource,
            "Name": name,
            "Dealed": dealed,
            "Remark": remark,
            "Type": type_,
            "Necessity": necessity,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_vul_batch(self, source_ip=None, resource=None):
        api_request = APIRequest('DescribeVulBatch', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Resource": resource}
        return self._handle_request(api_request).result

    def describe_vul_level(self, source_ip=None):
        api_request = APIRequest('DescribeVulLevel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def modify_vul_level(self, concern_level=None, source_ip=None):
        api_request = APIRequest('ModifyVulLevel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ConcernLevel": concern_level, "SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_vul_num_statistics(
            self,
            source_ip=None,
            end_ts=None,
            from_=None,
            start_ts=None,
            create_ts_end=None,
            include_app=None,
            create_ts_start=None,
            uuids=None):
        api_request = APIRequest('DescribeVulNumStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "EndTs": end_ts,
            "From": from_,
            "StartTs": start_ts,
            "CreateTsEnd": create_ts_end,
            "IncludeApp": include_app,
            "CreateTsStart": create_ts_start,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def export_vul(
            self,
            status_list=None,
            level=None,
            resource=None,
            remark=None,
            dealed=None,
            type_=None,
            batch_name=None,
            alias_name=None,
            source_ip=None,
            name=None,
            lang=None,
            necessity=None,
            uuids=None):
        api_request = APIRequest('ExportVul', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StatusList": status_list,
            "Level": level,
            "Resource": resource,
            "Remark": remark,
            "Dealed": dealed,
            "Type": type_,
            "BatchName": batch_name,
            "AliasName": alias_name,
            "SourceIp": source_ip,
            "Name": name,
            "Lang": lang,
            "Necessity": necessity,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_vul_machine_list(
            self,
            source_ip=None,
            end_ts=None,
            from_=None,
            start_ts=None,
            include_app=None,
            uuids=None):
        api_request = APIRequest('DescribeVulMachineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "EndTs": end_ts,
            "From": from_,
            "StartTs": start_ts,
            "IncludeApp": include_app,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_grouped_vul(
            self,
            status_list=None,
            level=None,
            group_id=None,
            cve_id=None,
            order_by=None,
            dealed=None,
            current_page=None,
            type_=None,
            last_ts_end=None,
            create_ts_start=None,
            alias_name=None,
            patch_id=None,
            source_ip=None,
            name=None,
            page_size=None,
            lang=None,
            create_ts_end=None,
            last_ts_start=None,
            necessity=None,
            uuids=None,
            direction=None):
        api_request = APIRequest('DescribeGroupedVul', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StatusList": status_list,
            "Level": level,
            "GroupId": group_id,
            "CveId": cve_id,
            "OrderBy": order_by,
            "Dealed": dealed,
            "CurrentPage": current_page,
            "Type": type_,
            "LastTsEnd": last_ts_end,
            "CreateTsStart": create_ts_start,
            "AliasName": alias_name,
            "PatchId": patch_id,
            "SourceIp": source_ip,
            "Name": name,
            "PageSize": page_size,
            "Lang": lang,
            "CreateTsEnd": create_ts_end,
            "LastTsStart": last_ts_start,
            "Necessity": necessity,
            "Uuids": uuids,
            "Direction": direction}
        return self._handle_request(api_request).result

    def describe_target_config(self, source_ip=None, type_=None, uuid=None):
        api_request = APIRequest('DescribeTargetConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Type": type_, "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_vul_export_info(self, source_ip=None, export_id=None):
        api_request = APIRequest('DescribeVulExportInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "ExportId": export_id}
        return self._handle_request(api_request).result

    def modify_vul_config(self, source_ip=None, type_=None, config=None):
        api_request = APIRequest('ModifyVulConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Type": type_, "Config": config}
        return self._handle_request(api_request).result

    def create_vul_whitelist(self, reason=None, source_ip=None, whitelist=None):
        api_request = APIRequest('CreateVulWhitelist', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Reason": reason, "SourceIp": source_ip, "Whitelist": whitelist}
        return self._handle_request(api_request).result

    def describe_auto_del_config(self, source_ip=None):
        api_request = APIRequest('DescribeAutoDelConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def modify_target_config(self, source_ip=None, type_=None, uuid=None, config=None):
        api_request = APIRequest('ModifyTargetConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Type": type_, "Uuid": uuid, "Config": config}
        return self._handle_request(api_request).result

    def describe_vul_whitelist(self, source_ip=None, page_size=None, current_page=None):
        api_request = APIRequest('DescribeVulWhitelist', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page}
        return self._handle_request(api_request).result

    def delete_vul_batch(self, batch_name=None, source_ip=None, resource=None):
        api_request = APIRequest('DeleteVulBatch', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BatchName": batch_name, "SourceIp": source_ip, "Resource": resource}
        return self._handle_request(api_request).result

    def modify_vul_target(self, source_ip=None, config=None, target=None):
        api_request = APIRequest('ModifyVulTarget', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Config": config, "Target": target}
        return self._handle_request(api_request).result

    def describe_vul_target_statistics(self, source_ip=None, type_=None):
        api_request = APIRequest('DescribeVulTargetStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Type": type_}
        return self._handle_request(api_request).result

    def delete_vul_whitelist(self, source_ip=None, whitelist=None):
        api_request = APIRequest('DeleteVulWhitelist', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Whitelist": whitelist}
        return self._handle_request(api_request).result

    def describe_target(self, source_ip=None, type_=None, config=None):
        api_request = APIRequest('DescribeTarget', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Type": type_, "Config": config}
        return self._handle_request(api_request).result

    def modify_auto_del_config(self, source_ip=None, days=None):
        api_request = APIRequest('ModifyAutoDelConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Days": days}
        return self._handle_request(api_request).result

    def describe_vul_config(self, source_ip=None, type_=None):
        api_request = APIRequest('DescribeVulConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Type": type_}
        return self._handle_request(api_request).result

    def operate_vul(self, reason=None, source_ip=None, operate_type=None, type_=None, info=None):
        api_request = APIRequest('OperateVul', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Reason": reason,
            "SourceIp": source_ip,
            "OperateType": operate_type,
            "Type": type_,
            "Info": info}
        return self._handle_request(api_request).result

    def describe_vul_level_statistics(
            self,
            source_ip=None,
            end_ts=None,
            from_=None,
            start_ts=None,
            include_app=None,
            uuids=None):
        api_request = APIRequest('DescribeVulLevelStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "EndTs": end_ts,
            "From": from_,
            "StartTs": start_ts,
            "IncludeApp": include_app,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_list_access_key_id_auth(self, source_ip=None):
        api_request = APIRequest('DescribeListAccessKeyIdAuth', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_screen_version_config(self, source_ip=None):
        api_request = APIRequest('DescribeScreenVersionConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_screen_operate_info(self, source_ip=None, start_time=None, lang=None):
        api_request = APIRequest('DescribeScreenOperateInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "StartTime": start_time, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_screen_host_statistics(self, source_ip=None):
        api_request = APIRequest('DescribeScreenHostStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_screen_alarm_event_list(
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
        api_request = APIRequest('DescribeScreenAlarmEventList', 'GET', 'http', 'RPC', 'query')
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

    def describe_screen_summary_info(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeScreenSummaryInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_screen_attack_analysis_data(
            self,
            source_ip=None,
            data=None,
            base64=None,
            page_size=None,
            end_time=None,
            current_page=None,
            start_time=None,
            lang=None,
            type_=None):
        api_request = APIRequest('DescribeScreenAttackAnalysisData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Data": data,
            "Base64": base64,
            "PageSize": page_size,
            "EndTime": end_time,
            "CurrentPage": current_page,
            "StartTime": start_time,
            "Lang": lang,
            "Type": type_}
        return self._handle_request(api_request).result

    def describe_screen_security_stat_info(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeScreenSecurityStatInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_screen_score_thread(self, source_ip=None, end_time=None, start_time=None):
        api_request = APIRequest('DescribeScreenScoreThread', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "EndTime": end_time, "StartTime": start_time}
        return self._handle_request(api_request).result

    def modify_screen_setting(self, source_ip=None, screen_title=None, screen_id_setting=None):
        api_request = APIRequest('ModifyScreenSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ScreenTitle": screen_title,
            "ScreenIdSetting": screen_id_setting}
        return self._handle_request(api_request).result

    def describe_screen_settings(self, source_ip=None):
        api_request = APIRequest('DescribeScreenSettings', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_screen_setting(self, source_ip=None, id_=None):
        api_request = APIRequest('DescribeScreenSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Id": id_}
        return self._handle_request(api_request).result

    def delete_screen_setting(self, source_ip=None, id_=None):
        api_request = APIRequest('DeleteScreenSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Id": id_}
        return self._handle_request(api_request).result

    def creat_screen_setting(self, source_ip=None, screen_title=None, screen_id_setting=None):
        api_request = APIRequest('CreatScreenSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ScreenTitle": screen_title,
            "ScreenIdSetting": screen_id_setting}
        return self._handle_request(api_request).result

    def describe_attack_analysis_data(
            self,
            source_ip=None,
            data=None,
            base64=None,
            page_size=None,
            end_time=None,
            current_page=None,
            start_time=None,
            lang=None,
            type_=None):
        api_request = APIRequest('DescribeAttackAnalysisData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Data": data,
            "Base64": base64,
            "PageSize": page_size,
            "EndTime": end_time,
            "CurrentPage": current_page,
            "StartTime": start_time,
            "Lang": lang,
            "Type": type_}
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

    def describe_alarm_event_list(
            self,
            alarm_event_name=None,
            source_ip=None,
            group_id=None,
            page_size=None,
            alarm_event_type=None,
            dealed=None,
            from_=None,
            remark=None,
            current_page=None,
            lang=None,
            levels=None,
            list_of_operate_error_code_list=None):
        api_request = APIRequest('DescribeAlarmEventList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AlarmEventName": alarm_event_name,
            "SourceIp": source_ip,
            "GroupId": group_id,
            "PageSize": page_size,
            "AlarmEventType": alarm_event_type,
            "Dealed": dealed,
            "From": from_,
            "Remark": remark,
            "CurrentPage": current_page,
            "Lang": lang,
            "Levels": levels,
            "OperateErrorCodeList": list_of_operate_error_code_list}
        repeat_info = {"OperateErrorCodeList": ('OperateErrorCodeList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def operate_suspicious_event(self, source_ip=None, data=None, operate_type=None):
        api_request = APIRequest('OperateSuspiciousEvent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Data": data, "OperateType": operate_type}
        return self._handle_request(api_request).result

    def describe_quara_file(self, source_ip=None, page_size=None, current_page=None):
        api_request = APIRequest('DescribeQuaraFile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page}
        return self._handle_request(api_request).result

    def rollback_quara_file(
            self,
            source_ip=None,
            event_type=None,
            tag=None,
            uuid=None,
            event_name=None):
        api_request = APIRequest('RollbackQuaraFile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "EventType": event_type,
            "Tag": tag,
            "Uuid": uuid,
            "EventName": event_name}
        return self._handle_request(api_request).result

    def describe_susp_event_types(self, source_ip=None):
        api_request = APIRequest('DescribeSuspEventTypes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_susp_trend_statistics(self, source_ip=None):
        api_request = APIRequest('DescribeSuspTrendStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_summary_info(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeSummaryInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_security_stat_info(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeSecurityStatInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_operate_info(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeOperateInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_web_lock_events(
            self,
            status_list=None,
            source_ip=None,
            level=None,
            group_id=None,
            page_size=None,
            remark=None,
            dealed=None,
            current_page=None,
            tag=None,
            lang=None,
            event_name=None):
        api_request = APIRequest('DescribeWebLockEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StatusList": status_list,
            "SourceIp": source_ip,
            "Level": level,
            "GroupId": group_id,
            "PageSize": page_size,
            "Remark": remark,
            "Dealed": dealed,
            "CurrentPage": current_page,
            "Tag": tag,
            "Lang": lang,
            "EventName": event_name}
        return self._handle_request(api_request).result

    def modify_web_lock_update_config(
            self,
            local_backup_dir=None,
            mode=None,
            inclusive_file_type=None,
            exclusive_file=None,
            source_ip=None,
            exclusive_file_type=None,
            id_=None,
            lang=None,
            dir=None,
            uuid=None,
            exclusive_dir=None):
        api_request = APIRequest('ModifyWebLockUpdateConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocalBackupDir": local_backup_dir,
            "Mode": mode,
            "InclusiveFileType": inclusive_file_type,
            "ExclusiveFile": exclusive_file,
            "SourceIp": source_ip,
            "ExclusiveFileType": exclusive_file_type,
            "Id": id_,
            "Lang": lang,
            "Dir": dir,
            "Uuid": uuid,
            "ExclusiveDir": exclusive_dir}
        return self._handle_request(api_request).result

    def modify_web_lock_create_config(
            self,
            local_backup_dir=None,
            mode=None,
            inclusive_file_type=None,
            exclusive_file=None,
            source_ip=None,
            exclusive_file_type=None,
            lang=None,
            dir=None,
            uuid=None,
            exclusive_dir=None):
        api_request = APIRequest('ModifyWebLockCreateConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocalBackupDir": local_backup_dir,
            "Mode": mode,
            "InclusiveFileType": inclusive_file_type,
            "ExclusiveFile": exclusive_file,
            "SourceIp": source_ip,
            "ExclusiveFileType": exclusive_file_type,
            "Lang": lang,
            "Dir": dir,
            "Uuid": uuid,
            "ExclusiveDir": exclusive_dir}
        return self._handle_request(api_request).result

    def modify_web_lock_delete_config(self, source_ip=None, id_=None, lang=None, uuid=None):
        api_request = APIRequest('ModifyWebLockDeleteConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Id": id_, "Lang": lang, "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_web_lock_config_list(self, source_ip=None, lang=None, uuid=None):
        api_request = APIRequest('DescribeWebLockConfigList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "Uuid": uuid}
        return self._handle_request(api_request).result

    def modify_web_lock_refresh(self, source_ip=None, lang=None, uuid=None):
        api_request = APIRequest('ModifyWebLockRefresh', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "Uuid": uuid}
        return self._handle_request(api_request).result

    def modify_web_lock_status(self, source_ip=None, lang=None, uuid=None, status=None):
        api_request = APIRequest('ModifyWebLockStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "Uuid": uuid, "Status": status}
        return self._handle_request(api_request).result

    def describe_web_lock_bind_list(
            self,
            source_ip=None,
            page_size=None,
            remark=None,
            current_page=None,
            lang=None,
            status=None):
        api_request = APIRequest('DescribeWebLockBindList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "Remark": remark,
            "CurrentPage": current_page,
            "Lang": lang,
            "Status": status}
        return self._handle_request(api_request).result

    def modify_web_lock_machine_list(self, source_ip=None, lang=None, uuids=None):
        api_request = APIRequest('ModifyWebLockMachineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_web_lock_machine_list(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeWebLockMachineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_web_lock_status(self, source_ip=None, from_=None, lang=None):
        api_request = APIRequest('DescribeWebLockStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_, "Lang": lang}
        return self._handle_request(api_request).result

    def operate_suspicious_target_config(
            self,
            target_operations=None,
            source_ip=None,
            target_type=None,
            lang=None,
            type_=None):
        api_request = APIRequest('OperateSuspiciousTargetConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TargetOperations": target_operations,
            "SourceIp": source_ip,
            "TargetType": target_type,
            "Lang": lang,
            "Type": type_}
        return self._handle_request(api_request).result

    def operate_suspicious_overall_config(self, source_ip=None, lang=None, type_=None, config=None):
        api_request = APIRequest('OperateSuspiciousOverallConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "Type": type_, "Config": config}
        return self._handle_request(api_request).result

    def describe_suspicious_uuid_config(self, source_ip=None, lang=None, type_=None):
        api_request = APIRequest('DescribeSuspiciousUUIDConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "Type": type_}
        return self._handle_request(api_request).result

    def describe_suspicious_overall_config(self, source_ip=None, type_=None):
        api_request = APIRequest('DescribeSuspiciousOverallConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Type": type_}
        return self._handle_request(api_request).result

    def describe_data_source(self, config_type=None, source_ip=None, lang=None):
        api_request = APIRequest('DescribeDataSource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ConfigType": config_type, "SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def delete_rule(self, source_ip=None, id_=None, lang=None):
        api_request = APIRequest('DeleteRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Id": id_, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_rule_list(
            self,
            warn_level=None,
            source_ip=None,
            group_id=None,
            page_size=None,
            remark=None,
            current_page=None,
            id_=None,
            lang=None,
            ex_group_id=None):
        api_request = APIRequest('DescribeRuleList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WarnLevel": warn_level,
            "SourceIp": source_ip,
            "GroupId": group_id,
            "PageSize": page_size,
            "Remark": remark,
            "CurrentPage": current_page,
            "Id": id_,
            "Lang": lang,
            "ExGroupId": ex_group_id}
        return self._handle_request(api_request).result

    def create_or_update_rule(
            self,
            warn_level=None,
            source_ip=None,
            statistics_rules=None,
            data_source_id=None,
            description=None,
            rule_name=None,
            id_=None,
            lang=None,
            expressions=None,
            actions=None,
            rule_group_ids=None):
        api_request = APIRequest('CreateOrUpdateRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WarnLevel": warn_level,
            "SourceIp": source_ip,
            "StatisticsRules": statistics_rules,
            "DataSourceId": data_source_id,
            "Description": description,
            "RuleName": rule_name,
            "Id": id_,
            "Lang": lang,
            "Expressions": expressions,
            "Actions": actions,
            "RuleGroupIds": rule_group_ids}
        return self._handle_request(api_request).result

    def delete_rule_group(self, source_ip=None, id_=None, lang=None):
        api_request = APIRequest('DeleteRuleGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Id": id_, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_group_list(
            self,
            warn_level=None,
            source_ip=None,
            rule_group_id=None,
            page_size=None,
            current_page=None,
            lang=None,
            ex_group_id=None):
        api_request = APIRequest('DescribeGroupList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WarnLevel": warn_level,
            "SourceIp": source_ip,
            "RuleGroupId": rule_group_id,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang,
            "ExGroupId": ex_group_id}
        return self._handle_request(api_request).result

    def create_or_update_group(
            self,
            rule_ids=None,
            source_ip=None,
            machine_group_ids=None,
            description=None,
            id_=None,
            lang=None,
            group_name=None):
        api_request = APIRequest('CreateOrUpdateGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RuleIds": rule_ids,
            "SourceIp": source_ip,
            "MachineGroupIds": machine_group_ids,
            "Description": description,
            "Id": id_,
            "Lang": lang,
            "GroupName": group_name}
        return self._handle_request(api_request).result

    def describe_buy_summary(self, source_ip=None):
        api_request = APIRequest('DescribeBuySummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def modify_open_log_shipper(self, source_ip=None, from_=None, lang=None):
        api_request = APIRequest('ModifyOpenLogShipper', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_log_shipper_status(self, source_ip=None, from_=None, lang=None):
        api_request = APIRequest('DescribeLogShipperStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_, "Lang": lang}
        return self._handle_request(api_request).result

    def modify_log_meta_status(
            self,
            source_ip=None,
            project=None,
            from_=None,
            lang=None,
            log_store=None,
            status=None):
        api_request = APIRequest('ModifyLogMetaStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Project": project,
            "From": from_,
            "Lang": lang,
            "LogStore": log_store,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_log_meta(self, source_ip=None, from_=None, lang=None):
        api_request = APIRequest('DescribeLogMeta', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_api_buy_summary(self, source_ip=None):
        api_request = APIRequest('DescribeApiBuySummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_version_config(self, source_ip=None):
        api_request = APIRequest('DescribeVersionConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_event_level_count(self, source_ip=None, from_=None, type_=None):
        api_request = APIRequest('DescribeEventLevelCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_, "Type": type_}
        return self._handle_request(api_request).result

    def describe_total_statistics(
            self,
            status_list=None,
            sale_id=None,
            rule_type=None,
            group_id=None,
            end_time=None,
            remark=None,
            dealed=None,
            current_page=None,
            start_time=None,
            type_=None,
            uuid=None,
            secure_token=None,
            source_ip=None,
            web_group_id=None,
            page_size=None,
            from_=None,
            action1=None,
            tag=None,
            flow=None,
            status=None):
        api_request = APIRequest('DescribeTotalStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StatusList": status_list,
            "SaleId": sale_id,
            "RuleType": rule_type,
            "GroupId": group_id,
            "EndTime": end_time,
            "Remark": remark,
            "Dealed": dealed,
            "CurrentPage": current_page,
            "StartTime": start_time,
            "Type": type_,
            "Uuid": uuid,
            "SecureToken": secure_token,
            "SourceIp": source_ip,
            "WebGroupId": web_group_id,
            "PageSize": page_size,
            "From": from_,
            "Action1": action1,
            "Tag": tag,
            "Flow": flow,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_instance_statistics(self, source_ip=None, lang=None, uuid=None):
        api_request = APIRequest('DescribeInstanceStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_all_regions_statistics(
            self,
            status_list=None,
            sale_id=None,
            rule_type=None,
            group_id=None,
            end_time=None,
            remark=None,
            dealed=None,
            current_page=None,
            start_time=None,
            type_=None,
            uuid=None,
            secure_token=None,
            source_ip=None,
            web_group_id=None,
            page_size=None,
            from_=None,
            action1=None,
            tag=None,
            flow=None,
            status=None):
        api_request = APIRequest('DescribeAllRegionsStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StatusList": status_list,
            "SaleId": sale_id,
            "RuleType": rule_type,
            "GroupId": group_id,
            "EndTime": end_time,
            "Remark": remark,
            "Dealed": dealed,
            "CurrentPage": current_page,
            "StartTime": start_time,
            "Type": type_,
            "Uuid": uuid,
            "SecureToken": secure_token,
            "SourceIp": source_ip,
            "WebGroupId": web_group_id,
            "PageSize": page_size,
            "From": from_,
            "Action1": action1,
            "Tag": tag,
            "Flow": flow,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_asset_summary(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeAssetSummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_emg_user_agreement(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeEmgUserAgreement', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def modify_emg_vul_submit(self, source_ip=None, name=None, user_agreement=None, lang=None):
        api_request = APIRequest('ModifyEmgVulSubmit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Name": name,
            "UserAgreement": user_agreement,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_emg_notice(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeEmgNotice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_emg_vul_group(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeEmgVulGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_yesterday_statistics(self, source_ip=None):
        api_request = APIRequest('DescribeYesterdayStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def modify_concern_necessity(self, source_ip=None, lang=None, concern_necessity=None):
        api_request = APIRequest('ModifyConcernNecessity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Lang": lang,
            "ConcernNecessity": concern_necessity}
        return self._handle_request(api_request).result

    def describe_concern_necessity(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeConcernNecessity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_vulnerability_summary(
            self,
            resource_owner_id=None,
            source_ip=None,
            cron_job_id=None):
        api_request = APIRequest('DescribeVulnerabilitySummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceIp": source_ip,
            "CronJobId": cron_job_id}
        return self._handle_request(api_request).result

    def save_susp_event_user_setting(self, source_ip=None, from_=None, levels_on=None):
        api_request = APIRequest('SaveSuspEventUserSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_, "LevelsOn": levels_on}
        return self._handle_request(api_request).result

    def rollback_susp_event_quara_file(self, source_ip=None, from_=None, quara_file_id=None):
        api_request = APIRequest('RollbackSuspEventQuaraFile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_, "QuaraFileId": quara_file_id}
        return self._handle_request(api_request).result

    def operation_susp_events(
            self,
            source_ip=None,
            warn_type=None,
            suspicious_event_ids=None,
            from_=None,
            sub_operation=None,
            operation=None):
        api_request = APIRequest('OperationSuspEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "WarnType": warn_type,
            "SuspiciousEventIds": suspicious_event_ids,
            "From": from_,
            "SubOperation": sub_operation,
            "Operation": operation}
        return self._handle_request(api_request).result

    def export_susp_events(
            self,
            time_end=None,
            source_ip=None,
            name=None,
            dealed=None,
            remark=None,
            from_=None,
            time_start=None,
            lang=None,
            levels=None,
            parent_event_types=None,
            status=None):
        api_request = APIRequest('ExportSuspEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TimeEnd": time_end,
            "SourceIp": source_ip,
            "Name": name,
            "Dealed": dealed,
            "Remark": remark,
            "From": from_,
            "TimeStart": time_start,
            "Lang": lang,
            "Levels": levels,
            "ParentEventTypes": parent_event_types,
            "Status": status}
        return self._handle_request(api_request).result

    def exec_strategy(self, source_ip=None, strategy_id=None):
        api_request = APIRequest('ExecStrategy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "StrategyId": strategy_id}
        return self._handle_request(api_request).result

    def describe_uuid_config(self, source_ip=None, uuid=None):
        api_request = APIRequest('DescribeUuidConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_susp_event_user_setting(self, source_ip=None, from_=None, id_=None):
        api_request = APIRequest('DescribeSuspEventUserSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_, "Id": id_}
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

    def describe_susp_event_quara_files(
            self,
            source_ip=None,
            page_size=None,
            current_page=None,
            from_=None,
            status=None):
        api_request = APIRequest('DescribeSuspEventQuaraFiles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "From": from_,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_susp_event_export_info(self, source_ip=None, from_=None, export_id=None):
        api_request = APIRequest('DescribeSuspEventExportInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "From": from_, "ExportId": export_id}
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

    def describe_strategy_exec_detail(self, source_ip=None, strategy_id=None):
        api_request = APIRequest('DescribeStrategyExecDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "StrategyId": strategy_id}
        return self._handle_request(api_request).result

    def describe_nsas_susp_event_type(
            self,
            source_ip=None,
            name=None,
            remark=None,
            from_=None,
            lang=None):
        api_request = APIRequest('DescribeNsasSuspEventType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Name": name,
            "Remark": remark,
            "From": from_,
            "Lang": lang}
        return self._handle_request(api_request).result

    def modify_asset_group(self, source_ip=None, group_id=None, uuids=None):
        api_request = APIRequest('ModifyAssetGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "GroupId": group_id, "Uuids": uuids}
        return self._handle_request(api_request).result

    def delete_search_condition(self, source_ip=None, name=None):
        api_request = APIRequest('DeleteSearchCondition', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Name": name}
        return self._handle_request(api_request).result

    def modify_search_condition(self, source_ip=None, name=None, filter_conditions=None):
        api_request = APIRequest('ModifySearchCondition', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Name": name,
            "FilterConditions": filter_conditions}
        return self._handle_request(api_request).result

    def describe_search_condition(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeSearchCondition', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def modify_sas_asset_statistics_column(self, source_ip=None, statistics_column=None):
        api_request = APIRequest('ModifySasAssetStatisticsColumn', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "StatisticsColumn": statistics_column}
        return self._handle_request(api_request).result

    def describe_sas_asset_statistics_column(self, source_ip=None):
        api_request = APIRequest('DescribeSasAssetStatisticsColumn', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_asset_detail_by_uuid(self, source_ip=None, lang=None, uuid=None):
        api_request = APIRequest('DescribeAssetDetailByUuid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "Uuid": uuid}
        return self._handle_request(api_request).result

    def transform_leakage(self, source_ip=None):
        api_request = APIRequest('TransformLeakage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def auto_upgrade_sas(self, source_ip=None):
        api_request = APIRequest('AutoUpgradeSas', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_top_risky_assets(self, source_ip=None, page_size=None, from_=None):
        api_request = APIRequest('DescribeTopRiskyAssets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "PageSize": page_size, "From": from_}
        return self._handle_request(api_request).result

    def describe_event_count_curve(
            self,
            types=None,
            source_ip=None,
            vul_event_levels=None,
            last_days=None,
            health_event_levels=None,
            suspicious_event_levels=None):
        api_request = APIRequest('DescribeEventCountCurve', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Types": types,
            "SourceIp": source_ip,
            "VulEventLevels": vul_event_levels,
            "LastDays": last_days,
            "HealthEventLevels": health_event_levels,
            "SuspiciousEventLevels": suspicious_event_levels}
        return self._handle_request(api_request).result

    def describe_sas_asset_statistics(
            self,
            source_ip=None,
            statistics_column=None,
            page_size=None,
            from_=None,
            current_page=None,
            uuids=None):
        api_request = APIRequest('DescribeSasAssetStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "StatisticsColumn": statistics_column,
            "PageSize": page_size,
            "From": from_,
            "CurrentPage": current_page,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_asset_list(
            self,
            source_ip=None,
            page_size=None,
            from_=None,
            current_page=None,
            lang=None,
            filter_conditions=None):
        api_request = APIRequest('DescribeAssetList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "From": from_,
            "CurrentPage": current_page,
            "Lang": lang,
            "FilterConditions": filter_conditions}
        return self._handle_request(api_request).result

    def describe_sas_left_condition(
            self,
            source_ip=None,
            condition_type=None,
            from_=None,
            lang=None,
            filter_conditions=None):
        api_request = APIRequest('DescribeSasLeftCondition', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ConditionType": condition_type,
            "From": from_,
            "Lang": lang,
            "FilterConditions": filter_conditions}
        return self._handle_request(api_request).result

    def operate_warning(
            self,
            reason=None,
            source_ip=None,
            operate_type=None,
            risk_warning_ids=None):
        api_request = APIRequest('OperateWarning', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Reason": reason,
            "SourceIp": source_ip,
            "OperateType": operate_type,
            "RiskWarningIds": risk_warning_ids}
        return self._handle_request(api_request).result

    def modify_machine_config(self, source_ip=None, type_=None, target=None):
        api_request = APIRequest('ModifyMachineConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Type": type_, "Target": target}
        return self._handle_request(api_request).result

    def export_warning(
            self,
            status_list=None,
            risk_levels=None,
            export_type=None,
            dealed=None,
            type_names=None,
            is_summary_export=None,
            risk_name=None,
            risk_ids=None,
            source_ip=None,
            strategy_id=None,
            lang=None,
            type_name=None,
            sub_type_names=None,
            uuids=None):
        api_request = APIRequest('ExportWarning', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StatusList": status_list,
            "RiskLevels": risk_levels,
            "ExportType": export_type,
            "Dealed": dealed,
            "TypeNames": type_names,
            "IsSummaryExport": is_summary_export,
            "RiskName": risk_name,
            "RiskIds": risk_ids,
            "SourceIp": source_ip,
            "StrategyId": strategy_id,
            "Lang": lang,
            "TypeName": type_name,
            "SubTypeNames": sub_type_names,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_user_setting(self, source_ip=None):
        api_request = APIRequest('DescribeUserSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describesummary(
            self,
            type_names=None,
            risk_name=None,
            status_list=None,
            source_ip=None,
            risk_levels=None,
            page_size=None,
            dealed=None,
            strategy_id=None,
            current_page=None,
            sub_type_names=None,
            uuids=None):
        api_request = APIRequest('Describesummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TypeNames": type_names,
            "RiskName": risk_name,
            "StatusList": status_list,
            "SourceIp": source_ip,
            "RiskLevels": risk_levels,
            "PageSize": page_size,
            "Dealed": dealed,
            "StrategyId": strategy_id,
            "CurrentPage": current_page,
            "SubTypeNames": sub_type_names,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_risk_white_list(
            self,
            risk_name=None,
            source_ip=None,
            page_size=None,
            current_page=None):
        api_request = APIRequest('DescribeRiskWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RiskName": risk_name,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page}
        return self._handle_request(api_request).result

    def describe_risk_type(self, source_ip=None, strategy_id=None, lang=None, uuids=None):
        api_request = APIRequest('DescribeRiskType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "StrategyId": strategy_id,
            "Lang": lang,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_risks(self, risk_name=None, source_ip=None, limit=None, lang=None, risk_id=None):
        api_request = APIRequest('DescribeRisks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RiskName": risk_name,
            "SourceIp": source_ip,
            "Limit": limit,
            "Lang": lang,
            "RiskId": risk_id}
        return self._handle_request(api_request).result

    def describe_machine_config(
            self,
            resource_owner_id=None,
            types=None,
            source_ip=None,
            page_size=None,
            current_page=None,
            type_=None,
            lang=None,
            config=None,
            target=None):
        api_request = APIRequest('DescribeMachineConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Types": types,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Type": type_,
            "Lang": lang,
            "Config": config,
            "Target": target}
        return self._handle_request(api_request).result

    def describe_mac_config(
            self,
            resource_owner_id=None,
            types=None,
            source_ip=None,
            extern=None,
            type_=None,
            config=None,
            target=None):
        api_request = APIRequest('DescribeMacConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Types": types,
            "SourceIp": source_ip,
            "Extern": extern,
            "Type": type_,
            "Config": config,
            "Target": target}
        return self._handle_request(api_request).result

    def describe_export_info(self, source_ip=None, export_id=None):
        api_request = APIRequest('DescribeExportInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "ExportId": export_id}
        return self._handle_request(api_request).result

    def create_user_white_list(self, risk_id_list=None, reason=None, source_ip=None):
        api_request = APIRequest('CreateUserWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RiskIdList": risk_id_list, "Reason": reason, "SourceIp": source_ip}
        return self._handle_request(api_request).result

    def create_user_setting(
            self,
            source_ip=None,
            alert_levels=None,
            invalid_warning_keep_days=None):
        api_request = APIRequest('CreateUserSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "AlertLevels": alert_levels,
            "InvalidWarningKeepDays": invalid_warning_keep_days}
        return self._handle_request(api_request).result

    def batch_delete_white_list(self, risk_id_list=None, source_ip=None):
        api_request = APIRequest('BatchDeleteWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RiskIdList": risk_id_list, "SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_suspicious_export_info(self, source_ip=None, export_id=None):
        api_request = APIRequest('DescribeSuspiciousExportInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "ExportId": export_id}
        return self._handle_request(api_request).result

    def create_suspicious_export(
            self,
            status_list=None,
            source_ip=None,
            event_name_remark=None,
            level=None,
            group_id=None,
            dealed=None,
            event_type=None,
            remark=None,
            tag=None):
        api_request = APIRequest('CreateSuspiciousExport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StatusList": status_list,
            "SourceIp": source_ip,
            "EventNameRemark": event_name_remark,
            "Level": level,
            "GroupId": group_id,
            "Dealed": dealed,
            "EventType": event_type,
            "Remark": remark,
            "Tag": tag}
        return self._handle_request(api_request).result

    def modify_strategy_target(self, source_ip=None, type_=None, config=None, target=None):
        api_request = APIRequest('ModifyStrategyTarget', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Type": type_,
            "Config": config,
            "Target": target}
        return self._handle_request(api_request).result

    def modify_strategy(
            self,
            risk_sub_type_name=None,
            source_ip=None,
            cycle_start_time=None,
            name=None,
            cycle_days=None,
            id_=None):
        api_request = APIRequest('ModifyStrategy', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "RiskSubTypeName": risk_sub_type_name,
            "SourceIp": source_ip,
            "CycleStartTime": cycle_start_time,
            "Name": name,
            "CycleDays": cycle_days,
            "Id": id_}
        return self._handle_request(api_request).result

    def modify_batch_ignore_vul(self, reason=None, source_ip=None, info=None):
        api_request = APIRequest('ModifyBatchIgnoreVul', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Reason": reason, "SourceIp": source_ip, "Info": info}
        return self._handle_request(api_request).result

    def describe_webshell(self, source_ip=None, group_id=None, remark=None, dealed=None, tag=None):
        api_request = APIRequest('DescribeWebshell', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "GroupId": group_id,
            "Remark": remark,
            "Dealed": dealed,
            "Tag": tag}
        return self._handle_request(api_request).result

    def describe_warning(
            self,
            type_names=None,
            risk_name=None,
            status_list=None,
            source_ip=None,
            risk_levels=None,
            page_size=None,
            strategy_id=None,
            current_page=None,
            dealed=None,
            sub_type_names=None,
            uuids=None):
        api_request = APIRequest('DescribeWarning', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TypeNames": type_names,
            "RiskName": risk_name,
            "StatusList": status_list,
            "SourceIp": source_ip,
            "RiskLevels": risk_levels,
            "PageSize": page_size,
            "StrategyId": strategy_id,
            "CurrentPage": current_page,
            "Dealed": dealed,
            "SubTypeNames": sub_type_names,
            "Uuids": uuids}
        return self._handle_request(api_request).result

    def describe_vul_list(
            self,
            status_list=None,
            level=None,
            resource=None,
            cve_id=None,
            group_id=None,
            remark=None,
            dealed=None,
            current_page=None,
            type_=None,
            create_ts_start=None,
            batch_name=None,
            alias_name=None,
            source_ip=None,
            name=None,
            page_size=None,
            ids=None,
            lang=None,
            create_ts_end=None,
            necessity=None,
            uuids=None):
        api_request = APIRequest('DescribeVulList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StatusList": status_list,
            "Level": level,
            "Resource": resource,
            "CveId": cve_id,
            "GroupId": group_id,
            "Remark": remark,
            "Dealed": dealed,
            "CurrentPage": current_page,
            "Type": type_,
            "CreateTsStart": create_ts_start,
            "BatchName": batch_name,
            "AliasName": alias_name,
            "SourceIp": source_ip,
            "Name": name,
            "PageSize": page_size,
            "Ids": ids,
            "Lang": lang,
            "CreateTsEnd": create_ts_end,
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

    def describe_suspicious_events(
            self,
            source_ip=None,
            level=None,
            page_size=None,
            current_page=None,
            dealed=None,
            remark=None,
            event_type=None,
            uuid=None):
        api_request = APIRequest('DescribeSuspiciousEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Level": level,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Dealed": dealed,
            "Remark": remark,
            "EventType": event_type,
            "Uuid": uuid}
        return self._handle_request(api_request).result

    def describe_stratety_detail(self, source_ip=None, id_=None, lang=None):
        api_request = APIRequest('DescribeStratetyDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Id": id_, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_stratety(self, source_ip=None, strategy_ids=None, lang=None):
        api_request = APIRequest('DescribeStratety', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "StrategyIds": strategy_ids, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_strategy_target(self, source_ip=None, type_=None, config=None):
        api_request = APIRequest('DescribeStrategyTarget', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Type": type_, "Config": config}
        return self._handle_request(api_request).result

    def describe_login_logs(
            self,
            types=None,
            source_ip=None,
            page_size=None,
            statuses=None,
            current_page=None,
            remark=None,
            tag=None):
        api_request = APIRequest('DescribeLoginLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Types": types,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "Statuses": statuses,
            "CurrentPage": current_page,
            "Remark": remark,
            "Tag": tag}
        return self._handle_request(api_request).result

    def delete_strategy(self, source_ip=None, id_=None):
        api_request = APIRequest('DeleteStrategy', 'POST', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Id": id_}
        return self._handle_request(api_request).result

    def query_login_event(
            self,
            end_time=None,
            current_page=None,
            start_time=None,
            uuid=None,
            status=None):
        api_request = APIRequest('QueryLoginEvent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndTime": end_time,
            "CurrentPage": current_page,
            "StartTime": start_time,
            "Uuid": uuid,
            "Status": status}
        return self._handle_request(api_request).result

    def query_crack_event(
            self,
            end_time=None,
            current_page=None,
            start_time=None,
            uuid=None,
            status=None):
        api_request = APIRequest('QueryCrackEvent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndTime": end_time,
            "CurrentPage": current_page,
            "StartTime": start_time,
            "Uuid": uuid,
            "Status": status}
        return self._handle_request(api_request).result

    def get_statistics_by_uuid(self, uuid=None):
        api_request = APIRequest('GetStatisticsByUuid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Uuid": uuid}
        return self._handle_request(api_request).result

    def get_statistics(self, end_time=None, start_time=None):
        api_request = APIRequest('GetStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"EndTime": end_time, "StartTime": start_time}
        return self._handle_request(api_request).result

    def get_entity_list(
            self,
            group_id=None,
            page_size=None,
            remark=None,
            event_type=None,
            current_page=None,
            region_no=None):
        api_request = APIRequest('GetEntityList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GroupId": group_id,
            "PageSize": page_size,
            "Remark": remark,
            "EventType": event_type,
            "CurrentPage": current_page,
            "RegionNo": region_no}
        return self._handle_request(api_request).result

    def get_crack_statistics(self, end_time=None, start_time=None):
        api_request = APIRequest('GetCrackStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"EndTime": end_time, "StartTime": start_time}
        return self._handle_request(api_request).result

    def get_account_statistics(self, end_time=None, start_time=None):
        api_request = APIRequest('GetAccountStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"EndTime": end_time, "StartTime": start_time}
        return self._handle_request(api_request).result

    def upgrade_instance(
            self,
            instance_id=None,
            client_token=None,
            vm_number=None,
            owner_id=None,
            version_code=None):
        api_request = APIRequest('UpgradeInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "ClientToken": client_token,
            "VmNumber": vm_number,
            "OwnerId": owner_id,
            "VersionCode": version_code}
        return self._handle_request(api_request).result

    def renew_instance(
            self,
            duration=None,
            instance_id=None,
            client_token=None,
            vm_number=None,
            owner_id=None,
            pricing_cycle=None):
        api_request = APIRequest('RenewInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "InstanceId": instance_id,
            "ClientToken": client_token,
            "VmNumber": vm_number,
            "OwnerId": owner_id,
            "PricingCycle": pricing_cycle}
        return self._handle_request(api_request).result

    def release_instance(self, instance_id=None, owner_id=None):
        api_request = APIRequest('ReleaseInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_instance(
            self,
            duration=None,
            is_auto_renew=None,
            client_token=None,
            vm_number=None,
            owner_id=None,
            version_code=None,
            pricing_cycle=None,
            auto_renew_duration=None):
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "IsAutoRenew": is_auto_renew,
            "ClientToken": client_token,
            "VmNumber": vm_number,
            "OwnerId": owner_id,
            "VersionCode": version_code,
            "PricingCycle": pricing_cycle,
            "AutoRenewDuration": auto_renew_duration}
        return self._handle_request(api_request).result
