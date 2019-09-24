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


class DrdsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Drds'
        self.api_version = '2019-01-23'
        self.location_service_code = 'drds'
        self.location_endpoint_type = 'openAPI'

    def create_drds_db_pre_check(
            self,
            encode=None,
            list_of_inst_db_name=None,
            password=None,
            list_of_rds_super_account=None,
            db_name=None,
            account_name=None,
            list_of_rds_instance=None,
            type_=None,
            db_inst_type=None,
            drds_instance_id=None,
            db_instance_is_creating=None):
        api_request = APIRequest('CreateDrdsDBPreCheck', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Encode": encode,
            "InstDbName": list_of_inst_db_name,
            "Password": password,
            "RdsSuperAccount": list_of_rds_super_account,
            "DbName": db_name,
            "AccountName": account_name,
            "RdsInstance": list_of_rds_instance,
            "Type": type_,
            "DbInstType": db_inst_type,
            "DrdsInstanceId": drds_instance_id,
            "DbInstanceIsCreating": db_instance_is_creating}
        repeat_info = {"InstDbName": ('InstDbName', 'list', 'dict', [('ShardDbName', 'list', 'str', None),
                                                                     ('DbInstanceId', 'str', None, None),
                                                                     ]),
                       "RdsSuperAccount": ('RdsSuperAccount', 'list', 'dict', [('Password', 'str', None, None),
                                                                               ('AccountName', 'str', None, None),
                                                                               ('DbInstanceId', 'str', None, None),
                                                                               ]),
                       "RdsInstance": ('RdsInstance', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def check_capacity_data_ready(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('CheckCapacityDataReady', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_hi_store_instance_info(self, histore_instance_id=None, drds_instance_id=None):
        api_request = APIRequest('DescribeHiStoreInstanceInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HistoreInstanceId": histore_instance_id,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def rollback_hi_store_instance(
            self,
            histore_instance_id=None,
            region_id=None,
            drds_password=None,
            drds_instance_id=None):
        api_request = APIRequest('RollbackHiStoreInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HistoreInstanceId": histore_instance_id,
            "RegionId": region_id,
            "DrdsPassword": drds_password,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def modify_polar_db_read_weight(
            self,
            db_name=None,
            db_instance_id=None,
            weights=None,
            drds_instance_id=None,
            db_node_ids=None):
        api_request = APIRequest('ModifyPolarDbReadWeight', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "DbInstanceId": db_instance_id,
            "Weights": weights,
            "DrdsInstanceId": drds_instance_id,
            "DbNodeIds": db_node_ids}
        return self._handle_request(api_request).result

    def datalink_replication_precheck(
            self,
            db_name=None,
            src_table_name=None,
            dst_table_name=None,
            drds_instance_id=None):
        api_request = APIRequest('DatalinkReplicationPrecheck', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "SrcTableName": src_table_name,
            "DstTableName": dst_table_name,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_drds_db_relation_info(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsDbRelationInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def release_hi_store_instance(
            self,
            histore_instance_id=None,
            region_id=None,
            drds_password=None,
            drds_instance_id=None):
        api_request = APIRequest('ReleaseHiStoreInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HistoreInstanceId": histore_instance_id,
            "RegionId": region_id,
            "DrdsPassword": drds_password,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def submit_smooth_expand_pre_check(
            self,
            db_name=None,
            db_inst_type=None,
            drds_instance_id=None):
        api_request = APIRequest('SubmitSmoothExpandPreCheck', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "DbInstType": db_inst_type,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_drds_db_cluster(self, db_name=None, db_instance_id=None, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsDBCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "DbInstanceId": db_instance_id,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def pre_check_create_hi_store_instance(
            self,
            region_id=None,
            drds_password=None,
            drds_instance_id=None):
        api_request = APIRequest('PreCheckCreateHiStoreInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "DrdsPassword": drds_password,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def submit_hot_expand_pre_check_task(
            self,
            db_name=None,
            list_of_table_list=None,
            db_inst_type=None,
            drds_instance_id=None):
        api_request = APIRequest('SubmitHotExpandPreCheckTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "TableList": list_of_table_list,
            "DbInstType": db_inst_type,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {"TableList": ('TableList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def upgrade_hi_store_instance(
            self,
            histore_instance_id=None,
            region_id=None,
            drds_password=None,
            drds_instance_id=None):
        api_request = APIRequest('UpgradeHiStoreInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HistoreInstanceId": histore_instance_id,
            "RegionId": region_id,
            "DrdsPassword": drds_password,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def submit_smooth_expand_pre_check_task(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('SubmitSmoothExpandPreCheckTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_pre_check_result(self, region_id=None, drds_instance_id=None, task_id=None):
        api_request = APIRequest('DescribePreCheckResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "DrdsInstanceId": drds_instance_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def describe_drds_db_rds_relation_info(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsDbRdsRelationInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_rds_performance(
            self,
            keys=None,
            end_time=None,
            start_time=None,
            rds_instance_id=None,
            db_inst_type=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeRDSPerformance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Keys": keys,
            "EndTime": end_time,
            "StartTime": start_time,
            "RdsInstanceId": rds_instance_id,
            "DbInstType": db_inst_type,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def update_instance_network(
            self,
            retain_classic=None,
            classic_expired_days=None,
            src_instance_network_type=None,
            drds_instance_id=None):
        api_request = APIRequest('UpdateInstanceNetwork', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RetainClassic": retain_classic,
            "ClassicExpiredDays": classic_expired_days,
            "SrcInstanceNetworkType": src_instance_network_type,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_drds_sql_audit_status(self, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsSqlAuditStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_storage_instance_sub_db_info(
            self,
            instance_id=None,
            db_name=None,
            drds_instance_id=None,
            inst_type=None):
        api_request = APIRequest('DescribeStorageInstanceSubDbInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "DbName": db_name,
            "DrdsInstanceId": drds_instance_id,
            "InstType": inst_type}
        return self._handle_request(api_request).result

    def describe_drds_db_rds_name_list(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsDbRdsNameList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def switch_global_broadcast_type(self, db_name=None, region_id=None, drds_instance_id=None):
        api_request = APIRequest('SwitchGlobalBroadcastType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def reset_drds_to_rds_connections(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('ResetDrdsToRdsConnections', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_instance_switch_azone(self, drds_instance_id=None):
        api_request = APIRequest('DescribeInstanceSwitchAzone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def change_instance_azone(
            self,
            origin_azone_id=None,
            target_azone_id=None,
            drds_region_id=None,
            drds_instance_id=None):
        api_request = APIRequest('ChangeInstanceAzone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OriginAzoneId": origin_azone_id,
            "TargetAzoneId": target_azone_id,
            "DrdsRegionId": drds_region_id,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_instance_switch_network(self, drds_instance_id=None):
        api_request = APIRequest('DescribeInstanceSwitchNetwork', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def change_instance_network(
            self,
            vswitch_id=None,
            retain_classic=None,
            classic_expired_days=None,
            vpc_id=None,
            src_instance_network_type=None,
            drds_instance_id=None):
        api_request = APIRequest('ChangeInstanceNetwork', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VswitchId": vswitch_id,
            "RetainClassic": retain_classic,
            "ClassicExpiredDays": classic_expired_days,
            "VpcId": vpc_id,
            "SrcInstanceNetworkType": src_instance_network_type,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_console_config(self, type_=None):
        api_request = APIRequest('DescribeConsoleConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Type": type_}
        return self._handle_request(api_request).result

    def describe_db_instances(
            self,
            search=None,
            page_size=None,
            db_inst_type=None,
            drds_instance_id=None,
            page_number=None):
        api_request = APIRequest('DescribeDbInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Search": search,
            "PageSize": page_size,
            "DbInstType": db_inst_type,
            "DrdsInstanceId": drds_instance_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_drds_instances(
            self,
            expired=None,
            region_id=None,
            page_size=None,
            description=None,
            list_of_tag=None,
            type_=None,
            page_number=None):
        api_request = APIRequest('DescribeDrdsInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Expired": expired,
            "RegionId": region_id,
            "PageSize": page_size,
            "Description": description,
            "Tag": list_of_tag,
            "Type": type_,
            "PageNumber": page_number}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_drds_dbs(self, page_size=None, drds_instance_id=None, page_number=None):
        api_request = APIRequest('DescribeDrdsDBs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "DrdsInstanceId": drds_instance_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_drds_instance(self, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_drds_instance_version(self, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsInstanceVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_rds_super_account_instances(
            self,
            list_of_rds_instance=None,
            db_inst_type=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeRdsSuperAccountInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RdsInstance": list_of_rds_instance,
            "DbInstType": db_inst_type,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {"RdsInstance": ('RdsInstance', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_drds_db(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsDB', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def create_drds_db_preview(
            self,
            list_of_inst_db_name=None,
            db_name=None,
            account_name=None,
            order_id=None,
            list_of_rds_instance=None,
            type_=None,
            db_inst_type=None,
            drds_instance_id=None,
            db_instance_is_creating=None):
        api_request = APIRequest('CreateDrdsDBPreview', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstDbName": list_of_inst_db_name,
            "DbName": db_name,
            "AccountName": account_name,
            "OrderId": order_id,
            "RdsInstance": list_of_rds_instance,
            "Type": type_,
            "DbInstType": db_inst_type,
            "DrdsInstanceId": drds_instance_id,
            "DbInstanceIsCreating": db_instance_is_creating}
        repeat_info = {"InstDbName": ('InstDbName', 'list', 'dict', [('ShardDbName', 'list', 'str', None),
                                                                     ('DbInstanceId', 'str', None, None),
                                                                     ]),
                       "RdsInstance": ('RdsInstance', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_drds_db(
            self,
            encode=None,
            list_of_inst_db_name=None,
            password=None,
            list_of_rds_super_account=None,
            db_name=None,
            account_name=None,
            list_of_rds_instance=None,
            type_=None,
            db_inst_type=None,
            drds_instance_id=None,
            db_instance_is_creating=None):
        api_request = APIRequest('CreateDrdsDB', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Encode": encode,
            "InstDbName": list_of_inst_db_name,
            "Password": password,
            "RdsSuperAccount": list_of_rds_super_account,
            "DbName": db_name,
            "AccountName": account_name,
            "RdsInstance": list_of_rds_instance,
            "Type": type_,
            "DbInstType": db_inst_type,
            "DrdsInstanceId": drds_instance_id,
            "DbInstanceIsCreating": db_instance_is_creating}
        repeat_info = {"InstDbName": ('InstDbName', 'list', 'dict', [('ShardDbName', 'list', 'str', None),
                                                                     ('DbInstanceId', 'str', None, None),
                                                                     ]),
                       "RdsSuperAccount": ('RdsSuperAccount', 'list', 'dict', [('Password', 'str', None, None),
                                                                               ('AccountName', 'str', None, None),
                                                                               ('DbInstanceId', 'str', None, None),
                                                                               ]),
                       "RdsInstance": ('RdsInstance', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_drds_regions(self,):
        api_request = APIRequest('DescribeDrdsRegions', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def modify_rds_read_weight(
            self,
            instance_names=None,
            db_name=None,
            weights=None,
            drds_instance_id=None):
        api_request = APIRequest('ModifyRdsReadWeight', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceNames": instance_names,
            "DbName": db_name,
            "Weights": weights,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def check_drds_db_name(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('CheckDrdsDbName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_instance_accounts(self, drds_instance_id=None):
        api_request = APIRequest('DescribeInstanceAccounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_drds_db_instance(self, db_name=None, db_instance_id=None, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsDbInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "DbInstanceId": db_instance_id,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_drds_db_instances(
            self,
            db_name=None,
            page_size=None,
            drds_instance_id=None,
            page_number=None):
        api_request = APIRequest('DescribeDrdsDbInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "PageSize": page_size,
            "DrdsInstanceId": drds_instance_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_drds_sharding_dbs(self, db_name=None, db_name_pattern=None, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsShardingDbs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "DbNamePattern": db_name_pattern,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def remove_drds_instance(self, drds_instance_id=None):
        api_request = APIRequest('RemoveDrdsInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def create_instance_account(
            self,
            password=None,
            account_name=None,
            drds_instance_id=None,
            list_of_db_privilege=None):
        api_request = APIRequest('CreateInstanceAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Password": password,
            "AccountName": account_name,
            "DrdsInstanceId": drds_instance_id,
            "DbPrivilege": list_of_db_privilege}
        repeat_info = {
            "DbPrivilege": (
                'DbPrivilege', 'list', 'dict', [
                    ('DbName', 'str', None, None), ('Privilege', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_account_description(
            self,
            account_name=None,
            description=None,
            drds_instance_id=None):
        api_request = APIRequest('ModifyAccountDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccountName": account_name,
            "Description": description,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def change_account_password(self, password=None, account_name=None, drds_instance_id=None):
        api_request = APIRequest('ChangeAccountPassword', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Password": password,
            "AccountName": account_name,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def remove_instance_account(self, account_name=None, drds_instance_id=None):
        api_request = APIRequest('RemoveInstanceAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AccountName": account_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def remove_drds_db(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('RemoveDrdsDb', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def modify_account_privilege(
            self,
            account_name=None,
            drds_instance_id=None,
            list_of_db_privilege=None):
        api_request = APIRequest('ModifyAccountPrivilege', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccountName": account_name,
            "DrdsInstanceId": drds_instance_id,
            "DbPrivilege": list_of_db_privilege}
        repeat_info = {
            "DbPrivilege": (
                'DbPrivilege', 'list', 'dict', [
                    ('DbName', 'str', None, None), ('Privilege', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_drds_slow_sqls(
            self,
            db_name=None,
            page_size=None,
            end_time=None,
            start_time=None,
            drds_instance_id=None,
            page_number=None,
            exe_time=None):
        api_request = APIRequest('DescribeDrdsSlowSqls', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "DrdsInstanceId": drds_instance_id,
            "PageNumber": page_number,
            "ExeTime": exe_time}
        return self._handle_request(api_request).result

    def modify_drds_ip_white_list(
            self,
            mode=None,
            db_name=None,
            group_attribute=None,
            ip_white_list=None,
            drds_instance_id=None,
            group_name=None):
        api_request = APIRequest('ModifyDrdsIpWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Mode": mode,
            "DbName": db_name,
            "GroupAttribute": group_attribute,
            "IpWhiteList": ip_white_list,
            "DrdsInstanceId": drds_instance_id,
            "GroupName": group_name}
        return self._handle_request(api_request).result

    def describe_drds_db_ip_white_list(self, db_name=None, drds_instance_id=None, group_name=None):
        api_request = APIRequest('DescribeDrdsDBIpWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "DrdsInstanceId": drds_instance_id,
            "GroupName": group_name}
        return self._handle_request(api_request).result

    def describe_drds_tasks(self, task_type=None, db_name=None, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TaskType": task_type,
            "DbName": db_name,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def configure_drds_db_instances(
            self,
            db_name=None,
            list_of_db_instance=None,
            drds_instance_id=None):
        api_request = APIRequest('ConfigureDrdsDbInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "DbInstance": list_of_db_instance,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {"DbInstance": ('DbInstance',
                                      'list',
                                      'dict',
                                      [('SlaveDbInstanceType',
                                        'str',
                                        None,
                                        None),
                                       ('SlaveDbInstanceId',
                                        'str',
                                        None,
                                        None),
                                          ('MasterDbInstanceId',
                                           'str',
                                           None,
                                           None),
                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def restart_drds_instance(self, drds_instance_id=None):
        api_request = APIRequest('RestartDrdsInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def submit_sql_flashback_task(
            self,
            trace_id=None,
            sql_type=None,
            sql_pk=None,
            recall_restore_type=None,
            recall_type=None,
            db_name=None,
            end_time=None,
            start_time=None,
            table_name=None,
            drds_instance_id=None):
        api_request = APIRequest('SubmitSqlFlashbackTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TraceId": trace_id,
            "SqlType": sql_type,
            "SqlPk": sql_pk,
            "RecallRestoreType": recall_restore_type,
            "RecallType": recall_type,
            "DbName": db_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "TableName": table_name,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def enable_sql_flashback_match_switch(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('EnableSqlFlashbackMatchSwitch', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def pre_check_sql_flashback_task(
            self,
            db_name=None,
            end_time=None,
            start_time=None,
            drds_instance_id=None):
        api_request = APIRequest('PreCheckSqlFlashbackTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def check_sls_status(self,):
        api_request = APIRequest('CheckSlsStatus', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def disable_sql_audit(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('DisableSqlAudit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def check_sql_audit_enable_status(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('CheckSqlAuditEnableStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def enable_sql_audit(
            self,
            recall_start_timestamp=None,
            db_name=None,
            is_recall=None,
            drds_instance_id=None,
            recall_end_timestamp=None):
        api_request = APIRequest('EnableSqlAudit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RecallStartTimestamp": recall_start_timestamp,
            "DbName": db_name,
            "IsRecall": is_recall,
            "DrdsInstanceId": drds_instance_id,
            "RecallEndTimestamp": recall_end_timestamp}
        return self._handle_request(api_request).result

    def check_drds_default_role(self,):
        api_request = APIRequest('CheckDrdsDefaultRole', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def refresh_drds_atom_url(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('RefreshDrdsAtomUrl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_instance_menu_switch(self, drds_instance_id=None):
        api_request = APIRequest('DescribeInstanceMenuSwitch', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_drds_instance_level_tasks(self, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsInstanceLevelTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_back_menu(self, drds_instance_id=None):
        api_request = APIRequest('DescribeBackMenu', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_backup_dbs(
            self,
            preferred_restore_time=None,
            backup_id=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeBackupDbs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PreferredRestoreTime": preferred_restore_time,
            "BackupId": backup_id,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_backup_local(self, drds_instance_id=None):
        api_request = APIRequest('DescribeBackupLocal', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_backup_sets(self, end_time=None, start_time=None, drds_instance_id=None):
        api_request = APIRequest('DescribeBackupSets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndTime": end_time,
            "StartTime": start_time,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_backup_policy(self, drds_instance_id=None):
        api_request = APIRequest('DescribeBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_backup_times(self, drds_instance_id=None):
        api_request = APIRequest('DescribeBackupTimes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_restore_order(
            self,
            preferred_backup_time=None,
            backup_db_names=None,
            backup_id=None,
            backup_mode=None,
            backup_level=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeRestoreOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PreferredBackupTime": preferred_backup_time,
            "BackupDbNames": backup_db_names,
            "BackupId": backup_id,
            "BackupMode": backup_mode,
            "BackupLevel": backup_level,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def put_restore_pre_check(
            self,
            preferred_backup_time=None,
            backup_db_names=None,
            backup_id=None,
            backup_mode=None,
            backup_level=None,
            drds_instance_id=None):
        api_request = APIRequest('PutRestorePreCheck', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PreferredBackupTime": preferred_backup_time,
            "BackupDbNames": backup_db_names,
            "BackupId": backup_id,
            "BackupMode": backup_mode,
            "BackupLevel": backup_level,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def set_backup_local(
            self,
            local_log_retention_hours=None,
            high_space_usage_protection=None,
            local_log_retention_space=None,
            drds_instance_id=None):
        api_request = APIRequest('SetBackupLocal', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocalLogRetentionHours": local_log_retention_hours,
            "HighSpaceUsageProtection": high_space_usage_protection,
            "LocalLogRetentionSpace": local_log_retention_space,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def remove_backups_set(self, backup_id=None, drds_instance_id=None):
        api_request = APIRequest('RemoveBackupsSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BackupId": backup_id, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def set_backup_policy(
            self,
            preferred_backup_period=None,
            backup_db_names=None,
            data_backup_retention_period=None,
            preferred_backup_start_time=None,
            preferred_backup_end_time=None,
            backup_mode=None,
            backup_log=None,
            backup_level=None,
            drds_instance_id=None,
            log_backup_retention_period=None):
        api_request = APIRequest('SetBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PreferredBackupPeriod": preferred_backup_period,
            "BackupDbNames": backup_db_names,
            "DataBackupRetentionPeriod": data_backup_retention_period,
            "PreferredBackupStartTime": preferred_backup_start_time,
            "PreferredBackupEndTime": preferred_backup_end_time,
            "BackupMode": backup_mode,
            "BackupLog": backup_log,
            "BackupLevel": backup_level,
            "DrdsInstanceId": drds_instance_id,
            "LogBackupRetentionPeriod": log_backup_retention_period}
        return self._handle_request(api_request).result

    def start_restore(
            self,
            preferred_backup_time=None,
            backup_db_names=None,
            backup_id=None,
            backup_mode=None,
            backup_level=None,
            drds_instance_id=None):
        api_request = APIRequest('StartRestore', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PreferredBackupTime": preferred_backup_time,
            "BackupDbNames": backup_db_names,
            "BackupId": backup_id,
            "BackupMode": backup_mode,
            "BackupLevel": backup_level,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def check_rds_super_account(
            self,
            password=None,
            account_name=None,
            db_instance_id=None,
            drds_instance_id=None):
        api_request = APIRequest('CheckRdsSuperAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Password": password,
            "AccountName": account_name,
            "DbInstanceId": db_instance_id,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def put_start_backup(
            self,
            backup_db_names=None,
            backup_mode=None,
            backup_level=None,
            drds_instance_id=None):
        api_request = APIRequest('PutStartBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BackupDbNames": backup_db_names,
            "BackupMode": backup_mode,
            "BackupLevel": backup_level,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_drds_db_tasks(self, task_type=None, db_name=None, drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsDbTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TaskType": task_type,
            "DbName": db_name,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def submit_smooth_expand_task(
            self,
            list_of_rds_super_instances=None,
            db_name=None,
            list_of_transfer_task_infos=None,
            drds_instance_id=None,
            db_instance_is_creating=None):
        api_request = APIRequest('SubmitSmoothExpandTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RdsSuperInstances": list_of_rds_super_instances,
            "DbName": db_name,
            "TransferTaskInfos": list_of_transfer_task_infos,
            "DrdsInstanceId": drds_instance_id,
            "DbInstanceIsCreating": db_instance_is_creating}
        repeat_info = {"RdsSuperInstances": ('RdsSuperInstances',
                                             'list',
                                             'dict',
                                             [('Password',
                                               'str',
                                               None,
                                               None),
                                              ('AccountName',
                                               'str',
                                               None,
                                               None),
                                                 ('RdsName',
                                                  'str',
                                                  None,
                                                  None),
                                              ]),
                       "TransferTaskInfos": ('TransferTaskInfos',
                                             'list',
                                             'dict',
                                             [('DbName',
                                               'str',
                                               None,
                                               None),
                                              ('SrcInstanceName',
                                                 'str',
                                                 None,
                                                 None),
                                                 ('InstanceType',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('DstInstanceName',
                                                  'str',
                                                  None,
                                                  None),
                                              ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def rearrange_db_to_instance(
            self,
            choose_sub_db=None,
            list_of_instance_list=None,
            db_name=None,
            order_id=None,
            choose_rds=None,
            drds_instance_id=None):
        api_request = APIRequest('RearrangeDbToInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ChooseSubDb": choose_sub_db,
            "InstanceList": list_of_instance_list,
            "DbName": db_name,
            "OrderId": order_id,
            "ChooseRds": choose_rds,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {"InstanceList": ('InstanceList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_db_instance_dbs(
            self,
            password=None,
            account_name=None,
            db_instance_id=None,
            db_inst_type=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeDbInstanceDbs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Password": password,
            "AccountName": account_name,
            "DbInstanceId": db_instance_id,
            "DbInstType": db_inst_type,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def submit_switch_task(
            self,
            job_id=None,
            db_name=None,
            parent_job_id=None,
            drds_instance_id=None,
            expand_type=None):
        api_request = APIRequest('SubmitSwitchTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "DbName": db_name,
            "ParentJobId": parent_job_id,
            "DrdsInstanceId": drds_instance_id,
            "ExpandType": expand_type}
        return self._handle_request(api_request).result

    def submit_clean_task(
            self,
            job_id=None,
            db_name=None,
            parent_job_id=None,
            drds_instance_id=None,
            expand_type=None):
        api_request = APIRequest('SubmitCleanTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "DbName": db_name,
            "ParentJobId": parent_job_id,
            "DrdsInstanceId": drds_instance_id,
            "ExpandType": expand_type}
        return self._handle_request(api_request).result

    def submit_rollback_task(
            self,
            job_id=None,
            db_name=None,
            parent_job_id=None,
            drds_instance_id=None,
            expand_type=None):
        api_request = APIRequest('SubmitRollbackTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "DbName": db_name,
            "ParentJobId": parent_job_id,
            "DrdsInstanceId": drds_instance_id,
            "ExpandType": expand_type}
        return self._handle_request(api_request).result

    def submit_hot_expand_task(
            self,
            list_of_instance_db_mapping=None,
            list_of_mapping=None,
            task_desc=None,
            db_name=None,
            list_of_supper_account_mapping=None,
            list_of_extended_mapping=None,
            task_name=None,
            drds_instance_id=None):
        api_request = APIRequest('SubmitHotExpandTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceDbMapping": list_of_instance_db_mapping,
            "Mapping": list_of_mapping,
            "TaskDesc": task_desc,
            "DbName": db_name,
            "SupperAccountMapping": list_of_supper_account_mapping,
            "ExtendedMapping": list_of_extended_mapping,
            "TaskName": task_name,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {"InstanceDbMapping": ('InstanceDbMapping',
                                             'list',
                                             'dict',
                                             [('DbList',
                                               'str',
                                               None,
                                               None),
                                              ('InstanceName',
                                               'str',
                                               None,
                                               None),
                                              ]),
                       "Mapping": ('Mapping',
                                   'list',
                                   'dict',
                                   [('DbShardColumn',
                                     'str',
                                     None,
                                     None),
                                    ('TbShardColumn',
                                       'str',
                                       None,
                                       None),
                                       ('ShardTbValue',
                                        'str',
                                        None,
                                        None),
                                       ('HotDbName',
                                        'str',
                                        None,
                                        None),
                                       ('ShardDbValue',
                                        'str',
                                        None,
                                        None),
                                       ('HotTableName',
                                        'str',
                                        None,
                                        None),
                                       ('LogicTable',
                                        'str',
                                        None,
                                        None),
                                    ]),
                       "SupperAccountMapping": ('SupperAccountMapping',
                                                'list',
                                                'dict',
                                                [('InstanceName',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('SupperAccount',
                                                    'str',
                                                    None,
                                                    None),
                                                    ('SupperPassword',
                                                     'str',
                                                     None,
                                                     None),
                                                 ]),
                       "ExtendedMapping": ('ExtendedMapping',
                                           'list',
                                           'dict',
                                           [('SrcInstanceId',
                                             'str',
                                             None,
                                             None),
                                            ('SrcDb',
                                               'str',
                                               None,
                                               None),
                                            ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_hot_db_list(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('GetHotDbList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def get_src_rds_list(self, db_name=None, list_of_partition_mapping=None, drds_instance_id=None):
        api_request = APIRequest('GetSrcRdsList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "PartitionMapping": list_of_partition_mapping,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {"PartitionMapping": ('PartitionMapping',
                                            'list',
                                            'dict',
                                            [('DbShardValue',
                                              'str',
                                              None,
                                              None),
                                             ('HotDbName',
                                              'str',
                                              None,
                                              None),
                                                ('HotTableName',
                                                 'str',
                                                 None,
                                                 None),
                                                ('TbShardValue',
                                                 'str',
                                                 None,
                                                 None),
                                                ('LogicTable',
                                                 'str',
                                                 None,
                                                 None),
                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_logic_table_info_list(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('GetLogicTableInfoList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def check_rds_expand_status(
            self,
            list_of_instance_list=None,
            db_name=None,
            drds_instance_id=None):
        api_request = APIRequest('CheckRdsExpandStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceList": list_of_instance_list,
            "DbName": db_name,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {"InstanceList": ('InstanceList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def check_expand_status(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('CheckExpandStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def get_candidate_instance_list(
            self,
            search=None,
            db_name=None,
            across_zone=None,
            page_size=None,
            drds_instance_id=None,
            page_number=None):
        api_request = APIRequest('GetCandidateInstanceList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Search": search,
            "DbName": db_name,
            "AcrossZone": across_zone,
            "PageSize": page_size,
            "DrdsInstanceId": drds_instance_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_expand_logic_table_info_list(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('GetExpandLogicTableInfoList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_src_rds_list(
            self,
            db_name=None,
            list_of_partition_mapping=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeSrcRdsList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "PartitionMapping": list_of_partition_mapping,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {"PartitionMapping": ('PartitionMapping',
                                            'list',
                                            'dict',
                                            [('DbShardValue',
                                              'str',
                                              None,
                                              None),
                                             ('HotDbName',
                                              'str',
                                              None,
                                              None),
                                                ('HotTableName',
                                                 'str',
                                                 None,
                                                 None),
                                                ('TbShardValue',
                                                 'str',
                                                 None,
                                                 None),
                                                ('LogicTable',
                                                 'str',
                                                 None,
                                                 None),
                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_candidate_instance_list(
            self,
            search=None,
            db_name=None,
            across_zone=None,
            page_size=None,
            drds_instance_id=None,
            page_number=None):
        api_request = APIRequest('DescribeCandidateInstanceList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Search": search,
            "DbName": db_name,
            "AcrossZone": across_zone,
            "PageSize": page_size,
            "DrdsInstanceId": drds_instance_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_expand_logic_table_info_list(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('DescribeExpandLogicTableInfoList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_can_expand_instance_detail_list(
            self, current_plan=None, db_name=None, drds_instance_id=None):
        api_request = APIRequest('DescribeCanExpandInstanceDetailList',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CurrentPlan": current_plan,
            "DbName": db_name,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_hot_db_list(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('DescribeHotDbList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_sql_flashbak_task(self, drds_instance_id=None):
        api_request = APIRequest('DescribeSqlFlashbakTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def migrate_jst_drds_db_across_region(
            self,
            db_name=None,
            src_drds_instance_id=None,
            dst_drds_instance_id=None):
        api_request = APIRequest('MigrateJstDrdsDbAcrossRegion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "SrcDrdsInstanceId": src_drds_instance_id,
            "DstDrdsInstanceId": dst_drds_instance_id}
        return self._handle_request(api_request).result

    def refresh_jst_migrate_drds_db_atom_url(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('RefreshJstMigrateDrdsDbAtomUrl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_inst_db_log_info(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('DescribeInstDbLogInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_inst_db_sls_info(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('DescribeInstDbSlsInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def remove_recycle_bin_table(
            self,
            db_name=None,
            region_id=None,
            table_name=None,
            drds_instance_id=None):
        api_request = APIRequest('RemoveRecycleBinTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "TableName": table_name,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def create_shard_task(
            self,
            task_type=None,
            db_name=None,
            region_id=None,
            source_table_name=None,
            target_table_name=None,
            drds_instance_id=None):
        api_request = APIRequest('CreateShardTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TaskType": task_type,
            "DbName": db_name,
            "RegionId": region_id,
            "SourceTableName": source_table_name,
            "TargetTableName": target_table_name,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def enable_instance_ipv6_address(
            self,
            region_id=None,
            drds_password=None,
            drds_instance_id=None):
        api_request = APIRequest('EnableInstanceIpv6Address', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "DrdsPassword": drds_password,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_table(self, db_name=None, region_id=None, table_name=None, drds_instance_id=None):
        api_request = APIRequest('DescribeTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "TableName": table_name,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def upgrade_instance_version(self, region_id=None, drds_password=None, drds_instance_id=None):
        api_request = APIRequest('UpgradeInstanceVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "DrdsPassword": drds_password,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_table_list_by_type(
            self,
            table_type=None,
            db_name=None,
            region_id=None,
            query=None,
            page_size=None,
            current_page=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeTableListByType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TableType": table_type,
            "DbName": db_name,
            "RegionId": region_id,
            "Query": query,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def validate_shard_task(
            self,
            task_type=None,
            db_name=None,
            region_id=None,
            source_table_name=None,
            target_table_name=None,
            drds_instance_id=None):
        api_request = APIRequest('ValidateShardTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TaskType": task_type,
            "DbName": db_name,
            "RegionId": region_id,
            "SourceTableName": source_table_name,
            "TargetTableName": target_table_name,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_tables(
            self,
            db_name=None,
            region_id=None,
            query=None,
            page_size=None,
            current_page=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeTables', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "Query": query,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_shard_task_list(
            self,
            task_type=None,
            db_name=None,
            region_id=None,
            query=None,
            page_size=None,
            current_page=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeShardTaskList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TaskType": task_type,
            "DbName": db_name,
            "RegionId": region_id,
            "Query": query,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def create_instance_internet_address(
            self,
            region_id=None,
            drds_password=None,
            drds_instance_id=None):
        api_request = APIRequest('CreateInstanceInternetAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "DrdsPassword": drds_password,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_broadcast_tables(
            self,
            db_name=None,
            region_id=None,
            query=None,
            page_size=None,
            current_page=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeBroadcastTables', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "Query": query,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def flashback_recycle_bin_table(
            self,
            db_name=None,
            region_id=None,
            table_name=None,
            drds_instance_id=None):
        api_request = APIRequest('FlashbackRecycleBinTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "TableName": table_name,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def setup_broadcast_tables(
            self,
            db_name=None,
            region_id=None,
            active=None,
            list_of_table_name=None,
            drds_instance_id=None):
        api_request = APIRequest('SetupBroadcastTables', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "Active": active,
            "TableName": list_of_table_name,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {"TableName": ('TableName', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def rollback_instance_version(self, region_id=None, drds_password=None, drds_instance_id=None):
        api_request = APIRequest('RollbackInstanceVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "DrdsPassword": drds_password,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_global_broadcast_type(self, db_name=None, region_id=None, drds_instance_id=None):
        api_request = APIRequest('DescribeGlobalBroadcastType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def release_instance_internet_address(
            self,
            region_id=None,
            drds_password=None,
            drds_instance_id=None):
        api_request = APIRequest('ReleaseInstanceInternetAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "DrdsPassword": drds_password,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_recycle_bin_tables(self, db_name=None, region_id=None, drds_instance_id=None):
        api_request = APIRequest('DescribeRecycleBinTables', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_drds_params(
            self,
            param_level=None,
            db_name=None,
            region_id=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeDrdsParams', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ParamLevel": param_level,
            "DbName": db_name,
            "RegionId": region_id,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def delete_shard_tasks(
            self,
            db_name=None,
            region_id=None,
            list_of_table_name=None,
            drds_instance_id=None):
        api_request = APIRequest('DeleteShardTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "TableName": list_of_table_name,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {
            "TableName": (
                'TableName', 'list', 'dict', [
                    ('SourceTableName', 'str', None, None), ('TargetTableName', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def setup_table(
            self,
            db_name=None,
            region_id=None,
            allow_full_table_scan=None,
            list_of_table_name=None,
            drds_instance_id=None):
        api_request = APIRequest('SetupTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "AllowFullTableScan": allow_full_table_scan,
            "TableName": list_of_table_name,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {"TableName": ('TableName', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def setup_drds_params(
            self,
            param_level=None,
            list_of_data=None,
            region_id=None,
            drds_instance_id=None):
        api_request = APIRequest('SetupDrdsParams', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ParamLevel": param_level,
            "Data": list_of_data,
            "RegionId": region_id,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {"Data": ('Data', 'list', 'dict', [('ParamType', 'str', None, None),
                                                         ('DbName', 'str', None, None),
                                                         ('ParamRanges', 'str', None, None),
                                                         ('ParamVariableName', 'str', None, None),
                                                         ('ParamValue', 'str', None, None),
                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_recycle_bin_status(self, db_name=None, region_id=None, drds_instance_id=None):
        api_request = APIRequest('DescribeRecycleBinStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def describe_shard_task_info(
            self,
            db_name=None,
            region_id=None,
            source_table_name=None,
            target_table_name=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeShardTaskInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "SourceTableName": source_table_name,
            "TargetTableName": target_table_name,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def setup_recycle_bin_status(
            self,
            status_action=None,
            db_name=None,
            region_id=None,
            drds_instance_id=None):
        api_request = APIRequest('SetupRecycleBinStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StatusAction": status_action,
            "DbName": db_name,
            "RegionId": region_id,
            "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def untag_resources(
            self,
            all_=None,
            no_role=None,
            list_of_resource_id=None,
            region_id=None,
            list_of_tag_key=None,
            resource_type=None):
        api_request = APIRequest('UntagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "All": all_,
            "NoRole": no_role,
            "ResourceId": list_of_resource_id,
            "RegionId": region_id,
            "TagKey": list_of_tag_key,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "TagKey": ('TagKey', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_drds_instance_monitor(
            self,
            region_id=None,
            end_time=None,
            start_time=None,
            drds_instance_id=None,
            key=None,
            period_multiple=None):
        api_request = APIRequest('DescribeDrdsInstanceMonitor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "EndTime": end_time,
            "StartTime": start_time,
            "DrdsInstanceId": drds_instance_id,
            "Key": key,
            "PeriodMultiple": period_multiple}
        return self._handle_request(api_request).result

    def describe_drds_instance_db_monitor(
            self,
            db_name=None,
            region_id=None,
            end_time=None,
            start_time=None,
            drds_instance_id=None,
            key=None):
        api_request = APIRequest('DescribeDrdsInstanceDbMonitor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbName": db_name,
            "RegionId": region_id,
            "EndTime": end_time,
            "StartTime": start_time,
            "DrdsInstanceId": drds_instance_id,
            "Key": key}
        return self._handle_request(api_request).result

    def tag_resources(
            self,
            no_role=None,
            list_of_resource_id=None,
            region_id=None,
            list_of_tag=None,
            resource_type=None):
        api_request = APIRequest('TagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NoRole": no_role,
            "ResourceId": list_of_resource_id,
            "RegionId": region_id,
            "Tag": list_of_tag,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def remove_drds_db_failed_record(self, db_name=None, drds_instance_id=None):
        api_request = APIRequest('RemoveDrdsDbFailedRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DbName": db_name, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result

    def list_tag_resources(
            self,
            no_role=None,
            list_of_resource_id=None,
            region_id=None,
            next_token=None,
            list_of_tag=None,
            resource_type=None):
        api_request = APIRequest('ListTagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NoRole": no_role,
            "ResourceId": list_of_resource_id,
            "RegionId": region_id,
            "NextToken": next_token,
            "Tag": list_of_tag,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_rds_commodity(
            self,
            region_id=None,
            commodity_code=None,
            drds_instance_id=None,
            order_type=None):
        api_request = APIRequest('DescribeRdsCommodity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "CommodityCode": commodity_code,
            "DrdsInstanceId": drds_instance_id,
            "OrderType": order_type}
        return self._handle_request(api_request).result

    def describe_rds_price(self, region_id=None, params=None):
        api_request = APIRequest('DescribeRdsPrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Params": params}
        return self._handle_request(api_request).result

    def create_order_for_rds(self, region_id=None, params=None):
        api_request = APIRequest('CreateOrderForRds', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Params": params}
        return self._handle_request(api_request).result

    def describe_rds_vpc_for_zone(self, region_id=None, zone_id=None):
        api_request = APIRequest('DescribeRdsVpcForZone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "ZoneId": zone_id}
        return self._handle_request(api_request).result

    def describe_rds_performance_summary(
            self,
            region_id=None,
            list_of_rds_instance_id=None,
            drds_instance_id=None):
        api_request = APIRequest('DescribeRdsPerformanceSummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "RdsInstanceId": list_of_rds_instance_id,
            "DrdsInstanceId": drds_instance_id}
        repeat_info = {"RdsInstanceId": ('RdsInstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_drds_instance_description(self, description=None, drds_instance_id=None):
        api_request = APIRequest('ModifyDrdsInstanceDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Description": description, "DrdsInstanceId": drds_instance_id}
        return self._handle_request(api_request).result
