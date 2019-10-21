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


class _OCSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ocs', _client=_client)
        self.instances = _create_resource_collection(
            _OCSInstanceResource, _client, _client.describe_instances,
            'Instances.OcsInstance', 'InstanceId', 
        )
        self.regions = _create_special_resource_collection(
            _OCSRegionResource, _client, _client.describe_regions,
            'RegionIds.OcsRegion', 'RegionId', 
        )
        self.zones = _create_special_resource_collection(
            _OCSZoneResource, _client, _client.describe_zones,
            'Zones.OcsZone', 'ZoneId', 
        )
    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _OCSInstanceResource(instance_id, _client=self._client)

class _OCSInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "ocs.instance", _client=_client)
        self.instance_id = instance_id
        
        self.bandwidth = None
        self.capacity = None
        self.connection_domain = None
        self.connections = None
        self.creation_time = None
        self.hotkey_enabled = None
        self.instance_name = None
        self.instance_status = None
        self.network_type = None
        self.port = None
        self.private_ip_address = None
        self.qps = None
        self.region_id = None
        self.user_name = None
        self.vswitch_id = None
        self.vpc_id = None
        self.zone_id = None

    def activate(self, **params):
        _params = _transfer_params(params)
        return self._client.activate_instance(instance_id=self.instance_id, **_params)

    def add_authentic_ip(self, **params):
        _params = _transfer_params(params)
        return self._client.add_authentic_ip(instance_id=self.instance_id, **_params)

    def data_operate(self, **params):
        _params = _transfer_params(params)
        return self._client.data_operate(instance_id=self.instance_id, **_params)

    def deactivate(self, **params):
        _params = _transfer_params(params)
        return self._client.deactivate_instance(instance_id=self.instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_instance(instance_id=self.instance_id, **_params)

    def describe_authentic_ip(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_authentic_ip(instance_id=self.instance_id, **_params)

    def describe_history_monitor_values(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_history_monitor_values(instance_id=self.instance_id, **_params)

    def describe_security_ips(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_security_ips(instance_id=self.instance_id, **_params)

    def flush(self, **params):
        _params = _transfer_params(params)
        return self._client.flush_instance(instance_id=self.instance_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_attribute(instance_id=self.instance_id, **_params)

    def modify_capacity(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance_capacity(instance_id=self.instance_id, **_params)

    def modify_hot_key_switch_mode(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_hot_key_switch_mode(instance_id=self.instance_id, **_params)

    def modify_network_type(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_network_type(instance_id=self.instance_id, **_params)

    def modify_security_ips(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_security_ips(instance_id=self.instance_id, **_params)

    def remove_authentic_ip(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_authentic_ip(instance_id=self.instance_id, **_params)

    def replace_authentic_ip(self, **params):
        _params = _transfer_params(params)
        return self._client.replace_authentic_ip(instance_id=self.instance_id, **_params)

    def verify_password(self, **params):
        _params = _transfer_params(params)
        return self._client.verify_password(instance_id=self.instance_id, **_params)

class _OCSRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "ocs.region", _client=_client)
        self.region_id = region_id
        
        self.local_name = None
        self.zone_ids = None

class _OCSZoneResource(ServiceResource):

    def __init__(self, zone_id, _client=None):
        ServiceResource.__init__(self, "ocs.zone", _client=_client)
        self.zone_id = zone_id
        
        self.description = None
        self.name = None
