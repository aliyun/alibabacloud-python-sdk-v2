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


class _HBRResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'hbr', _client=_client)
        self.backup_sources = _create_resource_collection(
            _HBRBackupSourceResource, _client, _client.describe_backup_sources,
            'BackupSources.BackupSource', 'BackupSourceId', 
        )
        self.backup_source_groups = _create_resource_collection(
            _HBRBackupSourceGroupResource, _client, _client.describe_backup_source_groups,
            'BackupSourceGroups.BackupSourceGroup', 'BackupSourceGroupId', 
        )
        self.clients = _create_resource_collection(
            _HBRClientResource, _client, _client.describe_clients,
            'Clients.Client', 'ClientId', 
        )
        self.contacts = _create_resource_collection(
            _HBRContactResource, _client, _client.describe_contacts,
            'Contacts.Contact', 'ContactId', 
        )
        self.contact_groups = _create_resource_collection(
            _HBRContactGroupResource, _client, _client.describe_contact_groups,
            'ContactGroups.ContactGroup', 'ContactGroupName', 
        )
        self.hana_nodes = _create_resource_collection(
            _HBRHanaNodeResource, _client, _client.describe_hana_nodes,
            'HanaNodes.HanaNode', 'HanaNodeId', 
        )
        self.jobs = _create_resource_collection(
            _HBRJobResource, _client, _client.describe_jobs,
            'Jobs.Job', 'JobId', 
        )
        self.plans = _create_resource_collection(
            _HBRPlanResource, _client, _client.describe_plans,
            'Plans.Plan', 'PlanId', 
        )
        self.policies = _create_resource_collection(
            _HBRPolicyResource, _client, _client.describe_policies,
            'Policies.Policy', 'PolicyId', 
        )
        self.regions = _create_special_resource_collection(
            _HBRRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId', 
        )
        self.restores = _create_resource_collection(
            _HBRRestoreResource, _client, _client.describe_restores,
            'Restores.Restore', 'RestoreId', 
        )
        self.servers = _create_resource_collection(
            _HBRServerResource, _client, _client.describe_servers,
            'Servers.Server', 'ServerId', 
        )
        self.snapshots = _create_resource_collection(
            _HBRSnapshotResource, _client, _client.describe_snapshots,
            'Snapshots.Snapshot', 'SnapshotId', 
        )
    def create_backup_source_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_backup_source_group(**_params)
        backup_source_group_id = _new_get_key_in_response(response, 'BackupSourceGroupId')
        return _HBRBackupSourceGroupResource(backup_source_group_id, _client=self._client)

    def create_client(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_client(**_params)
        client_id = _new_get_key_in_response(response, 'ClientId')
        return _HBRClientResource(client_id, _client=self._client)

    def create_contact(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_contact(**_params)
        contact_id = _new_get_key_in_response(response, 'ContactId')
        return _HBRContactResource(contact_id, _client=self._client)

    def create_contact_group(self, **params):
        _params = _transfer_params(params)
        self._client.create_contact_group(**_params)
        contact_group_name = _params.get("contact_group_name")
        return _HBRContactGroupResource(contact_group_name, _client=self._client)

    def create_job(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_job(**_params)
        job_id = _new_get_key_in_response(response, 'JobId')
        return _HBRJobResource(job_id, _client=self._client)

    def create_plan(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_plan(**_params)
        plan_id = _new_get_key_in_response(response, 'PlanId')
        return _HBRPlanResource(plan_id, _client=self._client)

    def create_policy(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_policy(**_params)
        policy_id = _new_get_key_in_response(response, 'PolicyId')
        return _HBRPolicyResource(policy_id, _client=self._client)

    def create_restore(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_restore(**_params)
        restore_id = _new_get_key_in_response(response, 'RestoreId')
        return _HBRRestoreResource(restore_id, _client=self._client)

    def add_server(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_server(**_params)
        server_id = _new_get_key_in_response(response, 'ServerId')
        return _HBRServerResource(server_id, _client=self._client)

    def create_snapshot(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_snapshot(**_params)
        snapshot_id = _new_get_key_in_response(response, 'SnapshotId')
        return _HBRSnapshotResource(snapshot_id, _client=self._client)

class _HBRBackupSourceResource(ServiceResource):

    def __init__(self, backup_source_id, _client=None):
        ServiceResource.__init__(self, "hbr.backup_source", _client=_client)
        self.backup_source_id = backup_source_id
        
        self.all_database = None
        self.backup_source_group_id = None
        self.cluster_id = None
        self.created_time = None
        self.database_name = None
        self.description = None
        self.source_type = None
        self.updated_time = None

class _HBRBackupSourceGroupResource(ServiceResource):

    def __init__(self, backup_source_group_id, _client=None):
        ServiceResource.__init__(self, "hbr.backup_source_group", _client=_client)
        self.backup_source_group_id = backup_source_group_id
        
        self.backup_source_count = None
        self.cluster_id = None
        self.created_time = None
        self.description = None
        self.source_type = None
        self.updated_time = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_backup_source_group(backup_source_group_id=self.backup_source_group_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_backup_source_group(backup_source_group_id=self.backup_source_group_id, **_params)

class _HBRClientResource(ServiceResource):

    def __init__(self, client_id, _client=None):
        ServiceResource.__init__(self, "hbr.client", _client=_client)
        self.client_id = client_id
        
        self.alert_setting = None
        self.client_name = None
        self.client_type = None
        self.client_version = None
        self.contact_id = None
        self.created_time = None
        self.eip_address = None
        self.gateway_id = None
        self.gateway_inner_ip = None
        self.gateway_name = None
        self.gateway_status = None
        self.host_name = None
        self.inner_ip_addresses = None
        self.instance_id = None
        self.instance_name = None
        self.jobs_count = None
        self.max_version = None
        self.network_type = None
        self.os_name = None
        self.platform_type = None
        self.private_ip_addresses = None
        self.public_ip_addresses = None
        self.snapshot_complete = None
        self.snapshot_failed = None
        self.snapshot_partial_complete = None
        self.snapshot_running = None
        self.snapshot_total = None
        self.source_types = None
        self.status = None
        self.status_message = None
        self.updated_time = None
        self.vault_id = None
        self.vault_type = None

    def generate_token(self, **params):
        _params = _transfer_params(params)
        return self._client.generate_token(client_id=self.client_id, **_params)

class _HBRContactResource(ServiceResource):

    def __init__(self, contact_id, _client=None):
        ServiceResource.__init__(self, "hbr.contact", _client=_client)
        self.contact_id = contact_id
        
        self.description = None
        self.email = None
        self.mobile = None
        self.name = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_contact(contact_id=self.contact_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_contact(contact_id=self.contact_id, **_params)

class _HBRContactGroupResource(ServiceResource):

    def __init__(self, contact_group_name, _client=None):
        ServiceResource.__init__(self, "hbr.contact_group", _client=_client)
        self.contact_group_name = contact_group_name
        
        self.contact_group_id = None
        self.contacts = None
        self.display_name = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_contact_group(contact_group_name=self.contact_group_name, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_contact_group(contact_group_name=self.contact_group_name, **_params)

class _HBRHanaNodeResource(ServiceResource):

    def __init__(self, hana_node_id, _client=None):
        ServiceResource.__init__(self, "hbr.hana_node", _client=_client)
        self.hana_node_id = hana_node_id
        
        self.client_id = None
        self.cluster_id = None
        self.instance_id = None
        self.instance_name = None
        self.status = None
        self.status_message = None
        self.vault_id = None

class _HBRJobResource(ServiceResource):

    def __init__(self, job_id, _client=None):
        ServiceResource.__init__(self, "hbr.job", _client=_client)
        self.job_id = job_id
        
        self.actual_bytes = None
        self.bytes_done = None
        self.bytes_total = None
        self.client_id = None
        self.complete_time = None
        self.created_time = None
        self.current_snapshot_id = None
        self.duration = None
        self.error_count = None
        self.exit_code = None
        self.instance_id = None
        self.items_done = None
        self.items_total = None
        self.job_name = None
        self.job_option = None
        self.job_status = None
        self.job_type = None
        self.last_run_time = None
        self.last_snapshot_id = None
        self.policy_id = None
        self.retention = None
        self.schedule = None
        self.snapshot_status = None
        self.source = None
        self.source_type = None
        self.updated_time = None
        self.vault_id = None

    def cancel(self, **params):
        _params = _transfer_params(params)
        return self._client.cancel_job(job_id=self.job_id, **_params)

    def cancel_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.cancel_backup_job(job_id=self.job_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_job(job_id=self.job_id, **_params)

    def disable(self, **params):
        _params = _transfer_params(params)
        return self._client.disable_job(job_id=self.job_id, **_params)

    def enable(self, **params):
        _params = _transfer_params(params)
        return self._client.enable_job(job_id=self.job_id, **_params)

    def execute(self, **params):
        _params = _transfer_params(params)
        return self._client.execute_job(job_id=self.job_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_job(job_id=self.job_id, **_params)

    def update_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.update_backup_job(job_id=self.job_id, **_params)

class _HBRPlanResource(ServiceResource):

    def __init__(self, plan_id, _client=None):
        ServiceResource.__init__(self, "hbr.plan", _client=_client)
        self.plan_id = plan_id
        
        self.client_id = None
        self.created_time = None
        self.diff_policy_id = None
        self.full_policy_id = None
        self.inc_policy_id = None
        self.is_removed = None
        self.plan_name = None
        self.plan_status = None
        self.retention = None
        self.schedule_type = None
        self.server_id = None
        self.server_type = None
        self.source = None
        self.source_type = None
        self.updated_time = None
        self.vault_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_plan(plan_id=self.plan_id, **_params)

    def delete_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_backup_plan(plan_id=self.plan_id, **_params)

    def delete_hana_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_hana_backup_plan(plan_id=self.plan_id, **_params)

    def disable_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.disable_backup_plan(plan_id=self.plan_id, **_params)

    def disable_hana_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.disable_hana_backup_plan(plan_id=self.plan_id, **_params)

    def enable_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.enable_backup_plan(plan_id=self.plan_id, **_params)

    def enable_hana_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.enable_hana_backup_plan(plan_id=self.plan_id, **_params)

    def execute_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.execute_backup_plan(plan_id=self.plan_id, **_params)

    def execute_hana_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.execute_hana_backup_plan(plan_id=self.plan_id, **_params)

    def remove(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_plan(plan_id=self.plan_id, **_params)

    def restore(self, **params):
        _params = _transfer_params(params)
        return self._client.restore_plan(plan_id=self.plan_id, **_params)

    def update_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.update_backup_plan(plan_id=self.plan_id, **_params)

    def update_hana_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.update_hana_backup_plan(plan_id=self.plan_id, **_params)

class _HBRPolicyResource(ServiceResource):

    def __init__(self, policy_id, _client=None):
        ServiceResource.__init__(self, "hbr.policy", _client=_client)
        self.policy_id = policy_id
        
        self.client_id = None
        self.created_time = None
        self.last_run_time = None
        self.policy_name = None
        self.retention = None
        self.schedule = None
        self.source = None
        self.status = None
        self.updated_time = None
        self.vault_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_policy(policy_id=self.policy_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_policy(policy_id=self.policy_id, **_params)

class _HBRRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "hbr.region", _client=_client)
        self.region_id = region_id
        
        self.local_name = None
        self.vault_count = None

class _HBRRestoreResource(ServiceResource):

    def __init__(self, restore_id, _client=None):
        ServiceResource.__init__(self, "hbr.restore", _client=_client)
        self.restore_id = restore_id
        
        self.actual_bytes = None
        self.bytes_done = None
        self.bytes_total = None
        self.client_id = None
        self.complete_time = None
        self.container_restore_id = None
        self.created_time = None
        self.duration = None
        self.error_count = None
        self.exit_code = None
        self.extra = None
        self.items_done = None
        self.items_total = None
        self.restore_name = None
        self.restore_type = None
        self.server_id = None
        self.snapshot_hash = None
        self.snapshot_id = None
        self.source = None
        self.source_client_id = None
        self.status = None
        self.target = None
        self.updated_time = None
        self.vault_id = None

    def cancel(self, **params):
        _params = _transfer_params(params)
        return self._client.cancel_restore(restore_id=self.restore_id, **_params)

    def cancel_restore_job(self, **params):
        _params = _transfer_params(params)
        return self._client.cancel_restore_job(restore_id=self.restore_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_restore(restore_id=self.restore_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_restore(restore_id=self.restore_id, **_params)

    def update_sql_server(self, **params):
        _params = _transfer_params(params)
        return self._client.update_sql_server_restore(restore_id=self.restore_id, **_params)

class _HBRServerResource(ServiceResource):

    def __init__(self, server_id, _client=None):
        ServiceResource.__init__(self, "hbr.server", _client=_client)
        self.server_id = server_id
        
        self.client_id = None
        self.created_time = None
        self.description = None
        self.detail_info = None
        self.host = None
        self.is_removed = None
        self.password = None
        self.server_status = None
        self.server_type = None
        self.updated_time = None
        self.username = None
        self.vault_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_server(server_id=self.server_id, **_params)

    def remove(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_server(server_id=self.server_id, **_params)

    def restore(self, **params):
        _params = _transfer_params(params)
        return self._client.restore_server(server_id=self.server_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_server(server_id=self.server_id, **_params)

class _HBRSnapshotResource(ServiceResource):

    def __init__(self, snapshot_id, _client=None):
        ServiceResource.__init__(self, "hbr.snapshot", _client=_client)
        self.snapshot_id = snapshot_id
        
        self.actual_bytes = None
        self.bytes_done = None
        self.bytes_total = None
        self.client_id = None
        self.complete_time = None
        self.container_snapshot_id = None
        self.created_time = None
        self.duration = None
        self.error_count = None
        self.error_file = None
        self.error_message = None
        self.error_type = None
        self.exit_code = None
        self.extra = None
        self.items_done = None
        self.items_total = None
        self.job_id = None
        self.parent_hash = None
        self.plan_id = None
        self.retention = None
        self.server_id = None
        self.size = None
        self.snapshot_hash = None
        self.snapshot_name = None
        self.snapshot_option = None
        self.snapshot_type = None
        self.source = None
        self.source_type = None
        self.status = None
        self.updated_time = None
        self.vault_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_snapshot(snapshot_id=self.snapshot_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_snapshot(snapshot_id=self.snapshot_id, **_params)

    def update_sql_server(self, **params):
        _params = _transfer_params(params)
        return self._client.update_sql_server_snapshot(snapshot_id=self.snapshot_id, **_params)
