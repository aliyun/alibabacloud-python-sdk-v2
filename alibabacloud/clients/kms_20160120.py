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

from alibabacloud.client import AlibabaCloudClient
from alibabacloud.request import APIRequest
from alibabacloud.utils.parameter_validation import verify_params


class KmsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Kms'
        self.api_version = '2016-01-20'
        self.location_service_code = 'kms'
        self.location_endpoint_type = 'openAPI'

    def describe_service(self,):
        api_request = APIRequest('DescribeService', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def update_alias(self, alias_name=None, key_id=None):
        api_request = APIRequest('UpdateAlias', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"AliasName": alias_name, "KeyId": key_id}
        return self._handle_request(api_request).result

    def untag_resource(self, tag_keys=None, key_id=None):
        api_request = APIRequest('UntagResource', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"TagKeys": tag_keys, "KeyId": key_id}
        return self._handle_request(api_request).result

    def tag_resource(self, key_id=None, tags=None):
        api_request = APIRequest('TagResource', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"KeyId": key_id, "Tags": tags}
        return self._handle_request(api_request).result

    def schedule_key_deletion(self, pending_window_in_days=None, key_id=None):
        api_request = APIRequest('ScheduleKeyDeletion', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"PendingWindowInDays": pending_window_in_days, "KeyId": key_id}
        return self._handle_request(api_request).result

    def list_resource_tags(self, key_id=None):
        api_request = APIRequest('ListResourceTags', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"KeyId": key_id}
        return self._handle_request(api_request).result

    def list_keys(self, page_size=None, page_number=None):
        api_request = APIRequest('ListKeys', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_aliases_by_key_id(self, page_size=None, key_id=None, page_number=None):
        api_request = APIRequest('ListAliasesByKeyId', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "KeyId": key_id, "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_aliases(self, page_size=None, page_number=None):
        api_request = APIRequest('ListAliases', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "PageNumber": page_number}
        return self._handle_request(api_request).result

    def import_key_material(
            self,
            import_token=None,
            encrypted_key_material=None,
            key_material_expire_unix=None,
            key_id=None):
        api_request = APIRequest('ImportKeyMaterial', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ImportToken": import_token,
            "EncryptedKeyMaterial": encrypted_key_material,
            "KeyMaterialExpireUnix": key_material_expire_unix,
            "KeyId": key_id}
        return self._handle_request(api_request).result

    def get_parameters_for_import(
            self,
            key_id=None,
            wrapping_algorithm=None,
            wrapping_key_spec=None):
        api_request = APIRequest('GetParametersForImport', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "KeyId": key_id,
            "WrappingAlgorithm": wrapping_algorithm,
            "WrappingKeySpec": wrapping_key_spec}
        return self._handle_request(api_request).result

    def generate_data_key(
            self,
            encryption_context=None,
            key_id=None,
            key_spec=None,
            number_of_bytes=None):
        api_request = APIRequest('GenerateDataKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "EncryptionContext": encryption_context,
            "KeyId": key_id,
            "KeySpec": key_spec,
            "NumberOfBytes": number_of_bytes}
        return self._handle_request(api_request).result

    def encrypt(self, encryption_context=None, key_id=None, plaintext=None):
        api_request = APIRequest('Encrypt', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "EncryptionContext": encryption_context,
            "KeyId": key_id,
            "Plaintext": plaintext}
        return self._handle_request(api_request).result

    def enable_key(self, key_id=None):
        api_request = APIRequest('EnableKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"KeyId": key_id}
        return self._handle_request(api_request).result

    def disable_key(self, key_id=None):
        api_request = APIRequest('DisableKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"KeyId": key_id}
        return self._handle_request(api_request).result

    def describe_key(self, key_id=None):
        api_request = APIRequest('DescribeKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"KeyId": key_id}
        return self._handle_request(api_request).result

    def delete_key_material(self, key_id=None):
        api_request = APIRequest('DeleteKeyMaterial', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"KeyId": key_id}
        return self._handle_request(api_request).result

    def delete_alias(self, alias_name=None):
        api_request = APIRequest('DeleteAlias', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"AliasName": alias_name}
        return self._handle_request(api_request).result

    def decrypt(self, encryption_context=None, ciphertext_blob=None):
        api_request = APIRequest('Decrypt', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "EncryptionContext": encryption_context,
            "CiphertextBlob": ciphertext_blob}
        return self._handle_request(api_request).result

    def create_key(self, protection_level=None, key_usage=None, origin=None, description=None):
        api_request = APIRequest('CreateKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "ProtectionLevel": protection_level,
            "KeyUsage": key_usage,
            "Origin": origin,
            "Description": description}
        return self._handle_request(api_request).result

    def create_alias(self, alias_name=None, key_id=None):
        api_request = APIRequest('CreateAlias', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"AliasName": alias_name, "KeyId": key_id}
        return self._handle_request(api_request).result

    def cancel_key_deletion(self, key_id=None):
        api_request = APIRequest('CancelKeyDeletion', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"KeyId": key_id}
        return self._handle_request(api_request).result
