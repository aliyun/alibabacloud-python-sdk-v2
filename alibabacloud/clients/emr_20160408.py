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


class EmrClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Emr'
        self.api_version = '2016-04-08'
        self.location_service_code = 'emr'
        self.location_endpoint_type = 'openAPI'

    def describe_hp_host(self, hp_host_biz_id=None, resource_owner_id=None, region_id=None):
        api_request = APIRequest('DescribeHpHost', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HpHostBizId": hp_host_biz_id,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def refresh_backup_list(self, resource_owner_id=None, region_id=None, backup_plan_id=None):
        api_request = APIRequest('RefreshBackupList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BackupPlanId": backup_plan_id}
        return self._handle_request(api_request).result

    def remove_backup_rule(self, resource_owner_id=None, region_id=None, backup_rule_id=None):
        api_request = APIRequest('RemoveBackupRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BackupRuleId": backup_rule_id}
        return self._handle_request(api_request).result

    def describe_cluster_service_config_for_admin(
            self,
            resource_owner_id=None,
            host_instance_id=None,
            tag_value=None,
            region_id=None,
            group_id=None,
            service_name=None,
            cluster_id=None,
            user_id=None,
            config_version=None):
        api_request = APIRequest('DescribeClusterServiceConfigForAdmin',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HostInstanceId": host_instance_id,
            "TagValue": tag_value,
            "RegionId": region_id,
            "GroupId": group_id,
            "ServiceName": service_name,
            "ClusterId": cluster_id,
            "UserId": user_id,
            "ConfigVersion": config_version}
        return self._handle_request(api_request).result

    def list_supported_service_name_for_admin(
            self,
            resource_owner_id=None,
            region_id=None,
            user_id=None):
        api_request = APIRequest('ListSupportedServiceNameForAdmin', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "UserId": user_id}
        return self._handle_request(api_request).result

    def describe_cluster_resource_pool_scheduler_type_for_admin(
            self, resource_owner_id=None, region_id=None, cluster_id=None, user_id=None):
        api_request = APIRequest(
            'DescribeClusterResourcePoolSchedulerTypeForAdmin',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "UserId": user_id}
        return self._handle_request(api_request).result

    def list_cluster_service_config_history_for_admin(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            service_name=None,
            cluster_id=None,
            user_id=None,
            page_number=None,
            config_version=None):
        api_request = APIRequest(
            'ListClusterServiceConfigHistoryForAdmin',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ServiceName": service_name,
            "ClusterId": cluster_id,
            "UserId": user_id,
            "PageNumber": page_number,
            "ConfigVersion": config_version}
        return self._handle_request(api_request).result

    def list_resource_pool_for_admin(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            cluster_id=None,
            user_id=None,
            page_number=None,
            pool_type=None):
        api_request = APIRequest('ListResourcePoolForAdmin', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "UserId": user_id,
            "PageNumber": page_number,
            "PoolType": pool_type}
        return self._handle_request(api_request).result

    def describe_workspace_repo_setting(
            self,
            resource_owner_id=None,
            region_id=None,
            workspace_id=None):
        api_request = APIRequest('DescribeWorkspaceRepoSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "WorkspaceId": workspace_id}
        return self._handle_request(api_request).result

    def refresh_cluster_resource_pool_for_admin(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_pool_id=None,
            cluster_id=None,
            user_id=None):
        api_request = APIRequest('RefreshClusterResourcePoolForAdmin',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourcePoolId": resource_pool_id,
            "ClusterId": cluster_id,
            "UserId": user_id}
        return self._handle_request(api_request).result

    def describe_cluster_service_config_tag_for_admin(
            self,
            resource_owner_id=None,
            region_id=None,
            config_tag=None,
            service_name=None,
            cluster_id=None,
            user_id=None):
        api_request = APIRequest(
            'DescribeClusterServiceConfigTagForAdmin',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ConfigTag": config_tag,
            "ServiceName": service_name,
            "ClusterId": cluster_id,
            "UserId": user_id}
        return self._handle_request(api_request).result

    def resize_cluster_with_host_pool(
            self,
            resource_owner_id=None,
            region_id=None,
            list_of_host_group=None,
            list_of_host_info=None,
            cluster_id=None):
        api_request = APIRequest('ResizeClusterWithHostPool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroup": list_of_host_group,
            "HostInfo": list_of_host_info,
            "clusterId": cluster_id}
        repeat_info = {"HostGroup": ('HostGroup', 'list', 'dict', [('GroupType', 'str', None, None),
                                                                   ('GroupId', 'str', None, None),
                                                                   ('GroupName', 'str', None, None),
                                                                   ]),
                       "HostInfo": ('HostInfo', 'list', 'dict', [('HpHostBizId', 'str', None, None),
                                                                 ('HostName', 'str', None, None),
                                                                 ('Role', 'str', None, None),
                                                                 ('GroupId', 'str', None, None),
                                                                 ('PrivateIp', 'str', None, None),
                                                                 ('ServiceComponentInfo', 'list', 'dict', [('serviceEcmVersion', 'str', None, None),
                                                                                                           ('ComponentName', 'str', None, None),
                                                                                                           ('ServiceName', 'str', None, None),
                                                                                                           ],),('HostGroupName', 'str', None, None),
                                                                 ('HostGroupType', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_streaming_sql_query(self, resource_owner_id=None, instance_id=None, region_id=None):
        api_request = APIRequest('ListStreamingSqlQuery', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def create_backup_rule(
            self,
            resource_owner_id=None,
            backup_method_type=None,
            description=None,
            backup_plan_id=None,
            metadata_type=None,
            region_id=None,
            name=None):
        api_request = APIRequest('CreateBackupRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BackupMethodType": backup_method_type,
            "Description": description,
            "BackupPlanId": backup_plan_id,
            "MetadataType": metadata_type,
            "RegionId": region_id,
            "Name": name}
        return self._handle_request(api_request).result

    def update_workspace_resource_setting(
            self,
            resource_owner_id=None,
            region_id=None,
            workspace_id=None,
            oss_setting=None):
        api_request = APIRequest('UpdateWorkspaceResourceSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "WorkspaceId": workspace_id,
            "OssSetting": oss_setting}
        return self._handle_request(api_request).result

    def get_flow_audit_logs(
            self,
            resource_owner_id=None,
            page_count=None,
            order_mode=None,
            entity_id=None,
            page_number=None,
            region_id=None,
            limit=None,
            page_size=None,
            current_size=None,
            order_field=None,
            entity_group_id=None,
            entity_type=None,
            operator_id=None,
            operation=None,
            status=None):
        api_request = APIRequest('GetFlowAuditLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageCount": page_count,
            "OrderMode": order_mode,
            "EntityId": entity_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "Limit": limit,
            "PageSize": page_size,
            "CurrentSize": current_size,
            "OrderField": order_field,
            "EntityGroupId": entity_group_id,
            "EntityType": entity_type,
            "OperatorId": operator_id,
            "Operation": operation,
            "Status": status}
        return self._handle_request(api_request).result

    def get_back_plan_info(self, resource_owner_id=None, region_id=None, backup_plan_id=None):
        api_request = APIRequest('GetBackPlanInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BackupPlanId": backup_plan_id}
        return self._handle_request(api_request).result

    def create_backup_plan(
            self,
            resource_owner_id=None,
            description=None,
            cluster_id=None,
            region_id=None,
            name=None,
            root_path=None):
        api_request = APIRequest('CreateBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Description": description,
            "ClusterId": cluster_id,
            "RegionId": region_id,
            "Name": name,
            "RootPath": root_path}
        return self._handle_request(api_request).result

    def get_audit_logs(
            self,
            resource_owner_id=None,
            page_count=None,
            order_mode=None,
            entity_id=None,
            page_number=None,
            region_id=None,
            limit=None,
            page_size=None,
            current_size=None,
            order_field=None,
            operation=None):
        api_request = APIRequest('GetAuditLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageCount": page_count,
            "OrderMode": order_mode,
            "EntityId": entity_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "Limit": limit,
            "PageSize": page_size,
            "CurrentSize": current_size,
            "OrderField": order_field,
            "Operation": operation}
        return self._handle_request(api_request).result

    def update_workspace_repo_setting(
            self,
            resource_owner_id=None,
            region_id=None,
            list_of_repo_maven=None,
            list_of_repo_pip=None,
            workspace_id=None):
        api_request = APIRequest('UpdateWorkspaceRepoSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "RepoMaven": list_of_repo_maven,
            "RepoPip": list_of_repo_pip,
            "WorkspaceId": workspace_id}
        repeat_info = {"RepoMaven": ('RepoMaven', 'list', 'dict', [('GroupId', 'str', None, None),
                                                                   ('ArtifactId', 'str', None, None),
                                                                   ('Version', 'str', None, None),
                                                                   ]),
                       "RepoPip": ('RepoPip', 'list', 'dict', [('PackageName', 'str', None, None),
                                                               ('Version', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def add_cluster_service_for_admin(
            self,
            resource_owner_id=None,
            region_id=None,
            service_list=None,
            comment=None,
            cluster_id=None,
            user_id=None):
        api_request = APIRequest('AddClusterServiceForAdmin', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ServiceList": service_list,
            "Comment": comment,
            "ClusterId": cluster_id,
            "UserId": user_id}
        return self._handle_request(api_request).result

    def list_cluster_tag_for_admin(
            self,
            resource_owner_id=None,
            list_of_cluster_id_list=None,
            region_id=None,
            user_id=None):
        api_request = APIRequest('ListClusterTagForAdmin', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClusterIdList": list_of_cluster_id_list,
            "RegionId": region_id,
            "UserId": user_id}
        repeat_info = {"ClusterIdList": ('ClusterIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_metadata_type_list(self, resource_owner_id=None, region_id=None):
        api_request = APIRequest('GetMetadataTypeList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def restore_backup(
            self,
            resource_owner_id=None,
            region_id=None,
            backup_plan_id=None,
            backup_id=None):
        api_request = APIRequest('RestoreBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BackupPlanId": backup_plan_id,
            "BackupId": backup_id}
        return self._handle_request(api_request).result

    def retry_sync_user_account(
            self,
            resource_owner_id=None,
            resource_id=None,
            list_of_aliyun_user_id_list=None,
            account_type=None,
            resource_type=None,
            region_id=None):
        api_request = APIRequest('RetrySyncUserAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "AliyunUserIdList": list_of_aliyun_user_id_list,
            "AccountType": account_type,
            "ResourceType": resource_type,
            "RegionId": region_id}
        repeat_info = {"AliyunUserIdList": ('AliyunUserIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_backup(
            self,
            resource_owner_id=None,
            backup_plan_id=None,
            metadata_type=None,
            region_id=None):
        api_request = APIRequest('CreateBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BackupPlanId": backup_plan_id,
            "MetadataType": metadata_type,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def get_backup_info(self, resource_owner_id=None, region_id=None, backup_id=None):
        api_request = APIRequest('GetBackupInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BackupId": backup_id}
        return self._handle_request(api_request).result

    def describe_workspace_resource_setting(
            self,
            resource_owner_id=None,
            region_id=None,
            workspace_id=None):
        api_request = APIRequest('DescribeWorkspaceResourceSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "WorkspaceId": workspace_id}
        return self._handle_request(api_request).result

    def list_cluster_service_custom_action_support_config_for_admin(
            self,
            service_custom_action_name=None,
            resource_owner_id=None,
            region_id=None,
            service_name=None,
            cluster_id=None,
            user_id=None):
        api_request = APIRequest(
            'ListClusterServiceCustomActionSupportConfigForAdmin',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ServiceCustomActionName": service_custom_action_name,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ServiceName": service_name,
            "ClusterId": cluster_id,
            "UserId": user_id}
        return self._handle_request(api_request).result

    def remove_backup_plan(self, resource_owner_id=None, region_id=None, backup_plan_id=None):
        api_request = APIRequest('RemoveBackupPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BackupPlanId": backup_plan_id}
        return self._handle_request(api_request).result

    def get_backup_rule_info(self, resource_owner_id=None, region_id=None, backup_rule_id=None):
        api_request = APIRequest('GetBackupRuleInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BackupRuleId": backup_rule_id}
        return self._handle_request(api_request).result

    def remove_backup(
            self,
            resource_owner_id=None,
            list_of_backup_id=None,
            backup_plan_id=None,
            region_id=None):
        api_request = APIRequest('RemoveBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BackupId": list_of_backup_id,
            "BackupPlanId": backup_plan_id,
            "RegionId": region_id}
        repeat_info = {"BackupId": ('BackupId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_backup_rules(
            self,
            resource_owner_id=None,
            page_count=None,
            order_mode=None,
            backup_plan_id=None,
            page_number=None,
            region_id=None,
            limit=None,
            page_size=None,
            id_=None,
            current_size=None,
            order_field=None,
            biz_id=None,
            status=None):
        api_request = APIRequest('ListBackupRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageCount": page_count,
            "OrderMode": order_mode,
            "BackupPlanId": backup_plan_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "Limit": limit,
            "PageSize": page_size,
            "Id": id_,
            "CurrentSize": current_size,
            "OrderField": order_field,
            "BizId": biz_id,
            "Status": status}
        return self._handle_request(api_request).result

    def list_backups(
            self,
            resource_owner_id=None,
            page_count=None,
            order_mode=None,
            backup_plan_id=None,
            page_number=None,
            region_id=None,
            limit=None,
            page_size=None,
            service_name=None,
            id_=None,
            current_size=None,
            order_field=None,
            list_of_backup_id=None,
            cluster_id=None,
            metadata_type=None,
            biz_id=None,
            status=None):
        api_request = APIRequest('ListBackups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageCount": page_count,
            "OrderMode": order_mode,
            "BackupPlanId": backup_plan_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "Limit": limit,
            "PageSize": page_size,
            "ServiceName": service_name,
            "Id": id_,
            "CurrentSize": current_size,
            "OrderField": order_field,
            "BackupId": list_of_backup_id,
            "ClusterId": cluster_id,
            "MetadataType": metadata_type,
            "BizId": biz_id,
            "Status": status}
        repeat_info = {"BackupId": ('BackupId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_hp_host(
            self,
            cpu_core=None,
            mem_size=None,
            resource_owner_id=None,
            rack_info=None,
            role=None,
            serial_number=None,
            host_type=None,
            security_group_id=None,
            list_of_hp_host_disk=None,
            vswitch_id=None,
            hp_host_biz_id=None,
            external_key=None,
            host_name=None,
            region_id=None,
            vpc_id=None,
            inner_ip=None,
            external_ip=None):
        api_request = APIRequest('ModifyHpHost', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CpuCore": cpu_core,
            "MemSize": mem_size,
            "ResourceOwnerId": resource_owner_id,
            "RackInfo": rack_info,
            "Role": role,
            "SerialNumber": serial_number,
            "HostType": host_type,
            "SecurityGroupId": security_group_id,
            "HpHostDisk": list_of_hp_host_disk,
            "VswitchId": vswitch_id,
            "HpHostBizId": hp_host_biz_id,
            "ExternalKey": external_key,
            "HostName": host_name,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "InnerIp": inner_ip,
            "ExternalIp": external_ip}
        repeat_info = {"HpHostDisk": ('HpHostDisk', 'list', 'dict', [('DiskSize', 'str', None, None),
                                                                     ('MountPath', 'str', None, None),
                                                                     ('DiskDevice', 'str', None, None),
                                                                     ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def render_resource_pool_xml_for_admin(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_pool_id=None,
            cluster_id=None,
            user_id=None):
        api_request = APIRequest('RenderResourcePoolXmlForAdmin', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourcePoolId": resource_pool_id,
            "ClusterId": cluster_id,
            "UserId": user_id}
        return self._handle_request(api_request).result

    def modify_cluster_service_config_for_admin(
            self,
            refresh_host_config=None,
            resource_owner_id=None,
            config_type=None,
            host_instance_id=None,
            author=None,
            group_id=None,
            cluster_id=None,
            user_id=None,
            custom_config_params=None,
            region_id=None,
            service_name=None,
            comment=None,
            list_of_gateway_cluster_id_list=None,
            config_params=None):
        api_request = APIRequest('ModifyClusterServiceConfigForAdmin',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RefreshHostConfig": refresh_host_config,
            "ResourceOwnerId": resource_owner_id,
            "ConfigType": config_type,
            "HostInstanceId": host_instance_id,
            "Author": author,
            "GroupId": group_id,
            "ClusterId": cluster_id,
            "UserId": user_id,
            "CustomConfigParams": custom_config_params,
            "RegionId": region_id,
            "ServiceName": service_name,
            "Comment": comment,
            "GatewayClusterIdList": list_of_gateway_cluster_id_list,
            "ConfigParams": config_params}
        repeat_info = {"GatewayClusterIdList": ('GatewayClusterIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_backup_plans(
            self,
            resource_owner_id=None,
            page_count=None,
            order_mode=None,
            page_number=None,
            region_id=None,
            limit=None,
            page_size=None,
            id_=None,
            current_size=None,
            order_field=None,
            cluster_id=None,
            biz_id=None,
            status=None):
        api_request = APIRequest('ListBackupPlans', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageCount": page_count,
            "OrderMode": order_mode,
            "PageNumber": page_number,
            "RegionId": region_id,
            "Limit": limit,
            "PageSize": page_size,
            "Id": id_,
            "CurrentSize": current_size,
            "OrderField": order_field,
            "ClusterId": cluster_id,
            "BizId": biz_id,
            "Status": status}
        return self._handle_request(api_request).result

    def list_cluster_host_component_for_admin(
            self,
            resource_owner_id=None,
            host_instance_id=None,
            component_name=None,
            cluster_id=None,
            user_id=None,
            page_number=None,
            component_status=None,
            host_name=None,
            region_id=None,
            page_size=None,
            service_name=None,
            host_role=None):
        api_request = APIRequest('ListClusterHostComponentForAdmin', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HostInstanceId": host_instance_id,
            "ComponentName": component_name,
            "ClusterId": cluster_id,
            "UserId": user_id,
            "PageNumber": page_number,
            "ComponentStatus": component_status,
            "HostName": host_name,
            "RegionId": region_id,
            "PageSize": page_size,
            "ServiceName": service_name,
            "HostRole": host_role}
        return self._handle_request(api_request).result

    def query_info_by_token(self,):
        api_request = APIRequest('QueryInfoByToken', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def update_user_status(
            self,
            resource_owner_id=None,
            region_id=None,
            aliyun_user_id=None,
            update_status=None):
        api_request = APIRequest('UpdateUserStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "AliyunUserId": aliyun_user_id,
            "UpdateStatus": update_status}
        return self._handle_request(api_request).result

    def delete_batch_resource_users(
            self,
            resource_owner_id=None,
            resource_id=None,
            list_of_user_id_list=None,
            resource_type=None,
            region_id=None):
        api_request = APIRequest('DeleteBatchResourceUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "UserIdList": list_of_user_id_list,
            "ResourceType": resource_type,
            "RegionId": region_id}
        repeat_info = {"UserIdList": ('UserIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def query_user_actions_policy(
            self,
            resource_owner_id=None,
            resource_id=None,
            resource_type=None,
            region_id=None,
            list_of_action_name_list=None,
            aliyun_user_id=None):
        api_request = APIRequest('QueryUserActionsPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "ResourceType": resource_type,
            "RegionId": region_id,
            "ActionNameList": list_of_action_name_list,
            "AliyunUserId": aliyun_user_id}
        repeat_info = {"ActionNameList": ('ActionNameList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_batch_users(
            self,
            resource_owner_id=None,
            list_of_user_base_param_list=None,
            list_of_role_id=None,
            list_of_group_id=None,
            description=None,
            region_id=None):
        api_request = APIRequest('CreateBatchUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UserBaseParamList": list_of_user_base_param_list,
            "RoleId": list_of_role_id,
            "GroupId": list_of_group_id,
            "Description": description,
            "RegionId": region_id}
        repeat_info = {
            "UserBaseParamList": (
                'UserBaseParamList',
                'list',
                'dict',
                [
                    ('AliyunUserId',
                     'str',
                     None,
                     None),
                    ('UserName',
                     'str',
                     None,
                     None),
                    ('UserType',
                     'str',
                     None,
                     None),
                    ('IsSuperAdmin',
                     'str',
                     None,
                     None),
                    ]),
            "RoleId": (
                'RoleId',
                'list',
                'str',
                None),
            "GroupId": (
                    'GroupId',
                    'list',
                    'str',
                    None),
                     }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def add_user_resource_role(
            self,
            resource_owner_id=None,
            resource_id=None,
            role_id=None,
            resource_type=None,
            region_id=None,
            aliyun_user_id=None):
        api_request = APIRequest('AddUserResourceRole', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "RoleId": role_id,
            "ResourceType": resource_type,
            "RegionId": region_id,
            "AliyunUserId": aliyun_user_id}
        return self._handle_request(api_request).result

    def delete_user_resource_role(
            self,
            resource_owner_id=None,
            resource_id=None,
            role_id=None,
            resource_type=None,
            region_id=None,
            aliyun_user_id=None):
        api_request = APIRequest('DeleteUserResourceRole', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "RoleId": role_id,
            "ResourceType": resource_type,
            "RegionId": region_id,
            "AliyunUserId": aliyun_user_id}
        return self._handle_request(api_request).result

    def create_user_group(
            self,
            resource_owner_id=None,
            description=None,
            type_=None,
            region_id=None,
            name=None,
            list_of_role_id_list=None):
        api_request = APIRequest('CreateUserGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Description": description,
            "Type": type_,
            "RegionId": region_id,
            "Name": name,
            "RoleIdList": list_of_role_id_list}
        repeat_info = {"RoleIdList": ('RoleIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_user(
            self,
            resource_owner_id=None,
            user_type=None,
            description=None,
            list_of_user_account_param_list=None,
            list_of_group_id_list=None,
            region_id=None,
            list_of_role_id_list=None,
            aliyun_user_id=None,
            user_name=None,
            status=None):
        api_request = APIRequest('CreateUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UserType": user_type,
            "Description": description,
            "UserAccountParamList": list_of_user_account_param_list,
            "GroupIdList": list_of_group_id_list,
            "RegionId": region_id,
            "RoleIdList": list_of_role_id_list,
            "AliyunUserId": aliyun_user_id,
            "UserName": user_name,
            "Status": status}
        repeat_info = {"UserAccountParamList": ('UserAccountParamList', 'list', 'dict', [('AccountType', 'str', None, None),
                                                                                         ('AuthType', 'str', None, None),
                                                                                         ('AccountPassword', 'str', None, None),
                                                                                         ]),
                       "GroupIdList": ('GroupIdList', 'list', 'str', None),
                       "RoleIdList": ('RoleIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_roles(self, resource_owner_id=None, resource_type=None, region_id=None):
        api_request = APIRequest('ListRoles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceType": resource_type,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def describe_user_group(self, resource_owner_id=None, region_id=None, group_id=None):
        api_request = APIRequest('DescribeUserGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "GroupId": group_id}
        return self._handle_request(api_request).result

    def update_user_group(
            self,
            resource_owner_id=None,
            list_of_role_id=None,
            description=None,
            type_=None,
            region_id=None,
            name=None,
            id_=None):
        api_request = APIRequest('UpdateUserGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RoleId": list_of_role_id,
            "Description": description,
            "Type": type_,
            "RegionId": region_id,
            "Name": name,
            "Id": id_}
        repeat_info = {"RoleId": ('RoleId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_user(self, resource_owner_id=None, region_id=None, aliyun_user_id=None):
        api_request = APIRequest('DescribeUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "AliyunUserId": aliyun_user_id}
        return self._handle_request(api_request).result

    def add_resource_to_users(
            self,
            resource_owner_id=None,
            resource_id=None,
            list_of_user_id_list=None,
            resource_type=None,
            region_id=None,
            list_of_role_id_list=None):
        api_request = APIRequest('AddResourceToUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "UserIdList": list_of_user_id_list,
            "ResourceType": resource_type,
            "RegionId": region_id,
            "RoleIdList": list_of_role_id_list}
        repeat_info = {"UserIdList": ('UserIdList', 'list', 'str', None),
                       "RoleIdList": ('RoleIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def save_batch_user_account_info(
            self,
            resource_owner_id=None,
            resource_id=None,
            list_of_aliyun_user_id_list=None,
            account_type=None,
            group_name=None,
            resource_type=None,
            auth_type=None,
            account_password=None,
            region_id=None):
        api_request = APIRequest('SaveBatchUserAccountInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "AliyunUserIdList": list_of_aliyun_user_id_list,
            "AccountType": account_type,
            "GroupName": group_name,
            "ResourceType": resource_type,
            "AuthType": auth_type,
            "AccountPassword": account_password,
            "RegionId": region_id}
        repeat_info = {"AliyunUserIdList": ('AliyunUserIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_user_groups(self, resource_owner_id=None, fuzzy_name=None, region_id=None):
        api_request = APIRequest('ListUserGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "FuzzyName": fuzzy_name,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def update_user(
            self,
            resource_owner_id=None,
            user_type=None,
            description=None,
            list_of_user_account_param_list=None,
            list_of_group_id_list=None,
            region_id=None,
            list_of_role_id_list=None,
            aliyun_user_id=None,
            user_name=None,
            status=None):
        api_request = APIRequest('UpdateUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UserType": user_type,
            "Description": description,
            "UserAccountParamList": list_of_user_account_param_list,
            "GroupIdList": list_of_group_id_list,
            "RegionId": region_id,
            "RoleIdList": list_of_role_id_list,
            "AliyunUserId": aliyun_user_id,
            "UserName": user_name,
            "Status": status}
        repeat_info = {"UserAccountParamList": ('UserAccountParamList', 'list', 'dict', [('AccountType', 'str', None, None),
                                                                                         ('AuthType', 'str', None, None),
                                                                                         ('AccountPassword', 'str', None, None),
                                                                                         ]),
                       "GroupIdList": ('GroupIdList', 'list', 'str', None),
                       "RoleIdList": ('RoleIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def page_list_users(
            self,
            resource_owner_id=None,
            fuzzy_name=None,
            page_number=None,
            region_id=None,
            page_size=None):
        api_request = APIRequest('PageListUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "FuzzyName": fuzzy_name,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size}
        return self._handle_request(api_request).result

    def delete_resource_user(
            self,
            resource_owner_id=None,
            resource_id=None,
            resource_type=None,
            region_id=None,
            aliyun_user_id=None):
        api_request = APIRequest('DeleteResourceUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "ResourceType": resource_type,
            "RegionId": region_id,
            "AliyunUserId": aliyun_user_id}
        return self._handle_request(api_request).result

    def list_users_by_condition(self, resource_owner_id=None, search_key=None, region_id=None):
        api_request = APIRequest('ListUsersByCondition', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SearchKey": search_key,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def save_user_account_info(
            self,
            resource_owner_id=None,
            account_type=None,
            group_name=None,
            auth_type=None,
            account_password=None,
            region_id=None,
            aliyun_user_id=None):
        api_request = APIRequest('SaveUserAccountInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountType": account_type,
            "GroupName": group_name,
            "AuthType": auth_type,
            "AccountPassword": account_password,
            "RegionId": region_id,
            "AliyunUserId": aliyun_user_id}
        return self._handle_request(api_request).result

    def query_user_policies(
            self,
            resource_owner_id=None,
            resource_id=None,
            resource_type=None,
            region_id=None):
        api_request = APIRequest('QueryUserPolicies', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "ResourceType": resource_type,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def page_list_user_groups(
            self,
            resource_owner_id=None,
            fuzzy_name=None,
            page_number=None,
            region_id=None,
            page_size=None):
        api_request = APIRequest('PageListUserGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "FuzzyName": fuzzy_name,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size}
        return self._handle_request(api_request).result

    def delete_user_group(self, resource_owner_id=None, region_id=None, group_id=None):
        api_request = APIRequest('DeleteUserGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "GroupId": group_id}
        return self._handle_request(api_request).result

    def page_list_resource_users(
            self,
            resource_owner_id=None,
            resource_id=None,
            search_key=None,
            resource_type=None,
            page_number=None,
            region_id=None,
            page_size=None):
        api_request = APIRequest('PageListResourceUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "SearchKey": search_key,
            "ResourceType": resource_type,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size}
        return self._handle_request(api_request).result

    def list_host_pool(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('ListHostPool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_kafka_reassign(
            self,
            resource_owner_id=None,
            topic_id=None,
            region_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('ListKafkaReassign', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TopicId": topic_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_host_pool(self, resource_owner_id=None, region_id=None, biz_id=None):
        api_request = APIRequest('DeleteHostPool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BizId": biz_id}
        return self._handle_request(api_request).result

    def offline_kafka_broker(
            self,
            throttle=None,
            resource_owner_id=None,
            region_id=None,
            host_id=None,
            cluster_id=None):
        api_request = APIRequest('OfflineKafkaBroker', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Throttle": throttle,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostId": host_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def create_host_pool(
            self,
            resource_owner_id=None,
            region_id=None,
            name=None,
            description=None,
            list_of_kube_cluster_info=None,
            type_=None):
        api_request = APIRequest('CreateHostPool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Description": description,
            "KubeClusterInfo": list_of_kube_cluster_info,
            "Type": type_}
        repeat_info = {"KubeClusterInfo": ('KubeClusterInfo',
                                           'list',
                                           'dict',
                                           [('ExternalKey',
                                             'str',
                                             None,
                                             None),
                                            ('InternalConfig',
                                             'str',
                                             None,
                                             None),
                                               ('PublicConfig',
                                                'str',
                                                None,
                                                None),
                                               ('SshConfig',
                                                'str',
                                                None,
                                                None),
                                            ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_kafka_reassign_topic(
            self,
            resource_owner_id=None,
            region_id=None,
            reassign_id=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('ListKafkaReassignTopic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ReassignId": reassign_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def plan_component_topo(
            self,
            cluster_type=None,
            resource_owner_id=None,
            region_id=None,
            list_of_host_group=None,
            list_of_host_info=None,
            stack_name=None,
            cluster_id=None,
            stack_version=None,
            list_of_service_info=None):
        api_request = APIRequest('PlanComponentTopo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClusterType": cluster_type,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroup": list_of_host_group,
            "HostInfo": list_of_host_info,
            "StackName": stack_name,
            "ClusterId": cluster_id,
            "StackVersion": stack_version,
            "ServiceInfo": list_of_service_info}
        repeat_info = {"HostGroup": ('HostGroup', 'list', 'dict', [('GroupType', 'str', None, None),
                                                                   ('NodeCount', 'str', None, None),
                                                                   ('GroupName', 'str', None, None),
                                                                   ]),
                       "HostInfo": ('HostInfo', 'list', 'dict', [('HpHostBizId', 'str', None, None),
                                                                 ('HostGroupName', 'str', None, None),
                                                                 ]),
                       "ServiceInfo": ('ServiceInfo', 'list', 'dict', [('ServiceEcmVersion', 'str', None, None),
                                                                       ('ServiceVersion', 'str', None, None),
                                                                       ('ServiceName', 'str', None, None),
                                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_kafka_topic_statistics(
            self,
            resource_owner_id=None,
            active_only=None,
            region_id=None,
            page_size=None,
            data_source_id=None,
            topic_name=None,
            cluster_id=None,
            page_number=None,
            fuzzy_topic_name=None):
        api_request = APIRequest('ListKafkaTopicStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ActiveOnly": active_only,
            "RegionId": region_id,
            "PageSize": page_size,
            "DataSourceId": data_source_id,
            "TopicName": topic_name,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "FuzzyTopicName": fuzzy_topic_name}
        return self._handle_request(api_request).result

    def start_kafka_preferred_replica_election(
            self, resource_owner_id=None, topic_id=None, region_id=None):
        api_request = APIRequest('StartKafkaPreferredReplicaElection',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TopicId": topic_id,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def list_cluster_support_service(self, resource_owner_id=None, region_id=None, cluster_id=None):
        api_request = APIRequest('ListClusterSupportService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_kafka_reassign(self, resource_owner_id=None, region_id=None, reassign_id=None):
        api_request = APIRequest('DescribeKafkaReassign', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ReassignId": reassign_id}
        return self._handle_request(api_request).result

    def list_stack_service(
            self,
            resource_owner_id=None,
            region_id=None,
            stack_name=None,
            stack_version=None):
        api_request = APIRequest('ListStackService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "StackName": stack_name,
            "StackVersion": stack_version}
        return self._handle_request(api_request).result

    def create_cluster_with_host_pool(
            self,
            resource_owner_id=None,
            cluster_name=None,
            eas_enable=None,
            list_of_host_info=None,
            related_cluster_id=None,
            cluster_type=None,
            region_id=None,
            list_of_host_group=None,
            stack_name=None,
            stack_version=None,
            list_of_service_info=None,
            list_of_config=None):
        api_request = APIRequest('CreateClusterWithHostPool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClusterName": cluster_name,
            "EasEnable": eas_enable,
            "HostInfo": list_of_host_info,
            "RelatedClusterId": related_cluster_id,
            "ClusterType": cluster_type,
            "RegionId": region_id,
            "HostGroup": list_of_host_group,
            "StackName": stack_name,
            "StackVersion": stack_version,
            "ServiceInfo": list_of_service_info,
            "Config": list_of_config}
        repeat_info = {"HostInfo": ('HostInfo', 'list', 'dict', [('HpHostBizId', 'str', None, None),
                                                                 ('HostName', 'str', None, None),
                                                                 ('Role', 'str', None, None),
                                                                 ('GroupId', 'str', None, None),
                                                                 ('PrivateIp', 'str', None, None),
                                                                 ('ServiceComponentInfo', 'list', 'dict', [('ServiceEcmVersion', 'str', None, None),
                                                                                                           ('ComponentName', 'str', None, None),
                                                                                                           ('ServiceName', 'str', None, None),
                                                                                                           ],),('HostGroupName', 'str', None, None),
                                                                 ]),
                       "HostGroup": ('HostGroup', 'list', 'dict', [('GroupType', 'str', None, None),
                                                                   ('GroupId', 'str', None, None),
                                                                   ('GroupName', 'str', None, None),
                                                                   ]),
                       "ServiceInfo": ('ServiceInfo', 'list', 'dict', [('ServiceEcmVersion', 'str', None, None),
                                                                       ('ServiceVersion', 'str', None, None),
                                                                       ('ServiceName', 'str', None, None),
                                                                       ]),
                       "Config": ('Config', 'list', 'dict', [('ConfigKey', 'str', None, None),
                                                             ('FileName', 'str', None, None),
                                                             ('ConfigValue', 'str', None, None),
                                                             ('ServiceName', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def start_kafka_broker_disk_balancer(
            self,
            throttle=None,
            resource_owner_id=None,
            broker_id=None,
            region_id=None,
            cluster_id=None,
            balance_threshold=None):
        api_request = APIRequest('StartKafkaBrokerDiskBalancer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Throttle": throttle,
            "ResourceOwnerId": resource_owner_id,
            "BrokerId": broker_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "BalanceThreshold": balance_threshold}
        return self._handle_request(api_request).result

    def list_hp_host(
            self,
            resource_owner_id=None,
            role=None,
            region_id=None,
            page_size=None,
            hp_biz_id=None,
            page_number=None,
            status=None):
        api_request = APIRequest('ListHpHost', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Role": role,
            "RegionId": region_id,
            "PageSize": page_size,
            "HpBizId": hp_biz_id,
            "PageNumber": page_number,
            "Status": status}
        return self._handle_request(api_request).result

    def remove_hp_host(self, hp_host_biz_id=None, resource_owner_id=None, region_id=None):
        api_request = APIRequest('RemoveHpHost', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HpHostBizId": hp_host_biz_id,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def list_cluster_installed_service(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('ListClusterInstalledService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def reassign_kafka(
            self,
            throttle=None,
            resource_owner_id=None,
            topic_id=None,
            list_of_broker_id=None,
            region_id=None):
        api_request = APIRequest('ReassignKafka', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Throttle": throttle,
            "ResourceOwnerId": resource_owner_id,
            "TopicId": topic_id,
            "BrokerId": list_of_broker_id,
            "RegionId": region_id}
        repeat_info = {"BrokerId": ('BrokerId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def update_kafka_reassign_param(
            self,
            throttle=None,
            resource_owner_id=None,
            region_id=None,
            reassign_id=None):
        api_request = APIRequest('UpdateKafkaReassignParam', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Throttle": throttle,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ReassignId": reassign_id}
        return self._handle_request(api_request).result

    def add_hp_host(
            self,
            resource_owner_id=None,
            list_of_hp_host=None,
            region_id=None,
            hp_biz_id=None):
        api_request = APIRequest('AddHpHost', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HpHost": list_of_hp_host,
            "RegionId": region_id,
            "HpBizId": hp_biz_id}
        repeat_info = {"HpHost": ('HpHost', 'list', 'dict', [('CpuCore', 'str', None, None),
                                                             ('MemSize', 'str', None, None),
                                                             ('RackInfo', 'str', None, None),
                                                             ('Role', 'str', None, None),
                                                             ('SerialNumber', 'str', None, None),
                                                             ('HostType', 'str', None, None),
                                                             ('SecurityGroupId', 'str', None, None),
                                                             ('HpHostDisk', 'list', 'dict', [('DiskSize', 'str', None, None),
                                                                                             ('MountPath', 'str', None, None),
                                                                                             ('DiskDevice', 'str', None, None),
                                                                                             ],),('VswitchId', 'str', None, None),
                                                             ('ExternalKey', 'str', None, None),
                                                             ('HostName', 'str', None, None),
                                                             ('VpcId', 'str', None, None),
                                                             ('InnerIp', 'str', None, None),
                                                             ('ExternalIp', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_host_pool(
            self,
            resource_owner_id=None,
            region_id=None,
            name=None,
            biz_id=None,
            description=None):
        api_request = APIRequest('ModifyHostPool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "BizId": biz_id,
            "Description": description}
        return self._handle_request(api_request).result

    def describe_kafka_broker(
            self,
            resource_owner_id=None,
            region_id=None,
            host_id=None,
            cluster_id=None):
        api_request = APIRequest('DescribeKafkaBroker', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostId": host_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_kafka_broker(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('ListKafkaBroker', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_stack(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            stack_name=None,
            stack_version=None,
            page_number=None):
        api_request = APIRequest('ListStack', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "StackName": stack_name,
            "StackVersion": stack_version,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def plan_host_name(
            self,
            resource_owner_id=None,
            region_id=None,
            list_of_host_group=None,
            list_of_host_info=None,
            cluster_id=None):
        api_request = APIRequest('PlanHostName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroup": list_of_host_group,
            "HostInfo": list_of_host_info,
            "ClusterId": cluster_id}
        repeat_info = {
            "HostGroup": (
                'HostGroup', 'list', 'dict', [
                    ('GroupType', 'str', None, None), ('GroupName', 'str', None, None), ]), "HostInfo": (
                'HostInfo', 'list', 'dict', [
                    ('HpHostBizId', 'str', None, None), ('HostGroupName', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_host_pool(
            self,
            resource_owner_id=None,
            region_id=None,
            biz_id=None,
            cluster_id=None):
        api_request = APIRequest('DescribeHostPool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BizId": biz_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_etl_job_release(
            self,
            resource_owner_id=None,
            region_id=None,
            etl_job_id=None,
            release_id=None,
            page_size=None,
            page_number=None,
            release_version=None,
            status=None):
        api_request = APIRequest('ListETLJobRelease', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "EtlJobId": etl_job_id,
            "ReleaseId": release_id,
            "PageSize": page_size,
            "PageNumber": page_number,
            "ReleaseVersion": release_version,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_data_source_schema_database(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            data_source_id=None):
        api_request = APIRequest('DescribeDataSourceSchemaDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "DataSourceId": data_source_id}
        return self._handle_request(api_request).result

    def update_project_setting(
            self,
            resource_owner_id=None,
            region_id=None,
            default_oss_path=None,
            project_id=None,
            oss_config=None):
        api_request = APIRequest('UpdateProjectSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "DefaultOssPath": default_oss_path,
            "ProjectId": project_id,
            "OssConfig": oss_config}
        return self._handle_request(api_request).result

    def describe_etl_job(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DescribeETLJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def describe_etl_job_instance(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DescribeETLJobInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def delete_etl_job(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DeleteETLJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def update_etl_job_stage(
            self,
            stage_name=None,
            stage_conf=None,
            resource_owner_id=None,
            stage_type=None,
            region_id=None,
            etl_job_id=None,
            stage_plugin=None):
        api_request = APIRequest('UpdateETLJobStage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StageName": stage_name,
            "StageConf": stage_conf,
            "ResourceOwnerId": resource_owner_id,
            "StageType": stage_type,
            "RegionId": region_id,
            "EtlJobId": etl_job_id,
            "StagePlugin": stage_plugin}
        return self._handle_request(api_request).result

    def create_nav_node(
            self,
            resource_owner_id=None,
            region_id=None,
            name=None,
            type_=None,
            project_id=None,
            category_type=None,
            object_id=None,
            parent_id=None):
        api_request = APIRequest('CreateNavNode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Type": type_,
            "ProjectId": project_id,
            "CategoryType": category_type,
            "ObjectId": object_id,
            "ParentId": parent_id}
        return self._handle_request(api_request).result

    def update_data_source(
            self,
            resource_owner_id=None,
            region_id=None,
            name=None,
            description=None,
            conf=None,
            id_=None):
        api_request = APIRequest('UpdateDataSource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Description": description,
            "Conf": conf,
            "Id": id_}
        return self._handle_request(api_request).result

    def delete_nav_node(self, resource_owner_id=None, region_id=None, id_=None, project_id=None):
        api_request = APIRequest('DeleteNavNode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def update_nav_node(
            self,
            resource_owner_id=None,
            region_id=None,
            name=None,
            id_=None,
            project_id=None,
            parent_id=None):
        api_request = APIRequest('UpdateNavNode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Id": id_,
            "ProjectId": project_id,
            "ParentId": parent_id}
        return self._handle_request(api_request).result

    def resolve_etl_job_sql_schema(
            self,
            stage_name=None,
            resource_owner_id=None,
            region_id=None,
            etl_job_id=None,
            data_source_id=None,
            sql=None):
        api_request = APIRequest('ResolveETLJobSqlSchema', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StageName": stage_name,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "EtlJobId": etl_job_id,
            "DataSourceId": data_source_id,
            "Sql": sql}
        return self._handle_request(api_request).result

    def check_data_source(
            self,
            resource_owner_id=None,
            region_id=None,
            conf=None,
            id_=None,
            cluster_id=None):
        api_request = APIRequest('CheckDataSource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Conf": conf,
            "Id": id_,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def clone_etl_job(self, resource_owner_id=None, region_id=None, name=None, id_=None):
        api_request = APIRequest('CloneETLJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Id": id_}
        return self._handle_request(api_request).result

    def list_etl_job_trigger_entity(self, resource_owner_id=None, entity_type=None, region_id=None):
        api_request = APIRequest('ListETLJobTriggerEntity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "EntityType": entity_type,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def kill_etl_job_instance(self, resource_owner_id=None, instance_id=None, region_id=None):
        api_request = APIRequest('KillETLJobInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def describe_etl_job_stage_output_schema(
            self,
            stage_name=None,
            resource_owner_id=None,
            region_id=None,
            etl_job_id=None):
        api_request = APIRequest('DescribeETLJobStageOutputSchema', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StageName": stage_name,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "EtlJobId": etl_job_id}
        return self._handle_request(api_request).result

    def describe_etl_job_sql_schema(self, resource_owner_id=None, region_id=None, resolve_id=None):
        api_request = APIRequest('DescribeETLJobSqlSchema', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResolveId": resolve_id}
        return self._handle_request(api_request).result

    def describe_data_source_command(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DescribeDataSourceCommand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def list_data_source_schema_database(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            data_source_id=None):
        api_request = APIRequest('ListDataSourceSchemaDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "DataSourceId": data_source_id}
        return self._handle_request(api_request).result

    def get_job_migrate_result(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('GetJobMigrateResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def list_data_source_schema_table(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            data_source_id=None,
            table_name=None):
        api_request = APIRequest('ListDataSourceSchemaTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "DataSourceId": data_source_id,
            "TableName": table_name}
        return self._handle_request(api_request).result

    def describe_flow_variable_collection(self, region_id=None, entity_id=None):
        api_request = APIRequest('DescribeFlowVariableCollection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "EntityId": entity_id}
        return self._handle_request(api_request).result

    def release_etl_job(self, resource_owner_id=None, region_id=None, release_id=None, id_=None):
        api_request = APIRequest('ReleaseETLJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ReleaseId": release_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def describe_data_source(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DescribeDataSource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def describe_data_source_schema_table(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            data_source_id=None,
            table_name=None):
        api_request = APIRequest('DescribeDataSourceSchemaTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "DataSourceId": data_source_id,
            "TableName": table_name}
        return self._handle_request(api_request).result

    def cancel_etl_job_release(
            self,
            resource_owner_id=None,
            region_id=None,
            etl_job_id=None,
            release_id=None):
        api_request = APIRequest('CancelETLJobRelease', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "EtlJobId": etl_job_id,
            "ReleaseId": release_id}
        return self._handle_request(api_request).result

    def delete_data_source(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DeleteDataSource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def list_cluster_tag(
            self,
            resource_owner_id=None,
            list_of_cluster_id_list=None,
            region_id=None):
        api_request = APIRequest('ListClusterTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClusterIdList": list_of_cluster_id_list,
            "RegionId": region_id}
        repeat_info = {"ClusterIdList": ('ClusterIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def update_etl_job(
            self,
            resource_owner_id=None,
            cluster_config=None,
            list_of_trigger_rule=None,
            alert_config=None,
            description=None,
            check=None,
            list_of_stage_connection=None,
            list_of_stage=None,
            region_id=None,
            name=None,
            id_=None):
        api_request = APIRequest('UpdateETLJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClusterConfig": cluster_config,
            "TriggerRule": list_of_trigger_rule,
            "AlertConfig": alert_config,
            "Description": description,
            "Check": check,
            "StageConnection": list_of_stage_connection,
            "Stage": list_of_stage,
            "RegionId": region_id,
            "Name": name,
            "Id": id_}
        repeat_info = {"TriggerRule": ('TriggerRule', 'list', 'dict', [('CronExpr', 'str', None, None),
                                                                       ('EndTime', 'str', None, None),
                                                                       ('StartTime', 'str', None, None),
                                                                       ('Enabled', 'str', None, None),
                                                                       ]),
                       "StageConnection": ('StageConnection', 'list', 'dict', [('Port', 'str', None, None),
                                                                               ('From', 'str', None, None),
                                                                               ('To', 'str', None, None),
                                                                               ]),
                       "Stage": ('Stage', 'list', 'dict', [('StageName', 'str', None, None),
                                                           ('StageConf', 'str', None, None),
                                                           ('StageType', 'str', None, None),
                                                           ('StagePlugin', 'str', None, None),
                                                           ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def sync_data_source_schema_table(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            etl_job_id=None,
            data_source_id=None,
            table_name=None):
        api_request = APIRequest('SyncDataSourceSchemaTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "EtlJobId": etl_job_id,
            "DataSourceId": data_source_id,
            "TableName": table_name}
        return self._handle_request(api_request).result

    def list_apm_application(
            self,
            resource_owner_id=None,
            diagnose_result=None,
            end_time_from=None,
            order_by=None,
            cluster_id=None,
            job_type=None,
            page_number=None,
            final_status=None,
            region_id=None,
            start_time_from=None,
            app_id=None,
            name=None,
            page_size=None,
            state=None,
            start_time_to=None,
            user=None,
            end_time_to=None,
            queue=None):
        api_request = APIRequest('ListApmApplication', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DiagnoseResult": diagnose_result,
            "EndTimeFrom": end_time_from,
            "OrderBy": order_by,
            "ClusterId": cluster_id,
            "JobType": job_type,
            "PageNumber": page_number,
            "FinalStatus": final_status,
            "RegionId": region_id,
            "StartTimeFrom": start_time_from,
            "AppId": app_id,
            "Name": name,
            "PageSize": page_size,
            "State": state,
            "StartTimeTo": start_time_to,
            "User": user,
            "EndTimeTo": end_time_to,
            "Queue": queue}
        return self._handle_request(api_request).result

    def sync_data_source_schema_database(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            etl_job_id=None,
            data_source_id=None):
        api_request = APIRequest('SyncDataSourceSchemaDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "EtlJobId": etl_job_id,
            "DataSourceId": data_source_id}
        return self._handle_request(api_request).result

    def list_etl_job_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            region_id=None,
            etl_job_id=None,
            page_size=None,
            page_number=None,
            status=None):
        api_request = APIRequest('ListETLJobInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "RegionId": region_id,
            "EtlJobId": etl_job_id,
            "PageSize": page_size,
            "PageNumber": page_number,
            "Status": status}
        return self._handle_request(api_request).result

    def modify_flow_variable_collection(self, data=None, region_id=None):
        api_request = APIRequest('ModifyFlowVariableCollection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Data": data, "RegionId": region_id}
        return self._handle_request(api_request).result

    def run_etl_job(
            self,
            resource_owner_id=None,
            list_of_instance_run_param=None,
            region_id=None,
            is_debug=None,
            id_=None):
        api_request = APIRequest('RunETLJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceRunParam": list_of_instance_run_param,
            "RegionId": region_id,
            "IsDebug": is_debug,
            "Id": id_}
        repeat_info = {
            "InstanceRunParam": (
                'InstanceRunParam', 'list', 'dict', [
                    ('Value', 'str', None, None), ('Key', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_data_source(
            self,
            resource_owner_id=None,
            create_from=None,
            region_id=None,
            page_size=None,
            name=None,
            source_type=None,
            id_=None,
            project_id=None,
            page_number=None):
        api_request = APIRequest('ListDataSource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "CreateFrom": create_from,
            "RegionId": region_id,
            "PageSize": page_size,
            "Name": name,
            "SourceType": source_type,
            "Id": id_,
            "ProjectId": project_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def migrate_jobs(self, resource_owner_id=None, project_name=None, region_id=None):
        api_request = APIRequest('MigrateJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ProjectName": project_name,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def clone_data_source(self, resource_owner_id=None, region_id=None, name=None, id_=None):
        api_request = APIRequest('CloneDataSource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Id": id_}
        return self._handle_request(api_request).result

    def list_nav_sub_tree(
            self,
            resource_owner_id=None,
            depth=None,
            region_id=None,
            name=None,
            page_size=None,
            type_=None,
            project_id=None,
            parent_id=None,
            page_number=None):
        api_request = APIRequest('ListNavSubTree', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Depth": depth,
            "RegionId": region_id,
            "Name": name,
            "PageSize": page_size,
            "Type": type_,
            "ProjectId": project_id,
            "ParentId": parent_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def create_etl_job(
            self,
            resource_owner_id=None,
            region_id=None,
            nav_parent_id=None,
            name=None,
            description=None,
            cluster_id=None,
            type_=None,
            project_id=None):
        api_request = APIRequest('CreateETLJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "NavParentId": nav_parent_id,
            "Name": name,
            "Description": description,
            "ClusterId": cluster_id,
            "Type": type_,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def create_data_source(
            self,
            resource_owner_id=None,
            region_id=None,
            nav_parent_id=None,
            name=None,
            description=None,
            source_type=None,
            conf=None,
            cluster_id=None):
        api_request = APIRequest('CreateDataSource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "NavParentId": nav_parent_id,
            "Name": name,
            "Description": description,
            "SourceType": source_type,
            "Conf": conf,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def delete_cluster_host_group(
            self,
            resource_owner_id=None,
            region_id=None,
            host_group_id=None,
            cluster_id=None):
        api_request = APIRequest('DeleteClusterHostGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def create_cluster_host_group(
            self,
            resource_owner_id=None,
            region_id=None,
            comment=None,
            cluster_id=None,
            host_group_name=None,
            host_group_type=None):
        api_request = APIRequest('CreateClusterHostGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Comment": comment,
            "ClusterId": cluster_id,
            "HostGroupName": host_group_name,
            "HostGroupType": host_group_type}
        return self._handle_request(api_request).result

    def render_resource_pool_xml(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_pool_id=None,
            cluster_id=None):
        api_request = APIRequest('RenderResourcePoolXml', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourcePoolId": resource_pool_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def modify_cluster_host_group(
            self,
            vswitch_id=None,
            resource_owner_id=None,
            region_id=None,
            host_group_id=None,
            security_group_id=None,
            comment=None,
            cluster_id=None,
            host_group_name=None):
        api_request = APIRequest('ModifyClusterHostGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VswitchId": vswitch_id,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "SecurityGroupId": security_group_id,
            "Comment": comment,
            "ClusterId": cluster_id,
            "HostGroupName": host_group_name}
        return self._handle_request(api_request).result

    def list_resource_queue(
            self,
            resource_owner_id=None,
            region_id=None,
            pool_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None,
            pool_type=None):
        api_request = APIRequest('ListResourceQueue', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PoolId": pool_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "PoolType": pool_type}
        return self._handle_request(api_request).result

    def common_api_white_list(self, resource_owner_id=None, region_id=None):
        api_request = APIRequest('CommonApiWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def list_cluster_service_custom_action_support_config(
            self,
            service_custom_action_name=None,
            resource_owner_id=None,
            region_id=None,
            service_name=None,
            cluster_id=None):
        api_request = APIRequest(
            'ListClusterServiceCustomActionSupportConfig',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ServiceCustomActionName": service_custom_action_name,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ServiceName": service_name,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def migrate_cluster_host_group_host(
            self,
            list_of_host_instance_id_list=None,
            resource_owner_id=None,
            region_id=None,
            host_group_id=None,
            cluster_id=None):
        api_request = APIRequest('MigrateClusterHostGroupHost', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HostInstanceIdList": list_of_host_instance_id_list,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "ClusterId": cluster_id}
        repeat_info = {"HostInstanceIdList": ('HostInstanceIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_supported_service_name(self, resource_owner_id=None, region_id=None):
        api_request = APIRequest('ListSupportedServiceName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def metastore_update_kafka_topic_batch(
            self,
            resource_owner_id=None,
            list_of_topic_param=None,
            region_id=None):
        api_request = APIRequest('MetastoreUpdateKafkaTopicBatch', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TopicParam": list_of_topic_param,
            "RegionId": region_id}
        repeat_info = {
            "TopicParam": (
                'TopicParam', 'list', 'dict', [
                    ('TopicId', 'str', None, None), ('NumPartitions', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def metastore_describe_kafka_topic(self, resource_owner_id=None, topic_id=None, region_id=None):
        api_request = APIRequest('MetastoreDescribeKafkaTopic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TopicId": topic_id,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def metastore_list_kafka_topic(
            self,
            resource_owner_id=None,
            active_only=None,
            region_id=None,
            page_size=None,
            data_source_id=None,
            topic_name=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('MetastoreListKafkaTopic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ActiveOnly": active_only,
            "RegionId": region_id,
            "PageSize": page_size,
            "DataSourceId": data_source_id,
            "TopicName": topic_name,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def metastore_update_kafka_topic(
            self,
            resource_owner_id=None,
            topic_id=None,
            region_id=None,
            list_of_advanced_config=None,
            num_partitions=None):
        api_request = APIRequest('MetastoreUpdateKafkaTopic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TopicId": topic_id,
            "RegionId": region_id,
            "AdvancedConfig": list_of_advanced_config,
            "NumPartitions": num_partitions}
        repeat_info = {
            "AdvancedConfig": (
                'AdvancedConfig', 'list', 'dict', [
                    ('Value', 'str', None, None), ('Key', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def metastore_list_kafka_consumer_group(
            self,
            resource_owner_id=None,
            topic_id=None,
            region_id=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('MetastoreListKafkaConsumerGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TopicId": topic_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def metastore_describe_kafka_consumer_group(
            self,
            resource_owner_id=None,
            topic_id=None,
            region_id=None,
            consumer_group_id=None):
        api_request = APIRequest('MetastoreDescribeKafkaConsumerGroup',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TopicId": topic_id,
            "RegionId": region_id,
            "ConsumerGroupId": consumer_group_id}
        return self._handle_request(api_request).result

    def metastore_create_kafka_topic(
            self,
            resource_owner_id=None,
            region_id=None,
            data_source_id=None,
            topic_name=None,
            list_of_advanced_config=None,
            num_partitions=None,
            replication_factor=None):
        api_request = APIRequest('MetastoreCreateKafkaTopic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "DataSourceId": data_source_id,
            "TopicName": topic_name,
            "AdvancedConfig": list_of_advanced_config,
            "NumPartitions": num_partitions,
            "ReplicationFactor": replication_factor}
        repeat_info = {
            "AdvancedConfig": (
                'AdvancedConfig', 'list', 'dict', [
                    ('Value', 'str', None, None), ('Key', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def attach_pub_ip(
            self,
            resource_owner_id=None,
            region_id=None,
            list_of_instance_ids=None,
            cluster_id=None):
        api_request = APIRequest('AttachPubIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "InstanceIds": list_of_instance_ids,
            "ClusterId": cluster_id}
        repeat_info = {"InstanceIds": ('InstanceIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def metastore_list_table_partition(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            table_id=None,
            database_id=None,
            page_number=None):
        api_request = APIRequest('MetastoreListTablePartition', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "TableId": table_id,
            "DatabaseId": database_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def context_query_log(
            self,
            pack_id=None,
            resource_owner_id=None,
            total_offset=None,
            size=None,
            region_id=None,
            pack_meta=None,
            from_=None,
            cluster_id=None,
            to=None,
            reverse=None,
            log_store=None):
        api_request = APIRequest('ContextQueryLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PackId": pack_id,
            "ResourceOwnerId": resource_owner_id,
            "TotalOffset": total_offset,
            "Size": size,
            "RegionId": region_id,
            "PackMeta": pack_meta,
            "From": from_,
            "ClusterId": cluster_id,
            "To": to,
            "Reverse": reverse,
            "LogStore": log_store}
        return self._handle_request(api_request).result

    def start_flow(self, flow_instance_id=None, region_id=None, project_id=None):
        api_request = APIRequest('StartFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FlowInstanceId": flow_instance_id,
            "RegionId": region_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def metastore_delete_kafka_topic(self, resource_owner_id=None, topic_id=None, region_id=None):
        api_request = APIRequest('MetastoreDeleteKafkaTopic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TopicId": topic_id,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def get_log_histogram(
            self,
            resource_owner_id=None,
            host_inner_ip=None,
            host_name=None,
            logstore_name=None,
            from_timestamp=None,
            region_id=None,
            to_timestamp=None,
            sls_query_string=None,
            cluster_id=None):
        api_request = APIRequest('GetLogHistogram', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HostInnerIp": host_inner_ip,
            "HostName": host_name,
            "LogstoreName": logstore_name,
            "FromTimestamp": from_timestamp,
            "RegionId": region_id,
            "ToTimestamp": to_timestamp,
            "SlsQueryString": sls_query_string,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def remove_cluster_hosts(
            self,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None,
            list_of_host_id_list=None):
        api_request = APIRequest('RemoveClusterHosts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "HostIdList": list_of_host_id_list}
        repeat_info = {"HostIdList": ('HostIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_flow_node_instance(
            self,
            list_of_status_list=None,
            region_id=None,
            page_size=None,
            order_by=None,
            start_time=None,
            project_id=None,
            page_number=None,
            order_type=None):
        api_request = APIRequest('ListFlowNodeInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StatusList": list_of_status_list,
            "RegionId": region_id,
            "PageSize": page_size,
            "OrderBy": order_by,
            "StartTime": start_time,
            "ProjectId": project_id,
            "PageNumber": page_number,
            "OrderType": order_type}
        repeat_info = {"StatusList": ('StatusList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_flow_job_statistic(self, from_app=None, region_id=None, project_id=None):
        api_request = APIRequest('DescribeFlowJobStatistic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"FromApp": from_app, "RegionId": region_id, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def describe_cluster_statistics(self, resource_owner_id=None, region_id=None, strategy=None):
        api_request = APIRequest('DescribeClusterStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Strategy": strategy}
        return self._handle_request(api_request).result

    def metastore_update_table(
            self,
            resource_owner_id=None,
            region_id=None,
            list_of_add_column=None,
            list_of_add_partition=None,
            list_of_delete_column_name=None,
            table_id=None,
            list_of_delete_partition_name=None):
        api_request = APIRequest('MetastoreUpdateTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "AddColumn": list_of_add_column,
            "AddPartition": list_of_add_partition,
            "DeleteColumnName": list_of_delete_column_name,
            "TableId": table_id,
            "DeletePartitionName": list_of_delete_partition_name}
        repeat_info = {"AddColumn": ('AddColumn', 'list', 'dict', [('Name', 'str', None, None),
                                                                   ('Comment', 'str', None, None),
                                                                   ('Type', 'str', None, None),
                                                                   ]),
                       "AddPartition": ('AddPartition', 'list', 'dict', [('Name', 'str', None, None),
                                                                         ('Comment', 'str', None, None),
                                                                         ('Type', 'str', None, None),
                                                                         ]),
                       "DeleteColumnName": ('DeleteColumnName', 'list', 'str', None),
                       "DeletePartitionName": ('DeletePartitionName', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def metastore_describe_task(self, resource_owner_id=None, region_id=None, task_id=None):
        api_request = APIRequest('MetastoreDescribeTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def metastore_retry_task(self, resource_owner_id=None, region_id=None, task_id=None):
        api_request = APIRequest('MetastoreRetryTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def metastore_list_task(
            self,
            resource_owner_id=None,
            task_status=None,
            task_source_type=None,
            task_type=None,
            region_id=None,
            page_size=None,
            data_source_id=None,
            page_number=None,
            task_id=None):
        api_request = APIRequest('MetastoreListTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TaskStatus": task_status,
            "TaskSourceType": task_source_type,
            "TaskType": task_type,
            "RegionId": region_id,
            "PageSize": page_size,
            "DataSourceId": data_source_id,
            "PageNumber": page_number,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def metastore_describe_data_source(
            self,
            resource_owner_id=None,
            region_id=None,
            data_source_id=None):
        api_request = APIRequest('MetastoreDescribeDataSource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "DataSourceId": data_source_id}
        return self._handle_request(api_request).result

    def metastore_list_data_source(
            self,
            resource_owner_id=None,
            region_id=None,
            cluster_released=None,
            page_size=None,
            source_type=None,
            data_source_name=None,
            page_number=None):
        api_request = APIRequest('MetastoreListDataSource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterReleased": cluster_released,
            "PageSize": page_size,
            "SourceType": source_type,
            "DataSourceName": data_source_name,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def query_sls_metric_data(
            self,
            resource_owner_id=None,
            period=None,
            region_id=None,
            cluster_id=None,
            start_time_stamp=None,
            metric_name=None,
            host_role=None,
            end_time_stamp=None):
        api_request = APIRequest('QuerySlsMetricData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "StartTimeStamp": start_time_stamp,
            "MetricName": metric_name,
            "HostRole": host_role,
            "EndTimeStamp": end_time_stamp}
        return self._handle_request(api_request).result

    def list_job_migrate_info(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            user_id=None,
            current_size=None):
        api_request = APIRequest('ListJobMigrateInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "UserId": user_id,
            "CurrentSize": current_size}
        return self._handle_request(api_request).result

    def list_execute_plan_migrate_info(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            user_id=None,
            current_size=None):
        api_request = APIRequest('ListExecutePlanMigrateInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "UserId": user_id,
            "CurrentSize": current_size}
        return self._handle_request(api_request).result

    def describe_security_group_attribute(
            self,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None):
        api_request = APIRequest('DescribeSecurityGroupAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def authorize_security_group(
            self,
            biz_type=None,
            resource_owner_id=None,
            biz_content=None,
            region_id=None,
            cluster_id=None):
        api_request = APIRequest('AuthorizeSecurityGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BizType": biz_type,
            "ResourceOwnerId": resource_owner_id,
            "BizContent": biz_content,
            "RegionId": region_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def modify_user_statistics(
            self,
            job_migrated_num=None,
            resource_owner_id=None,
            execute_plan_num=None,
            region_id=None,
            job_num=None,
            execute_plan_migrated_num=None,
            interaction_job_migrated_num=None,
            user_id=None,
            interaction_job_num=None):
        api_request = APIRequest('ModifyUserStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobMigratedNum": job_migrated_num,
            "ResourceOwnerId": resource_owner_id,
            "ExecutePlanNum": execute_plan_num,
            "RegionId": region_id,
            "JobNum": job_num,
            "ExecutePlanMigratedNum": execute_plan_migrated_num,
            "InteractionJobMigratedNum": interaction_job_migrated_num,
            "UserId": user_id,
            "InteractionJobNum": interaction_job_num}
        return self._handle_request(api_request).result

    def modify_alert_user_group(
            self,
            user_list=None,
            resource_owner_id=None,
            region_id=None,
            biz_id=None,
            name=None,
            description=None):
        api_request = APIRequest('ModifyAlertUserGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserList": user_list,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BizId": biz_id,
            "Name": name,
            "Description": description}
        return self._handle_request(api_request).result

    def modify_alert_ding_ding_group(
            self,
            resource_owner_id=None,
            region_id=None,
            biz_id=None,
            name=None,
            description=None,
            web_hook_url=None):
        api_request = APIRequest('ModifyAlertDingDingGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BizId": biz_id,
            "Name": name,
            "Description": description,
            "WebHookUrl": web_hook_url}
        return self._handle_request(api_request).result

    def modify_alert_contact(
            self,
            email_verification_code=None,
            resource_owner_id=None,
            region_id=None,
            phone_number_verification_code=None,
            biz_id=None,
            name=None,
            phone_number=None,
            email=None):
        api_request = APIRequest('ModifyAlertContact', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EmailVerificationCode": email_verification_code,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PhoneNumberVerificationCode": phone_number_verification_code,
            "BizId": biz_id,
            "Name": name,
            "PhoneNumber": phone_number,
            "Email": email}
        return self._handle_request(api_request).result

    def list_user_statistics(
            self,
            resource_owner_id=None,
            region_id=None,
            order_mode=None,
            page_size=None,
            order_field_name=None,
            current_size=None):
        api_request = APIRequest('ListUserStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "OrderMode": order_mode,
            "PageSize": page_size,
            "OrderFieldName": order_field_name,
            "CurrentSize": current_size}
        return self._handle_request(api_request).result

    def list_alert_user_group(
            self,
            resource_owner_id=None,
            from_app=None,
            region_id=None,
            ids=None,
            user_id=None):
        api_request = APIRequest('ListAlertUserGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "FromApp": from_app,
            "RegionId": region_id,
            "Ids": ids,
            "UserId": user_id}
        return self._handle_request(api_request).result

    def list_alert_ding_ding_group(
            self,
            resource_owner_id=None,
            from_app=None,
            region_id=None,
            ids=None,
            user_id=None):
        api_request = APIRequest('ListAlertDingDingGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "FromApp": from_app,
            "RegionId": region_id,
            "Ids": ids,
            "UserId": user_id}
        return self._handle_request(api_request).result

    def list_alert_contacts(
            self,
            resource_owner_id=None,
            from_app=None,
            region_id=None,
            ids=None,
            user_id=None):
        api_request = APIRequest('ListAlertContacts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "FromApp": from_app,
            "RegionId": region_id,
            "Ids": ids,
            "UserId": user_id}
        return self._handle_request(api_request).result

    def describe_user_statistics(self, resource_owner_id=None, region_id=None, user_id=None):
        api_request = APIRequest('DescribeUserStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "UserId": user_id}
        return self._handle_request(api_request).result

    def delete_alert_user_groups(self, resource_owner_id=None, region_id=None, ids=None):
        api_request = APIRequest('DeleteAlertUserGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Ids": ids}
        return self._handle_request(api_request).result

    def delete_alert_ding_ding_groups(self, resource_owner_id=None, region_id=None, ids=None):
        api_request = APIRequest('DeleteAlertDingDingGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Ids": ids}
        return self._handle_request(api_request).result

    def delete_alert_contacts(self, resource_owner_id=None, region_id=None, ids=None):
        api_request = APIRequest('DeleteAlertContacts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Ids": ids}
        return self._handle_request(api_request).result

    def create_verification_code(
            self,
            mode=None,
            resource_owner_id=None,
            region_id=None,
            target=None):
        api_request = APIRequest('CreateVerificationCode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Mode": mode,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Target": target}
        return self._handle_request(api_request).result

    def create_user_statistics(self, resource_owner_id=None, region_id=None):
        api_request = APIRequest('CreateUserStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def create_alert_user_group(
            self,
            user_list=None,
            resource_owner_id=None,
            region_id=None,
            name=None,
            description=None):
        api_request = APIRequest('CreateAlertUserGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserList": user_list,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Description": description}
        return self._handle_request(api_request).result

    def create_alert_ding_ding_group(
            self,
            resource_owner_id=None,
            region_id=None,
            name=None,
            description=None,
            web_hook_url=None):
        api_request = APIRequest('CreateAlertDingDingGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Description": description,
            "WebHookUrl": web_hook_url}
        return self._handle_request(api_request).result

    def create_alert_contact(
            self,
            email_verification_code=None,
            resource_owner_id=None,
            region_id=None,
            phone_number_verification_code=None,
            name=None,
            phone_number=None,
            email=None):
        api_request = APIRequest('CreateAlertContact', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EmailVerificationCode": email_verification_code,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PhoneNumberVerificationCode": phone_number_verification_code,
            "Name": name,
            "PhoneNumber": phone_number,
            "Email": email}
        return self._handle_request(api_request).result

    def clone_flow_job(self, region_id=None, id_=None, project_id=None):
        api_request = APIRequest('CloneFlowJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Id": id_, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def clone_flow(self, region_id=None, id_=None, project_id=None):
        api_request = APIRequest('CloneFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Id": id_, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def modify_scaling_task_group(
            self,
            resource_owner_id=None,
            region_id=None,
            host_group_id=None,
            active_rule_category=None,
            cluster_id=None,
            min_size=None,
            max_size=None,
            default_cooldown=None):
        api_request = APIRequest('ModifyScalingTaskGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "ActiveRuleCategory": active_rule_category,
            "ClusterId": cluster_id,
            "MinSize": min_size,
            "MaxSize": max_size,
            "DefaultCooldown": default_cooldown}
        return self._handle_request(api_request).result

    def modify_scaling_rule(
            self,
            launch_time=None,
            resource_owner_id=None,
            adjustment_value=None,
            adjustment_type=None,
            rule_name=None,
            cluster_id=None,
            scaling_rule_id=None,
            launch_expiration_time=None,
            recurrence_value=None,
            recurrence_end_time=None,
            list_of_cloud_watch_trigger=None,
            region_id=None,
            host_group_id=None,
            list_of_scheduler_trigger=None,
            cooldown=None,
            recurrence_type=None):
        api_request = APIRequest('ModifyScalingRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LaunchTime": launch_time,
            "ResourceOwnerId": resource_owner_id,
            "AdjustmentValue": adjustment_value,
            "AdjustmentType": adjustment_type,
            "RuleName": rule_name,
            "ClusterId": cluster_id,
            "ScalingRuleId": scaling_rule_id,
            "LaunchExpirationTime": launch_expiration_time,
            "RecurrenceValue": recurrence_value,
            "RecurrenceEndTime": recurrence_end_time,
            "CloudWatchTrigger": list_of_cloud_watch_trigger,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "SchedulerTrigger": list_of_scheduler_trigger,
            "Cooldown": cooldown,
            "RecurrenceType": recurrence_type}
        repeat_info = {"CloudWatchTrigger": ('CloudWatchTrigger',
                                             'list',
                                             'dict',
                                             [('Period',
                                               'str',
                                               None,
                                               None),
                                              ('EvaluationCount',
                                               'str',
                                               None,
                                               None),
                                                 ('Threshold',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('MetricName',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('ComparisonOperator',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('Statistics',
                                                  'str',
                                                  None,
                                                  None),
                                              ]),
                       "SchedulerTrigger": ('SchedulerTrigger',
                                            'list',
                                            'dict',
                                            [('LaunchTime',
                                              'str',
                                              None,
                                              None),
                                             ('LaunchExpirationTime',
                                                'str',
                                                None,
                                                None),
                                                ('RecurrenceValue',
                                                 'str',
                                                 None,
                                                 None),
                                                ('RecurrenceEndTime',
                                                 'str',
                                                 None,
                                                 None),
                                                ('RecurrenceType',
                                                 'str',
                                                 None,
                                                 None),
                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_scaling_task_group(self, resource_owner_id=None, region_id=None, cluster_id=None):
        api_request = APIRequest('ListScalingTaskGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_scaling_rule(
            self,
            resource_owner_id=None,
            region_id=None,
            host_group_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('ListScalingRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_scaling_activity(
            self,
            resource_owner_id=None,
            region_id=None,
            host_group_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('ListScalingActivity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_flow(
            self,
            job_id=None,
            region_id=None,
            periodic=None,
            name=None,
            page_size=None,
            id_=None,
            cluster_id=None,
            project_id=None,
            page_number=None,
            status=None):
        api_request = APIRequest('ListFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "RegionId": region_id,
            "Periodic": periodic,
            "Name": name,
            "PageSize": page_size,
            "Id": id_,
            "ClusterId": cluster_id,
            "ProjectId": project_id,
            "PageNumber": page_number,
            "Status": status}
        return self._handle_request(api_request).result

    def list_cluster_service_component_health_info(
            self,
            resource_owner_id=None,
            region_id=None,
            service_name=None,
            cluster_id=None):
        api_request = APIRequest('ListClusterServiceComponentHealthInfo',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ServiceName": service_name,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_scaling_task_group(
            self,
            resource_owner_id=None,
            region_id=None,
            host_group_id=None,
            cluster_id=None):
        api_request = APIRequest('DescribeScalingTaskGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_scaling_rule(
            self,
            resource_owner_id=None,
            region_id=None,
            host_group_id=None,
            cluster_id=None,
            scaling_rule_id=None):
        api_request = APIRequest('DescribeScalingRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "ClusterId": cluster_id,
            "ScalingRuleId": scaling_rule_id}
        return self._handle_request(api_request).result

    def describe_scaling_activity(
            self,
            resource_owner_id=None,
            region_id=None,
            host_group_id=None,
            cluster_id=None,
            scaling_activity_id=None):
        api_request = APIRequest('DescribeScalingActivity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "ClusterId": cluster_id,
            "ScalingActivityId": scaling_activity_id}
        return self._handle_request(api_request).result

    def delete_scaling_task_group(
            self,
            resource_owner_id=None,
            region_id=None,
            host_group_id=None,
            cluster_id=None):
        api_request = APIRequest('DeleteScalingTaskGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def delete_scaling_rule(
            self,
            resource_owner_id=None,
            region_id=None,
            host_group_id=None,
            cluster_id=None,
            scaling_rule_id=None):
        api_request = APIRequest('DeleteScalingRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "ClusterId": cluster_id,
            "ScalingRuleId": scaling_rule_id}
        return self._handle_request(api_request).result

    def create_scaling_task_group(
            self,
            resource_owner_id=None,
            data_disk_category=None,
            cluster_id=None,
            min_size=None,
            spot_strategy=None,
            data_disk_size=None,
            list_of_spot_price_limits=None,
            region_id=None,
            list_of_scaling_rule=None,
            active_rule_category=None,
            max_size=None,
            data_disk_count=None,
            default_cooldown=None,
            pay_type=None,
            list_of_instance_type_list=None):
        api_request = APIRequest('CreateScalingTaskGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DataDiskCategory": data_disk_category,
            "ClusterId": cluster_id,
            "MinSize": min_size,
            "SpotStrategy": spot_strategy,
            "DataDiskSize": data_disk_size,
            "SpotPriceLimits": list_of_spot_price_limits,
            "RegionId": region_id,
            "ScalingRule": list_of_scaling_rule,
            "ActiveRuleCategory": active_rule_category,
            "MaxSize": max_size,
            "DataDiskCount": data_disk_count,
            "DefaultCooldown": default_cooldown,
            "PayType": pay_type,
            "InstanceTypeList": list_of_instance_type_list}
        repeat_info = {"SpotPriceLimits": ('SpotPriceLimits', 'list', 'dict', [('InstanceType', 'str', None, None),
                                                                               ('PriceLimit', 'str', None, None),
                                                                               ]),
                       "ScalingRule": ('ScalingRule', 'list', 'dict', [('LaunchTime', 'str', None, None),
                                                                       ('RuleCategory', 'str', None, None),
                                                                       ('AdjustmentValue', 'str', None, None),
                                                                       ('SchedulerTrigger', 'list', 'dict', [('LaunchTime', 'str', None, None),
                                                                                                             ('LaunchExpirationTime', 'str', None, None),
                                                                                                             ('RecurrenceValue', 'str', None, None),
                                                                                                             ('RecurrenceEndTime', 'str', None, None),
                                                                                                             ('RecurrenceType', 'str', None, None),
                                                                                                             ],),('AdjustmentType', 'str', None, None),
                                                                       ('Cooldown', 'str', None, None),
                                                                       ('RuleName', 'str', None, None),
                                                                       ('LaunchExpirationTime', 'str', None, None),
                                                                       ('RecurrenceValue', 'str', None, None),
                                                                       ('RecurrenceEndTime', 'str', None, None),
                                                                       ('CloudWatchTrigger', 'list', 'dict', [('Period', 'str', None, None),
                                                                                                              ('EvaluationCount', 'str', None, None),
                                                                                                              ('Threshold', 'str', None, None),
                                                                                                              ('MetricName', 'str', None, None),
                                                                                                              ('ComparisonOperator', 'str', None, None),
                                                                                                              ('Statistics', 'str', None, None),
                                                                                                              ],),('RecurrenceType', 'str', None, None),
                                                                       ]),
                       "InstanceTypeList": ('InstanceTypeList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_scaling_rule(
            self,
            launch_time=None,
            resource_owner_id=None,
            rule_category=None,
            adjustment_value=None,
            adjustment_type=None,
            rule_name=None,
            cluster_id=None,
            launch_expiration_time=None,
            recurrence_value=None,
            recurrence_end_time=None,
            list_of_cloud_watch_trigger=None,
            region_id=None,
            host_group_id=None,
            list_of_scheduler_trigger=None,
            cooldown=None,
            recurrence_type=None):
        api_request = APIRequest('CreateScalingRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LaunchTime": launch_time,
            "ResourceOwnerId": resource_owner_id,
            "RuleCategory": rule_category,
            "AdjustmentValue": adjustment_value,
            "AdjustmentType": adjustment_type,
            "RuleName": rule_name,
            "ClusterId": cluster_id,
            "LaunchExpirationTime": launch_expiration_time,
            "RecurrenceValue": recurrence_value,
            "RecurrenceEndTime": recurrence_end_time,
            "CloudWatchTrigger": list_of_cloud_watch_trigger,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "SchedulerTrigger": list_of_scheduler_trigger,
            "Cooldown": cooldown,
            "RecurrenceType": recurrence_type}
        repeat_info = {"CloudWatchTrigger": ('CloudWatchTrigger',
                                             'list',
                                             'dict',
                                             [('Period',
                                               'str',
                                               None,
                                               None),
                                              ('EvaluationCount',
                                               'str',
                                               None,
                                               None),
                                                 ('Threshold',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('MetricName',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('ComparisonOperator',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('Statistics',
                                                  'str',
                                                  None,
                                                  None),
                                              ]),
                       "SchedulerTrigger": ('SchedulerTrigger',
                                            'list',
                                            'dict',
                                            [('LaunchTime',
                                              'str',
                                              None,
                                              None),
                                             ('LaunchExpirationTime',
                                                'str',
                                                None,
                                                None),
                                                ('RecurrenceValue',
                                                 'str',
                                                 None,
                                                 None),
                                                ('RecurrenceEndTime',
                                                 'str',
                                                 None,
                                                 None),
                                                ('RecurrenceType',
                                                 'str',
                                                 None,
                                                 None),
                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_flow_cluster_all_hosts(self, region_id=None, cluster_id=None, project_id=None):
        api_request = APIRequest('ListFlowClusterAllHosts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def list_emr_main_version(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            emr_version=None,
            stack_name=None,
            stack_version=None,
            page_number=None):
        api_request = APIRequest('ListEmrMainVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "EmrVersion": emr_version,
            "StackName": stack_name,
            "StackVersion": stack_version,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_emr_main_version(self, resource_owner_id=None, region_id=None, emr_version=None):
        api_request = APIRequest('DescribeEmrMainVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "EmrVersion": emr_version}
        return self._handle_request(api_request).result

    def delete_flow_project_by_id(self, region_id=None, project_id=None):
        api_request = APIRequest('DeleteFlowProjectById', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def operate_exists_node_cluster(
            self,
            resource_owner_id=None,
            log_path=None,
            list_of_master_instance_id_list=None,
            io_optimized=None,
            security_group_id=None,
            eas_enable=None,
            is_resize=None,
            deposit_type=None,
            machine_type=None,
            region_id=None,
            use_local_meta_db=None,
            emr_ver=None,
            period=None,
            cluster_id=None,
            vswitch_id=None,
            cluster_type=None,
            list_of_option_soft_ware_list=None,
            list_of_instance_id_list=None,
            vpc_id=None,
            net_type=None,
            name=None,
            zone_id=None,
            charge_type=None,
            operate_type=None,
            high_availability_enable=None):
        api_request = APIRequest('OperateExistsNodeCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "LogPath": log_path,
            "MasterInstanceIdList": list_of_master_instance_id_list,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "EasEnable": eas_enable,
            "IsResize": is_resize,
            "DepositType": deposit_type,
            "MachineType": machine_type,
            "RegionId": region_id,
            "UseLocalMetaDb": use_local_meta_db,
            "EmrVer": emr_ver,
            "Period": period,
            "ClusterId": cluster_id,
            "VSwitchId": vswitch_id,
            "ClusterType": cluster_type,
            "OptionSoftWareList": list_of_option_soft_ware_list,
            "InstanceIdList": list_of_instance_id_list,
            "VpcId": vpc_id,
            "NetType": net_type,
            "Name": name,
            "ZoneId": zone_id,
            "ChargeType": charge_type,
            "OperateType": operate_type,
            "HighAvailabilityEnable": high_availability_enable}
        repeat_info = {"MasterInstanceIdList": ('MasterInstanceIdList', 'list', 'str', None),
                       "OptionSoftWareList": ('OptionSoftWareList', 'list', 'str', None),
                       "InstanceIdList": ('InstanceIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def metastore_modify_data_resource(
            self,
            resource_owner_id=None,
            default=None,
            region_id=None,
            name=None,
            description=None,
            id_=None,
            cluster_id=None):
        api_request = APIRequest('MetastoreModifyDataResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Default": default,
            "RegionId": region_id,
            "Name": name,
            "Description": description,
            "Id": id_,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def metastore_list_data_resources(self, resource_owner_id=None, region_id=None):
        api_request = APIRequest('MetastoreListDataResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def metastore_delete_data_resource(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('MetastoreDeleteDataResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def metastore_create_data_resource(
            self,
            resource_owner_id=None,
            default=None,
            access_type=None,
            region_id=None,
            name=None,
            description=None,
            meta_type=None,
            cluster_id=None):
        api_request = APIRequest('MetastoreCreateDataResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Default": default,
            "AccessType": access_type,
            "RegionId": region_id,
            "Name": name,
            "Description": description,
            "MetaType": meta_type,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_users(self, resource_owner_id=None, region_id=None, cluster_id=None, type_=None):
        api_request = APIRequest('ListUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "Type": type_}
        return self._handle_request(api_request).result

    def list_flow_node_sql_result(
            self,
            offset=None,
            region_id=None,
            length=None,
            sql_index=None,
            node_instance_id=None,
            project_id=None):
        api_request = APIRequest('ListFlowNodeSqlResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Offset": offset,
            "RegionId": region_id,
            "Length": length,
            "SqlIndex": sql_index,
            "NodeInstanceId": node_instance_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def list_flow_job(
            self,
            region_id=None,
            name=None,
            page_size=None,
            id_=None,
            type_=None,
            adhoc=None,
            project_id=None,
            page_number=None):
        api_request = APIRequest('ListFlowJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "Name": name,
            "PageSize": page_size,
            "Id": id_,
            "Type": type_,
            "Adhoc": adhoc,
            "ProjectId": project_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_flow_cluster_all(self, region_id=None):
        api_request = APIRequest('ListFlowClusterAll', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id}
        return self._handle_request(api_request).result

    def list_emr_available_resource(
            self,
            resource_owner_id=None,
            cluster_id=None,
            deposit_type=None,
            destination_resource=None,
            cluster_type=None,
            spot_strategy=None,
            system_disk_type=None,
            region_id=None,
            net_type=None,
            zone_id=None,
            instance_type=None,
            data_disk_type=None,
            instance_charge_type=None):
        api_request = APIRequest('ListEmrAvailableResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClusterId": cluster_id,
            "DepositType": deposit_type,
            "DestinationResource": destination_resource,
            "ClusterType": cluster_type,
            "SpotStrategy": spot_strategy,
            "SystemDiskType": system_disk_type,
            "RegionId": region_id,
            "NetType": net_type,
            "ZoneId": zone_id,
            "InstanceType": instance_type,
            "DataDiskType": data_disk_type,
            "InstanceChargeType": instance_charge_type}
        return self._handle_request(api_request).result

    def list_emr_available_config(self, resource_owner_id=None, region_id=None):
        api_request = APIRequest('ListEmrAvailableConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def delete_user(
            self,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None,
            type_=None,
            user_id=None):
        api_request = APIRequest('DeleteUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "Type": type_,
            "UserId": user_id}
        return self._handle_request(api_request).result

    def create_users(
            self,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None,
            list_of_user_info=None):
        api_request = APIRequest('CreateUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "UserInfo": list_of_user_info}
        repeat_info = {"UserInfo": ('UserInfo', 'list', 'dict', [('Type', 'str', None, None),
                                                                 ('UserId', 'str', None, None),
                                                                 ('UserName', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_user_password(
            self,
            resource_owner_id=None,
            password=None,
            region_id=None,
            cluster_id=None,
            list_of_user_info=None):
        api_request = APIRequest('CreateUserPassword', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Password": password,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "UserInfo": list_of_user_info}
        repeat_info = {"UserInfo": ('UserInfo', 'list', 'dict', [('Type', 'str', None, None),
                                                                 ('GroupName', 'str', None, None),
                                                                 ('UserId', 'str', None, None),
                                                                 ('UserName', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_cluster_with_template(
            self,
            resource_owner_id=None,
            unique_tag=None,
            cluster_name=None,
            template_biz_id=None):
        api_request = APIRequest('CreateClusterWithTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UniqueTag": unique_tag,
            "ClusterName": cluster_name,
            "TemplateBizId": template_biz_id}
        return self._handle_request(api_request).result

    def modify_flow_for_web(
            self,
            cron_expr=None,
            parent_flow_list=None,
            alert_ding_ding_group_biz_id=None,
            periodic=None,
            start_schedule=None,
            description=None,
            cluster_id=None,
            alert_user_group_biz_id=None,
            graph=None,
            host_name=None,
            region_id=None,
            create_cluster=None,
            name=None,
            end_schedule=None,
            id_=None,
            alert_conf=None,
            project_id=None,
            status=None,
            parent_category=None):
        api_request = APIRequest('ModifyFlowForWeb', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CronExpr": cron_expr,
            "ParentFlowList": parent_flow_list,
            "AlertDingDingGroupBizId": alert_ding_ding_group_biz_id,
            "Periodic": periodic,
            "StartSchedule": start_schedule,
            "Description": description,
            "ClusterId": cluster_id,
            "AlertUserGroupBizId": alert_user_group_biz_id,
            "Graph": graph,
            "HostName": host_name,
            "RegionId": region_id,
            "CreateCluster": create_cluster,
            "Name": name,
            "EndSchedule": end_schedule,
            "Id": id_,
            "AlertConf": alert_conf,
            "ProjectId": project_id,
            "Status": status,
            "ParentCategory": parent_category}
        return self._handle_request(api_request).result

    def kill_flow_job(self, region_id=None, job_instance_id=None, project_id=None):
        api_request = APIRequest('KillFlowJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "JobInstanceId": job_instance_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def get_user_submission_statistic_info(
            self,
            from_datetime=None,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None,
            to_datetime=None,
            application_type=None,
            final_status=None):
        api_request = APIRequest('GetUserSubmissionStatisticInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FromDatetime": from_datetime,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "ToDatetime": to_datetime,
            "ApplicationType": application_type,
            "FinalStatus": final_status}
        return self._handle_request(api_request).result

    def get_user_output_statistic_info(
            self,
            from_datetime=None,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None,
            to_datetime=None):
        api_request = APIRequest('GetUserOutputStatisticInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FromDatetime": from_datetime,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "ToDatetime": to_datetime}
        return self._handle_request(api_request).result

    def get_user_input_statistic_info(
            self,
            from_datetime=None,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None,
            to_datetime=None):
        api_request = APIRequest('GetUserInputStatisticInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FromDatetime": from_datetime,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "ToDatetime": to_datetime}
        return self._handle_request(api_request).result

    def get_queue_submission_statistic_info(
            self,
            from_datetime=None,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None,
            to_datetime=None,
            application_type=None,
            final_status=None):
        api_request = APIRequest('GetQueueSubmissionStatisticInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FromDatetime": from_datetime,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "ToDatetime": to_datetime,
            "ApplicationType": application_type,
            "FinalStatus": final_status}
        return self._handle_request(api_request).result

    def get_queue_output_statistic_info(
            self,
            from_datetime=None,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None,
            to_datetime=None):
        api_request = APIRequest('GetQueueOutputStatisticInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FromDatetime": from_datetime,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "ToDatetime": to_datetime}
        return self._handle_request(api_request).result

    def get_queue_input_statistic_info(
            self,
            from_datetime=None,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None,
            to_datetime=None):
        api_request = APIRequest('GetQueueInputStatisticInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FromDatetime": from_datetime,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "ToDatetime": to_datetime}
        return self._handle_request(api_request).result

    def get_job_running_time_statistic_info(
            self,
            from_datetime=None,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            cluster_id=None,
            to_datetime=None,
            page_number=None):
        api_request = APIRequest('GetJobRunningTimeStatisticInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FromDatetime": from_datetime,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "ToDatetime": to_datetime,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_job_output_statistic_info(
            self,
            from_datetime=None,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            cluster_id=None,
            to_datetime=None,
            page_number=None):
        api_request = APIRequest('GetJobOutputStatisticInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FromDatetime": from_datetime,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "ToDatetime": to_datetime,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_job_input_statistic_info(
            self,
            from_datetime=None,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            cluster_id=None,
            to_datetime=None,
            page_number=None):
        api_request = APIRequest('GetJobInputStatisticInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FromDatetime": from_datetime,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "ToDatetime": to_datetime,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_hdfs_capacity_statistic_info(
            self,
            from_datetime=None,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None,
            to_datetime=None):
        api_request = APIRequest('GetHdfsCapacityStatisticInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FromDatetime": from_datetime,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "ToDatetime": to_datetime}
        return self._handle_request(api_request).result

    def create_flow_for_web(
            self,
            cron_expr=None,
            parent_flow_list=None,
            alert_ding_ding_group_biz_id=None,
            start_schedule=None,
            description=None,
            cluster_id=None,
            alert_user_group_biz_id=None,
            graph=None,
            host_name=None,
            region_id=None,
            create_cluster=None,
            name=None,
            end_schedule=None,
            alert_conf=None,
            project_id=None,
            parent_category=None):
        api_request = APIRequest('CreateFlowForWeb', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CronExpr": cron_expr,
            "ParentFlowList": parent_flow_list,
            "AlertDingDingGroupBizId": alert_ding_ding_group_biz_id,
            "StartSchedule": start_schedule,
            "Description": description,
            "ClusterId": cluster_id,
            "AlertUserGroupBizId": alert_user_group_biz_id,
            "Graph": graph,
            "HostName": host_name,
            "RegionId": region_id,
            "CreateCluster": create_cluster,
            "Name": name,
            "EndSchedule": end_schedule,
            "AlertConf": alert_conf,
            "ProjectId": project_id,
            "ParentCategory": parent_category}
        return self._handle_request(api_request).result

    def describe_available_instance_type(
            self,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None):
        api_request = APIRequest('DescribeAvailableInstanceType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def suspend_flow(self, flow_instance_id=None, region_id=None, project_id=None):
        api_request = APIRequest('SuspendFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FlowInstanceId": flow_instance_id,
            "RegionId": region_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def submit_flow_job(
            self,
            job_id=None,
            host_name=None,
            region_id=None,
            conf=None,
            cluster_id=None,
            project_id=None):
        api_request = APIRequest('SubmitFlowJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "HostName": host_name,
            "RegionId": region_id,
            "Conf": conf,
            "ClusterId": cluster_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def submit_flow(self, region_id=None, conf=None, project_id=None, flow_id=None):
        api_request = APIRequest('SubmitFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "Conf": conf,
            "ProjectId": project_id,
            "FlowId": flow_id}
        return self._handle_request(api_request).result

    def resume_flow(self, flow_instance_id=None, region_id=None, project_id=None):
        api_request = APIRequest('ResumeFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FlowInstanceId": flow_instance_id,
            "RegionId": region_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def rerun_flow(self, flow_instance_id=None, region_id=None, project_id=None, re_run_fail=None):
        api_request = APIRequest('RerunFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FlowInstanceId": flow_instance_id,
            "RegionId": region_id,
            "ProjectId": project_id,
            "ReRunFail": re_run_fail}
        return self._handle_request(api_request).result

    def modify_flow_project_cluster_setting(
            self,
            list_of_user_list=None,
            list_of_queue_list=None,
            region_id=None,
            list_of_host_list=None,
            cluster_id=None,
            default_queue=None,
            project_id=None,
            default_user=None):
        api_request = APIRequest('ModifyFlowProjectClusterSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserList": list_of_user_list,
            "QueueList": list_of_queue_list,
            "RegionId": region_id,
            "HostList": list_of_host_list,
            "ClusterId": cluster_id,
            "DefaultQueue": default_queue,
            "ProjectId": project_id,
            "DefaultUser": default_user}
        repeat_info = {"UserList": ('UserList', 'list', 'str', None),
                       "QueueList": ('QueueList', 'list', 'str', None),
                       "HostList": ('HostList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_flow_project(self, region_id=None, name=None, description=None, project_id=None):
        api_request = APIRequest('ModifyFlowProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "Name": name,
            "Description": description,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def modify_flow_job(
            self,
            run_conf=None,
            env_conf=None,
            description=None,
            cluster_id=None,
            params=None,
            param_conf=None,
            list_of_resource_list=None,
            fail_act=None,
            custom_variables=None,
            mode=None,
            retry_interval=None,
            monitor_conf=None,
            region_id=None,
            name=None,
            id_=None,
            max_retry=None,
            alert_conf=None,
            project_id=None):
        api_request = APIRequest('ModifyFlowJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RunConf": run_conf,
            "EnvConf": env_conf,
            "Description": description,
            "ClusterId": cluster_id,
            "Params": params,
            "ParamConf": param_conf,
            "ResourceList": list_of_resource_list,
            "FailAct": fail_act,
            "CustomVariables": custom_variables,
            "Mode": mode,
            "RetryInterval": retry_interval,
            "MonitorConf": monitor_conf,
            "RegionId": region_id,
            "Name": name,
            "Id": id_,
            "MaxRetry": max_retry,
            "AlertConf": alert_conf,
            "ProjectId": project_id}
        repeat_info = {
            "ResourceList": (
                'ResourceList', 'list', 'dict', [
                    ('Path', 'str', None, None), ('Alias', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_flow_category(
            self,
            region_id=None,
            name=None,
            id_=None,
            project_id=None,
            parent_id=None):
        api_request = APIRequest('ModifyFlowCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "Name": name,
            "Id": id_,
            "ProjectId": project_id,
            "ParentId": parent_id}
        return self._handle_request(api_request).result

    def modify_flow(
            self,
            cron_expr=None,
            parent_flow_list=None,
            alert_ding_ding_group_biz_id=None,
            periodic=None,
            start_schedule=None,
            description=None,
            cluster_id=None,
            alert_user_group_biz_id=None,
            host_name=None,
            application=None,
            region_id=None,
            create_cluster=None,
            name=None,
            end_schedule=None,
            id_=None,
            alert_conf=None,
            project_id=None,
            status=None,
            parent_category=None):
        api_request = APIRequest('ModifyFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CronExpr": cron_expr,
            "ParentFlowList": parent_flow_list,
            "AlertDingDingGroupBizId": alert_ding_ding_group_biz_id,
            "Periodic": periodic,
            "StartSchedule": start_schedule,
            "Description": description,
            "ClusterId": cluster_id,
            "AlertUserGroupBizId": alert_user_group_biz_id,
            "HostName": host_name,
            "Application": application,
            "RegionId": region_id,
            "CreateCluster": create_cluster,
            "Name": name,
            "EndSchedule": end_schedule,
            "Id": id_,
            "AlertConf": alert_conf,
            "ProjectId": project_id,
            "Status": status,
            "ParentCategory": parent_category}
        return self._handle_request(api_request).result

    def list_flow_project_user(
            self,
            region_id=None,
            page_size=None,
            project_id=None,
            page_number=None):
        api_request = APIRequest('ListFlowProjectUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "PageSize": page_size,
            "ProjectId": project_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_flow_project_cluster_setting(
            self,
            region_id=None,
            page_size=None,
            project_id=None,
            page_number=None):
        api_request = APIRequest('ListFlowProjectClusterSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "PageSize": page_size,
            "ProjectId": project_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_flow_project(
            self,
            region_id=None,
            name=None,
            page_size=None,
            project_id=None,
            page_number=None):
        api_request = APIRequest('ListFlowProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "Name": name,
            "PageSize": page_size,
            "ProjectId": project_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_flow_node_instance_container_status(
            self,
            region_id=None,
            page_size=None,
            node_instance_id=None,
            project_id=None,
            page_number=None):
        api_request = APIRequest('ListFlowNodeInstanceContainerStatus',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "PageSize": page_size,
            "NodeInstanceId": node_instance_id,
            "ProjectId": project_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_flow_job_history(
            self,
            time_range=None,
            list_of_status_list=None,
            instance_id=None,
            region_id=None,
            page_size=None,
            id_=None,
            project_id=None,
            job_type=None,
            page_number=None):
        api_request = APIRequest('ListFlowJobHistory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TimeRange": time_range,
            "StatusList": list_of_status_list,
            "InstanceId": instance_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "Id": id_,
            "ProjectId": project_id,
            "JobType": job_type,
            "PageNumber": page_number}
        repeat_info = {"StatusList": ('StatusList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_flow_instance(
            self,
            owner=None,
            time_range=None,
            list_of_status_list=None,
            order_by=None,
            page_number=None,
            instance_id=None,
            region_id=None,
            page_size=None,
            flow_name=None,
            id_=None,
            flow_id=None,
            project_id=None,
            order_type=None):
        api_request = APIRequest('ListFlowInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Owner": owner,
            "TimeRange": time_range,
            "StatusList": list_of_status_list,
            "OrderBy": order_by,
            "PageNumber": page_number,
            "InstanceId": instance_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "FlowName": flow_name,
            "Id": id_,
            "FlowId": flow_id,
            "ProjectId": project_id,
            "OrderType": order_type}
        repeat_info = {"StatusList": ('StatusList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_flow_cluster_host(self, region_id=None, cluster_id=None, project_id=None):
        api_request = APIRequest('ListFlowClusterHost', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def list_flow_cluster(self, region_id=None, page_size=None, project_id=None, page_number=None):
        api_request = APIRequest('ListFlowCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "PageSize": page_size,
            "ProjectId": project_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_flow_category(
            self,
            region_id=None,
            root=None,
            page_size=None,
            project_id=None,
            parent_id=None,
            page_number=None):
        api_request = APIRequest('ListFlowCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "Root": root,
            "PageSize": page_size,
            "ProjectId": project_id,
            "ParentId": parent_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def kill_flow(self, flow_instance_id=None, region_id=None, project_id=None):
        api_request = APIRequest('KillFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FlowInstanceId": flow_instance_id,
            "RegionId": region_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def describe_flow_project_cluster_setting(
            self, region_id=None, cluster_id=None, project_id=None):
        api_request = APIRequest('DescribeFlowProjectClusterSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def describe_flow_project(self, region_id=None, project_id=None):
        api_request = APIRequest('DescribeFlowProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def describe_flow_node_instance_launcher_log(
            self,
            offset=None,
            region_id=None,
            start=None,
            length=None,
            end_time=None,
            start_time=None,
            lines=None,
            reverse=None,
            node_instance_id=None,
            project_id=None):
        api_request = APIRequest('DescribeFlowNodeInstanceLauncherLog',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Offset": offset,
            "RegionId": region_id,
            "Start": start,
            "Length": length,
            "EndTime": end_time,
            "StartTime": start_time,
            "Lines": lines,
            "Reverse": reverse,
            "NodeInstanceId": node_instance_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def describe_flow_node_instance_container_log(
            self,
            offset=None,
            region_id=None,
            log_name=None,
            app_id=None,
            length=None,
            container_id=None,
            node_instance_id=None,
            project_id=None):
        api_request = APIRequest('DescribeFlowNodeInstanceContainerLog',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Offset": offset,
            "RegionId": region_id,
            "LogName": log_name,
            "AppId": app_id,
            "Length": length,
            "ContainerId": container_id,
            "NodeInstanceId": node_instance_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def describe_flow_node_instance(self, region_id=None, id_=None, project_id=None):
        api_request = APIRequest('DescribeFlowNodeInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Id": id_, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def describe_flow_job(self, region_id=None, id_=None, project_id=None):
        api_request = APIRequest('DescribeFlowJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Id": id_, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def describe_flow_instance(self, region_id=None, id_=None, project_id=None):
        api_request = APIRequest('DescribeFlowInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Id": id_, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def describe_flow_category_tree(self, region_id=None, type_=None, project_id=None):
        api_request = APIRequest('DescribeFlowCategoryTree', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Type": type_, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def describe_flow_category(self, region_id=None, id_=None, project_id=None):
        api_request = APIRequest('DescribeFlowCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Id": id_, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def describe_flow(self, region_id=None, id_=None, project_id=None):
        api_request = APIRequest('DescribeFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Id": id_, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def delete_flow_project_user(self, region_id=None, project_id=None, user_name=None):
        api_request = APIRequest('DeleteFlowProjectUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "ProjectId": project_id,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def delete_flow_project_cluster_setting(self, region_id=None, cluster_id=None, project_id=None):
        api_request = APIRequest('DeleteFlowProjectClusterSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def delete_flow_project(self, region_id=None, project_id=None):
        api_request = APIRequest('DeleteFlowProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def delete_flow_job(self, region_id=None, id_=None, project_id=None):
        api_request = APIRequest('DeleteFlowJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Id": id_, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def delete_flow_category(self, region_id=None, id_=None, project_id=None):
        api_request = APIRequest('DeleteFlowCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Id": id_, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def delete_flow(self, region_id=None, id_=None, project_id=None):
        api_request = APIRequest('DeleteFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Id": id_, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def create_flow_project_user(self, region_id=None, project_id=None, list_of_user=None):
        api_request = APIRequest('CreateFlowProjectUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "ProjectId": project_id, "User": list_of_user}
        repeat_info = {"User": ('User', 'list', 'dict', [('UserId', 'str', None, None),
                                                         ('UserName', 'str', None, None),
                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_flow_project_cluster_setting(
            self,
            list_of_user_list=None,
            list_of_queue_list=None,
            region_id=None,
            list_of_host_list=None,
            cluster_id=None,
            default_queue=None,
            project_id=None,
            default_user=None):
        api_request = APIRequest('CreateFlowProjectClusterSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserList": list_of_user_list,
            "QueueList": list_of_queue_list,
            "RegionId": region_id,
            "HostList": list_of_host_list,
            "ClusterId": cluster_id,
            "DefaultQueue": default_queue,
            "ProjectId": project_id,
            "DefaultUser": default_user}
        repeat_info = {"UserList": ('UserList', 'list', 'str', None),
                       "QueueList": ('QueueList', 'list', 'str', None),
                       "HostList": ('HostList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_flow_project(self, region_id=None, name=None, description=None):
        api_request = APIRequest('CreateFlowProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Name": name, "Description": description}
        return self._handle_request(api_request).result

    def create_flow_job(
            self,
            run_conf=None,
            env_conf=None,
            description=None,
            cluster_id=None,
            type_=None,
            params=None,
            param_conf=None,
            list_of_resource_list=None,
            fail_act=None,
            mode=None,
            retry_interval=None,
            monitor_conf=None,
            region_id=None,
            name=None,
            max_retry=None,
            adhoc=None,
            alert_conf=None,
            project_id=None,
            parent_category=None):
        api_request = APIRequest('CreateFlowJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RunConf": run_conf,
            "EnvConf": env_conf,
            "Description": description,
            "ClusterId": cluster_id,
            "Type": type_,
            "Params": params,
            "ParamConf": param_conf,
            "ResourceList": list_of_resource_list,
            "FailAct": fail_act,
            "Mode": mode,
            "RetryInterval": retry_interval,
            "MonitorConf": monitor_conf,
            "RegionId": region_id,
            "Name": name,
            "MaxRetry": max_retry,
            "Adhoc": adhoc,
            "AlertConf": alert_conf,
            "ProjectId": project_id,
            "ParentCategory": parent_category}
        repeat_info = {
            "ResourceList": (
                'ResourceList', 'list', 'dict', [
                    ('Path', 'str', None, None), ('Alias', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_flow_category(
            self,
            region_id=None,
            name=None,
            type_=None,
            project_id=None,
            parent_id=None):
        api_request = APIRequest('CreateFlowCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "Name": name,
            "Type": type_,
            "ProjectId": project_id,
            "ParentId": parent_id}
        return self._handle_request(api_request).result

    def create_flow(
            self,
            cron_expr=None,
            parent_flow_list=None,
            alert_ding_ding_group_biz_id=None,
            start_schedule=None,
            description=None,
            cluster_id=None,
            alert_user_group_biz_id=None,
            host_name=None,
            application=None,
            region_id=None,
            create_cluster=None,
            name=None,
            end_schedule=None,
            alert_conf=None,
            project_id=None,
            parent_category=None):
        api_request = APIRequest('CreateFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CronExpr": cron_expr,
            "ParentFlowList": parent_flow_list,
            "AlertDingDingGroupBizId": alert_ding_ding_group_biz_id,
            "StartSchedule": start_schedule,
            "Description": description,
            "ClusterId": cluster_id,
            "AlertUserGroupBizId": alert_user_group_biz_id,
            "HostName": host_name,
            "Application": application,
            "RegionId": region_id,
            "CreateCluster": create_cluster,
            "Name": name,
            "EndSchedule": end_schedule,
            "AlertConf": alert_conf,
            "ProjectId": project_id,
            "ParentCategory": parent_category}
        return self._handle_request(api_request).result

    def run_ops_command(
            self,
            resource_owner_id=None,
            region_id=None,
            ops_command_name=None,
            comment=None,
            custom_params=None,
            cluster_id=None,
            list_of_host_id_list=None,
            dimension=None):
        api_request = APIRequest('RunOpsCommand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "OpsCommandName": ops_command_name,
            "Comment": comment,
            "CustomParams": custom_params,
            "ClusterId": cluster_id,
            "HostIdList": list_of_host_id_list,
            "Dimension": dimension}
        repeat_info = {"HostIdList": ('HostIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_ops_operation_task(
            self,
            resource_owner_id=None,
            region_id=None,
            operation_id=None,
            page_number=None):
        api_request = APIRequest('ListOpsOperationTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "OperationId": operation_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_ops_operation(
            self,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('ListOpsOperation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_supported_ops_command(self, resource_owner_id=None, region_id=None):
        api_request = APIRequest('GetSupportedOpsCommand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def get_ops_command_result_once(
            self,
            resource_owner_id=None,
            region_id=None,
            cluster_id=None,
            task_id=None):
        api_request = APIRequest('GetOpsCommandResultOnce', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def get_ops_command_result(
            self,
            resource_owner_id=None,
            region_id=None,
            end_cursor=None,
            start_cursor=None,
            cluster_id=None,
            task_id=None):
        api_request = APIRequest('GetOpsCommandResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "EndCursor": end_cursor,
            "StartCursor": start_cursor,
            "ClusterId": cluster_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def get_ops_command_detail(self, resource_owner_id=None, region_id=None, ops_command_name=None):
        api_request = APIRequest('GetOpsCommandDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "OpsCommandName": ops_command_name}
        return self._handle_request(api_request).result

    def search_log(
            self,
            resource_owner_id=None,
            logstore_name=None,
            from_timestamp=None,
            offset=None,
            line=None,
            cluster_id=None,
            reverse=None,
            host_inner_ip=None,
            host_name=None,
            region_id=None,
            to_timestamp=None,
            sls_query_string=None):
        api_request = APIRequest('SearchLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "LogstoreName": logstore_name,
            "FromTimestamp": from_timestamp,
            "Offset": offset,
            "Line": line,
            "ClusterId": cluster_id,
            "Reverse": reverse,
            "HostInnerIp": host_inner_ip,
            "HostName": host_name,
            "RegionId": region_id,
            "ToTimestamp": to_timestamp,
            "SlsQueryString": sls_query_string}
        return self._handle_request(api_request).result

    def list_sls_logstore_info(
            self,
            resource_owner_id=None,
            region_id=None,
            component_name=None,
            service_name=None,
            cluster_id=None):
        api_request = APIRequest('ListSlsLogstoreInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ComponentName": component_name,
            "ServiceName": service_name,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_service_log(
            self,
            resource_owner_id=None,
            host_name=None,
            max_keys=None,
            logstore_name=None,
            region_id=None,
            marker=None,
            cluster_id=None):
        api_request = APIRequest('ListServiceLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HostName": host_name,
            "MaxKeys": max_keys,
            "LogstoreName": logstore_name,
            "RegionId": region_id,
            "Marker": marker,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def get_log_download_url(
            self,
            resource_owner_id=None,
            host_name=None,
            logstore_name=None,
            region_id=None,
            cluster_id=None,
            log_file_name=None):
        api_request = APIRequest('GetLogDownloadUrl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HostName": host_name,
            "LogstoreName": logstore_name,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "LogFileName": log_file_name}
        return self._handle_request(api_request).result

    def suspend_execution_plan_instance(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('SuspendExecutionPlanInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def retry_execution_plan_instance(
            self,
            resource_owner_id=None,
            region_id=None,
            arguments=None,
            id_=None,
            rerun_fail=None):
        api_request = APIRequest('RetryExecutionPlanInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Arguments": arguments,
            "Id": id_,
            "RerunFail": rerun_fail}
        return self._handle_request(api_request).result

    def resume_execution_plan_instance(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('ResumeExecutionPlanInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def refresh_cluster_resource_pool(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_pool_id=None,
            cluster_id=None):
        api_request = APIRequest('RefreshClusterResourcePool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourcePoolId": resource_pool_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def modify_resource_queue(
            self,
            resource_owner_id=None,
            parent_queue_id=None,
            region_id=None,
            name=None,
            qualified_name=None,
            resource_pool_id=None,
            id_=None,
            cluster_id=None,
            leaf=None,
            list_of_config=None):
        api_request = APIRequest('ModifyResourceQueue', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ParentQueueId": parent_queue_id,
            "RegionId": region_id,
            "Name": name,
            "QualifiedName": qualified_name,
            "ResourcePoolId": resource_pool_id,
            "Id": id_,
            "ClusterId": cluster_id,
            "Leaf": leaf,
            "Config": list_of_config}
        repeat_info = {"Config": ('Config', 'list', 'dict', [('ConfigKey', 'str', None, None),
                                                             ('Note', 'str', None, None),
                                                             ('ConfigValue', 'str', None, None),
                                                             ('Id', 'str', None, None),
                                                             ('Category', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_resource_pool(
            self,
            resource_owner_id=None,
            region_id=None,
            name=None,
            active=None,
            id_=None,
            cluster_id=None,
            yarnsiteconfig=None,
            list_of_config=None):
        api_request = APIRequest('ModifyResourcePool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Active": active,
            "Id": id_,
            "ClusterId": cluster_id,
            "Yarnsiteconfig": yarnsiteconfig,
            "Config": list_of_config}
        repeat_info = {"Config": ('Config', 'list', 'dict', [('ConfigKey', 'str', None, None),
                                                             ('Note', 'str', None, None),
                                                             ('ConfigValue', 'str', None, None),
                                                             ('Id', 'str', None, None),
                                                             ('Category', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_job_execution_plan_param(
            self,
            resource_owner_id=None,
            param_name=None,
            param_value=None,
            id_=None):
        api_request = APIRequest('ModifyJobExecutionPlanParam', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ParamName": param_name,
            "ParamValue": param_value,
            "Id": id_}
        return self._handle_request(api_request).result

    def modify_job_execution_plan_folder(
            self,
            resource_owner_id=None,
            name=None,
            id_=None,
            parent_id=None):
        api_request = APIRequest('ModifyJobExecutionPlanFolder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Name": name,
            "Id": id_,
            "ParentId": parent_id}
        return self._handle_request(api_request).result

    def modify_cluster_template(
            self,
            resource_owner_id=None,
            log_path=None,
            master_pwd=None,
            configurations=None,
            io_optimized=None,
            security_group_id=None,
            ssh_enable=None,
            eas_enable=None,
            key_pair_name=None,
            meta_store_type=None,
            security_group_name=None,
            deposit_type=None,
            machine_type=None,
            list_of_bootstrap_action=None,
            region_id=None,
            use_local_meta_db=None,
            meta_store_conf=None,
            emr_ver=None,
            template_name=None,
            user_defined_emr_ecs_role=None,
            is_open_public_ip=None,
            period=None,
            instance_generation=None,
            vswitch_id=None,
            cluster_type=None,
            auto_renew=None,
            list_of_option_soft_ware_list=None,
            vpc_id=None,
            net_type=None,
            biz_id=None,
            list_of_host_group=None,
            zone_id=None,
            charge_type=None,
            use_custom_hive_meta_db=None,
            list_of_config=None,
            high_availability_enable=None,
            init_custom_hive_meta_db=None):
        api_request = APIRequest('ModifyClusterTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "LogPath": log_path,
            "MasterPwd": master_pwd,
            "Configurations": configurations,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "SshEnable": ssh_enable,
            "EasEnable": eas_enable,
            "KeyPairName": key_pair_name,
            "MetaStoreType": meta_store_type,
            "SecurityGroupName": security_group_name,
            "DepositType": deposit_type,
            "MachineType": machine_type,
            "BootstrapAction": list_of_bootstrap_action,
            "RegionId": region_id,
            "UseLocalMetaDb": use_local_meta_db,
            "MetaStoreConf": meta_store_conf,
            "EmrVer": emr_ver,
            "TemplateName": template_name,
            "UserDefinedEmrEcsRole": user_defined_emr_ecs_role,
            "IsOpenPublicIp": is_open_public_ip,
            "Period": period,
            "InstanceGeneration": instance_generation,
            "VSwitchId": vswitch_id,
            "ClusterType": cluster_type,
            "AutoRenew": auto_renew,
            "OptionSoftWareList": list_of_option_soft_ware_list,
            "VpcId": vpc_id,
            "NetType": net_type,
            "BizId": biz_id,
            "HostGroup": list_of_host_group,
            "ZoneId": zone_id,
            "ChargeType": charge_type,
            "UseCustomHiveMetaDb": use_custom_hive_meta_db,
            "Config": list_of_config,
            "HighAvailabilityEnable": high_availability_enable,
            "InitCustomHiveMetaDb": init_custom_hive_meta_db}
        repeat_info = {"BootstrapAction": ('BootstrapAction', 'list', 'dict', [('Path', 'str', None, None),
                                                                               ('Arg', 'str', None, None),
                                                                               ('Name', 'str', None, None),
                                                                               ]),
                       "OptionSoftWareList": ('OptionSoftWareList', 'list', 'str', None),
                       "HostGroup": ('HostGroup', 'list', 'dict', [('Period', 'str', None, None),
                                                                   ('SysDiskCapacity', 'str', None, None),
                                                                   ('DiskCapacity', 'str', None, None),
                                                                   ('SysDiskType', 'str', None, None),
                                                                   ('ClusterId', 'str', None, None),
                                                                   ('DiskType', 'str', None, None),
                                                                   ('HostGroupName', 'str', None, None),
                                                                   ('VSwitchId', 'str', None, None),
                                                                   ('DiskCount', 'str', None, None),
                                                                   ('AutoRenew', 'str', None, None),
                                                                   ('HostGroupId', 'str', None, None),
                                                                   ('NodeCount', 'str', None, None),
                                                                   ('InstanceType', 'str', None, None),
                                                                   ('Comment', 'str', None, None),
                                                                   ('ChargeType', 'str', None, None),
                                                                   ('MultiInstanceTypes', 'str', None, None),
                                                                   ('CreateType', 'str', None, None),
                                                                   ('HostGroupType', 'str', None, None),
                                                                   ]),
                       "Config": ('Config', 'list', 'dict', [('ConfigKey', 'str', None, None),
                                                             ('FileName', 'str', None, None),
                                                             ('Encrypt', 'str', None, None),
                                                             ('Replace', 'str', None, None),
                                                             ('ConfigValue', 'str', None, None),
                                                             ('ServiceName', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_job_execution_plan_params(
            self,
            resource_owner_id=None,
            relate_id=None,
            param_biz_type=None):
        api_request = APIRequest('ListJobExecutionPlanParams', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RelateId": relate_id,
            "ParamBizType": param_biz_type}
        return self._handle_request(api_request).result

    def list_job_execution_plan_hierarchy(
            self,
            resource_owner_id=None,
            current_id=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('ListJobExecutionPlanHierarchy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "CurrentId": current_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_cluster_templates(
            self,
            resource_owner_id=None,
            region_id=None,
            biz_id=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('ListClusterTemplates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BizId": biz_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_cluster_template(self, resource_owner_id=None, biz_id=None):
        api_request = APIRequest('DescribeClusterTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "BizId": biz_id}
        return self._handle_request(api_request).result

    def delete_resource_queue(
            self,
            resource_owner_id=None,
            resource_queue_id=None,
            region_id=None,
            cluster_id=None):
        api_request = APIRequest('DeleteResourceQueue', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceQueueId": resource_queue_id,
            "RegionId": region_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def delete_cluster_template(self, resource_owner_id=None, region_id=None, biz_id=None):
        api_request = APIRequest('DeleteClusterTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "BizId": biz_id}
        return self._handle_request(api_request).result

    def create_resource_queue(
            self,
            resource_owner_id=None,
            parent_queue_id=None,
            region_id=None,
            name=None,
            qualified_name=None,
            resource_pool_id=None,
            cluster_id=None,
            leaf=None,
            list_of_config=None):
        api_request = APIRequest('CreateResourceQueue', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ParentQueueId": parent_queue_id,
            "RegionId": region_id,
            "Name": name,
            "QualifiedName": qualified_name,
            "ResourcePoolId": resource_pool_id,
            "ClusterId": cluster_id,
            "Leaf": leaf,
            "Config": list_of_config}
        repeat_info = {"Config": ('Config', 'list', 'dict', [('ConfigKey', 'str', None, None),
                                                             ('Note', 'str', None, None),
                                                             ('ConfigValue', 'str', None, None),
                                                             ('Category', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_cluster_template(
            self,
            resource_owner_id=None,
            log_path=None,
            master_pwd=None,
            configurations=None,
            io_optimized=None,
            security_group_id=None,
            ssh_enable=None,
            eas_enable=None,
            key_pair_name=None,
            meta_store_type=None,
            security_group_name=None,
            deposit_type=None,
            machine_type=None,
            list_of_bootstrap_action=None,
            region_id=None,
            use_local_meta_db=None,
            meta_store_conf=None,
            emr_ver=None,
            template_name=None,
            user_defined_emr_ecs_role=None,
            is_open_public_ip=None,
            period=None,
            instance_generation=None,
            vswitch_id=None,
            cluster_type=None,
            auto_renew=None,
            list_of_option_soft_ware_list=None,
            vpc_id=None,
            net_type=None,
            list_of_host_group=None,
            zone_id=None,
            use_custom_hive_meta_db=None,
            list_of_config=None,
            high_availability_enable=None,
            init_custom_hive_meta_db=None):
        api_request = APIRequest('CreateClusterTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "LogPath": log_path,
            "MasterPwd": master_pwd,
            "Configurations": configurations,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "SshEnable": ssh_enable,
            "EasEnable": eas_enable,
            "KeyPairName": key_pair_name,
            "MetaStoreType": meta_store_type,
            "SecurityGroupName": security_group_name,
            "DepositType": deposit_type,
            "MachineType": machine_type,
            "BootstrapAction": list_of_bootstrap_action,
            "RegionId": region_id,
            "UseLocalMetaDb": use_local_meta_db,
            "MetaStoreConf": meta_store_conf,
            "EmrVer": emr_ver,
            "TemplateName": template_name,
            "UserDefinedEmrEcsRole": user_defined_emr_ecs_role,
            "IsOpenPublicIp": is_open_public_ip,
            "Period": period,
            "InstanceGeneration": instance_generation,
            "VSwitchId": vswitch_id,
            "ClusterType": cluster_type,
            "AutoRenew": auto_renew,
            "OptionSoftWareList": list_of_option_soft_ware_list,
            "VpcId": vpc_id,
            "NetType": net_type,
            "HostGroup": list_of_host_group,
            "ZoneId": zone_id,
            "UseCustomHiveMetaDb": use_custom_hive_meta_db,
            "Config": list_of_config,
            "HighAvailabilityEnable": high_availability_enable,
            "InitCustomHiveMetaDb": init_custom_hive_meta_db}
        repeat_info = {"BootstrapAction": ('BootstrapAction', 'list', 'dict', [('Path', 'str', None, None),
                                                                               ('Arg', 'str', None, None),
                                                                               ('Name', 'str', None, None),
                                                                               ]),
                       "OptionSoftWareList": ('OptionSoftWareList', 'list', 'str', None),
                       "HostGroup": ('HostGroup', 'list', 'dict', [('Period', 'str', None, None),
                                                                   ('SysDiskCapacity', 'str', None, None),
                                                                   ('DiskCapacity', 'str', None, None),
                                                                   ('SysDiskType', 'str', None, None),
                                                                   ('ClusterId', 'str', None, None),
                                                                   ('DiskType', 'str', None, None),
                                                                   ('HostGroupName', 'str', None, None),
                                                                   ('VSwitchId', 'str', None, None),
                                                                   ('DiskCount', 'str', None, None),
                                                                   ('AutoRenew', 'str', None, None),
                                                                   ('HostGroupId', 'str', None, None),
                                                                   ('NodeCount', 'str', None, None),
                                                                   ('InstanceType', 'str', None, None),
                                                                   ('Comment', 'str', None, None),
                                                                   ('ChargeType', 'str', None, None),
                                                                   ('MultiInstanceTypes', 'str', None, None),
                                                                   ('CreateType', 'str', None, None),
                                                                   ('HostGroupType', 'str', None, None),
                                                                   ]),
                       "Config": ('Config', 'list', 'dict', [('ConfigKey', 'str', None, None),
                                                             ('FileName', 'str', None, None),
                                                             ('Encrypt', 'str', None, None),
                                                             ('Replace', 'str', None, None),
                                                             ('ConfigValue', 'str', None, None),
                                                             ('ServiceName', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_resource_pool_scheduler_type(
            self,
            resource_owner_id=None,
            region_id=None,
            scheduler_type=None,
            cluster_id=None):
        api_request = APIRequest('ModifyResourcePoolSchedulerType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "SchedulerType": scheduler_type,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_resource_pool(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None,
            pool_type=None):
        api_request = APIRequest('ListResourcePool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "PoolType": pool_type}
        return self._handle_request(api_request).result

    def describe_cluster_resource_pool_scheduler_type(
            self, resource_owner_id=None, region_id=None, cluster_id=None):
        api_request = APIRequest(
            'DescribeClusterResourcePoolSchedulerType',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def delete_resource_pool(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_pool_id=None,
            cluster_id=None):
        api_request = APIRequest('DeleteResourcePool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourcePoolId": resource_pool_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def create_resource_pool(
            self,
            note=None,
            resource_owner_id=None,
            region_id=None,
            name=None,
            active=None,
            cluster_id=None,
            yarn_site_config=None,
            list_of_config=None,
            pool_type=None):
        api_request = APIRequest('CreateResourcePool', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Note": note,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Active": active,
            "ClusterId": cluster_id,
            "YarnSiteConfig": yarn_site_config,
            "Config": list_of_config,
            "PoolType": pool_type}
        repeat_info = {"Config": ('Config', 'list', 'dict', [('ConfigKey', 'str', None, None),
                                                             ('Note', 'str', None, None),
                                                             ('configType', 'str', None, None),
                                                             ('TargetId', 'str', None, None),
                                                             ('ConfigValue', 'str', None, None),
                                                             ('Category', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def query_alarm_rules(self, resource_owner_id=None, region_id=None, cluster_id=None):
        api_request = APIRequest('QueryAlarmRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def query_alarm_history(
            self,
            cursor=None,
            resource_owner_id=None,
            size=None,
            region_id=None,
            cluster_id=None,
            start_time_stamp=None,
            end_time_stamp=None):
        api_request = APIRequest('QueryAlarmHistory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Cursor": cursor,
            "ResourceOwnerId": resource_owner_id,
            "Size": size,
            "RegionId": region_id,
            "ClusterId": cluster_id,
            "StartTimeStamp": start_time_stamp,
            "EndTimeStamp": end_time_stamp}
        return self._handle_request(api_request).result

    def list_cluster_service_quick_link(
            self,
            resource_owner_id=None,
            region_id=None,
            service_name=None,
            cluster_id=None):
        api_request = APIRequest('ListClusterServiceQuickLink', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ServiceName": service_name,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_cluster_service_config_history(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            service_name=None,
            cluster_id=None,
            page_number=None,
            config_version=None):
        api_request = APIRequest('ListClusterServiceConfigHistory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ServiceName": service_name,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "ConfigVersion": config_version}
        return self._handle_request(api_request).result

    def list_cluster_host_group(
            self,
            resource_owner_id=None,
            list_of_status_list=None,
            region_id=None,
            host_group_id=None,
            page_size=None,
            cluster_id=None,
            host_group_name=None,
            host_group_type=None,
            page_number=None):
        api_request = APIRequest('ListClusterHostGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "StatusList": list_of_status_list,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "HostGroupName": host_group_name,
            "HostGroupType": host_group_type,
            "PageNumber": page_number}
        repeat_info = {"StatusList": ('StatusList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_cluster_service_config_tag(
            self,
            resource_owner_id=None,
            region_id=None,
            config_tag=None,
            service_name=None,
            cluster_id=None):
        api_request = APIRequest('DescribeClusterServiceConfigTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ConfigTag": config_tag,
            "ServiceName": service_name,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def resize_cluster_v2(
            self,
            vswitch_id=None,
            is_open_public_ip=None,
            auto_pay_order=None,
            list_of_host_component_info=None,
            region_id=None,
            list_of_host_group=None,
            cluster_id=None):
        api_request = APIRequest('ResizeClusterV2', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VswitchId": vswitch_id,
            "IsOpenPublicIp": is_open_public_ip,
            "AutoPayOrder": auto_pay_order,
            "HostComponentInfo": list_of_host_component_info,
            "RegionId": region_id,
            "HostGroup": list_of_host_group,
            "ClusterId": cluster_id}
        repeat_info = {"HostComponentInfo": ('HostComponentInfo', 'list', 'dict', [('HostName', 'str', None, None),
                                                                                   ('ComponentNameList', 'list', 'str', None),
                                                                                   ('ServiceName', 'str', None, None),
                                                                                   ]),
                       "HostGroup": ('HostGroup', 'list', 'dict', [('Period', 'str', None, None),
                                                                   ('SysDiskCapacity', 'str', None, None),
                                                                   ('HostKeyPairName', 'str', None, None),
                                                                   ('DiskCapacity', 'str', None, None),
                                                                   ('SysDiskType', 'str', None, None),
                                                                   ('ClusterId', 'str', None, None),
                                                                   ('DiskType', 'str', None, None),
                                                                   ('HostGroupName', 'str', None, None),
                                                                   ('VswitchId', 'str', None, None),
                                                                   ('DiskCount', 'str', None, None),
                                                                   ('AutoRenew', 'str', None, None),
                                                                   ('HostGroupId', 'str', None, None),
                                                                   ('NodeCount', 'str', None, None),
                                                                   ('InstanceType', 'str', None, None),
                                                                   ('Comment', 'str', None, None),
                                                                   ('ChargeType', 'str', None, None),
                                                                   ('CreateType', 'str', None, None),
                                                                   ('HostPassword', 'str', None, None),
                                                                   ('HostGroupType', 'str', None, None),
                                                                   ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def release_cluster_host_group(
            self,
            resource_owner_id=None,
            region_id=None,
            host_group_id=None,
            instance_id_list=None,
            cluster_id=None):
        api_request = APIRequest('ReleaseClusterHostGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "InstanceIdList": instance_id_list,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_cluster_v2(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DescribeClusterV2', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def create_cluster_v2(
            self,
            auto_pay_order=None,
            resource_owner_id=None,
            log_path=None,
            master_pwd=None,
            configurations=None,
            io_optimized=None,
            security_group_id=None,
            ssh_enable=None,
            eas_enable=None,
            key_pair_name=None,
            meta_store_type=None,
            security_group_name=None,
            deposit_type=None,
            machine_type=None,
            list_of_host_component_info=None,
            list_of_bootstrap_action=None,
            region_id=None,
            use_local_meta_db=None,
            meta_store_conf=None,
            emr_ver=None,
            list_of_user_info=None,
            user_defined_emr_ecs_role=None,
            authorize_content=None,
            is_open_public_ip=None,
            period=None,
            white_list_type=None,
            related_cluster_id=None,
            instance_generation=None,
            vswitch_id=None,
            cluster_type=None,
            auto_renew=None,
            list_of_option_soft_ware_list=None,
            vpc_id=None,
            net_type=None,
            name=None,
            list_of_host_group=None,
            zone_id=None,
            charge_type=None,
            use_custom_hive_meta_db=None,
            list_of_config=None,
            high_availability_enable=None,
            init_custom_hive_meta_db=None):
        api_request = APIRequest('CreateClusterV2', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AutoPayOrder": auto_pay_order,
            "ResourceOwnerId": resource_owner_id,
            "LogPath": log_path,
            "MasterPwd": master_pwd,
            "Configurations": configurations,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "SshEnable": ssh_enable,
            "EasEnable": eas_enable,
            "KeyPairName": key_pair_name,
            "MetaStoreType": meta_store_type,
            "SecurityGroupName": security_group_name,
            "DepositType": deposit_type,
            "MachineType": machine_type,
            "HostComponentInfo": list_of_host_component_info,
            "BootstrapAction": list_of_bootstrap_action,
            "RegionId": region_id,
            "UseLocalMetaDb": use_local_meta_db,
            "MetaStoreConf": meta_store_conf,
            "EmrVer": emr_ver,
            "UserInfo": list_of_user_info,
            "UserDefinedEmrEcsRole": user_defined_emr_ecs_role,
            "AuthorizeContent": authorize_content,
            "IsOpenPublicIp": is_open_public_ip,
            "Period": period,
            "WhiteListType": white_list_type,
            "RelatedClusterId": related_cluster_id,
            "InstanceGeneration": instance_generation,
            "VSwitchId": vswitch_id,
            "ClusterType": cluster_type,
            "AutoRenew": auto_renew,
            "OptionSoftWareList": list_of_option_soft_ware_list,
            "VpcId": vpc_id,
            "NetType": net_type,
            "Name": name,
            "HostGroup": list_of_host_group,
            "ZoneId": zone_id,
            "ChargeType": charge_type,
            "UseCustomHiveMetaDB": use_custom_hive_meta_db,
            "Config": list_of_config,
            "HighAvailabilityEnable": high_availability_enable,
            "InitCustomHiveMetaDB": init_custom_hive_meta_db}
        repeat_info = {"HostComponentInfo": ('HostComponentInfo', 'list', 'dict', [('HostName', 'str', None, None),
                                                                                   ('ComponentNameList', 'list', 'str', None),
                                                                                   ('ServiceName', 'str', None, None),
                                                                                   ]),
                       "BootstrapAction": ('BootstrapAction', 'list', 'dict', [('Path', 'str', None, None),
                                                                               ('Arg', 'str', None, None),
                                                                               ('Name', 'str', None, None),
                                                                               ]),
                       "UserInfo": ('UserInfo', 'list', 'dict', [('Password', 'str', None, None),
                                                                 ('UserId', 'str', None, None),
                                                                 ('UserName', 'str', None, None),
                                                                 ]),
                       "OptionSoftWareList": ('OptionSoftWareList', 'list', 'str', None),
                       "HostGroup": ('HostGroup', 'list', 'dict', [('Period', 'str', None, None),
                                                                   ('SysDiskCapacity', 'str', None, None),
                                                                   ('DiskCapacity', 'str', None, None),
                                                                   ('SysDiskType', 'str', None, None),
                                                                   ('ClusterId', 'str', None, None),
                                                                   ('DiskType', 'str', None, None),
                                                                   ('HostGroupName', 'str', None, None),
                                                                   ('VSwitchId', 'str', None, None),
                                                                   ('DiskCount', 'str', None, None),
                                                                   ('AutoRenew', 'str', None, None),
                                                                   ('GpuDriver', 'str', None, None),
                                                                   ('HostGroupId', 'str', None, None),
                                                                   ('NodeCount', 'str', None, None),
                                                                   ('InstanceType', 'str', None, None),
                                                                   ('Comment', 'str', None, None),
                                                                   ('ChargeType', 'str', None, None),
                                                                   ('CreateType', 'str', None, None),
                                                                   ('HostGroupType', 'str', None, None),
                                                                   ]),
                       "Config": ('Config', 'list', 'dict', [('ConfigKey', 'str', None, None),
                                                             ('FileName', 'str', None, None),
                                                             ('Encrypt', 'str', None, None),
                                                             ('Replace', 'str', None, None),
                                                             ('ConfigValue', 'str', None, None),
                                                             ('ServiceName', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def terminate_cluster_operation(
            self,
            resource_owner_id=None,
            region_id=None,
            operation_id=None,
            cluster_id=None):
        api_request = APIRequest('TerminateClusterOperation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "OperationId": operation_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_cluster_op_log(
            self,
            resource_owner_id=None,
            region_id=None,
            end_time=None,
            id_=None,
            start_time=None):
        api_request = APIRequest('DescribeClusterOpLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "EndTime": end_time,
            "Id": id_,
            "StartTime": start_time}
        return self._handle_request(api_request).result

    def list_depended_service(
            self,
            resource_owner_id=None,
            region_id=None,
            service_name=None,
            cluster_id=None):
        api_request = APIRequest('ListDependedService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ServiceName": service_name,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def run_cluster_service_action(
            self,
            execute_strategy=None,
            list_of_host_group_id_list=None,
            resource_owner_id=None,
            only_restart_stale_config_nodes=None,
            node_count_per_batch=None,
            cluster_id=None,
            custom_command=None,
            component_name_list=None,
            region_id=None,
            service_action_name=None,
            is_rolling=None,
            totlerate_fail_count=None,
            service_name=None,
            comment=None,
            custom_params=None,
            interval=None,
            host_id_list=None,
            turn_on_maintenance_mode=None):
        api_request = APIRequest('RunClusterServiceAction', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ExecuteStrategy": execute_strategy,
            "HostGroupIdList": list_of_host_group_id_list,
            "ResourceOwnerId": resource_owner_id,
            "OnlyRestartStaleConfigNodes": only_restart_stale_config_nodes,
            "NodeCountPerBatch": node_count_per_batch,
            "ClusterId": cluster_id,
            "CustomCommand": custom_command,
            "ComponentNameList": component_name_list,
            "RegionId": region_id,
            "ServiceActionName": service_action_name,
            "IsRolling": is_rolling,
            "TotlerateFailCount": totlerate_fail_count,
            "ServiceName": service_name,
            "Comment": comment,
            "CustomParams": custom_params,
            "Interval": interval,
            "HostIdList": host_id_list,
            "TurnOnMaintenanceMode": turn_on_maintenance_mode}
        repeat_info = {"HostGroupIdList": ('HostGroupIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_cluster_service_config(
            self,
            refresh_host_config=None,
            resource_owner_id=None,
            config_type=None,
            host_instance_id=None,
            group_id=None,
            cluster_id=None,
            custom_config_params=None,
            region_id=None,
            service_name=None,
            comment=None,
            list_of_gateway_cluster_id_list=None,
            config_params=None):
        api_request = APIRequest('ModifyClusterServiceConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RefreshHostConfig": refresh_host_config,
            "ResourceOwnerId": resource_owner_id,
            "ConfigType": config_type,
            "HostInstanceId": host_instance_id,
            "GroupId": group_id,
            "ClusterId": cluster_id,
            "CustomConfigParams": custom_config_params,
            "RegionId": region_id,
            "ServiceName": service_name,
            "Comment": comment,
            "GatewayClusterIdList": list_of_gateway_cluster_id_list,
            "ConfigParams": config_params}
        repeat_info = {"GatewayClusterIdList": ('GatewayClusterIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_required_service(
            self,
            resource_owner_id=None,
            region_id=None,
            emr_version=None,
            service_name_list=None):
        api_request = APIRequest('ListRequiredService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "EmrVersion": emr_version,
            "ServiceNameList": service_name_list}
        return self._handle_request(api_request).result

    def list_cluster_service(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('ListClusterService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_cluster_operation_host_task(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            operation_id=None,
            host_id=None,
            cluster_id=None,
            page_number=None,
            status=None):
        api_request = APIRequest('ListClusterOperationHostTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "OperationId": operation_id,
            "HostId": host_id,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "Status": status}
        return self._handle_request(api_request).result

    def list_cluster_operation_host(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            operation_id=None,
            cluster_id=None,
            page_number=None,
            status=None):
        api_request = APIRequest('ListClusterOperationHost', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "OperationId": operation_id,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "Status": status}
        return self._handle_request(api_request).result

    def list_cluster_operation(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            service_name=None,
            cluster_id=None,
            page_number=None,
            status=None):
        api_request = APIRequest('ListClusterOperation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ServiceName": service_name,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "Status": status}
        return self._handle_request(api_request).result

    def list_cluster_host_component(
            self,
            resource_owner_id=None,
            host_name=None,
            host_instance_id=None,
            region_id=None,
            page_size=None,
            component_name=None,
            service_name=None,
            cluster_id=None,
            host_role=None,
            page_number=None,
            component_status=None):
        api_request = APIRequest('ListClusterHostComponent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HostName": host_name,
            "HostInstanceId": host_instance_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "ComponentName": component_name,
            "ServiceName": service_name,
            "ClusterId": cluster_id,
            "HostRole": host_role,
            "PageNumber": page_number,
            "ComponentStatus": component_status}
        return self._handle_request(api_request).result

    def list_cluster_host(
            self,
            resource_owner_id=None,
            host_instance_id=None,
            list_of_status_list=None,
            private_ip=None,
            component_name=None,
            public_ip=None,
            cluster_id=None,
            page_number=None,
            host_name=None,
            group_type=None,
            region_id=None,
            host_group_id=None,
            page_size=None):
        api_request = APIRequest('ListClusterHost', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HostInstanceId": host_instance_id,
            "StatusList": list_of_status_list,
            "PrivateIp": private_ip,
            "ComponentName": component_name,
            "PublicIp": public_ip,
            "ClusterId": cluster_id,
            "PageNumber": page_number,
            "HostName": host_name,
            "GroupType": group_type,
            "RegionId": region_id,
            "HostGroupId": host_group_id,
            "PageSize": page_size}
        repeat_info = {"StatusList": ('StatusList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_cluster_service_config_history(
            self,
            resource_owner_id=None,
            region_id=None,
            service_name=None,
            cluster_id=None,
            config_version=None):
        api_request = APIRequest('DescribeClusterServiceConfigHistory',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ServiceName": service_name,
            "ClusterId": cluster_id,
            "ConfigVersion": config_version}
        return self._handle_request(api_request).result

    def describe_cluster_service_config(
            self,
            resource_owner_id=None,
            host_instance_id=None,
            tag_value=None,
            region_id=None,
            group_id=None,
            service_name=None,
            cluster_id=None,
            config_version=None):
        api_request = APIRequest('DescribeClusterServiceConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HostInstanceId": host_instance_id,
            "TagValue": tag_value,
            "RegionId": region_id,
            "GroupId": group_id,
            "ServiceName": service_name,
            "ClusterId": cluster_id,
            "ConfigVersion": config_version}
        return self._handle_request(api_request).result

    def describe_cluster_service(
            self,
            resource_owner_id=None,
            region_id=None,
            service_name=None,
            cluster_id=None):
        api_request = APIRequest('DescribeClusterService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ServiceName": service_name,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_cluster_operation_host_task_log(
            self,
            resource_owner_id=None,
            region_id=None,
            operation_id=None,
            host_id=None,
            cluster_id=None,
            task_id=None,
            status=None):
        api_request = APIRequest('DescribeClusterOperationHostTaskLog',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "OperationId": operation_id,
            "HostId": host_id,
            "ClusterId": cluster_id,
            "TaskId": task_id,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_cluster_basic_info(self, resource_owner_id=None, region_id=None, cluster_id=None):
        api_request = APIRequest('DescribeClusterBasicInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def add_cluster_service(
            self,
            resource_owner_id=None,
            region_id=None,
            list_of_service=None,
            comment=None,
            cluster_id=None):
        api_request = APIRequest('AddClusterService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Service": list_of_service,
            "Comment": comment,
            "ClusterId": cluster_id}
        repeat_info = {"Service": ('Service', 'list', 'dict', [('ServiceName', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def cancel_order(self, resource_owner_id=None, region_id=None, cluster_id=None):
        api_request = APIRequest('CancelOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def run_note_paragraphs(self, resource_owner_id=None, region_id=None, note_id=None):
        api_request = APIRequest('RunNoteParagraphs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "NoteId": note_id}
        return self._handle_request(api_request).result

    def metastore_search_tables(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            table_name=None):
        api_request = APIRequest('MetastoreSearchTables', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "TableName": table_name}
        return self._handle_request(api_request).result

    def metastore_list_tables(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            page_size=None,
            table_id=None,
            database_id=None,
            table_name=None,
            page_number=None,
            fuzzy_table_name=None):
        api_request = APIRequest('MetastoreListTables', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "PageSize": page_size,
            "TableId": table_id,
            "DatabaseId": database_id,
            "TableName": table_name,
            "PageNumber": page_number,
            "FuzzyTableName": fuzzy_table_name}
        return self._handle_request(api_request).result

    def metastore_list_databases(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            page_size=None,
            fuzzy_database_name=None,
            page_number=None):
        api_request = APIRequest('MetastoreListDatabases', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "PageSize": page_size,
            "FuzzyDatabaseName": fuzzy_database_name,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def metastore_drop_table(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            table_id=None,
            table_name=None,
            database_id=None):
        api_request = APIRequest('MetastoreDropTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "TableId": table_id,
            "TableName": table_name,
            "DatabaseId": database_id}
        return self._handle_request(api_request).result

    def metastore_drop_database(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            database_id=None):
        api_request = APIRequest('MetastoreDropDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "DatabaseId": database_id}
        return self._handle_request(api_request).result

    def metastore_describe_table(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            id_=None,
            table_name=None,
            database_id=None):
        api_request = APIRequest('MetastoreDescribeTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "Id": id_,
            "TableName": table_name,
            "DatabaseId": database_id}
        return self._handle_request(api_request).result

    def metastore_describe_database(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            id_=None):
        api_request = APIRequest('MetastoreDescribeDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def metastore_data_preview(
            self,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            table_name=None):
        api_request = APIRequest('MetastoreDataPreview', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "TableName": table_name}
        return self._handle_request(api_request).result

    def metastore_create_table(
            self,
            resource_owner_id=None,
            field_delimiter=None,
            list_of_column=None,
            create_with=None,
            list_of_partition=None,
            db_name=None,
            region_id=None,
            create_sql=None,
            comment=None,
            location_uri=None,
            table_name=None,
            database_id=None):
        api_request = APIRequest('MetastoreCreateTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "FieldDelimiter": field_delimiter,
            "Column": list_of_column,
            "CreateWith": create_with,
            "Partition": list_of_partition,
            "DbName": db_name,
            "RegionId": region_id,
            "CreateSql": create_sql,
            "Comment": comment,
            "LocationUri": location_uri,
            "TableName": table_name,
            "DatabaseId": database_id}
        repeat_info = {"Column": ('Column', 'list', 'dict', [('Name', 'str', None, None),
                                                             ('Comment', 'str', None, None),
                                                             ('Type', 'str', None, None),
                                                             ]),
                       "Partition": ('Partition', 'list', 'dict', [('Name', 'str', None, None),
                                                                   ('Comment', 'str', None, None),
                                                                   ('Type', 'str', None, None),
                                                                   ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def metastore_create_database(
            self,
            db_source=None,
            resource_owner_id=None,
            db_name=None,
            region_id=None,
            data_source_id=None,
            description=None,
            comment=None,
            location_uri=None,
            cluster_biz_id=None):
        api_request = APIRequest('MetastoreCreateDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DbSource": db_source,
            "ResourceOwnerId": resource_owner_id,
            "DbName": db_name,
            "RegionId": region_id,
            "DataSourceId": data_source_id,
            "Description": description,
            "Comment": comment,
            "LocationUri": location_uri,
            "ClusterBizId": cluster_biz_id}
        return self._handle_request(api_request).result

    def stop_paragraph(self, resource_owner_id=None, region_id=None, note_id=None, id_=None):
        api_request = APIRequest('StopParagraph', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "NoteId": note_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def run_paragraph(
            self,
            resource_owner_id=None,
            region_id=None,
            note_id=None,
            id_=None,
            text=None):
        api_request = APIRequest('RunParagraph', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "NoteId": note_id,
            "Id": id_,
            "Text": text}
        return self._handle_request(api_request).result

    def describe_paragraph(self, resource_owner_id=None, region_id=None, note_id=None, id_=None):
        api_request = APIRequest('DescribeParagraph', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "NoteId": note_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def delete_paragraph(self, resource_owner_id=None, region_id=None, note_id=None, id_=None):
        api_request = APIRequest('DeleteParagraph', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "NoteId": note_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def delete_note(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DeleteNote', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def save_paragraph(
            self,
            resource_owner_id=None,
            region_id=None,
            note_id=None,
            id_=None,
            text=None):
        api_request = APIRequest('SaveParagraph', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "NoteId": note_id,
            "Id": id_,
            "Text": text}
        return self._handle_request(api_request).result

    def retry_execution_plan(
            self,
            resource_owner_id=None,
            region_id=None,
            execution_plan_work_node_ids=None,
            id_=None):
        api_request = APIRequest('RetryExecutionPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ExecutionPlanWorkNodeIds": execution_plan_work_node_ids,
            "Id": id_}
        return self._handle_request(api_request).result

    def list_notes(self, resource_owner_id=None, region_id=None):
        api_request = APIRequest('ListNotes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def detach_cluster_for_note(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DetachClusterForNote', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def describe_note(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DescribeNote', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def create_paragraph(self, resource_owner_id=None, region_id=None, note_id=None, text=None):
        api_request = APIRequest('CreateParagraph', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "NoteId": note_id,
            "Text": text}
        return self._handle_request(api_request).result

    def create_note(
            self,
            resource_owner_id=None,
            region_id=None,
            name=None,
            cluster_id=None,
            type_=None):
        api_request = APIRequest('CreateNote', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "ClusterId": cluster_id,
            "Type": type_}
        return self._handle_request(api_request).result

    def attach_cluster_for_note(
            self,
            resource_owner_id=None,
            region_id=None,
            id_=None,
            cluster_id=None):
        api_request = APIRequest('AttachClusterForNote', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def modify_execution_plan_schedule_info(
            self,
            resource_owner_id=None,
            time_interval=None,
            region_id=None,
            day_of_week=None,
            id_=None,
            start_time=None,
            strategy=None,
            time_unit=None,
            day_of_month=None):
        api_request = APIRequest('ModifyExecutionPlanScheduleInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TimeInterval": time_interval,
            "RegionId": region_id,
            "DayOfWeek": day_of_week,
            "Id": id_,
            "StartTime": start_time,
            "Strategy": strategy,
            "TimeUnit": time_unit,
            "DayOfMonth": day_of_month}
        return self._handle_request(api_request).result

    def modify_execution_plan_job_info(
            self,
            resource_owner_id=None,
            region_id=None,
            id_=None,
            list_of_job_id_list=None):
        api_request = APIRequest('ModifyExecutionPlanJobInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_,
            "JobIdList": list_of_job_id_list}
        repeat_info = {"JobIdList": ('JobIdList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_execution_plan_cluster_info(
            self,
            resource_owner_id=None,
            log_path=None,
            cluster_name=None,
            configurations=None,
            io_optimized=None,
            security_group_id=None,
            eas_enable=None,
            create_cluster_on_demand=None,
            list_of_bootstrap_action=None,
            region_id=None,
            use_local_meta_db=None,
            emr_ver=None,
            id_=None,
            is_open_public_ip=None,
            cluster_id=None,
            instance_generation=None,
            cluster_type=None,
            vswitch_id=None,
            list_of_option_soft_ware_list=None,
            vpc_id=None,
            net_type=None,
            list_of_ecs_order=None,
            zone_id=None,
            high_availability_enable=None,
            log_enable=None):
        api_request = APIRequest('ModifyExecutionPlanClusterInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "LogPath": log_path,
            "ClusterName": cluster_name,
            "Configurations": configurations,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "EasEnable": eas_enable,
            "CreateClusterOnDemand": create_cluster_on_demand,
            "BootstrapAction": list_of_bootstrap_action,
            "RegionId": region_id,
            "UseLocalMetaDb": use_local_meta_db,
            "EmrVer": emr_ver,
            "Id": id_,
            "IsOpenPublicIp": is_open_public_ip,
            "ClusterId": cluster_id,
            "InstanceGeneration": instance_generation,
            "ClusterType": cluster_type,
            "VSwitchId": vswitch_id,
            "OptionSoftWareList": list_of_option_soft_ware_list,
            "VpcId": vpc_id,
            "NetType": net_type,
            "EcsOrder": list_of_ecs_order,
            "ZoneId": zone_id,
            "HighAvailabilityEnable": high_availability_enable,
            "LogEnable": log_enable}
        repeat_info = {"BootstrapAction": ('BootstrapAction',
                                           'list',
                                           'dict',
                                           [('Path',
                                             'str',
                                             None,
                                             None),
                                            ('Arg',
                                             'str',
                                             None,
                                             None),
                                               ('Name',
                                                'str',
                                                None,
                                                None),
                                            ]),
                       "OptionSoftWareList": ('OptionSoftWareList',
                                              'list',
                                              'str',
                                              None),
                       "EcsOrder": ('EcsOrder',
                                    'list',
                                    'dict',
                                    [('NodeType',
                                      'str',
                                      None,
                                      None),
                                     ('DiskCount',
                                        'str',
                                        None,
                                        None),
                                        ('NodeCount',
                                         'str',
                                         None,
                                         None),
                                        ('DiskCapacity',
                                         'str',
                                         None,
                                         None),
                                        ('Index',
                                         'str',
                                         None,
                                         None),
                                        ('InstanceType',
                                         'str',
                                         None,
                                         None),
                                        ('DiskType',
                                         'str',
                                         None,
                                         None),
                                     ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_execution_plan_basic_info(
            self,
            resource_owner_id=None,
            region_id=None,
            name=None,
            id_=None,
            cluster_id=None):
        api_request = APIRequest('ModifyExecutionPlanBasicInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Id": id_,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_job_execution_instance_trend(self, resource_owner_id=None, region_id=None):
        api_request = APIRequest('ListJobExecutionInstanceTrend', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def list_failure_job_execution_instances(
            self, resource_owner_id=None, region_id=None, count=None):
        api_request = APIRequest('ListFailureJobExecutionInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Count": count}
        return self._handle_request(api_request).result

    def list_execution_plan_instance_trend(self, resource_owner_id=None, region_id=None):
        api_request = APIRequest('ListExecutionPlanInstanceTrend', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def list_cluster_scripts(self, resource_owner_id=None, region_id=None, cluster_id=None):
        api_request = APIRequest('ListClusterScripts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_cluster_script(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DescribeClusterScript', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def delete_cluster_script(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DeleteClusterScript', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def create_cluster_script(
            self,
            args=None,
            path=None,
            resource_owner_id=None,
            region_id=None,
            name=None,
            cluster_id=None,
            node_id_list=None):
        api_request = APIRequest('CreateClusterScript', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Args": args,
            "Path": path,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "ClusterId": cluster_id,
            "NodeIdList": node_id_list}
        return self._handle_request(api_request).result

    def kill_execution_plan_instance(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('KillExecutionPlanInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def suspend_execution_plan_scheduler(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('SuspendExecutionPlanScheduler', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def run_execution_plan(self, resource_owner_id=None, region_id=None, arguments=None, id_=None):
        api_request = APIRequest('RunExecutionPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Arguments": arguments,
            "Id": id_}
        return self._handle_request(api_request).result

    def resume_execution_plan_scheduler(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('ResumeExecutionPlanScheduler', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def release_cluster(self, resource_owner_id=None, region_id=None, force_release=None, id_=None):
        api_request = APIRequest('ReleaseCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ForceRelease": force_release,
            "Id": id_}
        return self._handle_request(api_request).result

    def modify_job(
            self,
            run_parameter=None,
            retry_interval=None,
            resource_owner_id=None,
            region_id=None,
            name=None,
            id_=None,
            type_=None,
            max_retry=None,
            fail_act=None):
        api_request = APIRequest('ModifyJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RunParameter": run_parameter,
            "RetryInterval": retry_interval,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Id": id_,
            "Type": type_,
            "MaxRetry": max_retry,
            "FailAct": fail_act}
        return self._handle_request(api_request).result

    def modify_execution_plan(
            self,
            resource_owner_id=None,
            log_path=None,
            time_interval=None,
            cluster_name=None,
            configurations=None,
            io_optimized=None,
            security_group_id=None,
            eas_enable=None,
            create_cluster_on_demand=None,
            start_time=None,
            list_of_job_id_list=None,
            day_of_month=None,
            list_of_bootstrap_action=None,
            region_id=None,
            use_local_meta_db=None,
            emr_ver=None,
            id_=None,
            user_defined_emr_ecs_role=None,
            is_open_public_ip=None,
            execution_plan_version=None,
            cluster_id=None,
            time_unit=None,
            instance_generation=None,
            cluster_type=None,
            vswitch_id=None,
            list_of_option_soft_ware_list=None,
            vpc_id=None,
            net_type=None,
            workflow_definition=None,
            list_of_ecs_order=None,
            name=None,
            zone_id=None,
            day_of_week=None,
            use_custom_hive_meta_db=None,
            strategy=None,
            list_of_config=None,
            high_availability_enable=None,
            init_custom_hive_meta_db=None,
            log_enable=None):
        api_request = APIRequest('ModifyExecutionPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "LogPath": log_path,
            "TimeInterval": time_interval,
            "ClusterName": cluster_name,
            "Configurations": configurations,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "EasEnable": eas_enable,
            "CreateClusterOnDemand": create_cluster_on_demand,
            "StartTime": start_time,
            "JobIdList": list_of_job_id_list,
            "DayOfMonth": day_of_month,
            "BootstrapAction": list_of_bootstrap_action,
            "RegionId": region_id,
            "UseLocalMetaDb": use_local_meta_db,
            "EmrVer": emr_ver,
            "Id": id_,
            "UserDefinedEmrEcsRole": user_defined_emr_ecs_role,
            "IsOpenPublicIp": is_open_public_ip,
            "ExecutionPlanVersion": execution_plan_version,
            "ClusterId": cluster_id,
            "TimeUnit": time_unit,
            "InstanceGeneration": instance_generation,
            "ClusterType": cluster_type,
            "VSwitchId": vswitch_id,
            "OptionSoftWareList": list_of_option_soft_ware_list,
            "VpcId": vpc_id,
            "NetType": net_type,
            "WorkflowDefinition": workflow_definition,
            "EcsOrder": list_of_ecs_order,
            "Name": name,
            "ZoneId": zone_id,
            "DayOfWeek": day_of_week,
            "UseCustomHiveMetaDB": use_custom_hive_meta_db,
            "Strategy": strategy,
            "Config": list_of_config,
            "HighAvailabilityEnable": high_availability_enable,
            "InitCustomHiveMetaDB": init_custom_hive_meta_db,
            "LogEnable": log_enable}
        repeat_info = {"JobIdList": ('JobIdList', 'list', 'str', None),
                       "BootstrapAction": ('BootstrapAction', 'list', 'dict', [('Path', 'str', None, None),
                                                                               ('Arg', 'str', None, None),
                                                                               ('Name', 'str', None, None),
                                                                               ]),
                       "OptionSoftWareList": ('OptionSoftWareList', 'list', 'str', None),
                       "EcsOrder": ('EcsOrder', 'list', 'dict', [('NodeType', 'str', None, None),
                                                                 ('DiskCount', 'str', None, None),
                                                                 ('NodeCount', 'str', None, None),
                                                                 ('DiskCapacity', 'str', None, None),
                                                                 ('Index', 'str', None, None),
                                                                 ('InstanceType', 'str', None, None),
                                                                 ('DiskType', 'str', None, None),
                                                                 ]),
                       "Config": ('Config', 'list', 'dict', [('ConfigKey', 'str', None, None),
                                                             ('FileName', 'str', None, None),
                                                             ('Encrypt', 'str', None, None),
                                                             ('Replace', 'str', None, None),
                                                             ('ConfigValue', 'str', None, None),
                                                             ('ServiceName', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_cluster_name(self, resource_owner_id=None, region_id=None, name=None, id_=None):
        api_request = APIRequest('ModifyClusterName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Id": id_}
        return self._handle_request(api_request).result

    def list_jobs(
            self,
            resource_owner_id=None,
            region_id=None,
            page_size=None,
            query_string=None,
            is_desc=None,
            page_number=None,
            query_type=None):
        api_request = APIRequest('ListJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "QueryString": query_string,
            "IsDesc": is_desc,
            "PageNumber": page_number,
            "QueryType": query_type}
        return self._handle_request(api_request).result

    def list_job_instance_workers(
            self,
            resource_owner_id=None,
            region_id=None,
            job_instance_id=None):
        api_request = APIRequest('ListJobInstanceWorkers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "JobInstanceId": job_instance_id}
        return self._handle_request(api_request).result

    def list_job_execution_instances(
            self,
            resource_owner_id=None,
            execution_plan_instance_id=None,
            region_id=None,
            page_size=None,
            is_desc=None,
            page_number=None):
        api_request = APIRequest('ListJobExecutionInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ExecutionPlanInstanceId": execution_plan_instance_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "IsDesc": is_desc,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_execution_plans(
            self,
            job_id=None,
            resource_owner_id=None,
            list_of_status_list=None,
            region_id=None,
            page_size=None,
            query_string=None,
            cluster_id=None,
            is_desc=None,
            strategy=None,
            page_number=None,
            query_type=None):
        api_request = APIRequest('ListExecutionPlans', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "StatusList": list_of_status_list,
            "RegionId": region_id,
            "PageSize": page_size,
            "QueryString": query_string,
            "ClusterId": cluster_id,
            "IsDesc": is_desc,
            "Strategy": strategy,
            "PageNumber": page_number,
            "QueryType": query_type}
        repeat_info = {"StatusList": ('StatusList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_execution_plan_instances(
            self,
            only_last_instance=None,
            resource_owner_id=None,
            list_of_execution_plan_id_list=None,
            list_of_status_list=None,
            region_id=None,
            page_size=None,
            is_desc=None,
            page_number=None):
        api_request = APIRequest('ListExecutionPlanInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OnlyLastInstance": only_last_instance,
            "ResourceOwnerId": resource_owner_id,
            "ExecutionPlanIdList": list_of_execution_plan_id_list,
            "StatusList": list_of_status_list,
            "RegionId": region_id,
            "PageSize": page_size,
            "IsDesc": is_desc,
            "PageNumber": page_number}
        repeat_info = {"ExecutionPlanIdList": ('ExecutionPlanIdList', 'list', 'str', None),
                       "StatusList": ('StatusList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_clusters(
            self,
            resource_owner_id=None,
            list_of_status_list=None,
            region_id=None,
            page_size=None,
            list_of_cluster_type_list=None,
            is_desc=None,
            create_type=None,
            deposit_type=None,
            default_status=None,
            page_number=None,
            machine_type=None):
        api_request = APIRequest('ListClusters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "StatusList": list_of_status_list,
            "RegionId": region_id,
            "PageSize": page_size,
            "ClusterTypeList": list_of_cluster_type_list,
            "IsDesc": is_desc,
            "CreateType": create_type,
            "DepositType": deposit_type,
            "DefaultStatus": default_status,
            "PageNumber": page_number,
            "MachineType": machine_type}
        repeat_info = {"StatusList": ('StatusList', 'list', 'str', None),
                       "ClusterTypeList": ('ClusterTypeList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def kill_execution_job_instance(
            self,
            resource_owner_id=None,
            region_id=None,
            job_instance_id=None):
        api_request = APIRequest('KillExecutionJobInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "JobInstanceId": job_instance_id}
        return self._handle_request(api_request).result

    def describe_job(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DescribeJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def describe_execution_plan(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DescribeExecutionPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def delete_job(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DeleteJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def delete_execution_plan(self, resource_owner_id=None, region_id=None, id_=None):
        api_request = APIRequest('DeleteExecutionPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Id": id_}
        return self._handle_request(api_request).result

    def create_job(
            self,
            run_parameter=None,
            retry_interval=None,
            resource_owner_id=None,
            region_id=None,
            name=None,
            type_=None,
            max_retry=None,
            fail_act=None):
        api_request = APIRequest('CreateJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RunParameter": run_parameter,
            "RetryInterval": retry_interval,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "Name": name,
            "Type": type_,
            "MaxRetry": max_retry,
            "FailAct": fail_act}
        return self._handle_request(api_request).result

    def create_execution_plan(
            self,
            resource_owner_id=None,
            time_interval=None,
            log_path=None,
            cluster_name=None,
            configurations=None,
            io_optimized=None,
            security_group_id=None,
            eas_enable=None,
            create_cluster_on_demand=None,
            start_time=None,
            list_of_job_id_list=None,
            day_of_month=None,
            list_of_bootstrap_action=None,
            region_id=None,
            use_local_meta_db=None,
            emr_ver=None,
            user_defined_emr_ecs_role=None,
            is_open_public_ip=None,
            cluster_id=None,
            time_unit=None,
            instance_generation=None,
            cluster_type=None,
            vswitch_id=None,
            list_of_option_soft_ware_list=None,
            vpc_id=None,
            net_type=None,
            list_of_ecs_order=None,
            workflow_definition=None,
            name=None,
            day_of_week=None,
            zone_id=None,
            use_custom_hive_meta_db=None,
            strategy=None,
            list_of_config=None,
            high_availability_enable=None,
            init_custom_hive_meta_db=None,
            log_enable=None):
        api_request = APIRequest('CreateExecutionPlan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TimeInterval": time_interval,
            "LogPath": log_path,
            "ClusterName": cluster_name,
            "Configurations": configurations,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "EasEnable": eas_enable,
            "CreateClusterOnDemand": create_cluster_on_demand,
            "StartTime": start_time,
            "JobIdList": list_of_job_id_list,
            "DayOfMonth": day_of_month,
            "BootstrapAction": list_of_bootstrap_action,
            "RegionId": region_id,
            "UseLocalMetaDb": use_local_meta_db,
            "EmrVer": emr_ver,
            "UserDefinedEmrEcsRole": user_defined_emr_ecs_role,
            "IsOpenPublicIp": is_open_public_ip,
            "ClusterId": cluster_id,
            "TimeUnit": time_unit,
            "InstanceGeneration": instance_generation,
            "ClusterType": cluster_type,
            "VSwitchId": vswitch_id,
            "OptionSoftWareList": list_of_option_soft_ware_list,
            "VpcId": vpc_id,
            "NetType": net_type,
            "EcsOrder": list_of_ecs_order,
            "WorkflowDefinition": workflow_definition,
            "Name": name,
            "DayOfWeek": day_of_week,
            "ZoneId": zone_id,
            "UseCustomHiveMetaDB": use_custom_hive_meta_db,
            "Strategy": strategy,
            "Config": list_of_config,
            "HighAvailabilityEnable": high_availability_enable,
            "InitCustomHiveMetaDB": init_custom_hive_meta_db,
            "LogEnable": log_enable}
        repeat_info = {"JobIdList": ('JobIdList', 'list', 'str', None),
                       "BootstrapAction": ('BootstrapAction', 'list', 'dict', [('Path', 'str', None, None),
                                                                               ('Arg', 'str', None, None),
                                                                               ('Name', 'str', None, None),
                                                                               ]),
                       "OptionSoftWareList": ('OptionSoftWareList', 'list', 'str', None),
                       "EcsOrder": ('EcsOrder', 'list', 'dict', [('NodeType', 'str', None, None),
                                                                 ('DiskCount', 'str', None, None),
                                                                 ('NodeCount', 'str', None, None),
                                                                 ('DiskCapacity', 'str', None, None),
                                                                 ('Index', 'str', None, None),
                                                                 ('InstanceType', 'str', None, None),
                                                                 ('DiskType', 'str', None, None),
                                                                 ]),
                       "Config": ('Config', 'list', 'dict', [('ConfigKey', 'str', None, None),
                                                             ('FileName', 'str', None, None),
                                                             ('Encrypt', 'str', None, None),
                                                             ('Replace', 'str', None, None),
                                                             ('ConfigValue', 'str', None, None),
                                                             ('ServiceName', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result
