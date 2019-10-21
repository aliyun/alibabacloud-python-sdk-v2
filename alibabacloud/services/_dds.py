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


class _DDSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'dds', _client=_client)
        self.db_instances = _create_resource_collection(
            _DDSDBInstanceResource, _client, _client.describe_db_instances,
            'DBInstances.DBInstance', 'DBInstanceId', 
        )
        self.parameters = _create_special_resource_collection(
            _DDSParameterResource, _client, _client.describe_parameters,
            'ConfigParameters.Parameter', 'ParameterName', 
        )
        self.regions = _create_special_resource_collection(
            _DDSRegionResource, _client, _client.describe_regions,
            'Regions.DdsRegion', 'RegionId', 
        )
        self.replicas = _create_resource_collection(
            _DDSReplicaResource, _client, _client.describe_replicas,
            'Replicas.Items', 'ReplicaId', key_to_total_count="TotalRecordCount",key_to_page_size="PageRecordCount",key_to_page_number="PageNumber"
        )
    def create_db_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_db_instance(**_params)
        db_instance_id = _new_get_key_in_response(response, 'DBInstanceId')
        return _DDSDBInstanceResource(db_instance_id, _client=self._client)

class _DDSDBInstanceResource(ServiceResource):

    def __init__(self, db_instance_id, _client=None):
        ServiceResource.__init__(self, "dds.db_instance", _client=_client)
        self.db_instance_id = db_instance_id
        
        self.charge_type = None
        self.creation_time = None
        self.db_instance_class = None
        self.db_instance_description = None
        self.db_instance_status = None
        self.db_instance_storage = None
        self.db_instance_type = None
        self.destroy_time = None
        self.engine = None
        self.engine_version = None
        self.expire_time = None
        self.last_downgrade_time = None
        self.lock_mode = None
        self.mongos_list = None
        self.network_type = None
        self.region_id = None
        self.replication_factor = None
        self.resource_group_id = None
        self.shard_list = None
        self.tags = None
        self.vpc_auth_mode = None
        self.zone_id = None

        self.accounts = _create_sub_resource_without_page_collection(
            _DDSAccountResource, _client, _client.describe_accounts,
            'Accounts.Account', 'AccountName', parent_identifier="DBInstanceId",parent_identifier_value=self.db_instance_id
        )
        self.backups = _create_sub_resource_without_page_collection(
            _DDSBackupResource, _client, _client.describe_backups,
            'Backups.Backup', 'BackupId', parent_identifier="DBInstanceId",parent_identifier_value=self.db_instance_id
        )
    def allocate_node_private_network_address(self, **params):
        _params = _transfer_params(params)
        return self._client.allocate_node_private_network_address(db_instance_id=self.db_instance_id, **_params)

    def allocate_public_network_address(self, **params):
        _params = _transfer_params(params)
        return self._client.allocate_public_network_address(db_instance_id=self.db_instance_id, **_params)

    def check_cloud_resource_authorized(self, **params):
        _params = _transfer_params(params)
        return self._client.check_cloud_resource_authorized(db_instance_id=self.db_instance_id, **_params)

    def create_node(self, **params):
        _params = _transfer_params(params)
        return self._client.create_node(db_instance_id=self.db_instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_db_instance(db_instance_id=self.db_instance_id, **_params)

    def delete_node(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_node(db_instance_id=self.db_instance_id, **_params)

    def describe_audit_files(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_audit_files(db_instance_id=self.db_instance_id, **_params)

    def describe_audit_log_filter(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_audit_log_filter(db_instance_id=self.db_instance_id, **_params)

    def describe_audit_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_audit_policy(db_instance_id=self.db_instance_id, **_params)

    def describe_audit_records(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_audit_records(db_instance_id=self.db_instance_id, **_params)

    def describe_available_engine_version(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_available_engine_version(db_instance_id=self.db_instance_id, **_params)

    def describe_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_backup_policy(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_instance_attribute(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_monitor(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_instance_monitor(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_performance(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_instance_performance(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_ssl(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_instance_ssl(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_tde_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_instance_tde_info(db_instance_id=self.db_instance_id, **_params)

    def describe_error_log_records(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_error_log_records(db_instance_id=self.db_instance_id, **_params)

    def describe_parameter_modification_history(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_parameter_modification_history(db_instance_id=self.db_instance_id, **_params)

    def describe_renewal_price(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_renewal_price(db_instance_id=self.db_instance_id, **_params)

    def describe_replica_set_role(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_replica_set_role(db_instance_id=self.db_instance_id, **_params)

    def describe_role_zone_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_role_zone_info(db_instance_id=self.db_instance_id, **_params)

    def describe_running_log_records(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_running_log_records(db_instance_id=self.db_instance_id, **_params)

    def describe_security_ips(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_security_ips(db_instance_id=self.db_instance_id, **_params)

    def describe_sharding_network_address(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_sharding_network_address(db_instance_id=self.db_instance_id, **_params)

    def describe_slow_log_records(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_slow_log_records(db_instance_id=self.db_instance_id, **_params)

    def migrate_available_zone(self, **params):
        _params = _transfer_params(params)
        return self._client.migrate_available_zone(db_instance_id=self.db_instance_id, **_params)

    def modify_audit_log_filter(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_audit_log_filter(db_instance_id=self.db_instance_id, **_params)

    def modify_audit_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_audit_policy(db_instance_id=self.db_instance_id, **_params)

    def modify_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_backup_policy(db_instance_id=self.db_instance_id, **_params)

    def modify_connection_string(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_connection_string(db_instance_id=self.db_instance_id, **_params)

    def modify_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_description(db_instance_id=self.db_instance_id, **_params)

    def modify_instance_auto_renewal_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_auto_renewal_attribute(db_instance_id=self.db_instance_id, **_params)

    def modify_instance_vpc_auth_mode(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_vpc_auth_mode(db_instance_id=self.db_instance_id, **_params)

    def modify_maintain_time(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_maintain_time(db_instance_id=self.db_instance_id, **_params)

    def modify_monitor(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_monitor(db_instance_id=self.db_instance_id, **_params)

    def modify_net_expire_time(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_net_expire_time(db_instance_id=self.db_instance_id, **_params)

    def modify_network_type(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_network_type(db_instance_id=self.db_instance_id, **_params)

    def modify_node_spec(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_node_spec(db_instance_id=self.db_instance_id, **_params)

    def modify_parameters(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_parameters(db_instance_id=self.db_instance_id, **_params)

    def modify_ssl(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_ssl(db_instance_id=self.db_instance_id, **_params)

    def modify_security_ips(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_security_ips(db_instance_id=self.db_instance_id, **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_spec(db_instance_id=self.db_instance_id, **_params)

    def modify_tde(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_tde(db_instance_id=self.db_instance_id, **_params)

    def release_node_private_network_address(self, **params):
        _params = _transfer_params(params)
        return self._client.release_node_private_network_address(db_instance_id=self.db_instance_id, **_params)

    def release_public_network_address(self, **params):
        _params = _transfer_params(params)
        return self._client.release_public_network_address(db_instance_id=self.db_instance_id, **_params)

    def renew(self, **params):
        _params = _transfer_params(params)
        return self._client.renew_db_instance(db_instance_id=self.db_instance_id, **_params)

    def restart(self, **params):
        _params = _transfer_params(params)
        return self._client.restart_db_instance(db_instance_id=self.db_instance_id, **_params)

    def sample(self, **params):
        _params = _transfer_params(params)
        return self._client.sample(db_instance_id=self.db_instance_id, **_params)

    def switch_db_instance_ha(self, **params):
        _params = _transfer_params(params)
        return self._client.switch_db_instance_ha(db_instance_id=self.db_instance_id, **_params)

    def swithc_db_instance_ha(self, **params):
        _params = _transfer_params(params)
        return self._client.swithc_db_instance_ha(db_instance_id=self.db_instance_id, **_params)

    def upgrade_db_instance_engine_version(self, **params):
        _params = _transfer_params(params)
        return self._client.upgrade_db_instance_engine_version(db_instance_id=self.db_instance_id, **_params)

    def create_account(self, **params):
        _params = _transfer_params(params)
        self._client.create_account(db_instance_id=self.db_instance_id,**_params)
        account_name = _params.get("account_name")
        return _DDSAccountResource(account_name,self.db_instance_id, _client=self._client)

    def create_backup(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_backup(db_instance_id=self.db_instance_id,**_params)
        backup_id = _new_get_key_in_response(response, 'BackupId')
        return _DDSBackupResource(backup_id,self.db_instance_id, _client=self._client)

class _DDSAccountResource(ServiceResource):

    def __init__(self, account_name,db_instance_id, _client=None):
        ServiceResource.__init__(self, "dds.account", _client=_client)
        self.account_name = account_name
        self.db_instance_id = db_instance_id
        self.account_description = None
        self.account_status = None
        self.character_type = None

    def modify_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_account_description(account_name=self.account_name,db_instance_id=self.db_instance_id, **_params)

    def reset_account_password(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_account_password(account_name=self.account_name,db_instance_id=self.db_instance_id, **_params)

class _DDSBackupResource(ServiceResource):

    def __init__(self, backup_id,db_instance_id, _client=None):
        ServiceResource.__init__(self, "dds.backup", _client=_client)
        self.backup_id = backup_id
        self.db_instance_id = db_instance_id
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

    def restore_db_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.restore_db_instance(backup_id=self.backup_id,db_instance_id=self.db_instance_id, **_params)

class _DDSParameterResource(ServiceResource):

    def __init__(self, parameter_name, _client=None):
        ServiceResource.__init__(self, "dds.parameter", _client=_client)
        self.parameter_name = parameter_name
        
        self.checking_code = None
        self.force_restart = None
        self.modifiable_status = None
        self.parameter_description = None
        self.parameter_value = None

class _DDSRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "dds.region", _client=_client)
        self.region_id = region_id
        
        self.zone_ids = None
        self.zones = None

class _DDSReplicaResource(ServiceResource):

    def __init__(self, replica_id, _client=None):
        ServiceResource.__init__(self, "dds.replica", _client=_client)
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
