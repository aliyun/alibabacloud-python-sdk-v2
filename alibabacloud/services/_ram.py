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
from alibabacloud.resources.collection import _create_resource_collection
from alibabacloud.resources.collection import _create_default_resource_collection
from alibabacloud.utils.utils import _assert_is_not_none, _new_get_key_in_response, _transfer_params


class _RAMResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ram', _client=_client)
        self.access_keys = _create_resource_collection(
            _RAMAccessKeyResource, _client, _client.list_access_keys,
            'AccessKeys.AccessKey', 'AccessKeyId',
        )
        self.public_keys = _create_resource_collection(
            _RAMPublicKeyResource, _client, _client.list_public_keys,
            'PublicKeys.PublicKey', 'PublicKeyId',
        )
        self.roles = _create_resource_collection(
            _RAMRoleResource, _client, _client.list_roles,
            'Roles.Role', 'RoleId',
        )
        self.users = _create_resource_collection(
            _RAMUserResource, _client, _client.list_users,
            'Users.User', 'UserId',
        )
class _RAMAccessKeyResource(ServiceResource):

    def __init__(self, access_key_id, _client=None):
        ServiceResource.__init__(self, "ram.access_key", _client=_client)
        self.access_key_id = access_key_id

        self.create_date = None
        self.status = None

    def refresh(self):
        result = self._client.list_access_keys(access_key_id=json.dumps([self.access_key_id],))
        items = _new_get_key_in_response(result, 'AccessKeys.AccessKey')
        if not items:
            raise ClientException(msg=
                                  "Failed to find access_key data from ListAccessKeys response. "
                                  "AccessKeyId = {0}".format(self.access_key_id))
        self._assign_attributes(items[0])

class _RAMPublicKeyResource(ServiceResource):

    def __init__(self, public_key_id, _client=None):
        ServiceResource.__init__(self, "ram.public_key", _client=_client)
        self.public_key_id = public_key_id

        self.create_date = None
        self.status = None

class _RAMRoleResource(ServiceResource):

    def __init__(self, role_id, _client=None):
        ServiceResource.__init__(self, "ram.role", _client=_client)
        self.role_id = role_id

        self.arn = None
        self.create_date = None
        self.description = None
        self.role_name = None
        self.update_date = None

class _RAMUserResource(ServiceResource):

    def __init__(self, user_id, _client=None):
        ServiceResource.__init__(self, "ram.user", _client=_client)
        self.user_id = user_id

        self.comments = None
        self.create_date = None
        self.display_name = None
        self.email = None
        self.mobile_phone = None
        self.update_date = None
        self.user_name = None
