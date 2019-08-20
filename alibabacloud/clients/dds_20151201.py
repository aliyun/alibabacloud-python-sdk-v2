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


class DdsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Dds'
        self.api_version = '2015-12-01'
        self.location_service_code = 'Dds'
        self.location_endpoint_type = 'openAPI'

    def release_node_private_network_address(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            network_type=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('ReleaseNodePrivateNetworkAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "NetworkType": network_type,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def describe_role_zone_info(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeRoleZoneInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def allocate_node_private_network_address(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            account_password=None,
            account_name=None,
            security_token=None,
            zone_id=None,
            db_instance_id=None,
            node_id=None):
        api_request = APIRequest('AllocateNodePrivateNetworkAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AccountPassword": account_password,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ZoneId": zone_id,
            "DBInstanceId": db_instance_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def modify_instance_vpc_auth_mode(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            vpc_auth_mode=None,
            db_instance_id=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('ModifyInstanceVpcAuthMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "VpcAuthMode": vpc_auth_mode,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def migrate_available_zone(
            self,
            vswitch=None,
            resource_owner_id=None,
            resource_owner_account=None,
            effective_time=None,
            owner_account=None,
            zone_id=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('MigrateAvailableZone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Vswitch": vswitch,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "EffectiveTime": effective_time,
            "OwnerAccount": owner_account,
            "ZoneId": zone_id,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def check_recovery_condition(
            self,
            resource_owner_id=None,
            restore_time=None,
            database_names=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            backup_id=None,
            source_db_instance=None,
            owner_id=None):
        api_request = APIRequest('CheckRecoveryCondition', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RestoreTime": restore_time,
            "DatabaseNames": database_names,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "BackupId": backup_id,
            "SourceDBInstance": source_db_instance,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_backup_dbs(
            self,
            resource_owner_id=None,
            restore_time=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            backup_id=None,
            page_size=None,
            source_db_instance=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeBackupDBs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RestoreTime": restore_time,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "BackupId": backup_id,
            "PageSize": page_size,
            "SourceDBInstance": source_db_instance,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_tag_resources(
            self,
            resource_owner_id=None,
            list_of_resource_id=None,
            resource_owner_account=None,
            region_id=None,
            next_token=None,
            owner_account=None,
            list_of_tag=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('ListTagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": list_of_resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NextToken": next_token,
            "OwnerAccount": owner_account,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def untag_resources(
            self,
            all_=None,
            resource_owner_id=None,
            list_of_resource_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            list_of_tag_key=None,
            resource_type=None):
        api_request = APIRequest('UntagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "All": all_,
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": list_of_resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TagKey": list_of_tag_key,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "TagKey": ('TagKey', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def tag_resources(
            self,
            resource_owner_id=None,
            list_of_resource_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            list_of_tag=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('TagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": list_of_resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_available_engine_version(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeAvailableEngineVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_renewal_price(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            coupon_no=None,
            db_instance_id=None,
            owner_id=None,
            business_info=None):
        api_request = APIRequest('DescribeRenewalPrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "CouponNo": coupon_no,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "BusinessInfo": business_info}
        return self._handle_request(api_request).result

    def migrate_to_other_zone(
            self,
            vswitch_id=None,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            effective_time=None,
            owner_account=None,
            zone_id=None,
            owner_id=None):
        api_request = APIRequest('MigrateToOtherZone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "EffectiveTime": effective_time,
            "OwnerAccount": owner_account,
            "ZoneId": zone_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_instance_auto_renewal_attribute(
            self,
            duration=None,
            resource_owner_id=None,
            auto_renew=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyInstanceAutoRenewalAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "ResourceOwnerId": resource_owner_id,
            "AutoRenew": auto_renew,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instance_auto_renewal_attribute(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            db_instance_id=None,
            owner_id=None,
            page_number=None,
            db_instance_type=None):
        api_request = APIRequest('DescribeInstanceAutoRenewalAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "DBInstanceType": db_instance_type}
        return self._handle_request(api_request).result

    def describe_replication_group(
            self,
            destination_instance_ids=None,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            replication_group_id=None,
            owner_account=None,
            source_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeReplicationGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DestinationInstanceIds": destination_instance_ids,
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "ReplicationGroupId": replication_group_id,
            "OwnerAccount": owner_account,
            "SourceInstanceId": source_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_active_operation_task(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            ids=None,
            switch_time=None,
            owner_id=None):
        api_request = APIRequest('ModifyActiveOperationTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Ids": ids,
            "SwitchTime": switch_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_active_operation_task_type(
            self,
            resource_owner_id=None,
            is_history=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeActiveOperationTaskType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "IsHistory": is_history,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_active_operation_task_region(
            self,
            resource_owner_id=None,
            is_history=None,
            task_type=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeActiveOperationTaskRegion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "IsHistory": is_history,
            "TaskType": task_type,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_active_operation_task_count(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeActiveOperationTaskCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_active_operation_task(
            self,
            resource_owner_id=None,
            task_type=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            page_number=None,
            is_history=None,
            security_token=None,
            page_size=None,
            region=None):
        api_request = APIRequest('DescribeActiveOperationTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TaskType": task_type,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "IsHistory": is_history,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "Region": region}
        return self._handle_request(api_request).result

    def describe_slow_log_records(
            self,
            sql_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            db_name=None,
            security_token=None,
            page_size=None,
            db_instance_id=None,
            node_id=None):
        api_request = APIRequest('DescribeSlowLogRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SQLId": sql_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "DBName": db_name,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def describe_running_log_records(
            self,
            sql_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            db_name=None,
            security_token=None,
            page_size=None,
            db_instance_id=None,
            role_type=None,
            node_id=None):
        api_request = APIRequest('DescribeRunningLogRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SQLId": sql_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "DBName": db_name,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "RoleType": role_type,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def describe_error_log_records(
            self,
            sql_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            db_name=None,
            security_token=None,
            page_size=None,
            db_instance_id=None,
            role_type=None,
            node_id=None):
        api_request = APIRequest('DescribeErrorLogRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SQLId": sql_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "DBName": db_name,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "RoleType": role_type,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def modify_db_instance_ssl(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            ssl_action=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBInstanceSSL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SSLAction": ssl_action,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_instance_ssl(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceSSL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_instance_connection_string(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            new_connection_string=None,
            owner_id=None,
            node_id=None,
            current_connection_string=None):
        api_request = APIRequest('ModifyDBInstanceConnectionString', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "NewConnectionString": new_connection_string,
            "OwnerId": owner_id,
            "NodeId": node_id,
            "CurrentConnectionString": current_connection_string}
        return self._handle_request(api_request).result

    def modify_audit_log_filter(
            self,
            filter_=None,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            role_type=None,
            owner_id=None):
        api_request = APIRequest('ModifyAuditLogFilter', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Filter": filter_,
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "RoleType": role_type,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_audit_log_filter(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            role_type=None,
            owner_id=None):
        api_request = APIRequest('DescribeAuditLogFilter', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "RoleType": role_type,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def evaluate_fail_over_switch(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('EvaluateFailOverSwitch', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def upgrade_db_instance_kernel_version(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('UpgradeDBInstanceKernelVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_kernel_release_notes(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            kernel_version=None):
        api_request = APIRequest('DescribeKernelReleaseNotes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "KernelVersion": kernel_version}
        return self._handle_request(api_request).result

    def modify_audit_policy(
            self,
            resource_owner_id=None,
            audit_status=None,
            storage_period=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyAuditPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AuditStatus": audit_status,
            "StoragePeriod": storage_period,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_audit_policy(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeAuditPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def destroy_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DestroyInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_available_time_range(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('DescribeAvailableTimeRange', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def transform_to_pre_paid(
            self,
            resource_owner_id=None,
            period=None,
            auto_pay=None,
            from_app=None,
            resource_owner_account=None,
            owner_account=None,
            coupon_no=None,
            owner_id=None,
            instance_id=None,
            auto_renew=None,
            security_token=None,
            business_info=None):
        api_request = APIRequest('TransformToPrePaid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "AutoPay": auto_pay,
            "FromApp": from_app,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "CouponNo": coupon_no,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "AutoRenew": auto_renew,
            "SecurityToken": security_token,
            "BusinessInfo": business_info}
        return self._handle_request(api_request).result

    def describe_rds_vswitchs(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            vpc_id=None,
            zone_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeRdsVSwitchs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "VpcId": vpc_id,
            "ZoneId": zone_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_rds_vpcs(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            zone_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeRdsVpcs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ZoneId": zone_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_index_recommendation(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            collection=None,
            start_time=None,
            operation_type=None,
            owner_id=None,
            page_number=None,
            database=None,
            instance_id=None,
            security_token=None,
            page_size=None,
            node_id=None,
            task_id=None):
        api_request = APIRequest('DescribeIndexRecommendation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "Collection": collection,
            "StartTime": start_time,
            "OperationType": operation_type,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "Database": database,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "NodeId": node_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def create_recommendation_task(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('CreateRecommendationTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def describe_avaliable_time_range(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('DescribeAvaliableTimeRange', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def describe_strategy(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeStrategy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_replica_conflict_info(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            security_token=None,
            replica_id=None,
            page_size=None):
        api_request = APIRequest('DescribeReplicaConflictInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "SecurityToken": security_token,
            "ReplicaId": replica_id,
            "PageSize": page_size}
        return self._handle_request(api_request).result

    def create_static_verification(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            destination_instance_id=None,
            source_instance_id=None,
            owner_id=None):
        api_request = APIRequest('CreateStaticVerification', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "DestinationInstanceId": destination_instance_id,
            "SourceInstanceId": source_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_replica_recovery_mode(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            recovery_mode=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyReplicaRecoveryMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "RecoveryMode": recovery_mode,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_static_verification_list(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            destination_instance_id=None,
            source_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeStaticVerificationList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "DestinationInstanceId": destination_instance_id,
            "SourceInstanceId": source_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_verification_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            security_token=None,
            replica_id=None,
            page_size=None):
        api_request = APIRequest('DescribeVerificationList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "SecurityToken": security_token,
            "ReplicaId": replica_id,
            "PageSize": page_size}
        return self._handle_request(api_request).result

    def modify_replica_verification_mode(
            self,
            resource_owner_id=None,
            verification_mode=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyReplicaVerificationMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "VerificationMode": verification_mode,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_instance_monitor(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            granularity=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBInstanceMonitor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "Granularity": granularity,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_instance_monitor(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceMonitor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def switch_db_instance_ha(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            target_instance_id=None,
            role_ids=None,
            security_token=None,
            switch_type=None,
            db_instance_id=None,
            source_instance_id=None,
            node_id=None):
        api_request = APIRequest('SwitchDBInstanceHA', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TargetInstanceId": target_instance_id,
            "RoleIds": role_ids,
            "SecurityToken": security_token,
            "SwitchType": switch_type,
            "DBInstanceId": db_instance_id,
            "SourceInstanceId": source_instance_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def swithc_db_instance_ha(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            target_instance_id=None,
            security_token=None,
            switch_type=None,
            db_instance_id=None,
            source_instance_id=None,
            node_id=None):
        api_request = APIRequest('SwithcDBInstanceHA', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TargetInstanceId": target_instance_id,
            "SecurityToken": security_token,
            "SwitchType": switch_type,
            "DBInstanceId": db_instance_id,
            "SourceInstanceId": source_instance_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def modify_replica_relation(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyReplicaRelation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_replica_mode(
            self,
            domain_mode=None,
            resource_owner_id=None,
            primary_instance_id=None,
            replica_mode=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyReplicaMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainMode": domain_mode,
            "ResourceOwnerId": resource_owner_id,
            "PrimaryInstanceId": primary_instance_id,
            "ReplicaMode": replica_mode,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_guard_domain_mode(
            self,
            domain_mode=None,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyGuardDomainMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainMode": domain_mode,
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_parameters(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            node_id=None,
            parameters=None):
        api_request = APIRequest('ModifyParameters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "NodeId": node_id,
            "Parameters": parameters}
        return self._handle_request(api_request).result

    def describe_parameter_templates(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            engine=None,
            owner_account=None,
            engine_version=None,
            owner_id=None):
        api_request = APIRequest('DescribeParameterTemplates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "Engine": engine,
            "OwnerAccount": owner_account,
            "EngineVersion": engine_version,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_parameters(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('DescribeParameters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def describe_parameter_modification_history(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('DescribeParameterModificationHistory',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def upgrade_db_instance_engine_version(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            engine_version=None,
            owner_id=None):
        api_request = APIRequest('UpgradeDBInstanceEngineVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "EngineVersion": engine_version,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def release_public_network_address(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('ReleasePublicNetworkAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def allocate_public_network_address(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('AllocatePublicNetworkAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def modify_db_instance_maintain_time(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            maintain_start_time=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            maintain_end_time=None):
        api_request = APIRequest('ModifyDBInstanceMaintainTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "MaintainStartTime": maintain_start_time,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "MaintainEndTime": maintain_end_time}
        return self._handle_request(api_request).result

    def describe_sharding_network_address(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('DescribeShardingNetworkAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def describe_audit_records(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            query_keywords=None,
            page_number=None,
            database=None,
            form=None,
            security_token=None,
            page_size=None,
            db_instance_id=None,
            node_id=None,
            user=None):
        api_request = APIRequest('DescribeAuditRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "QueryKeywords": query_keywords,
            "PageNumber": page_number,
            "Database": database,
            "Form": form,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "NodeId": node_id,
            "User": user}
        return self._handle_request(api_request).result

    def describe_audit_files(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            db_instance_id=None,
            owner_id=None,
            node_id=None,
            page_number=None):
        api_request = APIRequest('DescribeAuditFiles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "NodeId": node_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_db_instance_net_expire_time(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            connection_string=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            classic_expend_expired_days=None):
        api_request = APIRequest('ModifyDBInstanceNetExpireTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "ConnectionString": connection_string,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "ClassicExpendExpiredDays": classic_expend_expired_days}
        return self._handle_request(api_request).result

    def describe_replicas(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            attach_db_instance_data=None,
            owner_account=None,
            replica_id=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeReplicas', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "AttachDbInstanceData": attach_db_instance_data,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def release_replica(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('ReleaseReplica', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_replica_description(
            self,
            replica_description=None,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyReplicaDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ReplicaDescription": replica_description,
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_replica_usage(
            self,
            resource_owner_id=None,
            source_db_instance_id=None,
            destination_db_instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeReplicaUsage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceDBInstanceId": source_db_instance_id,
            "DestinationDBInstanceId": destination_db_instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_replica_performance(
            self,
            resource_owner_id=None,
            destination_db_instance_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            source_db_instance_id=None,
            security_token=None,
            replica_id=None,
            key=None):
        api_request = APIRequest('DescribeReplicaPerformance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DestinationDBInstanceId": destination_db_instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "SourceDBInstanceId": source_db_instance_id,
            "SecurityToken": security_token,
            "ReplicaId": replica_id,
            "Key": key}
        return self._handle_request(api_request).result

    def describe_replica_initialize_progress(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeReplicaInitializeProgress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_node_spec(
            self,
            resource_owner_id=None,
            auto_pay=None,
            from_app=None,
            resource_owner_account=None,
            client_token=None,
            node_storage=None,
            owner_account=None,
            owner_id=None,
            node_class=None,
            security_token=None,
            effective_time=None,
            db_instance_id=None,
            node_id=None):
        api_request = APIRequest('ModifyNodeSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "FromApp": from_app,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "NodeStorage": node_storage,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NodeClass": node_class,
            "SecurityToken": security_token,
            "EffectiveTime": effective_time,
            "DBInstanceId": db_instance_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def delete_node(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('DeleteNode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def create_sharding_db_instance(
            self,
            resource_owner_id=None,
            client_token=None,
            engine_version=None,
            network_type=None,
            list_of_replica_set=None,
            storage_engine=None,
            security_token=None,
            engine=None,
            db_instance_description=None,
            period=None,
            restore_time=None,
            resource_owner_account=None,
            src_db_instance_id=None,
            owner_account=None,
            list_of_config_server=None,
            owner_id=None,
            list_of_mongos=None,
            security_ip_list=None,
            vswitch_id=None,
            account_password=None,
            auto_renew=None,
            vpc_id=None,
            zone_id=None,
            charge_type=None):
        api_request = APIRequest('CreateShardingDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "EngineVersion": engine_version,
            "NetworkType": network_type,
            "ReplicaSet": list_of_replica_set,
            "StorageEngine": storage_engine,
            "SecurityToken": security_token,
            "Engine": engine,
            "DBInstanceDescription": db_instance_description,
            "Period": period,
            "RestoreTime": restore_time,
            "ResourceOwnerAccount": resource_owner_account,
            "SrcDBInstanceId": src_db_instance_id,
            "OwnerAccount": owner_account,
            "ConfigServer": list_of_config_server,
            "OwnerId": owner_id,
            "Mongos": list_of_mongos,
            "SecurityIPList": security_ip_list,
            "VSwitchId": vswitch_id,
            "AccountPassword": account_password,
            "AutoRenew": auto_renew,
            "VpcId": vpc_id,
            "ZoneId": zone_id,
            "ChargeType": charge_type}
        repeat_info = {
            "ReplicaSet": (
                'ReplicaSet', 'list', 'dict', [
                    ('Storage', 'str', None, None), ('Class', 'str', None, None), ]), "ConfigServer": (
                'ConfigServer', 'list', 'dict', [
                    ('Storage', 'str', None, None), ('Class', 'str', None, None), ]), "Mongos": (
                        'Mongos', 'list', 'dict', [
                            ('Class', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_node(
            self,
            resource_owner_id=None,
            node_type=None,
            auto_pay=None,
            from_app=None,
            resource_owner_account=None,
            client_token=None,
            node_storage=None,
            owner_account=None,
            owner_id=None,
            node_class=None,
            security_token=None,
            db_instance_id=None):
        api_request = APIRequest('CreateNode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "NodeType": node_type,
            "AutoPay": auto_pay,
            "FromApp": from_app,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "NodeStorage": node_storage,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NodeClass": node_class,
            "SecurityToken": security_token,
            "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def sample(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('Sample', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_instance_network_type(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            network_type=None,
            owner_id=None,
            vswitch_id=None,
            security_token=None,
            retain_classic=None,
            classic_expired_days=None,
            vpc_id=None,
            db_instance_id=None):
        api_request = APIRequest('ModifyDBInstanceNetworkType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "NetworkType": network_type,
            "OwnerId": owner_id,
            "VSwitchId": vswitch_id,
            "SecurityToken": security_token,
            "RetainClassic": retain_classic,
            "ClassicExpiredDays": classic_expired_days,
            "VpcId": vpc_id,
            "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def renew_db_instance(
            self,
            resource_owner_id=None,
            period=None,
            auto_pay=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            coupon_no=None,
            owner_id=None,
            security_token=None,
            db_instance_id=None,
            business_info=None):
        api_request = APIRequest('RenewDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "CouponNo": coupon_no,
            "OwnerId": owner_id,
            "SecurityToken": security_token,
            "DBInstanceId": db_instance_id,
            "BusinessInfo": business_info}
        return self._handle_request(api_request).result

    def create_backup(
            self,
            backup_method=None,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('CreateBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BackupMethod": backup_method,
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_account(
            self,
            resource_owner_id=None,
            account_password=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            account_description=None):
        api_request = APIRequest('CreateAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountPassword": account_password,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "AccountDescription": account_description}
        return self._handle_request(api_request).result

    def describe_db_instance_performance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            role_id=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            replica_set_role=None,
            security_token=None,
            db_instance_id=None,
            node_id=None,
            key=None):
        api_request = APIRequest('DescribeDBInstancePerformance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RoleId": role_id,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "ReplicaSetRole": replica_set_role,
            "SecurityToken": security_token,
            "DBInstanceId": db_instance_id,
            "NodeId": node_id,
            "Key": key}
        return self._handle_request(api_request).result

    def describe_db_instance_attribute(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            engine=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "Engine": engine,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_backups(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            backup_id=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            security_token=None,
            page_size=None,
            db_instance_id=None,
            node_id=None):
        api_request = APIRequest('DescribeBackups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "BackupId": backup_id,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def describe_backup_policy(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_accounts(
            self,
            resource_owner_id=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeAccounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_db_instance(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_db_instance(
            self,
            resource_owner_id=None,
            db_instance_storage=None,
            client_token=None,
            readonly_replicas=None,
            coupon_no=None,
            engine_version=None,
            network_type=None,
            replication_factor=None,
            storage_engine=None,
            resource_group_id=None,
            database_names=None,
            security_token=None,
            engine=None,
            db_instance_description=None,
            business_info=None,
            period=None,
            restore_time=None,
            resource_owner_account=None,
            src_db_instance_id=None,
            owner_account=None,
            backup_id=None,
            owner_id=None,
            db_instance_class=None,
            security_ip_list=None,
            vswitch_id=None,
            account_password=None,
            auto_renew=None,
            vpc_id=None,
            zone_id=None,
            charge_type=None):
        api_request = APIRequest('CreateDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "ClientToken": client_token,
            "ReadonlyReplicas": readonly_replicas,
            "CouponNo": coupon_no,
            "EngineVersion": engine_version,
            "NetworkType": network_type,
            "ReplicationFactor": replication_factor,
            "StorageEngine": storage_engine,
            "ResourceGroupId": resource_group_id,
            "DatabaseNames": database_names,
            "SecurityToken": security_token,
            "Engine": engine,
            "DBInstanceDescription": db_instance_description,
            "BusinessInfo": business_info,
            "Period": period,
            "RestoreTime": restore_time,
            "ResourceOwnerAccount": resource_owner_account,
            "SrcDBInstanceId": src_db_instance_id,
            "OwnerAccount": owner_account,
            "BackupId": backup_id,
            "OwnerId": owner_id,
            "DBInstanceClass": db_instance_class,
            "SecurityIPList": security_ip_list,
            "VSwitchId": vswitch_id,
            "AccountPassword": account_password,
            "AutoRenew": auto_renew,
            "VpcId": vpc_id,
            "ZoneId": zone_id,
            "ChargeType": charge_type}
        return self._handle_request(api_request).result

    def describe_security_ips(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeSecurityIps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_replica_set_role(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeReplicaSetRole', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_regions(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_instances(
            self,
            resource_owner_id=None,
            engine_version=None,
            network_type=None,
            page_number=None,
            replication_factor=None,
            expired=None,
            security_token=None,
            engine=None,
            page_size=None,
            db_instance_id=None,
            db_instance_description=None,
            db_instance_status=None,
            list_of_tag=None,
            expire_time=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            db_instance_type=None,
            db_instance_class=None,
            vswitch_id=None,
            vpc_id=None,
            zone_id=None,
            charge_type=None):
        api_request = APIRequest('DescribeDBInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "EngineVersion": engine_version,
            "NetworkType": network_type,
            "PageNumber": page_number,
            "ReplicationFactor": replication_factor,
            "Expired": expired,
            "SecurityToken": security_token,
            "Engine": engine,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "DBInstanceDescription": db_instance_description,
            "DBInstanceStatus": db_instance_status,
            "Tag": list_of_tag,
            "ExpireTime": expire_time,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "DBInstanceType": db_instance_type,
            "DBInstanceClass": db_instance_class,
            "VSwitchId": vswitch_id,
            "VpcId": vpc_id,
            "ZoneId": zone_id,
            "ChargeType": charge_type}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def restore_db_instance(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            backup_id=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('RestoreDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "BackupId": backup_id,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def restart_db_instance(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('RestartDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def reset_account_password(
            self,
            resource_owner_id=None,
            account_password=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ResetAccountPassword', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountPassword": account_password,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_security_ips(
            self,
            resource_owner_id=None,
            modify_mode=None,
            resource_owner_account=None,
            owner_account=None,
            security_ips=None,
            owner_id=None,
            security_ip_group_name=None,
            security_token=None,
            db_instance_id=None,
            security_ip_group_attribute=None):
        api_request = APIRequest('ModifySecurityIps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ModifyMode": modify_mode,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SecurityIps": security_ips,
            "OwnerId": owner_id,
            "SecurityIpGroupName": security_ip_group_name,
            "SecurityToken": security_token,
            "DBInstanceId": db_instance_id,
            "SecurityIpGroupAttribute": security_ip_group_attribute}
        return self._handle_request(api_request).result

    def modify_db_instance_spec(
            self,
            resource_owner_id=None,
            db_instance_storage=None,
            auto_pay=None,
            from_app=None,
            resource_owner_account=None,
            owner_account=None,
            readonly_replicas=None,
            coupon_no=None,
            owner_id=None,
            replication_factor=None,
            db_instance_class=None,
            security_token=None,
            effective_time=None,
            db_instance_id=None,
            business_info=None,
            order_type=None):
        api_request = APIRequest('ModifyDBInstanceSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "AutoPay": auto_pay,
            "FromApp": from_app,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReadonlyReplicas": readonly_replicas,
            "CouponNo": coupon_no,
            "OwnerId": owner_id,
            "ReplicationFactor": replication_factor,
            "DBInstanceClass": db_instance_class,
            "SecurityToken": security_token,
            "EffectiveTime": effective_time,
            "DBInstanceId": db_instance_id,
            "BusinessInfo": business_info,
            "OrderType": order_type}
        return self._handle_request(api_request).result

    def modify_db_instance_description(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            db_instance_description=None,
            owner_id=None,
            node_id=None):
        api_request = APIRequest('ModifyDBInstanceDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "DBInstanceDescription": db_instance_description,
            "OwnerId": owner_id,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def modify_backup_policy(
            self,
            preferred_backup_time=None,
            preferred_backup_period=None,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PreferredBackupTime": preferred_backup_time,
            "PreferredBackupPeriod": preferred_backup_period,
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_account_description(
            self,
            resource_owner_id=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            account_description=None):
        api_request = APIRequest('ModifyAccountDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "AccountDescription": account_description}
        return self._handle_request(api_request).result
