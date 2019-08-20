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


class PolardbClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'polardb'
        self.api_version = '2017-08-01'
        self.location_service_code = 'polardb'
        self.location_endpoint_type = 'openAPI'

    def continue_db_cluster_migration(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ContinueDBClusterMigration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def abort_db_cluster_migration(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('AbortDBClusterMigration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def unlock_db_cluster_deletion(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('UnlockDBClusterDeletion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def lock_db_cluster_deletion(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('LockDBClusterDeletion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_cluster_migration(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBClusterMigration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def close_db_cluster_migration(
            self,
            resource_owner_id=None,
            continue_enable_binlog=None,
            security_token=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CloseDBClusterMigration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ContinueEnableBinlog": continue_enable_binlog,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_cluster_migration(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            source_rdsdb_instance_id=None,
            new_master_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBClusterMigration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "SourceRDSDBInstanceId": source_rdsdb_instance_id,
            "NewMasterInstanceId": new_master_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_auto_renew_attribute(
            self,
            duration=None,
            resource_owner_id=None,
            period_unit=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            renewal_status=None,
            owner_id=None,
            db_cluster_ids=None):
        api_request = APIRequest('ModifyAutoRenewAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "ResourceOwnerId": resource_owner_id,
            "PeriodUnit": period_unit,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "RenewalStatus": renewal_status,
            "OwnerId": owner_id,
            "DBClusterIds": db_cluster_ids}
        return self._handle_request(api_request).result

    def modify_db_node_class(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            db_cluster_id=None,
            owner_account=None,
            modify_type=None,
            db_node_target_class=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBNodeClass', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "ModifyType": modify_type,
            "DBNodeTargetClass": db_node_target_class,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_auto_renew_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None,
            db_cluster_ids=None):
        api_request = APIRequest('DescribeAutoRenewAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "DBClusterIds": db_cluster_ids}
        return self._handle_request(api_request).result

    def create_db_nodes(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None,
            list_of_db_node=None):
        api_request = APIRequest('CreateDBNodes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "DBNode": list_of_db_node}
        repeat_info = {"DBNode": ('DBNode', 'list', 'dict', [('TargetClass', 'str', None, None),
                                                             ('ZoneId', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_db_nodes(
            self,
            resource_owner_id=None,
            list_of_db_node_id=None,
            resource_owner_account=None,
            client_token=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteDBNodes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBNodeId": list_of_db_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        repeat_info = {"DBNodeId": ('DBNodeId', 'list', 'str', None),
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

    def modify_db_endpoint_address(
            self,
            resource_owner_id=None,
            connection_string_prefix=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            net_type=None,
            db_endpoint_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBEndpointAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ConnectionStringPrefix": connection_string_prefix,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "NetType": net_type,
            "DBEndpointId": db_endpoint_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_description(
            self,
            resource_owner_id=None,
            db_name=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            db_description=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "DBDescription": db_description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_cluster_parameters(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            effective_time=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None,
            parameters=None):
        api_request = APIRequest('ModifyDBClusterParameters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "EffectiveTime": effective_time,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Parameters": parameters}
        return self._handle_request(api_request).result

    def modify_db_cluster_endpoint(
            self,
            auto_add_new_nodes=None,
            resource_owner_id=None,
            nodes=None,
            read_write_mode=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            db_endpoint_id=None,
            endpoint_config=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBClusterEndpoint', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AutoAddNewNodes": auto_add_new_nodes,
            "ResourceOwnerId": resource_owner_id,
            "Nodes": nodes,
            "ReadWriteMode": read_write_mode,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "DBEndpointId": db_endpoint_id,
            "EndpointConfig": endpoint_config,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_account_password(
            self,
            resource_owner_id=None,
            account_name=None,
            new_account_password=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyAccountPassword', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "NewAccountPassword": new_account_password,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_cluster_parameters(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBClusterParameters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_cluster_endpoints(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            db_endpoint_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBClusterEndpoints', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "DBEndpointId": db_endpoint_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_db_endpoint_address(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            net_type=None,
            db_endpoint_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteDBEndpointAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "NetType": net_type,
            "DBEndpointId": db_endpoint_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_db_cluster_endpoint(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            db_endpoint_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteDBClusterEndpoint', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "DBEndpointId": db_endpoint_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_db_endpoint_address(
            self,
            resource_owner_id=None,
            connection_string_prefix=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            net_type=None,
            db_endpoint_id=None,
            owner_id=None):
        api_request = APIRequest('CreateDBEndpointAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ConnectionStringPrefix": connection_string_prefix,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "NetType": net_type,
            "DBEndpointId": db_endpoint_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_db_cluster_endpoint(
            self,
            auto_add_new_nodes=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            db_cluster_id=None,
            owner_account=None,
            endpoint_config=None,
            owner_id=None,
            nodes=None,
            read_write_mode=None,
            endpoint_type=None):
        api_request = APIRequest('CreateDBClusterEndpoint', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AutoAddNewNodes": auto_add_new_nodes,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "EndpointConfig": endpoint_config,
            "OwnerId": owner_id,
            "Nodes": nodes,
            "ReadWriteMode": read_write_mode,
            "EndpointType": endpoint_type}
        return self._handle_request(api_request).result

    def restart_db_node(
            self,
            resource_owner_id=None,
            db_node_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('RestartDBNode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBNodeId": db_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_cluster_access_whitelist(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            security_ips=None,
            db_cluster_ip_array_name=None,
            owner_id=None,
            db_cluster_ip_array_attribute=None):
        api_request = APIRequest('ModifyDBClusterAccessWhitelist', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "SecurityIps": security_ips,
            "DBClusterIPArrayName": db_cluster_ip_array_name,
            "OwnerId": owner_id,
            "DBClusterIPArrayAttribute": db_cluster_ip_array_attribute}
        return self._handle_request(api_request).result

    def describe_db_cluster_access_whitelist(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBClusterAccessWhitelist', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_cluster_maintain_time(
            self,
            maintain_time=None,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBClusterMaintainTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MaintainTime": maintain_time,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def revoke_account_privilege(
            self,
            resource_owner_id=None,
            account_name=None,
            db_name=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('RevokeAccountPrivilege', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def reset_account(
            self,
            resource_owner_id=None,
            account_password=None,
            account_name=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ResetAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountPassword": account_password,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def grant_account_privilege(
            self,
            resource_owner_id=None,
            account_name=None,
            db_name=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None,
            account_privilege=None):
        api_request = APIRequest('GrantAccountPrivilege', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AccountPrivilege": account_privilege}
        return self._handle_request(api_request).result

    def describe_databases(
            self,
            resource_owner_id=None,
            db_name=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeDatabases', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_database(
            self,
            resource_owner_id=None,
            db_name=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_account(
            self,
            resource_owner_id=None,
            account_name=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_database(
            self,
            resource_owner_id=None,
            db_name=None,
            account_name=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            db_description=None,
            owner_id=None,
            character_set_name=None,
            account_privilege=None):
        api_request = APIRequest('CreateDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBName": db_name,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "DBDescription": db_description,
            "OwnerId": owner_id,
            "CharacterSetName": character_set_name,
            "AccountPrivilege": account_privilege}
        return self._handle_request(api_request).result

    def delete_backup(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            backup_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "BackupId": backup_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_cluster_description(
            self,
            resource_owner_id=None,
            db_cluster_description=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBClusterDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBClusterDescription": db_cluster_description,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_account_description(
            self,
            resource_owner_id=None,
            account_name=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None,
            account_description=None):
        api_request = APIRequest('ModifyAccountDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AccountDescription": account_description}
        return self._handle_request(api_request).result

    def describe_regions(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_accounts(
            self,
            resource_owner_id=None,
            account_name=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeAccounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_db_cluster(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteDBCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_db_cluster(
            self,
            resource_owner_id=None,
            db_cluster_description=None,
            period=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            owner_id=None,
            used_time=None,
            cluster_network_type=None,
            vswitch_id=None,
            db_node_class=None,
            auto_renew=None,
            engine=None,
            vpc_id=None,
            db_type=None,
            zone_id=None,
            db_version=None,
            creation_option=None,
            source_resource_id=None,
            clone_data_point=None,
            pay_type=None):
        api_request = APIRequest('CreateDBCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBClusterDescription": db_cluster_description,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "ClusterNetworkType": cluster_network_type,
            "VSwitchId": vswitch_id,
            "DBNodeClass": db_node_class,
            "AutoRenew": auto_renew,
            "Engine": engine,
            "VPCId": vpc_id,
            "DBType": db_type,
            "ZoneId": zone_id,
            "DBVersion": db_version,
            "CreationOption": creation_option,
            "SourceResourceId": source_resource_id,
            "CloneDataPoint": clone_data_point,
            "PayType": pay_type}
        return self._handle_request(api_request).result

    def create_backup(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CreateBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_account(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            account_type=None,
            owner_id=None,
            account_description=None,
            account_privilege=None,
            account_password=None,
            account_name=None,
            db_name=None):
        api_request = APIRequest('CreateAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "AccountType": account_type,
            "OwnerId": owner_id,
            "AccountDescription": account_description,
            "AccountPrivilege": account_privilege,
            "AccountPassword": account_password,
            "AccountName": account_name,
            "DBName": db_name}
        return self._handle_request(api_request).result

    def describe_backups(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            backup_id=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            backup_status=None,
            page_size=None,
            backup_mode=None):
        api_request = APIRequest('DescribeBackups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "BackupId": backup_id,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "BackupStatus": backup_status,
            "PageSize": page_size,
            "BackupMode": backup_mode}
        return self._handle_request(api_request).result

    def modify_backup_policy(
            self,
            preferred_backup_time=None,
            preferred_backup_period=None,
            backup_retention_period=None,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PreferredBackupTime": preferred_backup_time,
            "PreferredBackupPeriod": preferred_backup_period,
            "BackupRetentionPeriod": backup_retention_period,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_backup_policy(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_clusters(
            self,
            resource_owner_id=None,
            db_cluster_description=None,
            db_cluster_status=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            page_number=None,
            region_id=None,
            db_type=None,
            page_size=None,
            list_of_tag=None,
            db_cluster_ids=None):
        api_request = APIRequest('DescribeDBClusters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBClusterDescription": db_cluster_description,
            "DBClusterStatus": db_cluster_status,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "DBType": db_type,
            "PageSize": page_size,
            "Tag": list_of_tag,
            "DBClusterIds": db_cluster_ids}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_db_cluster_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_cluster_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBClusterAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBClusterId": db_cluster_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result
