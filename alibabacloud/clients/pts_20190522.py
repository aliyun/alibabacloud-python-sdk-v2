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


class PTSClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'PTS'
        self.api_version = '2019-05-22'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def get_aliware_report(self, report_id=None):
        api_request = APIRequest('GetAliwareReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ReportId": report_id}
        return self._handle_request(api_request).result

    def get_report(self, report_id=None):
        api_request = APIRequest('GetReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ReportId": report_id}
        return self._handle_request(api_request).result

    def start_scene(self, team_id=None, scene_id=None, user_id=None, task_id=None):
        api_request = APIRequest('StartScene', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TeamId": team_id,
            "SceneId": scene_id,
            "UserId": user_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result
