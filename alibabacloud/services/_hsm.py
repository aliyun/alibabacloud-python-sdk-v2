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


class _HSMResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'hsm', _client=_client)
        self.instances = _create_special_resource_collection(
            _HSMInstanceResource, _client, _client.describe_instances,
            'Instances.Instance', 'InstanceId', 
        )
        self.regions = _create_special_resource_collection(
            _HSMRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId', 
        )
    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_ids = _new_get_key_in_response(response, 'InstanceIds.InstanceId')
        instances = []
        for instance_id in instance_ids:
            instance = _HSMInstanceResource(instance_id, _client=self._client)
            instances.append(instance)
        return instances

class _HSMInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "hsm.instance", _client=_client)
        self.instance_id = instance_id
        
        self.create_time = None
        self.expired_time = None
        self.hsm_device_type = None
        self.hsm_oem = None
        self.hsm_status = None
        self.ip = None
        self.region_id = None
        self.remark = None
        self.vpc_id = None
        self.vswitch_id = None
        self.white_list = None
        self.zone_id = None

    def config_network(self, **params):
        _params = _transfer_params(params)
        return self._client.config_network(instance_id=self.instance_id, **_params)

    def config_white_list(self, **params):
        _params = _transfer_params(params)
        return self._client.config_white_list(instance_id=self.instance_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance(instance_id=self.instance_id, **_params)

    def release(self, **params):
        _params = _transfer_params(params)
        return self._client.release_instance(instance_id=self.instance_id, **_params)

    def renew(self, **params):
        _params = _transfer_params(params)
        return self._client.renew_instance(instance_id=self.instance_id, **_params)

class _HSMRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "hsm.region", _client=_client)
        self.region_id = region_id
        
        self.zones = None
