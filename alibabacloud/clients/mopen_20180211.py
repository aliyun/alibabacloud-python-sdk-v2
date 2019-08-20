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


class MoPenClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'MoPen'
        self.api_version = '2018-02-11'
        self.location_service_code = 'mopen'
        self.location_endpoint_type = 'openAPI'

    def mo_pen_find_group(self, creator=None):
        api_request = APIRequest('MoPenFindGroup', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"Creator": creator}
        return self._handle_request(api_request).result

    def mo_pen_query_canvas(self, device_name=None, session_id=None, page_id=None, status=None):
        api_request = APIRequest('MoPenQueryCanvas', 'POST', 'https', 'RPC', 'body')
        api_request._params = {
            "DeviceName": device_name,
            "SessionId": session_id,
            "PageId": page_id,
            "Status": status}
        return self._handle_request(api_request).result

    def mo_pen_do_recognize(
            self,
            canvas_id=None,
            end_y=None,
            end_x=None,
            json_conf=None,
            export_type=None,
            start_y=None,
            start_x=None):
        api_request = APIRequest('MoPenDoRecognize', 'POST', 'https', 'RPC', 'body')
        api_request._params = {
            "CanvasId": canvas_id,
            "EndY": end_y,
            "EndX": end_x,
            "JsonConf": json_conf,
            "ExportType": export_type,
            "StartY": start_y,
            "StartX": start_x}
        return self._handle_request(api_request).result

    def mo_pen_send_mqtt_message(self, payload=None, device_name=None):
        api_request = APIRequest('MoPenSendMqttMessage', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"Payload": payload, "DeviceName": device_name}
        return self._handle_request(api_request).result

    def mopen_create_group(self, creator=None):
        api_request = APIRequest('MopenCreateGroup', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"Creator": creator}
        return self._handle_request(api_request).result

    def mo_pen_add_group_member(self, group_id=None, device_name=None):
        api_request = APIRequest('MoPenAddGroupMember', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"GroupId": group_id, "DeviceName": device_name}
        return self._handle_request(api_request).result

    def mo_pen_delete_group(self, group_id=None):
        api_request = APIRequest('MoPenDeleteGroup', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"GroupId": group_id}
        return self._handle_request(api_request).result

    def mo_pen_bind_isv(self, order_key=None, device_name=None):
        api_request = APIRequest('MoPenBindIsv', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"OrderKey": order_key, "DeviceName": device_name}
        return self._handle_request(api_request).result

    def mo_pen_delete_group_member(self, group_id=None, device_name=None):
        api_request = APIRequest('MoPenDeleteGroupMember', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"GroupId": group_id, "DeviceName": device_name}
        return self._handle_request(api_request).result

    def mo_pen_create_device(self, device_name=None, device_type=None):
        api_request = APIRequest('MoPenCreateDevice', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"DeviceName": device_name, "DeviceType": device_type}
        return self._handle_request(api_request).result
