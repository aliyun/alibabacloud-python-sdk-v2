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


class HPCClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'HPC'
        self.api_version = '2016-06-03'
        self.location_service_code = 'hpc'
        self.location_endpoint_type = 'openAPI'

    def stop_jumpserver(self, instance_id=None, region_id=None, force=None, token=None):
        api_request = APIRequest('StopJumpserver', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "RegionId": region_id,
            "Force": force,
            "TOKEN": token}
        return self._handle_request(api_request).result

    def start_jumpserver(self, instance_id=None, region_id=None, force=None, token=None):
        api_request = APIRequest('StartJumpserver', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "RegionId": region_id,
            "Force": force,
            "TOKEN": token}
        return self._handle_request(api_request).result

    def reboot_jumpserver(self, instance_id=None, region_id=None, force=None, token=None):
        api_request = APIRequest('RebootJumpserver', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "RegionId": region_id,
            "Force": force,
            "TOKEN": token}
        return self._handle_request(api_request).result

    def reboot_instance(self, instance_id=None, region_id=None, token=None):
        api_request = APIRequest('RebootInstance', 'POST', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "RegionId": region_id, "TOKEN": token}
        return self._handle_request(api_request).result

    def modify_jumpserver_password(self, instance_id=None, new_password=None, token=None):
        api_request = APIRequest('ModifyJumpserverPassword', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "NewPassword": new_password,
            "TOKEN": token}
        return self._handle_request(api_request).result

    def describe_instances(self, instance_id=None, instance_type=None, token=None):
        api_request = APIRequest('DescribeInstances', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "InstanceType": instance_type,
            "TOKEN": token}
        return self._handle_request(api_request).result

    def delete_instance(self, instance_id=None, region_id=None, token=None):
        api_request = APIRequest('DeleteInstance', 'POST', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "RegionId": region_id, "TOKEN": token}
        return self._handle_request(api_request).result

    def create_instance(self, region_id=None, package_id=None, token=None):
        api_request = APIRequest('CreateInstance', 'POST', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "PackageId": package_id, "TOKEN": token}
        return self._handle_request(api_request).result
