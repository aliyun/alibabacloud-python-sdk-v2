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


class _OTSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ots', _client=_client)
        self.instances = _create_special_resource_collection(
            _OTSInstanceResource, _client, _client.list_instance,
            'InstanceInfos.InstanceInfo', 'InstanceName', 
        )
    def get_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_instance(**_params)
        instance_name = _new_get_key_in_response(response, 'InstanceName')
        return _OTSInstanceResource(instance_name, _client=self._client)

class _OTSInstanceResource(ServiceResource):

    def __init__(self, instance_name, _client=None):
        ServiceResource.__init__(self, "ots.instance", _client=_client)
        self.instance_name = instance_name
        
        self.timestamp = None

    def bind_instance2_vpc(self, **params):
        _params = _transfer_params(params)
        return self._client.bind_instance2_vpc(instance_name=self.instance_name, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_instance(instance_name=self.instance_name, **_params)

    def delete_tags(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_tags(instance_name=self.instance_name, **_params)

    def insert(self, **params):
        _params = _transfer_params(params)
        return self._client.insert_instance(instance_name=self.instance_name, **_params)

    def insert_tags(self, **params):
        _params = _transfer_params(params)
        return self._client.insert_tags(instance_name=self.instance_name, **_params)

    def list_vpc_info_by(self, **params):
        _params = _transfer_params(params)
        return self._client.list_vpc_info_by_instance(instance_name=self.instance_name, **_params)

    def unbind_instance2_vpc(self, **params):
        _params = _transfer_params(params)
        return self._client.unbind_instance2_vpc(instance_name=self.instance_name, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_instance(instance_name=self.instance_name, **_params)
