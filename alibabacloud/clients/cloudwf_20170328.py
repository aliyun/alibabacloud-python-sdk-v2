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


class CloudwfClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'cloudwf'
        self.api_version = '2017-03-28'
        self.location_service_code = 'cloudwf'
        self.location_endpoint_type = 'openAPI'

    def config_auto_renew(
            self,
            offset_days=None,
            months=None,
            auto_renew=None,
            list_of_ap_list=None):
        api_request = APIRequest('ConfigAutoRenew', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OffsetDays": offset_days,
            "Months": months,
            "AutoRenew": auto_renew,
            "ApList": list_of_ap_list}
        repeat_info = {"ApList": ('ApList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_sta_top(self, apgroup_id=None):
        api_request = APIRequest('GetStaTop', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApgroupId": apgroup_id}
        return self._handle_request(api_request).result

    def get_scan_probe_time_ser(
            self,
            zoom_start=None,
            company_id=None,
            apgroup_id=None,
            start=None,
            zoom_end=None,
            end=None):
        api_request = APIRequest('GetScanProbeTimeSer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ZoomStart": zoom_start,
            "CompanyId": company_id,
            "ApgroupId": apgroup_id,
            "Start": start,
            "ZoomEnd": zoom_end,
            "End": end}
        return self._handle_request(api_request).result

    def get_daily_statistic(self, apgroup_id=None):
        api_request = APIRequest('GetDailyStatistic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApgroupId": apgroup_id}
        return self._handle_request(api_request).result

    def get_ap_top(self, apgroup_id=None):
        api_request = APIRequest('GetApTop', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApgroupId": apgroup_id}
        return self._handle_request(api_request).result

    def get_ap_sta_misc_agg(self, apgroup_id=None):
        api_request = APIRequest('GetApStaMiscAgg', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApgroupId": apgroup_id}
        return self._handle_request(api_request).result

    def query_renew_price(self, time_cycle_num=None, list_of_ap_list=None):
        api_request = APIRequest('QueryRenewPrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TimeCycleNum": time_cycle_num, "ApList": list_of_ap_list}
        repeat_info = {"ApList": ('ApList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_renew_order(self, time_cycle_num=None, list_of_ap_list=None):
        api_request = APIRequest('CreateRenewOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TimeCycleNum": time_cycle_num, "ApList": list_of_ap_list}
        repeat_info = {"ApList": ('ApList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_page_properties(self,):
        api_request = APIRequest('GetPageProperties', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def modify_sub_account_permission(
            self,
            list_of_shop_group_ids=None,
            list_of_shop_ids=None,
            page_permission=None,
            id_=None,
            list_of_business_ids=None):
        api_request = APIRequest('ModifySubAccountPermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ShopGroupIds": list_of_shop_group_ids,
            "ShopIds": list_of_shop_ids,
            "PagePermission": page_permission,
            "Id": id_,
            "BusinessIds": list_of_business_ids}
        repeat_info = {"ShopGroupIds": ('ShopGroupIds', 'list', 'str', None),
                       "ShopIds": ('ShopIds', 'list', 'str', None),
                       "BusinessIds": ('BusinessIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_sub_account_permission(self, search_uid=None, length=None, page_index=None):
        api_request = APIRequest('ListSubAccountPermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SearchUid": search_uid, "Length": length, "PageIndex": page_index}
        return self._handle_request(api_request).result

    def list_businesses(self,):
        api_request = APIRequest('ListBusinesses', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def list_business_details(
            self,
            order_col=None,
            search_name=None,
            length=None,
            page_index=None,
            order_dir=None):
        api_request = APIRequest('ListBusinessDetails', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "SearchName": search_name,
            "Length": length,
            "PageIndex": page_index,
            "OrderDir": order_dir}
        return self._handle_request(api_request).result

    def get_sub_account_permission(self, id_=None):
        api_request = APIRequest('GetSubAccountPermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_sids_and_gids4_bid(self, query_type=None, query_id=None):
        api_request = APIRequest('GetSidsAndGids4Bid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"QueryType": query_type, "QueryId": query_id}
        return self._handle_request(api_request).result

    def get_bids4_uid4_root(self, uid=None):
        api_request = APIRequest('GetBids4Uid4Root', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Uid": uid}
        return self._handle_request(api_request).result

    def get_all_active_shop_by_group(self, list_of_gids=None, bid=None):
        api_request = APIRequest('GetAllActiveShopByGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gids": list_of_gids, "Bid": bid}
        repeat_info = {"Gids": ('Gids', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def del_sub_account_permission(self, id_=None):
        api_request = APIRequest('DelSubAccountPermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def create_sub_account_permission(
            self,
            uid=None,
            list_of_shop_group_ids=None,
            list_of_shop_ids=None,
            page_permission=None,
            permission_type=None,
            list_of_business_ids=None):
        api_request = APIRequest('CreateSubAccountPermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Uid": uid,
            "ShopGroupIds": list_of_shop_group_ids,
            "ShopIds": list_of_shop_ids,
            "PagePermission": page_permission,
            "PermissionType": permission_type,
            "BusinessIds": list_of_business_ids}
        repeat_info = {"ShopGroupIds": ('ShopGroupIds', 'list', 'str', None),
                       "ShopIds": ('ShopIds', 'list', 'str', None),
                       "BusinessIds": ('BusinessIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_ap_portal_bind(self, config_type=None, bind_id=None):
        api_request = APIRequest('GetApPortalBind', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ConfigType": config_type, "BindId": bind_id}
        return self._handle_request(api_request).result

    def oem_heat_setting(self, gsid=None):
        api_request = APIRequest('OemHeatSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def oem_heat_map(self, gsid=None):
        api_request = APIRequest('OemHeatMap', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def oem_heat_line(self, gsid=None):
        api_request = APIRequest('OemHeatLine', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def save_umeng_page_permission4_root(
            self,
            gs_permission=None,
            aliyun_pk=None,
            page_permission=None,
            id_=None,
            bid=None):
        api_request = APIRequest('SaveUmengPagePermission4Root', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GsPermission": gs_permission,
            "AliyunPk": aliyun_pk,
            "PagePermission": page_permission,
            "Id": id_,
            "Bid": bid}
        return self._handle_request(api_request).result

    def save_page_config_template(
            self,
            temp_type=None,
            temp_desc=None,
            temp_name=None,
            id_=None,
            temp_permission=None):
        api_request = APIRequest('SavePageConfigTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TempType": temp_type,
            "TempDesc": temp_desc,
            "TempName": temp_name,
            "Id": id_,
            "TempPermission": temp_permission}
        return self._handle_request(api_request).result

    def oem_siting_selction(self, bid=None):
        api_request = APIRequest('OemSitingSelction', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def oem_siting_contrast(self, bid=None):
        api_request = APIRequest('OemSitingContrast', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def oem_marketing_setting_data(self, bid=None):
        api_request = APIRequest('OemMarketingSettingData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def oem_marketing_potential(self, bid=None):
        api_request = APIRequest('OemMarketingPotential', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def oem_marketing_customer(self, bid=None):
        api_request = APIRequest('OemMarketingCustomer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def oem_flowrate_ranking(self, bid=None):
        api_request = APIRequest('OemFlowrateRanking', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def oem_flowrate_overview(self, bid=None):
        api_request = APIRequest('OemFlowrateOverview', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def oem_flowrate_monitor(self, gsid=None):
        api_request = APIRequest('OemFlowrateMonitor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def oem_flowrate_intelligent(self, gsid=None):
        api_request = APIRequest('OemFlowrateIntelligent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def oem_flowrate_analyse(self, gsid=None):
        api_request = APIRequest('OemFlowrateAnalyse', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def list_umeng_page_permission4_root(
            self,
            order_col=None,
            length=None,
            search_email=None,
            page_index=None,
            order_dir=None):
        api_request = APIRequest('ListUmengPagePermission4Root', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "Length": length,
            "SearchEmail": search_email,
            "PageIndex": page_index,
            "OrderDir": order_dir}
        return self._handle_request(api_request).result

    def list_page_config_template(self, length=None, page_index=None, search_temp_name=None):
        api_request = APIRequest('ListPageConfigTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Length": length,
            "PageIndex": page_index,
            "SearchTempName": search_temp_name}
        return self._handle_request(api_request).result

    def get_user_umeng_page_permission(self, bid=None):
        api_request = APIRequest('GetUserUmengPagePermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def get_umeng_page_permission4_root(self, id_=None):
        api_request = APIRequest('GetUmengPagePermission4Root', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_page_config_template(self, id_=None):
        api_request = APIRequest('GetPageConfigTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def del_umeng_page_permission4_root(self, id_=None):
        api_request = APIRequest('DelUmengPagePermission4Root', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def del_page_config_template(self, id_=None):
        api_request = APIRequest('DelPageConfigTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def upgrade_ap_group(self, list_of_ids=None):
        api_request = APIRequest('UpgradeAPGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Ids": list_of_ids}
        repeat_info = {"Ids": ('Ids', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def upgrade_ap(self, list_of_ids=None):
        api_request = APIRequest('UpgradeAP', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Ids": list_of_ids}
        repeat_info = {"Ids": ('Ids', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def set_upgrade_img_by_model(
            self,
            img_addr=None,
            img_version=None,
            ap_model_id=None,
            comment=None):
        api_request = APIRequest('SetUpgradeImgByModel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ImgAddr": img_addr,
            "ImgVersion": img_version,
            "ApModelId": ap_model_id,
            "Comment": comment}
        return self._handle_request(api_request).result

    def send_command_by_mac(self, list_of_mac_list=None, command=None):
        api_request = APIRequest('SendCommandByMac', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MacList": list_of_mac_list, "Command": command}
        repeat_info = {"MacList": ('MacList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_upgrade_img(self, length=None, page_index=None):
        api_request = APIRequest('ListUpgradeImg', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Length": length, "PageIndex": page_index}
        return self._handle_request(api_request).result

    def list_probeinfo(
            self,
            order_col=None,
            search_user_mac=None,
            search_sensor_mac=None,
            length=None,
            search_sensor_name=None,
            page_index=None,
            order_dir=None):
        api_request = APIRequest('ListProbeinfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "SearchUserMac": search_user_mac,
            "SearchSensorMac": search_sensor_mac,
            "Length": length,
            "SearchSensorName": search_sensor_name,
            "PageIndex": page_index,
            "OrderDir": order_dir}
        return self._handle_request(api_request).result

    def list_ap_upgrade(
            self,
            order_col=None,
            search_name=None,
            search_ap_model_name=None,
            length=None,
            search_mac=None,
            page_index=None,
            order_dir=None):
        api_request = APIRequest('ListApUpgrade', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "SearchName": search_name,
            "SearchApModelName": search_ap_model_name,
            "Length": length,
            "SearchMac": search_mac,
            "PageIndex": page_index,
            "OrderDir": order_dir}
        return self._handle_request(api_request).result

    def get_upgrade_img(self, id_=None):
        api_request = APIRequest('GetUpgradeImg', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_upgrade_ap_progress(self,):
        api_request = APIRequest('GetUpgradeAPProgress', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def get_upgrade_ap_group_progress(self,):
        api_request = APIRequest('GetUpgradeAPGroupProgress', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def get_send_command_by_mac_progress(self,):
        api_request = APIRequest('GetSendCommandByMacProgress', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def get_device_info_by_mac(self, mac=None):
        api_request = APIRequest('GetDeviceInfoByMac', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Mac": mac}
        return self._handle_request(api_request).result

    def get_all_ap_model(self,):
        api_request = APIRequest('GetAllApModel', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def check_root_permission(self,):
        api_request = APIRequest('CheckRootPermission', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def get_instance_by_shop(self, shop_id=None):
        api_request = APIRequest('GetInstanceByShop', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ShopId": shop_id}
        return self._handle_request(api_request).result

    def save_portal_template(
            self,
            text_content=None,
            temp_name=None,
            text_align=None,
            text_color=None,
            id_=None,
            oss_file_id=None):
        api_request = APIRequest('SavePortalTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TextContent": text_content,
            "TempName": temp_name,
            "TextAlign": text_align,
            "TextColor": text_color,
            "Id": id_,
            "OssFileId": oss_file_id}
        return self._handle_request(api_request).result

    def resume_instance(self, trace_id=None, sp_msg=None):
        api_request = APIRequest('ResumeInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TraceId": trace_id, "SpMsg": sp_msg}
        return self._handle_request(api_request).result

    def release_instance(self, trace_id=None, sp_msg=None):
        api_request = APIRequest('ReleaseInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TraceId": trace_id, "SpMsg": sp_msg}
        return self._handle_request(api_request).result

    def produce_instance(self, trace_id=None, produce_parameter=None):
        api_request = APIRequest('ProduceInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TraceId": trace_id, "ProduceParameter": produce_parameter}
        return self._handle_request(api_request).result

    def list_portal_template(
            self,
            order_col=None,
            length=None,
            page_index=None,
            order_dir=None,
            search_temp_name=None):
        api_request = APIRequest('ListPortalTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "Length": length,
            "PageIndex": page_index,
            "OrderDir": order_dir,
            "SearchTempName": search_temp_name}
        return self._handle_request(api_request).result

    def get_portal_temp_detail(self, id_=None, unique_id=None):
        api_request = APIRequest('GetPortalTempDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "UniqueId": unique_id}
        return self._handle_request(api_request).result

    def del_portal_temp(self, id_=None):
        api_request = APIRequest('DelPortalTemp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def cease_instance(self, trace_id=None, sp_msg=None):
        api_request = APIRequest('CeaseInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TraceId": trace_id, "SpMsg": sp_msg}
        return self._handle_request(api_request).result

    def reset_ap_config(self, id_=None):
        api_request = APIRequest('ResetApConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def report_zone_realtime(self, agsid=None):
        api_request = APIRequest('ReportZoneRealtime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Agsid": agsid}
        return self._handle_request(api_request).result

    def report_zone_minute(self, begin_date=None, end_date=None, agsid=None):
        api_request = APIRequest('ReportZoneMinute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BeginDate": begin_date, "EndDate": end_date, "Agsid": agsid}
        return self._handle_request(api_request).result

    def report_zone_hour(self, begin_date=None, end_date=None, agsid=None):
        api_request = APIRequest('ReportZoneHour', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BeginDate": begin_date, "EndDate": end_date, "Agsid": agsid}
        return self._handle_request(api_request).result

    def report_zone_day(self, begin_date=None, end_date=None, agsid=None):
        api_request = APIRequest('ReportZoneDay', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BeginDate": begin_date, "EndDate": end_date, "Agsid": agsid}
        return self._handle_request(api_request).result

    def report_realtime(self, agsid=None):
        api_request = APIRequest('ReportRealtime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Agsid": agsid}
        return self._handle_request(api_request).result

    def report_minute(self, begin_date=None, end_date=None, agsid=None):
        api_request = APIRequest('ReportMinute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BeginDate": begin_date, "EndDate": end_date, "Agsid": agsid}
        return self._handle_request(api_request).result

    def report_hour(self, begin_date=None, end_date=None, agsid=None):
        api_request = APIRequest('ReportHour', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BeginDate": begin_date, "EndDate": end_date, "Agsid": agsid}
        return self._handle_request(api_request).result

    def report_day(self, begin_date=None, end_date=None, agsid=None):
        api_request = APIRequest('ReportDay', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BeginDate": begin_date, "EndDate": end_date, "Agsid": agsid}
        return self._handle_request(api_request).result

    def set_scan_mode(self, operation=None, list_of_mac_list=None):
        api_request = APIRequest('SetScanMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Operation": operation, "MacList": list_of_mac_list}
        repeat_info = {"MacList": ('MacList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def save_probe_data_subscriber(
            self,
            api_url=None,
            param_gen_script=None,
            name=None,
            http_method=None,
            description=None,
            id_=None,
            type_=None,
            list_of_resource_ids=None):
        api_request = APIRequest('SaveProbeDataSubscriber', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ApiUrl": api_url,
            "ParamGenScript": param_gen_script,
            "Name": name,
            "HttpMethod": http_method,
            "Description": description,
            "Id": id_,
            "Type": type_,
            "ResourceIds": list_of_resource_ids}
        repeat_info = {"ResourceIds": ('ResourceIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_sub_account_status(self,):
        api_request = APIRequest('GetSubAccountStatus', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def get_scan_mode(self, list_of_mac_list=None):
        api_request = APIRequest('GetScanMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MacList": list_of_mac_list}
        repeat_info = {"MacList": ('MacList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_probe_data_subscriber_config(self, id_=None):
        api_request = APIRequest('GetProbeDataSubscriberConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def user_data_update(self, iid=None, upload_file=None, name=None, bid=None, type_=None):
        api_request = APIRequest('UserDataUpdate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Iid": iid,
            "UploadFile": upload_file,
            "Name": name,
            "Bid": bid,
            "Type": type_}
        return self._handle_request(api_request).result

    def user_data_show_list(self, iid=None, name=None, page=None, bid=None, per=None):
        api_request = APIRequest('UserDataShowList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Iid": iid, "Name": name, "Page": page, "Bid": bid, "Per": per}
        return self._handle_request(api_request).result

    def user_data_delete(self, iid=None, bid=None):
        api_request = APIRequest('UserDataDelete', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Iid": iid, "Bid": bid}
        return self._handle_request(api_request).result

    def user_data_create(self, upload_file=None, name=None, bid=None, type_=None):
        api_request = APIRequest('UserDataCreate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UploadFile": upload_file, "Name": name, "Bid": bid, "Type": type_}
        return self._handle_request(api_request).result

    def user_analyse(self, gsid=None):
        api_request = APIRequest('UserAnalyse', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def up_load_map(
            self,
            file_name=None,
            upload_id=None,
            object_name=None,
            chunk_index=None,
            chunk_cnt=None):
        api_request = APIRequest('UpLoadMap', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FileName": file_name,
            "UploadId": upload_id,
            "ObjectName": object_name,
            "ChunkIndex": chunk_index,
            "ChunkCnt": chunk_cnt}
        return self._handle_request(api_request).result

    def shop_update(
            self,
            shop_coordinate=None,
            shop_province=None,
            shop_top_type=None,
            shop_address=None,
            shop_type=None,
            warn_email=None,
            sid=None,
            shop_tel=None,
            warnp_hone=None,
            warn=None,
            shop_area=None,
            shop_remarks=None,
            shop_city=None,
            shop_subtype=None,
            shop_brand=None,
            shop_name=None,
            shop_close_warn=None,
            shop_manager=None,
            shop_business_hours=None):
        api_request = APIRequest('ShopUpdate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ShopCoordinate": shop_coordinate,
            "ShopProvince": shop_province,
            "ShopTopType": shop_top_type,
            "ShopAddress": shop_address,
            "ShopType": shop_type,
            "WarnEmail": warn_email,
            "Sid": sid,
            "ShopTel": shop_tel,
            "WarnpHone": warnp_hone,
            "Warn": warn,
            "ShopArea": shop_area,
            "ShopRemarks": shop_remarks,
            "ShopCity": shop_city,
            "ShopSubtype": shop_subtype,
            "ShopBrand": shop_brand,
            "ShopName": shop_name,
            "ShopCloseWarn": shop_close_warn,
            "ShopManager": shop_manager,
            "ShopBusinessHours": shop_business_hours}
        return self._handle_request(api_request).result

    def shop_show_list(
            self,
            gid=None,
            address=None,
            name=None,
            dirc=None,
            page=None,
            bid=None,
            per=None,
            shop_status=None):
        api_request = APIRequest('ShopShowList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Gid": gid,
            "Address": address,
            "Name": name,
            "Dirc": dirc,
            "Page": page,
            "Bid": bid,
            "Per": per,
            "ShopStatus": shop_status}
        return self._handle_request(api_request).result

    def shop_setredress(
            self,
            workday=None,
            filterclose=None,
            minstoptime=None,
            holiday=None,
            hnum=None,
            sid=None,
            clerk=None,
            filterstate=None,
            wnum=None,
            state=None,
            crowdfixed=None,
            maxstoptime=None):
        api_request = APIRequest('ShopSetredress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Workday": workday,
            "Filterclose": filterclose,
            "Minstoptime": minstoptime,
            "Holiday": holiday,
            "Hnum": hnum,
            "Sid": sid,
            "Clerk": clerk,
            "Filterstate": filterstate,
            "Wnum": wnum,
            "State": state,
            "Crowdfixed": crowdfixed,
            "Maxstoptime": maxstoptime}
        return self._handle_request(api_request).result

    def shop_setfiltermac(self, mac=None, sid=None):
        api_request = APIRequest('ShopSetfiltermac', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Mac": mac, "Sid": sid}
        return self._handle_request(api_request).result

    def shop_overview(self, gsid=None):
        api_request = APIRequest('ShopOverview', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def shop_marketing_list(self, name=None, page=None, per=None, sid=None):
        api_request = APIRequest('ShopMarketingList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name, "Page": page, "Per": per, "Sid": sid}
        return self._handle_request(api_request).result

    def shop_info(self, sid=None):
        api_request = APIRequest('ShopInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Sid": sid}
        return self._handle_request(api_request).result

    def shop_group_update(self, gid=None, shop_ids=None, name=None, description=None):
        api_request = APIRequest('ShopGroupUpdate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Gid": gid,
            "ShopIds": shop_ids,
            "Name": name,
            "Description": description}
        return self._handle_request(api_request).result

    def shop_group_show_list(self, page=None, bid=None, per=None):
        api_request = APIRequest('ShopGroupShowList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Page": page, "Bid": bid, "Per": per}
        return self._handle_request(api_request).result

    def shop_group_info(self, gid=None):
        api_request = APIRequest('ShopGroupInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gid": gid}
        return self._handle_request(api_request).result

    def shop_group_delete(self, gid=None):
        api_request = APIRequest('ShopGroupDelete', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gid": gid}
        return self._handle_request(api_request).result

    def shop_group_create(self, shop_ids=None, name=None, description=None, bid=None):
        api_request = APIRequest('ShopGroupCreate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ShopIds": shop_ids,
            "Name": name,
            "Description": description,
            "Bid": bid}
        return self._handle_request(api_request).result

    def shop_getredress(self, sid=None):
        api_request = APIRequest('ShopGetredress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Sid": sid}
        return self._handle_request(api_request).result

    def shop_getfiltermac(self, sid=None):
        api_request = APIRequest('ShopGetfiltermac', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Sid": sid}
        return self._handle_request(api_request).result

    def shop_deletemarketing(self, id_=None, sid=None):
        api_request = APIRequest('ShopDeletemarketing', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "Sid": sid}
        return self._handle_request(api_request).result

    def shop_delete(self, sid=None):
        api_request = APIRequest('ShopDelete', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Sid": sid}
        return self._handle_request(api_request).result

    def shop_data_alarm(
            self,
            warn_phone=None,
            warn=None,
            close_warn=None,
            warn_email=None,
            sid=None):
        api_request = APIRequest('ShopDataAlarm', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WarnPhone": warn_phone,
            "Warn": warn,
            "CloseWarn": close_warn,
            "WarnEmail": warn_email,
            "Sid": sid}
        return self._handle_request(api_request).result

    def shop_createmarketing(self, etime=None, name=None, stime=None, sid=None):
        api_request = APIRequest('ShopCreatemarketing', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Etime": etime, "Name": name, "Stime": stime, "Sid": sid}
        return self._handle_request(api_request).result

    def shop_create(
            self,
            shop_coordinate=None,
            shop_province=None,
            shop_top_type=None,
            shop_address=None,
            shop_type=None,
            warn_email=None,
            shop_tel=None,
            warnp_hone=None,
            warn=None,
            shop_area=None,
            shop_remarks=None,
            shop_city=None,
            shop_subtype=None,
            shop_brand=None,
            shop_name=None,
            shop_close_warn=None,
            bid=None,
            shop_manager=None,
            shop_business_hours=None):
        api_request = APIRequest('ShopCreate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ShopCoordinate": shop_coordinate,
            "ShopProvince": shop_province,
            "ShopTopType": shop_top_type,
            "ShopAddress": shop_address,
            "ShopType": shop_type,
            "WarnEmail": warn_email,
            "ShopTel": shop_tel,
            "WarnpHone": warnp_hone,
            "Warn": warn,
            "ShopArea": shop_area,
            "ShopRemarks": shop_remarks,
            "ShopCity": shop_city,
            "ShopSubtype": shop_subtype,
            "ShopBrand": shop_brand,
            "ShopName": shop_name,
            "ShopCloseWarn": shop_close_warn,
            "Bid": bid,
            "ShopManager": shop_manager,
            "ShopBusinessHours": shop_business_hours}
        return self._handle_request(api_request).result

    def shop_camera(self, gsid=None):
        api_request = APIRequest('ShopCamera', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def shop_action_returning(self, gsid=None):
        api_request = APIRequest('ShopActionReturning', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def shop_action_custome(self, gsid=None):
        api_request = APIRequest('ShopActionCustome', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def save_sta_status(self, description=None, id_=None):
        api_request = APIRequest('SaveStaStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Description": description, "Id": id_}
        return self._handle_request(api_request).result

    def save_portal_config(self, json_data=None):
        api_request = APIRequest('SavePortalConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JsonData": json_data}
        return self._handle_request(api_request).result

    def save_group_ap_radio_config(self, json_data=None):
        api_request = APIRequest('SaveGroupApRadioConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JsonData": json_data}
        return self._handle_request(api_request).result

    def save_ap_scan_config(self, json_data=None, ap_config_id=None):
        api_request = APIRequest('SaveApScanConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JsonData": json_data, "ApConfigId": ap_config_id}
        return self._handle_request(api_request).result

    def save_ap_radio_ssid_config(
            self,
            nasid=None,
            auth_port=None,
            hidden=None,
            dynamic_vlan=None,
            auth_server=None,
            secondary_acct_server=None,
            ssid=None,
            cir=None,
            mac=None,
            secondary_acct_secret=None,
            ieee80211w=None,
            network=None,
            isolate=None,
            ap_asset_id=None,
            enc_key=None,
            multicast_forward=None,
            encryption=None,
            wmm=None,
            auth_cache=None,
            disabled=None,
            id_=None,
            radio_index=None,
            ignore_weak_probe=None,
            maxassoc=None,
            acct_server=None,
            secondary_auth_server=None,
            dae_client=None,
            dae_secret=None,
            disassoc_low_ack=None,
            secondary_auth_port=None,
            acct_secret=None,
            disassoc_weak_rssi=None,
            secondary_acct_port=None,
            dae_port=None,
            ssid_lb=None,
            acct_port=None,
            max_inactivity=None,
            vlan_dhcp=None,
            instantly_effective=None,
            short_preamble=None,
            auth_secret=None,
            secondary_auth_secret=None,
            ownip=None):
        api_request = APIRequest('SaveApRadioSsidConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Nasid": nasid,
            "AuthPort": auth_port,
            "Hidden": hidden,
            "DynamicVlan": dynamic_vlan,
            "AuthServer": auth_server,
            "SecondaryAcctServer": secondary_acct_server,
            "Ssid": ssid,
            "Cir": cir,
            "Mac": mac,
            "SecondaryAcctSecret": secondary_acct_secret,
            "Ieee80211w": ieee80211w,
            "Network": network,
            "Isolate": isolate,
            "ApAssetId": ap_asset_id,
            "EncKey": enc_key,
            "MulticastForward": multicast_forward,
            "Encryption": encryption,
            "Wmm": wmm,
            "AuthCache": auth_cache,
            "Disabled": disabled,
            "Id": id_,
            "RadioIndex": radio_index,
            "IgnoreWeakProbe": ignore_weak_probe,
            "Maxassoc": maxassoc,
            "AcctServer": acct_server,
            "SecondaryAuthServer": secondary_auth_server,
            "DaeClient": dae_client,
            "DaeSecret": dae_secret,
            "DisassocLowAck": disassoc_low_ack,
            "SecondaryAuthPort": secondary_auth_port,
            "AcctSecret": acct_secret,
            "DisassocWeakRssi": disassoc_weak_rssi,
            "SecondaryAcctPort": secondary_acct_port,
            "DaePort": dae_port,
            "SsidLb": ssid_lb,
            "AcctPort": acct_port,
            "MaxInactivity": max_inactivity,
            "VlanDhcp": vlan_dhcp,
            "InstantlyEffective": instantly_effective,
            "ShortPreamble": short_preamble,
            "AuthSecret": auth_secret,
            "SecondaryAuthSecret": secondary_auth_secret,
            "Ownip": ownip}
        return self._handle_request(api_request).result

    def save_ap_radio_config(
            self,
            require_mode=None,
            htmode=None,
            frag=None,
            minrate=None,
            mcast_rate=None,
            probereq=None,
            channel=None,
            shortgi=None,
            hwmode=None,
            uapsd=None,
            beacon_int=None,
            mac=None,
            rts=None,
            txpower=None,
            noscan=None,
            bcast_rate=None,
            disabled=None,
            instantly_effective=None,
            id_=None,
            radio_index=None):
        api_request = APIRequest('SaveApRadioConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RequireMode": require_mode,
            "Htmode": htmode,
            "Frag": frag,
            "Minrate": minrate,
            "McastRate": mcast_rate,
            "Probereq": probereq,
            "Channel": channel,
            "Shortgi": shortgi,
            "Hwmode": hwmode,
            "Uapsd": uapsd,
            "BeaconInt": beacon_int,
            "Mac": mac,
            "Rts": rts,
            "Txpower": txpower,
            "Noscan": noscan,
            "BcastRate": bcast_rate,
            "Disabled": disabled,
            "InstantlyEffective": instantly_effective,
            "Id": id_,
            "RadioIndex": radio_index}
        return self._handle_request(api_request).result

    def save_ap_portal_config(
            self,
            auth_key=None,
            portal_url=None,
            portal_status=None,
            whitelist=None,
            check_url=None,
            ap_config_id=None,
            auth_secret=None,
            web_auth_url=None,
            network=None):
        api_request = APIRequest('SaveApPortalConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AuthKey": auth_key,
            "PortalUrl": portal_url,
            "PortalStatus": portal_status,
            "Whitelist": whitelist,
            "CheckUrl": check_url,
            "ApConfigId": ap_config_id,
            "AuthSecret": auth_secret,
            "WebAuthUrl": web_auth_url,
            "Network": network}
        return self._handle_request(api_request).result

    def save_ap_map_info(self, json_data=None):
        api_request = APIRequest('SaveApMapInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JsonData": json_data}
        return self._handle_request(api_request).result

    def save_apgroup_ssid_config(self, json_data=None):
        api_request = APIRequest('SaveApgroupSsidConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JsonData": json_data}
        return self._handle_request(api_request).result

    def save_apgroup_scan_config(self, json_data=None, apgroup_id=None):
        api_request = APIRequest('SaveApgroupScanConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JsonData": json_data, "ApgroupId": apgroup_id}
        return self._handle_request(api_request).result

    def save_apgroup_config(
            self,
            country=None,
            log_level=None,
            name=None,
            echo_int=None,
            scan=None,
            description=None,
            id_=None,
            dai=None,
            log_ip=None):
        api_request = APIRequest('SaveApgroupConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "LogLevel": log_level,
            "Name": name,
            "EchoInt": echo_int,
            "Scan": scan,
            "Description": description,
            "Id": id_,
            "Dai": dai,
            "LogIp": log_ip}
        return self._handle_request(api_request).result

    def save_ap_config(
            self,
            country=None,
            ap_asset_id=None,
            log_level=None,
            name=None,
            echo_int=None,
            scan=None,
            description=None,
            id_=None,
            dai=None,
            log_ip=None,
            mac=None):
        api_request = APIRequest('SaveApConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "ApAssetId": ap_asset_id,
            "LogLevel": log_level,
            "Name": name,
            "EchoInt": echo_int,
            "Scan": scan,
            "Description": description,
            "Id": id_,
            "Dai": dai,
            "LogIp": log_ip,
            "Mac": mac}
        return self._handle_request(api_request).result

    def save_account_config(self, json_data=None):
        api_request = APIRequest('SaveAccountConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JsonData": json_data}
        return self._handle_request(api_request).result

    def reset_ap(self, id_=None):
        api_request = APIRequest('ResetAp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def repair_group_ap(self, id_=None):
        api_request = APIRequest('RepairGroupAp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def repair_ap(self, id_=None):
        api_request = APIRequest('RepairAp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def put_oss_file(self, json_data=None):
        api_request = APIRequest('PutOssFile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JsonData": json_data}
        return self._handle_request(api_request).result

    def profile_trade(self, begin_date=None, end_date=None, data_type=None, gsid=None):
        api_request = APIRequest('ProfileTrade', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BeginDate": begin_date,
            "EndDate": end_date,
            "DataType": data_type,
            "Gsid": gsid}
        return self._handle_request(api_request).result

    def profile_tag(
            self,
            idtype=None,
            begin_date=None,
            end_date=None,
            app_type=None,
            tag=None,
            agsid=None,
            area_number=None):
        api_request = APIRequest('ProfileTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Idtype": idtype,
            "BeginDate": begin_date,
            "EndDate": end_date,
            "AppType": app_type,
            "Tag": tag,
            "Agsid": agsid,
            "AreaNumber": area_number}
        return self._handle_request(api_request).result

    def profile_media(self, begin_date=None, end_date=None, data_type=None, gsid=None):
        api_request = APIRequest('ProfileMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BeginDate": begin_date,
            "EndDate": end_date,
            "DataType": data_type,
            "Gsid": gsid}
        return self._handle_request(api_request).result

    def profile_history_list(self, idtype=None, page=None, per=None, agsid=None):
        api_request = APIRequest('ProfileHistoryList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Idtype": idtype, "Page": page, "Per": per, "Agsid": agsid}
        return self._handle_request(api_request).result

    def profile_history(self, idtype=None, end_month=None, begin_month=None, agsid=None):
        api_request = APIRequest('ProfileHistory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Idtype": idtype,
            "EndMonth": end_month,
            "BeginMonth": begin_month,
            "Agsid": agsid}
        return self._handle_request(api_request).result

    def profile_district(self, begin_date=None, end_date=None, data_type=None, gsid=None):
        api_request = APIRequest('ProfileDistrict', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BeginDate": begin_date,
            "EndDate": end_date,
            "DataType": data_type,
            "Gsid": gsid}
        return self._handle_request(api_request).result

    def profile_consume(self, begin_date=None, end_date=None, data_type=None, gsid=None):
        api_request = APIRequest('ProfileConsume', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BeginDate": begin_date,
            "EndDate": end_date,
            "DataType": data_type,
            "Gsid": gsid}
        return self._handle_request(api_request).result

    def profile_base(self, begin_date=None, end_date=None, data_type=None, gsid=None):
        api_request = APIRequest('ProfileBase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BeginDate": begin_date,
            "EndDate": end_date,
            "DataType": data_type,
            "Gsid": gsid}
        return self._handle_request(api_request).result

    def periphery_analyse(self, gsid=None):
        api_request = APIRequest('PeripheryAnalyse', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def onoff_group_ap_radio(self, apgroup_id=None, disabled=None):
        api_request = APIRequest('OnoffGroupApRadio', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApgroupId": apgroup_id, "Disabled": disabled}
        return self._handle_request(api_request).result

    def list_sta_status(
            self,
            order_col=None,
            search_group_name=None,
            search_status=None,
            length=None,
            search_username=None,
            order_dir=None,
            search_protocal=None,
            search_ssid=None,
            search_ap_name=None,
            search_ip=None,
            page_index=None,
            search_mac=None,
            search_description=None):
        api_request = APIRequest('ListStaStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "SearchGroupName": search_group_name,
            "SearchStatus": search_status,
            "Length": length,
            "SearchUsername": search_username,
            "OrderDir": order_dir,
            "SearchProtocal": search_protocal,
            "SearchSsid": search_ssid,
            "SearchApName": search_ap_name,
            "SearchIp": search_ip,
            "PageIndex": page_index,
            "SearchMac": search_mac,
            "SearchDescription": search_description}
        return self._handle_request(api_request).result

    def list_sta_onoff_log(
            self,
            order_col=None,
            search_ssid=None,
            search_ap_name=None,
            length=None,
            search_username=None,
            page_index=None,
            id_=None,
            order_dir=None):
        api_request = APIRequest('ListStaOnoffLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "SearchSsid": search_ssid,
            "SearchApName": search_ap_name,
            "Length": length,
            "SearchUsername": search_username,
            "PageIndex": page_index,
            "Id": id_,
            "OrderDir": order_dir}
        return self._handle_request(api_request).result

    def list_group_ap_brief_config(
            self,
            order_col=None,
            search_name=None,
            apgroup_id=None,
            col_cnt=None,
            length=None,
            page_index=None,
            search_mac=None,
            order_dir=None):
        api_request = APIRequest('ListGroupApBriefConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "SearchName": search_name,
            "ApgroupId": apgroup_id,
            "ColCnt": col_cnt,
            "Length": length,
            "PageIndex": page_index,
            "SearchMac": search_mac,
            "OrderDir": order_dir}
        return self._handle_request(api_request).result

    def list_config_by_action(self, search_name=None, limit=None, action_name=None):
        api_request = APIRequest('ListConfigByAction', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SearchName": search_name, "Limit": limit, "ActionName": action_name}
        return self._handle_request(api_request).result

    def list_brief_config_by_action(self, ancestor_apgroup_id=None, limit=None, fuzzy_search=None):
        api_request = APIRequest('ListBriefConfigByAction', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AncestorApgroupId": ancestor_apgroup_id,
            "Limit": limit,
            "FuzzySearch": fuzzy_search}
        return self._handle_request(api_request).result

    def list_brief_ap_config(
            self,
            search_scan=None,
            order_col=None,
            search_name=None,
            length=None,
            search_mac=None,
            page_index=None,
            order_dir=None,
            search_model=None):
        api_request = APIRequest('ListBriefApConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SearchScan": search_scan,
            "OrderCol": order_col,
            "SearchName": search_name,
            "Length": length,
            "SearchMac": search_mac,
            "PageIndex": page_index,
            "OrderDir": order_dir,
            "SearchModel": search_model}
        return self._handle_request(api_request).result

    def list_ap_status(
            self,
            order_col=None,
            search_name=None,
            search_group_name=None,
            search_status=None,
            search_wan_ip=None,
            search_ap_model_name=None,
            length=None,
            order_dir=None,
            search_bss_equals=None,
            search_sw_version=None,
            search_company_name=None,
            search_mac=None,
            page_index=None):
        api_request = APIRequest('ListApStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "SearchName": search_name,
            "SearchGroupName": search_group_name,
            "SearchStatus": search_status,
            "SearchWanIp": search_wan_ip,
            "SearchApModelName": search_ap_model_name,
            "Length": length,
            "OrderDir": order_dir,
            "SearchBssEquals": search_bss_equals,
            "SearchSwVersion": search_sw_version,
            "SearchCompanyName": search_company_name,
            "SearchMac": search_mac,
            "PageIndex": page_index}
        return self._handle_request(api_request).result

    def list_ap_sta_status(
            self,
            order_col=None,
            search_protocal=None,
            search_ssid=None,
            search_ip=None,
            length=None,
            search_username=None,
            search_mac=None,
            page_index=None,
            id_=None,
            order_dir=None):
        api_request = APIRequest('ListApStaStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "SearchProtocal": search_protocal,
            "SearchSsid": search_ssid,
            "SearchIp": search_ip,
            "Length": length,
            "SearchUsername": search_username,
            "SearchMac": search_mac,
            "PageIndex": page_index,
            "Id": id_,
            "OrderDir": order_dir}
        return self._handle_request(api_request).result

    def list_ap_radio_status(
            self,
            search_disabled=None,
            order_col=None,
            search_name=None,
            search_channel_equals=None,
            length=None,
            search_mac=None,
            search_apgroup_name=None,
            page_index=None,
            order_dir=None,
            search_ap_status=None):
        api_request = APIRequest('ListApRadioStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SearchDisabled": search_disabled,
            "OrderCol": order_col,
            "SearchName": search_name,
            "SearchChannelEquals": search_channel_equals,
            "Length": length,
            "SearchMac": search_mac,
            "SearchApgroupName": search_apgroup_name,
            "PageIndex": page_index,
            "OrderDir": order_dir,
            "SearchApStatus": search_ap_status}
        return self._handle_request(api_request).result

    def list_ap_position_status(self, json_data=None):
        api_request = APIRequest('ListApPositionStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JsonData": json_data}
        return self._handle_request(api_request).result

    def list_ap_position_map(
            self,
            order_col=None,
            search_name=None,
            total_item=None,
            length=None,
            map_type=None,
            page_index=None,
            search_apgroup_name=None,
            order_dir=None):
        api_request = APIRequest('ListApPositionMap', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "SearchName": search_name,
            "TotalItem": total_item,
            "Length": length,
            "MapType": map_type,
            "PageIndex": page_index,
            "SearchApgroupName": search_apgroup_name,
            "OrderDir": order_dir}
        return self._handle_request(api_request).result

    def list_ap_position(self, map_id=None):
        api_request = APIRequest('ListApPosition', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MapId": map_id}
        return self._handle_request(api_request).result

    def list_apgroup_config(
            self,
            order_col=None,
            search_name=None,
            search_company=None,
            length=None,
            page_index=None,
            order_dir=None):
        api_request = APIRequest('ListApgroupConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "SearchName": search_name,
            "SearchCompany": search_company,
            "Length": length,
            "PageIndex": page_index,
            "OrderDir": order_dir}
        return self._handle_request(api_request).result

    def list_ap_detail_info(self, ap_asset_id=None):
        api_request = APIRequest('ListApDetailInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApAssetId": ap_asset_id}
        return self._handle_request(api_request).result

    def list_ap_asset_can_be_added(
            self,
            search_name=None,
            apgroup_id=None,
            length=None,
            page_index=None,
            search_mac=None,
            search_model=None):
        api_request = APIRequest('ListApAssetCanBeAdded', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SearchName": search_name,
            "ApgroupId": apgroup_id,
            "Length": length,
            "PageIndex": page_index,
            "SearchMac": search_mac,
            "SearchModel": search_model}
        return self._handle_request(api_request).result

    def list_ap_asset(
            self,
            order_col=None,
            search_name=None,
            search_serial_no=None,
            length=None,
            page_index=None,
            search_mac=None,
            order_dir=None,
            search_model=None):
        api_request = APIRequest('ListApAsset', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "SearchName": search_name,
            "SearchSerialNo": search_serial_no,
            "Length": length,
            "PageIndex": page_index,
            "SearchMac": search_mac,
            "OrderDir": order_dir,
            "SearchModel": search_model}
        return self._handle_request(api_request).result

    def list_account_config(
            self,
            order_col=None,
            length=None,
            search_email=None,
            page_index=None,
            order_dir=None):
        api_request = APIRequest('ListAccountConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OrderCol": order_col,
            "Length": length,
            "SearchEmail": search_email,
            "PageIndex": page_index,
            "OrderDir": order_dir}
        return self._handle_request(api_request).result

    def kick_sta(self, id_=None):
        api_request = APIRequest('KickSta', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def kick_and_clear_pm_kcache(self, id_=None):
        api_request = APIRequest('KickAndClearPMKcache', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def headquarters_trend(self, bid=None):
        api_request = APIRequest('HeadquartersTrend', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def headquarters_tools_o2_o(self, bid=None):
        api_request = APIRequest('HeadquartersToolsO2O', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def headquarters_tools_contrast(self, bid=None):
        api_request = APIRequest('HeadquartersToolsContrast', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def headquarters_tools_coincide(self, bid=None):
        api_request = APIRequest('HeadquartersToolsCoincide', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def headquarters_ranking(self, bid=None):
        api_request = APIRequest('HeadquartersRanking', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def headquarters_overview(self, bid=None):
        api_request = APIRequest('HeadquartersOverview', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def group_trend(self, gsid=None):
        api_request = APIRequest('GroupTrend', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def group_overview(self, gsid=None):
        api_request = APIRequest('GroupOverview', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def group_intime(self, gsid=None):
        api_request = APIRequest('GroupIntime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def group_details(self, gsid=None):
        api_request = APIRequest('GroupDetails', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def get_sta_run_history_time_ser(self, id_=None):
        api_request = APIRequest('GetStaRunHistoryTimeSer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_sta_detailed_status(self, id_=None):
        api_request = APIRequest('GetStaDetailedStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_radio_run_history_time_ser(self, id_=None):
        api_request = APIRequest('GetRadioRunHistoryTimeSer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_oss_server_sign(self, dir_type=None):
        api_request = APIRequest('GetOssServerSign', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DirType": dir_type}
        return self._handle_request(api_request).result

    def get_online_sta_time_ser(
            self,
            zoom_start=None,
            company_id=None,
            apgroup_id=None,
            start=None,
            zoom_end=None,
            end=None):
        api_request = APIRequest('GetOnlineStaTimeSer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ZoomStart": zoom_start,
            "CompanyId": company_id,
            "ApgroupId": apgroup_id,
            "Start": start,
            "ZoomEnd": zoom_end,
            "End": end}
        return self._handle_request(api_request).result

    def get_online_ap_time_ser(
            self,
            zoom_start=None,
            company_id=None,
            apgroup_id=None,
            start=None,
            zoom_end=None,
            end=None):
        api_request = APIRequest('GetOnlineApTimeSer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ZoomStart": zoom_start,
            "CompanyId": company_id,
            "ApgroupId": apgroup_id,
            "Start": start,
            "ZoomEnd": zoom_end,
            "End": end}
        return self._handle_request(api_request).result

    def get_map_url(self, map_id=None):
        api_request = APIRequest('GetMapUrl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MapId": map_id}
        return self._handle_request(api_request).result

    def get_latest_sta_statistic(self, apgroup_id=None):
        api_request = APIRequest('GetLatestStaStatistic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApgroupId": apgroup_id}
        return self._handle_request(api_request).result

    def get_latest_ap_statistic(self, apgroup_id=None):
        api_request = APIRequest('GetLatestApStatistic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApgroupId": apgroup_id}
        return self._handle_request(api_request).result

    def get_group_ap_repair_progress(self, id_=None):
        api_request = APIRequest('GetGroupApRepairProgress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_group_ap_radio_onoff_progress(self, id_=None):
        api_request = APIRequest('GetGroupApRadioOnoffProgress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_group_ap_radio_config_template(self,):
        api_request = APIRequest('GetGroupApRadioConfigTemplate', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def get_group_ap_radio_config_progress(self, id_=None):
        api_request = APIRequest('GetGroupApRadioConfigProgress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_group_ap_change_name_template(self,):
        api_request = APIRequest('GetGroupApChangeNameTemplate', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def get_crowd_list(
            self,
            gsid=None,
            class_type=None,
            gs_type=None,
            end_time=None,
            page=None,
            start_time=None,
            per=None,
            bid=None):
        api_request = APIRequest('GetCrowdList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Gsid": gsid,
            "ClassType": class_type,
            "GsType": gs_type,
            "EndTime": end_time,
            "Page": page,
            "StartTime": start_time,
            "Per": per,
            "Bid": bid}
        return self._handle_request(api_request).result

    def get_bind_ap4_umeng(self,):
        api_request = APIRequest('GetBindAp4Umeng', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def get_bid(self, length=None, page_index=None):
        api_request = APIRequest('GetBid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Length": length, "PageIndex": page_index}
        return self._handle_request(api_request).result

    def get_batch_save_ap_asset_progress(self,):
        api_request = APIRequest('GetBatchSaveApAssetProgress', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def get_ap_run_history_time_ser(self, start=None, end=None, id_=None):
        api_request = APIRequest('GetApRunHistoryTimeSer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Start": start, "End": end, "Id": id_}
        return self._handle_request(api_request).result

    def get_apgroup_ssid_config_progress(self, id_=None):
        api_request = APIRequest('GetApgroupSsidConfigProgress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_apgroup_scan_config_save_progress(self, id_=None):
        api_request = APIRequest('GetApgroupScanConfigSaveProgress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_apgroup_portal_config_progress(self, id_=None):
        api_request = APIRequest('GetApgroupPortalConfigProgress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_apgroup_detailed_config(self, id_=None):
        api_request = APIRequest('GetApgroupDetailedConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_apgroup_config_progress(self, id_=None):
        api_request = APIRequest('GetApgroupConfigProgress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_ap_detailed_status(self, id_=None):
        api_request = APIRequest('GetApDetailedStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_ap_detailed_config(self, id_=None):
        api_request = APIRequest('GetApDetailedConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_add_aps_progress(self, id_=None):
        api_request = APIRequest('GetAddApsProgress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def get_account_config(self, id_=None):
        api_request = APIRequest('GetAccountConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def frequency_analyse(self, gsid=None):
        api_request = APIRequest('FrequencyAnalyse', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Gsid": gsid}
        return self._handle_request(api_request).result

    def find_ap(self, id_=None):
        api_request = APIRequest('FindAp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def excel_to_json(self, upload_data=None):
        api_request = APIRequest('ExcelToJson', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UploadData": upload_data}
        return self._handle_request(api_request).result

    def device_update(self, device_position=None, device_name=None, did=None):
        api_request = APIRequest('DeviceUpdate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DevicePosition": device_position,
            "DeviceName": device_name,
            "Did": did}
        return self._handle_request(api_request).result

    def device_show_list(self, dirc=None, page=None, per=None, device_type=None, sid=None):
        api_request = APIRequest('DeviceShowList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Dirc": dirc,
            "Page": page,
            "Per": per,
            "DeviceType": device_type,
            "Sid": sid}
        return self._handle_request(api_request).result

    def device_delete(self, did=None, mac=None):
        api_request = APIRequest('DeviceDelete', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Did": did, "Mac": mac}
        return self._handle_request(api_request).result

    def device_create(
            self,
            device_num=None,
            device_position=None,
            device_name=None,
            device_type=None,
            sid=None):
        api_request = APIRequest('DeviceCreate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DeviceNum": device_num,
            "DevicePosition": device_position,
            "DeviceName": device_name,
            "DeviceType": device_type,
            "Sid": sid}
        return self._handle_request(api_request).result

    def device_batch_create(self, sn=None, device_type=None):
        api_request = APIRequest('DeviceBatchCreate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Sn": sn, "DeviceType": device_type}
        return self._handle_request(api_request).result

    def delete_position_map(self, map_id=None):
        api_request = APIRequest('DeletePositionMap', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MapId": map_id}
        return self._handle_request(api_request).result

    def delete_ap_radio_ssid_config(self, instantly_effective=None, id_=None):
        api_request = APIRequest('DeleteApRadioSsidConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstantlyEffective": instantly_effective, "Id": id_}
        return self._handle_request(api_request).result

    def delete_apgroup_ssid_config(self, apgroup_id=None, id_=None):
        api_request = APIRequest('DeleteApgroupSsidConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApgroupId": apgroup_id, "Id": id_}
        return self._handle_request(api_request).result

    def delete_apgroup_config(self, id_=None):
        api_request = APIRequest('DeleteApgroupConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_}
        return self._handle_request(api_request).result

    def del_ap_position(self, ap_asset_id=None, map_id=None):
        api_request = APIRequest('DelApPosition', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApAssetId": ap_asset_id, "MapId": map_id}
        return self._handle_request(api_request).result

    def check_umeng_data_analysis_permission(self,):
        api_request = APIRequest('CheckUmengDataAnalysisPermission', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def business_update(
            self,
            warn=None,
            business_city=None,
            warn_email=None,
            business_address=None,
            bid=None,
            business_manager=None,
            business_province=None):
        api_request = APIRequest('BusinessUpdate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Warn": warn,
            "BusinessCity": business_city,
            "WarnEmail": warn_email,
            "BusinessAddress": business_address,
            "Bid": bid,
            "BusinessManager": business_manager,
            "BusinessProvince": business_province}
        return self._handle_request(api_request).result

    def business_show_list(self, page=None, per=None):
        api_request = APIRequest('BusinessShowList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Page": page, "Per": per}
        return self._handle_request(api_request).result

    def business_info(self, bid=None):
        api_request = APIRequest('BusinessInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Bid": bid}
        return self._handle_request(api_request).result

    def business_create(
            self,
            business_city=None,
            combo=None,
            warn_email=None,
            business_manager=None,
            business_type=None,
            warn=None,
            business_name=None,
            business_top_type=None,
            business_address=None,
            business_tel=None,
            business_province=None,
            business_subtype=None):
        api_request = APIRequest('BusinessCreate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BusinessCity": business_city,
            "Combo": combo,
            "WarnEmail": warn_email,
            "BusinessManager": business_manager,
            "BusinessType": business_type,
            "Warn": warn,
            "BusinessName": business_name,
            "BusinessTopType": business_top_type,
            "BusinessAddress": business_address,
            "BusinessTel": business_tel,
            "BusinessProvince": business_province,
            "BusinessSubtype": business_subtype}
        return self._handle_request(api_request).result

    def batch_save_ap_position(self, json_data=None):
        api_request = APIRequest('BatchSaveApPosition', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JsonData": json_data}
        return self._handle_request(api_request).result

    def batch_register_ap_asset(self, json_data=None):
        api_request = APIRequest('BatchRegisterApAsset', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JsonData": json_data}
        return self._handle_request(api_request).result

    def batch_change_group_ap_name(self, json_data=None):
        api_request = APIRequest('BatchChangeGroupApName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JsonData": json_data}
        return self._handle_request(api_request).result

    def area_update(self, name=None, dids=None, aid=None, sid=None):
        api_request = APIRequest('AreaUpdate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name, "Dids": dids, "Aid": aid, "Sid": sid}
        return self._handle_request(api_request).result

    def area_show_list(self, page=None, per=None, sid=None):
        api_request = APIRequest('AreaShowList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Page": page, "Per": per, "Sid": sid}
        return self._handle_request(api_request).result

    def area_info(self, aid=None, sid=None):
        api_request = APIRequest('AreaInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Aid": aid, "Sid": sid}
        return self._handle_request(api_request).result

    def area_delete(self, aid=None, sid=None):
        api_request = APIRequest('AreaDelete', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Aid": aid, "Sid": sid}
        return self._handle_request(api_request).result

    def area_create(self, name=None, dids=None, sid=None):
        api_request = APIRequest('AreaCreate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name, "Dids": dids, "Sid": sid}
        return self._handle_request(api_request).result

    def apgroup_batch_delete_ap(self, ap_asset_ids=None):
        api_request = APIRequest('ApgroupBatchDeleteAp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApAssetIds": ap_asset_ids}
        return self._handle_request(api_request).result

    def apgroup_batch_add_ap(self, ap_asset_ids=None, apgroup_id=None):
        api_request = APIRequest('ApgroupBatchAddAp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApAssetIds": ap_asset_ids, "ApgroupId": apgroup_id}
        return self._handle_request(api_request).result

    def aliyun_register_ap_asset(self, apgroup_id=None, mac=None, serial_no=None):
        api_request = APIRequest('AliyunRegisterApAsset', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ApgroupId": apgroup_id, "Mac": mac, "SerialNo": serial_no}
        return self._handle_request(api_request).result

    def add_apgroup_config(self, parent_apgroup_id=None, name=None, description=None):
        api_request = APIRequest('AddApgroupConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ParentApgroupId": parent_apgroup_id,
            "Name": name,
            "Description": description}
        return self._handle_request(api_request).result

    def inner_produce_cloud_wf(self, data=None):
        api_request = APIRequest('InnerProduceCloudWF', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"data": data}
        return self._handle_request(api_request).result

    def inner_check_order(self, data=None):
        api_request = APIRequest('InnerCheckOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"data": data}
        return self._handle_request(api_request).result
