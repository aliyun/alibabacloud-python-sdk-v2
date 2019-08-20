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


class DbsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Dbs'
        self.api_version = '2019-03-06'
        self.location_service_code = 'cbs'
        self.location_endpoint_type = 'openAPI'

    def modify_backup_strategy(
            self,
            backup_period=None,
            backup_start_time=None,
            client_token=None,
            backup_plan_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyBackupStrategy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BackupPeriod": backup_period,
            "BackupStartTime": backup_start_time,
            "ClientToken": client_token,
            "BackupPlanId": backup_plan_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_backup_source_endpoint(
            self,
            source_endpoint_region=None,
            backup_gateway_id=None,
            source_endpoint_instance_id=None,
            source_endpoint_user_name=None,
            client_token=None,
            source_endpoint_password=None,
            backup_plan_id=None,
            backup_objects=None,
            owner_id=None,
            source_endpoint_port=None,
            source_endpoint_database_name=None,
            source_endpoint_instance_type=None,
            source_endpoint_ip=None,
            source_endpoint_oracle_sid=None):
        api_request = APIRequest('ModifyBackupSourceEndpoint', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceEndpointRegion": source_endpoint_region,
            "BackupGatewayId": backup_gateway_id,
            "SourceEndpointInstanceID": source_endpoint_instance_id,
            "SourceEndpointUserName": source_endpoint_user_name,
            "ClientToken": client_token,
            "SourceEndpointPassword": source_endpoint_password,
            "BackupPlanId": backup_plan_id,
            "BackupObjects": backup_objects,
            "OwnerId": owner_id,
            "SourceEndpointPort": source_endpoint_port,
            "SourceEndpointDatabaseName": source_endpoint_database_name,
            "SourceEndpointInstanceType": source_endpoint_instance_type,
            "SourceEndpointIP": source_endpoint_ip,
            "SourceEndpointOracleSID": source_endpoint_oracle_sid}
        return self._handle_request(api_request).result

    def modify_backup_plan_name(
            self,
            backup_plan_name=None,
            client_token=None,
            backup_plan_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyBackupPlanName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BackupPlanName": backup_plan_name,
            "ClientToken": client_token,
            "BackupPlanId": backup_plan_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def renew_backup_plan(
            self,
            period=None,
            client_token=None,
            backup_plan_id=None,
            owner_id=None,
            used_time=None):
        api_request = APIRequest('RenewBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "ClientToken": client_token,
            "BackupPlanId": backup_plan_id,
            "OwnerId": owner_id,
            "UsedTime": used_time}
        return self._handle_request(api_request).result

    def modify_backup_objects(
            self,
            client_token=None,
            backup_plan_id=None,
            backup_objects=None,
            owner_id=None):
        api_request = APIRequest('ModifyBackupObjects', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "BackupPlanId": backup_plan_id,
            "BackupObjects": backup_objects,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_restore_task_list(
            self,
            client_token=None,
            restore_task_id=None,
            page_size=None,
            backup_plan_id=None,
            page_num=None,
            owner_id=None):
        api_request = APIRequest('DescribeRestoreTaskList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "RestoreTaskId": restore_task_id,
            "PageSize": page_size,
            "BackupPlanId": backup_plan_id,
            "PageNum": page_num,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_node_cidr_list(self, client_token=None, region=None, owner_id=None):
        api_request = APIRequest('DescribeNodeCidrList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClientToken": client_token, "Region": region, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_restore_task(self, client_token=None, restore_task_id=None, owner_id=None):
        api_request = APIRequest('StartRestoreTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "RestoreTaskId": restore_task_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_restore_task(
            self,
            backup_gateway_id=None,
            destination_endpoint_oracle_sid=None,
            restore_time=None,
            destination_endpoint_instance_type=None,
            client_token=None,
            destination_endpoint_instance_id=None,
            destination_endpoint_port=None,
            backup_plan_id=None,
            backup_set_id=None,
            owner_id=None,
            destination_endpoint_region=None,
            restore_dir=None,
            destination_endpoint_ip=None,
            destination_endpoint_database_name=None,
            destination_endpoint_user_name=None,
            restore_objects=None,
            restore_task_name=None,
            duplicate_conflict=None,
            destination_endpoint_password=None):
        api_request = APIRequest('CreateRestoreTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BackupGatewayId": backup_gateway_id,
            "DestinationEndpointOracleSID": destination_endpoint_oracle_sid,
            "RestoreTime": restore_time,
            "DestinationEndpointInstanceType": destination_endpoint_instance_type,
            "ClientToken": client_token,
            "DestinationEndpointInstanceID": destination_endpoint_instance_id,
            "DestinationEndpointPort": destination_endpoint_port,
            "BackupPlanId": backup_plan_id,
            "BackupSetId": backup_set_id,
            "OwnerId": owner_id,
            "DestinationEndpointRegion": destination_endpoint_region,
            "RestoreDir": restore_dir,
            "DestinationEndpointIP": destination_endpoint_ip,
            "DestinationEndpointDatabaseName": destination_endpoint_database_name,
            "DestinationEndpointUserName": destination_endpoint_user_name,
            "RestoreObjects": restore_objects,
            "RestoreTaskName": restore_task_name,
            "DuplicateConflict": duplicate_conflict,
            "DestinationEndpointPassword": destination_endpoint_password}
        return self._handle_request(api_request).result

    def describe_backup_plan_list(
            self,
            client_token=None,
            page_size=None,
            backup_plan_id=None,
            region=None,
            page_num=None,
            owner_id=None):
        api_request = APIRequest('DescribeBackupPlanList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "PageSize": page_size,
            "BackupPlanId": backup_plan_id,
            "Region": region,
            "PageNum": page_num,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_full_backup_list(
            self,
            client_token=None,
            page_size=None,
            backup_plan_id=None,
            page_num=None,
            owner_id=None):
        api_request = APIRequest('DescribeFullBackupList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "PageSize": page_size,
            "BackupPlanId": backup_plan_id,
            "PageNum": page_num,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_backup_plan(
            self,
            stop_method=None,
            client_token=None,
            backup_plan_id=None,
            owner_id=None):
        api_request = APIRequest('StopBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StopMethod": stop_method,
            "ClientToken": client_token,
            "BackupPlanId": backup_plan_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_backup_gateway_list(
            self,
            identifier=None,
            client_token=None,
            page_size=None,
            region=None,
            page_num=None,
            owner_id=None):
        api_request = APIRequest('DescribeBackupGatewayList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Identifier": identifier,
            "ClientToken": client_token,
            "PageSize": page_size,
            "Region": region,
            "PageNum": page_num,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_increment_backup_list(
            self,
            client_token=None,
            page_size=None,
            backup_plan_id=None,
            page_num=None,
            owner_id=None):
        api_request = APIRequest('DescribeIncrementBackupList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "PageSize": page_size,
            "BackupPlanId": backup_plan_id,
            "PageNum": page_num,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def configure_backup_plan(
            self,
            source_endpoint_region=None,
            duplication_archive_period=None,
            backup_gateway_id=None,
            source_endpoint_instance_id=None,
            source_endpoint_user_name=None,
            client_token=None,
            source_endpoint_password=None,
            backup_plan_id=None,
            backup_objects=None,
            owner_id=None,
            source_endpoint_port=None,
            source_endpoint_database_name=None,
            backup_retention_period=None,
            duplication_infrequent_access_period=None,
            backup_period=None,
            backup_start_time=None,
            source_endpoint_instance_type=None,
            source_endpoint_ip=None,
            backup_plan_name=None,
            source_endpoint_oracle_sid=None,
            oss_bucket_name=None,
            enable_backup_log=None):
        api_request = APIRequest('ConfigureBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceEndpointRegion": source_endpoint_region,
            "DuplicationArchivePeriod": duplication_archive_period,
            "BackupGatewayId": backup_gateway_id,
            "SourceEndpointInstanceID": source_endpoint_instance_id,
            "SourceEndpointUserName": source_endpoint_user_name,
            "ClientToken": client_token,
            "SourceEndpointPassword": source_endpoint_password,
            "BackupPlanId": backup_plan_id,
            "BackupObjects": backup_objects,
            "OwnerId": owner_id,
            "SourceEndpointPort": source_endpoint_port,
            "SourceEndpointDatabaseName": source_endpoint_database_name,
            "BackupRetentionPeriod": backup_retention_period,
            "DuplicationInfrequentAccessPeriod": duplication_infrequent_access_period,
            "BackupPeriod": backup_period,
            "BackupStartTime": backup_start_time,
            "SourceEndpointInstanceType": source_endpoint_instance_type,
            "SourceEndpointIP": source_endpoint_ip,
            "BackupPlanName": backup_plan_name,
            "SourceEndpointOracleSID": source_endpoint_oracle_sid,
            "OSSBucketName": oss_bucket_name,
            "EnableBackupLog": enable_backup_log}
        return self._handle_request(api_request).result

    def start_backup_plan(self, client_token=None, backup_plan_id=None, owner_id=None):
        api_request = APIRequest('StartBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "BackupPlanId": backup_plan_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_backup_plan(
            self,
            database_type=None,
            period=None,
            client_token=None,
            owner_id=None,
            used_time=None,
            instance_class=None,
            storage_type=None,
            backup_method=None,
            database_region=None,
            storage_region=None,
            instance_type=None,
            region=None,
            pay_type=None):
        api_request = APIRequest('CreateBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DatabaseType": database_type,
            "Period": period,
            "ClientToken": client_token,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "InstanceClass": instance_class,
            "StorageType": storage_type,
            "BackupMethod": backup_method,
            "DatabaseRegion": database_region,
            "StorageRegion": storage_region,
            "InstanceType": instance_type,
            "Region": region,
            "PayType": pay_type}
        return self._handle_request(api_request).result
