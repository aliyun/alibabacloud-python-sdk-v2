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


class BatchComputeClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'BatchCompute'
        self.api_version = '2015-06-30'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def modify_job(self, resource_owner_id=None, resource_name=None):
        api_request = APIRequest('ModifyJob', 'PUT', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/jobs/[ResourceName]'
        api_request._params = {"ResourceOwnerId": resource_owner_id, "ResourceName": resource_name}
        return self._handle_request(api_request).result

    def release_job(self, resource_owner_id=None, resource_name=None):
        api_request = APIRequest('ReleaseJob', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/2013-01-11/jobs/[ResourceName]'
        api_request._params = {"ResourceOwnerId": resource_owner_id, "ResourceName": resource_name}
        return self._handle_request(api_request).result

    def put_job(self, resource_owner_id=None, resource_name=None):
        api_request = APIRequest('PutJob', 'PUT', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/jobs/[ResourceName]/Priority'
        api_request._params = {"ResourceOwnerId": resource_owner_id, "ResourceName": resource_name}
        return self._handle_request(api_request).result

    def post_job(self, resource_owner_id=None):
        api_request = APIRequest('PostJob', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/jobs'
        api_request._params = {"ResourceOwnerId": resource_owner_id}
        return self._handle_request(api_request).result

    def list_snapshots(self, resource_owner_id=None):
        api_request = APIRequest('ListSnapshots', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/snapshots'
        api_request._params = {"ResourceOwnerId": resource_owner_id}
        return self._handle_request(api_request).result

    def list_jobs(self, resource_owner_id=None):
        api_request = APIRequest('ListJobs', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/jobs'
        api_request._params = {"ResourceOwnerId": resource_owner_id}
        return self._handle_request(api_request).result

    def list_images(self, resource_owner_id=None):
        api_request = APIRequest('ListImages', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/images'
        api_request._params = {"ResourceOwnerId": resource_owner_id}
        return self._handle_request(api_request).result

    def get_tasks(self, resource_owner_id=None, resource_name=None):
        api_request = APIRequest('GetTasks', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/jobs/[ResourceName]/tasks'
        api_request._params = {"ResourceOwnerId": resource_owner_id, "ResourceName": resource_name}
        return self._handle_request(api_request).result

    def get_job_description(self, resource_owner_id=None, resource_name=None):
        api_request = APIRequest('GetJobDescription', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/jobs/[ResourceName]/description'
        api_request._params = {"ResourceOwnerId": resource_owner_id, "ResourceName": resource_name}
        return self._handle_request(api_request).result

    def get_job(self, resource_owner_id=None, resource_name=None):
        api_request = APIRequest('GetJob', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/jobs/[ResourceName]'
        api_request._params = {"ResourceOwnerId": resource_owner_id, "ResourceName": resource_name}
        return self._handle_request(api_request).result

    def delete_job(self, resource_owner_id=None, resource_name=None):
        api_request = APIRequest('DeleteJob', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/jobs/[ResourceName]'
        api_request._params = {"ResourceOwnerId": resource_owner_id, "ResourceName": resource_name}
        return self._handle_request(api_request).result
