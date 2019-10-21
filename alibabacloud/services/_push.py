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


class _PUSHResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'push', _client=_client)
        self.tags = _create_special_resource_collection(
            _PUSHTagResource, _client, _client.query_tags,
            'TagInfos.TagInfo', 'TagName', 
        )
        self.tags = _create_special_resource_collection(
            _PUSHTagResource, _client, _client.query_tags,
            'TagInfos.TagInfo', 'TagName', 
        )
    def check_devices(self, **params):
        _params = _transfer_params(params)
        response = self._client.check_devices(**_params)
        device_ids = _new_get_key_in_response(response, 'None')
        devices = []
        for device_id in device_ids:
            device = _PUSHDeviceResource(device_id, _client=self._client)
            devices.append(device)
        return devices

class _PUSHDeviceResource(ServiceResource):

    def __init__(self, device_id, _client=None):
        ServiceResource.__init__(self, "push.device", _client=_client)
        self.device_id = device_id
        

        self.aliases = _create_sub_resource_without_page_collection(
            _PUSHAliasResource, _client, _client.query_aliases,
            'AliasInfos.AliasInfo', 'AliasName', parent_identifier="DeviceId",parent_identifier_value=self.device_id
        )
    def bind_phone(self, **params):
        _params = _transfer_params(params)
        return self._client.bind_phone(device_id=self.device_id, **_params)

    def check(self, **params):
        _params = _transfer_params(params)
        return self._client.check_device(device_id=self.device_id, **_params)

    def query_device_info(self, **params):
        _params = _transfer_params(params)
        return self._client.query_device_info(device_id=self.device_id, **_params)

    def unbind_alias(self, **params):
        _params = _transfer_params(params)
        return self._client.unbind_alias(device_id=self.device_id, **_params)

    def unbind_phone(self, **params):
        _params = _transfer_params(params)
        return self._client.unbind_phone(device_id=self.device_id, **_params)

class _PUSHAliasResource(ServiceResource):

    def __init__(self, alias_name,device_id, _client=None):
        ServiceResource.__init__(self, "push.alias", _client=_client)
        self.alias_name = alias_name
        self.device_id = device_id

    def bind(self, **params):
        _params = _transfer_params(params)
        return self._client.bind_alias(alias_name=self.alias_name,device_id=self.device_id, **_params)

class _PUSHTagResource(ServiceResource):

    def __init__(self, tag_name, _client=None):
        ServiceResource.__init__(self, "push.tag", _client=_client)
        self.tag_name = tag_name
        

    def bind(self, **params):
        _params = _transfer_params(params)
        return self._client.bind_tag(tag_name=self.tag_name, **_params)

    def remove(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_tag(tag_name=self.tag_name, **_params)

    def unbind(self, **params):
        _params = _transfer_params(params)
        return self._client.unbind_tag(tag_name=self.tag_name, **_params)
