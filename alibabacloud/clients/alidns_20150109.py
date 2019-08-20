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


class AlidnsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Alidns'
        self.api_version = '2015-01-09'
        self.location_service_code = 'Alidns'
        self.location_endpoint_type = 'openAPI'

    def describe_gtm_recovery_plan(self, user_client_ip=None, recovery_plan_id=None, lang=None):
        api_request = APIRequest('DescribeGtmRecoveryPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "RecoveryPlanId": recovery_plan_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def add_gtm_recovery_plan(
            self,
            fault_addr_pool=None,
            user_client_ip=None,
            name=None,
            remark=None,
            lang=None):
        api_request = APIRequest('AddGtmRecoveryPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FaultAddrPool": fault_addr_pool,
            "UserClientIp": user_client_ip,
            "Name": name,
            "Remark": remark,
            "Lang": lang}
        return self._handle_request(api_request).result

    def update_gtm_recovery_plan(
            self,
            fault_addr_pool=None,
            user_client_ip=None,
            name=None,
            remark=None,
            recovery_plan_id=None,
            lang=None):
        api_request = APIRequest('UpdateGtmRecoveryPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FaultAddrPool": fault_addr_pool,
            "UserClientIp": user_client_ip,
            "Name": name,
            "Remark": remark,
            "RecoveryPlanId": recovery_plan_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def delete_gtm_recovery_plan(self, user_client_ip=None, recovery_plan_id=None, lang=None):
        api_request = APIRequest('DeleteGtmRecoveryPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "RecoveryPlanId": recovery_plan_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_gtm_recovery_plans(
            self,
            user_client_ip=None,
            page_size=None,
            lang=None,
            keyword=None,
            page_number=None):
        api_request = APIRequest('DescribeGtmRecoveryPlans', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "Lang": lang,
            "Keyword": keyword,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_gtm_recovery_plan_available_config(self, user_client_ip=None, lang=None):
        api_request = APIRequest('DescribeGtmRecoveryPlanAvailableConfig',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UserClientIp": user_client_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def execute_gtm_recovery_plan(self, user_client_ip=None, recovery_plan_id=None, lang=None):
        api_request = APIRequest('ExecuteGtmRecoveryPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "RecoveryPlanId": recovery_plan_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def rollback_gtm_recovery_plan(self, user_client_ip=None, recovery_plan_id=None, lang=None):
        api_request = APIRequest('RollbackGtmRecoveryPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "RecoveryPlanId": recovery_plan_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def preview_gtm_recovery_plan(
            self,
            user_client_ip=None,
            page_size=None,
            recovery_plan_id=None,
            lang=None,
            page_number=None):
        api_request = APIRequest('PreviewGtmRecoveryPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "RecoveryPlanId": recovery_plan_id,
            "Lang": lang,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_domain_statistics(
            self,
            end_date=None,
            user_client_ip=None,
            domain_name=None,
            lang=None,
            start_date=None):
        api_request = APIRequest('DescribeDomainStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndDate": end_date,
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "Lang": lang,
            "StartDate": start_date}
        return self._handle_request(api_request).result

    def describe_record_statistics(
            self,
            rr=None,
            end_date=None,
            user_client_ip=None,
            domain_name=None,
            lang=None,
            start_date=None):
        api_request = APIRequest('DescribeRecordStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Rr": rr,
            "EndDate": end_date,
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "Lang": lang,
            "StartDate": start_date}
        return self._handle_request(api_request).result

    def describe_gtm_instance_system_cname(self, instance_id=None, user_client_ip=None, lang=None):
        api_request = APIRequest('DescribeGtmInstanceSystemCname', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "UserClientIp": user_client_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_domain_statistics_summary(
            self,
            end_date=None,
            user_client_ip=None,
            page_size=None,
            order_by=None,
            search_mode=None,
            threshold=None,
            lang=None,
            start_date=None,
            keyword=None,
            page_number=None,
            direction=None):
        api_request = APIRequest('DescribeDomainStatisticsSummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndDate": end_date,
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "OrderBy": order_by,
            "SearchMode": search_mode,
            "Threshold": threshold,
            "Lang": lang,
            "StartDate": start_date,
            "Keyword": keyword,
            "PageNumber": page_number,
            "Direction": direction}
        return self._handle_request(api_request).result

    def describe_record_statistics_summary(
            self,
            end_date=None,
            user_client_ip=None,
            page_size=None,
            domain_name=None,
            order_by=None,
            search_mode=None,
            threshold=None,
            lang=None,
            start_date=None,
            keyword=None,
            page_number=None,
            direction=None):
        api_request = APIRequest('DescribeRecordStatisticsSummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndDate": end_date,
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "DomainName": domain_name,
            "OrderBy": order_by,
            "SearchMode": search_mode,
            "Threshold": threshold,
            "Lang": lang,
            "StartDate": start_date,
            "Keyword": keyword,
            "PageNumber": page_number,
            "Direction": direction}
        return self._handle_request(api_request).result

    def operate_batch_domain(
            self,
            user_client_ip=None,
            list_of_domain_record_info=None,
            lang=None,
            type_=None):
        api_request = APIRequest('OperateBatchDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "DomainRecordInfo": list_of_domain_record_info,
            "Lang": lang,
            "Type": type_}
        repeat_info = {"DomainRecordInfo": ('DomainRecordInfo',
                                            'list',
                                            'dict',
                                            [('Rr',
                                              'str',
                                              None,
                                              None),
                                             ('NewType',
                                              'str',
                                              None,
                                              None),
                                                ('NewValue',
                                                 'str',
                                                 None,
                                                 None),
                                                ('Line',
                                                 'str',
                                                 None,
                                                 None),
                                                ('Domain',
                                                 'str',
                                                 None,
                                                 None),
                                                ('Type',
                                                 'str',
                                                 None,
                                                 None),
                                                ('Priority',
                                                 'str',
                                                 None,
                                                 None),
                                                ('Value',
                                                 'str',
                                                 None,
                                                 None),
                                                ('Ttl',
                                                 'str',
                                                 None,
                                                 None),
                                                ('NewRr',
                                                 'str',
                                                 None,
                                                 None),
                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_batch_result_detail(
            self,
            batch_type=None,
            user_client_ip=None,
            page_size=None,
            lang=None,
            page_number=None,
            task_id=None):
        api_request = APIRequest('DescribeBatchResultDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BatchType": batch_type,
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "Lang": lang,
            "PageNumber": page_number,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def describe_batch_result_count(
            self,
            batch_type=None,
            user_client_ip=None,
            lang=None,
            task_id=None):
        api_request = APIRequest('DescribeBatchResultCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BatchType": batch_type,
            "UserClientIp": user_client_ip,
            "Lang": lang,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def set_gtm_access_mode(
            self,
            user_client_ip=None,
            strategy_id=None,
            lang=None,
            access_mode=None):
        api_request = APIRequest('SetGtmAccessMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "StrategyId": strategy_id,
            "Lang": lang,
            "AccessMode": access_mode}
        return self._handle_request(api_request).result

    def set_gtm_monitor_status(
            self,
            user_client_ip=None,
            monitor_config_id=None,
            lang=None,
            status=None):
        api_request = APIRequest('SetGtmMonitorStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "MonitorConfigId": monitor_config_id,
            "Lang": lang,
            "Status": status}
        return self._handle_request(api_request).result

    def update_gtm_instance_global_config(
            self,
            alert_group=None,
            instance_id=None,
            instance_name=None,
            user_domain_name=None,
            cname_mode=None,
            user_client_ip=None,
            lba_strategy=None,
            lang=None,
            ttl=None,
            cname_custom_domain_name=None):
        api_request = APIRequest('UpdateGtmInstanceGlobalConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AlertGroup": alert_group,
            "InstanceId": instance_id,
            "InstanceName": instance_name,
            "UserDomainName": user_domain_name,
            "CnameMode": cname_mode,
            "UserClientIp": user_client_ip,
            "LbaStrategy": lba_strategy,
            "Lang": lang,
            "Ttl": ttl,
            "CnameCustomDomainName": cname_custom_domain_name}
        return self._handle_request(api_request).result

    def describe_gtm_logs(
            self,
            instance_id=None,
            user_client_ip=None,
            page_size=None,
            lang=None,
            keyword=None,
            start_timestamp=None,
            page_number=None,
            end_timestamp=None):
        api_request = APIRequest('DescribeGtmLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "Lang": lang,
            "Keyword": keyword,
            "StartTimestamp": start_timestamp,
            "PageNumber": page_number,
            "EndTimestamp": end_timestamp}
        return self._handle_request(api_request).result

    def delete_gtm_access_strategy(self, user_client_ip=None, strategy_id=None, lang=None):
        api_request = APIRequest('DeleteGtmAccessStrategy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "StrategyId": strategy_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def add_gtm_monitor(
            self,
            monitor_extend_info=None,
            addr_pool_id=None,
            user_client_ip=None,
            evaluation_count=None,
            protocol_type=None,
            interval=None,
            lang=None,
            timeout=None,
            list_of_isp_city_node=None):
        api_request = APIRequest('AddGtmMonitor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MonitorExtendInfo": monitor_extend_info,
            "AddrPoolId": addr_pool_id,
            "UserClientIp": user_client_ip,
            "EvaluationCount": evaluation_count,
            "ProtocolType": protocol_type,
            "Interval": interval,
            "Lang": lang,
            "Timeout": timeout,
            "IspCityNode": list_of_isp_city_node}
        repeat_info = {
            "IspCityNode": (
                'IspCityNode', 'list', 'dict', [
                    ('CityCode', 'str', None, None), ('IspCode', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def add_gtm_address_pool(
            self,
            monitor_extend_info=None,
            monitor_status=None,
            type_=None,
            timeout=None,
            min_available_addr_num=None,
            instance_id=None,
            user_client_ip=None,
            name=None,
            evaluation_count=None,
            protocol_type=None,
            interval=None,
            lang=None,
            list_of_addr=None,
            list_of_isp_city_node=None):
        api_request = APIRequest('AddGtmAddressPool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MonitorExtendInfo": monitor_extend_info,
            "MonitorStatus": monitor_status,
            "Type": type_,
            "Timeout": timeout,
            "MinAvailableAddrNum": min_available_addr_num,
            "InstanceId": instance_id,
            "UserClientIp": user_client_ip,
            "Name": name,
            "EvaluationCount": evaluation_count,
            "ProtocolType": protocol_type,
            "Interval": interval,
            "Lang": lang,
            "Addr": list_of_addr,
            "IspCityNode": list_of_isp_city_node}
        repeat_info = {"Addr": ('Addr', 'list', 'dict', [('Mode', 'str', None, None),
                                                         ('LbaWeight', 'str', None, None),
                                                         ('Value', 'str', None, None),
                                                         ]),
                       "IspCityNode": ('IspCityNode', 'list', 'dict', [('CityCode', 'str', None, None),
                                                                       ('IspCode', 'str', None, None),
                                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def add_gtm_access_strategy(
            self,
            strategy_name=None,
            default_addr_pool_id=None,
            access_lines=None,
            instance_id=None,
            failover_addr_pool_id=None,
            user_client_ip=None,
            lang=None):
        api_request = APIRequest('AddGtmAccessStrategy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StrategyName": strategy_name,
            "DefaultAddrPoolId": default_addr_pool_id,
            "AccessLines": access_lines,
            "InstanceId": instance_id,
            "FailoverAddrPoolId": failover_addr_pool_id,
            "UserClientIp": user_client_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_gtm_instances(
            self,
            resource_group_id=None,
            user_client_ip=None,
            page_size=None,
            lang=None,
            keyword=None,
            page_number=None,
            need_detail_attributes=None):
        api_request = APIRequest('DescribeGtmInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "Lang": lang,
            "Keyword": keyword,
            "PageNumber": page_number,
            "NeedDetailAttributes": need_detail_attributes}
        return self._handle_request(api_request).result

    def delete_gtm_address_pool(self, addr_pool_id=None, user_client_ip=None, lang=None):
        api_request = APIRequest('DeleteGtmAddressPool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AddrPoolId": addr_pool_id,
            "UserClientIp": user_client_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_gtm_access_strategies(
            self,
            instance_id=None,
            user_client_ip=None,
            page_size=None,
            lang=None,
            page_number=None):
        api_request = APIRequest('DescribeGtmAccessStrategies', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "Lang": lang,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_gtm_access_strategy(self, user_client_ip=None, strategy_id=None, lang=None):
        api_request = APIRequest('DescribeGtmAccessStrategy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "StrategyId": strategy_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_gtm_access_strategy_available_config(
            self, instance_id=None, user_client_ip=None, lang=None):
        api_request = APIRequest(
            'DescribeGtmAccessStrategyAvailableConfig',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "InstanceId": instance_id,
            "UserClientIp": user_client_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_gtm_available_alert_group(self, user_client_ip=None, lang=None):
        api_request = APIRequest('DescribeGtmAvailableAlertGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UserClientIp": user_client_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_gtm_instance(
            self,
            instance_id=None,
            user_client_ip=None,
            lang=None,
            need_detail_attributes=None):
        api_request = APIRequest('DescribeGtmInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "UserClientIp": user_client_ip,
            "Lang": lang,
            "NeedDetailAttributes": need_detail_attributes}
        return self._handle_request(api_request).result

    def describe_gtm_instance_address_pool(self, addr_pool_id=None, user_client_ip=None, lang=None):
        api_request = APIRequest('DescribeGtmInstanceAddressPool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AddrPoolId": addr_pool_id,
            "UserClientIp": user_client_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_gtm_instance_address_pools(
            self,
            instance_id=None,
            user_client_ip=None,
            page_size=None,
            lang=None,
            page_number=None):
        api_request = APIRequest('DescribeGtmInstanceAddressPools', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "Lang": lang,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_gtm_instance_status(self, instance_id=None, user_client_ip=None, lang=None):
        api_request = APIRequest('DescribeGtmInstanceStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "UserClientIp": user_client_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_gtm_monitor_available_config(self, user_client_ip=None, lang=None):
        api_request = APIRequest('DescribeGtmMonitorAvailableConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UserClientIp": user_client_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_gtm_monitor_config(self, user_client_ip=None, monitor_config_id=None, lang=None):
        api_request = APIRequest('DescribeGtmMonitorConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "MonitorConfigId": monitor_config_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def update_gtm_access_strategy(
            self,
            strategy_name=None,
            default_addr_pool_id=None,
            access_lines=None,
            failover_addr_pool_id=None,
            user_client_ip=None,
            strategy_id=None,
            lang=None):
        api_request = APIRequest('UpdateGtmAccessStrategy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StrategyName": strategy_name,
            "DefaultAddrPoolId": default_addr_pool_id,
            "AccessLines": access_lines,
            "FailoverAddrPoolId": failover_addr_pool_id,
            "UserClientIp": user_client_ip,
            "StrategyId": strategy_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def update_gtm_address_pool(
            self,
            addr_pool_id=None,
            user_client_ip=None,
            name=None,
            lang=None,
            type_=None,
            list_of_addr=None,
            min_available_addr_num=None):
        api_request = APIRequest('UpdateGtmAddressPool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AddrPoolId": addr_pool_id,
            "UserClientIp": user_client_ip,
            "Name": name,
            "Lang": lang,
            "Type": type_,
            "Addr": list_of_addr,
            "MinAvailableAddrNum": min_available_addr_num}
        repeat_info = {"Addr": ('Addr', 'list', 'dict', [('Mode', 'str', None, None),
                                                         ('LbaWeight', 'str', None, None),
                                                         ('Value', 'str', None, None),
                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def update_gtm_monitor(
            self,
            monitor_extend_info=None,
            user_client_ip=None,
            monitor_config_id=None,
            evaluation_count=None,
            protocol_type=None,
            interval=None,
            lang=None,
            timeout=None,
            list_of_isp_city_node=None):
        api_request = APIRequest('UpdateGtmMonitor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MonitorExtendInfo": monitor_extend_info,
            "UserClientIp": user_client_ip,
            "MonitorConfigId": monitor_config_id,
            "EvaluationCount": evaluation_count,
            "ProtocolType": protocol_type,
            "Interval": interval,
            "Lang": lang,
            "Timeout": timeout,
            "IspCityNode": list_of_isp_city_node}
        repeat_info = {
            "IspCityNode": (
                'IspCityNode', 'list', 'dict', [
                    ('CityCode', 'str', None, None), ('IspCode', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_instance(
            self,
            month=None,
            user_client_ip=None,
            domain_name=None,
            lang=None,
            instance_version=None,
            owner_id=None,
            token=None):
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Month": month,
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "Lang": lang,
            "InstanceVersion": instance_version,
            "OwnerId": owner_id,
            "Token": token}
        return self._handle_request(api_request).result

    def query_create_instance_price(
            self,
            month=None,
            user_client_ip=None,
            lang=None,
            instance_version=None,
            owner_id=None):
        api_request = APIRequest('QueryCreateInstancePrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Month": month,
            "UserClientIp": user_client_ip,
            "Lang": lang,
            "InstanceVersion": instance_version,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_support_lines(self, user_client_ip=None, domain_name=None, lang=None):
        api_request = APIRequest('DescribeSupportLines', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_domain_ns(self, user_client_ip=None, domain_name=None, lang=None):
        api_request = APIRequest('DescribeDomainNs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_dns_product_instance(self, instance_id=None, user_client_ip=None, lang=None):
        api_request = APIRequest('DescribeDnsProductInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "UserClientIp": user_client_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def update_domain_record(
            self,
            record_id=None,
            rr=None,
            line=None,
            user_client_ip=None,
            lang=None,
            type_=None,
            priority=None,
            value=None,
            ttl=None):
        api_request = APIRequest('UpdateDomainRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RecordId": record_id,
            "RR": rr,
            "Line": line,
            "UserClientIp": user_client_ip,
            "Lang": lang,
            "Type": type_,
            "Priority": priority,
            "Value": value,
            "TTL": ttl}
        return self._handle_request(api_request).result

    def update_domain_group(self, group_id=None, user_client_ip=None, lang=None, group_name=None):
        api_request = APIRequest('UpdateDomainGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GroupId": group_id,
            "UserClientIp": user_client_ip,
            "Lang": lang,
            "GroupName": group_name}
        return self._handle_request(api_request).result

    def update_dnsslb_weight(self, record_id=None, user_client_ip=None, weight=None, lang=None):
        api_request = APIRequest('UpdateDNSSLBWeight', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RecordId": record_id,
            "UserClientIp": user_client_ip,
            "Weight": weight,
            "Lang": lang}
        return self._handle_request(api_request).result

    def set_domain_record_status(self, record_id=None, user_client_ip=None, lang=None, status=None):
        api_request = APIRequest('SetDomainRecordStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RecordId": record_id,
            "UserClientIp": user_client_ip,
            "Lang": lang,
            "Status": status}
        return self._handle_request(api_request).result

    def set_dnsslb_status(
            self,
            user_client_ip=None,
            domain_name=None,
            sub_domain=None,
            lang=None,
            open=None):
        api_request = APIRequest('SetDNSSLBStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "SubDomain": sub_domain,
            "Lang": lang,
            "Open": open}
        return self._handle_request(api_request).result

    def modify_hichina_domain_dns(self, user_client_ip=None, domain_name=None, lang=None):
        api_request = APIRequest('ModifyHichinaDomainDNS', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "Lang": lang}
        return self._handle_request(api_request).result

    def get_main_domain_name(self, input_string=None, user_client_ip=None, lang=None):
        api_request = APIRequest('GetMainDomainName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InputString": input_string,
            "UserClientIp": user_client_ip,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_sub_domain_records(
            self,
            line=None,
            user_client_ip=None,
            page_size=None,
            domain_name=None,
            sub_domain=None,
            lang=None,
            type_=None,
            page_number=None):
        api_request = APIRequest('DescribeSubDomainRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Line": line,
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "DomainName": domain_name,
            "SubDomain": sub_domain,
            "Lang": lang,
            "Type": type_,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_record_logs(
            self,
            end_date=None,
            user_client_ip=None,
            domain_name=None,
            page_size=None,
            lang=None,
            key_word=None,
            start_date=None,
            page_number=None):
        api_request = APIRequest('DescribeRecordLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "endDate": end_date,
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "PageSize": page_size,
            "Lang": lang,
            "KeyWord": key_word,
            "StartDate": start_date,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_domains(
            self,
            resource_group_id=None,
            group_id=None,
            user_client_ip=None,
            page_size=None,
            search_mode=None,
            lang=None,
            key_word=None,
            page_number=None):
        api_request = APIRequest('DescribeDomains', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "GroupId": group_id,
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "SearchMode": search_mode,
            "Lang": lang,
            "KeyWord": key_word,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_domain_records(
            self,
            value_key_word=None,
            line=None,
            group_id=None,
            domain_name=None,
            order_by=None,
            type_=None,
            page_number=None,
            user_client_ip=None,
            page_size=None,
            search_mode=None,
            lang=None,
            key_word=None,
            type_key_word=None,
            rr_key_word=None,
            direction=None,
            status=None):
        api_request = APIRequest('DescribeDomainRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ValueKeyWord": value_key_word,
            "Line": line,
            "GroupId": group_id,
            "DomainName": domain_name,
            "OrderBy": order_by,
            "Type": type_,
            "PageNumber": page_number,
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "SearchMode": search_mode,
            "Lang": lang,
            "KeyWord": key_word,
            "TypeKeyWord": type_key_word,
            "RRKeyWord": rr_key_word,
            "Direction": direction,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_domain_record_info(self, record_id=None, user_client_ip=None, lang=None):
        api_request = APIRequest('DescribeDomainRecordInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RecordId": record_id, "UserClientIp": user_client_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_domain_logs(
            self,
            end_date=None,
            group_id=None,
            user_client_ip=None,
            page_size=None,
            lang=None,
            key_word=None,
            start_date=None,
            type_=None,
            page_number=None):
        api_request = APIRequest('DescribeDomainLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "endDate": end_date,
            "GroupId": group_id,
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "Lang": lang,
            "KeyWord": key_word,
            "StartDate": start_date,
            "Type": type_,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_domain_info(
            self,
            user_client_ip=None,
            domain_name=None,
            lang=None,
            need_detail_attributes=None):
        api_request = APIRequest('DescribeDomainInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "Lang": lang,
            "NeedDetailAttributes": need_detail_attributes}
        return self._handle_request(api_request).result

    def describe_domain_groups(
            self,
            user_client_ip=None,
            page_size=None,
            lang=None,
            key_word=None,
            page_number=None):
        api_request = APIRequest('DescribeDomainGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "Lang": lang,
            "KeyWord": key_word,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_dnsslb_sub_domains(
            self,
            user_client_ip=None,
            domain_name=None,
            page_size=None,
            lang=None,
            page_number=None):
        api_request = APIRequest('DescribeDNSSLBSubDomains', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "PageSize": page_size,
            "Lang": lang,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_dns_product_instances(
            self,
            user_client_ip=None,
            page_size=None,
            lang=None,
            version_code=None,
            page_number=None):
        api_request = APIRequest('DescribeDnsProductInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "PageSize": page_size,
            "Lang": lang,
            "VersionCode": version_code,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_sub_domain_records(
            self,
            rr=None,
            user_client_ip=None,
            domain_name=None,
            lang=None,
            type_=None):
        api_request = APIRequest('DeleteSubDomainRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RR": rr,
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "Lang": lang,
            "Type": type_}
        return self._handle_request(api_request).result

    def delete_domain_record(self, record_id=None, user_client_ip=None, lang=None):
        api_request = APIRequest('DeleteDomainRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RecordId": record_id, "UserClientIp": user_client_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def delete_domain_group(self, group_id=None, user_client_ip=None, lang=None):
        api_request = APIRequest('DeleteDomainGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"GroupId": group_id, "UserClientIp": user_client_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def delete_domain(self, user_client_ip=None, domain_name=None, lang=None):
        api_request = APIRequest('DeleteDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "Lang": lang}
        return self._handle_request(api_request).result

    def check_domain_record(
            self,
            rr=None,
            user_client_ip=None,
            domain_name=None,
            lang=None,
            type_=None,
            value=None):
        api_request = APIRequest('CheckDomainRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RR": rr,
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "Lang": lang,
            "Type": type_,
            "Value": value}
        return self._handle_request(api_request).result

    def change_domain_of_dns_product(
            self,
            instance_id=None,
            new_domain=None,
            user_client_ip=None,
            force=None,
            lang=None):
        api_request = APIRequest('ChangeDomainOfDnsProduct', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "NewDomain": new_domain,
            "UserClientIp": user_client_ip,
            "Force": force,
            "Lang": lang}
        return self._handle_request(api_request).result

    def change_domain_group(self, group_id=None, user_client_ip=None, domain_name=None, lang=None):
        api_request = APIRequest('ChangeDomainGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GroupId": group_id,
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "Lang": lang}
        return self._handle_request(api_request).result

    def add_domain_record(
            self,
            rr=None,
            line=None,
            user_client_ip=None,
            domain_name=None,
            lang=None,
            type_=None,
            priority=None,
            value=None,
            ttl=None):
        api_request = APIRequest('AddDomainRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RR": rr,
            "Line": line,
            "UserClientIp": user_client_ip,
            "DomainName": domain_name,
            "Lang": lang,
            "Type": type_,
            "Priority": priority,
            "Value": value,
            "TTL": ttl}
        return self._handle_request(api_request).result

    def add_domain_group(self, user_client_ip=None, lang=None, group_name=None):
        api_request = APIRequest('AddDomainGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserClientIp": user_client_ip,
            "Lang": lang,
            "GroupName": group_name}
        return self._handle_request(api_request).result

    def add_domain(
            self,
            resource_group_id=None,
            group_id=None,
            domain_name=None,
            user_client_ip=None,
            lang=None):
        api_request = APIRequest('AddDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "GroupId": group_id,
            "DomainName": domain_name,
            "UserClientIp": user_client_ip,
            "Lang": lang}
        return self._handle_request(api_request).result
