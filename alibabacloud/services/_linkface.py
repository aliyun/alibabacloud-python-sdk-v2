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


class _LINKFACEResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'linkface', _client=_client)
    def create_group(self, **params):
        _params = _transfer_params(params)
        self._client.create_group(**_params)
        group_name = _params.get("group_name")
        return _LINKFACEGroupResource(group_name, _client=self._client)

class _LINKFACEGroupResource(ServiceResource):

    def __init__(self, group_name, _client=None):
        ServiceResource.__init__(self, "linkface.group", _client=_client)
        self.group_name = group_name
        

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_group(group_name=self.group_name, **_params)

    def delete_device(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_device_group(group_name=self.group_name, **_params)

    def query_group_users(self, **params):
        _params = _transfer_params(params)
        return self._client.query_group_users(group_name=self.group_name, **_params)

    def register_face(self, **params):
        _params = _transfer_params(params)
        return self._client.register_face(group_name=self.group_name, **_params)

    def search_face(self, **params):
        _params = _transfer_params(params)
        return self._client.search_face(group_name=self.group_name, **_params)

    def sync_face_pictures(self, **params):
        _params = _transfer_params(params)
        return self._client.sync_face_pictures(group_name=self.group_name, **_params)

    def unlink_face(self, **params):
        _params = _transfer_params(params)
        return self._client.unlink_face(group_name=self.group_name, **_params)

    def link_face(self, **params):
        _params = _transfer_params(params)
        return self._client.link_face(group_name=self.group_name, **_params)
