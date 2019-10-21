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

import json
import time

from alibabacloud.exceptions import ClientException
from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, _create_special_resource_collection
from alibabacloud.resources.collection import _create_default_resource_collection
from alibabacloud.resources.collection import _create_sub_resource_with_page_collection
from alibabacloud.resources.collection import _create_sub_resource_without_page_collection
from alibabacloud.utils.utils import _assert_is_not_none, _new_get_key_in_response, _transfer_params


class _OOSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'oos', _client=_client)
        self.executions = _create_special_resource_collection(
            _OOSExecutionResource, _client, _client.list_executions,
            'Executions.Execution', 'ExecutionId', 
        )
        self.regions = _create_special_resource_collection(
            _OOSRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId', 
        )
        self.task_executions = _create_special_resource_collection(
            _OOSTaskExecutionResource, _client, _client.list_task_executions,
            'TaskExecutions.TaskExecution', 'TaskExecutionId', 
        )
        self.templates = _create_special_resource_collection(
            _OOSTemplateResource, _client, _client.list_templates,
            'Templates.Template', 'TemplateName', 
        )
    def create_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_template(**_params)
        template_name = _new_get_key_in_response(response, 'TemplateName')
        return _OOSTemplateResource(template_name, _client=self._client)

    def get_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_template(**_params)
        template_name = _new_get_key_in_response(response, 'TemplateName')
        return _OOSTemplateResource(template_name, _client=self._client)

    def update_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_template(**_params)
        template_name = _new_get_key_in_response(response, 'TemplateName')
        return _OOSTemplateResource(template_name, _client=self._client)

class _OOSExecutionResource(ServiceResource):

    def __init__(self, execution_id, _client=None):
        ServiceResource.__init__(self, "oos.execution", _client=_client)
        self.execution_id = execution_id
        
        self.counters = None
        self.create_date = None
        self.current_tasks = None
        self.end_date = None
        self.executed_by = None
        self.is_parent = None
        self.loop_mode = None
        self.mode = None
        self.outputs = None
        self.parameters = None
        self.parent_execution_id = None
        self.ram_role = None
        self.safety_check = None
        self.start_date = None
        self.status = None
        self.status_message = None
        self.status_reason = None
        self.template_id = None
        self.template_name = None
        self.template_version = None
        self.update_date = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_executions(execution_id=self.execution_id, **_params)

    def cancel(self, **params):
        _params = _transfer_params(params)
        return self._client.cancel_execution(execution_id=self.execution_id, **_params)

    def get_execution_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_execution_template(execution_id=self.execution_id, **_params)
        return response

    def list_execution_logs(self, **params):
        _params = _transfer_params(params)
        return self._client.list_execution_logs(execution_id=self.execution_id, **_params)

    def notify(self, **params):
        _params = _transfer_params(params)
        return self._client.notify_execution(execution_id=self.execution_id, **_params)

class _OOSRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "oos.region", _client=_client)
        self.region_id = region_id
        
        self.local_name = None
        self.region_endpoint = None

class _OOSTaskExecutionResource(ServiceResource):

    def __init__(self, task_execution_id, _client=None):
        ServiceResource.__init__(self, "oos.task_execution", _client=_client)
        self.task_execution_id = task_execution_id
        
        self.child_execution_id = None
        self.create_date = None
        self.end_date = None
        self.execution_id = None
        self.extra_data = None
        self.loop = None
        self.loop_batch_number = None
        self.loop_item = None
        self.outputs = None
        self.parent_task_execution_id = None
        self.properties = None
        self.start_date = None
        self.status = None
        self.status_message = None
        self.task_action = None
        self.task_name = None
        self.template_id = None
        self.update_date = None

class _OOSTemplateResource(ServiceResource):

    def __init__(self, template_name, _client=None):
        ServiceResource.__init__(self, "oos.template", _client=_client)
        self.template_name = template_name
        
        self.created_by = None
        self.created_date = None
        self.description = None
        self.has_trigger = None
        self.hash = None
        self.popularity = None
        self.share_type = None
        self.template_format = None
        self.template_id = None
        self.template_version = None
        self.total_execution_count = None
        self.updated_by = None
        self.updated_date = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_template(template_name=self.template_name, **_params)

    def generate_execution_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.generate_execution_policy(template_name=self.template_name, **_params)

    def list_execution_risky_tasks(self, **params):
        _params = _transfer_params(params)
        return self._client.list_execution_risky_tasks(template_name=self.template_name, **_params)

    def start_execution(self, **params):
        _params = _transfer_params(params)
        return self._client.start_execution(template_name=self.template_name, **_params)
