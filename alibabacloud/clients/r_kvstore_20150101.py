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


class RkvstoreClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'R-kvstore'
        self.api_version = '2015-01-01'
        self.location_service_code = 'redisa'
        self.location_endpoint_type = 'openAPI'

    def create_sharding_instance(
            self,
            shard_storage_quantity=None,
            resource_owner_id=None,
            node_type=None,
            coupon_no=None,
            network_type=None,
            engine_version=None,
            instance_class=None,
            capacity=None,
            password=None,
            shard_replica_class=None,
            security_token=None,
            incremental_backup_mode=None,
            instance_type=None,
            business_info=None,
            period=None,
            resource_owner_account=None,
            src_db_instance_id=None,
            owner_account=None,
            backup_id=None,
            owner_id=None,
            token=None,
            shard_quantity=None,
            vswitch_id=None,
            private_ip_address=None,
            security_ip_list=None,
            instance_name=None,
            shard_replica_quantity=None,
            architecture_type=None,
            vpc_id=None,
            redis_manager_class=None,
            zone_id=None,
            charge_type=None,
            proxy_quantity=None,
            config=None,
            proxy_mode=None):
        api_request = APIRequest('CreateShardingInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ShardStorageQuantity": shard_storage_quantity,
            "ResourceOwnerId": resource_owner_id,
            "NodeType": node_type,
            "CouponNo": coupon_no,
            "NetworkType": network_type,
            "EngineVersion": engine_version,
            "InstanceClass": instance_class,
            "Capacity": capacity,
            "Password": password,
            "ShardReplicaClass": shard_replica_class,
            "SecurityToken": security_token,
            "IncrementalBackupMode": incremental_backup_mode,
            "InstanceType": instance_type,
            "BusinessInfo": business_info,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "SrcDBInstanceId": src_db_instance_id,
            "OwnerAccount": owner_account,
            "BackupId": backup_id,
            "OwnerId": owner_id,
            "Token": token,
            "ShardQuantity": shard_quantity,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "SecurityIPList": security_ip_list,
            "InstanceName": instance_name,
            "ShardReplicaQuantity": shard_replica_quantity,
            "ArchitectureType": architecture_type,
            "VpcId": vpc_id,
            "RedisManagerClass": redis_manager_class,
            "ZoneId": zone_id,
            "ChargeType": charge_type,
            "ProxyQuantity": proxy_quantity,
            "Config": config,
            "ProxyMode": proxy_mode}
        return self._handle_request(api_request).result

    def describe_sharding_instances(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            instance_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeShardingInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "InstanceIds": instance_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_tags(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            next_token=None,
            owner_account=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('DescribeTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NextToken": next_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        return self._handle_request(api_request).result

    def describe_available_resource(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            zone_id=None,
            owner_id=None,
            instance_charge_type=None,
            order_type=None):
        api_request = APIRequest('DescribeAvailableResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ZoneId": zone_id,
            "OwnerId": owner_id,
            "InstanceChargeType": instance_charge_type,
            "OrderType": order_type}
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

    def release_instance_public_connection(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            current_connection_string=None):
        api_request = APIRequest('ReleaseInstancePublicConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "CurrentConnectionString": current_connection_string}
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

    def migrate_to_other_zone(
            self,
            vswitch_id=None,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            effective_time=None,
            owner_account=None,
            zone_id=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('MigrateToOtherZone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "EffectiveTime": effective_time,
            "OwnerAccount": owner_account,
            "ZoneId": zone_id,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
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

    def modify_audit_log_config(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            audit_command=None,
            owner_account=None,
            owner_id=None,
            retention=None):
        api_request = APIRequest('ModifyAuditLogConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "AuditCommand": audit_command,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Retention": retention}
        return self._handle_request(api_request).result

    def modify_db_instance_monitor(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            interval=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBInstanceMonitor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "Interval": interval,
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

    def describe_cache_analysis_report_list(
            self,
            date=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            instance_id=None,
            security_token=None,
            page_size=None,
            page_numbers=None,
            days=None,
            node_id=None):
        api_request = APIRequest('DescribeCacheAnalysisReportList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Date": date,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "PageNumbers": page_numbers,
            "Days": days,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def describe_intranet_attribute(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeIntranetAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_intranet_attribute(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyIntranetAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cache_analysis_report(
            self,
            date=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            analysis_type=None,
            instance_id=None,
            security_token=None,
            page_size=None,
            page_numbers=None,
            node_id=None):
        api_request = APIRequest('DescribeCacheAnalysisReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Date": date,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AnalysisType": analysis_type,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "PageNumbers": page_numbers,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def create_cache_analysis_task(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CreateCacheAnalysisTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
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
            host_address=None,
            instance_id=None,
            account_name=None,
            security_token=None,
            database_name=None,
            page_size=None,
            node_id=None):
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
            "HostAddress": host_address,
            "InstanceId": instance_id,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "DatabaseName": database_name,
            "PageSize": page_size,
            "NodeId": node_id}
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
            slow_log_record_type=None,
            instance_id=None,
            db_name=None,
            security_token=None,
            page_size=None,
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
            "SlowLogRecordType": slow_log_record_type,
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token,
            "PageSize": page_size,
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
            instance_id=None,
            db_name=None,
            security_token=None,
            page_size=None,
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
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "RoleType": role_type,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def restart_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            effective_time=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('RestartInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "EffectiveTime": effective_time,
            "OwnerAccount": owner_account,
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
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            db_instance_id=None,
            owner_id=None,
            page_number=None,
            proxy_id=None):
        api_request = APIRequest('DescribeInstanceAutoRenewalAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "proxyId": proxy_id}
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
            instance_id=None,
            db_name=None,
            security_token=None,
            page_size=None,
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
            "InstanceId": instance_id,
            "DBName": db_name,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "RoleType": role_type,
            "NodeId": node_id}
        return self._handle_request(api_request).result

    def unlink_replica_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('UnlinkReplicaInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
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

    def modify_instance_major_version(
            self,
            resource_owner_id=None,
            instance_id=None,
            major_version=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            effect_time=None):
        api_request = APIRequest('ModifyInstanceMajorVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "MajorVersion": major_version,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "EffectTime": effect_time}
        return self._handle_request(api_request).result

    def describe_parameter_templates(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            engine=None,
            owner_account=None,
            engine_version=None,
            owner_id=None,
            character_type=None):
        api_request = APIRequest('DescribeParameterTemplates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "Engine": engine,
            "OwnerAccount": owner_account,
            "EngineVersion": engine_version,
            "OwnerId": owner_id,
            "CharacterType": character_type}
        return self._handle_request(api_request).result

    def revoke_account_privilege(
            self,
            resource_owner_id=None,
            instance_id=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('RevokeAccountPrivilege', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
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

    def modify_account_description(
            self,
            resource_owner_id=None,
            instance_id=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            account_description=None):
        api_request = APIRequest('ModifyAccountDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AccountDescription": account_description}
        return self._handle_request(api_request).result

    def reset_account(
            self,
            resource_owner_id=None,
            account_password=None,
            instance_id=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ResetAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountPassword": account_password,
            "InstanceId": instance_id,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_account(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            account_type=None,
            owner_id=None,
            account_description=None,
            account_privilege=None,
            account_password=None,
            instance_id=None,
            account_name=None,
            security_token=None):
        api_request = APIRequest('CreateAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AccountType": account_type,
            "OwnerId": owner_id,
            "AccountDescription": account_description,
            "AccountPrivilege": account_privilege,
            "AccountPassword": account_password,
            "InstanceId": instance_id,
            "AccountName": account_name,
            "SecurityToken": security_token}
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

    def reset_account_password(
            self,
            resource_owner_id=None,
            account_password=None,
            instance_id=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ResetAccountPassword', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountPassword": account_password,
            "InstanceId": instance_id,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_accounts(
            self,
            resource_owner_id=None,
            instance_id=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeAccounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def grant_account_privilege(
            self,
            resource_owner_id=None,
            instance_id=None,
            account_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            account_privilege=None):
        api_request = APIRequest('GrantAccountPrivilege', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "AccountName": account_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AccountPrivilege": account_privilege}
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

    def destroy_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DestroyInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_instance_vpc_auth_mode(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            vpc_auth_mode=None,
            owner_id=None):
        api_request = APIRequest('ModifyInstanceVpcAuthMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "VpcAuthMode": vpc_auth_mode,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_instance_connection_string(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            new_connection_string=None,
            owner_id=None,
            ip_type=None,
            current_connection_string=None,
            security_token=None,
            port=None,
            db_instance_id=None):
        api_request = APIRequest('ModifyDBInstanceConnectionString', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "NewConnectionString": new_connection_string,
            "OwnerId": owner_id,
            "IPType": ip_type,
            "CurrentConnectionString": current_connection_string,
            "SecurityToken": security_token,
            "Port": port,
            "DBInstanceId": db_instance_id}
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

    def describe_instances_by_expire_time(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            page_number=None,
            security_token=None,
            has_expired_res=None,
            page_size=None,
            instance_type=None,
            expire_period=None):
        api_request = APIRequest('DescribeInstancesByExpireTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "SecurityToken": security_token,
            "HasExpiredRes": has_expired_res,
            "PageSize": page_size,
            "InstanceType": instance_type,
            "ExpirePeriod": expire_period}
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

    def modify_instance_ssl(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            ssl_enabled=None):
        api_request = APIRequest('ModifyInstanceSSL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "SSLEnabled": ssl_enabled}
        return self._handle_request(api_request).result

    def describe_instance_ssl(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceSSL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_logic_instance_topology(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeLogicInstanceTopology', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_instance_spec(
            self,
            resource_owner_id=None,
            auto_pay=None,
            from_app=None,
            resource_owner_account=None,
            owner_account=None,
            coupon_no=None,
            owner_id=None,
            instance_class=None,
            instance_id=None,
            security_token=None,
            effective_time=None,
            force_upgrade=None,
            business_info=None):
        api_request = APIRequest('ModifyInstanceSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "FromApp": from_app,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "CouponNo": coupon_no,
            "OwnerId": owner_id,
            "InstanceClass": instance_class,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "EffectiveTime": effective_time,
            "ForceUpgrade": force_upgrade,
            "BusinessInfo": business_info}
        return self._handle_request(api_request).result

    def modify_instance_spec_pre_check(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            target_instance_class=None):
        api_request = APIRequest('ModifyInstanceSpecPreCheck', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TargetInstanceClass": target_instance_class}
        return self._handle_request(api_request).result

    def modify_instance_net_expire_time(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            connection_string=None,
            classic_expired_days=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyInstanceNetExpireTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "ConnectionString": connection_string,
            "ClassicExpiredDays": classic_expired_days,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
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

    def modify_instance_minor_version(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            minorversion=None,
            owner_account=None,
            owner_id=None,
            effect_time=None):
        api_request = APIRequest('ModifyInstanceMinorVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "Minorversion": minorversion,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "EffectTime": effect_time}
        return self._handle_request(api_request).result

    def modify_certification(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            no_certification=None):
        api_request = APIRequest('ModifyCertification', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NoCertification": no_certification}
        return self._handle_request(api_request).result

    def describe_certification(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            parameters=None):
        api_request = APIRequest('DescribeCertification', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Parameters": parameters}
        return self._handle_request(api_request).result

    def describe_db_instance_net_info(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceNetInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_monthly_service_status_detail(
            self,
            resource_owner_id=None,
            instance_id=None,
            month=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeMonthlyServiceStatusDetail',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "Month": month,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_monthly_service_status(
            self,
            resource_owner_id=None,
            month=None,
            security_token=None,
            resource_owner_account=None,
            instance_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeMonthlyServiceStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Month": month,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "InstanceIds": instance_ids,
            "OwnerAccount": owner_account,
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
            instance_id=None,
            security_token=None,
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
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "SecurityIpGroupAttribute": security_ip_group_attribute}
        return self._handle_request(api_request).result

    def describe_security_ips(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeSecurityIps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_instance_maintain_time(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            maintain_start_time=None,
            owner_account=None,
            owner_id=None,
            maintain_end_time=None):
        api_request = APIRequest('ModifyInstanceMaintainTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "MaintainStartTime": maintain_start_time,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "MaintainEndTime": maintain_end_time}
        return self._handle_request(api_request).result

    def describe_instance_attribute(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def restore_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            backup_id=None,
            owner_id=None):
        api_request = APIRequest('RestoreInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "BackupId": backup_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_backup_policy(
            self,
            preferred_backup_time=None,
            preferred_backup_period=None,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PreferredBackupTime": preferred_backup_time,
            "PreferredBackupPeriod": preferred_backup_period,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
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
            instance_id=None,
            security_token=None,
            page_size=None):
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
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "PageSize": page_size}
        return self._handle_request(api_request).result

    def describe_backup_policy(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_backup(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CreateBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def switch_network(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            vswitch_id=None,
            instance_id=None,
            security_token=None,
            target_network_type=None,
            retain_classic=None,
            classic_expired_days=None,
            vpc_id=None):
        api_request = APIRequest('SwitchNetwork', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "VSwitchId": vswitch_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "TargetNetworkType": target_network_type,
            "RetainClassic": retain_classic,
            "ClassicExpiredDays": classic_expired_days,
            "VpcId": vpc_id}
        return self._handle_request(api_request).result

    def describe_zones(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            accept_language=None,
            owner_id=None):
        api_request = APIRequest('DescribeZones', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AcceptLanguage": accept_language,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_snapshot(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteSnapshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_temp_instance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CreateTempInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_snapshot(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CreateSnapshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_temp_instance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteTempInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_snapshot_settings(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteSnapshotSettings', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_snapshot_settings(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('GetSnapshotSettings', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_temp_instance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeTempInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_snapshots(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            begin_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeSnapshots', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "BeginTime": begin_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def restore_snapshot(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('RestoreSnapshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_task(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def switch_temp_instance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('SwitchTempInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_snapshot_settings(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('SetSnapshotSettings', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def renew_multi_instance(
            self,
            resource_owner_id=None,
            period=None,
            auto_pay=None,
            from_app=None,
            resource_owner_account=None,
            owner_account=None,
            coupon_no=None,
            owner_id=None,
            security_token=None,
            instance_ids=None,
            business_info=None):
        api_request = APIRequest('RenewMultiInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "AutoPay": auto_pay,
            "FromApp": from_app,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "CouponNo": coupon_no,
            "OwnerId": owner_id,
            "SecurityToken": security_token,
            "InstanceIds": instance_ids,
            "BusinessInfo": business_info}
        return self._handle_request(api_request).result

    def transform_to_pre_paid(
            self,
            resource_owner_id=None,
            period=None,
            instance_id=None,
            auto_pay=None,
            from_app=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('TransformToPrePaid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "InstanceId": instance_id,
            "AutoPay": auto_pay,
            "FromApp": from_app,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def renew_instance(
            self,
            resource_owner_id=None,
            period=None,
            auto_pay=None,
            from_app=None,
            resource_owner_account=None,
            owner_account=None,
            coupon_no=None,
            owner_id=None,
            instance_class=None,
            capacity=None,
            instance_id=None,
            security_token=None,
            force_upgrade=None,
            business_info=None):
        api_request = APIRequest('RenewInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "AutoPay": auto_pay,
            "FromApp": from_app,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "CouponNo": coupon_no,
            "OwnerId": owner_id,
            "InstanceClass": instance_class,
            "Capacity": capacity,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ForceUpgrade": force_upgrade,
            "BusinessInfo": business_info}
        return self._handle_request(api_request).result

    def verify_password(
            self,
            resource_owner_id=None,
            password=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('VerifyPassword', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Password": password,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_instance_config(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            config=None):
        api_request = APIRequest('ModifyInstanceConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Config": config}
        return self._handle_request(api_request).result

    def modify_instance_attribute(
            self,
            resource_owner_id=None,
            instance_id=None,
            instance_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            new_password=None):
        api_request = APIRequest('ModifyInstanceAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "InstanceName": instance_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NewPassword": new_password}
        return self._handle_request(api_request).result

    def flush_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('FlushInstance', 'GET', 'http', 'RPC', 'query')
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
            accept_language=None,
            owner_id=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AcceptLanguage": accept_language,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_monitor_items(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeMonitorItems', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instances(
            self,
            resource_owner_id=None,
            instance_status=None,
            resource_owner_account=None,
            owner_account=None,
            search_key=None,
            network_type=None,
            engine_version=None,
            owner_id=None,
            instance_class=None,
            page_number=None,
            vswitch_id=None,
            expired=None,
            security_token=None,
            instance_ids=None,
            architecture_type=None,
            vpc_id=None,
            page_size=None,
            instance_type=None,
            zone_id=None,
            charge_type=None,
            list_of_tag=None):
        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceStatus": instance_status,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SearchKey": search_key,
            "NetworkType": network_type,
            "EngineVersion": engine_version,
            "OwnerId": owner_id,
            "InstanceClass": instance_class,
            "PageNumber": page_number,
            "VSwitchId": vswitch_id,
            "Expired": expired,
            "SecurityToken": security_token,
            "InstanceIds": instance_ids,
            "ArchitectureType": architecture_type,
            "VpcId": vpc_id,
            "PageSize": page_size,
            "InstanceType": instance_type,
            "ZoneId": zone_id,
            "ChargeType": charge_type,
            "Tag": list_of_tag}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_instance_config(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_history_monitor_values(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            instance_id=None,
            security_token=None,
            interval_for_history=None,
            node_id=None,
            monitor_keys=None):
        api_request = APIRequest('DescribeHistoryMonitorValues', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "IntervalForHistory": interval_for_history,
            "NodeId": node_id,
            "MonitorKeys": monitor_keys}
        return self._handle_request(api_request).result

    def delete_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_instance(
            self,
            resource_owner_id=None,
            node_type=None,
            coupon_no=None,
            network_type=None,
            engine_version=None,
            auto_use_coupon=None,
            instance_class=None,
            capacity=None,
            password=None,
            security_token=None,
            instance_type=None,
            business_info=None,
            auto_renew_period=None,
            period=None,
            resource_owner_account=None,
            src_db_instance_id=None,
            owner_account=None,
            backup_id=None,
            owner_id=None,
            token=None,
            vswitch_id=None,
            private_ip_address=None,
            instance_name=None,
            auto_renew=None,
            vpc_id=None,
            zone_id=None,
            charge_type=None,
            config=None):
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "NodeType": node_type,
            "CouponNo": coupon_no,
            "NetworkType": network_type,
            "EngineVersion": engine_version,
            "AutoUseCoupon": auto_use_coupon,
            "InstanceClass": instance_class,
            "Capacity": capacity,
            "Password": password,
            "SecurityToken": security_token,
            "InstanceType": instance_type,
            "BusinessInfo": business_info,
            "AutoRenewPeriod": auto_renew_period,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "SrcDBInstanceId": src_db_instance_id,
            "OwnerAccount": owner_account,
            "BackupId": backup_id,
            "OwnerId": owner_id,
            "Token": token,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "InstanceName": instance_name,
            "AutoRenew": auto_renew,
            "VpcId": vpc_id,
            "ZoneId": zone_id,
            "ChargeType": charge_type,
            "Config": config}
        return self._handle_request(api_request).result
