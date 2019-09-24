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


class _RAMResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ram', _client=_client)
        self.groups = _create_special_resource_collection(
            _RAMGroupResource, _client, _client.list_groups,
            'Groups.Group', 'GroupName',
        )
        self.policies = _create_special_resource_collection(
            _RAMPolicyResource, _client, _client.list_policies,
            'Policies.Policy', 'PolicyName',
        )
        self.roles = _create_special_resource_collection(
            _RAMRoleResource, _client, _client.list_roles,
            'Roles.Role', 'RoleName',
        )
        self.users = _create_special_resource_collection(
            _RAMUserResource, _client, _client.list_users,
            'Users.User', 'UserName',
        )

    def create_group(self, **params):
        _params = _transfer_params(params)
        self._client.create_group(**_params)
        group_name = _params.get("group_name")
        return _RAMGroupResource(group_name, _client=self._client)

    def create_policy(self, **params):
        _params = _transfer_params(params)
        self._client.create_policy(**_params)
        policy_name = _params.get("policy_name")
        return _RAMPolicyResource(policy_name, _client=self._client)

    def create_role(self, **params):
        _params = _transfer_params(params)
        self._client.create_role(**_params)
        role_name = _params.get("role_name")
        return _RAMRoleResource(role_name, _client=self._client)

    def create_user(self, **params):
        _params = _transfer_params(params)
        self._client.create_user(**_params)
        user_name = _params.get("user_name")
        return _RAMUserResource(user_name, _client=self._client)

    def create_virtual_mfa_device(self, **params):
        _params = _transfer_params(params)
        self._client.create_virtual_mfa_device(**_params)
        virtual_mfa_device_name = _params.get("virtual_mfa_device_name")
        return _RAMVirtualMFADeviceResource(virtual_mfa_device_name, _client=self._client)


