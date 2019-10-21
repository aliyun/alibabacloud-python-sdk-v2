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


class _R_KVSTOREResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'r-kvstore', _client=_client)
        self.backups = _create_resource_collection(
            _R_KVSTOREBackupResource, _client, _client.describe_backups,
            'Backups.Backup', 'BackupId', 
        )
        self.instances = _create_resource_collection(
            _R_KVSTOREInstanceResource, _client, _client.describe_instances,
            'Instances.KVStoreInstance', 'InstanceId', 
        )
        self.parameters = _create_special_resource_collection(
            _R_KVSTOREParameterResource, _client, _client.describe_parameters,
            'ConfigParameters.Parameter', 'ParameterName', 
        )
        self.regions = _create_special_resource_collection(
            _R_KVSTORERegionResource, _client, _client.describe_regions,
            'RegionIds.KVStoreRegion', 'RegionId', 
        )
        self.replicas = _create_resource_collection(
            _R_KVSTOREReplicaResource, _client, _client.describe_replicas,
            'Replicas.Items', 'ReplicaId', key_to_total_count="TotalRecordCount",key_to_page_size="PageRecordCount",key_to_page_number="PageNumber"
        )
        self.zones = _create_special_resource_collection(
            _R_KVSTOREZoneResource, _client, _client.describe_zones,
            'Zones.KVStoreZone', 'ZoneId', 
        )
    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _R_KVSTOREInstanceResource(instance_id, _client=self._client)

class _R_KVSTOREBackupResource(ServiceResource):

    def __init__(self, backup_id, _client=None):
        ServiceResource.__init__(self, "r-kvstore.backup", _client=_client)
        self.backup_id = backup_id
        
        self.backup_db_names = None
        self.backup_download_url = None
        self.backup_end_time = None
        self.backup_intranet_download_url = None
        self.backup_method = None
        self.backup_mode = None
        self.backup_size = None
        self.backup_start_time = None
        self.backup_status = None
        self.backup_type = None
        self.engine_version = None
        self.node_instance_id = None

