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


class WelfareinnerClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'welfare-inner'
        self.api_version = '2018-05-24'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def get_welfare_geek_info(self, app_name=None, pk=None):
        api_request = APIRequest('GetWelfareGeekInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AppName": app_name, "Pk": pk}
        return self._handle_request(api_request).result

    def do_logical_delete_resource(
            self,
            country=None,
            hid=None,
            success=None,
            interrupt=None,
            gmt_wakeup=None,
            pk=None,
            invoker=None,
            bid=None,
            message=None,
            task_extra_data=None,
            task_identifier=None):
        api_request = APIRequest('DoLogicalDeleteResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "Hid": hid,
            "Success": success,
            "Interrupt": interrupt,
            "GmtWakeup": gmt_wakeup,
            "Pk": pk,
            "Invoker": invoker,
            "Bid": bid,
            "Message": message,
            "TaskExtraData": task_extra_data,
            "TaskIdentifier": task_identifier}
        return self._handle_request(api_request).result

    def do_check_resource(
            self,
            country=None,
            hid=None,
            level=None,
            invoker=None,
            message=None,
            url=None,
            success=None,
            interrupt=None,
            gmt_wakeup=None,
            pk=None,
            bid=None,
            prompt=None,
            task_extra_data=None,
            task_identifier=None):
        api_request = APIRequest('DoCheckResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "Hid": hid,
            "Level": level,
            "Invoker": invoker,
            "Message": message,
            "Url": url,
            "Success": success,
            "Interrupt": interrupt,
            "GmtWakeup": gmt_wakeup,
            "Pk": pk,
            "Bid": bid,
            "Prompt": prompt,
            "TaskExtraData": task_extra_data,
            "TaskIdentifier": task_identifier}
        return self._handle_request(api_request).result

    def do_physical_delete_resource(
            self,
            country=None,
            hid=None,
            success=None,
            interrupt=None,
            gmt_wakeup=None,
            pk=None,
            invoker=None,
            bid=None,
            message=None,
            task_extra_data=None,
            task_identifier=None):
        api_request = APIRequest('DoPhysicalDeleteResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "Hid": hid,
            "Success": success,
            "Interrupt": interrupt,
            "GmtWakeup": gmt_wakeup,
            "Pk": pk,
            "Invoker": invoker,
            "Bid": bid,
            "Message": message,
            "TaskExtraData": task_extra_data,
            "TaskIdentifier": task_identifier}
        return self._handle_request(api_request).result
