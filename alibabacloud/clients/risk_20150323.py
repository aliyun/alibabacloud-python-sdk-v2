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


class RiskClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Risk'
        self.api_version = '2015-03-23'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def validate_verify_code(
            self,
            id_type=None,
            verify_code=None,
            code_type=None,
            request_id=None,
            umid_token=None,
            collina=None,
            ip=None,
            channel_type=None,
            user_id=None,
            mtee_code=None):
        api_request = APIRequest('ValidateVerifyCode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IdType": id_type,
            "VerifyCode": verify_code,
            "CodeType": code_type,
            "RequestId": request_id,
            "UmidToken": umid_token,
            "Collina": collina,
            "Ip": ip,
            "ChannelType": channel_type,
            "UserId": user_id,
            "MteeCode": mtee_code}
        return self._handle_request(api_request).result

    def send_verify_code(
            self,
            id_type=None,
            event_id=None,
            time_interval=None,
            code_type=None,
            request_id=None,
            channel_type=None,
            biz_id=None,
            message_reiver=None,
            user_id=None,
            mtee_code=None):
        api_request = APIRequest('SendVerifyCode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IdType": id_type,
            "EventId": event_id,
            "TimeInterval": time_interval,
            "CodeType": code_type,
            "RequestId": request_id,
            "ChannelType": channel_type,
            "BizId": biz_id,
            "MessageReiver": message_reiver,
            "UserId": user_id,
            "MteeCode": mtee_code}
        return self._handle_request(api_request).result

    def find_risk(
            self,
            id_type=None,
            code_type=None,
            phone=None,
            umid_token=None,
            collina=None,
            ip=None,
            user_id=None,
            mtee_code=None,
            email=None):
        api_request = APIRequest('FindRisk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IdType": id_type,
            "CodeType": code_type,
            "Phone": phone,
            "UmidToken": umid_token,
            "Collina": collina,
            "Ip": ip,
            "UserId": user_id,
            "MteeCode": mtee_code,
            "Email": email}
        return self._handle_request(api_request).result