class _R_KVSTOREInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "r-kvstore.instance", _client=_client)
        self.instance_id = instance_id
        
        self.architecture_type = None
        self.bandwidth = None
        self.capacity = None
        self.charge_type = None
        self.config = None
        self.connection_domain = None
        self.connection_mode = None
        self.connections = None
        self.create_time = None
        self.destroy_time = None
        self.end_time = None
        self.engine_version = None
        self.has_renew_change_order = None
        self.instance_class = None
        self.instance_name = None
        self.instance_status = None
        self.instance_type = None
        self.is_rds = None
        self.network_type = None
        self.node_type = None
        self.package_type = None
        self.port = None
        self.private_ip = None
        self.qps = None
        self.region_id = None
        self.replacate_id = None
        self.search_key = None
        self.tags = None
        self.user_name = None
        self.vswitch_id = None
        self.vpc_cloud_instance_id = None
        self.vpc_id = None
        self.zone_id = None

        self.accounts = _create_sub_resource_without_page_collection(
            _R_KVSTOREAccountResource, _client, _client.describe_accounts,
            'Accounts.Account', 'AccountName', parent_identifier="InstanceId",parent_identifier_value=self.instance_id
        )
        self.snapshots = _create_sub_resource_without_page_collection(
            _R_KVSTORESnapshotResource, _client, _client.describe_snapshots,
            'Snapshots.Snapshot', 'SnapshotId', parent_identifier="InstanceId",parent_identifier_value=self.instance_id
        )
        self.temp_instances = _create_sub_resource_without_page_collection(
            _R_KVSTORETempInstanceResource, _client, _client.describe_temp_instance,
            'TempInstances.TempInstance', 'TempInstanceId', parent_identifier="InstanceId",parent_identifier_value=self.instance_id
        )
    def allocate_instance_public_connection(self, **params):
        _params = _transfer_params(params)
        return self._client.allocate_instance_public_connection(instance_id=self.instance_id, **_params)

    def create_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.create_backup(instance_id=self.instance_id, **_params)

    def create_cache_analysis_task(self, **params):
        _params = _transfer_params(params)
        return self._client.create_cache_analysis_task(instance_id=self.instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_instance(instance_id=self.instance_id, **_params)

    def delete_snapshot_settings(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_snapshot_settings(instance_id=self.instance_id, **_params)

    def describe_audit_records(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_audit_records(instance_id=self.instance_id, **_params)

    def describe_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_backup_policy(instance_id=self.instance_id, **_params)

    def describe_cache_analysis_report(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cache_analysis_report(instance_id=self.instance_id, **_params)

    def describe_cache_analysis_report_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cache_analysis_report_list(instance_id=self.instance_id, **_params)

    def describe_certification(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_certification(instance_id=self.instance_id, **_params)

    def describe_db_instance_net_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_instance_net_info(instance_id=self.instance_id, **_params)

    def describe_error_log_records(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_error_log_records(instance_id=self.instance_id, **_params)

    def describe_history_monitor_values(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_history_monitor_values(instance_id=self.instance_id, **_params)

    def describe_instance_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_instance_attribute(instance_id=self.instance_id, **_params)

    def describe_instance_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_instance_config(instance_id=self.instance_id, **_params)

    def describe_instance_ssl(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_instance_ssl(instance_id=self.instance_id, **_params)

    def describe_intranet_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_intranet_attribute(instance_id=self.instance_id, **_params)

    def describe_logic_instance_topology(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_logic_instance_topology(instance_id=self.instance_id, **_params)

    def describe_monthly_service_status_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_monthly_service_status_detail(instance_id=self.instance_id, **_params)

    def describe_running_log_records(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_running_log_records(instance_id=self.instance_id, **_params)

    def describe_security_ips(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_security_ips(instance_id=self.instance_id, **_params)

    def describe_slow_log_records(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_slow_log_records(instance_id=self.instance_id, **_params)

    def destroy(self, **params):
        _params = _transfer_params(params)
        return self._client.destroy_instance(instance_id=self.instance_id, **_params)

    def flush(self, **params):
        _params = _transfer_params(params)
        return self._client.flush_instance(instance_id=self.instance_id, **_params)

    def get_snapshot_settings(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_snapshot_settings(instance_id=self.instance_id, **_params)
        return response

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_attribute(instance_id=self.instance_id, **_params)

    def modify_audit_log_config(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_audit_log_config(instance_id=self.instance_id, **_params)

    def modify_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_backup_policy(instance_id=self.instance_id, **_params)

    def modify_certification(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_certification(instance_id=self.instance_id, **_params)

    def modify_config(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_config(instance_id=self.instance_id, **_params)

    def modify_intranet_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_intranet_attribute(instance_id=self.instance_id, **_params)

    def modify_maintain_time(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_maintain_time(instance_id=self.instance_id, **_params)

    def modify_major_version(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_major_version(instance_id=self.instance_id, **_params)

    def modify_minor_version(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_minor_version(instance_id=self.instance_id, **_params)

    def modify_net_expire_time(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_net_expire_time(instance_id=self.instance_id, **_params)

    def modify_ssl(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_ssl(instance_id=self.instance_id, **_params)

    def modify_security_ips(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_security_ips(instance_id=self.instance_id, **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_spec(instance_id=self.instance_id, **_params)

    def modify_spec_pre_check(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_spec_pre_check(instance_id=self.instance_id, **_params)

    def modify_vpc_auth_mode(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_vpc_auth_mode(instance_id=self.instance_id, **_params)

    def query_task(self, **params):
        _params = _transfer_params(params)
        return self._client.query_task(instance_id=self.instance_id, **_params)

    def release_instance_public_connection(self, **params):
        _params = _transfer_params(params)
        return self._client.release_instance_public_connection(instance_id=self.instance_id, **_params)

    def renew(self, **params):
        _params = _transfer_params(params)
        return self._client.renew_instance(instance_id=self.instance_id, **_params)

    def restart(self, **params):
        _params = _transfer_params(params)
        return self._client.restart_instance(instance_id=self.instance_id, **_params)

    def set_snapshot_settings(self, **params):
        _params = _transfer_params(params)
        return self._client.set_snapshot_settings(instance_id=self.instance_id, **_params)

    def switch_network(self, **params):
        _params = _transfer_params(params)
        return self._client.switch_network(instance_id=self.instance_id, **_params)

    def transform_to_pre_paid(self, **params):
        _params = _transfer_params(params)
        return self._client.transform_to_pre_paid(instance_id=self.instance_id, **_params)

    def verify_password(self, **params):
        _params = _transfer_params(params)
        return self._client.verify_password(instance_id=self.instance_id, **_params)

    def restore(self, **params):
        _params = _transfer_params(params)
        return self._client.restore_instance(instance_id=self.instance_id, **_params)

    def create_account(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_account(instance_id=self.instance_id,**_params)
        account_name = _new_get_key_in_response(response, 'AccountName')
        return _R_KVSTOREAccountResource(account_name,self.instance_id, _client=self._client)

    def create_snapshot(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_snapshot(instance_id=self.instance_id,**_params)
        snapshot_id = _new_get_key_in_response(response, 'SnapshotId')
        return _R_KVSTORESnapshotResource(snapshot_id,self.instance_id, _client=self._client)

    def create_temp_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_temp_instance(instance_id=self.instance_id,**_params)
        temp_instance_id = _new_get_key_in_response(response, 'TempInstanceId')
        return _R_KVSTORETempInstanceResource(temp_instance_id,self.instance_id, _client=self._client)

class _R_KVSTOREAccountResource(ServiceResource):

    def __init__(self, account_name,instance_id, _client=None):
        ServiceResource.__init__(self, "r-kvstore.account", _client=_client)
        self.account_name = account_name
        self.instance_id = instance_id
        self.account_description = None
        self.account_status = None
        self.account_type = None
        self.database_privileges = None
        self.priv_exceeded = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_account(account_name=self.account_name,instance_id=self.instance_id, **_params)

    def grant_account_privilege(self, **params):
        _params = _transfer_params(params)
        return self._client.grant_account_privilege(account_name=self.account_name,instance_id=self.instance_id, **_params)

    def modify_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_account_description(account_name=self.account_name,instance_id=self.instance_id, **_params)

    def reset(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_account(account_name=self.account_name,instance_id=self.instance_id, **_params)

    def reset_account_password(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_account_password(account_name=self.account_name,instance_id=self.instance_id, **_params)

    def revoke_account_privilege(self, **params):
        _params = _transfer_params(params)
        return self._client.revoke_account_privilege(account_name=self.account_name,instance_id=self.instance_id, **_params)

class _R_KVSTORESnapshotResource(ServiceResource):

    def __init__(self, snapshot_id,instance_id, _client=None):
        ServiceResource.__init__(self, "r-kvstore.snapshot", _client=_client)
        self.snapshot_id = snapshot_id
        self.instance_id = instance_id
        self.create_time = None
        self.memory = None
        self.oss_download_in_path = None
        self.oss_download_out_path = None
        self.rdb_size = None
        self.snapshot_name = None
        self.status = None
        self.type_ = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_snapshot(snapshot_id=self.snapshot_id,instance_id=self.instance_id, **_params)

    def restore(self, **params):
        _params = _transfer_params(params)
        return self._client.restore_snapshot(snapshot_id=self.snapshot_id,instance_id=self.instance_id, **_params)

class _R_KVSTORETempInstanceResource(ServiceResource):

    def __init__(self, temp_instance_id,instance_id, _client=None):
        ServiceResource.__init__(self, "r-kvstore.temp_instance", _client=_client)
        self.temp_instance_id = temp_instance_id
        self.instance_id = instance_id
        self.create_time = None
        self.domain = None
        self.expire_time = None
        self.memory = None
        self.snapshot_id = None
        self.status = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_temp_instance(temp_instance_id=self.temp_instance_id,instance_id=self.instance_id, **_params)

    def switch(self, **params):
        _params = _transfer_params(params)
        return self._client.switch_temp_instance(temp_instance_id=self.temp_instance_id,instance_id=self.instance_id, **_params)

class _R_KVSTOREParameterResource(ServiceResource):

    def __init__(self, parameter_name, _client=None):
        ServiceResource.__init__(self, "r-kvstore.parameter", _client=_client)
        self.parameter_name = parameter_name
        
        self.checking_code = None
        self.force_restart = None
        self.modifiable_status = None
        self.parameter_description = None
        self.parameter_value = None

class _R_KVSTORERegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "r-kvstore.region", _client=_client)
        self.region_id = region_id
        
        self.local_name = None
        self.region_endpoint = None
        self.zone_id_list = None
        self.zone_ids = None

class _R_KVSTOREReplicaResource(ServiceResource):

    def __init__(self, replica_id, _client=None):
        ServiceResource.__init__(self, "r-kvstore.replica", _client=_client)
        self.replica_id = replica_id
        
        self.db_instances = None
        self.domain_mode = None
        self.replica_description = None
        self.replica_mode = None
        self.replica_status = None

    def create_static_verification(self, **params):
        _params = _transfer_params(params)
        return self._client.create_static_verification(replica_id=self.replica_id, **_params)

    def describe_replica_conflict_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_replica_conflict_info(replica_id=self.replica_id, **_params)

    def describe_replica_performance(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_replica_performance(replica_id=self.replica_id, **_params)

    def describe_replica_usage(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_replica_usage(replica_id=self.replica_id, **_params)

    def describe_static_verification_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_static_verification_list(replica_id=self.replica_id, **_params)

    def describe_strategy(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_strategy(replica_id=self.replica_id, **_params)

    def describe_verification_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_verification_list(replica_id=self.replica_id, **_params)

    def evaluate_fail_over_switch(self, **params):
        _params = _transfer_params(params)
        return self._client.evaluate_fail_over_switch(replica_id=self.replica_id, **_params)

    def modify_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_replica_description(replica_id=self.replica_id, **_params)

    def modify_guard_domain_mode(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_guard_domain_mode(replica_id=self.replica_id, **_params)

    def modify_mode(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_replica_mode(replica_id=self.replica_id, **_params)

    def modify_recovery_mode(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_replica_recovery_mode(replica_id=self.replica_id, **_params)

    def modify_relation(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_replica_relation(replica_id=self.replica_id, **_params)

    def modify_verification_mode(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_replica_verification_mode(replica_id=self.replica_id, **_params)

    def release(self, **params):
        _params = _transfer_params(params)
        return self._client.release_replica(replica_id=self.replica_id, **_params)

    def unlink_replica_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.unlink_replica_instance(replica_id=self.replica_id, **_params)

class _R_KVSTOREZoneResource(ServiceResource):

    def __init__(self, zone_id, _client=None):
        ServiceResource.__init__(self, "r-kvstore.zone", _client=_client)
        self.zone_id = zone_id
        
        self.disabled = None
        self.is_rds = None
        self.region_id = None
        self.switch_network = None
        self.zone_name = None

    def migrate_to_other(self, **params):
        _params = _transfer_params(params)
        return self._client.migrate_to_other_zone(zone_id=self.zone_id, **_params)
