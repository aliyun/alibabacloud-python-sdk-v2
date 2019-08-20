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


class TeslaDamClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'TeslaDam'
        self.api_version = '2018-01-18'
        self.location_service_code = 'tesladam'
        self.location_endpoint_type = 'openAPI'

    def action(self, order_id=None, step_code=None):
        api_request = APIRequest('Action', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OrderId": order_id, "StepCode": step_code}
        return self._handle_request(api_request).result

    def action_disk_rma(
            self,
            disk_name=None,
            execution_id=None,
            disk_slot=None,
            hostname=None,
            disk_mount=None,
            disk_reason=None,
            disk_sn=None):
        api_request = APIRequest('ActionDiskRma', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DiskName": disk_name,
            "ExecutionId": execution_id,
            "DiskSlot": disk_slot,
            "Hostname": hostname,
            "DiskMount": disk_mount,
            "DiskReason": disk_reason,
            "DiskSn": disk_sn}
        return self._handle_request(api_request).result

    def host_gets(self, query=None, end_time=None, start_time=None, query_type=None):
        api_request = APIRequest('HostGets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Query": query,
            "EndTime": end_time,
            "StartTime": start_time,
            "QueryType": query_type}
        return self._handle_request(api_request).result

    def action_disk_mask(self, op=None, disk_mount=None, ip=None):
        api_request = APIRequest('ActionDiskMask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Op": op, "DiskMount": disk_mount, "Ip": ip}
        return self._handle_request(api_request).result

    def action_disk_check(self, disk_mount=None, ip=None):
        api_request = APIRequest('ActionDiskCheck', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DiskMount": disk_mount, "Ip": ip}
        return self._handle_request(api_request).result
