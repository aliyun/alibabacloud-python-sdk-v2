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


class OosClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'oos'
        self.api_version = '2019-06-01'
        self.location_service_code = 'oos'
        self.location_endpoint_type = 'openAPI'

    def describe_regions(self, region_id=None, accept_language=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "AcceptLanguage": accept_language}
        return self._handle_request(api_request).result

    def generate_execution_policy(self, region_id=None, template_name=None):
        api_request = APIRequest('GenerateExecutionPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "TemplateName": template_name}
        return self._handle_request(api_request).result

    def get_execution_template(self, execution_id=None, region_id=None):
        api_request = APIRequest('GetExecutionTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ExecutionId": execution_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def get_template(self, template_version=None, region_id=None, template_name=None):
        api_request = APIRequest('GetTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TemplateVersion": template_version,
            "RegionId": region_id,
            "TemplateName": template_name}
        return self._handle_request(api_request).result

    def list_actions(self, region_id=None, next_token=None, max_results=None, oos_action_name=None):
        api_request = APIRequest('ListActions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "NextToken": next_token,
            "MaxResults": max_results,
            "OOSActionName": oos_action_name}
        return self._handle_request(api_request).result

    def list_execution_logs(
            self,
            execution_id=None,
            log_type=None,
            region_id=None,
            next_token=None,
            max_results=None,
            task_execution_id=None):
        api_request = APIRequest('ListExecutionLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ExecutionId": execution_id,
            "LogType": log_type,
            "RegionId": region_id,
            "NextToken": next_token,
            "MaxResults": max_results,
            "TaskExecutionId": task_execution_id}
        return self._handle_request(api_request).result

    def list_executions(
            self,
            executed_by=None,
            include_child_execution=None,
            start_date_after=None,
            start_date_before=None,
            mode=None,
            execution_id=None,
            parent_execution_id=None,
            region_id=None,
            ram_role=None,
            next_token=None,
            end_date_after=None,
            max_results=None,
            template_name=None,
            end_date_before=None,
            sort_order=None,
            sort_field=None,
            status=None):
        api_request = APIRequest('ListExecutions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ExecutedBy": executed_by,
            "IncludeChildExecution": include_child_execution,
            "StartDateAfter": start_date_after,
            "StartDateBefore": start_date_before,
            "Mode": mode,
            "ExecutionId": execution_id,
            "ParentExecutionId": parent_execution_id,
            "RegionId": region_id,
            "RamRole": ram_role,
            "NextToken": next_token,
            "EndDateAfter": end_date_after,
            "MaxResults": max_results,
            "TemplateName": template_name,
            "EndDateBefore": end_date_before,
            "SortOrder": sort_order,
            "SortField": sort_field,
            "Status": status}
        return self._handle_request(api_request).result

    def list_task_executions(
            self,
            start_date_after=None,
            start_date_before=None,
            task_name=None,
            include_child_task_execution=None,
            execution_id=None,
            parent_task_execution_id=None,
            region_id=None,
            next_token=None,
            end_date_after=None,
            max_results=None,
            end_date_before=None,
            task_execution_id=None,
            sort_order=None,
            sort_field=None,
            task_action=None,
            status=None):
        api_request = APIRequest('ListTaskExecutions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartDateAfter": start_date_after,
            "StartDateBefore": start_date_before,
            "TaskName": task_name,
            "IncludeChildTaskExecution": include_child_task_execution,
            "ExecutionId": execution_id,
            "ParentTaskExecutionId": parent_task_execution_id,
            "RegionId": region_id,
            "NextToken": next_token,
            "EndDateAfter": end_date_after,
            "MaxResults": max_results,
            "EndDateBefore": end_date_before,
            "TaskExecutionId": task_execution_id,
            "SortOrder": sort_order,
            "SortField": sort_field,
            "TaskAction": task_action,
            "Status": status}
        return self._handle_request(api_request).result

    def list_templates(
            self,
            has_trigger=None,
            created_date_before=None,
            region_id=None,
            created_by=None,
            next_token=None,
            created_date_after=None,
            max_results=None,
            template_name=None,
            sort_order=None,
            template_format=None,
            share_type=None,
            sort_field=None):
        api_request = APIRequest('ListTemplates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HasTrigger": has_trigger,
            "CreatedDateBefore": created_date_before,
            "RegionId": region_id,
            "CreatedBy": created_by,
            "NextToken": next_token,
            "CreatedDateAfter": created_date_after,
            "MaxResults": max_results,
            "TemplateName": template_name,
            "SortOrder": sort_order,
            "TemplateFormat": template_format,
            "ShareType": share_type,
            "SortField": sort_field}
        return self._handle_request(api_request).result

    def notify_execution(
            self,
            execution_id=None,
            execution_status=None,
            region_id=None,
            notify_note=None,
            task_name=None,
            notify_type=None,
            parameters=None,
            loop_item=None):
        api_request = APIRequest('NotifyExecution', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ExecutionId": execution_id,
            "ExecutionStatus": execution_status,
            "RegionId": region_id,
            "NotifyNote": notify_note,
            "TaskName": task_name,
            "NotifyType": notify_type,
            "Parameters": parameters,
            "LoopItem": loop_item}
        return self._handle_request(api_request).result

    def start_execution(
            self,
            mode=None,
            template_version=None,
            parent_execution_id=None,
            region_id=None,
            template_name=None,
            safety_check=None,
            parameters=None,
            loop_mode=None):
        api_request = APIRequest('StartExecution', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Mode": mode,
            "TemplateVersion": template_version,
            "ParentExecutionId": parent_execution_id,
            "RegionId": region_id,
            "TemplateName": template_name,
            "SafetyCheck": safety_check,
            "Parameters": parameters,
            "LoopMode": loop_mode}
        return self._handle_request(api_request).result

    def update_template(self, region_id=None, template_name=None, content=None):
        api_request = APIRequest('UpdateTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "TemplateName": template_name,
            "Content": content}
        return self._handle_request(api_request).result

    def validate_template_content(self, region_id=None, content=None):
        api_request = APIRequest('ValidateTemplateContent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "Content": content}
        return self._handle_request(api_request).result

    def delete_executions(self, execution_ids=None, region_id=None):
        api_request = APIRequest('DeleteExecutions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ExecutionIds": execution_ids, "RegionId": region_id}
        return self._handle_request(api_request).result

    def create_template(self, region_id=None, template_name=None, content=None):
        api_request = APIRequest('CreateTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "TemplateName": template_name,
            "Content": content}
        return self._handle_request(api_request).result

    def cancel_execution(self, execution_id=None, region_id=None):
        api_request = APIRequest('CancelExecution', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ExecutionId": execution_id, "RegionId": region_id}
        return self._handle_request(api_request).result

    def delete_template(self, region_id=None, template_name=None):
        api_request = APIRequest('DeleteTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "TemplateName": template_name}
        return self._handle_request(api_request).result
