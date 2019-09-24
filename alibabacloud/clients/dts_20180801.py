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


class DtsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Dts'
        self.api_version = '2018-08-01'
        self.location_service_code = 'dts'
        self.location_endpoint_type = 'openAPI'

    def describe_consumer_group(
            self,
            page_size=None,
            subscription_instance_id=None,
            page_num=None,
            owner_id=None):
        api_request = APIRequest('DescribeConsumerGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "SubscriptionInstanceId": subscription_instance_id,
            "PageNum": page_num,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_consumer_group_password(
            self,
            consumer_group_name=None,
            consumer_group_user_name=None,
            consumer_group_id=None,
            subscription_instance_id=None,
            owner_id=None,
            consumer_group_new_password=None,
            consumer_group_password=None):
        api_request = APIRequest('ModifyConsumerGroupPassword', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "ConsumerGroupName": consumer_group_name,
            "ConsumerGroupUserName": consumer_group_user_name,
            "ConsumerGroupID": consumer_group_id,
            "SubscriptionInstanceId": subscription_instance_id,
            "OwnerId": owner_id,
            "consumerGroupNewPassword": consumer_group_new_password,
            "ConsumerGroupPassword": consumer_group_password}
        return self._handle_request(api_request).result

    def delete_consumer_group(
            self,
            consumer_group_id=None,
            subscription_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteConsumerGroup', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "ConsumerGroupID": consumer_group_id,
            "SubscriptionInstanceId": subscription_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_consumer_group(
            self,
            consumer_group_name=None,
            consumer_group_user_name=None,
            subscription_instance_id=None,
            owner_id=None,
            consumer_group_password=None):
        api_request = APIRequest('CreateConsumerGroup', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "ConsumerGroupName": consumer_group_name,
            "ConsumerGroupUserName": consumer_group_user_name,
            "SubscriptionInstanceId": subscription_instance_id,
            "OwnerId": owner_id,
            "ConsumerGroupPassword": consumer_group_password}
        return self._handle_request(api_request).result

    def reset_synchronization_job(
            self,
            synchronization_job_id=None,
            owner_id=None,
            synchronization_direction=None):
        api_request = APIRequest('ResetSynchronizationJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SynchronizationJobId": synchronization_job_id,
            "OwnerId": owner_id,
            "SynchronizationDirection": synchronization_direction}
        return self._handle_request(api_request).result

    def switch_synchronization_endpoint(
            self,
            synchronization_job_id=None,
            endpoint_type=None,
            endpoint_instance_type=None,
            endpoint_port=None,
            endpoint_instance_id=None,
            endpoint_ip=None,
            owner_id=None,
            synchronization_direction=None):
        api_request = APIRequest('SwitchSynchronizationEndpoint', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SynchronizationJobId": synchronization_job_id,
            "Endpoint.Type": endpoint_type,
            "Endpoint.InstanceType": endpoint_instance_type,
            "Endpoint.Port": endpoint_port,
            "Endpoint.InstanceId": endpoint_instance_id,
            "Endpoint.IP": endpoint_ip,
            "OwnerId": owner_id,
            "SynchronizationDirection": synchronization_direction}
        return self._handle_request(api_request).result

    def describe_endpoint_switch_status(self, client_token=None, owner_id=None, task_id=None):
        api_request = APIRequest('DescribeEndpointSwitchStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClientToken": client_token, "OwnerId": owner_id, "TaskId": task_id}
        return self._handle_request(api_request).result

    def modify_migration_object(
            self,
            migration_object=None,
            client_token=None,
            migration_job_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyMigrationObject', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "MigrationObject": migration_object,
            "ClientToken": client_token,
            "MigrationJobId": migration_job_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_initialization_status(
            self,
            synchronization_job_id=None,
            page_size=None,
            page_num=None,
            owner_id=None):
        api_request = APIRequest('DescribeInitializationStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SynchronizationJobId": synchronization_job_id,
            "PageSize": page_size,
            "PageNum": page_num,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def configure_migration_job(
            self,
            source_endpoint_instance_id=None,
            checkpoint=None,
            source_endpoint_engine_name=None,
            source_endpoint_oracle_sid=None,
            destination_endpoint_instance_id=None,
            source_endpoint_ip=None,
            destination_endpoint_password=None,
            migration_object=None,
            migration_mode_data_intialization=None,
            migration_job_id=None,
            source_endpoint_instance_type=None,
            destination_endpoint_engine_name=None,
            migration_mode_structure_intialization=None,
            migration_mode_data_synchronization=None,
            destination_endpoint_region=None,
            source_endpoint_user_name=None,
            source_endpoint_database_name=None,
            source_endpoint_port=None,
            source_endpoint_owner_id=None,
            destination_endpoint_user_name=None,
            destination_endpoint_port=None,
            source_endpoint_region=None,
            source_endpoint_role=None,
            owner_id=None,
            destination_endpoint_data_base_name=None,
            source_endpoint_password=None,
            migration_reserved=None,
            destination_endpoint_ip=None,
            migration_job_name=None,
            destination_endpoint_instance_type=None):
        api_request = APIRequest('ConfigureMigrationJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceEndpoint.InstanceID": source_endpoint_instance_id,
            "Checkpoint": checkpoint,
            "SourceEndpoint.EngineName": source_endpoint_engine_name,
            "SourceEndpoint.OracleSID": source_endpoint_oracle_sid,
            "DestinationEndpoint.InstanceID": destination_endpoint_instance_id,
            "SourceEndpoint.IP": source_endpoint_ip,
            "DestinationEndpoint.Password": destination_endpoint_password,
            "MigrationObject": migration_object,
            "MigrationMode.DataIntialization": migration_mode_data_intialization,
            "MigrationJobId": migration_job_id,
            "SourceEndpoint.InstanceType": source_endpoint_instance_type,
            "DestinationEndpoint.EngineName": destination_endpoint_engine_name,
            "MigrationMode.StructureIntialization": migration_mode_structure_intialization,
            "MigrationMode.DataSynchronization": migration_mode_data_synchronization,
            "DestinationEndpoint.Region": destination_endpoint_region,
            "SourceEndpoint.UserName": source_endpoint_user_name,
            "SourceEndpoint.DatabaseName": source_endpoint_database_name,
            "SourceEndpoint.Port": source_endpoint_port,
            "SourceEndpoint.OwnerID": source_endpoint_owner_id,
            "DestinationEndpoint.UserName": destination_endpoint_user_name,
            "DestinationEndpoint.Port": destination_endpoint_port,
            "SourceEndpoint.Region": source_endpoint_region,
            "SourceEndpoint.Role": source_endpoint_role,
            "OwnerId": owner_id,
            "DestinationEndpoint.DataBaseName": destination_endpoint_data_base_name,
            "SourceEndpoint.Password": source_endpoint_password,
            "MigrationReserved": migration_reserved,
            "DestinationEndpoint.IP": destination_endpoint_ip,
            "MigrationJobName": migration_job_name,
            "DestinationEndpoint.InstanceType": destination_endpoint_instance_type}
        return self._handle_request(api_request).result

    def configure_subscription_instance(
            self,
            source_endpoint_instance_id=None,
            source_endpoint_port=None,
            source_endpoint_oracle_sid=None,
            source_endpoint_owner_id=None,
            source_endpoint_ip=None,
            subscription_instance_vpc_id=None,
            subscription_instance_network_type=None,
            subscription_data_type_dml=None,
            subscription_instance_id=None,
            source_endpoint_role=None,
            owner_id=None,
            source_endpoint_instance_type=None,
            subscription_data_type_ddl=None,
            source_endpoint_password=None,
            subscription_object=None,
            subscription_instance_vswitch_id=None,
            subscription_instance_name=None,
            source_endpoint_user_name=None,
            source_endpoint_database_name=None):
        api_request = APIRequest('ConfigureSubscriptionInstance', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceEndpoint.InstanceID": source_endpoint_instance_id,
            "SourceEndpoint.Port": source_endpoint_port,
            "SourceEndpoint.OracleSID": source_endpoint_oracle_sid,
            "SourceEndpoint.OwnerID": source_endpoint_owner_id,
            "SourceEndpoint.IP": source_endpoint_ip,
            "SubscriptionInstance.VPCId": subscription_instance_vpc_id,
            "SubscriptionInstanceNetworkType": subscription_instance_network_type,
            "SubscriptionDataType.DML": subscription_data_type_dml,
            "SubscriptionInstanceId": subscription_instance_id,
            "SourceEndpoint.Role": source_endpoint_role,
            "OwnerId": owner_id,
            "SourceEndpoint.InstanceType": source_endpoint_instance_type,
            "SubscriptionDataType.DDL": subscription_data_type_ddl,
            "SourceEndpoint.Password": source_endpoint_password,
            "SubscriptionObject": subscription_object,
            "SubscriptionInstance.VSwitchId": subscription_instance_vswitch_id,
            "SubscriptionInstanceName": subscription_instance_name,
            "SourceEndpoint.UserName": source_endpoint_user_name,
            "SourceEndpoint.DatabaseName": source_endpoint_database_name}
        return self._handle_request(api_request).result

    def describe_migration_job_status(
            self,
            client_token=None,
            migration_job_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeMigrationJobStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "MigrationJobId": migration_job_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_migration_job(self, migration_job_id=None, owner_id=None):
        api_request = APIRequest('StartMigrationJob', 'POST', 'http', 'RPC', 'query')
        api_request._params = {"MigrationJobId": migration_job_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_consumption_timestamp(
            self,
            subscription_instance_id=None,
            consumption_timestamp=None,
            owner_id=None):
        api_request = APIRequest('ModifyConsumptionTimestamp', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "SubscriptionInstanceId": subscription_instance_id,
            "ConsumptionTimestamp": consumption_timestamp,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_migration_job_detail(
            self,
            migration_mode_data_synchronization=None,
            client_token=None,
            migration_mode_data_initialization=None,
            page_size=None,
            migration_job_id=None,
            page_num=None,
            owner_id=None,
            migration_mode_structure_initialization=None):
        api_request = APIRequest('DescribeMigrationJobDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MigrationMode.DataSynchronization": migration_mode_data_synchronization,
            "ClientToken": client_token,
            "MigrationMode.DataInitialization": migration_mode_data_initialization,
            "PageSize": page_size,
            "MigrationJobId": migration_job_id,
            "PageNum": page_num,
            "OwnerId": owner_id,
            "MigrationMode.StructureInitialization": migration_mode_structure_initialization}
        return self._handle_request(api_request).result

    def create_subscription_instance(
            self,
            period=None,
            client_token=None,
            region=None,
            owner_id=None,
            pay_type=None,
            used_time=None,
            source_endpoint_instance_type=None):
        api_request = APIRequest('CreateSubscriptionInstance', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "ClientToken": client_token,
            "Region": region,
            "OwnerId": owner_id,
            "PayType": pay_type,
            "UsedTime": used_time,
            "SourceEndpoint.InstanceType": source_endpoint_instance_type}
        return self._handle_request(api_request).result

    def describe_migration_jobs(
            self,
            page_size=None,
            migration_job_name=None,
            page_num=None,
            owner_id=None):
        api_request = APIRequest('DescribeMigrationJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "MigrationJobName": migration_job_name,
            "PageNum": page_num,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_subscription_instance(self, subscription_instance_id=None, owner_id=None):
        api_request = APIRequest('StartSubscriptionInstance', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "SubscriptionInstanceId": subscription_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_subscription_instance_status(self, subscription_instance_id=None, owner_id=None):
        api_request = APIRequest('DescribeSubscriptionInstanceStatus',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SubscriptionInstanceId": subscription_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_subscription_object_modify_status(
            self,
            client_token=None,
            subscription_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeSubscriptionObjectModifyStatus',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "SubscriptionInstanceId": subscription_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_subscription_instance(self, subscription_instance_id=None, owner_id=None):
        api_request = APIRequest('DeleteSubscriptionInstance', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "SubscriptionInstanceId": subscription_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_subscription_instances(
            self,
            client_token=None,
            page_size=None,
            subscription_instance_name=None,
            page_num=None,
            owner_id=None):
        api_request = APIRequest('DescribeSubscriptionInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "PageSize": page_size,
            "SubscriptionInstanceName": subscription_instance_name,
            "PageNum": page_num,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def suspend_migration_job(self, client_token=None, migration_job_id=None, owner_id=None):
        api_request = APIRequest('SuspendMigrationJob', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "MigrationJobId": migration_job_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_migration_job(self, client_token=None, migration_job_id=None, owner_id=None):
        api_request = APIRequest('StopMigrationJob', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "MigrationJobId": migration_job_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_migration_job(
            self,
            client_token=None,
            region=None,
            migration_job_class=None,
            owner_id=None):
        api_request = APIRequest('CreateMigrationJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "Region": region,
            "MigrationJobClass": migration_job_class,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_migration_job(self, migration_job_id=None, owner_id=None):
        api_request = APIRequest('DeleteMigrationJob', 'POST', 'http', 'RPC', 'query')
        api_request._params = {"MigrationJobId": migration_job_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_subscription_object(
            self,
            subscription_object=None,
            subscription_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifySubscriptionObject', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "SubscriptionObject": subscription_object,
            "SubscriptionInstanceId": subscription_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_synchronization_job(
            self,
            synchronization_job_id=None,
            owner_id=None,
            synchronization_direction=None):
        api_request = APIRequest('StartSynchronizationJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SynchronizationJobId": synchronization_job_id,
            "OwnerId": owner_id,
            "SynchronizationDirection": synchronization_direction}
        return self._handle_request(api_request).result

    def configure_synchronization_job(
            self,
            source_endpoint_instance_id=None,
            checkpoint=None,
            destination_endpoint_instance_id=None,
            source_endpoint_ip=None,
            synchronization_objects=None,
            destination_endpoint_password=None,
            data_initialization=None,
            structure_initialization=None,
            partition_key_modify_time__minute=None,
            partition_key_modify_time__day=None,
            source_endpoint_instance_type=None,
            synchronization_job_id=None,
            synchronization_job_name=None,
            source_endpoint_user_name=None,
            partition_key_modify_time__month=None,
            source_endpoint_port=None,
            source_endpoint_owner_id=None,
            destination_endpoint_user_name=None,
            destination_endpoint_port=None,
            partition_key_modify_time__year=None,
            source_endpoint_role=None,
            owner_id=None,
            partition_key_modify_time__hour=None,
            source_endpoint_password=None,
            migration_reserved=None,
            destination_endpoint_ip=None,
            destination_endpoint_instance_type=None,
            synchronization_direction=None):
        api_request = APIRequest('ConfigureSynchronizationJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceEndpoint.InstanceId": source_endpoint_instance_id,
            "Checkpoint": checkpoint,
            "DestinationEndpoint.InstanceId": destination_endpoint_instance_id,
            "SourceEndpoint.IP": source_endpoint_ip,
            "SynchronizationObjects": synchronization_objects,
            "DestinationEndpoint.Password": destination_endpoint_password,
            "DataInitialization": data_initialization,
            "StructureInitialization": structure_initialization,
            "PartitionKey.ModifyTime_Minute": partition_key_modify_time__minute,
            "PartitionKey.ModifyTime_Day": partition_key_modify_time__day,
            "SourceEndpoint.InstanceType": source_endpoint_instance_type,
            "SynchronizationJobId": synchronization_job_id,
            "SynchronizationJobName": synchronization_job_name,
            "SourceEndpoint.UserName": source_endpoint_user_name,
            "PartitionKey.ModifyTime_Month": partition_key_modify_time__month,
            "SourceEndpoint.Port": source_endpoint_port,
            "SourceEndpoint.OwnerID": source_endpoint_owner_id,
            "DestinationEndpoint.UserName": destination_endpoint_user_name,
            "DestinationEndpoint.Port": destination_endpoint_port,
            "PartitionKey.ModifyTime_Year": partition_key_modify_time__year,
            "SourceEndpoint.Role": source_endpoint_role,
            "OwnerId": owner_id,
            "PartitionKey.ModifyTime_Hour": partition_key_modify_time__hour,
            "SourceEndpoint.Password": source_endpoint_password,
            "MigrationReserved": migration_reserved,
            "DestinationEndpoint.IP": destination_endpoint_ip,
            "DestinationEndpoint.InstanceType": destination_endpoint_instance_type,
            "SynchronizationDirection": synchronization_direction}
        return self._handle_request(api_request).result

    def delete_synchronization_job(self, synchronization_job_id=None, owner_id=None):
        api_request = APIRequest('DeleteSynchronizationJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SynchronizationJobId": synchronization_job_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_synchronization_jobs(
            self,
            synchronization_job_name=None,
            client_token=None,
            page_size=None,
            page_num=None,
            owner_id=None):
        api_request = APIRequest('DescribeSynchronizationJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SynchronizationJobName": synchronization_job_name,
            "ClientToken": client_token,
            "PageSize": page_size,
            "PageNum": page_num,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def suspend_synchronization_job(
            self,
            synchronization_job_id=None,
            owner_id=None,
            synchronization_direction=None):
        api_request = APIRequest('SuspendSynchronizationJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SynchronizationJobId": synchronization_job_id,
            "OwnerId": owner_id,
            "SynchronizationDirection": synchronization_direction}
        return self._handle_request(api_request).result

    def modify_synchronization_object(
            self,
            synchronization_job_id=None,
            synchronization_objects=None,
            owner_id=None,
            synchronization_direction=None):
        api_request = APIRequest('ModifySynchronizationObject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SynchronizationJobId": synchronization_job_id,
            "SynchronizationObjects": synchronization_objects,
            "OwnerId": owner_id,
            "SynchronizationDirection": synchronization_direction}
        return self._handle_request(api_request).result

    def describe_synchronization_job_status(
            self,
            synchronization_job_id=None,
            client_token=None,
            owner_id=None,
            synchronization_direction=None):
        api_request = APIRequest('DescribeSynchronizationJobStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SynchronizationJobId": synchronization_job_id,
            "ClientToken": client_token,
            "OwnerId": owner_id,
            "SynchronizationDirection": synchronization_direction}
        return self._handle_request(api_request).result

    def describe_synchronization_object_modify_status(
            self, client_token=None, owner_id=None, task_id=None):
        api_request = APIRequest(
            'DescribeSynchronizationObjectModifyStatus',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {"ClientToken": client_token, "OwnerId": owner_id, "TaskId": task_id}
        return self._handle_request(api_request).result

    def create_synchronization_job(
            self,
            period=None,
            dest_region=None,
            client_token=None,
            topology=None,
            synchronization_job_class=None,
            network_type=None,
            owner_id=None,
            source_region=None,
            pay_type=None,
            used_time=None,
            source_endpoint_instance_type=None,
            destination_endpoint_instance_type=None):
        api_request = APIRequest('CreateSynchronizationJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "DestRegion": dest_region,
            "ClientToken": client_token,
            "Topology": topology,
            "SynchronizationJobClass": synchronization_job_class,
            "networkType": network_type,
            "OwnerId": owner_id,
            "SourceRegion": source_region,
            "PayType": pay_type,
            "UsedTime": used_time,
            "SourceEndpoint.InstanceType": source_endpoint_instance_type,
            "DestinationEndpoint.InstanceType": destination_endpoint_instance_type}
        return self._handle_request(api_request).result
