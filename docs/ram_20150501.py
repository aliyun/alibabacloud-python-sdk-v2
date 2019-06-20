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

"""
只是一个测试
"""


class AlibabaCloudClient:
    """
    Add a stream handler for the given name and level to the logging module.
    By default, this logs all boto3 messages to ``stdout``.

        >>> import boto3
        >>> boto3.set_stream_logger('boto3.resources', logging.INFO)

    For debugging purposes a good choice is to set the stream logger to ``''``
    which is equivalent to saying "log everything".

    .. WARNING::
       Be aware that when logging anything from ``'botocore'`` the full wire
       trace will appear in your logs. If your payloads contain sensitive data
       this should not be used in production.

    :type name: string
    :param name: Log name
    :type level: int
    :param level: Logging level, e.g. ``logging.INFO``
    :type format_string: str
    :param format_string: Log message format
    """
    def __init__(self, client_config, credentials_provider):
        pass

    def _handle_request(self, request): pass


class APIRequest:
    def __init__(self, name, method, protocol, style, position):
        pass


class RamClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None):
        """
        初始化
        :client_config: config object
        :credentials_provider: a provider
        """
        AlibabaCloudClient.__init__(self, client_config, credentials_provider)
        self.product_code = 'Ram'
        self.api_version = '2015-05-01'
        self.location_service_code = 'ram'
        self.location_endpoint_type = 'openAPI'

    def get_access_key_last_used(self, user_access_key_id=None, user_name=None):
        """
        GetAccessKeyLastUsed
        :user_access_key_id: str
        :user_name:str
        :return:
        """
        api_request = APIRequest('GetAccessKeyLastUsed', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserAccessKeyId": user_access_key_id, "UserName": user_name}
        return self._handle_request(api_request).result

    def upload_public_key(self, public_key_spec=None, user_name=None):
        """
        UploadPublicKey
        :public_key_spec: str
        :user_name: str
        :return:
        """
        api_request = APIRequest('UploadPublicKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"PublicKeySpec": public_key_spec, "UserName": user_name}
        return self._handle_request(api_request).result

    def update_public_key(self, user_public_key_id=None, user_name=None, status=None):
        """
        UpdatePublicKey
        :user_public_key_id: str
        :user_name: str
        :status: str
        :return:
        """
        api_request = APIRequest('UpdatePublicKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "UserPublicKeyId": user_public_key_id,
            "UserName": user_name,
            "Status": status}
        return self._handle_request(api_request).result

    def list_public_keys(self, user_name=None):
        """
        ListPublicKeys
        :user_name: str
        :return:
        """
        api_request = APIRequest('ListPublicKeys', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserName": user_name}
        return self._handle_request(api_request).result

    def delete_public_key(self, user_public_key_id=None, user_name=None):
        """
        组装的APIRequest

        :ivar action_name:
        :ivar method: HTTP请求方法
        :ivar scheme: HTTP请求scheme
        :ivar style: 请求样式
        :ivar param_position: 请求位置
        """
        api_request = APIRequest('DeletePublicKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserPublicKeyId": user_public_key_id, "UserName": user_name}
        return self._handle_request(api_request).result

    def get_public_key(self, user_public_key_id=None, user_name=None):
        api_request = APIRequest('GetPublicKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserPublicKeyId": user_public_key_id, "UserName": user_name}
        return self._handle_request(api_request).result

    def change_password(self, old_password=None, new_password=None):
        api_request = APIRequest('ChangePassword', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"OldPassword": old_password, "NewPassword": new_password}
        return self._handle_request(api_request).result

    def update_role(self, new_assume_role_policy_document=None, role_name=None):
        api_request = APIRequest('UpdateRole', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "NewAssumeRolePolicyDocument": new_assume_role_policy_document,
            "RoleName": role_name}
        return self._handle_request(api_request).result

    def set_security_preference(
            self,
            allow_user_to_manage_access_keys=None,
            allow_user_to_manage_mfa_devices=None,
            allow_user_to_manage_public_keys=None,
            enable_save_mfa_ticket=None,
            login_network_masks=None,
            allow_user_to_change_password=None,
            login_session_duration=None):
        api_request = APIRequest('SetSecurityPreference', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "AllowUserToManageAccessKeys": allow_user_to_manage_access_keys,
            "AllowUserToManageMFADevices": allow_user_to_manage_mfa_devices,
            "AllowUserToManagePublicKeys": allow_user_to_manage_public_keys,
            "EnableSaveMFATicket": enable_save_mfa_ticket,
            "LoginNetworkMasks": login_network_masks,
            "AllowUserToChangePassword": allow_user_to_change_password,
            "LoginSessionDuration": login_session_duration}
        return self._handle_request(api_request).result

    def list_roles(self, marker=None, max_items=None):
        api_request = APIRequest('ListRoles', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"Marker": marker, "MaxItems": max_items}
        return self._handle_request(api_request).result

    def list_policies_for_role(self, role_name=None):
        api_request = APIRequest('ListPoliciesForRole', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"RoleName": role_name}
        return self._handle_request(api_request).result

    def get_security_preference(self,):
        api_request = APIRequest('GetSecurityPreference', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def get_role(self, role_name=None):
        api_request = APIRequest('GetRole', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"RoleName": role_name}
        return self._handle_request(api_request).result

    def detach_policy_from_role(self, policy_type=None, role_name=None, policy_name=None):
        api_request = APIRequest('DetachPolicyFromRole', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "PolicyType": policy_type,
            "RoleName": role_name,
            "PolicyName": policy_name}
        return self._handle_request(api_request).result

    def delete_role(self, role_name=None):
        api_request = APIRequest('DeleteRole', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"RoleName": role_name}
        return self._handle_request(api_request).result

    def create_role(self, role_name=None, description=None, assume_role_policy_document=None):
        api_request = APIRequest('CreateRole', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "RoleName": role_name,
            "Description": description,
            "AssumeRolePolicyDocument": assume_role_policy_document}
        return self._handle_request(api_request).result

    def attach_policy_to_role(self, policy_type=None, role_name=None, policy_name=None):
        api_request = APIRequest('AttachPolicyToRole', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "PolicyType": policy_type,
            "RoleName": role_name,
            "PolicyName": policy_name}
        return self._handle_request(api_request).result

    def unbind_mfa_device(self, user_name=None):
        api_request = APIRequest('UnbindMFADevice', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserName": user_name}
        return self._handle_request(api_request).result

    def list_virtual_mfa_devices(self,):
        api_request = APIRequest('ListVirtualMFADevices', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def get_user_mfa_info(self, user_name=None):
        api_request = APIRequest('GetUserMFAInfo', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserName": user_name}
        return self._handle_request(api_request).result

    def delete_virtual_mfa_device(self, serial_number=None):
        api_request = APIRequest('DeleteVirtualMFADevice', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"SerialNumber": serial_number}
        return self._handle_request(api_request).result

    def create_virtual_mfa_device(self, virtual_mfa_device_name=None):
        api_request = APIRequest('CreateVirtualMFADevice', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"VirtualMFADeviceName": virtual_mfa_device_name}
        return self._handle_request(api_request).result

    def bind_mfa_device(
            self,
            serial_number=None,
            authentication_code2=None,
            authentication_code1=None,
            user_name=None):
        api_request = APIRequest('BindMFADevice', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "SerialNumber": serial_number,
            "AuthenticationCode2": authentication_code2,
            "AuthenticationCode1": authentication_code1,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def update_login_profile(
            self,
            password=None,
            password_reset_required=None,
            mfa_bind_required=None,
            user_name=None):
        api_request = APIRequest('UpdateLoginProfile', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Password": password,
            "PasswordResetRequired": password_reset_required,
            "MFABindRequired": mfa_bind_required,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def get_login_profile(self, user_name=None):
        api_request = APIRequest('GetLoginProfile', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserName": user_name}
        return self._handle_request(api_request).result

    def delete_login_profile(self, user_name=None):
        api_request = APIRequest('DeleteLoginProfile', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserName": user_name}
        return self._handle_request(api_request).result

    def create_login_profile(
            self,
            password=None,
            password_reset_required=None,
            mfa_bind_required=None,
            user_name=None):
        api_request = APIRequest('CreateLoginProfile', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Password": password,
            "PasswordResetRequired": password_reset_required,
            "MFABindRequired": mfa_bind_required,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def update_user(
            self,
            new_user_name=None,
            new_display_name=None,
            new_mobile_phone=None,
            new_comments=None,
            new_email=None,
            user_name=None):
        api_request = APIRequest('UpdateUser', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "NewUserName": new_user_name,
            "NewDisplayName": new_display_name,
            "NewMobilePhone": new_mobile_phone,
            "NewComments": new_comments,
            "NewEmail": new_email,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def list_users(self, marker=None, max_items=None):
        api_request = APIRequest('ListUsers', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"Marker": marker, "MaxItems": max_items}
        return self._handle_request(api_request).result

    def get_user(self, user_name=None):
        api_request = APIRequest('GetUser', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserName": user_name}
        return self._handle_request(api_request).result

    def delete_user(self, user_name=None):
        api_request = APIRequest('DeleteUser', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserName": user_name}
        return self._handle_request(api_request).result

    def create_user(
            self,
            comments=None,
            display_name=None,
            mobile_phone=None,
            email=None,
            user_name=None):
        api_request = APIRequest('CreateUser', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Comments": comments,
            "DisplayName": display_name,
            "MobilePhone": mobile_phone,
            "Email": email,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def update_access_key(self, user_access_key_id=None, user_name=None, status=None):
        api_request = APIRequest('UpdateAccessKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "UserAccessKeyId": user_access_key_id,
            "UserName": user_name,
            "Status": status}
        return self._handle_request(api_request).result

    def list_access_keys(self, user_name=None):
        api_request = APIRequest('ListAccessKeys', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserName": user_name}
        return self._handle_request(api_request).result

    def delete_access_key(self, user_access_key_id=None, user_name=None):
        api_request = APIRequest('DeleteAccessKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserAccessKeyId": user_access_key_id, "UserName": user_name}
        return self._handle_request(api_request).result

    def create_access_key(self, user_name=None):
        api_request = APIRequest('CreateAccessKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserName": user_name}
        return self._handle_request(api_request).result

    def set_password_policy(
            self,
            require_numbers=None,
            password_reuse_prevention=None,
            require_uppercase_characters=None,
            max_password_age=None,
            max_login_attemps=None,
            hard_expiry=None,
            minimum_password_length=None,
            require_lowercase_characters=None,
            require_symbols=None):
        api_request = APIRequest('SetPasswordPolicy', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "RequireNumbers": require_numbers,
            "PasswordReusePrevention": password_reuse_prevention,
            "RequireUppercaseCharacters": require_uppercase_characters,
            "MaxPasswordAge": max_password_age,
            "MaxLoginAttemps": max_login_attemps,
            "HardExpiry": hard_expiry,
            "MinimumPasswordLength": minimum_password_length,
            "RequireLowercaseCharacters": require_lowercase_characters,
            "RequireSymbols": require_symbols}
        return self._handle_request(api_request).result

    def set_account_alias(self, account_alias=None):
        api_request = APIRequest('SetAccountAlias', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"AccountAlias": account_alias}
        return self._handle_request(api_request).result

    def get_password_policy(self,):
        api_request = APIRequest('GetPasswordPolicy', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def get_account_alias(self,):
        api_request = APIRequest('GetAccountAlias', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def clear_account_alias(self,):
        api_request = APIRequest('ClearAccountAlias', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def set_default_policy_version(self, version_id=None, policy_name=None):
        api_request = APIRequest('SetDefaultPolicyVersion', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"VersionId": version_id, "PolicyName": policy_name}
        return self._handle_request(api_request).result

    def list_policy_versions(self, policy_type=None, policy_name=None):
        api_request = APIRequest('ListPolicyVersions', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"PolicyType": policy_type, "PolicyName": policy_name}
        return self._handle_request(api_request).result

    def get_policy_version(self, version_id=None, policy_type=None, policy_name=None):
        api_request = APIRequest('GetPolicyVersion', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "VersionId": version_id,
            "PolicyType": policy_type,
            "PolicyName": policy_name}
        return self._handle_request(api_request).result

    def delete_policy_version(self, version_id=None, policy_name=None):
        api_request = APIRequest('DeletePolicyVersion', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"VersionId": version_id, "PolicyName": policy_name}
        return self._handle_request(api_request).result

    def create_policy_version(self, set_as_default=None, policy_name=None, policy_document=None):
        api_request = APIRequest('CreatePolicyVersion', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "SetAsDefault": set_as_default,
            "PolicyName": policy_name,
            "PolicyDocument": policy_document}
        return self._handle_request(api_request).result

    def list_policies_for_user(self, user_name=None):
        api_request = APIRequest('ListPoliciesForUser', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserName": user_name}
        return self._handle_request(api_request).result

    def list_policies_for_group(self, group_name=None):
        api_request = APIRequest('ListPoliciesForGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"GroupName": group_name}
        return self._handle_request(api_request).result

    def list_entities_for_policy(self, policy_type=None, policy_name=None):
        api_request = APIRequest('ListEntitiesForPolicy', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"PolicyType": policy_type, "PolicyName": policy_name}
        return self._handle_request(api_request).result

    def detach_policy_from_user(self, policy_type=None, policy_name=None, user_name=None):
        api_request = APIRequest('DetachPolicyFromUser', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "PolicyType": policy_type,
            "PolicyName": policy_name,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def detach_policy_from_group(self, policy_type=None, policy_name=None, group_name=None):
        api_request = APIRequest('DetachPolicyFromGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "PolicyType": policy_type,
            "PolicyName": policy_name,
            "GroupName": group_name}
        return self._handle_request(api_request).result

    def attach_policy_to_user(self, policy_type=None, policy_name=None, user_name=None):
        api_request = APIRequest('AttachPolicyToUser', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "PolicyType": policy_type,
            "PolicyName": policy_name,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def attach_policy_to_group(self, policy_type=None, policy_name=None, group_name=None):
        api_request = APIRequest('AttachPolicyToGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "PolicyType": policy_type,
            "PolicyName": policy_name,
            "GroupName": group_name}
        return self._handle_request(api_request).result

    def list_policies(self, policy_type=None, marker=None, max_items=None):
        api_request = APIRequest('ListPolicies', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"PolicyType": policy_type, "Marker": marker, "MaxItems": max_items}
        return self._handle_request(api_request).result

    def get_policy(self, policy_type=None, policy_name=None):
        api_request = APIRequest('GetPolicy', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"PolicyType": policy_type, "PolicyName": policy_name}
        return self._handle_request(api_request).result

    def delete_policy(self, policy_name=None):
        api_request = APIRequest('DeletePolicy', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"PolicyName": policy_name}
        return self._handle_request(api_request).result

    def create_policy(self, description=None, policy_name=None, policy_document=None):
        api_request = APIRequest('CreatePolicy', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Description": description,
            "PolicyName": policy_name,
            "PolicyDocument": policy_document}
        return self._handle_request(api_request).result

    def remove_user_from_group(self, group_name=None, user_name=None):
        api_request = APIRequest('RemoveUserFromGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"GroupName": group_name, "UserName": user_name}
        return self._handle_request(api_request).result

    def list_users_for_group(self, marker=None, max_items=None, group_name=None):
        api_request = APIRequest('ListUsersForGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"Marker": marker, "MaxItems": max_items, "GroupName": group_name}
        return self._handle_request(api_request).result

    def list_groups_for_user(self, user_name=None):
        api_request = APIRequest('ListGroupsForUser', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserName": user_name}
        return self._handle_request(api_request).result

    def add_user_to_group(self, group_name=None, user_name=None):
        api_request = APIRequest('AddUserToGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"GroupName": group_name, "UserName": user_name}
        return self._handle_request(api_request).result

    def update_group(self, new_group_name=None, new_comments=None, group_name=None):
        api_request = APIRequest('UpdateGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "NewGroupName": new_group_name,
            "NewComments": new_comments,
            "GroupName": group_name}
        return self._handle_request(api_request).result

    def list_groups(self, marker=None, max_items=None):
        api_request = APIRequest('ListGroups', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"Marker": marker, "MaxItems": max_items}
        return self._handle_request(api_request).result

    def get_group(self, group_name=None):
        api_request = APIRequest('GetGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"GroupName": group_name}
        return self._handle_request(api_request).result

    def delete_group(self, group_name=None):
        api_request = APIRequest('DeleteGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"GroupName": group_name}
        return self._handle_request(api_request).result

    def create_group(self, comments=None, group_name=None):
        api_request = APIRequest('CreateGroup', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"Comments": comments, "GroupName": group_name}
        return self._handle_request(api_request).result
