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


class CSBClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'CSB'
        self.api_version = '2017-11-18'
        self.location_service_code = 'csb'
        self.location_endpoint_type = 'openAPI'

    def approve_order_list(self, data=None, ):
        api_request = APIRequest(
            'ApproveOrderList',
            'POST',
            'https',
            'RPC',
            'body')
        api_request._params = {"Data": data, }
        return self._handle_request(api_request).result


class crClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'cr'
        self.api_version = '2016-06-07'
        self.location_service_code = 'cr'
        self.location_endpoint_type = 'openAPI'

    def get_namespace_authorization_list(
            self, namespace=None, authorize=None, ):
        api_request = APIRequest(
            'GetNamespaceAuthorizationList',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/namespace/[Namespace]/authorizations'
        api_request._params = {
            "Namespace": namespace,
            "Authorize": authorize,
        }
        return self._handle_request(api_request).result


class OpenanalyticsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'openanalytics'
        self.api_version = '2018-03-01'
        self.location_service_code = 'openanalytics'
        self.location_endpoint_type = 'openAPI'

    def get_region_status(self, target_uid=None, ):
        api_request = APIRequest(
            'GetRegionStatus', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"TargetUid": target_uid, }
        return self._handle_request(api_request).result
