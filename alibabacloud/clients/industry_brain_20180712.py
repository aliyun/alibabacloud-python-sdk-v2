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


class IndustrybrainClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'industry-brain'
        self.api_version = '2018-07-12'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def get_image_detail(self, user_code=None, service_id=None):
        api_request = APIRequest('GetImageDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UserCode": user_code, "ServiceId": service_id}
        return self._handle_request(api_request).result

    def get_data_set_info(self, user_code=None, service_id=None):
        api_request = APIRequest('GetDataSetInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"UserCode": user_code, "ServiceId": service_id}
        return self._handle_request(api_request).result

    def async_response_post(
            self,
            data=None,
            context=None,
            progress=None,
            message=None,
            task_id=None,
            status=None):
        api_request = APIRequest('AsyncResponsePost', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "Data": data,
            "Context": context,
            "Progress": progress,
            "Message": message,
            "TaskId": task_id,
            "Status": status}
        return self._handle_request(api_request).result

    def get_data_properties(self, service_id=None):
        api_request = APIRequest('GetDataProperties', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ServiceId": service_id}
        return self._handle_request(api_request).result

    def post_real_time_device_data(self, data=None, service_id=None):
        api_request = APIRequest('PostRealTimeDeviceData', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"Data": data, "ServiceId": service_id}
        return self._handle_request(api_request).result

    def operate_equipment(self, operation=None, project_id=None, request_data=None):
        api_request = APIRequest('OperateEquipment', 'POST', 'https', 'RPC', 'body')
        api_request._params = {
            "Operation": operation,
            "ProjectId": project_id,
            "RequestData": request_data}
        return self._handle_request(api_request).result

    def get_industry_info_list(self,):
        api_request = APIRequest('GetIndustryInfoList', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def get_industry_info_lineage_list(self, industry_code=None):
        api_request = APIRequest('GetIndustryInfoLineageList', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"IndustryCode": industry_code}
        return self._handle_request(api_request).result

    def get_industry_info_children_list(self, industry_code=None):
        api_request = APIRequest('GetIndustryInfoChildrenList', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"IndustryCode": industry_code}
        return self._handle_request(api_request).result

    def get_industry_info(self, industry_code=None):
        api_request = APIRequest('GetIndustryInfo', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"IndustryCode": industry_code}
        return self._handle_request(api_request).result

    def invoke_service(
            self,
            request_params=None,
            show_biz_info=None,
            service_id=None,
            request_data=None,
            show_params=None):
        api_request = APIRequest('InvokeService', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "RequestParams": request_params,
            "ShowBizInfo": show_biz_info,
            "ServiceId": service_id,
            "RequestData": request_data,
            "ShowParams": show_params}
        return self._handle_request(api_request).result

    def get_service_input_mapping(
            self,
            show_latest_data=None,
            limit=None,
            service_id=None,
            algorithm_id=None):
        api_request = APIRequest('GetServiceInputMapping', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ShowLatestData": show_latest_data,
            "Limit": limit,
            "ServiceId": service_id,
            "AlgorithmId": algorithm_id}
        return self._handle_request(api_request).result

    def get_algorithm_list(self, service_id=None):
        api_request = APIRequest('GetAlgorithmList', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"ServiceId": service_id}
        return self._handle_request(api_request).result

    def get_oss_image_access(self, user_code=None, project_id=None):
        api_request = APIRequest('GetOSSImageAccess', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserCode": user_code, "ProjectId": project_id}
        return self._handle_request(api_request).result

    def get_async_service_result(self, task_id=None):
        api_request = APIRequest('GetAsyncServiceResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TaskId": task_id}
        return self._handle_request(api_request).result

    def get_service_result_async(self, task_id=None):
        api_request = APIRequest('GetServiceResultAsync', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TaskId": task_id}
        return self._handle_request(api_request).result

    def invoke_service_async(
            self,
            is_show_input=None,
            service_id=None,
            params=None,
            request_data=None):
        api_request = APIRequest('InvokeServiceAsync', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "IsShowInput": is_show_input,
            "ServiceId": service_id,
            "Params": params,
            "RequestData": request_data}
        return self._handle_request(api_request).result

    def get_online_service_result(self, service_id=None):
        api_request = APIRequest('GetOnlineServiceResult', 'POST', 'https', 'RPC', 'query')
        api_request._params = {"ServiceId": service_id}
        return self._handle_request(api_request).result
