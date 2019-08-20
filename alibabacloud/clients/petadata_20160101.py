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


class PetaDataClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'PetaData'
        self.api_version = '2016-01-01'
        self.location_service_code = 'petadata'
        self.location_endpoint_type = 'openAPI'

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

    def revoke_account_privilege(
            self,
            resource_owner_id=None,
            account_name=None,
            db_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('RevokeAccountPrivilege', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "DBName": db_name,
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

    def grant_account_privilege(
            self,
            resource_owner_id=None,
            account_name=None,
            db_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            account_privilege=None):
        api_request = APIRequest('GrantAccountPrivilege', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "DBName": db_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "AccountPrivilege": account_privilege}
        return self._handle_request(api_request).result

    def release_instance_public_connection(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            current_connection_string=None):
        api_request = APIRequest('ReleaseInstancePublicConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "CurrentConnectionString": current_connection_string}
        return self._handle_request(api_request).result

    def restore_database(
            self,
            resource_owner_id=None,
            restore_time=None,
            src_db_name=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            backup_id=None,
            owner_id=None,
            restore_type=None,
            instance_name=None,
            security_token=None,
            src_instance_id=None):
        api_request = APIRequest('RestoreDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RestoreTime": restore_time,
            "SrcDBName": src_db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "BackupId": backup_id,
            "OwnerId": owner_id,
            "RestoreType": restore_type,
            "InstanceName": instance_name,
            "SecurityToken": security_token,
            "SrcInstanceId": src_instance_id}
        return self._handle_request(api_request).result

    def modify_backup_policy(
            self,
            preferred_backup_period=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            preferred_backup_time=None,
            backup_retention_period=None,
            enable_binlog_backup=None,
            instance_id=None,
            db_name=None,
            security_token=None):
        api_request = APIRequest('ModifyBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PreferredBackupPeriod": preferred_backup_period,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PreferredBackupTime": preferred_backup_time,
            "BackupRetentionPeriod": backup_retention_period,
            "EnableBinlogBackup": enable_binlog_backup,
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token}
        return self._handle_request(api_request).result

    def describe_database_backup(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            backup_id=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            backup_status=None,
            instance_id=None,
            db_name=None,
            security_token=None,
            page_size=None,
            backup_mode=None):
        api_request = APIRequest('DescribeDatabaseBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "BackupId": backup_id,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "BackupStatus": backup_status,
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "BackupMode": backup_mode}
        return self._handle_request(api_request).result

    def describe_backup_policy(
            self,
            resource_owner_id=None,
            instance_id=None,
            db_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_database_backup(
            self,
            resource_owner_id=None,
            instance_id=None,
            db_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CreateDatabaseBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def allocate_instance_public_connection(
            self,
            resource_owner_id=None,
            connection_string_prefix=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            port=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('AllocateInstancePublicConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ConnectionStringPrefix": connection_string_prefix,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "Port": port,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def switch_instance_net_type(
            self,
            vswitch_id=None,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            target_network_type=None,
            owner_account=None,
            vpc_id=None,
            owner_id=None):
        api_request = APIRequest('SwitchInstanceNetType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "TargetNetworkType": target_network_type,
            "OwnerAccount": owner_account,
            "VpcId": vpc_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def reset_account_password(
            self,
            resource_owner_id=None,
            instance_id=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            new_password=None):
        api_request = APIRequest('ResetAccountPassword', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NewPassword": new_password}
        return self._handle_request(api_request).result

    def modify_security_ips(
            self,
            resource_owner_id=None,
            modify_mode=None,
            resource_owner_account=None,
            owner_account=None,
            security_ip_list_attribute=None,
            owner_id=None,
            security_ip_list=None,
            instance_id=None,
            security_token=None,
            security_ip_list_name=None):
        api_request = APIRequest('ModifySecurityIPs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ModifyMode": modify_mode,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SecurityIPListAttribute": security_ip_list_attribute,
            "OwnerId": owner_id,
            "SecurityIPList": security_ip_list,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "SecurityIPListName": security_ip_list_name}
        return self._handle_request(api_request).result

    def modify_instance_name(
            self,
            resource_owner_id=None,
            instance_id=None,
            new_instance_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyInstanceName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "NewInstanceName": new_instance_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_account_password(
            self,
            resource_owner_id=None,
            instance_id=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            old_password=None,
            owner_id=None,
            new_password=None):
        api_request = APIRequest('ModifyAccountPassword', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OldPassword": old_password,
            "OwnerId": owner_id,
            "NewPassword": new_password}
        return self._handle_request(api_request).result

    def describe_user_info(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeUserInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_task_status(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            task_id=None):
        api_request = APIRequest('DescribeTaskStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def describe_tasks(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            max_records_per_page=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            instance_id=None,
            security_token=None,
            page_numbers=None,
            task_action=None,
            status=None):
        api_request = APIRequest('DescribeTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "MaxRecordsPerPage": max_records_per_page,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "PageNumbers": page_numbers,
            "TaskAction": task_action,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_security_ips(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeSecurityIPs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
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

    def describe_price(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            commodities=None,
            owner_id=None,
            order_type=None):
        api_request = APIRequest('DescribePrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Commodities": commodities,
            "OwnerId": owner_id,
            "OrderType": order_type}
        return self._handle_request(api_request).result

    def describe_monitor_items(
            self,
            item_level=None,
            monitor_version=None,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeMonitorItems', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ItemLevel": item_level,
            "MonitorVersion": monitor_version,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instance_resource_usage(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            interval=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceResourceUsage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "Interval": interval,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instance_performance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            key_list=None,
            instance_id=None,
            security_token=None,
            monitor_group=None,
            interval=None):
        api_request = APIRequest('DescribeInstancePerformance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "KeyList": key_list,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "MonitorGroup": monitor_group,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_instances(
            self,
            resource_owner_id=None,
            instance_status=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            page_number=None,
            instance_id=None,
            security_token=None,
            page_size=None,
            charge_type=None):
        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceStatus": instance_status,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "ChargeType": charge_type}
        return self._handle_request(api_request).result

    def describe_instance_info(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_databases(
            self,
            resource_owner_id=None,
            instance_id=None,
            db_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeDatabases', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_database_resource_usage(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            instance_id=None,
            db_name=None,
            security_token=None,
            interval=None):
        api_request = APIRequest('DescribeDatabaseResourceUsage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_database_performance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            key_list=None,
            instance_id=None,
            db_name=None,
            security_token=None,
            monitor_group=None,
            interval=None):
        api_request = APIRequest('DescribeDatabasePerformance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "KeyList": key_list,
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token,
            "MonitorGroup": monitor_group,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_database_partitions(
            self,
            resource_owner_id=None,
            instance_id=None,
            db_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeDatabasePartitions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_accounts(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeAccounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_database(
            self,
            resource_owner_id=None,
            instance_id=None,
            db_name=None,
            security_token=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_account(
            self,
            resource_owner_id=None,
            instance_id=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_instance(
            self,
            resource_owner_id=None,
            node_spec=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            network_type=None,
            owner_id=None,
            security_ip_list=None,
            vswitch_id=None,
            account_password=None,
            instance_name=None,
            db_name=None,
            account_name=None,
            security_token=None,
            node_number=None,
            vpc_id=None,
            zone_id=None,
            charge_type=None):
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "NodeSpec": node_spec,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "NetworkType": network_type,
            "OwnerId": owner_id,
            "SecurityIPList": security_ip_list,
            "VSwitchId": vswitch_id,
            "AccountPassword": account_password,
            "InstanceName": instance_name,
            "DBName": db_name,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "NodeNumber": node_number,
            "VpcId": vpc_id,
            "ZoneId": zone_id,
            "ChargeType": charge_type}
        return self._handle_request(api_request).result

    def create_database(
            self,
            resource_owner_id=None,
            node_spec=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            token=None,
            instance_id=None,
            db_name=None,
            security_token=None,
            node_number=None):
        api_request = APIRequest('CreateDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "NodeSpec": node_spec,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Token": token,
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token,
            "NodeNumber": node_number}
        return self._handle_request(api_request).result

    def create_account(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            account_type=None,
            owner_id=None,
            account_version=None,
            account_description=None,
            account_privilege=None,
            account_password=None,
            instance_id=None,
            account_name=None,
            db_name=None,
            security_token=None,
            db_info=None):
        api_request = APIRequest('CreateAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "AccountType": account_type,
            "OwnerId": owner_id,
            "AccountVersion": account_version,
            "AccountDescription": account_description,
            "AccountPrivilege": account_privilege,
            "AccountPassword": account_password,
            "InstanceId": instance_id,
            "AccountName": account_name,
            "DBName": db_name,
            "SecurityToken": security_token,
            "DBInfo": db_info}
        return self._handle_request(api_request).result
