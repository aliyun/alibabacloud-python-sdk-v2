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


class FaasClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'faas'
        self.api_version = '2017-08-24'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def delete_publish_fpga_image(self, image_id=None, fpga_image_uuid=None, caller_uid=None):
        api_request = APIRequest('DeletePublishFpgaImage', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageID": image_id,
            "FpgaImageUUID": fpga_image_uuid,
            "callerUid": caller_uid}
        return self._handle_request(api_request).result

    def update_image_attribute(
            self,
            name=None,
            description=None,
            fpga_image_uuid=None,
            caller_uid=None,
            tags=None):
        api_request = APIRequest('UpdateImageAttribute', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "Name": name,
            "Description": description,
            "FpgaImageUUID": fpga_image_uuid,
            "callerUid": caller_uid,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_publish_fpga_images(self, image_id=None, security_token=None, caller_uid=None):
        api_request = APIRequest('DescribePublishFpgaImages', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageID": image_id,
            "SecurityToken": security_token,
            "callerUid": caller_uid}
        return self._handle_request(api_request).result

    def publish_fpga_image(self, image_id=None, fpga_image_uuid=None, caller_uid=None):
        api_request = APIRequest('PublishFpgaImage', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageID": image_id,
            "FpgaImageUUID": fpga_image_uuid,
            "callerUid": caller_uid}
        return self._handle_request(api_request).result

    def update_create_task(
            self,
            state=None,
            owner_id=None,
            fpga_image_object_name=None,
            fpga_image_uuid=None,
            caller_uid=None):
        api_request = APIRequest('UpdateCreateTask', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "State": state,
            "OwnerId": owner_id,
            "FpgaImageObjectName": fpga_image_object_name,
            "FpgaImageUUID": fpga_image_uuid,
            "callerUid": caller_uid}
        return self._handle_request(api_request).result

    def pull_create_task(self,):
        api_request = APIRequest('PullCreateTask', 'POST', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def load_fpga_image_task(
            self,
            fpga_image_type=None,
            shell_uuid=None,
            owner_alias=None,
            fpga_image_uuid=None,
            instance_id=None,
            security_token=None,
            role_arn=None,
            fpga_type=None,
            fpga_uuid=None,
            object=None):
        api_request = APIRequest('LoadFpgaImageTask', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "FpgaImageType": fpga_image_type,
            "ShellUUID": shell_uuid,
            "OwnerAlias": owner_alias,
            "FpgaImageUUID": fpga_image_uuid,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "RoleArn": role_arn,
            "FpgaType": fpga_type,
            "FpgaUUID": fpga_uuid,
            "Object": object}
        return self._handle_request(api_request).result

    def describe_load_task_status(
            self,
            instance_id=None,
            security_token=None,
            role_arn=None,
            fpga_uuid=None):
        api_request = APIRequest('DescribeLoadTaskStatus', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "RoleArn": role_arn,
            "FpgaUUID": fpga_uuid}
        return self._handle_request(api_request).result

    def describe_fpga_instances(self, instance_id=None, security_token=None, role_arn=None):
        api_request = APIRequest('DescribeFpgaInstances', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "RoleArn": role_arn}
        return self._handle_request(api_request).result

    def describe_fpga_images(self, caller_uid=None):
        api_request = APIRequest('DescribeFpgaImages', 'POST', 'http', 'RPC', 'query')
        api_request._params = {"callerUid": caller_uid}
        return self._handle_request(api_request).result

    def delete_fpga_image(self, fpga_image_uuid=None, caller_uid=None):
        api_request = APIRequest('DeleteFpgaImage', 'POST', 'http', 'RPC', 'query')
        api_request._params = {"FpgaImageUUID": fpga_image_uuid, "callerUid": caller_uid}
        return self._handle_request(api_request).result

    def create_fpga_image_task(
            self,
            description=None,
            key_id=None,
            shell_uuid=None,
            tags=None,
            bucket=None,
            encrypted=None,
            role_arn=None,
            name=None,
            fpga_type=None,
            email=None,
            object=None):
        api_request = APIRequest('CreateFpgaImageTask', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "Description": description,
            "KeyId": key_id,
            "ShellUUID": shell_uuid,
            "Tags": tags,
            "Bucket": bucket,
            "Encrypted": encrypted,
            "RoleArn": role_arn,
            "Name": name,
            "FpgaType": fpga_type,
            "Email": email,
            "Object": object}
        return self._handle_request(api_request).result
