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


class _POLARDBResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'polardb', _client=_client)
        self.db_clusters = _create_resource_collection(
            _POLARDBDBClusterResource, _client, _client.describe_db_clusters,
            'Items.DBCluster', 'DBClusterId', key_to_total_count="TotalRecordCount",key_to_page_size="PageRecordCount",key_to_page_number="PageNumber"
        )
        self.regions = _create_special_resource_collection(
            _POLARDBRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId', 
        )
    def create_db_cluster(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_db_cluster(**_params)
        db_cluster_id = _new_get_key_in_response(response, 'DBClusterId')
        return _POLARDBDBClusterResource(db_cluster_id, _client=self._client)

class _POLARDBDBClusterResource(ServiceResource):

    def __init__(self, db_cluster_id, _client=None):
        ServiceResource.__init__(self, "polardb.db_cluster", _client=_client)
        self.db_cluster_id = db_cluster_id
        
        self.create_time = None
        self.db_cluster_description = None
        self.db_cluster_network_type = None
        self.db_cluster_status = None
        self.db_node_class = None
        self.db_node_number = None
        self.db_nodes = None
        self.db_type = None
        self.db_version = None
        self.deletion_lock = None
        self.engine = None
        self.expire_time = None
        self.expired = None
        self.lock_mode = None
        self.pay_type = None
        self.region_id = None
        self.storage_used = None
        self.tags = None
        self.vpc_id = None
        self.zone_id = None

        self.accounts = _create_sub_resource_without_page_collection(
            _POLARDBAccountResource, _client, _client.describe_accounts,
            'Accounts.DBAccount', 'AccountName', parent_identifier="DBClusterId",parent_identifier_value=self.db_cluster_id
        )
        self.backups = _create_sub_resource_with_page_collection(
            _POLARDBBackupResource, _client, _client.describe_backups,
            'Items.Backup', 'BackupId', parent_identifier="DBClusterId",parent_identifier_value=self.db_cluster_id,key_to_total_count="TotalRecordCount",key_to_page_size="PageRecordCount",key_to_page_number="PageNumber"
        )
        self.databases = _create_sub_resource_without_page_collection(
            _POLARDBDatabaseResource, _client, _client.describe_databases,
            'Databases.Database', 'DatabaseName', parent_identifier="DBClusterId",parent_identifier_value=self.db_cluster_id
        )
    def modify_auto_renew_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_auto_renew_attribute(db_cluster_id=self.db_cluster_id, **_params)

    def abort_db_cluster_migration(self, **params):
        _params = _transfer_params(params)
        return self._client.abort_db_cluster_migration(db_cluster_id=self.db_cluster_id, **_params)

    def close_db_cluster_migration(self, **params):
        _params = _transfer_params(params)
        return self._client.close_db_cluster_migration(db_cluster_id=self.db_cluster_id, **_params)

    def continue_db_cluster_migration(self, **params):
        _params = _transfer_params(params)
        return self._client.continue_db_cluster_migration(db_cluster_id=self.db_cluster_id, **_params)

    def create_db_cluster_endpoint(self, **params):
        _params = _transfer_params(params)
        return self._client.create_db_cluster_endpoint(db_cluster_id=self.db_cluster_id, **_params)

    def create_db_endpoint_address(self, **params):
        _params = _transfer_params(params)
        return self._client.create_db_endpoint_address(db_cluster_id=self.db_cluster_id, **_params)

    def create_db_nodes(self, **params):
        _params = _transfer_params(params)
        return self._client.create_db_nodes(db_cluster_id=self.db_cluster_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_db_cluster(db_cluster_id=self.db_cluster_id, **_params)

    def delete_db_endpoint_address(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_db_endpoint_address(db_cluster_id=self.db_cluster_id, **_params)

    def delete_db_nodes(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_db_nodes(db_cluster_id=self.db_cluster_id, **_params)

    def describe_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_backup_policy(db_cluster_id=self.db_cluster_id, **_params)

    def describe_db_cluster_access_whitelist(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_cluster_access_whitelist(db_cluster_id=self.db_cluster_id, **_params)

    def describe_db_cluster_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_cluster_attribute(db_cluster_id=self.db_cluster_id, **_params)

    def describe_db_cluster_endpoints(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_cluster_endpoints(db_cluster_id=self.db_cluster_id, **_params)

    def describe_db_cluster_migration(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_cluster_migration(db_cluster_id=self.db_cluster_id, **_params)

    def describe_db_cluster_parameters(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_cluster_parameters(db_cluster_id=self.db_cluster_id, **_params)

    def lock_db_cluster_deletion(self, **params):
        _params = _transfer_params(params)
        return self._client.lock_db_cluster_deletion(db_cluster_id=self.db_cluster_id, **_params)

    def modify_access_whitelist(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_cluster_access_whitelist(db_cluster_id=self.db_cluster_id, **_params)

    def modify_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_backup_policy(db_cluster_id=self.db_cluster_id, **_params)

    def modify_db_endpoint_address(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_endpoint_address(db_cluster_id=self.db_cluster_id, **_params)

    def modify_db_node_class(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_node_class(db_cluster_id=self.db_cluster_id, **_params)

    def modify_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_cluster_description(db_cluster_id=self.db_cluster_id, **_params)

    def modify_maintain_time(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_cluster_maintain_time(db_cluster_id=self.db_cluster_id, **_params)

    def modify_migration(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_cluster_migration(db_cluster_id=self.db_cluster_id, **_params)

    def modify_parameters(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_cluster_parameters(db_cluster_id=self.db_cluster_id, **_params)

    def unlock_db_cluster_deletion(self, **params):
        _params = _transfer_params(params)
        return self._client.unlock_db_cluster_deletion(db_cluster_id=self.db_cluster_id, **_params)

    def delete_db_cluster_endpoint(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_db_cluster_endpoint(db_cluster_id=self.db_cluster_id, **_params)

    def modify_endpoint(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_cluster_endpoint(db_cluster_id=self.db_cluster_id, **_params)

    def create_account(self, **params):
        _params = _transfer_params(params)
        self._client.create_account(db_cluster_id=self.db_cluster_id,**_params)
        account_name = _params.get("account_name")
        return _POLARDBAccountResource(account_name,self.db_cluster_id, _client=self._client)

    def create_backup(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_backup(db_cluster_id=self.db_cluster_id,**_params)
        backup_id = _new_get_key_in_response(response, 'BackupId')
        return _POLARDBBackupResource(backup_id,self.db_cluster_id, _client=self._client)

    def create_database(self, **params):
        _params = _transfer_params(params)
        self._client.create_database(db_cluster_id=self.db_cluster_id,**_params)
        database_name = _params.get("database_name")
        return _POLARDBDatabaseResource(database_name,self.db_cluster_id, _client=self._client)

class _POLARDBAccountResource(ServiceResource):

    def __init__(self, account_name,db_cluster_id, _client=None):
        ServiceResource.__init__(self, "polardb.account", _client=_client)
        self.account_name = account_name
        self.db_cluster_id = db_cluster_id
        self.account_description = None
        self.account_status = None
        self.account_type = None
        self.database_privileges = None
        self.privilege_exceeded = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_account(account_name=self.account_name,db_cluster_id=self.db_cluster_id, **_params)

    def modify_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_account_description(account_name=self.account_name,db_cluster_id=self.db_cluster_id, **_params)

    def modify_password(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_account_password(account_name=self.account_name,db_cluster_id=self.db_cluster_id, **_params)

    def reset(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_account(account_name=self.account_name,db_cluster_id=self.db_cluster_id, **_params)

    def grant_account_privilege(self, **params):
        _params = _transfer_params(params)
        return self._client.grant_account_privilege(account_name=self.account_name,db_cluster_id=self.db_cluster_id, **_params)

    def revoke_account_privilege(self, **params):
        _params = _transfer_params(params)
        return self._client.revoke_account_privilege(account_name=self.account_name,db_cluster_id=self.db_cluster_id, **_params)

class _POLARDBBackupResource(ServiceResource):

    def __init__(self, backup_id,db_cluster_id, _client=None):
        ServiceResource.__init__(self, "polardb.backup", _client=_client)
        self.backup_id = backup_id
        self.db_cluster_id = db_cluster_id
        self.backup_end_time = None
        self.backup_method = None
        self.backup_mode = None
        self.backup_set_size = None
        self.backup_start_time = None
        self.backup_status = None
        self.backup_type = None
        self.store_status = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_backup(backup_id=self.backup_id,db_cluster_id=self.db_cluster_id, **_params)

class _POLARDBDatabaseResource(ServiceResource):

    def __init__(self, database_name,db_cluster_id, _client=None):
        ServiceResource.__init__(self, "polardb.database", _client=_client)
        self.database_name = database_name
        self.db_cluster_id = db_cluster_id
        self.accounts = None
        self.character_set_name = None
        self.db_description = None
        self.db_name = None
        self.db_status = None
        self.engine = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_database(database_name=self.database_name,db_cluster_id=self.db_cluster_id, **_params)

    def modify_db_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_description(database_name=self.database_name,db_cluster_id=self.db_cluster_id, **_params)

class _POLARDBRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "polardb.region", _client=_client)
        self.region_id = region_id
        
        self.zones = None
