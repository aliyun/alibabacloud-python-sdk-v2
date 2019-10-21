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


class _ADBResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'adb', _client=_client)
        self.backups = _create_resource_collection(
            _ADBBackupResource, _client, _client.describe_backups,
            'Items.Backup', 'BackupId', 
        )
        self.db_clusters = _create_resource_collection(
            _ADBDBClusterResource, _client, _client.describe_db_clusters,
            'Items.DBCluster', 'DBClusterId', 
        )
        self.regions = _create_special_resource_collection(
            _ADBRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId', 
        )
class _ADBBackupResource(ServiceResource):

    def __init__(self, backup_id, _client=None):
        ServiceResource.__init__(self, "adb.backup", _client=_client)
        self.backup_id = backup_id
        
        self.backup_end_time = None
        self.backup_method = None
        self.backup_size = None
        self.backup_start_time = None
        self.backup_type = None
        self.db_cluster_id = None

class _ADBDBClusterResource(ServiceResource):

    def __init__(self, db_cluster_id, _client=None):
        ServiceResource.__init__(self, "adb.db_cluster", _client=_client)
        self.db_cluster_id = db_cluster_id
        
        self.commodity_code = None
        self.create_time = None
        self.db_cluster_description = None
        self.db_cluster_status = None
        self.db_cluster_type = None
        self.db_node_class = None
        self.db_node_count = None
        self.db_node_storage = None
        self.db_version = None
        self.expire_time = None
        self.expired = None
        self.lock_mode = None
        self.lock_reason = None
        self.pay_type = None
        self.region_id = None
        self.tags = None

        self.accounts = _create_sub_resource_without_page_collection(
            _ADBAccountResource, _client, _client.describe_accounts,
            'AccountList.DBAccount', 'AccountName', parent_identifier="DBClusterId",parent_identifier_value=self.db_cluster_id
        )
    def allocate_cluster_public_connection(self, **params):
        _params = _transfer_params(params)
        return self._client.allocate_cluster_public_connection(db_cluster_id=self.db_cluster_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_db_cluster(db_cluster_id=self.db_cluster_id, **_params)

    def describe_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_backup_policy(db_cluster_id=self.db_cluster_id, **_params)

    def describe_db_cluster_access_white_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_cluster_access_white_list(db_cluster_id=self.db_cluster_id, **_params)

    def describe_db_cluster_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_cluster_attribute(db_cluster_id=self.db_cluster_id, **_params)

    def describe_db_cluster_net_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_cluster_net_info(db_cluster_id=self.db_cluster_id, **_params)

    def describe_db_cluster_performance(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_cluster_performance(db_cluster_id=self.db_cluster_id, **_params)

    def describe_operator_permission(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_operator_permission(db_cluster_id=self.db_cluster_id, **_params)

    def describe_slow_log_records(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_slow_log_records(db_cluster_id=self.db_cluster_id, **_params)

    def describe_slow_log_trend(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_slow_log_trend(db_cluster_id=self.db_cluster_id, **_params)

    def describe_slow_logs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_slow_logs(db_cluster_id=self.db_cluster_id, **_params)

    def grant_operator_permission(self, **params):
        _params = _transfer_params(params)
        return self._client.grant_operator_permission(db_cluster_id=self.db_cluster_id, **_params)

    def modify_access_white_list(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_cluster_access_white_list(db_cluster_id=self.db_cluster_id, **_params)

    def modify_auto_renew_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_auto_renew_attribute(db_cluster_id=self.db_cluster_id, **_params)

    def modify_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_backup_policy(db_cluster_id=self.db_cluster_id, **_params)

    def modify_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_cluster_description(db_cluster_id=self.db_cluster_id, **_params)

    def modify_log_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_log_backup_policy(db_cluster_id=self.db_cluster_id, **_params)

    def modify_maintain_time(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_cluster_maintain_time(db_cluster_id=self.db_cluster_id, **_params)

    def release_cluster_public_connection(self, **params):
        _params = _transfer_params(params)
        return self._client.release_cluster_public_connection(db_cluster_id=self.db_cluster_id, **_params)

    def revoke_operator_permission(self, **params):
        _params = _transfer_params(params)
        return self._client.revoke_operator_permission(db_cluster_id=self.db_cluster_id, **_params)

    def create_account(self, **params):
        _params = _transfer_params(params)
        self._client.create_account(db_cluster_id=self.db_cluster_id,**_params)
        account_name = _params.get("account_name")
        return _ADBAccountResource(account_name,self.db_cluster_id, _client=self._client)

class _ADBAccountResource(ServiceResource):

    def __init__(self, account_name,db_cluster_id, _client=None):
        ServiceResource.__init__(self, "adb.account", _client=_client)
        self.account_name = account_name
        self.db_cluster_id = db_cluster_id
        self.account_description = None
        self.account_status = None
        self.account_type = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_account(account_name=self.account_name,db_cluster_id=self.db_cluster_id, **_params)

    def modify_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_account_description(account_name=self.account_name,db_cluster_id=self.db_cluster_id, **_params)

    def reset_account_password(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_account_password(account_name=self.account_name,db_cluster_id=self.db_cluster_id, **_params)

class _ADBRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "adb.region", _client=_client)
        self.region_id = region_id
        
        self.zones = None
