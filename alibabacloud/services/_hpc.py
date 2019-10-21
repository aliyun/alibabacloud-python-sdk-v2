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


class _HPCResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'hpc', _client=_client)
        self.instances = _create_special_resource_collection(
            _HPCInstanceResource, _client, _client.describe_instances,
            'Instances.Instance', 'InstanceId', 
        )
    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _HPCInstanceResource(instance_id, _client=self._client)

    def delete_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _HPCInstanceResource(instance_id, _client=self._client)

class _HPCInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "hpc.instance", _client=_client)
        self.instance_id = instance_id
        
        self.inner_ip_address = None
        self.instance_type = None
        self.jump_server_public_ip_address = None
        self.jumpserver_inner_ip_address = None
        self.jumpserver_status = None
        self.package_id = None
        self.status = None

    def modify_jumpserver_password(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_jumpserver_password(instance_id=self.instance_id, **_params)

    def reboot(self, **params):
        _params = _transfer_params(params)
        return self._client.reboot_instance(instance_id=self.instance_id, **_params)

    def reboot_jumpserver(self, **params):
        _params = _transfer_params(params)
        return self._client.reboot_jumpserver(instance_id=self.instance_id, **_params)

    def start_jumpserver(self, **params):
        _params = _transfer_params(params)
        return self._client.start_jumpserver(instance_id=self.instance_id, **_params)

    def stop_jumpserver(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_jumpserver(instance_id=self.instance_id, **_params)
