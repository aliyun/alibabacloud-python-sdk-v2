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


class _PETADATAResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'petadata', _client=_client)
        self.instances = _create_resource_collection(
            _PETADATAInstanceResource, _client, _client.describe_instances,
            'Instances.Instance', 'InstanceId', 
        )
        self.regions = _create_special_resource_collection(
            _PETADATARegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId', 
        )
        self.tasks = _create_special_resource_collection(
            _PETADATATaskResource, _client, _client.describe_tasks,
            'Tasks.Task', 'TaskId', 
        )
class _PETADATAInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "petadata.instance", _client=_client)
        self.instance_id = instance_id
        
        self.connection_string = None
        self.create_time = None
        self.databases = None
        self.instance_name = None
        self.instance_status = None
        self.network_type = None
        self.port = None
        self.private_ip_address = None
        self.region_id = None
        self.vswitch_id = None
        self.vpc_id = None
        self.zone_id = None

        self.accounts = _create_sub_resource_without_page_collection(
            _PETADATAAccountResource, _client, _client.describe_accounts,
            'AccountList.Account', 'AccountName', parent_identifier="InstanceId",parent_identifier_value=self.instance_id
        )
        self.databases = _create_sub_resource_without_page_collection(
            _PETADATADatabaseResource, _client, _client.describe_databases,
            'Databases.Database', 'DatabaseName', parent_identifier="InstanceId",parent_identifier_value=self.instance_id
        )
    def allocate_instance_public_connection(self, **params):
        _params = _transfer_params(params)
        return self._client.allocate_instance_public_connection(instance_id=self.instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_instance(instance_id=self.instance_id, **_params)

    def describe_instance_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_instance_info(instance_id=self.instance_id, **_params)

    def describe_instance_performance(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_instance_performance(instance_id=self.instance_id, **_params)

    def describe_instance_resource_usage(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_instance_resource_usage(instance_id=self.instance_id, **_params)

    def describe_security_ips(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_security_ips(instance_id=self.instance_id, **_params)

    def modify_name(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_name(instance_id=self.instance_id, **_params)

    def modify_security_ips(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_security_ips(instance_id=self.instance_id, **_params)

    def switch_instance_net_type(self, **params):
        _params = _transfer_params(params)
        return self._client.switch_instance_net_type(instance_id=self.instance_id, **_params)

    def create_account(self, **params):
        _params = _transfer_params(params)
        self._client.create_account(instance_id=self.instance_id,**_params)
        account_name = _params.get("account_name")
        return _PETADATAAccountResource(account_name,self.instance_id, _client=self._client)

    def create_database(self, **params):
        _params = _transfer_params(params)
        self._client.create_database(instance_id=self.instance_id,**_params)
        database_name = _params.get("database_name")
        return _PETADATADatabaseResource(database_name,self.instance_id, _client=self._client)

class _PETADATAAccountResource(ServiceResource):

    def __init__(self, account_name,instance_id, _client=None):
        ServiceResource.__init__(self, "petadata.account", _client=_client)
        self.account_name = account_name
        self.instance_id = instance_id
        self.account_description = None
        self.account_status = None
        self.account_type = None
        self.database_privileges = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_account(account_name=self.account_name,instance_id=self.instance_id, **_params)

    def modify_description(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_account_description(account_name=self.account_name,instance_id=self.instance_id, **_params)

    def modify_password(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_account_password(account_name=self.account_name,instance_id=self.instance_id, **_params)

    def reset_account_password(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_account_password(account_name=self.account_name,instance_id=self.instance_id, **_params)

    def grant_account_privilege(self, **params):
        _params = _transfer_params(params)
        return self._client.grant_account_privilege(account_name=self.account_name,instance_id=self.instance_id, **_params)

    def revoke_account_privilege(self, **params):
        _params = _transfer_params(params)
        return self._client.revoke_account_privilege(account_name=self.account_name,instance_id=self.instance_id, **_params)

class _PETADATADatabaseResource(ServiceResource):

    def __init__(self, database_name,instance_id, _client=None):
        ServiceResource.__init__(self, "petadata.database", _client=_client)
        self.database_name = database_name
        self.instance_id = instance_id
        self.charge_type = None
        self.create_time = None
        self.db_name = None
        self.db_status = None
        self.db_type = None
        self.end_time = None
        self.node_number = None
        self.node_spec = None
        self.source_instance_id = None

    def create_database_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.create_database_backup(database_name=self.database_name,instance_id=self.instance_id, **_params)

    def create_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.create_instance(database_name=self.database_name,instance_id=self.instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_database(database_name=self.database_name,instance_id=self.instance_id, **_params)

    def describe_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_backup_policy(database_name=self.database_name,instance_id=self.instance_id, **_params)

    def describe_database_backup(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_database_backup(database_name=self.database_name,instance_id=self.instance_id, **_params)

    def describe_database_partitions(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_database_partitions(database_name=self.database_name,instance_id=self.instance_id, **_params)

    def describe_database_performance(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_database_performance(database_name=self.database_name,instance_id=self.instance_id, **_params)

    def describe_database_resource_usage(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_database_resource_usage(database_name=self.database_name,instance_id=self.instance_id, **_params)

    def modify_backup_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_backup_policy(database_name=self.database_name,instance_id=self.instance_id, **_params)

class _PETADATARegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "petadata.region", _client=_client)
        self.region_id = region_id
        
        self.zone_id = None
        self.zones = None

class _PETADATATaskResource(ServiceResource):

    def __init__(self, task_id, _client=None):
        ServiceResource.__init__(self, "petadata.task", _client=_client)
        self.task_id = task_id
        
        self.begin_time = None
        self.db_name = None
        self.expected_finish_time = None
        self.finish_time = None
        self.progress = None
        self.progress_info = None
        self.status = None
        self.task_action = None

    def describe_task_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_task_status(task_id=self.task_id, **_params)
