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


class _GPDBResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'gpdb', _client=_client)
        self.db_instances = _create_resource_collection(
            _GPDBDBInstanceResource, _client, _client.describe_db_instances,
            'Items.DBInstance', 'DBInstanceId', key_to_total_count="TotalRecordCount",key_to_page_size="PageRecordCount",key_to_page_number="PageNumber"
        )
        self.regions = _create_special_resource_collection(
            _GPDBRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId', 
        )
    def add_bu_db_instance_relation(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_bu_db_instance_relation(**_params)
        db_instance_name = _new_get_key_in_response(response, 'DBInstanceName')
        return _GPDBBuDBInstanceRelationResource(db_instance_name, _client=self._client)

    def create_db_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_db_instance(**_params)
        db_instance_id = _new_get_key_in_response(response, 'DBInstanceId')
        return _GPDBDBInstanceResource(db_instance_id, _client=self._client)

class _GPDBBuDBInstanceRelationResource(ServiceResource):

    def __init__(self, db_instance_name, _client=None):
        ServiceResource.__init__(self, "gpdb.bu_db_instance_relation", _client=_client)
        self.db_instance_name = db_instance_name
        

class _GPDBDBInstanceResource(ServiceResource):

    def __init__(self, db_instance_id, _client=None):
        ServiceResource.__init__(self, "gpdb.db_instance", _client=_client)
        self.db_instance_id = db_instance_id
        
        self.connection_mode = None
        self.create_time = None
        self.db_instance_description = None
        self.db_instance_net_type = None
        self.db_instance_status = None
        self.engine = None
        self.engine_version = None
        self.expire_time = None
        self.instance_network_type = None
        self.lock_mode = None
        self.lock_reason = None
        self.pay_type = None
        self.region_id = None
        self.tags = None
        self.vswitch_id = None
        self.vpc_id = None
        self.zone_id = None

        self.accounts = _create_sub_resource_without_page_collection(
            _GPDBAccountResource, _client, _client.describe_accounts,
            'Accounts.DBInstanceAccount', 'AccountName', parent_identifier="DBInstanceId",parent_identifier_value=self.db_instance_id
        )
    def allocate_instance_public_connection(self, **params):
        _params = _transfer_params(params)
        return self._client.allocate_instance_public_connection(db_instance_id=self.db_instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_db_instance(db_instance_id=self.db_instance_id, **_params)

    def delete_database(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_database(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_instance_attribute(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_ip_array_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_instance_ip_array_list(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_net_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_instance_net_info(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_performance(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_db_instance_performance(db_instance_id=self.db_instance_id, **_params)

    def describe_resource_usage(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_resource_usage(db_instance_id=self.db_instance_id, **_params)

    def describe_sql_collector_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_sql_collector_policy(db_instance_id=self.db_instance_id, **_params)

    def describe_sql_log_files(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_sql_log_files(db_instance_id=self.db_instance_id, **_params)

    def describe_sql_log_records(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_sql_log_records(db_instance_id=self.db_instance_id, **_params)

    def describe_slow_log_records(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_slow_log_records(db_instance_id=self.db_instance_id, **_params)

    def modify_connection_mode(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_connection_mode(db_instance_id=self.db_instance_id, **_params)

    def modify_connection_string(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_connection_string(db_instance_id=self.db_instance_id, **_params)

    def modify_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_description(db_instance_id=self.db_instance_id, **_params)

    def modify_maintain_time(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_maintain_time(db_instance_id=self.db_instance_id, **_params)

    def modify_network_type(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_db_instance_network_type(db_instance_id=self.db_instance_id, **_params)

    def modify_sql_collector_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_sql_collector_policy(db_instance_id=self.db_instance_id, **_params)

    def modify_security_ips(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_security_ips(db_instance_id=self.db_instance_id, **_params)

    def release_instance_public_connection(self, **params):
        _params = _transfer_params(params)
        return self._client.release_instance_public_connection(db_instance_id=self.db_instance_id, **_params)

    def restart(self, **params):
        _params = _transfer_params(params)
        return self._client.restart_db_instance(db_instance_id=self.db_instance_id, **_params)

    def switch_db_instance_net_type(self, **params):
        _params = _transfer_params(params)
        return self._client.switch_db_instance_net_type(db_instance_id=self.db_instance_id, **_params)

    def upgrade(self, **params):
        _params = _transfer_params(params)
        return self._client.upgrade_db_instance(db_instance_id=self.db_instance_id, **_params)

    def upgrade_db_version(self, **params):
        _params = _transfer_params(params)
        return self._client.upgrade_db_version(db_instance_id=self.db_instance_id, **_params)

    def create_account(self, **params):
        _params = _transfer_params(params)
        self._client.create_account(db_instance_id=self.db_instance_id,**_params)
        account_name = _params.get("account_name")
        return _GPDBAccountResource(account_name,self.db_instance_id, _client=self._client)

class _GPDBAccountResource(ServiceResource):

    def __init__(self, account_name,db_instance_id, _client=None):
        ServiceResource.__init__(self, "gpdb.account", _client=_client)
        self.account_name = account_name
        self.db_instance_id = db_instance_id
        self.account_description = None
        self.account_status = None

    def modify_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_account_description(account_name=self.account_name,db_instance_id=self.db_instance_id, **_params)

    def reset_account_password(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_account_password(account_name=self.account_name,db_instance_id=self.db_instance_id, **_params)

class _GPDBRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "gpdb.region", _client=_client)
        self.region_id = region_id
        
        self.zones = None
