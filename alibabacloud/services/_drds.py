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


class _DRDSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'drds', _client=_client)
        self.regions = _create_special_resource_collection(
            _DRDSRegionResource, _client, _client.describe_drds_regions,
            'Regions.Region', 'RegionId', 
        )
    def create_drds_db_pre_check(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_drds_db_pre_check(**_params)
        task_id = _new_get_key_in_response(response, 'TaskId')
        return _DRDSDBPreCheckResource(task_id, _client=self._client)

    def create_instance_internet_address(self, **params):
        _params = _transfer_params(params)
        self._client.create_instance_internet_address(**_params)
        instance_internet_address_name = _params.get("instance_internet_address_name")
        return _DRDSInstanceInternetAddressResource(instance_internet_address_name, _client=self._client)

class _DRDSDBPreCheckResource(ServiceResource):

    def __init__(self, task_id, _client=None):
        ServiceResource.__init__(self, "drds.db_pre_check", _client=_client)
        self.task_id = task_id
        

class _DRDSInstanceInternetAddressResource(ServiceResource):

    def __init__(self, instance_internet_address_name, _client=None):
        ServiceResource.__init__(self, "drds.instance_internet_address", _client=_client)
        self.instance_internet_address_name = instance_internet_address_name
        

    def change_account_password(self, **params):
        _params = _transfer_params(params)
        return self._client.change_account_password(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def change_instance_azone(self, **params):
        _params = _transfer_params(params)
        return self._client.change_instance_azone(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def change_instance_network(self, **params):
        _params = _transfer_params(params)
        return self._client.change_instance_network(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def check_capacity_data_ready(self, **params):
        _params = _transfer_params(params)
        return self._client.check_capacity_data_ready(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def check_db_name(self, **params):
        _params = _transfer_params(params)
        return self._client.check_drds_db_name(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def check_expand_status(self, **params):
        _params = _transfer_params(params)
        return self._client.check_expand_status(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def check_rds_expand_status(self, **params):
        _params = _transfer_params(params)
        return self._client.check_rds_expand_status(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def check_rds_super_account(self, **params):
        _params = _transfer_params(params)
        return self._client.check_rds_super_account(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def check_sql_audit_enable_status(self, **params):
        _params = _transfer_params(params)
        return self._client.check_sql_audit_enable_status(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def configure_db_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.configure_drds_db_instances(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def create_db(self, **params):
        _params = _transfer_params(params)
        return self._client.create_drds_db(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def create_db_preview(self, **params):
        _params = _transfer_params(params)
        return self._client.create_drds_db_preview(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def create_instance_account(self, **params):
        _params = _transfer_params(params)
        return self._client.create_instance_account(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def create_shard_task(self, **params):
        _params = _transfer_params(params)
        return self._client.create_shard_task(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def datalink_replication_precheck(self, **params):
        _params = _transfer_params(params)
        return self._client.datalink_replication_precheck(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def delete_shard_tasks(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_shard_tasks(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_back_menu(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_back_menu(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_backup_dbs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_backup_dbs(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_backup_local(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_backup_local(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_backup_policy(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_backup_sets(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_backup_sets(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_backup_times(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_backup_times(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_broadcast_tables(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_broadcast_tables(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_can_expand_instance_detail_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_can_expand_instance_detail_list(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_candidate_instance_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_candidate_instance_list(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_db(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_db(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_db_cluster(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_db_cluster(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_db_ip_white_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_db_ip_white_list(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_dbs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_dbs(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_db_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_db_instance(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_db_instance_dbs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_instance_dbs(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_db_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_db_instances(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_db_rds_name_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_db_rds_name_list(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_db_rds_relation_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_db_rds_relation_info(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_db_relation_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_db_relation_info(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_db_tasks(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_db_tasks(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_expand_logic_table_info_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_expand_logic_table_info_list(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_global_broadcast_type(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_global_broadcast_type(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_hi_store_instance_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_hi_store_instance_info(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_hot_db_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_hot_db_list(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_inst_db_log_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_inst_db_log_info(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_inst_db_sls_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_inst_db_sls_info(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_instance(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_instance_accounts(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_instance_accounts(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_instance_db_monitor(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_instance_db_monitor(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_instance_level_tasks(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_instance_level_tasks(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_instance_menu_switch(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_instance_menu_switch(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_instance_monitor(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_instance_monitor(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_instance_switch_azone(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_instance_switch_azone(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_instance_switch_network(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_instance_switch_network(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_instance_version(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_instance_version(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_params(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_params(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_pre_check_result(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_pre_check_result(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_rds_performance(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_rds_performance(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_rds_commodity(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_rds_commodity(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_rds_performance_summary(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_rds_performance_summary(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_rds_super_account_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_rds_super_account_instances(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_recycle_bin_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_recycle_bin_status(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_recycle_bin_tables(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_recycle_bin_tables(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_restore_order(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_restore_order(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_shard_task_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_shard_task_info(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_shard_task_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_shard_task_list(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_sharding_dbs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_sharding_dbs(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_slow_sqls(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_slow_sqls(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_sql_audit_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_sql_audit_status(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_sql_flashbak_task(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_sql_flashbak_task(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_src_rds_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_src_rds_list(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_storage_instance_sub_db_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_storage_instance_sub_db_info(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_table(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_table(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_table_list_by_type(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_table_list_by_type(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_tables(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_tables(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def describe_tasks(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_drds_tasks(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def disable_sql_audit(self, **params):
        _params = _transfer_params(params)
        return self._client.disable_sql_audit(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def enable_instance_ipv6_address(self, **params):
        _params = _transfer_params(params)
        return self._client.enable_instance_ipv6_address(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def enable_sql_audit(self, **params):
        _params = _transfer_params(params)
        return self._client.enable_sql_audit(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def enable_sql_flashback_match_switch(self, **params):
        _params = _transfer_params(params)
        return self._client.enable_sql_flashback_match_switch(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def flashback_recycle_bin_table(self, **params):
        _params = _transfer_params(params)
        return self._client.flashback_recycle_bin_table(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def get_candidate_instance_list(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_candidate_instance_list(instance_internet_address_name=self.instance_internet_address_name, **_params)
        return response

    def get_expand_logic_table_info_list(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_expand_logic_table_info_list(instance_internet_address_name=self.instance_internet_address_name, **_params)
        return response

    def get_hot_db_list(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_hot_db_list(instance_internet_address_name=self.instance_internet_address_name, **_params)
        return response

    def get_logic_table_info_list(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_logic_table_info_list(instance_internet_address_name=self.instance_internet_address_name, **_params)
        return response

    def get_src_rds_list(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_src_rds_list(instance_internet_address_name=self.instance_internet_address_name, **_params)
        return response

    def modify_account_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_account_description(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def modify_account_privilege(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_account_privilege(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def modify_instance_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_drds_instance_description(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def modify_ip_white_list(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_drds_ip_white_list(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def modify_polar_db_read_weight(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_polar_db_read_weight(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def modify_rds_read_weight(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_rds_read_weight(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def pre_check_create_hi_store_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.pre_check_create_hi_store_instance(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def pre_check_sql_flashback_task(self, **params):
        _params = _transfer_params(params)
        return self._client.pre_check_sql_flashback_task(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def put_restore_pre_check(self, **params):
        _params = _transfer_params(params)
        return self._client.put_restore_pre_check(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def put_start_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.put_start_backup(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def rearrange_db_to_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.rearrange_db_to_instance(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def refresh_atom_url(self, **params):
        _params = _transfer_params(params)
        return self._client.refresh_drds_atom_url(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def refresh_jst_migrate_db_atom_url(self, **params):
        _params = _transfer_params(params)
        return self._client.refresh_jst_migrate_drds_db_atom_url(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def release(self, **params):
        _params = _transfer_params(params)
        return self._client.release_instance_internet_address(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def release_hi_store_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.release_hi_store_instance(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def remove_backups_set(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_backups_set(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def remove_db(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_drds_db(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def remove_db_failed_record(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_drds_db_failed_record(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def remove_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_drds_instance(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def remove_instance_account(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_instance_account(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def remove_recycle_bin_table(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_recycle_bin_table(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def reset_to_rds_connections(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_drds_to_rds_connections(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def restart_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.restart_drds_instance(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def rollback_hi_store_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.rollback_hi_store_instance(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def rollback_instance_version(self, **params):
        _params = _transfer_params(params)
        return self._client.rollback_instance_version(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def set_backup_local(self, **params):
        _params = _transfer_params(params)
        return self._client.set_backup_local(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def set_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.set_backup_policy(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def setup_broadcast_tables(self, **params):
        _params = _transfer_params(params)
        return self._client.setup_broadcast_tables(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def setup_params(self, **params):
        _params = _transfer_params(params)
        return self._client.setup_drds_params(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def setup_recycle_bin_status(self, **params):
        _params = _transfer_params(params)
        return self._client.setup_recycle_bin_status(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def setup_table(self, **params):
        _params = _transfer_params(params)
        return self._client.setup_table(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def start_restore(self, **params):
        _params = _transfer_params(params)
        return self._client.start_restore(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def submit_clean_task(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_clean_task(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def submit_hot_expand_pre_check_task(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_hot_expand_pre_check_task(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def submit_hot_expand_task(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_hot_expand_task(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def submit_rollback_task(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_rollback_task(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def submit_smooth_expand_pre_check(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_smooth_expand_pre_check(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def submit_smooth_expand_pre_check_task(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_smooth_expand_pre_check_task(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def submit_smooth_expand_task(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_smooth_expand_task(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def submit_sql_flashback_task(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_sql_flashback_task(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def submit_switch_task(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_switch_task(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def switch_global_broadcast_type(self, **params):
        _params = _transfer_params(params)
        return self._client.switch_global_broadcast_type(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def update_instance_network(self, **params):
        _params = _transfer_params(params)
        return self._client.update_instance_network(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def upgrade_hi_store_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.upgrade_hi_store_instance(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def upgrade_instance_version(self, **params):
        _params = _transfer_params(params)
        return self._client.upgrade_instance_version(instance_internet_address_name=self.instance_internet_address_name, **_params)

    def validate_shard_task(self, **params):
        _params = _transfer_params(params)
        return self._client.validate_shard_task(instance_internet_address_name=self.instance_internet_address_name, **_params)

class _DRDSRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "drds.region", _client=_client)
        self.region_id = region_id
        
        self.region_endpoint = None
        self.region_name = None
