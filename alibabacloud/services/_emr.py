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

from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, \
    _create_special_resource_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _EMRResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'emr', _client=_client)
        self.flow_instances = _create_special_resource_collection(
            _EMRFlowInstanceResource, _client, _client.describe_flow_instance,
            'DependencyFlowList.ParentFlow', 'FlowInstanceId',
        )
        self.host_pools = _create_resource_collection(
            _EMRHostPoolResource, _client, _client.list_host_pool,
            'HostPoolList.HostPool', 'BizId',
        )

    def create_host_pool(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_host_pool(**_params)
        biz_id = _new_get_key_in_response(response, 'BizId')
        return _EMRHostPoolResource(biz_id, _client=self._client)


class _EMRFlowInstanceResource(ServiceResource):

    def __init__(self, flow_instance_id, _client=None):
        ServiceResource.__init__(self, "emr.flow_instance", _client=_client)
        self.flow_instance_id = flow_instance_id

        self.biz_date = None
        self.dependency_flow_id = None
        self.dependency_instance_id = None
        self.flow_id = None
        self.project_id = None
        self.schedule_key = None

    def kill_flow(self, **params):
        _params = _transfer_params(params)
        return self._client.kill_flow(flow_instance_id=self.flow_instance_id, **_params)

    def rerun_flow(self, **params):
        _params = _transfer_params(params)
        return self._client.rerun_flow(flow_instance_id=self.flow_instance_id, **_params)

    def resume_flow(self, **params):
        _params = _transfer_params(params)
        return self._client.resume_flow(flow_instance_id=self.flow_instance_id, **_params)

    def start_flow(self, **params):
        _params = _transfer_params(params)
        return self._client.start_flow(flow_instance_id=self.flow_instance_id, **_params)

    def suspend_flow(self, **params):
        _params = _transfer_params(params)
        return self._client.suspend_flow(flow_instance_id=self.flow_instance_id, **_params)


class _EMRHostPoolResource(ServiceResource):

    def __init__(self, biz_id, _client=None):
        ServiceResource.__init__(self, "emr.host_pool", _client=_client)
        self.biz_id = biz_id

        self.description = None
        self.gmt_create = None
        self.host_count = None
        self.name = None
        self.status = None
        self.type_ = None

    def delete_cluster_template(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_cluster_template(biz_id=self.biz_id, **_params)

    def describe_cluster_template(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cluster_template(biz_id=self.biz_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_host_pool(biz_id=self.biz_id, **_params)

    def modify_alert_contact(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_alert_contact(biz_id=self.biz_id, **_params)

    def modify_alert_ding_ding_group(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_alert_ding_ding_group(biz_id=self.biz_id, **_params)

    def modify_alert_user_group(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_alert_user_group(biz_id=self.biz_id, **_params)

    def modify_cluster_template(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_cluster_template(biz_id=self.biz_id, **_params)


class _EMRScalingRuleResource(ServiceResource):

    def __init__(self, scaling_rule_id, _client=None):
        ServiceResource.__init__(self, "emr.scaling_rule", _client=_client)
        self.scaling_rule_id = scaling_rule_id

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_scaling_rule(scaling_rule_id=self.scaling_rule_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scaling_rule(scaling_rule_id=self.scaling_rule_id, **_params)
