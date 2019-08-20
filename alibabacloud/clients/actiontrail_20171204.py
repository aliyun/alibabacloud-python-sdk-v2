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


class ActiontrailClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Actiontrail'
        self.api_version = '2017-12-04'
        self.location_service_code = 'actiontrail'
        self.location_endpoint_type = 'openAPI'

    def describe_regions(self,):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def lookup_events(
            self,
            request=None,
            event_access_key_id=None,
            end_time=None,
            event_rw=None,
            start_time=None,
            resource_type=None,
            event_name=None,
            next_token=None,
            max_results=None,
            event_type=None,
            service_name=None,
            resource_name=None,
            event=None,
            user=None):
        api_request = APIRequest('LookupEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Request": request,
            "EventAccessKeyId": event_access_key_id,
            "EndTime": end_time,
            "EventRW": event_rw,
            "StartTime": start_time,
            "ResourceType": resource_type,
            "EventName": event_name,
            "NextToken": next_token,
            "MaxResults": max_results,
            "EventType": event_type,
            "ServiceName": service_name,
            "ResourceName": resource_name,
            "Event": event,
            "User": user}
        return self._handle_request(api_request).result

    def update_trail(
            self,
            sls_project_arn=None,
            sls_write_role_arn=None,
            role_name=None,
            name=None,
            oss_bucket_name=None,
            oss_key_prefix=None,
            event_rw=None):
        api_request = APIRequest('UpdateTrail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SlsProjectArn": sls_project_arn,
            "SlsWriteRoleArn": sls_write_role_arn,
            "RoleName": role_name,
            "Name": name,
            "OssBucketName": oss_bucket_name,
            "OssKeyPrefix": oss_key_prefix,
            "EventRW": event_rw}
        return self._handle_request(api_request).result

    def stop_logging(self, name=None):
        api_request = APIRequest('StopLogging', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name}
        return self._handle_request(api_request).result

    def get_trail_status(self, name=None):
        api_request = APIRequest('GetTrailStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name}
        return self._handle_request(api_request).result

    def describe_trails(self, name_list=None, include_shadow_trails=None):
        api_request = APIRequest('DescribeTrails', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"NameList": name_list, "IncludeShadowTrails": include_shadow_trails}
        return self._handle_request(api_request).result

    def start_logging(self, name=None):
        api_request = APIRequest('StartLogging', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name}
        return self._handle_request(api_request).result

    def create_trail(
            self,
            sls_project_arn=None,
            sls_write_role_arn=None,
            role_name=None,
            name=None,
            oss_bucket_name=None,
            oss_key_prefix=None,
            event_rw=None):
        api_request = APIRequest('CreateTrail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SlsProjectArn": sls_project_arn,
            "SlsWriteRoleArn": sls_write_role_arn,
            "RoleName": role_name,
            "Name": name,
            "OssBucketName": oss_bucket_name,
            "OssKeyPrefix": oss_key_prefix,
            "EventRW": event_rw}
        return self._handle_request(api_request).result

    def delete_trail(self, name=None):
        api_request = APIRequest('DeleteTrail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name}
        return self._handle_request(api_request).result
