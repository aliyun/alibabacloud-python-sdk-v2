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


class NASClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'NAS'
        self.api_version = '2017-06-26'
        self.location_service_code = 'nas'
        self.location_endpoint_type = 'openAPI'

    def describe_ldap_config(self, file_system_id=None):
        api_request = APIRequest('DescribeLDAPConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def modify_ldap_config(self, bind_dn=None, search_base=None, uri=None, file_system_id=None):
        api_request = APIRequest('ModifyLDAPConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BindDN": bind_dn,
            "SearchBase": search_base,
            "URI": uri,
            "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def create_ldap_config(self, bind_dn=None, search_base=None, uri=None, file_system_id=None):
        api_request = APIRequest('CreateLDAPConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BindDN": bind_dn,
            "SearchBase": search_base,
            "URI": uri,
            "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def delete_ldap_config(self, file_system_id=None):
        api_request = APIRequest('DeleteLDAPConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def describe_tags(
            self,
            page_size=None,
            list_of_tag=None,
            page_number=None,
            file_system_id=None):
        api_request = APIRequest('DescribeTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "Tag": list_of_tag,
            "PageNumber": page_number,
            "FileSystemId": file_system_id}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def remove_tags(self, list_of_tag=None, file_system_id=None):
        api_request = APIRequest('RemoveTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Tag": list_of_tag, "FileSystemId": file_system_id}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def add_tags(self, list_of_tag=None, file_system_id=None):
        api_request = APIRequest('AddTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Tag": list_of_tag, "FileSystemId": file_system_id}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def reset_file_system(self, snapshot_id=None, file_system_id=None):
        api_request = APIRequest('ResetFileSystem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"snapshotId": snapshot_id, "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def create_auto_snapshot_policy(
            self,
            time_points=None,
            retention_days=None,
            repeat_weekdays=None,
            file_system_type=None,
            auto_snapshot_policy_name=None):
        api_request = APIRequest('CreateAutoSnapshotPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TimePoints": time_points,
            "RetentionDays": retention_days,
            "RepeatWeekdays": repeat_weekdays,
            "FileSystemType": file_system_type,
            "AutoSnapshotPolicyName": auto_snapshot_policy_name}
        return self._handle_request(api_request).result

    def describe_auto_snapshot_policies(
            self,
            auto_snapshot_policy_id=None,
            page_size=None,
            file_system_type=None,
            page_number=None):
        api_request = APIRequest('DescribeAutoSnapshotPolicies', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AutoSnapshotPolicyId": auto_snapshot_policy_id,
            "PageSize": page_size,
            "FileSystemType": file_system_type,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def cancel_auto_snapshot_policy(self, file_system_ids=None):
        api_request = APIRequest('CancelAutoSnapshotPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"FileSystemIds": file_system_ids}
        return self._handle_request(api_request).result

    def apply_auto_snapshot_policy(self, auto_snapshot_policy_id=None, file_system_ids=None):
        api_request = APIRequest('ApplyAutoSnapshotPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AutoSnapshotPolicyId": auto_snapshot_policy_id,
            "FileSystemIds": file_system_ids}
        return self._handle_request(api_request).result

    def modify_auto_snapshot_policy(
            self,
            auto_snapshot_policy_id=None,
            retention_days=None,
            time_points=None,
            repeat_weekdays=None,
            auto_snapshot_policy_name=None):
        api_request = APIRequest('ModifyAutoSnapshotPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AutoSnapshotPolicyId": auto_snapshot_policy_id,
            "RetentionDays": retention_days,
            "TimePoints": time_points,
            "RepeatWeekdays": repeat_weekdays,
            "AutoSnapshotPolicyName": auto_snapshot_policy_name}
        return self._handle_request(api_request).result

    def delete_auto_snapshot_policy(self, auto_snapshot_policy_id=None):
        api_request = APIRequest('DeleteAutoSnapshotPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AutoSnapshotPolicyId": auto_snapshot_policy_id}
        return self._handle_request(api_request).result

    def delete_snapshot(self, snapshot_id=None):
        api_request = APIRequest('DeleteSnapshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SnapshotId": snapshot_id}
        return self._handle_request(api_request).result

    def create_snapshot(
            self,
            description=None,
            snapshot_name=None,
            retention_days=None,
            file_system_id=None):
        api_request = APIRequest('CreateSnapshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Description": description,
            "SnapshotName": snapshot_name,
            "RetentionDays": retention_days,
            "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def describe_snapshots(
            self,
            snapshot_type=None,
            snapshot_ids=None,
            page_size=None,
            snapshot_name=None,
            file_system_type=None,
            page_number=None,
            file_system_id=None,
            status=None):
        api_request = APIRequest('DescribeSnapshots', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SnapshotType": snapshot_type,
            "SnapshotIds": snapshot_ids,
            "PageSize": page_size,
            "SnapshotName": snapshot_name,
            "FileSystemType": file_system_type,
            "PageNumber": page_number,
            "FileSystemId": file_system_id,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_zones(self, region_id=None):
        api_request = APIRequest('DescribeZones', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id}
        return self._handle_request(api_request).result

    def create_access_group(
            self,
            description=None,
            access_group_type=None,
            access_group_name=None,
            file_system_type=None):
        api_request = APIRequest('CreateAccessGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Description": description,
            "AccessGroupType": access_group_type,
            "AccessGroupName": access_group_name,
            "FileSystemType": file_system_type}
        return self._handle_request(api_request).result

    def create_mount_target(
            self,
            vswitch_id=None,
            vpc_id=None,
            network_type=None,
            access_group_name=None,
            file_system_id=None):
        api_request = APIRequest('CreateMountTarget', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "VpcId": vpc_id,
            "NetworkType": network_type,
            "AccessGroupName": access_group_name,
            "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def create_file_system(
            self,
            zone_id=None,
            description=None,
            protocol_type=None,
            storage_type=None):
        api_request = APIRequest('CreateFileSystem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ZoneId": zone_id,
            "Description": description,
            "ProtocolType": protocol_type,
            "StorageType": storage_type}
        return self._handle_request(api_request).result

    def create_access_rule(
            self,
            rw_access_type=None,
            source_cidr_ip=None,
            user_access_type=None,
            priority=None,
            access_group_name=None,
            file_system_type=None):
        api_request = APIRequest('CreateAccessRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RWAccessType": rw_access_type,
            "SourceCidrIp": source_cidr_ip,
            "UserAccessType": user_access_type,
            "Priority": priority,
            "AccessGroupName": access_group_name,
            "FileSystemType": file_system_type}
        return self._handle_request(api_request).result

    def describe_access_rules(
            self,
            page_size=None,
            access_group_name=None,
            access_rule_id=None,
            file_system_type=None,
            page_number=None):
        api_request = APIRequest('DescribeAccessRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "AccessGroupName": access_group_name,
            "AccessRuleId": access_rule_id,
            "FileSystemType": file_system_type,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_access_groups(
            self,
            page_size=None,
            access_group_name=None,
            file_system_type=None,
            page_number=None):
        api_request = APIRequest('DescribeAccessGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "AccessGroupName": access_group_name,
            "FileSystemType": file_system_type,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_mount_target(self, mount_target_domain=None, file_system_id=None):
        api_request = APIRequest('DeleteMountTarget', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MountTargetDomain": mount_target_domain,
            "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def delete_file_system(self, file_system_id=None):
        api_request = APIRequest('DeleteFileSystem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def delete_access_rule(
            self,
            access_group_name=None,
            access_rule_id=None,
            file_system_type=None):
        api_request = APIRequest('DeleteAccessRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccessGroupName": access_group_name,
            "AccessRuleId": access_rule_id,
            "FileSystemType": file_system_type}
        return self._handle_request(api_request).result

    def delete_access_group(self, access_group_name=None, file_system_type=None):
        api_request = APIRequest('DeleteAccessGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccessGroupName": access_group_name,
            "FileSystemType": file_system_type}
        return self._handle_request(api_request).result

    def modify_access_rule(
            self,
            rw_access_type=None,
            source_cidr_ip=None,
            user_access_type=None,
            priority=None,
            access_group_name=None,
            access_rule_id=None,
            file_system_type=None):
        api_request = APIRequest('ModifyAccessRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RWAccessType": rw_access_type,
            "SourceCidrIp": source_cidr_ip,
            "UserAccessType": user_access_type,
            "Priority": priority,
            "AccessGroupName": access_group_name,
            "AccessRuleId": access_rule_id,
            "FileSystemType": file_system_type}
        return self._handle_request(api_request).result

    def modify_access_group(self, description=None, access_group_name=None, file_system_type=None):
        api_request = APIRequest('ModifyAccessGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Description": description,
            "AccessGroupName": access_group_name,
            "FileSystemType": file_system_type}
        return self._handle_request(api_request).result

    def describe_regions(self, page_size=None, file_system_type=None, page_number=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "FileSystemType": file_system_type,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_mount_targets(
            self,
            mount_target_domain=None,
            page_size=None,
            page_number=None,
            file_system_id=None):
        api_request = APIRequest('DescribeMountTargets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MountTargetDomain": mount_target_domain,
            "PageSize": page_size,
            "PageNumber": page_number,
            "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def describe_file_systems(
            self,
            vpc_id=None,
            page_size=None,
            file_system_type=None,
            page_number=None,
            file_system_id=None):
        api_request = APIRequest('DescribeFileSystems', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VpcId": vpc_id,
            "PageSize": page_size,
            "FileSystemType": file_system_type,
            "PageNumber": page_number,
            "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def modify_mount_target(
            self,
            mount_target_domain=None,
            access_group_name=None,
            file_system_id=None,
            status=None):
        api_request = APIRequest('ModifyMountTarget', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MountTargetDomain": mount_target_domain,
            "AccessGroupName": access_group_name,
            "FileSystemId": file_system_id,
            "Status": status}
        return self._handle_request(api_request).result

    def modify_file_system(self, description=None, file_system_id=None):
        api_request = APIRequest('ModifyFileSystem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Description": description, "FileSystemId": file_system_id}
        return self._handle_request(api_request).result
