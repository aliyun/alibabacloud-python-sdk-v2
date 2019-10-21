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


class _FNFResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'fnf', _client=_client)
        self.executions = _create_special_resource_collection(
            _FNFExecutionResource, _client, _client.list_executions,
            'Executions.Executions', 'FlowName', 
        )
        self.flows = _create_special_resource_collection(
            _FNFFlowResource, _client, _client.list_flows,
            'Flows.Flows', 'Name', 
        )
    def create_flow(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_flow(**_params)
        name = _new_get_key_in_response(response, 'Name')
        return _FNFFlowResource(name, _client=self._client)

    def update_flow(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_flow(**_params)
        name = _new_get_key_in_response(response, 'Name')
        return _FNFFlowResource(name, _client=self._client)

class _FNFExecutionResource(ServiceResource):

    def __init__(self, flow_name, _client=None):
        ServiceResource.__init__(self, "fnf.execution", _client=_client)
        self.flow_name = flow_name
        
        self.flow_definition = None
        self.input = None
        self.name = None
        self.output = None
        self.started_time = None
        self.status = None
        self.stopped_time = None

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_execution(flow_name=self.flow_name, **_params)

    def get_execution_history(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_execution_history(flow_name=self.flow_name, **_params)
        return response

    def start(self, **params):
        _params = _transfer_params(params)
        return self._client.start_execution(flow_name=self.flow_name, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_execution(flow_name=self.flow_name, **_params)

class _FNFFlowResource(ServiceResource):

    def __init__(self, name, _client=None):
        ServiceResource.__init__(self, "fnf.flow", _client=_client)
        self.name = name
        
        self.created_time = None
        self.definition = None
        self.description = None
        self.id_ = None
        self.last_modified_time = None
        self.role_arn = None
        self.type_ = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_flow(name=self.name, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_flow(name=self.name, **_params)
