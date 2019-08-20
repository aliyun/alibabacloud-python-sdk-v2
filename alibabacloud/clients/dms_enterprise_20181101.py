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


class DmsenterpriseClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'dms-enterprise'
        self.api_version = '2018-11-01'
        self.location_service_code = 'dmsenterprise'
        self.location_endpoint_type = 'openAPI'

    def disable_user(self, uid=None, tid=None):
        api_request = APIRequest('DisableUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Uid": uid, "Tid": tid}
        return self._handle_request(api_request).result

    def enable_user(self, uid=None, tid=None):
        api_request = APIRequest('EnableUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Uid": uid, "Tid": tid}
        return self._handle_request(api_request).result

    def delete_user(self, uid=None, tid=None):
        api_request = APIRequest('DeleteUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Uid": uid, "Tid": tid}
        return self._handle_request(api_request).result

    def get_op_log(
            self,
            module=None,
            page_size=None,
            end_time=None,
            start_time=None,
            tid=None,
            page_number=None):
        api_request = APIRequest('GetOpLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Module": module,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "Tid": tid,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def register_user(self, role_names=None, uid=None, user_nick=None, tid=None):
        api_request = APIRequest('RegisterUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RoleNames": role_names,
            "Uid": uid,
            "UserNick": user_nick,
            "Tid": tid}
        return self._handle_request(api_request).result

    def register_instance(
            self,
            ecs_instance_id=None,
            ecs_region=None,
            export_timeout=None,
            database_password=None,
            instance_alias=None,
            network_type=None,
            tid=None,
            sid=None,
            database_user=None,
            port=None,
            vpc_id=None,
            instance_source=None,
            env_type=None,
            host=None,
            instance_type=None,
            query_timeout=None,
            dba_uid=None,
            safe_rule=None):
        api_request = APIRequest('RegisterInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EcsInstanceId": ecs_instance_id,
            "EcsRegion": ecs_region,
            "ExportTimeout": export_timeout,
            "DatabasePassword": database_password,
            "InstanceAlias": instance_alias,
            "NetworkType": network_type,
            "Tid": tid,
            "Sid": sid,
            "DatabaseUser": database_user,
            "Port": port,
            "VpcId": vpc_id,
            "InstanceSource": instance_source,
            "EnvType": env_type,
            "Host": host,
            "InstanceType": instance_type,
            "QueryTimeout": query_timeout,
            "DbaUid": dba_uid,
            "SafeRule": safe_rule}
        return self._handle_request(api_request).result
