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


class UbsmsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Ubsms'
        self.api_version = '2015-06-23'
        self.location_service_code = 'ubsms'
        self.location_endpoint_type = 'openAPI'

    def describe_business_status(self, password=None, caller_bid=None):
        api_request = APIRequest('DescribeBusinessStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Password": password, "callerBid": caller_bid}
        return self._handle_request(api_request).result

    def notify_user_business_command(
            self,
            uid=None,
            password=None,
            instance_id=None,
            service_code=None,
            client_token=None,
            cmd=None,
            region=None):
        api_request = APIRequest('NotifyUserBusinessCommand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Uid": uid,
            "Password": password,
            "InstanceId": instance_id,
            "ServiceCode": service_code,
            "ClientToken": client_token,
            "Cmd": cmd,
            "Region": region}
        return self._handle_request(api_request).result

    def set_user_business_status(self, uid=None, status_value=None, service=None, status_key=None):
        api_request = APIRequest('SetUserBusinessStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Uid": uid,
            "StatusValue": status_value,
            "Service": service,
            "StatusKey": status_key}
        return self._handle_request(api_request).result
