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


class HbrClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'hbr'
        self.api_version = '2017-09-08'
        self.location_service_code = 'hbr'
        self.location_endpoint_type = 'openAPI'

    def delete_sql_server_instance(self, vault_id=None, cluster_id=None):
        api_request = APIRequest('DeleteSqlServerInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"VaultId": vault_id, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_nas_file_systems(self,):
        api_request = APIRequest('DescribeNasFileSystems', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def create_nas_instance(
            self,
            create_time=None,
            vault_id=None,
            description=None,
            file_system_id=None):
        api_request = APIRequest('CreateNasInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CreateTime": create_time,
            "VaultId": vault_id,
            "Description": description,
            "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def delete_nas_instance(self, create_time=None, file_system_id=None):
        api_request = APIRequest('DeleteNasInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CreateTime": create_time, "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def attach_nas_file_system(self, create_time=None, file_system_id=None):
        api_request = APIRequest('AttachNasFileSystem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CreateTime": create_time, "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def detach_nas_file_system(self, create_time=None, file_system_id=None):
        api_request = APIRequest('DetachNasFileSystem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CreateTime": create_time, "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def describe_nas_instances(self, vault_id=None, page_size=None, page_number=None):
        api_request = APIRequest('DescribeNasInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_recent_snapshots(
            self,
            page_size=None,
            source_type=None,
            list_of_filters=None,
            page_number=None):
        api_request = APIRequest('DescribeRecentSnapshots', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "SourceType": source_type,
            "Filters": list_of_filters,
            "PageNumber": page_number}
        repeat_info = {"Filters": ('Filters', 'list', 'dict', [('Values', 'list', 'str', None),
                                                               ('Key', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def search_historical_snapshots(
            self,
            next_token=None,
            query=None,
            limit=None,
            source_type=None):
        api_request = APIRequest('SearchHistoricalSnapshots', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NextToken": next_token,
            "Query": query,
            "Limit": limit,
            "SourceType": source_type}
        return self._handle_request(api_request).result

    def create_restore_job(
            self,
            restore_type=None,
            snapshot_hash=None,
            target_prefix=None,
            snapshot_id=None,
            target_create_time=None,
            vault_id=None,
            options=None,
            source_type=None,
            target_file_system_id=None,
            target_path=None,
            target_bucket=None):
        api_request = APIRequest('CreateRestoreJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RestoreType": restore_type,
            "SnapshotHash": snapshot_hash,
            "TargetPrefix": target_prefix,
            "SnapshotId": snapshot_id,
            "TargetCreateTime": target_create_time,
            "VaultId": vault_id,
            "Options": options,
            "SourceType": source_type,
            "TargetFileSystemId": target_file_system_id,
            "TargetPath": target_path,
            "TargetBucket": target_bucket}
        return self._handle_request(api_request).result

    def cancel_restore_job(self, restore_id=None):
        api_request = APIRequest('CancelRestoreJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RestoreId": restore_id}
        return self._handle_request(api_request).result

    def describe_restore_jobs2(
            self,
            restore_type=None,
            page_size=None,
            list_of_filters=None,
            page_number=None):
        api_request = APIRequest('DescribeRestoreJobs2', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RestoreType": restore_type,
            "PageSize": page_size,
            "Filters": list_of_filters,
            "PageNumber": page_number}
        repeat_info = {"Filters": ('Filters', 'list', 'dict', [('Values', 'list', 'str', None),
                                                               ('Key', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_nas_to_restore(self, vault_id=None, page_size=None, page_number=None):
        api_request = APIRequest('GetNasToRestore', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_oss_buckets_to_restore(self, vault_id=None, page_size=None, page_number=None):
        api_request = APIRequest('GetOssBucketsToRestore', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_hana_instance(self, vault_id=None, cluster_id=None, sid=None):
        api_request = APIRequest('DeleteHanaInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"VaultId": vault_id, "ClusterId": cluster_id, "Sid": sid}
        return self._handle_request(api_request).result

    def get_sql_servers_to_restore(self, vault_id=None, page_size=None, page_number=None):
        api_request = APIRequest('GetSqlServersToRestore', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_hana_backups_async(
            self,
            recovery_point_in_time=None,
            log_position=None,
            vault_id=None,
            include_log=None,
            cluster_id=None,
            source=None,
            page_number=None,
            mode=None,
            include_incremental=None,
            use_backint=None,
            database_name=None,
            page_size=None,
            volume_id=None,
            source_cluster_id=None,
            include_differential=None,
            system_copy=None):
        api_request = APIRequest('DescribeHanaBackupsAsync', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RecoveryPointInTime": recovery_point_in_time,
            "LogPosition": log_position,
            "VaultId": vault_id,
            "IncludeLog": include_log,
            "ClusterId": cluster_id,
            "Source": source,
            "PageNumber": page_number,
            "Mode": mode,
            "IncludeIncremental": include_incremental,
            "UseBackint": use_backint,
            "DatabaseName": database_name,
            "PageSize": page_size,
            "VolumeId": volume_id,
            "SourceClusterId": source_cluster_id,
            "IncludeDifferential": include_differential,
            "SystemCopy": system_copy}
        return self._handle_request(api_request).result

    def start_hana_database_async(self, vault_id=None, database_name=None, cluster_id=None):
        api_request = APIRequest('StartHanaDatabaseAsync', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "DatabaseName": database_name,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def stop_hana_database_async(self, vault_id=None, database_name=None, cluster_id=None):
        api_request = APIRequest('StopHanaDatabaseAsync', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "DatabaseName": database_name,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_backup_sources(
            self,
            page_size=None,
            source_type=None,
            list_of_filters=None,
            page_number=None):
        api_request = APIRequest('DescribeBackupSources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "SourceType": source_type,
            "Filters": list_of_filters,
            "PageNumber": page_number}
        repeat_info = {"Filters": ('Filters', 'list', 'dict', [('Values', 'list', 'str', None),
                                                               ('Key', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_sql_server_databases(
            self,
            vault_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('DescribeSqlServerDatabases', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_backup_source_groups(
            self,
            page_size=None,
            source_type=None,
            list_of_filters=None,
            page_number=None):
        api_request = APIRequest('DescribeBackupSourceGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "SourceType": source_type,
            "Filters": list_of_filters,
            "PageNumber": page_number}
        repeat_info = {"Filters": ('Filters', 'list', 'dict', [('Values', 'list', 'str', None),
                                                               ('Key', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_sql_server_instance(
            self,
            windows_login=None,
            sql_server_type=None,
            windows_password=None,
            sql_login=None,
            vault_id=None,
            use_windows_auth=None,
            sql_password=None,
            server_name=None,
            token=None):
        api_request = APIRequest('CreateSqlServerInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WindowsLogin": windows_login,
            "SqlServerType": sql_server_type,
            "WindowsPassword": windows_password,
            "SqlLogin": sql_login,
            "VaultId": vault_id,
            "UseWindowsAuth": use_windows_auth,
            "SqlPassword": sql_password,
            "ServerName": server_name,
            "Token": token}
        return self._handle_request(api_request).result

    def create_backup_source_group(
            self,
            list_of_backup_source=None,
            implicitly_create_backup_sources=None,
            list_of_backup_source_id=None,
            description=None,
            source_type=None,
            cluster_id=None,
            backup_source_group_id=None):
        api_request = APIRequest('CreateBackupSourceGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BackupSource": list_of_backup_source,
            "ImplicitlyCreateBackupSources": implicitly_create_backup_sources,
            "BackupSourceId": list_of_backup_source_id,
            "Description": description,
            "SourceType": source_type,
            "ClusterId": cluster_id,
            "BackupSourceGroupId": backup_source_group_id}
        repeat_info = {"BackupSource": ('BackupSource',
                                        'list',
                                        'dict',
                                        [('BackupSourceId',
                                          'str',
                                          None,
                                          None),
                                         ('DatabaseName',
                                          'str',
                                          None,
                                          None),
                                            ('Description',
                                             'str',
                                             None,
                                             None),
                                            ('ClusterId',
                                             'str',
                                             None,
                                             None),
                                         ]),
                       "BackupSourceId": ('BackupSourceId',
                                          'list',
                                          'str',
                                          None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_sql_server_instances(
            self,
            sql_server_type=None,
            vault_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeSqlServerInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SqlServerType": sql_server_type,
            "VaultId": vault_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def update_sql_server_snapshot(
            self,
            error_message=None,
            snapshot_hash=None,
            expire_time=None,
            snapshot_id=None,
            vault_id=None,
            percentage=None,
            cluster_id=None,
            database_id=None,
            bytes_total=None,
            token=None,
            status=None):
        api_request = APIRequest('UpdateSqlServerSnapshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ErrorMessage": error_message,
            "SnapshotHash": snapshot_hash,
            "ExpireTime": expire_time,
            "SnapshotId": snapshot_id,
            "VaultId": vault_id,
            "Percentage": percentage,
            "ClusterId": cluster_id,
            "DatabaseId": database_id,
            "BytesTotal": bytes_total,
            "Token": token,
            "Status": status}
        return self._handle_request(api_request).result

    def update_backup_source_group(
            self,
            list_of_backup_source=None,
            implicitly_create_backup_sources=None,
            list_of_backup_source_id=None,
            description=None,
            backup_source_group_id=None):
        api_request = APIRequest('UpdateBackupSourceGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BackupSource": list_of_backup_source,
            "ImplicitlyCreateBackupSources": implicitly_create_backup_sources,
            "BackupSourceId": list_of_backup_source_id,
            "Description": description,
            "BackupSourceGroupId": backup_source_group_id}
        repeat_info = {"BackupSource": ('BackupSource',
                                        'list',
                                        'dict',
                                        [('BackupSourceId',
                                          'str',
                                          None,
                                          None),
                                         ('DatabaseName',
                                          'str',
                                          None,
                                          None),
                                            ('Description',
                                             'str',
                                             None,
                                             None),
                                            ('ClusterId',
                                             'str',
                                             None,
                                             None),
                                         ]),
                       "BackupSourceId": ('BackupSourceId',
                                          'list',
                                          'str',
                                          None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_sql_server_restore(
            self,
            target_database_name=None,
            snapshot_id=None,
            vault_id=None,
            file_destination=None,
            source_database_name=None,
            source_cluster_id=None,
            cluster_id=None,
            replace_database=None,
            token=None,
            point_in_time=None):
        api_request = APIRequest('CreateSqlServerRestore', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TargetDatabaseName": target_database_name,
            "SnapshotId": snapshot_id,
            "VaultId": vault_id,
            "FileDestination": file_destination,
            "SourceDatabaseName": source_database_name,
            "SourceClusterId": source_cluster_id,
            "ClusterId": cluster_id,
            "ReplaceDatabase": replace_database,
            "Token": token,
            "PointInTime": point_in_time}
        return self._handle_request(api_request).result

    def describe_sql_server_restores(
            self,
            vault_id=None,
            page_size=None,
            restore_id=None,
            cluster_id=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeSqlServerRestores', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PageSize": page_size,
            "RestoreId": restore_id,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def delete_backup_source_group(self, backup_source_group_id=None):
        api_request = APIRequest('DeleteBackupSourceGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BackupSourceGroupId": backup_source_group_id}
        return self._handle_request(api_request).result

    def update_sql_server_restore(
            self,
            error_message=None,
            vault_id=None,
            percentage=None,
            restore_id=None,
            cluster_id=None,
            bytes_total=None,
            token=None,
            status=None):
        api_request = APIRequest('UpdateSqlServerRestore', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ErrorMessage": error_message,
            "VaultId": vault_id,
            "Percentage": percentage,
            "RestoreId": restore_id,
            "ClusterId": cluster_id,
            "BytesTotal": bytes_total,
            "Token": token,
            "Status": status}
        return self._handle_request(api_request).result

    def create_backup_plan(
            self,
            create_time=None,
            vault_id=None,
            prefix=None,
            cluster_id=None,
            bucket=None,
            schedule=None,
            list_of_path=None,
            plan_name=None,
            source_type=None,
            backup_source_group_id=None,
            backup_type=None,
            retention=None,
            file_system_id=None):
        api_request = APIRequest('CreateBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CreateTime": create_time,
            "VaultId": vault_id,
            "Prefix": prefix,
            "ClusterId": cluster_id,
            "Bucket": bucket,
            "Schedule": schedule,
            "Path": list_of_path,
            "PlanName": plan_name,
            "SourceType": source_type,
            "BackupSourceGroupId": backup_source_group_id,
            "BackupType": backup_type,
            "Retention": retention,
            "FileSystemId": file_system_id}
        repeat_info = {"Path": ('Path', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def update_sql_server_instance(
            self,
            windows_login=None,
            windows_password=None,
            sql_login=None,
            vault_id=None,
            use_windows_auth=None,
            sql_password=None,
            server_name=None,
            cluster_id=None,
            token=None):
        api_request = APIRequest('UpdateSqlServerInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WindowsLogin": windows_login,
            "WindowsPassword": windows_password,
            "SqlLogin": sql_login,
            "VaultId": vault_id,
            "UseWindowsAuth": use_windows_auth,
            "SqlPassword": sql_password,
            "ServerName": server_name,
            "ClusterId": cluster_id,
            "Token": token}
        return self._handle_request(api_request).result

    def update_backup_plan(
            self,
            schedule=None,
            list_of_path=None,
            prefix=None,
            plan_name=None,
            plan_id=None,
            retention=None):
        api_request = APIRequest('UpdateBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Schedule": schedule,
            "Path": list_of_path,
            "Prefix": prefix,
            "PlanName": plan_name,
            "PlanId": plan_id,
            "Retention": retention}
        repeat_info = {"Path": ('Path', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_sql_server_snapshot(
            self,
            expire_time=None,
            vault_id=None,
            snapshot_name=None,
            cluster_id=None,
            start_time=None,
            token=None,
            snapshot_hash=None,
            database_name=None,
            complete_time=None,
            parent_snapshot_hash=None,
            plan_id=None,
            database_id=None,
            backup_type=None,
            bytes_total=None,
            status=None):
        api_request = APIRequest('CreateSqlServerSnapshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ExpireTime": expire_time,
            "VaultId": vault_id,
            "SnapshotName": snapshot_name,
            "ClusterId": cluster_id,
            "StartTime": start_time,
            "Token": token,
            "SnapshotHash": snapshot_hash,
            "DatabaseName": database_name,
            "CompleteTime": complete_time,
            "ParentSnapshotHash": parent_snapshot_hash,
            "PlanId": plan_id,
            "DatabaseId": database_id,
            "BackupType": backup_type,
            "BytesTotal": bytes_total,
            "Status": status}
        return self._handle_request(api_request).result

    def add_sql_server_log(
            self,
            snapshot_hash=None,
            expire_time=None,
            vault_id=None,
            database_name=None,
            complete_time=None,
            snapshot_name=None,
            cluster_id=None,
            start_time=None,
            database_id=None,
            bytes_total=None,
            token=None,
            status=None):
        api_request = APIRequest('AddSqlServerLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SnapshotHash": snapshot_hash,
            "ExpireTime": expire_time,
            "VaultId": vault_id,
            "DatabaseName": database_name,
            "CompleteTime": complete_time,
            "SnapshotName": snapshot_name,
            "ClusterId": cluster_id,
            "StartTime": start_time,
            "DatabaseId": database_id,
            "BytesTotal": bytes_total,
            "Token": token,
            "Status": status}
        return self._handle_request(api_request).result

    def delete_backup_plan(self, plan_id=None):
        api_request = APIRequest('DeleteBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PlanId": plan_id}
        return self._handle_request(api_request).result

    def describe_sql_server_snapshots(
            self,
            snapshot_hash=None,
            vault_id=None,
            database_name=None,
            page_size=None,
            end_time=None,
            plan_id=None,
            cluster_id=None,
            start_time=None,
            database_id=None,
            page_number=None,
            backup_type=None,
            token=None):
        api_request = APIRequest('DescribeSqlServerSnapshots', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SnapshotHash": snapshot_hash,
            "VaultId": vault_id,
            "DatabaseName": database_name,
            "PageSize": page_size,
            "EndTime": end_time,
            "PlanId": plan_id,
            "ClusterId": cluster_id,
            "StartTime": start_time,
            "DatabaseId": database_id,
            "PageNumber": page_number,
            "BackupType": backup_type,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_backup_plans(
            self,
            page_size=None,
            source_type=None,
            list_of_filters=None,
            page_number=None):
        api_request = APIRequest('DescribeBackupPlans', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "SourceType": source_type,
            "Filters": list_of_filters,
            "PageNumber": page_number}
        repeat_info = {"Filters": ('Filters', 'list', 'dict', [('Values', 'list', 'str', None),
                                                               ('Key', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_sql_server_logs(
            self,
            start_database_id=None,
            vault_id=None,
            end_database_id=None,
            limit=None,
            end_time=None,
            cluster_id=None,
            start_time=None,
            token=None,
            direction=None):
        api_request = APIRequest('DescribeSqlServerLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartDatabaseId": start_database_id,
            "VaultId": vault_id,
            "EndDatabaseId": end_database_id,
            "Limit": limit,
            "EndTime": end_time,
            "ClusterId": cluster_id,
            "StartTime": start_time,
            "Token": token,
            "Direction": direction}
        return self._handle_request(api_request).result

    def execute_backup_plan(self, plan_id=None):
        api_request = APIRequest('ExecuteBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PlanId": plan_id}
        return self._handle_request(api_request).result

    def cancel_sql_server_restore(
            self,
            vault_id=None,
            source_database_id=None,
            restore_id=None,
            cluster_id=None,
            token=None):
        api_request = APIRequest('CancelSqlServerRestore', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "SourceDatabaseId": source_database_id,
            "RestoreId": restore_id,
            "ClusterId": cluster_id,
            "Token": token}
        return self._handle_request(api_request).result

    def get_sql_server_databases_to_restore(
            self,
            vault_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('GetSqlServerDatabasesToRestore', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def disable_backup_plan(self, plan_id=None):
        api_request = APIRequest('DisableBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PlanId": plan_id}
        return self._handle_request(api_request).result

    def cancel_backup_job(self, job_id=None):
        api_request = APIRequest('CancelBackupJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JobId": job_id}
        return self._handle_request(api_request).result

    def enable_backup_plan(self, plan_id=None):
        api_request = APIRequest('EnableBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PlanId": plan_id}
        return self._handle_request(api_request).result

    def describe_backup_jobs2(
            self,
            page_size=None,
            source_type=None,
            list_of_filters=None,
            page_number=None):
        api_request = APIRequest('DescribeBackupJobs2', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "SourceType": source_type,
            "Filters": list_of_filters,
            "PageNumber": page_number}
        repeat_info = {"Filters": ('Filters', 'list', 'dict', [('Values', 'list', 'str', None),
                                                               ('Key', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def update_backup_job(
            self,
            error_message=None,
            job_id=None,
            expire_time=None,
            progress=None,
            user_account_id=None,
            bytes_done=None,
            bytes_total=None,
            status=None,
            token=None):
        api_request = APIRequest('UpdateBackupJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ErrorMessage": error_message,
            "JobId": job_id,
            "ExpireTime": expire_time,
            "Progress": progress,
            "UserAccountId": user_account_id,
            "BytesDone": bytes_done,
            "BytesTotal": bytes_total,
            "Status": status,
            "Token": token}
        return self._handle_request(api_request).result

    def update_alert_config(
            self,
            alert_setting=None,
            contact_group_ids=None,
            id_=None,
            type_=None,
            contact_ids=None):
        api_request = APIRequest('UpdateAlertConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AlertSetting": alert_setting,
            "ContactGroupIds": contact_group_ids,
            "Id": id_,
            "Type": type_,
            "ContactIds": contact_ids}
        return self._handle_request(api_request).result

    def describe_alert_config(self, id_=None, type_=None):
        api_request = APIRequest('DescribeAlertConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "Type": type_}
        return self._handle_request(api_request).result

    def describe_vault_replication_regions(self, vault_id=None, token=None):
        api_request = APIRequest('DescribeVaultReplicationRegions', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"VaultId": vault_id, "Token": token}
        return self._handle_request(api_request).result

    def get_clients_to_restore(
            self,
            client_type=None,
            inner_ip_addresses=None,
            private_ip_addresses=None,
            vault_id=None,
            instance_ids=None,
            page_size=None,
            source_type=None,
            page_number=None,
            token=None):
        api_request = APIRequest('GetClientsToRestore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientType": client_type,
            "InnerIpAddresses": inner_ip_addresses,
            "PrivateIpAddresses": private_ip_addresses,
            "VaultId": vault_id,
            "InstanceIds": instance_ids,
            "PageSize": page_size,
            "SourceType": source_type,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def get_hana_instances_to_restore(self, vault_id=None, page_size=None, page_number=None):
        api_request = APIRequest('GetHanaInstancesToRestore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_hana_retention_setting(self, vault_id=None, database_name=None, cluster_id=None):
        api_request = APIRequest('DescribeHanaRetentionSetting', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "DatabaseName": database_name,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def update_hana_retention_setting(
            self,
            schedule=None,
            vault_id=None,
            database_name=None,
            retention_days=None,
            disabled=None,
            cluster_id=None):
        api_request = APIRequest('UpdateHanaRetentionSetting', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Schedule": schedule,
            "VaultId": vault_id,
            "DatabaseName": database_name,
            "RetentionDays": retention_days,
            "Disabled": disabled,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_hana_alert_config(self, vault_id=None, cluster_id=None, token=None):
        api_request = APIRequest('DescribeHanaAlertConfig', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"VaultId": vault_id, "ClusterId": cluster_id, "Token": token}
        return self._handle_request(api_request).result

    def update_client_alert_config(
            self,
            alert_setting=None,
            client_id=None,
            vault_id=None,
            contact_group_ids=None,
            contact_ids=None,
            token=None):
        api_request = APIRequest('UpdateClientAlertConfig', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "AlertSetting": alert_setting,
            "ClientId": client_id,
            "VaultId": vault_id,
            "ContactGroupIds": contact_group_ids,
            "ContactIds": contact_ids,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_client_alert_config(self, client_id=None, vault_id=None, token=None):
        api_request = APIRequest('DescribeClientAlertConfig', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"ClientId": client_id, "VaultId": vault_id, "Token": token}
        return self._handle_request(api_request).result

    def update_hana_alert_config(
            self,
            alert_setting=None,
            vault_id=None,
            contact_group_ids=None,
            cluster_id=None,
            contact_ids=None,
            token=None):
        api_request = APIRequest('UpdateHanaAlertConfig', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "AlertSetting": alert_setting,
            "VaultId": vault_id,
            "ContactGroupIds": contact_group_ids,
            "ClusterId": cluster_id,
            "ContactIds": contact_ids,
            "Token": token}
        return self._handle_request(api_request).result

    def create_contact_group(
            self,
            contact_group_id=None,
            display_name=None,
            contact_ids=None,
            token=None):
        api_request = APIRequest('CreateContactGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ContactGroupId": contact_group_id,
            "DisplayName": display_name,
            "ContactIds": contact_ids,
            "Token": token}
        return self._handle_request(api_request).result

    def delete_contact_group(self, contact_group_id=None, token=None):
        api_request = APIRequest('DeleteContactGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"ContactGroupId": contact_group_id, "Token": token}
        return self._handle_request(api_request).result

    def describe_contact_groups(self, page_size=None, page_number=None, token=None):
        api_request = APIRequest('DescribeContactGroups', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "PageNumber": page_number, "Token": token}
        return self._handle_request(api_request).result

    def update_contact_group(
            self,
            contact_group_id=None,
            display_name=None,
            contact_ids=None,
            token=None):
        api_request = APIRequest('UpdateContactGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ContactGroupId": contact_group_id,
            "DisplayName": display_name,
            "ContactIds": contact_ids,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_vault_alert_config(self, vault_id=None):
        api_request = APIRequest('DescribeVaultAlertConfig', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"VaultId": vault_id}
        return self._handle_request(api_request).result

    def update_vault_alert_config(
            self,
            alert_setting=None,
            vault_id=None,
            contact_group_ids=None,
            contact_ids=None):
        api_request = APIRequest('UpdateVaultAlertConfig', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "AlertSetting": alert_setting,
            "VaultId": vault_id,
            "ContactGroupIds": contact_group_ids,
            "ContactIds": contact_ids}
        return self._handle_request(api_request).result

    def execute_hana_backup(
            self,
            vault_id=None,
            backup_prefix=None,
            database_name=None,
            cluster_id=None,
            backup_type=None,
            token=None):
        api_request = APIRequest('ExecuteHanaBackup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "BackupPrefix": backup_prefix,
            "DatabaseName": database_name,
            "ClusterId": cluster_id,
            "BackupType": backup_type,
            "Token": token}
        return self._handle_request(api_request).result

    def update_hana_restore(
            self,
            phase=None,
            utc_reached_time=None,
            sys_end_time=None,
            vault_id=None,
            sys_start_time=None,
            restore_id=None,
            max_phase=None,
            cluster_id=None,
            message=None,
            database_restore_id=None,
            max_progress=None,
            current_progress=None,
            utc_end_time=None,
            token=None,
            current_phase=None,
            utc_start_time=None,
            service_name=None,
            state=None,
            sys_reached_time=None,
            status=None):
        api_request = APIRequest('UpdateHanaRestore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Phase": phase,
            "UtcReachedTime": utc_reached_time,
            "SysEndTime": sys_end_time,
            "VaultId": vault_id,
            "SysStartTime": sys_start_time,
            "RestoreId": restore_id,
            "MaxPhase": max_phase,
            "ClusterId": cluster_id,
            "Message": message,
            "DatabaseRestoreId": database_restore_id,
            "MaxProgress": max_progress,
            "CurrentProgress": current_progress,
            "UtcEndTime": utc_end_time,
            "Token": token,
            "CurrentPhase": current_phase,
            "UtcStartTime": utc_start_time,
            "ServiceName": service_name,
            "State": state,
            "SysReachedTime": sys_reached_time,
            "Status": status}
        return self._handle_request(api_request).result

    def create_hana_restore(
            self,
            sid_admin=None,
            recovery_point_in_time=None,
            log_position=None,
            vault_id=None,
            backup_id=None,
            log_paths=None,
            cluster_id=None,
            source=None,
            clear_log=None,
            extra_options=None,
            token=None,
            mode=None,
            check_access=None,
            use_delta=None,
            master_client_id=None,
            use_catalog=None,
            backup_prefix=None,
            database_name=None,
            volume_id=None,
            source_cluster_id=None,
            system_copy=None):
        api_request = APIRequest('CreateHanaRestore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "SidAdmin": sid_admin,
            "RecoveryPointInTime": recovery_point_in_time,
            "LogPosition": log_position,
            "VaultId": vault_id,
            "BackupId": backup_id,
            "LogPaths": log_paths,
            "ClusterId": cluster_id,
            "Source": source,
            "ClearLog": clear_log,
            "ExtraOptions": extra_options,
            "Token": token,
            "Mode": mode,
            "CheckAccess": check_access,
            "UseDelta": use_delta,
            "MasterClientId": master_client_id,
            "UseCatalog": use_catalog,
            "BackupPrefix": backup_prefix,
            "DatabaseName": database_name,
            "VolumeId": volume_id,
            "SourceClusterId": source_cluster_id,
            "SystemCopy": system_copy}
        return self._handle_request(api_request).result

    def describe_hana_restores(
            self,
            vault_id=None,
            database_name=None,
            backup_id=None,
            page_size=None,
            restore_status=None,
            restore_id=None,
            cluster_id=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeHanaRestores', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "DatabaseName": database_name,
            "BackupId": backup_id,
            "PageSize": page_size,
            "RestoreStatus": restore_status,
            "RestoreId": restore_id,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_hana_backups(
            self,
            recovery_point_in_time=None,
            log_position=None,
            vault_id=None,
            include_log=None,
            cluster_id=None,
            source=None,
            page_number=None,
            token=None,
            mode=None,
            include_incremental=None,
            use_backint=None,
            database_name=None,
            page_size=None,
            volume_id=None,
            source_cluster_id=None,
            include_differential=None,
            system_copy=None):
        api_request = APIRequest('DescribeHanaBackups', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "RecoveryPointInTime": recovery_point_in_time,
            "LogPosition": log_position,
            "VaultId": vault_id,
            "IncludeLog": include_log,
            "ClusterId": cluster_id,
            "Source": source,
            "PageNumber": page_number,
            "Token": token,
            "Mode": mode,
            "IncludeIncremental": include_incremental,
            "UseBackint": use_backint,
            "DatabaseName": database_name,
            "PageSize": page_size,
            "VolumeId": volume_id,
            "SourceClusterId": source_cluster_id,
            "IncludeDifferential": include_differential,
            "SystemCopy": system_copy}
        return self._handle_request(api_request).result

    def describe_hana_databases(
            self,
            vault_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeHanaDatabases', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_hana_running_backups(
            self,
            vault_id=None,
            database_name=None,
            page_size=None,
            cluster_id=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeHanaRunningBackups', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "DatabaseName": database_name,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def create_hana_backup_plan(
            self,
            schedule=None,
            vault_id=None,
            backup_prefix=None,
            database_name=None,
            plan_name=None,
            cluster_id=None,
            backup_type=None,
            token=None):
        api_request = APIRequest('CreateHanaBackupPlan', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Schedule": schedule,
            "VaultId": vault_id,
            "BackupPrefix": backup_prefix,
            "DatabaseName": database_name,
            "PlanName": plan_name,
            "ClusterId": cluster_id,
            "BackupType": backup_type,
            "Token": token}
        return self._handle_request(api_request).result

    def delete_hana_backup_plan(self, vault_id=None, plan_id=None, cluster_id=None, token=None):
        api_request = APIRequest('DeleteHanaBackupPlan', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PlanId": plan_id,
            "ClusterId": cluster_id,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_hana_backup_plans(
            self,
            vault_id=None,
            database_name=None,
            page_size=None,
            cluster_id=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeHanaBackupPlans', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "DatabaseName": database_name,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def disable_hana_backup_plan(self, vault_id=None, plan_id=None, cluster_id=None, token=None):
        api_request = APIRequest('DisableHanaBackupPlan', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PlanId": plan_id,
            "ClusterId": cluster_id,
            "Token": token}
        return self._handle_request(api_request).result

    def enable_hana_backup_plan(self, vault_id=None, plan_id=None, cluster_id=None, token=None):
        api_request = APIRequest('EnableHanaBackupPlan', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PlanId": plan_id,
            "ClusterId": cluster_id,
            "Token": token}
        return self._handle_request(api_request).result

    def update_hana_backup_plan(
            self,
            schedule=None,
            vault_id=None,
            backup_prefix=None,
            plan_name=None,
            plan_id=None,
            cluster_id=None,
            token=None):
        api_request = APIRequest('UpdateHanaBackupPlan', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Schedule": schedule,
            "VaultId": vault_id,
            "BackupPrefix": backup_prefix,
            "PlanName": plan_name,
            "PlanId": plan_id,
            "ClusterId": cluster_id,
            "Token": token}
        return self._handle_request(api_request).result

    def execute_hana_backup_plan(self, vault_id=None, plan_id=None, cluster_id=None, token=None):
        api_request = APIRequest('ExecuteHanaBackupPlan', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PlanId": plan_id,
            "ClusterId": cluster_id,
            "Token": token}
        return self._handle_request(api_request).result

    def cancel_hana_restore(self, vault_id=None, database_name=None, cluster_id=None, token=None):
        api_request = APIRequest('CancelHanaRestore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "DatabaseName": database_name,
            "ClusterId": cluster_id,
            "Token": token}
        return self._handle_request(api_request).result

    def cancel_hana_backup(
            self,
            vault_id=None,
            database_name=None,
            backup_id=None,
            cluster_id=None,
            token=None):
        api_request = APIRequest('CancelHanaBackup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "DatabaseName": database_name,
            "BackupId": backup_id,
            "ClusterId": cluster_id,
            "Token": token}
        return self._handle_request(api_request).result

    def add_hana_metadata(
            self,
            updated_time=None,
            client_id=None,
            snapshot_id=None,
            vault_id=None,
            paths=None,
            cluster_id=None,
            token=None,
            sid=None,
            tags=None):
        api_request = APIRequest('AddHanaMetadata', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "UpdatedTime": updated_time,
            "ClientId": client_id,
            "SnapshotId": snapshot_id,
            "VaultId": vault_id,
            "Paths": paths,
            "ClusterId": cluster_id,
            "Token": token,
            "Sid": sid,
            "Tags": tags}
        return self._handle_request(api_request).result

    def check_hana_node(self, instance_id=None, region_id=None):
        api_request = APIRequest('CheckHanaNode', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def delete_hana_metadata(
            self,
            client_id=None,
            snapshot_id=None,
            vault_id=None,
            paths=None,
            cluster_id=None,
            token=None,
            sid=None,
            tags=None):
        api_request = APIRequest('DeleteHanaMetadata', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "SnapshotId": snapshot_id,
            "VaultId": vault_id,
            "Paths": paths,
            "ClusterId": cluster_id,
            "Token": token,
            "Sid": sid,
            "Tags": tags}
        return self._handle_request(api_request).result

    def create_hana_instance(
            self,
            hana_name=None,
            validate_certificate=None,
            ecs_instance_id=None,
            vault_id=None,
            contact_id=None,
            instance_number=None,
            use_ssl=None,
            token=None,
            sid=None,
            alert_setting=None,
            password=None,
            host=None,
            user_name=None):
        api_request = APIRequest('CreateHanaInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HanaName": hana_name,
            "ValidateCertificate": validate_certificate,
            "EcsInstanceId": ecs_instance_id,
            "VaultId": vault_id,
            "ContactId": contact_id,
            "InstanceNumber": instance_number,
            "UseSsl": use_ssl,
            "Token": token,
            "Sid": sid,
            "AlertSetting": alert_setting,
            "Password": password,
            "Host": host,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def describe_hana_metadata(
            self,
            end_snapshot_id=None,
            client_id=None,
            end_paths=None,
            vault_id=None,
            end_tags=None,
            start_tags=None,
            cluster_id=None,
            start_paths=None,
            token=None,
            sid=None,
            start_snapshot_id=None):
        api_request = APIRequest('DescribeHanaMetadata', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "EndSnapshotId": end_snapshot_id,
            "ClientId": client_id,
            "EndPaths": end_paths,
            "VaultId": vault_id,
            "EndTags": end_tags,
            "StartTags": start_tags,
            "ClusterId": cluster_id,
            "StartPaths": start_paths,
            "Token": token,
            "Sid": sid,
            "StartSnapshotId": start_snapshot_id}
        return self._handle_request(api_request).result

    def describe_hana_instances(
            self,
            vault_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeHanaInstances', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_hana_backup_setting(
            self,
            vault_id=None,
            database_name=None,
            cluster_id=None,
            token=None):
        api_request = APIRequest('DescribeHanaBackupSetting', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "DatabaseName": database_name,
            "ClusterId": cluster_id,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_hana_nodes(
            self,
            vault_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeHanaNodes', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def update_hana_backup_setting(
            self,
            log_backup_parameter_file=None,
            vault_id=None,
            log_backup_using_backint=None,
            log_backup_timeout=None,
            catalog_backup_using_backint=None,
            database_name=None,
            data_backup_parameter_file=None,
            cluster_id=None,
            enable_auto_log_backup=None,
            token=None,
            catalog_backup_parameter_file=None):
        api_request = APIRequest('UpdateHanaBackupSetting', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LogBackupParameterFile": log_backup_parameter_file,
            "VaultId": vault_id,
            "LogBackupUsingBackint": log_backup_using_backint,
            "LogBackupTimeout": log_backup_timeout,
            "CatalogBackupUsingBackint": catalog_backup_using_backint,
            "DatabaseName": database_name,
            "DataBackupParameterFile": data_backup_parameter_file,
            "ClusterId": cluster_id,
            "EnableAutoLogBackup": enable_auto_log_backup,
            "Token": token,
            "CatalogBackupParameterFile": catalog_backup_parameter_file}
        return self._handle_request(api_request).result

    def update_hana_instance(
            self,
            hana_name=None,
            validate_certificate=None,
            alert_setting=None,
            password=None,
            vault_id=None,
            contact_id=None,
            host=None,
            cluster_id=None,
            instance_number=None,
            use_ssl=None,
            token=None,
            user_name=None):
        api_request = APIRequest('UpdateHanaInstance', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "HanaName": hana_name,
            "ValidateCertificate": validate_certificate,
            "AlertSetting": alert_setting,
            "Password": password,
            "VaultId": vault_id,
            "ContactId": contact_id,
            "Host": host,
            "ClusterId": cluster_id,
            "InstanceNumber": instance_number,
            "UseSsl": use_ssl,
            "Token": token,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def report_statistics(
            self,
            statistics_type=None,
            client_id=None,
            vault_id=None,
            user_account_id=None,
            detail=None,
            token=None):
        api_request = APIRequest('ReportStatistics', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "StatisticsType": statistics_type,
            "ClientId": client_id,
            "VaultId": vault_id,
            "UserAccountId": user_account_id,
            "Detail": detail,
            "Token": token}
        return self._handle_request(api_request).result

    def verify_hana_nodes(self, vault_id=None, cluster_id=None, token=None):
        api_request = APIRequest('VerifyHanaNodes', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"VaultId": vault_id, "ClusterId": cluster_id, "Token": token}
        return self._handle_request(api_request).result

    def delete_clients(self, vault_id=None, token=None, client_ids=None):
        api_request = APIRequest('DeleteClients', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"VaultId": vault_id, "Token": token, "ClientIds": client_ids}
        return self._handle_request(api_request).result

    def uninstall_client(self, client_id=None, vault_id=None, token=None):
        api_request = APIRequest('UninstallClient', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"ClientId": client_id, "VaultId": vault_id, "Token": token}
        return self._handle_request(api_request).result

    def get_vault_list(self, vault_region_id=None):
        api_request = APIRequest('GetVaultList', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"VaultRegionId": vault_region_id}
        return self._handle_request(api_request).result

    def upgrade_client(self, client_id=None, vault_id=None, token=None):
        api_request = APIRequest('UpgradeClient', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"ClientId": client_id, "VaultId": vault_id, "Token": token}
        return self._handle_request(api_request).result

    def activate_ecs_client(
            self,
            ak_secret=None,
            client_id=None,
            vault_id=None,
            ak_id=None,
            token=None):
        api_request = APIRequest('ActivateEcsClient', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "AkSecret": ak_secret,
            "ClientId": client_id,
            "VaultId": vault_id,
            "AkId": ak_id,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_task(self, task_id=None, token=None):
        api_request = APIRequest('DescribeTask', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"TaskId": task_id, "Token": token}
        return self._handle_request(api_request).result

    def browse_files(
            self,
            snapshot_hash=None,
            path=None,
            client_id=None,
            security_token=None,
            vault_id=None,
            page_size=None,
            page_number=None,
            token=None):
        api_request = APIRequest('BrowseFiles', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "SnapshotHash": snapshot_hash,
            "Path": path,
            "ClientId": client_id,
            "SecurityToken": security_token,
            "VaultId": vault_id,
            "PageSize": page_size,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def cancel_job(self, job_id=None, client_id=None, vault_id=None, token=None):
        api_request = APIRequest('CancelJob', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ClientId": client_id,
            "VaultId": vault_id,
            "Token": token}
        return self._handle_request(api_request).result

    def cancel_restore(
            self,
            client_id=None,
            security_token=None,
            vault_id=None,
            restore_id=None,
            token=None):
        api_request = APIRequest('CancelRestore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "SecurityToken": security_token,
            "VaultId": vault_id,
            "RestoreId": restore_id,
            "Token": token}
        return self._handle_request(api_request).result

    def create_clients(
            self,
            alert_setting=None,
            client_type=None,
            vault_id=None,
            client_info=None,
            token=None):
        api_request = APIRequest('CreateClients', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "AlertSetting": alert_setting,
            "ClientType": client_type,
            "VaultId": vault_id,
            "ClientInfo": client_info,
            "Token": token}
        return self._handle_request(api_request).result

    def create_jobs(self, vault_id=None, jobs=None, job_type=None, token=None):
        api_request = APIRequest('CreateJobs', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "Jobs": jobs,
            "JobType": job_type,
            "Token": token}
        return self._handle_request(api_request).result

    def get_job_template_download_link(
            self,
            vault_id=None,
            token=None,
            show_delete_source_option=None):
        api_request = APIRequest('GetJobTemplateDownloadLink', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"VaultId": vault_id, "Token": token,
                               "ShowDeleteSourceOption": show_delete_source_option}
        return self._handle_request(api_request).result

    def execute_job(self, job_id=None, client_id=None, vault_id=None, token=None):
        api_request = APIRequest('ExecuteJob', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ClientId": client_id,
            "VaultId": vault_id,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_backup_jobs(
            self,
            vault_region_id=None,
            vault_id=None,
            page_size=None,
            job_type=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeBackupJobs', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultRegionId": vault_region_id,
            "VaultId": vault_id,
            "PageSize": page_size,
            "JobType": job_type,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_instances_info(
            self,
            inner_ip_addresses=None,
            instance_name=None,
            private_ip_addresses=None,
            region_id=None,
            instance_ids=None,
            vpc_id=None,
            page_size=None,
            network_type=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeInstancesInfo', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "InnerIpAddresses": inner_ip_addresses,
            "InstanceName": instance_name,
            "PrivateIpAddresses": private_ip_addresses,
            "RegionId": region_id,
            "InstanceIds": instance_ids,
            "VpcId": vpc_id,
            "PageSize": page_size,
            "NetworkType": network_type,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_restore_jobs(
            self,
            snapshot_id=None,
            vault_id=None,
            restore_id=None,
            source=None,
            page_number=None,
            token=None,
            target=None,
            restore_type=None,
            vault_region_id=None,
            security_token=None,
            page_size=None,
            status=None):
        api_request = APIRequest('DescribeRestoreJobs', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "SnapshotId": snapshot_id,
            "VaultId": vault_id,
            "RestoreId": restore_id,
            "Source": source,
            "PageNumber": page_number,
            "Token": token,
            "Target": target,
            "RestoreType": restore_type,
            "VaultRegionId": vault_region_id,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "Status": status}
        return self._handle_request(api_request).result

    def get_client_template_download_link(
            self,
            inner_ip_addresses=None,
            private_ip_addresses=None,
            region_id=None,
            token=None):
        api_request = APIRequest('GetClientTemplateDownloadLink', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "InnerIpAddresses": inner_ip_addresses,
            "PrivateIpAddresses": private_ip_addresses,
            "RegionId": region_id,
            "Token": token}
        return self._handle_request(api_request).result

    def get_snapshot_error_file_download_link(
            self,
            client_id=None,
            vault_id=None,
            error_file=None,
            token=None):
        api_request = APIRequest('GetSnapshotErrorFileDownloadLink', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "VaultId": vault_id,
            "ErrorFile": error_file,
            "Token": token}
        return self._handle_request(api_request).result

    def enable_job(self, job_id=None, client_id=None, vault_id=None, token=None):
        api_request = APIRequest('EnableJob', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ClientId": client_id,
            "VaultId": vault_id,
            "Token": token}
        return self._handle_request(api_request).result

    def disable_job(self, job_id=None, client_id=None, vault_id=None, token=None):
        api_request = APIRequest('DisableJob', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ClientId": client_id,
            "VaultId": vault_id,
            "Token": token}
        return self._handle_request(api_request).result

    def generate_mqtt_token(self, client_id=None, vault_id=None, user_account_id=None, token=None):
        api_request = APIRequest('GenerateMqttToken', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "VaultId": vault_id,
            "UserAccountId": user_account_id,
            "Token": token}
        return self._handle_request(api_request).result

    def check_beta(self, feature=None):
        api_request = APIRequest('CheckBeta', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"Feature": feature}
        return self._handle_request(api_request).result

    def search_backup_files(
            self,
            client_id=None,
            vault_id=None,
            next_token=None,
            query=None,
            limit=None,
            page_number=None,
            token=None):
        api_request = APIRequest('SearchBackupFiles', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "VaultId": vault_id,
            "NextToken": next_token,
            "Query": query,
            "Limit": limit,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def delete_client(self, client_id=None, vault_id=None, token=None):
        api_request = APIRequest('DeleteClient', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"ClientId": client_id, "VaultId": vault_id, "Token": token}
        return self._handle_request(api_request).result

    def send_mobile_verify_code(self, mobile=None, token=None):
        api_request = APIRequest('SendMobileVerifyCode', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"Mobile": mobile, "Token": token}
        return self._handle_request(api_request).result

    def send_email_verify_code(self, email=None, token=None):
        api_request = APIRequest('SendEmailVerifyCode', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"Email": email, "Token": token}
        return self._handle_request(api_request).result

    def describe_contacts(self, contact_id=None, page_size=None, page_number=None, token=None):
        api_request = APIRequest('DescribeContacts', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ContactId": contact_id,
            "PageSize": page_size,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def delete_contact(self, contact_id=None, token=None):
        api_request = APIRequest('DeleteContact', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"ContactId": contact_id, "Token": token}
        return self._handle_request(api_request).result

    def update_contact(
            self,
            email_verify_code=None,
            contact_id=None,
            name=None,
            mobile=None,
            description=None,
            mobile_verify_code=None,
            email=None,
            token=None):
        api_request = APIRequest('UpdateContact', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "EmailVerifyCode": email_verify_code,
            "ContactId": contact_id,
            "Name": name,
            "Mobile": mobile,
            "Description": description,
            "MobileVerifyCode": mobile_verify_code,
            "Email": email,
            "Token": token}
        return self._handle_request(api_request).result

    def create_contact(
            self,
            email_verify_code=None,
            name=None,
            mobile=None,
            description=None,
            mobile_verify_code=None,
            email=None,
            token=None):
        api_request = APIRequest('CreateContact', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "EmailVerifyCode": email_verify_code,
            "Name": name,
            "Mobile": mobile,
            "Description": description,
            "MobileVerifyCode": mobile_verify_code,
            "Email": email,
            "Token": token}
        return self._handle_request(api_request).result

    def update_client(
            self,
            source_types=None,
            alert_setting=None,
            client_id=None,
            vault_id=None,
            contact_id=None,
            cluster_id=None,
            token=None):
        api_request = APIRequest('UpdateClient', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "SourceTypes": source_types,
            "AlertSetting": alert_setting,
            "ClientId": client_id,
            "VaultId": vault_id,
            "ContactId": contact_id,
            "ClusterId": cluster_id,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_resource_packages(
            self,
            client_id=None,
            vault_id=None,
            page_size=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeResourcePackages', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "VaultId": vault_id,
            "PageSize": page_size,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def add_server(
            self,
            password=None,
            client_id=None,
            server_type=None,
            vault_id=None,
            host=None,
            description=None,
            detail_info=None,
            token=None,
            username=None):
        api_request = APIRequest('AddServer', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Password": password,
            "ClientId": client_id,
            "ServerType": server_type,
            "VaultId": vault_id,
            "Host": host,
            "Description": description,
            "DetailInfo": detail_info,
            "Token": token,
            "Username": username}
        return self._handle_request(api_request).result

    def remove_server(self, client_id=None, vault_id=None, server_id=None, token=None):
        api_request = APIRequest('RemoveServer', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "VaultId": vault_id,
            "ServerId": server_id,
            "Token": token}
        return self._handle_request(api_request).result

    def delete_server(self, client_id=None, vault_id=None, server_id=None, token=None):
        api_request = APIRequest('DeleteServer', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "VaultId": vault_id,
            "ServerId": server_id,
            "Token": token}
        return self._handle_request(api_request).result

    def update_server(
            self,
            password=None,
            client_id=None,
            server_type=None,
            vault_id=None,
            server_status=None,
            host=None,
            description=None,
            detail_info=None,
            server_id=None,
            token=None,
            username=None):
        api_request = APIRequest('UpdateServer', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Password": password,
            "ClientId": client_id,
            "ServerType": server_type,
            "VaultId": vault_id,
            "ServerStatus": server_status,
            "Host": host,
            "Description": description,
            "DetailInfo": detail_info,
            "ServerId": server_id,
            "Token": token,
            "Username": username}
        return self._handle_request(api_request).result

    def describe_servers(
            self,
            client_id=None,
            server_type=None,
            vault_id=None,
            server_status=None,
            page_size=None,
            is_removed=None,
            server_id=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeServers', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "ServerType": server_type,
            "VaultId": vault_id,
            "ServerStatus": server_status,
            "PageSize": page_size,
            "IsRemoved": is_removed,
            "ServerId": server_id,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def restore_server(self, client_id=None, vault_id=None, server_id=None, token=None):
        api_request = APIRequest('RestoreServer', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "VaultId": vault_id,
            "ServerId": server_id,
            "Token": token}
        return self._handle_request(api_request).result

    def create_plan(
            self,
            diff_policy_id=None,
            schedule_type=None,
            client_id=None,
            server_type=None,
            vault_id=None,
            inc_policy_id=None,
            source=None,
            server_id=None,
            token=None,
            plan_name=None,
            source_type=None,
            full_policy_id=None,
            retention=None):
        api_request = APIRequest('CreatePlan', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "DiffPolicyId": diff_policy_id,
            "ScheduleType": schedule_type,
            "ClientId": client_id,
            "ServerType": server_type,
            "VaultId": vault_id,
            "IncPolicyId": inc_policy_id,
            "Source": source,
            "ServerId": server_id,
            "Token": token,
            "PlanName": plan_name,
            "SourceType": source_type,
            "FullPolicyId": full_policy_id,
            "Retention": retention}
        return self._handle_request(api_request).result

    def update_plan(
            self,
            diff_policy_id=None,
            schedule_type=None,
            client_id=None,
            vault_id=None,
            plan_status=None,
            inc_policy_id=None,
            plan_name=None,
            plan_id=None,
            source=None,
            full_policy_id=None,
            retention=None,
            token=None):
        api_request = APIRequest('UpdatePlan', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "DiffPolicyId": diff_policy_id,
            "ScheduleType": schedule_type,
            "ClientId": client_id,
            "VaultId": vault_id,
            "PlanStatus": plan_status,
            "IncPolicyId": inc_policy_id,
            "PlanName": plan_name,
            "PlanId": plan_id,
            "Source": source,
            "FullPolicyId": full_policy_id,
            "Retention": retention,
            "Token": token}
        return self._handle_request(api_request).result

    def remove_plan(self, client_id=None, vault_id=None, plan_id=None, token=None):
        api_request = APIRequest('RemovePlan', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "VaultId": vault_id,
            "PlanId": plan_id,
            "Token": token}
        return self._handle_request(api_request).result

    def restore_plan(self, client_id=None, vault_id=None, plan_id=None, token=None):
        api_request = APIRequest('RestorePlan', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "VaultId": vault_id,
            "PlanId": plan_id,
            "Token": token}
        return self._handle_request(api_request).result

    def delete_plan(self, client_id=None, vault_id=None, plan_id=None, token=None):
        api_request = APIRequest('DeletePlan', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "VaultId": vault_id,
            "PlanId": plan_id,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_plans(
            self,
            schedule_type=None,
            client_id=None,
            server_type=None,
            vault_id=None,
            plan_status=None,
            page_size=None,
            plan_id=None,
            is_removed=None,
            source_type=None,
            server_id=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribePlans', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ScheduleType": schedule_type,
            "ClientId": client_id,
            "ServerType": server_type,
            "VaultId": vault_id,
            "PlanStatus": plan_status,
            "PageSize": page_size,
            "PlanId": plan_id,
            "IsRemoved": is_removed,
            "SourceType": source_type,
            "ServerId": server_id,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def renew_client_token(
            self,
            client_id=None,
            expire_in_seconds=None,
            vault_id=None,
            user_account_id=None,
            token=None):
        api_request = APIRequest('RenewClientToken', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "ExpireInSeconds": expire_in_seconds,
            "VaultId": vault_id,
            "UserAccountId": user_account_id,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_snapshot_history(
            self,
            vault_region_id=None,
            status_list=None,
            page_size=None,
            end_time=None,
            start_time=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeSnapshotHistory', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultRegionId": vault_region_id,
            "StatusList": status_list,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def create_restore(
            self,
            client_id=None,
            snapshot_id=None,
            excludes=None,
            source_client_id=None,
            vault_id=None,
            includes=None,
            source=None,
            server_id=None,
            token=None,
            restore_name=None,
            target=None,
            snapshot_hash=None,
            restore_type=None,
            extra=None,
            container_restore_id=None):
        api_request = APIRequest('CreateRestore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "SnapshotId": snapshot_id,
            "Excludes": excludes,
            "SourceClientId": source_client_id,
            "VaultId": vault_id,
            "Includes": includes,
            "Source": source,
            "ServerId": server_id,
            "Token": token,
            "RestoreName": restore_name,
            "Target": target,
            "SnapshotHash": snapshot_hash,
            "RestoreType": restore_type,
            "Extra": extra,
            "ContainerRestoreId": container_restore_id}
        return self._handle_request(api_request).result

    def delete_restore(
            self,
            client_id=None,
            vault_id=None,
            restore_id=None,
            user_account_id=None,
            token=None):
        api_request = APIRequest('DeleteRestore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "VaultId": vault_id,
            "RestoreId": restore_id,
            "UserAccountId": user_account_id,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_restores(
            self,
            client_id=None,
            snapshot_id=None,
            vault_id=None,
            restore_id=None,
            user_account_id=None,
            source=None,
            server_id=None,
            page_number=None,
            token=None,
            target=None,
            restore_type=None,
            page_size=None,
            container_restore_id=None,
            status=None):
        api_request = APIRequest('DescribeRestores', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "SnapshotId": snapshot_id,
            "VaultId": vault_id,
            "RestoreId": restore_id,
            "UserAccountId": user_account_id,
            "Source": source,
            "ServerId": server_id,
            "PageNumber": page_number,
            "Token": token,
            "Target": target,
            "RestoreType": restore_type,
            "PageSize": page_size,
            "ContainerRestoreId": container_restore_id,
            "Status": status}
        return self._handle_request(api_request).result

    def update_restore(
            self,
            actual_bytes=None,
            client_id=None,
            vault_id=None,
            restore_id=None,
            user_account_id=None,
            exit_code=None,
            token=None,
            duration=None,
            items_done=None,
            items_total=None,
            complete_time=None,
            error_count=None,
            bytes_done=None,
            bytes_total=None,
            status=None):
        api_request = APIRequest('UpdateRestore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ActualBytes": actual_bytes,
            "ClientId": client_id,
            "VaultId": vault_id,
            "RestoreId": restore_id,
            "UserAccountId": user_account_id,
            "ExitCode": exit_code,
            "Token": token,
            "Duration": duration,
            "ItemsDone": items_done,
            "ItemsTotal": items_total,
            "CompleteTime": complete_time,
            "ErrorCount": error_count,
            "BytesDone": bytes_done,
            "BytesTotal": bytes_total,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_jobs(
            self,
            job_id=None,
            client_id=None,
            policy_id=None,
            vault_id=None,
            job_status=None,
            page_size=None,
            user_account_id=None,
            job_type=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribeJobs', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ClientId": client_id,
            "PolicyId": policy_id,
            "VaultId": vault_id,
            "JobStatus": job_status,
            "PageSize": page_size,
            "UserAccountId": user_account_id,
            "JobType": job_type,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def update_job(
            self,
            current_snapshot_id=None,
            client_id=None,
            vault_id=None,
            job_status=None,
            user_account_id=None,
            source=None,
            token=None,
            job_id=None,
            schedule=None,
            policy_id=None,
            last_snapshot_id=None,
            job_option=None,
            job_name=None,
            retention=None):
        api_request = APIRequest('UpdateJob', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "CurrentSnapshotId": current_snapshot_id,
            "ClientId": client_id,
            "VaultId": vault_id,
            "JobStatus": job_status,
            "UserAccountId": user_account_id,
            "Source": source,
            "Token": token,
            "JobId": job_id,
            "Schedule": schedule,
            "PolicyId": policy_id,
            "LastSnapshotId": last_snapshot_id,
            "JobOption": job_option,
            "JobName": job_name,
            "Retention": retention}
        return self._handle_request(api_request).result

    def delete_job(
            self,
            job_id=None,
            client_id=None,
            vault_id=None,
            user_account_id=None,
            token=None):
        api_request = APIRequest('DeleteJob', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ClientId": client_id,
            "VaultId": vault_id,
            "UserAccountId": user_account_id,
            "Token": token}
        return self._handle_request(api_request).result

    def create_job(
            self,
            client_id=None,
            policy_id=None,
            vault_id=None,
            job_option=None,
            source_type=None,
            user_account_id=None,
            source=None,
            job_type=None,
            job_name=None,
            retention=None,
            token=None):
        api_request = APIRequest('CreateJob', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "PolicyId": policy_id,
            "VaultId": vault_id,
            "JobOption": job_option,
            "SourceType": source_type,
            "UserAccountId": user_account_id,
            "Source": source,
            "JobType": job_type,
            "JobName": job_name,
            "Retention": retention,
            "Token": token}
        return self._handle_request(api_request).result

    def generate_client_token(
            self,
            client_id=None,
            expire_in_seconds=None,
            vault_id=None,
            token=None):
        api_request = APIRequest('GenerateClientToken', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "ExpireInSeconds": expire_in_seconds,
            "VaultId": vault_id,
            "Token": token}
        return self._handle_request(api_request).result

    def generate_sts_credential(
            self,
            credential_type=None,
            client_id=None,
            expire_in_seconds=None,
            vault_id=None,
            user_account_id=None,
            token=None):
        api_request = APIRequest('GenerateStsCredential', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "CredentialType": credential_type,
            "ClientId": client_id,
            "ExpireInSeconds": expire_in_seconds,
            "VaultId": vault_id,
            "UserAccountId": user_account_id,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_client_version(
            self,
            client_type=None,
            current_version=None,
            platform_type=None,
            user_account_id=None,
            token=None):
        api_request = APIRequest('DescribeClientVersion', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientType": client_type,
            "CurrentVersion": current_version,
            "PlatformType": platform_type,
            "UserAccountId": user_account_id,
            "Token": token}
        return self._handle_request(api_request).result

    def activate_client(
            self,
            host_name=None,
            client_id=None,
            expire_in_seconds=None,
            client_version=None,
            vault_id=None,
            platform_type=None,
            user_account_id=None,
            network_type=None,
            token=None):
        api_request = APIRequest('ActivateClient', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "HostName": host_name,
            "ClientId": client_id,
            "ExpireInSeconds": expire_in_seconds,
            "ClientVersion": client_version,
            "VaultId": vault_id,
            "PlatformType": platform_type,
            "UserAccountId": user_account_id,
            "NetworkType": network_type,
            "Token": token}
        return self._handle_request(api_request).result

    def check_role(self, check_role_type=None):
        api_request = APIRequest('CheckRole', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"CheckRoleType": check_role_type}
        return self._handle_request(api_request).result

    def create_client(
            self,
            source_types=None,
            client_type=None,
            alert_setting=None,
            instance_id=None,
            vault_id=None,
            contact_id=None,
            client_name=None,
            platform_type=None,
            network_type=None,
            cluster_id=None,
            token=None):
        api_request = APIRequest('CreateClient', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "SourceTypes": source_types,
            "ClientType": client_type,
            "AlertSetting": alert_setting,
            "InstanceId": instance_id,
            "VaultId": vault_id,
            "ContactId": contact_id,
            "ClientName": client_name,
            "PlatformType": platform_type,
            "NetworkType": network_type,
            "ClusterId": cluster_id,
            "Token": token}
        return self._handle_request(api_request).result

    def create_policy(
            self,
            schedule=None,
            client_id=None,
            vault_id=None,
            policy_name=None,
            source=None,
            retention=None,
            token=None,
            status=None):
        api_request = APIRequest('CreatePolicy', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Schedule": schedule,
            "ClientId": client_id,
            "VaultId": vault_id,
            "PolicyName": policy_name,
            "Source": source,
            "Retention": retention,
            "Token": token,
            "Status": status}
        return self._handle_request(api_request).result

    def create_snapshot(
            self,
            client_id=None,
            vault_id=None,
            snapshot_name=None,
            user_account_id=None,
            source=None,
            parent_hash=None,
            container_snapshot_id=None,
            server_id=None,
            token=None,
            snapshot_option=None,
            job_id=None,
            snapshot_type=None,
            extra=None,
            source_type=None,
            plan_id=None,
            retention=None):
        api_request = APIRequest('CreateSnapshot', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "VaultId": vault_id,
            "SnapshotName": snapshot_name,
            "UserAccountId": user_account_id,
            "Source": source,
            "ParentHash": parent_hash,
            "ContainerSnapshotId": container_snapshot_id,
            "ServerId": server_id,
            "Token": token,
            "SnapshotOption": snapshot_option,
            "JobId": job_id,
            "SnapshotType": snapshot_type,
            "Extra": extra,
            "SourceType": source_type,
            "PlanId": plan_id,
            "Retention": retention}
        return self._handle_request(api_request).result

    def create_vault(
            self,
            replication_source_vault_id=None,
            vault_region_id=None,
            vault_storage_class=None,
            vault_type=None,
            search_enabled=None,
            description=None,
            vault_name=None,
            token=None):
        api_request = APIRequest('CreateVault', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ReplicationSourceVaultId": replication_source_vault_id,
            "VaultRegionId": vault_region_id,
            "VaultStorageClass": vault_storage_class,
            "VaultType": vault_type,
            "SearchEnabled": search_enabled,
            "Description": description,
            "VaultName": vault_name,
            "Token": token}
        return self._handle_request(api_request).result

    def deactivate_client(self, client_id=None, vault_id=None, token=None):
        api_request = APIRequest('DeactivateClient', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"ClientId": client_id, "VaultId": vault_id, "Token": token}
        return self._handle_request(api_request).result

    def delete_policy(self, client_id=None, policy_id=None, vault_id=None, token=None):
        api_request = APIRequest('DeletePolicy', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "PolicyId": policy_id,
            "VaultId": vault_id,
            "Token": token}
        return self._handle_request(api_request).result

    def delete_snapshot(
            self,
            client_id=None,
            snapshot_id=None,
            vault_id=None,
            user_account_id=None,
            token=None):
        api_request = APIRequest('DeleteSnapshot', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "SnapshotId": snapshot_id,
            "VaultId": vault_id,
            "UserAccountId": user_account_id,
            "Token": token}
        return self._handle_request(api_request).result

    def delete_vault(self, vault_id=None, token=None):
        api_request = APIRequest('DeleteVault', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"VaultId": vault_id, "Token": token}
        return self._handle_request(api_request).result

    def describe_clients(
            self,
            client_type=None,
            inner_ip_addresses=None,
            client_id=None,
            private_ip_addresses=None,
            vault_id=None,
            cluster_id=None,
            page_number=None,
            token=None,
            vault_region_id=None,
            instance_ids=None,
            page_size=None,
            source_type=None,
            status=None):
        api_request = APIRequest('DescribeClients', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientType": client_type,
            "InnerIpAddresses": inner_ip_addresses,
            "ClientId": client_id,
            "PrivateIpAddresses": private_ip_addresses,
            "VaultId": vault_id,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "Token": token,
            "VaultRegionId": vault_region_id,
            "InstanceIds": instance_ids,
            "PageSize": page_size,
            "SourceType": source_type,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_policies(
            self,
            client_id=None,
            policy_id=None,
            vault_id=None,
            page_size=None,
            page_number=None,
            token=None):
        api_request = APIRequest('DescribePolicies', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "PolicyId": policy_id,
            "VaultId": vault_id,
            "PageSize": page_size,
            "PageNumber": page_number,
            "Token": token}
        return self._handle_request(api_request).result

    def describe_regions(self, token=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"Token": token}
        return self._handle_request(api_request).result

    def describe_snapshots(
            self,
            client_id=None,
            snapshot_id=None,
            status_list=None,
            vault_id=None,
            user_account_id=None,
            source=None,
            parent_hash=None,
            container_snapshot_id=None,
            server_id=None,
            page_number=None,
            token=None,
            job_id=None,
            complete_time_before=None,
            snapshot_type=None,
            complete_time_after=None,
            page_size=None,
            plan_id=None,
            status=None):
        api_request = APIRequest('DescribeSnapshots', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "SnapshotId": snapshot_id,
            "StatusList": status_list,
            "VaultId": vault_id,
            "UserAccountId": user_account_id,
            "Source": source,
            "ParentHash": parent_hash,
            "ContainerSnapshotId": container_snapshot_id,
            "ServerId": server_id,
            "PageNumber": page_number,
            "Token": token,
            "JobId": job_id,
            "CompleteTimeBefore": complete_time_before,
            "SnapshotType": snapshot_type,
            "CompleteTimeAfter": complete_time_after,
            "PageSize": page_size,
            "PlanId": plan_id,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_user_business_status(self, user_account_id=None, token=None):
        api_request = APIRequest('DescribeUserBusinessStatus', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserAccountId": user_account_id, "Token": token}
        return self._handle_request(api_request).result

    def describe_vaults(
            self,
            vault_region_id=None,
            vault_id=None,
            vault_type=None,
            page_size=None,
            page_number=None,
            status=None,
            token=None):
        api_request = APIRequest('DescribeVaults', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultRegionId": vault_region_id,
            "VaultId": vault_id,
            "VaultType": vault_type,
            "PageSize": page_size,
            "PageNumber": page_number,
            "Status": status,
            "Token": token}
        return self._handle_request(api_request).result

    def generate_token(self, client_id=None):
        api_request = APIRequest('GenerateToken', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClientId": client_id}
        return self._handle_request(api_request).result

    def get_client_download_link(self, client_type=None, platform_type=None, token=None):
        api_request = APIRequest('GetClientDownloadLink', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ClientType": client_type,
            "PlatformType": platform_type,
            "Token": token}
        return self._handle_request(api_request).result

    def update_policy(
            self,
            schedule=None,
            client_id=None,
            policy_id=None,
            vault_id=None,
            last_run_time=None,
            policy_name=None,
            source=None,
            retention=None,
            token=None,
            status=None):
        api_request = APIRequest('UpdatePolicy', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Schedule": schedule,
            "ClientId": client_id,
            "PolicyId": policy_id,
            "VaultId": vault_id,
            "LastRunTime": last_run_time,
            "PolicyName": policy_name,
            "Source": source,
            "Retention": retention,
            "Token": token,
            "Status": status}
        return self._handle_request(api_request).result

    def update_snapshot(
            self,
            error_message=None,
            actual_bytes=None,
            snapshot_id=None,
            client_id=None,
            vault_id=None,
            error_file=None,
            user_account_id=None,
            parent_hash=None,
            exit_code=None,
            token=None,
            duration=None,
            snapshot_hash=None,
            items_done=None,
            size=None,
            items_total=None,
            complete_time=None,
            error_count=None,
            bytes_done=None,
            bytes_total=None,
            status=None):
        api_request = APIRequest('UpdateSnapshot', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ErrorMessage": error_message,
            "ActualBytes": actual_bytes,
            "SnapshotId": snapshot_id,
            "ClientId": client_id,
            "VaultId": vault_id,
            "ErrorFile": error_file,
            "UserAccountId": user_account_id,
            "ParentHash": parent_hash,
            "ExitCode": exit_code,
            "Token": token,
            "Duration": duration,
            "SnapshotHash": snapshot_hash,
            "ItemsDone": items_done,
            "Size": size,
            "ItemsTotal": items_total,
            "CompleteTime": complete_time,
            "ErrorCount": error_count,
            "BytesDone": bytes_done,
            "BytesTotal": bytes_total,
            "Status": status}
        return self._handle_request(api_request).result

    def update_vault(self, vault_id=None, search_enabled=None, description=None, vault_name=None):
        api_request = APIRequest('UpdateVault', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VaultId": vault_id,
            "SearchEnabled": search_enabled,
            "Description": description,
            "VaultName": vault_name}
        return self._handle_request(api_request).result
