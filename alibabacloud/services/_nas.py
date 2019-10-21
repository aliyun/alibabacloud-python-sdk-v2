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

import json
import time

from alibabacloud.exceptions import ClientException
from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, _create_special_resource_collection
from alibabacloud.resources.collection import _create_default_resource_collection
from alibabacloud.resources.collection import _create_sub_resource_with_page_collection
from alibabacloud.resources.collection import _create_sub_resource_without_page_collection
from alibabacloud.utils.utils import _assert_is_not_none, _new_get_key_in_response, _transfer_params


class _NASResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'nas', _client=_client)
        self.access_groups = _create_resource_collection(
            _NASAccessGroupResource, _client, _client.describe_access_groups,
            'AccessGroups.AccessGroup', 'AccessGroupName', 
        )
        self.auto_snapshot_policies = _create_resource_collection(
            _NASAutoSnapshotPolicyResource, _client, _client.describe_auto_snapshot_policies,
            'AutoSnapshotPolicies.AutoSnapshotPolicy', 'AutoSnapshotPolicyId', 
        )
        self.file_systems = _create_resource_collection(
            _NASFileSystemResource, _client, _client.describe_file_systems,
            'FileSystems.FileSystem', 'FileSystemId', 
        )
        self.snapshots = _create_resource_collection(
            _NASSnapshotResource, _client, _client.describe_snapshots,
            'Snapshots.Snapshot', 'SnapshotId', 
        )
        self.zones = _create_special_resource_collection(
            _NASZoneResource, _client, _client.describe_zones,
            'Zones.Zone', 'ZoneId', 
        )
    def create_access_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_access_group(**_params)
        access_group_name = _new_get_key_in_response(response, 'AccessGroupName')
        return _NASAccessGroupResource(access_group_name, _client=self._client)

    def create_auto_snapshot_policy(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_auto_snapshot_policy(**_params)
        auto_snapshot_policy_id = _new_get_key_in_response(response, 'AutoSnapshotPolicyId')
        return _NASAutoSnapshotPolicyResource(auto_snapshot_policy_id, _client=self._client)

    def create_file_system(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_file_system(**_params)
        file_system_id = _new_get_key_in_response(response, 'FileSystemId')
        return _NASFileSystemResource(file_system_id, _client=self._client)

    def create_snapshot(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_snapshot(**_params)
        snapshot_id = _new_get_key_in_response(response, 'SnapshotId')
        return _NASSnapshotResource(snapshot_id, _client=self._client)

class _NASAccessGroupResource(ServiceResource):

    def __init__(self, access_group_name, _client=None):
        ServiceResource.__init__(self, "nas.access_group", _client=_client)
        self.access_group_name = access_group_name
        
        self.access_group_type = None
        self.description = None
        self.mount_target_count = None
        self.rule_count = None

        self.access_rules = _create_sub_resource_without_page_collection(
            _NASAccessRuleResource, _client, _client.describe_access_rules,
            'AccessRules.AccessRule', 'AccessRuleId', parent_identifier="AccessGroupName",parent_identifier_value=self.access_group_name
        )
    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_access_group(access_group_name=self.access_group_name, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_access_group(access_group_name=self.access_group_name, **_params)

    def create_access_rule(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_access_rule(access_group_name=self.access_group_name,**_params)
        access_rule_id = _new_get_key_in_response(response, 'AccessRuleId')
        return _NASAccessRuleResource(access_rule_id,self.access_group_name, _client=self._client)

class _NASAccessRuleResource(ServiceResource):

    def __init__(self, access_rule_id,access_group_name, _client=None):
        ServiceResource.__init__(self, "nas.access_rule", _client=_client)
        self.access_rule_id = access_rule_id
        self.access_group_name = access_group_name
        self.priority = None
        self.rw_access = None
        self.source_cidr_ip = None
        self.user_access = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_access_rule(access_rule_id=self.access_rule_id,access_group_name=self.access_group_name, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_access_rule(access_rule_id=self.access_rule_id,access_group_name=self.access_group_name, **_params)

class _NASAutoSnapshotPolicyResource(ServiceResource):

    def __init__(self, auto_snapshot_policy_id, _client=None):
        ServiceResource.__init__(self, "nas.auto_snapshot_policy", _client=_client)
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        
        self.auto_snapshot_policy_name = None
        self.create_time = None
        self.file_system_nums = None
        self.region_id = None
        self.repeat_weekdays = None
        self.retention_days = None
        self.status = None
        self.time_points = None

    def apply(self, **params):
        _params = _transfer_params(params)
        return self._client.apply_auto_snapshot_policy(auto_snapshot_policy_id=self.auto_snapshot_policy_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_auto_snapshot_policy(auto_snapshot_policy_id=self.auto_snapshot_policy_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_auto_snapshot_policy(auto_snapshot_policy_id=self.auto_snapshot_policy_id, **_params)

class _NASFileSystemResource(ServiceResource):

    def __init__(self, file_system_id, _client=None):
        ServiceResource.__init__(self, "nas.file_system", _client=_client)
        self.file_system_id = file_system_id
        
        self.auto_snapshot_policy_id = None
        self.bandwidth = None
        self.capacity = None
        self.create_time = None
        self.description = None
        self.encrypt_type = None
        self.ldap = None
        self.metered_size = None
        self.mount_targets = None
        self.packages = None
        self.protocol_type = None
        self.region_id = None
        self.status = None
        self.storage_type = None
        self.zone_id = None

    def cancel_auto_snapshot_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.cancel_auto_snapshot_policy(file_system_id=self.file_system_id, **_params)

    def add_client_to_black_list(self, **params):
        _params = _transfer_params(params)
        return self._client.add_client_to_black_list(file_system_id=self.file_system_id, **_params)

    def add_tags(self, **params):
        _params = _transfer_params(params)
        return self._client.add_tags(file_system_id=self.file_system_id, **_params)

    def create_ldap_config(self, **params):
        _params = _transfer_params(params)
        return self._client.create_ldap_config(file_system_id=self.file_system_id, **_params)

    def create_mount_target(self, **params):
        _params = _transfer_params(params)
        return self._client.create_mount_target(file_system_id=self.file_system_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_file_system(file_system_id=self.file_system_id, **_params)

    def delete_ldap_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_ldap_config(file_system_id=self.file_system_id, **_params)

    def delete_mount_target(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_mount_target(file_system_id=self.file_system_id, **_params)

    def describe_black_list_clients(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_black_list_clients(file_system_id=self.file_system_id, **_params)

    def describe_ldap_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ldap_config(file_system_id=self.file_system_id, **_params)

    def describe_mount_targets(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_mount_targets(file_system_id=self.file_system_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_file_system(file_system_id=self.file_system_id, **_params)

    def modify_ldap_config(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_ldap_config(file_system_id=self.file_system_id, **_params)

    def modify_mount_target(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_mount_target(file_system_id=self.file_system_id, **_params)

    def remove_client_from_black_list(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_client_from_black_list(file_system_id=self.file_system_id, **_params)

    def remove_tags(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_tags(file_system_id=self.file_system_id, **_params)

    def reset(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_file_system(file_system_id=self.file_system_id, **_params)

class _NASSnapshotResource(ServiceResource):

    def __init__(self, snapshot_id, _client=None):
        ServiceResource.__init__(self, "nas.snapshot", _client=_client)
        self.snapshot_id = snapshot_id
        
        self.create_time = None
        self.description = None
        self.progress = None
        self.remain_time = None
        self.retention_days = None
        self.snapshot_name = None
        self.source_file_system_id = None
        self.source_file_system_size = None
        self.status = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_snapshot(snapshot_id=self.snapshot_id, **_params)

class _NASZoneResource(ServiceResource):

    def __init__(self, zone_id, _client=None):
        ServiceResource.__init__(self, "nas.zone", _client=_client)
        self.zone_id = zone_id
        
        self.capacity = None
        self.performance = None
