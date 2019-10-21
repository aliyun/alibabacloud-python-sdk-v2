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


class _MOPENResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'mopen', _client=_client)
    def mo_pen_create_device(self, **params):
        _params = _transfer_params(params)
        response = self._client.mo_pen_create_device(**_params)
        device_name = _new_get_key_in_response(response, 'DeviceName')
        return _MOPENDeviceResource(device_name, _client=self._client)

    def mo_pen_find_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.mo_pen_find_group(**_params)
        group_id = _new_get_key_in_response(response, 'GroupId')
        return _MOPENGroupResource(group_id, _client=self._client)

    def mopen_create_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.mopen_create_group(**_params)
        group_id = _new_get_key_in_response(response, 'GroupId')
        return _MOPENGroupResource(group_id, _client=self._client)

class _MOPENDeviceResource(ServiceResource):

    def __init__(self, device_name, _client=None):
        ServiceResource.__init__(self, "mopen.device", _client=_client)
        self.device_name = device_name
        

    def add_group_member(self, **params):
        _params = _transfer_params(params)
        return self._client.mo_pen_add_group_member(device_name=self.device_name, **_params)

    def bind_isv(self, **params):
        _params = _transfer_params(params)
        return self._client.mo_pen_bind_isv(device_name=self.device_name, **_params)

    def query_canvas(self, **params):
        _params = _transfer_params(params)
        return self._client.mo_pen_query_canvas(device_name=self.device_name, **_params)

    def send_mqtt_message(self, **params):
        _params = _transfer_params(params)
        return self._client.mo_pen_send_mqtt_message(device_name=self.device_name, **_params)

class _MOPENGroupResource(ServiceResource):

    def __init__(self, group_id, _client=None):
        ServiceResource.__init__(self, "mopen.group", _client=_client)
        self.group_id = group_id
        

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.mo_pen_delete_group(group_id=self.group_id, **_params)

    def delete_group_member(self, **params):
        _params = _transfer_params(params)
        return self._client.mo_pen_delete_group_member(group_id=self.group_id, **_params)