class _RAMGroupResource(ServiceResource):

    def __init__(self, group_name, _client=None):
        ServiceResource.__init__(self, "ram.group", _client=_client)
        self.group_name = group_name

        self.comments = None
        self.create_date = None
        self.update_date = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_group(group_name=self.group_name, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        self._client.get_group(group_name=self.group_name, **_params)

    def list_policies_for(self, **params):
        _params = _transfer_params(params)
        self._client.list_policies_for_group(group_name=self.group_name, **_params)

    def list_users_for(self, **params):
        _params = _transfer_params(params)
        self._client.list_users_for_group(group_name=self.group_name, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        self._client.update_group(group_name=self.group_name, **_params)

    def refresh(self):
        result = self._client.get_group(group_name=self.group_name)
        items = _new_get_key_in_response(result, 'Group')
        if not items:
            raise ClientException(msg="Failed to find group data from GetGroup response. "
                                  "GroupName = {0}".format(self.group_name))
        self._assign_attributes(items[0])


class _RAMPolicyResource(ServiceResource):

    def __init__(self, policy_name, _client=None):
        ServiceResource.__init__(self, "ram.policy", _client=_client)
        self.policy_name = policy_name

        self.attachment_count = None
        self.create_date = None
        self.default_version = None
        self.description = None
        self.policy_type = None
        self.update_date = None

    def create_policy_version(self, **params):
        _params = _transfer_params(params)
        self._client.create_policy_version(policy_name=self.policy_name, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_policy(policy_name=self.policy_name, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        self._client.get_policy(policy_name=self.policy_name, **_params)

    def list_entities_for(self, **params):
        _params = _transfer_params(params)
        self._client.list_entities_for_policy(policy_name=self.policy_name, **_params)

    def list_policy_versions(self, **params):
        _params = _transfer_params(params)
        self._client.list_policy_versions(policy_name=self.policy_name, **_params)

    def attach_policy_to_group(self, **params):
        _params = _transfer_params(params)
        self._client.attach_policy_to_group(policy_name=self.policy_name, **_params)

    def attach_policy_to_role(self, **params):
        _params = _transfer_params(params)
        self._client.attach_policy_to_role(policy_name=self.policy_name, **_params)

    def attach_policy_to_user(self, **params):
        _params = _transfer_params(params)
        self._client.attach_policy_to_user(policy_name=self.policy_name, **_params)

    def delete_policy_version(self, **params):
        _params = _transfer_params(params)
        self._client.delete_policy_version(policy_name=self.policy_name, **_params)

    def detach_policy_from_group(self, **params):
        _params = _transfer_params(params)
        self._client.detach_policy_from_group(policy_name=self.policy_name, **_params)

    def detach_policy_from_role(self, **params):
        _params = _transfer_params(params)
        self._client.detach_policy_from_role(policy_name=self.policy_name, **_params)

    def detach_policy_from_user(self, **params):
        _params = _transfer_params(params)
        self._client.detach_policy_from_user(policy_name=self.policy_name, **_params)

    def get_policy_version(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_policy_version(policy_name=self.policy_name, **_params)
        return response

    def set_default_policy_version(self, **params):
        _params = _transfer_params(params)
        self._client.set_default_policy_version(policy_name=self.policy_name, **_params)

    def refresh(self):
        result = self._client.get_policy(policy_name=self.policy_name)
        items = _new_get_key_in_response(result, 'Policy')
        if not items:
            raise ClientException(msg="Failed to find policy data from GetPolicy response. "
                                  "PolicyName = {0}".format(self.policy_name))
        self._assign_attributes(items[0])


class _RAMRoleResource(ServiceResource):

    def __init__(self, role_name, _client=None):
        ServiceResource.__init__(self, "ram.role", _client=_client)
        self.role_name = role_name

        self.arn = None
        self.create_date = None
        self.description = None
        self.role_id = None
        self.update_date = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_role(role_name=self.role_name, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        self._client.get_role(role_name=self.role_name, **_params)

    def list_policies_for(self, **params):
        _params = _transfer_params(params)
        self._client.list_policies_for_role(role_name=self.role_name, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        self._client.update_role(role_name=self.role_name, **_params)

    def refresh(self):
        result = self._client.get_role(role_name=self.role_name)
        items = _new_get_key_in_response(result, 'Role')
        if not items:
            raise ClientException(msg="Failed to find role data from GetRole response. "
                                  "RoleName = {0}".format(self.role_name))
        self._assign_attributes(items[0])


class _RAMUserResource(ServiceResource):

    def __init__(self, user_name, _client=None):
        ServiceResource.__init__(self, "ram.user", _client=_client)
        self.user_name = user_name

        self.comments = None
        self.create_date = None
        self.display_name = None
        self.email = None
        self.mobile_phone = None
        self.update_date = None
        self.user_id = None

    def bind_mfa_device(self, **params):
        _params = _transfer_params(params)
        self._client.bind_mfa_device(user_name=self.user_name, **_params)

    def create_access_key(self, **params):
        _params = _transfer_params(params)
        self._client.create_access_key(user_name=self.user_name, **_params)

    def create_login_profile(self, **params):
        _params = _transfer_params(params)
        self._client.create_login_profile(user_name=self.user_name, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_user(user_name=self.user_name, **_params)

    def delete_access_key(self, **params):
        _params = _transfer_params(params)
        self._client.delete_access_key(user_name=self.user_name, **_params)

    def delete_login_profile(self, **params):
        _params = _transfer_params(params)
        self._client.delete_login_profile(user_name=self.user_name, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        self._client.get_user(user_name=self.user_name, **_params)

    def get_access_key_last_used(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_access_key_last_used(user_name=self.user_name, **_params)
        return response

    def get_login_profile(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_login_profile(user_name=self.user_name, **_params)
        return response

    def get_user_mfa_info(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_user_mfa_info(user_name=self.user_name, **_params)
        return response

    def list_access_keys(self, **params):
        _params = _transfer_params(params)
        self._client.list_access_keys(user_name=self.user_name, **_params)

    def list_groups_for(self, **params):
        _params = _transfer_params(params)
        self._client.list_groups_for_user(user_name=self.user_name, **_params)

    def list_policies_for(self, **params):
        _params = _transfer_params(params)
        self._client.list_policies_for_user(user_name=self.user_name, **_params)

    def unbind_mfa_device(self, **params):
        _params = _transfer_params(params)
        self._client.unbind_mfa_device(user_name=self.user_name, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        self._client.update_user(user_name=self.user_name, **_params)

    def update_access_key(self, **params):
        _params = _transfer_params(params)
        self._client.update_access_key(user_name=self.user_name, **_params)

    def update_login_profile(self, **params):
        _params = _transfer_params(params)
        self._client.update_login_profile(user_name=self.user_name, **_params)

    def add_user_to_group(self, **params):
        _params = _transfer_params(params)
        self._client.add_user_to_group(user_name=self.user_name, **_params)

    def remove_user_from_group(self, **params):
        _params = _transfer_params(params)
        self._client.remove_user_from_group(user_name=self.user_name, **_params)

    def refresh(self):
        result = self._client.get_user(user_name=self.user_name)
        items = _new_get_key_in_response(result, 'User')
        if not items:
            raise ClientException(msg="Failed to find user data from GetUser response. "
                                  "UserName = {0}".format(self.user_name))
        self._assign_attributes(items)


class _RAMVirtualMFADeviceResource(ServiceResource):

    def __init__(self, virtual_mfa_device_name, _client=None):
        ServiceResource.__init__(self, "ram.virtual_mfa_device", _client=_client)
        self.virtual_mfa_device_name = virtual_mfa_device_name

