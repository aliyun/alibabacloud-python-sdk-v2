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
from alibabacloud.resources.collection import _create_special_resource_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _CMSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'cms', _client=_client)
        self.monitor_groups = _create_special_resource_collection(
            _CMSMonitorGroupResource, _client, _client.describe_monitor_groups,
            'Resources.Resource', 'GroupId',
        )
        self.monitoring_agent_processes = _create_special_resource_collection(
            _CMSMonitoringAgentProcessResource, _client,
            _client.describe_monitoring_agent_processes,
            'NodeProcesses.NodeProcess', 'MonitoringAgentProcessName',
        )

    def delete_metric_rule_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_metric_rule_template(**_params)
        template_id = _new_get_key_in_response(response, 'TemplateId')
        return _CMSMetricRuleTemplateResource(template_id, _client=self._client)

    def create_monitor_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_monitor_group(**_params)
        group_id = _new_get_key_in_response(response, 'GroupId')
        return _CMSMonitorGroupResource(group_id, _client=self._client)

    def create_monitoring_agent_process(self, **params):
        _params = _transfer_params(params)
        self._client.create_monitoring_agent_process(**_params)
        monitoring_agent_process_name = _params.get("monitoring_agent_process_name")
        return _CMSMonitoringAgentProcessResource(monitoring_agent_process_name,
                                                  _client=self._client)


class _CMSMetricRuleTemplateResource(ServiceResource):

    def __init__(self, template_id, _client=None):
        ServiceResource.__init__(self, "cms.metric_rule_template", _client=_client)
        self.template_id = template_id

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_metric_rule_template(template_id=self.template_id, **_params)


class _CMSMonitorGroupResource(ServiceResource):

    def __init__(self, group_id, _client=None):
        ServiceResource.__init__(self, "cms.monitor_group", _client=_client)
        self.group_id = group_id

        self.bind_url = None
        self.contact_groups = None
        self.gmt_create = None
        self.gmt_modified = None
        self.group_name = None
        self.service_id = None
        self.type_ = None

    def apply_metric_rule_template(self, **params):
        _params = _transfer_params(params)
        return self._client.apply_metric_rule_template(group_id=self.group_id, **_params)

    def create_group_metric_rules(self, **params):
        _params = _transfer_params(params)
        return self._client.create_group_metric_rules(group_id=self.group_id, **_params)

    def create_host_availability(self, **params):
        _params = _transfer_params(params)
        return self._client.create_host_availability(group_id=self.group_id, **_params)

    def create_monitor_group_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.create_monitor_group_instances(group_id=self.group_id, **_params)

    def create_monitor_group_notify_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.create_monitor_group_notify_policy(group_id=self.group_id, **_params)

    def delete_custom_metric(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_custom_metric(group_id=self.group_id, **_params)

    def delete_monitor_group_dynamic_rule(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_monitor_group_dynamic_rule(group_id=self.group_id, **_params)

    def delete_monitor_group_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_monitor_group_instances(group_id=self.group_id, **_params)

    def describe_custom_metric_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_custom_metric_list(group_id=self.group_id, **_params)

    def describe_monitor_group_categories(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_monitor_group_categories(group_id=self.group_id, **_params)

    def describe_monitor_group_dynamic_rules(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_monitor_group_dynamic_rules(group_id=self.group_id, **_params)

    def describe_monitor_group_instance_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_monitor_group_instance_attribute(group_id=self.group_id,
                                                                      **_params)

    def describe_monitor_group_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_monitor_group_instances(group_id=self.group_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_monitor_group(group_id=self.group_id, **_params)

    def modify_host_availability(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_host_availability(group_id=self.group_id, **_params)

    def modify_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_monitor_group_instances(group_id=self.group_id, **_params)

    def put_group_metric_rule(self, **params):
        _params = _transfer_params(params)
        return self._client.put_group_metric_rule(group_id=self.group_id, **_params)

    def put_monitor_group_dynamic_rule(self, **params):
        _params = _transfer_params(params)
        return self._client.put_monitor_group_dynamic_rule(group_id=self.group_id, **_params)


class _CMSMonitoringAgentProcessResource(ServiceResource):

    def __init__(self, monitoring_agent_process_name, _client=None):
        ServiceResource.__init__(self, "cms.monitoring_agent_process", _client=_client)
        self.monitoring_agent_process_name = monitoring_agent_process_name

        self.command = None
        self.instance_id = None
        self.process_id = None
        self.process_name = None
        self.process_user = None

    def install_monitoring_agent(self, **params):
        _params = _transfer_params(params)
        return self._client.install_monitoring_agent(
            monitoring_agent_process_name=self.monitoring_agent_process_name, **_params)

    def create_monitor_agent_process(self, **params):
        _params = _transfer_params(params)
        return self._client.create_monitor_agent_process(
            monitoring_agent_process_name=self.monitoring_agent_process_name, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_monitoring_agent_process(
            monitoring_agent_process_name=self.monitoring_agent_process_name, **_params)

    def uninstall_monitoring_agent(self, **params):
        _params = _transfer_params(params)
        return self._client.uninstall_monitoring_agent(
            monitoring_agent_process_name=self.monitoring_agent_process_name, **_params)
