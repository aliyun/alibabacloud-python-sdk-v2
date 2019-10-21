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


class _KMSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'kms', _client=_client)
        self.aliases = _create_resource_collection(
            _KMSAliasResource, _client, _client.list_aliases,
            'Aliases.Alias', 'AliasName', 
        )
    def create_alias(self, **params):
        _params = _transfer_params(params)
        self._client.create_alias(**_params)
        alias_name = _params.get("alias_name")
        return _KMSAliasResource(alias_name, _client=self._client)

    def create_key(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_key(**_params)
        key_id = _new_get_key_in_response(response, 'KeyId')
        return _KMSKeyResource(key_id, _client=self._client)

class _KMSAliasResource(ServiceResource):

    def __init__(self, alias_name, _client=None):
        ServiceResource.__init__(self, "kms.alias", _client=_client)
        self.alias_name = alias_name
        
        self.alias_arn = None
        self.key_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_alias(alias_name=self.alias_name, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_alias(alias_name=self.alias_name, **_params)

class _KMSKeyResource(ServiceResource):

    def __init__(self, key_id, _client=None):
        ServiceResource.__init__(self, "kms.key", _client=_client)
        self.key_id = key_id
        

    def cancel_key_deletion(self, **params):
        _params = _transfer_params(params)
        return self._client.cancel_key_deletion(key_id=self.key_id, **_params)

    def delete_key_material(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_key_material(key_id=self.key_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_key(key_id=self.key_id, **_params)

    def disable(self, **params):
        _params = _transfer_params(params)
        return self._client.disable_key(key_id=self.key_id, **_params)

    def enable(self, **params):
        _params = _transfer_params(params)
        return self._client.enable_key(key_id=self.key_id, **_params)

    def encrypt(self, **params):
        _params = _transfer_params(params)
        return self._client.encrypt(key_id=self.key_id, **_params)

    def generate_data(self, **params):
        _params = _transfer_params(params)
        return self._client.generate_data_key(key_id=self.key_id, **_params)

    def get_parameters_for_import(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_parameters_for_import(key_id=self.key_id, **_params)
        return response

    def import_key_material(self, **params):
        _params = _transfer_params(params)
        return self._client.import_key_material(key_id=self.key_id, **_params)

    def list_aliases_by_key_id(self, **params):
        _params = _transfer_params(params)
        return self._client.list_aliases_by_key_id(key_id=self.key_id, **_params)

    def list_resource_tags(self, **params):
        _params = _transfer_params(params)
        return self._client.list_resource_tags(key_id=self.key_id, **_params)

    def schedule_key_deletion(self, **params):
        _params = _transfer_params(params)
        return self._client.schedule_key_deletion(key_id=self.key_id, **_params)

    def tag_resource(self, **params):
        _params = _transfer_params(params)
        return self._client.tag_resource(key_id=self.key_id, **_params)

    def untag_resource(self, **params):
        _params = _transfer_params(params)
        return self._client.untag_resource(key_id=self.key_id, **_params)
