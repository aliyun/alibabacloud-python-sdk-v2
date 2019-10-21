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
from alibabacloud.resources.collection import _create_sub_resource_without_page_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _ESSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ess', _client=_client)
        self.alarms = _create_resource_collection(
            _ESSAlarmResource, _client, _client.describe_alarms,
            'AlarmList.Alarm', 'AlarmTaskId',
        )
        self.regions = _create_special_resource_collection(
            _ESSRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId',
        )
        self.scaling_activities = _create_resource_collection(
            _ESSScalingActivityResource, _client, _client.describe_scaling_activities,
            'ScalingActivities.ScalingActivity', 'ScalingActivityId',
        )
        self.scaling_configurations = _create_resource_collection(
            _ESSScalingConfigurationResource, _client, _client.describe_scaling_configurations,
            'ScalingConfigurations.ScalingConfiguration', 'ScalingConfigurationId',
        )
        self.scaling_groups = _create_resource_collection(
            _ESSScalingGroupResource, _client, _client.describe_scaling_groups,
            'ScalingGroups.ScalingGroup', 'ScalingGroupId',
        )
        self.scaling_rules = _create_resource_collection(
            _ESSScalingRuleResource, _client, _client.describe_scaling_rules,
            'ScalingRules.ScalingRule', 'ScalingRuleId',
        )
        self.scheduled_tasks = _create_resource_collection(
            _ESSScheduledTaskResource, _client, _client.describe_scheduled_tasks,
            'ScheduledTasks.ScheduledTask', 'ScheduledTaskId',
        )

    def create_alarm(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_alarm(**_params)
        alarm_task_id = _new_get_key_in_response(response, 'AlarmTaskId')
        return _ESSAlarmResource(alarm_task_id, _client=self._client)

    def delete_alarm(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_alarm(**_params)
        alarm_task_id = _new_get_key_in_response(response, 'AlarmTaskId')
        return _ESSAlarmResource(alarm_task_id, _client=self._client)

    def create_scaling_configuration(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_scaling_configuration(**_params)
        scaling_configuration_id = _new_get_key_in_response(response, 'ScalingConfigurationId')
        return _ESSScalingConfigurationResource(scaling_configuration_id, _client=self._client)

    def create_scaling_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_scaling_group(**_params)
        scaling_group_id = _new_get_key_in_response(response, 'ScalingGroupId')
        return _ESSScalingGroupResource(scaling_group_id, _client=self._client)

    def create_scaling_rule(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_scaling_rule(**_params)
        scaling_rule_id = _new_get_key_in_response(response, 'ScalingRuleId')
        return _ESSScalingRuleResource(scaling_rule_id, _client=self._client)

    def create_scheduled_task(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_scheduled_task(**_params)
        scheduled_task_id = _new_get_key_in_response(response, 'ScheduledTaskId')
        return _ESSScheduledTaskResource(scheduled_task_id, _client=self._client)


class _ESSAlarmResource(ServiceResource):

    def __init__(self, alarm_task_id, _client=None):
        ServiceResource.__init__(self, "ess.alarm", _client=_client)
        self.alarm_task_id = alarm_task_id

        self.alarm_actions = None
        self.comparison_operator = None
        self.description = None
        self.dimensions = None
        self.enable = None
        self.evaluation_count = None
        self.metric_name = None
        self.metric_type = None
        self.name = None
        self.period = None
        self.scaling_group_id = None
        self.state = None
        self.statistics = None
        self.threshold = None

    def disable(self, **params):
        _params = _transfer_params(params)
        return self._client.disable_alarm(alarm_task_id=self.alarm_task_id, **_params)

    def enable(self, **params):
        _params = _transfer_params(params)
        return self._client.enable_alarm(alarm_task_id=self.alarm_task_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_alarm(alarm_task_id=self.alarm_task_id, **_params)


class _ESSRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "ess.region", _client=_client)
        self.region_id = region_id

        self.classic_unavailable = None
        self.local_name = None
        self.region_endpoint = None
        self.vpc_unavailable = None


class _ESSScalingActivityResource(ServiceResource):

    def __init__(self, scaling_activity_id, _client=None):
        ServiceResource.__init__(self, "ess.scaling_activity", _client=_client)
        self.scaling_activity_id = scaling_activity_id

        self.attached_capacity = None
        self.auto_created_capacity = None
        self.cause = None
        self.description = None
        self.end_time = None
        self.progress = None
        self.scaling_group_id = None
        self.scaling_instance_number = None
        self.start_time = None
        self.status_code = None
        self.status_message = None
        self.total_capacity = None


class _ESSScalingConfigurationResource(ServiceResource):

    def __init__(self, scaling_configuration_id, _client=None):
        ServiceResource.__init__(self, "ess.scaling_configuration", _client=_client)
        self.scaling_configuration_id = scaling_configuration_id

        self.cpu = None
        self.creation_time = None
        self.data_disks = None
        self.deployment_set_id = None
        self.host_name = None
        self.hpc_cluster_id = None
        self.image_id = None
        self.image_name = None
        self.instance_description = None
        self.instance_generation = None
        self.instance_name = None
        self.instance_type = None
        self.instance_types = None
        self.internet_charge_type = None
        self.internet_max_bandwidth_in = None
        self.internet_max_bandwidth_out = None
        self.io_optimized = None
        self.key_pair_name = None
        self.lifecycle_state = None
        self.load_balancer_weight = None
        self.memory = None
        self.password_inherit = None
        self.ram_role_name = None
        self.resource_group_id = None
        self.scaling_configuration_name = None
        self.scaling_group_id = None
        self.security_enhancement_strategy = None
        self.security_group_id = None
        self.security_group_ids = None
        self.spot_price_limit = None
        self.spot_strategy = None
        self.system_disk_category = None
        self.system_disk_description = None
        self.system_disk_name = None
        self.system_disk_size = None
        self.tags = None
        self.user_data = None

    def deactivate(self, **params):
        _params = _transfer_params(params)
        return self._client.deactivate_scaling_configuration(
            scaling_configuration_id=self.scaling_configuration_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_scaling_configuration(
            scaling_configuration_id=self.scaling_configuration_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_scaling_configuration(
            scaling_configuration_id=self.scaling_configuration_id, **_params)


class _ESSScalingGroupResource(ServiceResource):

    def __init__(self, scaling_group_id, _client=None):
        ServiceResource.__init__(self, "ess.scaling_group", _client=_client)
        self.scaling_group_id = scaling_group_id

        self.active_capacity = None
        self.active_scaling_configuration_id = None
        self.creation_time = None
        self.db_instance_ids = None
        self.default_cooldown = None
        self.health_check_type = None
        self.launch_template_id = None
        self.launch_template_version = None
        self.lifecycle_state = None
        self.load_balancer_ids = None
        self.max_size = None
        self.min_size = None
        self.modification_time = None
        self.multi_az_policy = None
        self.on_demand_base_capacity = None
        self.on_demand_percentage_above_base_capacity = None
        self.pending_capacity = None
        self.pending_wait_capacity = None
        self.protected_capacity = None
        self.region_id = None
        self.removal_policies = None
        self.removing_capacity = None
        self.removing_wait_capacity = None
        self.scaling_group_name = None
        self.scaling_policy = None
        self.spot_instance_pools = None
        self.spot_instance_remedy = None
        self.standby_capacity = None
        self.stopped_capacity = None
        self.total_capacity = None
        self.vserver_groups = None
        self.vswitch_id = None
        self.vswitch_ids = None
        self.vpc_id = None

        self.lifecycle_hooks = _create_sub_resource_without_page_collection(
            _ESSLifecycleHookResource, _client, _client.describe_lifecycle_hooks,
            'LifecycleHooks.LifecycleHook', 'LifecycleHookId', parent_identifier="ScalingGroupId",
            parent_identifier_value=self.scaling_group_id
        )

    def attach_db_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.attach_db_instances(scaling_group_id=self.scaling_group_id, **_params)

    def attach_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.attach_instances(scaling_group_id=self.scaling_group_id, **_params)

    def attach_load_balancers(self, **params):
        _params = _transfer_params(params)
        return self._client.attach_load_balancers(scaling_group_id=self.scaling_group_id, **_params)

    def attach_vserver_groups(self, **params):
        _params = _transfer_params(params)
        return self._client.attach_vserver_groups(scaling_group_id=self.scaling_group_id, **_params)

    def create_notification_configuration(self, **params):
        _params = _transfer_params(params)
        return self._client.create_notification_configuration(
            scaling_group_id=self.scaling_group_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_scaling_group(scaling_group_id=self.scaling_group_id, **_params)

    def delete_notification_configuration(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_notification_configuration(
            scaling_group_id=self.scaling_group_id, **_params)

    def describe_alert_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_alert_config(scaling_group_id=self.scaling_group_id, **_params)

    def describe_capacity_history(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_capacity_history(scaling_group_id=self.scaling_group_id,
                                                      **_params)

    def describe_notification_configurations(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_notification_configurations(
            scaling_group_id=self.scaling_group_id, **_params)

    def detach_db_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.detach_db_instances(scaling_group_id=self.scaling_group_id, **_params)

    def detach_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.detach_instances(scaling_group_id=self.scaling_group_id, **_params)

    def detach_load_balancers(self, **params):
        _params = _transfer_params(params)
        return self._client.detach_load_balancers(scaling_group_id=self.scaling_group_id, **_params)

    def detach_vserver_groups(self, **params):
        _params = _transfer_params(params)
        return self._client.detach_vserver_groups(scaling_group_id=self.scaling_group_id, **_params)

    def disable(self, **params):
        _params = _transfer_params(params)
        return self._client.disable_scaling_group(scaling_group_id=self.scaling_group_id, **_params)

    def enable(self, **params):
        _params = _transfer_params(params)
        return self._client.enable_scaling_group(scaling_group_id=self.scaling_group_id, **_params)

    def enter_standby(self, **params):
        _params = _transfer_params(params)
        return self._client.enter_standby(scaling_group_id=self.scaling_group_id, **_params)

    def exit_standby(self, **params):
        _params = _transfer_params(params)
        return self._client.exit_standby(scaling_group_id=self.scaling_group_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_scaling_group(scaling_group_id=self.scaling_group_id, **_params)

    def modify_alert_config(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_alert_config(scaling_group_id=self.scaling_group_id, **_params)

    def modify_notification_configuration(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_notification_configuration(
            scaling_group_id=self.scaling_group_id, **_params)

    def rebalance_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.rebalance_instances(scaling_group_id=self.scaling_group_id, **_params)

    def remove_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_instances(scaling_group_id=self.scaling_group_id, **_params)

    def set_instances_protection(self, **params):
        _params = _transfer_params(params)
        return self._client.set_instances_protection(scaling_group_id=self.scaling_group_id,
                                                     **_params)

    def create_lifecycle_hook(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_lifecycle_hook(scaling_group_id=self.scaling_group_id,
                                                      **_params)
        lifecycle_hook_id = _new_get_key_in_response(response, 'LifecycleHookId')
        return _ESSLifecycleHookResource(lifecycle_hook_id, self.scaling_group_id,
                                         _client=self._client)


class _ESSLifecycleHookResource(ServiceResource):

    def __init__(self, lifecycle_hook_id, scaling_group_id, _client=None):
        ServiceResource.__init__(self, "ess.lifecycle_hook", _client=_client)
        self.lifecycle_hook_id = lifecycle_hook_id
        self.scaling_group_id = scaling_group_id
        self.default_result = None
        self.heartbeat_timeout = None
        self.lifecycle_hook_name = None
        self.lifecycle_transition = None
        self.notification_arn = None
        self.notification_metadata = None

    def complete_lifecycle_action(self, **params):
        _params = _transfer_params(params)
        return self._client.complete_lifecycle_action(lifecycle_hook_id=self.lifecycle_hook_id,
                                                      scaling_group_id=self.scaling_group_id,
                                                      **_params)

    def record_lifecycle_action_heartbeat(self, **params):
        _params = _transfer_params(params)
        return self._client.record_lifecycle_action_heartbeat(
            lifecycle_hook_id=self.lifecycle_hook_id, scaling_group_id=self.scaling_group_id,
            **_params)


class _ESSScalingRuleResource(ServiceResource):

    def __init__(self, scaling_rule_id, _client=None):
        ServiceResource.__init__(self, "ess.scaling_rule", _client=_client)
        self.scaling_rule_id = scaling_rule_id

        self.adjustment_type = None
        self.adjustment_value = None
        self.alarms = None
        self.cooldown = None
        self.disable_scale_in = None
        self.estimated_instance_warmup = None
        self.initial_max_size = None
        self.max_size = None
        self.metric_name = None
        self.min_adjustment_magnitude = None
        self.min_size = None
        self.predictive_scaling_mode = None
        self.predictive_task_buffer_time = None
        self.predictive_value_behavior = None
        self.predictive_value_buffer = None
        self.scaling_group_id = None
        self.scaling_rule_ari = None
        self.scaling_rule_name = None
        self.scaling_rule_type = None
        self.step_adjustments = None
        self.target_value = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_scaling_rule(scaling_rule_id=self.scaling_rule_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_scaling_rule(scaling_rule_id=self.scaling_rule_id, **_params)


class _ESSScheduledTaskResource(ServiceResource):

    def __init__(self, scheduled_task_id, _client=None):
        ServiceResource.__init__(self, "ess.scheduled_task", _client=_client)
        self.scheduled_task_id = scheduled_task_id

        self.description = None
        self.launch_expiration_time = None
        self.launch_time = None
        self.max_value = None
        self.min_value = None
        self.recurrence_end_time = None
        self.recurrence_type = None
        self.recurrence_value = None
        self.scheduled_action = None
        self.scheduled_task_name = None
        self.task_enabled = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_scheduled_task(scheduled_task_id=self.scheduled_task_id,
                                                  **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_scheduled_task(scheduled_task_id=self.scheduled_task_id,
                                                  **_params)
