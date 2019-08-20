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


class TeslaStreamClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'TeslaStream'
        self.api_version = '2018-01-15'
        self.location_service_code = 'teslastream'
        self.location_endpoint_type = 'openAPI'

    def get_job_topology(self, job_name=None):
        api_request = APIRequest('GetJobTopology', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JobName": job_name}
        return self._handle_request(api_request).result

    def batch_get_plugin_config_info(self, plugin_infos=None):
        api_request = APIRequest('BatchGetPluginConfigInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PluginInfos": plugin_infos}
        return self._handle_request(api_request).result

    def batch_get_job_metric_info(self, job_infos=None):
        api_request = APIRequest('BatchGetJobMetricInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JobInfos": job_infos}
        return self._handle_request(api_request).result
