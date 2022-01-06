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


class _IOTResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'iot', _client=_client)
        self.devices = _create_special_resource_collection(
            _IOTDeviceResource, _client, _client.query_device,
            'Data.DeviceInfo', 'DeviceName',
        )

    def register_device(self, **params):
        _params = _transfer_params(params)
        response = self._client.register_device(**_params)
        device_name = _new_get_key_in_response(response, 'DeviceName')
        return _IOTDeviceResource(device_name, _client=self._client)

    def query_device_file(self, **params):
        _params = _transfer_params(params)
        response = self._client.query_device_file(**_params)
        file_id = _new_get_key_in_response(response, 'FileId')
        return _IOTDeviceFileResource(file_id, _client=self._client)

    def create_device_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_device_group(**_params)
        group_id = _new_get_key_in_response(response, 'GroupId')
        return _IOTDeviceGroupResource(group_id, _client=self._client)

    def create_edge_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_edge_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _IOTEdgeInstanceResource(instance_id, _client=self._client)

    def get_edge_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_edge_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _IOTEdgeInstanceResource(instance_id, _client=self._client)

    def create_lo_ra_nodes_task(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_lo_ra_nodes_task(**_params)
        task_id = _new_get_key_in_response(response, 'TaskId')
        return _IOTLoRaNodesTaskResource(task_id, _client=self._client)

    def create_product(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_product(**_params)
        product_name = _new_get_key_in_response(response, 'ProductName')
        return _IOTProductResource(product_name, _client=self._client)

    def query_product(self, **params):
        _params = _transfer_params(params)
        response = self._client.query_product(**_params)
        product_name = _new_get_key_in_response(response, 'ProductName')
        return _IOTProductResource(product_name, _client=self._client)

    def create_product_topic(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_product_topic(**_params)
        topic_id = _new_get_key_in_response(response, 'TopicId')
        return _IOTProductTopicResource(topic_id, _client=self._client)

    def create_rule(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_rule(**_params)
        rule_id = _new_get_key_in_response(response, 'RuleId')
        return _IOTRuleResource(rule_id, _client=self._client)

    def create_rule_action(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_rule_action(**_params)
        action_id = _new_get_key_in_response(response, 'ActionId')
        return _IOTRuleActionResource(action_id, _client=self._client)


class _IOTDeviceResource(ServiceResource):

    def __init__(self, device_name, _client=None):
        ServiceResource.__init__(self, "iot.device", _client=_client)
        self.device_name = device_name

        self.device_id = None
        self.device_secret = None
        self.device_status = None
        self.device_type = None
        self.gmt_create = None
        self.gmt_modified = None
        self.iot_id = None
        self.nickname = None
        self.product_key = None
        self.utc_create = None
        self.utc_modified = None

    def invoke_things_service(self, **params):
        _params = _transfer_params(params)
        return self._client.invoke_things_service(device_name=self.device_name, **_params)

    def set_devices_property(self, **params):
        _params = _transfer_params(params)
        return self._client.set_devices_property(device_name=self.device_name, **_params)

    def get_device_shadow(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_device_shadow(device_name=self.device_name, **_params)
        return response

    def query_device_group_by(self, **params):
        _params = _transfer_params(params)
        return self._client.query_device_group_by_device(device_name=self.device_name, **_params)

    def query_device_properties_data(self, **params):
        _params = _transfer_params(params)
        return self._client.query_device_properties_data(device_name=self.device_name, **_params)

    def rrpc(self, **params):
        _params = _transfer_params(params)
        return self._client.rrpc(device_name=self.device_name, **_params)

    def update_device_shadow(self, **params):
        _params = _transfer_params(params)
        return self._client.update_device_shadow(device_name=self.device_name, **_params)


class _IOTDeviceFileResource(ServiceResource):

    def __init__(self, file_id, _client=None):
        ServiceResource.__init__(self, "iot.device_file", _client=_client)
        self.file_id = file_id

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_device_file(file_id=self.file_id, **_params)


class _IOTDeviceGroupResource(ServiceResource):

    def __init__(self, group_id, _client=None):
        ServiceResource.__init__(self, "iot.device_group", _client=_client)
        self.group_id = group_id

    def batch_add_device_group_relations(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_add_device_group_relations(group_id=self.group_id, **_params)

    def batch_delete_device_group_relations(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_delete_device_group_relations(group_id=self.group_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_device_group(group_id=self.group_id, **_params)

    def query_device_group_info(self, **params):
        _params = _transfer_params(params)
        return self._client.query_device_group_info(group_id=self.group_id, **_params)

    def query_device_group_tag_list(self, **params):
        _params = _transfer_params(params)
        return self._client.query_device_group_tag_list(group_id=self.group_id, **_params)

    def query_device_list_by(self, **params):
        _params = _transfer_params(params)
        return self._client.query_device_list_by_device_group(group_id=self.group_id, **_params)

    def query_super(self, **params):
        _params = _transfer_params(params)
        return self._client.query_super_device_group(group_id=self.group_id, **_params)

    def set_device_group_tags(self, **params):
        _params = _transfer_params(params)
        return self._client.set_device_group_tags(group_id=self.group_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_device_group(group_id=self.group_id, **_params)


class _IOTEdgeInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "iot.edge_instance", _client=_client)
        self.instance_id = instance_id

    def batch_clear_edge_instance_device_config(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_clear_edge_instance_device_config(instance_id=self.instance_id,
                                                                    **_params)

    def batch_get_edge_instance_device_config(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_get_edge_instance_device_config(instance_id=self.instance_id,
                                                                  **_params)

    def batch_set_edge_instance_device_config(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_set_edge_instance_device_config(instance_id=self.instance_id,
                                                                  **_params)

    def batch_unbind_device_from(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_unbind_device_from_edge_instance(instance_id=self.instance_id,
                                                                   **_params)

    def batch_get_device_driver(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_get_device_driver(instance_id=self.instance_id, **_params)

    def batch_get_edge_instance_driver_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_get_edge_instance_driver_configs(instance_id=self.instance_id,
                                                                   **_params)

    def bind_gateway_to(self, **params):
        _params = _transfer_params(params)
        return self._client.bind_gateway_to_edge_instance(instance_id=self.instance_id, **_params)

    def close_edge_instance_deployment(self, **params):
        _params = _transfer_params(params)
        return self._client.close_edge_instance_deployment(instance_id=self.instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_edge_instance(instance_id=self.instance_id, **_params)

    def query_device_by_driver(self, **params):
        _params = _transfer_params(params)
        return self._client.query_device_by_driver(instance_id=self.instance_id, **_params)

    def query_edge_instance_device(self, **params):
        _params = _transfer_params(params)
        return self._client.query_edge_instance_device(instance_id=self.instance_id, **_params)

    def query_edge_instance_driver(self, **params):
        _params = _transfer_params(params)
        return self._client.query_edge_instance_driver(instance_id=self.instance_id, **_params)

    def query_edge_instance_gateway(self, **params):
        _params = _transfer_params(params)
        return self._client.query_edge_instance_gateway(instance_id=self.instance_id, **_params)

    def query_edge_instance_historic_deployment(self, **params):
        _params = _transfer_params(params)
        return self._client.query_edge_instance_historic_deployment(instance_id=self.instance_id,
                                                                    **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_edge_instance(instance_id=self.instance_id, **_params)

    def batch_bind_device_to_edge_instance_with_driver(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_bind_device_to_edge_instance_with_driver(
            instance_id=self.instance_id, **_params)

    def bind_driver_to(self, **params):
        _params = _transfer_params(params)
        return self._client.bind_driver_to_edge_instance(instance_id=self.instance_id, **_params)

    def clear_edge_instance_driver_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.clear_edge_instance_driver_configs(instance_id=self.instance_id,
                                                               **_params)

    def set_edge_instance_driver_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.set_edge_instance_driver_configs(instance_id=self.instance_id,
                                                             **_params)

    def unbind_driver_from(self, **params):
        _params = _transfer_params(params)
        return self._client.unbind_driver_from_edge_instance(instance_id=self.instance_id,
                                                             **_params)

    def create_edge_instance_deployment(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_edge_instance_deployment(instance_id=self.instance_id,
                                                                **_params)
        deployment_id = _new_get_key_in_response(response, 'DeploymentId')
        return _IOTEdgeInstanceDeploymentResource(deployment_id, self.instance_id,
                                                  _client=self._client)

    def get_edge_instance_deployment(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_edge_instance_deployment(instance_id=self.instance_id,
                                                             **_params)
        deployment_id = _new_get_key_in_response(response, 'DeploymentId')
        return _IOTEdgeInstanceDeploymentResource(deployment_id, self.instance_id,
                                                  _client=self._client)


class _IOTEdgeInstanceDeploymentResource(ServiceResource):

    def __init__(self, deployment_id, instance_id, _client=None):
        ServiceResource.__init__(self, "iot.edge_instance_deployment", _client=_client)
        self.deployment_id = deployment_id
        self.instance_id = instance_id


class _IOTLoRaNodesTaskResource(ServiceResource):

    def __init__(self, task_id, _client=None):
        ServiceResource.__init__(self, "iot.lo_ra_nodes_task", _client=_client)
        self.task_id = task_id

    def get_lora_nodes_task(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_lora_nodes_task(task_id=self.task_id, **_params)
        return response

    def get_nodes_adding_task(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_nodes_adding_task(task_id=self.task_id, **_params)
        return response


class _IOTProductResource(ServiceResource):

    def __init__(self, product_name, _client=None):
        ServiceResource.__init__(self, "iot.product", _client=_client)
        self.product_name = product_name

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_product(product_name=self.product_name, **_params)


class _IOTProductTopicResource(ServiceResource):

    def __init__(self, topic_id, _client=None):
        ServiceResource.__init__(self, "iot.product_topic", _client=_client)
        self.topic_id = topic_id

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_product_topic(topic_id=self.topic_id, **_params)


class _IOTRuleResource(ServiceResource):

    def __init__(self, rule_id, _client=None):
        ServiceResource.__init__(self, "iot.rule", _client=_client)
        self.rule_id = rule_id

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_rule(rule_id=self.rule_id, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_rule(rule_id=self.rule_id, **_params)

    def list_rule_actions(self, **params):
        _params = _transfer_params(params)
        return self._client.list_rule_actions(rule_id=self.rule_id, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        return self._client.start_rule(rule_id=self.rule_id, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_rule(rule_id=self.rule_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_rule(rule_id=self.rule_id, **_params)


class _IOTRuleActionResource(ServiceResource):

    def __init__(self, action_id, _client=None):
        ServiceResource.__init__(self, "iot.rule_action", _client=_client)
        self.action_id = action_id

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_rule_action(action_id=self.action_id, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_rule_action(action_id=self.action_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_rule_action(action_id=self.action_id, **_params)
