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

from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_special_resource_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _ECIResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'eci', _client=_client)
        self.container_groups = _create_special_resource_collection(
            _ECIContainerGroupResource, _client, _client.describe_container_groups,
            'ContainerGroups.ContainerGroup', 'ContainerGroupId',
        )

    def create_container_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_container_group(**_params)
        container_group_id = _new_get_key_in_response(response, 'ContainerGroupId')
        return _ECIContainerGroupResource(container_group_id, _client=self._client)


class _ECIContainerGroupResource(ServiceResource):

    def __init__(self, container_group_id, _client=None):
        ServiceResource.__init__(self, "eci.container_group", _client=_client)
        self.container_group_id = container_group_id

        self.container_group_name = None
        self.containers = None
        self.cpu = None
        self.creation_time = None
        self.dns_config = None
        self.eci_security_context = None
        self.eni_instance_id = None
        self.events = None
        self.expired_time = None
        self.failed_time = None
        self.host_aliases = None
        self.init_containers = None
        self.instance_type = None
        self.internet_ip = None
        self.intranet_ip = None
        self.memory = None
        self.ram_role_name = None
        self.region_id = None
        self.restart_policy = None
        self.security_group_id = None
        self.status = None
        self.succeeded_time = None
        self.tags = None
        self.vswitch_id = None
        self.volumes = None
        self.zone_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_container_group(container_group_id=self.container_group_id,
                                                   **_params)

    def describe_container_group_metric(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_container_group_metric(
            container_group_id=self.container_group_id, **_params)

    def describe_container_log(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_container_log(container_group_id=self.container_group_id,
                                                   **_params)

    def exec_container_command(self, **params):
        _params = _transfer_params(params)
        return self._client.exec_container_command(container_group_id=self.container_group_id,
                                                   **_params)

    def restart(self, **params):
        _params = _transfer_params(params)
        return self._client.restart_container_group(container_group_id=self.container_group_id,
                                                    **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_container_group(container_group_id=self.container_group_id,
                                                   **_params)
