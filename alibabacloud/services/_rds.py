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


class _RDSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'rds', _client=_client)
        self.db_instances = _create_resource_collection(
            _RDSDBInstanceResource,
            _client,
            _client.describe_db_instances,
            'Items.DBInstance',
            'DBInstanceId',
            key_to_total_count="TotalRecordCount",
            key_to_page_size="PageRecordCount",
            key_to_page_number="PageNumber")
        self.migrate_tasks = _create_resource_collection(
            _RDSMigrateTaskResource,
            _client,
            _client.describe_migrate_tasks,
            'Items.MigrateTask',
            'MigrateTaskId',
            key_to_total_count="TotalRecordCount",
            key_to_page_size="PageRecordCount",
            key_to_page_number="PageNumber")
        self.parameters = _create_special_resource_collection(
            _RDSParameterResource, _client, _client.describe_parameters,
            'ConfigParameters.DBInstanceParameter', 'ParameterName',
        )
        self.regions = _create_special_resource_collection(
            _RDSRegionResource, _client, _client.describe_regions,
            'Regions.RDSRegion', 'RegionId',
        )
        self.slow_logs = _create_resource_collection(
            _RDSSlowLogResource,
            _client,
            _client.describe_slow_logs,
            'Items.SQLSlowLog',
            'SlowLogId',
            key_to_total_count="TotalRecordCount",
            key_to_page_size="PageRecordCount",
            key_to_page_number="PageNumber")
        self.tasks = _create_resource_collection(
            _RDSTaskResource, _client, _client.describe_tasks,
            'Items.TaskProgressInfo', 'TaskId',
        )

    def clone_db_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.clone_db_instance(**_params)
        db_instance_id = _new_get_key_in_response(response, 'DBInstanceId')
        return _RDSDBInstanceResource(db_instance_id, _client=self._client)

    def create_db_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_db_instance(**_params)
        db_instance_id = _new_get_key_in_response(response, 'DBInstanceId')
        return _RDSDBInstanceResource(db_instance_id, _client=self._client)

    def recovery_db_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.recovery_db_instance(**_params)
        db_instance_id = _new_get_key_in_response(response, 'DBInstanceId')
        return _RDSDBInstanceResource(db_instance_id, _client=self._client)

    def create_diagnostic_report(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_diagnostic_report(**_params)
        report_id = _new_get_key_in_response(response, 'ReportId')
        return _RDSDiagnosticReportResource(report_id, _client=self._client)


class _RDSDBInstanceResource(ServiceResource):

    def __init__(self, db_instance_id, _client=None):
        ServiceResource.__init__(self, "rds.db_instance", _client=_client)
        self.db_instance_id = db_instance_id

        self.auto_upgrade_minor_version = None
        self.category = None
        self.connection_mode = None
        self.create_time = None
        self.db_instance_class = None
        self.db_instance_description = None
        self.db_instance_net_type = None
        self.db_instance_status = None
        self.db_instance_storage_type = None
        self.db_instance_type = None
        self.destroy_time = None
        self.engine = None
        self.engine_version = None
        self.expire_time = None
        self.guard_db_instance_id = None
        self.ins_id = None
        self.instance_network_type = None
        self.lock_mode = None
        self.lock_reason = None
        self.master_instance_id = None
        self.mutri_orsignle = None
        self.pay_type = None
        self.read_only_db_instance_ids = None
        self.region_id = None
        self.replicate_id = None
        self.resource_group_id = None
        self.temp_db_instance_id = None
        self.vswitch_id = None
        self.vpc_cloud_instance_id = None
        self.vpc_id = None
        self.zone_id = None

        self.accounts = _create_sub_resource_without_page_collection(
            _RDSAccountResource,
            _client,
            _client.describe_accounts,
            'Accounts.DBInstanceAccount',
            'AccountName',
            parent_identifier="DBInstanceId",
            parent_identifier_value=self.db_instance_id)
        self.backups = _create_sub_resource_with_page_collection(
            _RDSBackupResource,
            _client,
            _client.describe_backups,
            'Items.Backup',
            'BackupId',
            parent_identifier="DBInstanceId",
            parent_identifier_value=self.db_instance_id,
            key_to_total_count="TotalRecordCount",
            key_to_page_size="PageRecordCount",
            key_to_page_number="PageNumber")
        self.dbs = _create_sub_resource_without_page_collection(
            _RDSDBResource,
            _client,
            _client.describe_databases,
            'Databases.Database',
            'DBName',
            parent_identifier="DBInstanceId",
            parent_identifier_value=self.db_instance_id)

    def add_tags_to_resource(self, **params):
        _params = _transfer_params(params)
        self._client.add_tags_to_resource(db_instance_id=self.db_instance_id, **_params)

    def allocate_instance_private_connection(self, **params):
        _params = _transfer_params(params)
        self._client.allocate_instance_private_connection(
            db_instance_id=self.db_instance_id, **_params)

    def allocate_instance_public_connection(self, **params):
        _params = _transfer_params(params)
        self._client.allocate_instance_public_connection(
            db_instance_id=self.db_instance_id, **_params)

    def allocate_instance_vpc_network_type(self, **params):
        _params = _transfer_params(params)
        self._client.allocate_instance_vpc_network_type(
            db_instance_id=self.db_instance_id, **_params)

    def allocate_read_write_splitting_connection(self, **params):
        _params = _transfer_params(params)
        self._client.allocate_read_write_splitting_connection(
            db_instance_id=self.db_instance_id, **_params)

    def calculate_db_instance_weight(self, **params):
        _params = _transfer_params(params)
        self._client.calculate_db_instance_weight(db_instance_id=self.db_instance_id, **_params)

    def cancel_import(self, **params):
        _params = _transfer_params(params)
        self._client.cancel_import(db_instance_id=self.db_instance_id, **_params)

    def check_instance_exist(self, **params):
        _params = _transfer_params(params)
        self._client.check_instance_exist(db_instance_id=self.db_instance_id, **_params)

    def check_recovery_conditions(self, **params):
        _params = _transfer_params(params)
        self._client.check_recovery_conditions(db_instance_id=self.db_instance_id, **_params)

    def copy_database_between_instances(self, **params):
        _params = _transfer_params(params)
        self._client.copy_database_between_instances(db_instance_id=self.db_instance_id, **_params)

    def create_read_only(self, **params):
        _params = _transfer_params(params)
        self._client.create_read_only_db_instance(db_instance_id=self.db_instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_db_instance(db_instance_id=self.db_instance_id, **_params)

    def descibe_imports_from_database(self, **params):
        _params = _transfer_params(params)
        self._client.descibe_imports_from_database(db_instance_id=self.db_instance_id, **_params)

    def describe_backup_database(self, **params):
        _params = _transfer_params(params)
        self._client.describe_backup_database(db_instance_id=self.db_instance_id, **_params)

    def describe_backup_policy(self, **params):
        _params = _transfer_params(params)
        self._client.describe_backup_policy(db_instance_id=self.db_instance_id, **_params)

    def describe_backup_tasks(self, **params):
        _params = _transfer_params(params)
        self._client.describe_backup_tasks(db_instance_id=self.db_instance_id, **_params)

    def describe_binlog_files(self, **params):
        _params = _transfer_params(params)
        self._client.describe_binlog_files(db_instance_id=self.db_instance_id, **_params)

    def describe_cloud_db_expert_service(self, **params):
        _params = _transfer_params(params)
        self._client.describe_cloud_db_expert_service(db_instance_id=self.db_instance_id, **_params)

    def describe_cross_region_backups(self, **params):
        _params = _transfer_params(params)
        self._client.describe_cross_region_backups(db_instance_id=self.db_instance_id, **_params)

    def describe_cross_region_log_backup_files(self, **params):
        _params = _transfer_params(params)
        self._client.describe_cross_region_log_backup_files(
            db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_attribute(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_ha_config(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_ha_config(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_ip_array_list(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_ip_array_list(
            db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_ip_hostname(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_ip_hostname(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_monitor(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_monitor(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_net_info(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_net_info(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_performance(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_performance(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_proxy_configuration(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_proxy_configuration(
            db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_ssl(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_ssl(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_tde(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_tde(db_instance_id=self.db_instance_id, **_params)

    def describe_dtc_security_ip_hosts_for_sql_server(self, **params):
        _params = _transfer_params(params)
        self._client.describe_dtc_security_ip_hosts_for_sql_server(
            db_instance_id=self.db_instance_id, **_params)

    def describe_diagnostic_report_list(self, **params):
        _params = _transfer_params(params)
        self._client.describe_diagnostic_report_list(db_instance_id=self.db_instance_id, **_params)

    def describe_error_logs(self, **params):
        _params = _transfer_params(params)
        self._client.describe_error_logs(db_instance_id=self.db_instance_id, **_params)

    def describe_instance_cross_backup_policy(self, **params):
        _params = _transfer_params(params)
        self._client.describe_instance_cross_backup_policy(
            db_instance_id=self.db_instance_id, **_params)

    def describe_instance_vpc_migrate_info(self, **params):
        _params = _transfer_params(params)
        self._client.describe_instance_vpc_migrate_info(
            db_instance_id=self.db_instance_id, **_params)

    def describe_log_backup_files(self, **params):
        _params = _transfer_params(params)
        self._client.describe_log_backup_files(db_instance_id=self.db_instance_id, **_params)

    def describe_meta_list(self, **params):
        _params = _transfer_params(params)
        self._client.describe_meta_list(db_instance_id=self.db_instance_id, **_params)

    def describe_migrate_tasks_for_sql_server(self, **params):
        _params = _transfer_params(params)
        self._client.describe_migrate_tasks_for_sql_server(
            db_instance_id=self.db_instance_id, **_params)

    def describe_modify_parameter_log(self, **params):
        _params = _transfer_params(params)
        self._client.describe_modify_parameter_log(db_instance_id=self.db_instance_id, **_params)

    def describe_oss_downloads(self, **params):
        _params = _transfer_params(params)
        self._client.describe_oss_downloads(db_instance_id=self.db_instance_id, **_params)

    def describe_oss_downloads_for_sql_server(self, **params):
        _params = _transfer_params(params)
        self._client.describe_oss_downloads_for_sql_server(
            db_instance_id=self.db_instance_id, **_params)

    def describe_proxy_function_support(self, **params):
        _params = _transfer_params(params)
        self._client.describe_proxy_function_support(db_instance_id=self.db_instance_id, **_params)

    def describe_read_db_instance_delay(self, **params):
        _params = _transfer_params(params)
        self._client.describe_read_db_instance_delay(db_instance_id=self.db_instance_id, **_params)

    def describe_resource_usage(self, **params):
        _params = _transfer_params(params)
        self._client.describe_resource_usage(db_instance_id=self.db_instance_id, **_params)

    def describe_sql_log_files(self, **params):
        _params = _transfer_params(params)
        self._client.describe_sql_log_files(db_instance_id=self.db_instance_id, **_params)

    def describe_sql_log_records(self, **params):
        _params = _transfer_params(params)
        self._client.describe_sql_log_records(db_instance_id=self.db_instance_id, **_params)

    def describe_sql_log_report_list(self, **params):
        _params = _transfer_params(params)
        self._client.describe_sql_log_report_list(db_instance_id=self.db_instance_id, **_params)

    def describe_sql_log_reports(self, **params):
        _params = _transfer_params(params)
        self._client.describe_sql_log_reports(db_instance_id=self.db_instance_id, **_params)

    def describe_sql_reports(self, **params):
        _params = _transfer_params(params)
        self._client.describe_sql_reports(db_instance_id=self.db_instance_id, **_params)

    def describe_security_group_configuration(self, **params):
        _params = _transfer_params(params)
        self._client.describe_security_group_configuration(
            db_instance_id=self.db_instance_id, **_params)

    def describe_slow_log_records(self, **params):
        _params = _transfer_params(params)
        self._client.describe_slow_log_records(db_instance_id=self.db_instance_id, **_params)

    def describe_task_info(self, **params):
        _params = _transfer_params(params)
        self._client.describe_task_info(db_instance_id=self.db_instance_id, **_params)

    def describe_templates_list(self, **params):
        _params = _transfer_params(params)
        self._client.describe_templates_list(db_instance_id=self.db_instance_id, **_params)

    def grant_operator_permission(self, **params):
        _params = _transfer_params(params)
        self._client.grant_operator_permission(db_instance_id=self.db_instance_id, **_params)

    def import_data_for_sql_server(self, **params):
        _params = _transfer_params(params)
        self._client.import_data_for_sql_server(db_instance_id=self.db_instance_id, **_params)

    def import_database_between_instances(self, **params):
        _params = _transfer_params(params)
        self._client.import_database_between_instances(
            db_instance_id=self.db_instance_id, **_params)

    def migrate_security_ip_mode(self, **params):
        _params = _transfer_params(params)
        self._client.migrate_security_ip_mode(db_instance_id=self.db_instance_id, **_params)

    def migrate_to_other_region(self, **params):
        _params = _transfer_params(params)
        self._client.migrate_to_other_region(db_instance_id=self.db_instance_id, **_params)

    def migrate_to_other_zone(self, **params):
        _params = _transfer_params(params)
        self._client.migrate_to_other_zone(db_instance_id=self.db_instance_id, **_params)

    def modify_auto_upgrade_minor_version(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_auto_upgrade_minor_version(
            db_instance_id=self.db_instance_id, **_params)

    def modify_backup_policy(self, **params):
        _params = _transfer_params(params)
        self._client.modify_backup_policy(db_instance_id=self.db_instance_id, **_params)

    def modify_collation_time_zone(self, **params):
        _params = _transfer_params(params)
        self._client.modify_collation_time_zone(db_instance_id=self.db_instance_id, **_params)

    def modify_connection_mode(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_connection_mode(
            db_instance_id=self.db_instance_id, **_params)

    def modify_connection_string(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_connection_string(
            db_instance_id=self.db_instance_id, **_params)

    def modify_dtc_security_ip_hosts_for_sql_server(self, **params):
        _params = _transfer_params(params)
        self._client.modify_dtc_security_ip_hosts_for_sql_server(
            db_instance_id=self.db_instance_id, **_params)

    def modify_description(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_description(db_instance_id=self.db_instance_id, **_params)

    def modify_instance_auto_renewal_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_auto_renewal_attribute(
            db_instance_id=self.db_instance_id, **_params)

    def modify_instance_cross_backup_policy(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_cross_backup_policy(
            db_instance_id=self.db_instance_id, **_params)

    def modify_maintain_time(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_maintain_time(db_instance_id=self.db_instance_id, **_params)

    def modify_monitor(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_monitor(db_instance_id=self.db_instance_id, **_params)

    def modify_my_sqldb_instance_delay(self, **params):
        _params = _transfer_params(params)
        self._client.modify_my_sqldb_instance_delay(db_instance_id=self.db_instance_id, **_params)

    def modify_network_expire_time(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_network_expire_time(
            db_instance_id=self.db_instance_id, **_params)

    def modify_network_type(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_network_type(db_instance_id=self.db_instance_id, **_params)

    def modify_parameter(self, **params):
        _params = _transfer_params(params)
        self._client.modify_parameter(db_instance_id=self.db_instance_id, **_params)

    def modify_pay_type(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_pay_type(db_instance_id=self.db_instance_id, **_params)

    def modify_proxy_configuration(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_proxy_configuration(
            db_instance_id=self.db_instance_id, **_params)

    def modify_read_write_splitting_connection(self, **params):
        _params = _transfer_params(params)
        self._client.modify_read_write_splitting_connection(
            db_instance_id=self.db_instance_id, **_params)

    def modify_readonly_instance_delay_replication_time(self, **params):
        _params = _transfer_params(params)
        self._client.modify_readonly_instance_delay_replication_time(
            db_instance_id=self.db_instance_id, **_params)

    def modify_resource_group(self, **params):
        _params = _transfer_params(params)
        self._client.modify_resource_group(db_instance_id=self.db_instance_id, **_params)

    def modify_sql_collector_policy(self, **params):
        _params = _transfer_params(params)
        self._client.modify_sql_collector_policy(db_instance_id=self.db_instance_id, **_params)

    def modify_ssl(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_ssl(db_instance_id=self.db_instance_id, **_params)

    def modify_security_group_configuration(self, **params):
        _params = _transfer_params(params)
        self._client.modify_security_group_configuration(
            db_instance_id=self.db_instance_id, **_params)

    def modify_security_ips(self, **params):
        _params = _transfer_params(params)
        self._client.modify_security_ips(db_instance_id=self.db_instance_id, **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_spec(db_instance_id=self.db_instance_id, **_params)

    def modify_tde(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_tde(db_instance_id=self.db_instance_id, **_params)

    def purge_db_instance_log(self, **params):
        _params = _transfer_params(params)
        self._client.purge_db_instance_log(db_instance_id=self.db_instance_id, **_params)

    def release_instance_public_connection(self, **params):
        _params = _transfer_params(params)
        self._client.release_instance_public_connection(
            db_instance_id=self.db_instance_id, **_params)

    def release_read_write_splitting_connection(self, **params):
        _params = _transfer_params(params)
        self._client.release_read_write_splitting_connection(
            db_instance_id=self.db_instance_id, **_params)

    def remove_tags_from_resource(self, **params):
        _params = _transfer_params(params)
        self._client.remove_tags_from_resource(db_instance_id=self.db_instance_id, **_params)

    def renew_instance(self, **params):
        _params = _transfer_params(params)
        self._client.renew_instance(db_instance_id=self.db_instance_id, **_params)

    def request_service_of_cloud_db_expert(self, **params):
        _params = _transfer_params(params)
        self._client.request_service_of_cloud_db_expert(
            db_instance_id=self.db_instance_id, **_params)

    def restart(self, **params):
        _params = _transfer_params(params)
        self._client.restart_db_instance(db_instance_id=self.db_instance_id, **_params)

    def restore(self, **params):
        _params = _transfer_params(params)
        self._client.restore_db_instance(db_instance_id=self.db_instance_id, **_params)

    def restore_table(self, **params):
        _params = _transfer_params(params)
        self._client.restore_table(db_instance_id=self.db_instance_id, **_params)

    def revoke_operator_permission(self, **params):
        _params = _transfer_params(params)
        self._client.revoke_operator_permission(db_instance_id=self.db_instance_id, **_params)

    def switch_db_instance_ha(self, **params):
        _params = _transfer_params(params)
        self._client.switch_db_instance_ha(db_instance_id=self.db_instance_id, **_params)

    def switch_db_instance_net_type(self, **params):
        _params = _transfer_params(params)
        self._client.switch_db_instance_net_type(db_instance_id=self.db_instance_id, **_params)

    def switch_db_instance_vpc(self, **params):
        _params = _transfer_params(params)
        self._client.switch_db_instance_vpc(db_instance_id=self.db_instance_id, **_params)

    def upgrade_db_instance_engine_version(self, **params):
        _params = _transfer_params(params)
        self._client.upgrade_db_instance_engine_version(
            db_instance_id=self.db_instance_id, **_params)

    def upgrade_db_instance_kernel_version(self, **params):
        _params = _transfer_params(params)
        self._client.upgrade_db_instance_kernel_version(
            db_instance_id=self.db_instance_id, **_params)

    def create_account(self, **params):
        _params = _transfer_params(params)
        self._client.create_account(db_instance_id=self.db_instance_id,**_params)
        account_name = _params.get("account_name")
        return _RDSAccountResource(account_name,self.db_instance_id, _client=self._client)

    def create_backup(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_backup(db_instance_id=self.db_instance_id,**_params)
        backup_id = _new_get_key_in_response(response, 'BackupJobId')
        return _RDSBackupResource(backup_id,self.db_instance_id, _client=self._client)

    def create_database(self, **params):
        _params = _transfer_params(params)
        self._client.create_database(db_instance_id=self.db_instance_id,**_params)
        db_name = _params.get("db_name")
        return _RDSDBResource(db_name,self.db_instance_id, _client=self._client)

    def create_temp_db_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_temp_db_instance(
            db_instance_id=self.db_instance_id,**_params)
        temp_db_instance_id = _new_get_key_in_response(response, 'TempDBInstanceId')
        return _RDSTempDBInstanceResource(
            temp_db_instance_id,
            self.db_instance_id,
            _client=self._client)

    def refresh(self):
        result = self._client.describe_db_instances(db_instance_id=self.db_instance_id)
        items = _new_get_key_in_response(result, 'Items.DBInstance')
        if not items:
            raise ClientException(
                msg="Failed to find db_instance data from DescribeDBInstances response. "
                "DBInstanceId = {0}".format(
                    self.db_instance_id))
        self._assign_attributes(items[0])


class _RDSAccountResource(ServiceResource):

    def __init__(self, account_name,db_instance_id, _client=None):
        ServiceResource.__init__(self, "rds.account", _client=_client)
        self.account_name = account_name
        self.db_instance_id = db_instance_id
        self.account_description = None
        self.account_status = None
        self.account_type = None
        self.database_privileges = None
        self.priv_exceeded = None

    def check_account_name_available(self, **params):
        _params = _transfer_params(params)
        self._client.check_account_name_available(
            account_name=self.account_name,
            db_instance_id=self.db_instance_id,
            **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_account(
            account_name=self.account_name,
            db_instance_id=self.db_instance_id,
            **_params)

    def modify_description(self, **params):
        _params = _transfer_params(params)
        self._client.modify_account_description(
            account_name=self.account_name,
            db_instance_id=self.db_instance_id,
            **_params)

    def reset(self, **params):
        _params = _transfer_params(params)
        self._client.reset_account(
            account_name=self.account_name,
            db_instance_id=self.db_instance_id,
            **_params)

    def reset_account_for_pg(self, **params):
        _params = _transfer_params(params)
        self._client.reset_account_for_pg(
            account_name=self.account_name,
            db_instance_id=self.db_instance_id,
            **_params)

    def reset_account_password(self, **params):
        _params = _transfer_params(params)
        self._client.reset_account_password(
            account_name=self.account_name,
            db_instance_id=self.db_instance_id,
            **_params)

    def grant_account_privilege(self, **params):
        _params = _transfer_params(params)
        self._client.grant_account_privilege(
            account_name=self.account_name,
            db_instance_id=self.db_instance_id,
            **_params)

    def revoke_account_privilege(self, **params):
        _params = _transfer_params(params)
        self._client.revoke_account_privilege(
            account_name=self.account_name,
            db_instance_id=self.db_instance_id,
            **_params)

    def refresh(self):
        result = self._client.describe_accounts(
            account_name=self.account_name,
            db_instance_id=self.db_instance_id)
        items = _new_get_key_in_response(result, 'Accounts.DBInstanceAccount')
        if not items:
            raise ClientException(msg="Failed to find account data from DescribeAccounts response. "
                                  "AccountName = {0}".format(self.account_name))
        self._assign_attributes(items[0])

    def wait_until(self, target_account_status, timeout=120):
        start_time = time.time()
        while True:
            end_time = time.time()
            if end_time - start_time >= timeout:
                raise Exception("Timed out: no {0} status after {1} seconds.".format(
                    target_account_status, timeout))

            self.refresh()
            if self.account_status == target_account_status:
                return
            time.sleep(1)


class _RDSBackupResource(ServiceResource):

    def __init__(self, backup_id,db_instance_id, _client=None):
        ServiceResource.__init__(self, "rds.backup", _client=_client)
        self.backup_id = backup_id
        self.db_instance_id = db_instance_id
        self.backup_db_names = None
        self.backup_download_url = None
        self.backup_end_time = None
        self.backup_extraction_status = None
        self.backup_intranet_download_url = None
        self.backup_location = None
        self.backup_method = None
        self.backup_mode = None
        self.backup_scale = None
        self.backup_size = None
        self.backup_start_time = None
        self.backup_status = None
        self.backup_type = None
        self.host_instance_id = None
        self.meta_status = None
        self.slave_status = None
        self.store_status = None
        self.total_backup_size = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_backup(
            backup_id=self.backup_id,
            db_instance_id=self.db_instance_id,
            **_params)

    def refresh(self):
        result = self._client.describe_backups(
            backup_id=self.backup_id,
            db_instance_id=self.db_instance_id)
        items = _new_get_key_in_response(result, 'Items.Backup')
        if not items:
            raise ClientException(msg="Failed to find backup data from DescribeBackups response. "
                                  "BackupId = {0}".format(self.backup_id))
        self._assign_attributes(items[0])

    def wait_until(self, target_backup_status, timeout=120):
        start_time = time.time()
        while True:
            end_time = time.time()
            if end_time - start_time >= timeout:
                raise Exception("Timed out: no {0} status after {1} seconds.".format(
                    target_backup_status, timeout))

            self.refresh()
            if self.backup_status == target_backup_status:
                return
            time.sleep(1)


class _RDSDBResource(ServiceResource):

    def __init__(self, db_name,db_instance_id, _client=None):
        ServiceResource.__init__(self, "rds.db", _client=_client)
        self.db_name = db_name
        self.db_instance_id = db_instance_id
        self.accounts = None
        self.character_set_name = None
        self.db_description = None
        self.db_status = None
        self.engine = None

    def create_migrate_task(self, **params):
        _params = _transfer_params(params)
        self._client.create_migrate_task(
            db_name=self.db_name,
            db_instance_id=self.db_instance_id,
            **_params)

    def create_migrate_task_for_sql_server(self, **params):
        _params = _transfer_params(params)
        self._client.create_migrate_task_for_sql_server(
            db_name=self.db_name,db_instance_id=self.db_instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_database(
            db_name=self.db_name,
            db_instance_id=self.db_instance_id,
            **_params)

    def modify_db_description(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_description(
            db_name=self.db_name,
            db_instance_id=self.db_instance_id,
            **_params)

    def create_online_database_task(self, **params):
        _params = _transfer_params(params)
        self._client.create_online_database_task(
            db_name=self.db_name,db_instance_id=self.db_instance_id, **_params)

    def refresh(self):
        result = self._client.describe_databases(
            db_name=self.db_name,db_instance_id=self.db_instance_id)
        items = _new_get_key_in_response(result, 'Databases.Database')
        if not items:
            raise ClientException(msg="Failed to find db data from DescribeDatabases response. "
                                  "DBName = {0}".format(self.db_name))
        self._assign_attributes(items[0])

    def wait_until(self, target_db_status, timeout=120):
        start_time = time.time()
        while True:
            end_time = time.time()
            if end_time - start_time >= timeout:
                raise Exception("Timed out: no {0} status after {1} seconds.".format(
                    target_db_status, timeout))

            self.refresh()
            if self.db_status == target_db_status:
                return
            time.sleep(1)


class _RDSTempDBInstanceResource(ServiceResource):

    def __init__(self, temp_db_instance_id,db_instance_id, _client=None):
        ServiceResource.__init__(self, "rds.temp_db_instance", _client=_client)
        self.temp_db_instance_id = temp_db_instance_id
        self.db_instance_id = db_instance_id


class _RDSDiagnosticReportResource(ServiceResource):

    def __init__(self, report_id, _client=None):
        ServiceResource.__init__(self, "rds.diagnostic_report", _client=_client)
        self.report_id = report_id


class _RDSMigrateTaskResource(ServiceResource):

    def __init__(self, migrate_task_id, _client=None):
        ServiceResource.__init__(self, "rds.migrate_task", _client=_client)
        self.migrate_task_id = migrate_task_id

        self.backup_mode = None
        self.create_time = None
        self.db_name = None
        self.description = None
        self.end_time = None
        self.is_db_replaced = None
        self.status = None


class _RDSParameterResource(ServiceResource):

    def __init__(self, parameter_name, _client=None):
        ServiceResource.__init__(self, "rds.parameter", _client=_client)
        self.parameter_name = parameter_name

        self.parameter_description = None
        self.parameter_value = None


class _RDSRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "rds.region", _client=_client)
        self.region_id = region_id

        self.local_name = None
        self.region_endpoint = None
        self.status = None

    def refresh(self):
        result = self._client.describe_regions(region_id=self.region_id)
        items = _new_get_key_in_response(result, 'Regions.Region')
        if not items:
            raise ClientException(msg="Failed to find region data from DescribeRegions response. "
                                  "RegionId = {0}".format(self.region_id))
        self._assign_attributes(items[0])


class _RDSSlowLogResource(ServiceResource):

    def __init__(self, slow_log_id, _client=None):
        ServiceResource.__init__(self, "rds.slow_log", _client=_client)
        self.slow_log_id = slow_log_id

        self.avg_execution_time = None
        self.create_time = None
        self.db_name = None
        self.max_execution_time = None
        self.max_lock_time = None
        self.my_sql_total_execution_counts = None
        self.my_sql_total_execution_times = None
        self.parse_max_row_count = None
        self.parse_total_row_counts = None
        self.report_time = None
        self.return_max_row_count = None
        self.return_total_row_counts = None
        self.sqlhash = None
        self.sql_id_str = None
        self.sql_server_total_execution_counts = None
        self.sql_server_total_execution_times = None
        self.sql_text = None
        self.total_lock_times = None
        self.total_logical_read_counts = None
        self.total_physical_read_counts = None


class _RDSTaskResource(ServiceResource):

    def __init__(self, task_id, _client=None):
        ServiceResource.__init__(self, "rds.task", _client=_client)
        self.task_id = task_id

        self.creation_time = None
        self.finished_time = None
        self.support_cancel = None
        self.task_action = None
        self.task_status = None

    def refresh(self):
        result = self._client.describe_tasks(task_ids=self.task_id)
        items = _new_get_key_in_response(result, 'TaskSet.Task')
        if not items:
            raise ClientException(msg="Failed to find task data from DescribeTasks response. "
                                  "TaskId = {0}".format(self.task_id))
        self._assign_attributes(items[0])
