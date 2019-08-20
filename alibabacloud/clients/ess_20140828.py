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


class EssClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Ess'
        self.api_version = '2014-08-28'
        self.location_service_code = 'ess'
        self.location_endpoint_type = 'openAPI'

    def detach_vserver_groups(
            self,
            resource_owner_account=None,
            region_id=None,
            scaling_group_id=None,
            force_detach=None,
            owner_id=None,
            list_of_vserver_group=None):
        api_request = APIRequest('DetachVServerGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ScalingGroupId": scaling_group_id,
            "ForceDetach": force_detach,
            "OwnerId": owner_id,
            "VServerGroup": list_of_vserver_group}
        repeat_info = {
            "VServerGroup": (
                'VServerGroup', 'list', 'dict', [
                    ('LoadBalancerId', 'str', None, None), ('VServerGroupAttribute', 'list', 'dict', [
                        ('VServerGroupId', 'str', None, None), ('Port', 'str', None, None), ],),]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def attach_vserver_groups(
            self,
            resource_owner_account=None,
            region_id=None,
            scaling_group_id=None,
            force_attach=None,
            owner_id=None,
            list_of_vserver_group=None):
        api_request = APIRequest('AttachVServerGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ScalingGroupId": scaling_group_id,
            "ForceAttach": force_attach,
            "OwnerId": owner_id,
            "VServerGroup": list_of_vserver_group}
        repeat_info = {
            "VServerGroup": (
                'VServerGroup', 'list', 'dict', [
                    ('LoadBalancerId', 'str', None, None), ('VServerGroupAttribute', 'list', 'dict', [
                        ('VServerGroupId', 'str', None, None), ('Port', 'str', None, None), ('Weight', 'str', None, None), ],),]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_alarm(
            self,
            metric_type=None,
            period=None,
            resource_owner_account=None,
            group_id=None,
            description=None,
            list_of_alarm_action=None,
            threshold=None,
            owner_id=None,
            alarm_task_id=None,
            region_id=None,
            name=None,
            evaluation_count=None,
            metric_name=None,
            comparison_operator=None,
            list_of_dimension=None,
            statistics=None):
        api_request = APIRequest('ModifyAlarm', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MetricType": metric_type,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "GroupId": group_id,
            "Description": description,
            "AlarmAction": list_of_alarm_action,
            "Threshold": threshold,
            "OwnerId": owner_id,
            "AlarmTaskId": alarm_task_id,
            "RegionId": region_id,
            "Name": name,
            "EvaluationCount": evaluation_count,
            "MetricName": metric_name,
            "ComparisonOperator": comparison_operator,
            "Dimension": list_of_dimension,
            "Statistics": statistics}
        repeat_info = {
            "AlarmAction": (
                'AlarmAction', 'list', 'str', None), "Dimension": (
                'Dimension', 'list', 'dict', [
                    ('DimensionValue', 'str', None, None), ('DimensionKey', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def enable_alarm(
            self,
            resource_owner_account=None,
            region_id=None,
            owner_id=None,
            alarm_task_id=None):
        api_request = APIRequest('EnableAlarm', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerId": owner_id,
            "AlarmTaskId": alarm_task_id}
        return self._handle_request(api_request).result

    def disable_alarm(
            self,
            resource_owner_account=None,
            region_id=None,
            owner_id=None,
            alarm_task_id=None):
        api_request = APIRequest('DisableAlarm', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerId": owner_id,
            "AlarmTaskId": alarm_task_id}
        return self._handle_request(api_request).result

    def describe_alarms(
            self,
            is_enable=None,
            metric_type=None,
            resource_owner_account=None,
            region_id=None,
            scaling_group_id=None,
            page_size=None,
            state=None,
            owner_id=None,
            alarm_task_id=None,
            page_number=None):
        api_request = APIRequest('DescribeAlarms', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IsEnable": is_enable,
            "MetricType": metric_type,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ScalingGroupId": scaling_group_id,
            "PageSize": page_size,
            "State": state,
            "OwnerId": owner_id,
            "AlarmTaskId": alarm_task_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_alarm(
            self,
            resource_owner_account=None,
            region_id=None,
            owner_id=None,
            alarm_task_id=None):
        api_request = APIRequest('DeleteAlarm', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerId": owner_id,
            "AlarmTaskId": alarm_task_id}
        return self._handle_request(api_request).result

    def create_alarm(
            self,
            metric_type=None,
            period=None,
            resource_owner_account=None,
            scaling_group_id=None,
            group_id=None,
            description=None,
            list_of_alarm_action=None,
            threshold=None,
            owner_id=None,
            region_id=None,
            name=None,
            evaluation_count=None,
            metric_name=None,
            comparison_operator=None,
            list_of_dimension=None,
            statistics=None):
        api_request = APIRequest('CreateAlarm', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MetricType": metric_type,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "GroupId": group_id,
            "Description": description,
            "AlarmAction": list_of_alarm_action,
            "Threshold": threshold,
            "OwnerId": owner_id,
            "RegionId": region_id,
            "Name": name,
            "EvaluationCount": evaluation_count,
            "MetricName": metric_name,
            "ComparisonOperator": comparison_operator,
            "Dimension": list_of_dimension,
            "Statistics": statistics}
        repeat_info = {
            "AlarmAction": (
                'AlarmAction', 'list', 'str', None), "Dimension": (
                'Dimension', 'list', 'dict', [
                    ('DimensionValue', 'str', None, None), ('DimensionKey', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def detach_db_instances(
            self,
            resource_owner_account=None,
            scaling_group_id=None,
            list_of_db_instance=None,
            force_detach=None,
            owner_id=None):
        api_request = APIRequest('DetachDBInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "DBInstance": list_of_db_instance,
            "ForceDetach": force_detach,
            "OwnerId": owner_id}
        repeat_info = {"DBInstance": ('DBInstance', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def attach_db_instances(
            self,
            resource_owner_account=None,
            scaling_group_id=None,
            force_attach=None,
            list_of_db_instance=None,
            owner_id=None):
        api_request = APIRequest('AttachDBInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "ForceAttach": force_attach,
            "DBInstance": list_of_db_instance,
            "OwnerId": owner_id}
        repeat_info = {"DBInstance": ('DBInstance', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def detach_load_balancers(
            self,
            list_of_load_balancer=None,
            resource_owner_account=None,
            scaling_group_id=None,
            force_detach=None,
            owner_id=None):
        api_request = APIRequest('DetachLoadBalancers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LoadBalancer": list_of_load_balancer,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "ForceDetach": force_detach,
            "OwnerId": owner_id}
        repeat_info = {"LoadBalancer": ('LoadBalancer', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def attach_load_balancers(
            self,
            list_of_load_balancer=None,
            resource_owner_account=None,
            scaling_group_id=None,
            force_attach=None,
            owner_id=None):
        api_request = APIRequest('AttachLoadBalancers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LoadBalancer": list_of_load_balancer,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "ForceAttach": force_attach,
            "OwnerId": owner_id}
        repeat_info = {"LoadBalancer": ('LoadBalancer', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_scaling_configuration(
            self,
            image_id=None,
            memory=None,
            hpc_cluster_id=None,
            io_optimized=None,
            list_of_instance_types=None,
            internet_max_bandwidth_out=None,
            security_group_id=None,
            key_pair_name=None,
            list_of_spot_price_limit=None,
            system_disk_category=None,
            user_data=None,
            resource_group_id=None,
            host_name=None,
            password_inherit=None,
            image_name=None,
            instance_description=None,
            override=None,
            deployment_set_id=None,
            resource_owner_account=None,
            owner_account=None,
            cpu=None,
            system_disk_disk_name=None,
            ram_role_name=None,
            owner_id=None,
            list_of_security_group_ids=None,
            list_of_data_disk=None,
            scaling_configuration_name=None,
            tags=None,
            scaling_configuration_id=None,
            spot_strategy=None,
            instance_name=None,
            load_balancer_weight=None,
            system_disk_size=None,
            internet_charge_type=None,
            system_disk_description=None):
        api_request = APIRequest('ModifyScalingConfiguration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageId": image_id,
            "Memory": memory,
            "HpcClusterId": hpc_cluster_id,
            "IoOptimized": io_optimized,
            "InstanceTypes": list_of_instance_types,
            "InternetMaxBandwidthOut": internet_max_bandwidth_out,
            "SecurityGroupId": security_group_id,
            "KeyPairName": key_pair_name,
            "SpotPriceLimit": list_of_spot_price_limit,
            "SystemDisk.Category": system_disk_category,
            "UserData": user_data,
            "ResourceGroupId": resource_group_id,
            "HostName": host_name,
            "PasswordInherit": password_inherit,
            "ImageName": image_name,
            "InstanceDescription": instance_description,
            "Override": override,
            "DeploymentSetId": deployment_set_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Cpu": cpu,
            "SystemDisk.DiskName": system_disk_disk_name,
            "RamRoleName": ram_role_name,
            "OwnerId": owner_id,
            "SecurityGroupIds": list_of_security_group_ids,
            "DataDisk": list_of_data_disk,
            "ScalingConfigurationName": scaling_configuration_name,
            "Tags": tags,
            "ScalingConfigurationId": scaling_configuration_id,
            "SpotStrategy": spot_strategy,
            "InstanceName": instance_name,
            "LoadBalancerWeight": load_balancer_weight,
            "SystemDisk.Size": system_disk_size,
            "InternetChargeType": internet_charge_type,
            "SystemDisk.Description": system_disk_description}
        repeat_info = {"InstanceTypes": ('InstanceTypes', 'list', 'str', None),
                       "SpotPriceLimit": ('SpotPriceLimit', 'list', 'dict', [('InstanceType', 'str', None, None),
                                                                             ('PriceLimit', 'str', None, None),
                                                                             ]),
                       "SecurityGroupIds": ('SecurityGroupIds', 'list', 'str', None),
                       "DataDisk": ('DataDisk', 'list', 'dict', [('DiskName', 'str', None, None),
                                                                 ('SnapshotId', 'str', None, None),
                                                                 ('Size', 'str', None, None),
                                                                 ('Encrypted', 'str', None, None),
                                                                 ('Description', 'str', None, None),
                                                                 ('Category', 'str', None, None),
                                                                 ('KMSKeyId', 'str', None, None),
                                                                 ('Device', 'str', None, None),
                                                                 ('DeleteWithInstance', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_lifecycle_hooks(
            self,
            lifecycle_hook_name=None,
            resource_owner_account=None,
            scaling_group_id=None,
            list_of_lifecycle_hook_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeLifecycleHooks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LifecycleHookName": lifecycle_hook_name,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "LifecycleHookId": list_of_lifecycle_hook_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        repeat_info = {"LifecycleHookId": ('LifecycleHookId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_lifecycle_hook(
            self,
            default_result=None,
            resource_owner_account=None,
            heartbeat_timeout=None,
            lifecycle_hook_id=None,
            scaling_group_id=None,
            owner_account=None,
            notification_metadata=None,
            owner_id=None,
            lifecycle_transition=None,
            lifecycle_hook_name=None,
            notification_arn=None):
        api_request = APIRequest('ModifyLifecycleHook', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DefaultResult": default_result,
            "ResourceOwnerAccount": resource_owner_account,
            "HeartbeatTimeout": heartbeat_timeout,
            "LifecycleHookId": lifecycle_hook_id,
            "ScalingGroupId": scaling_group_id,
            "OwnerAccount": owner_account,
            "NotificationMetadata": notification_metadata,
            "OwnerId": owner_id,
            "LifecycleTransition": lifecycle_transition,
            "LifecycleHookName": lifecycle_hook_name,
            "NotificationArn": notification_arn}
        return self._handle_request(api_request).result

    def delete_lifecycle_hook(
            self,
            lifecycle_hook_name=None,
            resource_owner_account=None,
            lifecycle_hook_id=None,
            scaling_group_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteLifecycleHook', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LifecycleHookName": lifecycle_hook_name,
            "ResourceOwnerAccount": resource_owner_account,
            "LifecycleHookId": lifecycle_hook_id,
            "ScalingGroupId": scaling_group_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def complete_lifecycle_action(
            self,
            lifecycle_action_token=None,
            resource_owner_account=None,
            lifecycle_hook_id=None,
            owner_account=None,
            owner_id=None,
            lifecycle_action_result=None):
        api_request = APIRequest('CompleteLifecycleAction', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LifecycleActionToken": lifecycle_action_token,
            "ResourceOwnerAccount": resource_owner_account,
            "LifecycleHookId": lifecycle_hook_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "LifecycleActionResult": lifecycle_action_result}
        return self._handle_request(api_request).result

    def create_lifecycle_hook(
            self,
            default_result=None,
            resource_owner_account=None,
            heartbeat_timeout=None,
            scaling_group_id=None,
            owner_account=None,
            notification_metadata=None,
            owner_id=None,
            lifecycle_transition=None,
            lifecycle_hook_name=None,
            notification_arn=None,
            list_of_lifecycle_hook=None):
        api_request = APIRequest('CreateLifecycleHook', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DefaultResult": default_result,
            "ResourceOwnerAccount": resource_owner_account,
            "HeartbeatTimeout": heartbeat_timeout,
            "ScalingGroupId": scaling_group_id,
            "OwnerAccount": owner_account,
            "NotificationMetadata": notification_metadata,
            "OwnerId": owner_id,
            "LifecycleTransition": lifecycle_transition,
            "LifecycleHookName": lifecycle_hook_name,
            "NotificationArn": notification_arn,
            "LifecycleHook": list_of_lifecycle_hook}
        repeat_info = {"LifecycleHook": ('LifecycleHook',
                                         'list',
                                         'dict',
                                         [('DefaultResult',
                                           'str',
                                           None,
                                           None),
                                          ('LifecycleHookName',
                                           'str',
                                           None,
                                           None),
                                             ('HeartbeatTimeout',
                                              'str',
                                              None,
                                              None),
                                             ('NotificationArn',
                                              'str',
                                              None,
                                              None),
                                             ('NotificationMetadata',
                                              'str',
                                              None,
                                              None),
                                             ('LifecycleTransition',
                                              'str',
                                              None,
                                              None),
                                          ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def record_lifecycle_action_heartbeat(
            self,
            lifecycle_action_token=None,
            resource_owner_account=None,
            heartbeat_timeout=None,
            lifecycle_hook_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('RecordLifecycleActionHeartbeat', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "lifecycleActionToken": lifecycle_action_token,
            "ResourceOwnerAccount": resource_owner_account,
            "heartbeatTimeout": heartbeat_timeout,
            "lifecycleHookId": lifecycle_hook_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_instances_protection(
            self,
            list_of_instance_id=None,
            resource_owner_account=None,
            scaling_group_id=None,
            owner_id=None,
            protected_from_scale_in=None):
        api_request = APIRequest('SetInstancesProtection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": list_of_instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "OwnerId": owner_id,
            "ProtectedFromScaleIn": protected_from_scale_in}
        repeat_info = {"InstanceId": ('InstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def rebalance_instances(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            scaling_group_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('RebalanceInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_notification_configuration(
            self,
            resource_owner_account=None,
            scaling_group_id=None,
            notification_arn=None,
            owner_id=None):
        api_request = APIRequest('DeleteNotificationConfiguration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "NotificationArn": notification_arn,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_notification_configuration(
            self,
            resource_owner_account=None,
            scaling_group_id=None,
            notification_arn=None,
            list_of_notification_type=None,
            owner_id=None):
        api_request = APIRequest('ModifyNotificationConfiguration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "NotificationArn": notification_arn,
            "NotificationType": list_of_notification_type,
            "OwnerId": owner_id}
        repeat_info = {"NotificationType": ('NotificationType', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_notification_configurations(
            self,
            resource_owner_account=None,
            scaling_group_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeNotificationConfigurations',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_notification_types(self, resource_owner_account=None, owner_id=None):
        api_request = APIRequest('DescribeNotificationTypes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerAccount": resource_owner_account, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_notification_configuration(
            self,
            resource_owner_account=None,
            scaling_group_id=None,
            notification_arn=None,
            list_of_notification_type=None,
            owner_id=None):
        api_request = APIRequest('CreateNotificationConfiguration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "NotificationArn": notification_arn,
            "NotificationType": list_of_notification_type,
            "OwnerId": owner_id}
        repeat_info = {"NotificationType": ('NotificationType', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def exit_standby(
            self,
            list_of_instance_id=None,
            resource_owner_account=None,
            scaling_group_id=None,
            owner_id=None):
        api_request = APIRequest('ExitStandby', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": list_of_instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "OwnerId": owner_id}
        repeat_info = {"InstanceId": ('InstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def enter_standby(
            self,
            list_of_instance_id=None,
            resource_owner_account=None,
            scaling_group_id=None,
            owner_id=None):
        api_request = APIRequest('EnterStandby', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": list_of_instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "OwnerId": owner_id}
        repeat_info = {"InstanceId": ('InstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def deactivate_scaling_configuration(
            self,
            scaling_configuration_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeactivateScalingConfiguration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ScalingConfigurationId": scaling_configuration_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_alert_config(
            self,
            success_config=None,
            reject_config=None,
            resource_owner_account=None,
            scaling_group_id=None,
            owner_id=None,
            fail_config=None):
        api_request = APIRequest('ModifyAlertConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SuccessConfig": success_config,
            "RejectConfig": reject_config,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "OwnerId": owner_id,
            "FailConfig": fail_config}
        return self._handle_request(api_request).result

    def describe_alert_config(
            self,
            resource_owner_account=None,
            scaling_group_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeAlertConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def verify_authentication(
            self,
            uid=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('VerifyAuthentication', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Uid": uid,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def verify_user(self, resource_owner_id=None, resource_owner_account=None, owner_id=None):
        api_request = APIRequest('VerifyUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_regions(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            accept_language=None,
            owner_id=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "AcceptLanguage": accept_language,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_capacity_history(
            self,
            resource_owner_account=None,
            scaling_group_id=None,
            page_size=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeCapacityHistory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_limitation(self, resource_owner_account=None, owner_id=None):
        api_request = APIRequest('DescribeLimitation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerAccount": resource_owner_account, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_scaling_activity_detail(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            scaling_activity_id=None):
        api_request = APIRequest('DescribeScalingActivityDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "ScalingActivityId": scaling_activity_id}
        return self._handle_request(api_request).result

    def remove_instances(
            self,
            resource_owner_id=None,
            list_of_instance_id=None,
            remove_policy=None,
            resource_owner_account=None,
            scaling_group_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('RemoveInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": list_of_instance_id,
            "RemovePolicy": remove_policy,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        repeat_info = {"InstanceId": ('InstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_scheduled_task(
            self,
            launch_time=None,
            resource_owner_id=None,
            scheduled_action=None,
            max_value=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            owner_id=None,
            recurrence_value=None,
            launch_expiration_time=None,
            recurrence_end_time=None,
            min_value=None,
            scheduled_task_name=None,
            task_enabled=None,
            scheduled_task_id=None,
            recurrence_type=None):
        api_request = APIRequest('ModifyScheduledTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LaunchTime": launch_time,
            "ResourceOwnerId": resource_owner_id,
            "ScheduledAction": scheduled_action,
            "MaxValue": max_value,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "RecurrenceValue": recurrence_value,
            "LaunchExpirationTime": launch_expiration_time,
            "RecurrenceEndTime": recurrence_end_time,
            "MinValue": min_value,
            "ScheduledTaskName": scheduled_task_name,
            "TaskEnabled": task_enabled,
            "ScheduledTaskId": scheduled_task_id,
            "RecurrenceType": recurrence_type}
        return self._handle_request(api_request).result

    def modify_scaling_rule(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            adjustment_value=None,
            list_of_step_adjustment=None,
            estimated_instance_warmup=None,
            owner_account=None,
            predictive_task_buffer_time=None,
            adjustment_type=None,
            disable_scale_in=None,
            owner_id=None,
            scaling_rule_id=None,
            initial_max_size=None,
            predictive_value_buffer=None,
            scaling_rule_name=None,
            cooldown=None,
            min_adjustment_magnitude=None,
            predictive_value_behavior=None,
            target_value=None,
            metric_name=None,
            predictive_scaling_mode=None):
        api_request = APIRequest('ModifyScalingRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "AdjustmentValue": adjustment_value,
            "StepAdjustment": list_of_step_adjustment,
            "EstimatedInstanceWarmup": estimated_instance_warmup,
            "OwnerAccount": owner_account,
            "PredictiveTaskBufferTime": predictive_task_buffer_time,
            "AdjustmentType": adjustment_type,
            "DisableScaleIn": disable_scale_in,
            "OwnerId": owner_id,
            "ScalingRuleId": scaling_rule_id,
            "InitialMaxSize": initial_max_size,
            "PredictiveValueBuffer": predictive_value_buffer,
            "ScalingRuleName": scaling_rule_name,
            "Cooldown": cooldown,
            "MinAdjustmentMagnitude": min_adjustment_magnitude,
            "PredictiveValueBehavior": predictive_value_behavior,
            "TargetValue": target_value,
            "MetricName": metric_name,
            "PredictiveScalingMode": predictive_scaling_mode}
        repeat_info = {"StepAdjustment": ('StepAdjustment',
                                          'list',
                                          'dict',
                                          [('MetricIntervalLowerBound',
                                            'str',
                                            None,
                                            None),
                                           ('MetricIntervalUpperBound',
                                            'str',
                                            None,
                                            None),
                                              ('ScalingAdjustment',
                                               'str',
                                               None,
                                               None),
                                           ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_scaling_group(
            self,
            resource_owner_id=None,
            health_check_type=None,
            launch_template_id=None,
            resource_owner_account=None,
            scaling_group_name=None,
            scaling_group_id=None,
            list_of_vswitch_ids=None,
            owner_account=None,
            spot_instance_pools=None,
            active_scaling_configuration_id=None,
            min_size=None,
            owner_id=None,
            launch_template_version=None,
            on_demand_base_capacity=None,
            on_demand_percentage_above_base_capacity=None,
            spot_instance_remedy=None,
            max_size=None,
            default_cooldown=None,
            removal_policy1=None,
            removal_policy2=None):
        api_request = APIRequest('ModifyScalingGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HealthCheckType": health_check_type,
            "LaunchTemplateId": launch_template_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupName": scaling_group_name,
            "ScalingGroupId": scaling_group_id,
            "VSwitchIds": list_of_vswitch_ids,
            "OwnerAccount": owner_account,
            "SpotInstancePools": spot_instance_pools,
            "ActiveScalingConfigurationId": active_scaling_configuration_id,
            "MinSize": min_size,
            "OwnerId": owner_id,
            "LaunchTemplateVersion": launch_template_version,
            "OnDemandBaseCapacity": on_demand_base_capacity,
            "OnDemandPercentageAboveBaseCapacity": on_demand_percentage_above_base_capacity,
            "SpotInstanceRemedy": spot_instance_remedy,
            "MaxSize": max_size,
            "DefaultCooldown": default_cooldown,
            "RemovalPolicy.1": removal_policy1,
            "RemovalPolicy.2": removal_policy2}
        repeat_info = {"VSwitchIds": ('VSwitchIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def execute_scaling_rule(
            self,
            resource_owner_id=None,
            scaling_rule_ari=None,
            resource_owner_account=None,
            client_token=None,
            breach_threshold=None,
            owner_account=None,
            owner_id=None,
            metric_value=None):
        api_request = APIRequest('ExecuteScalingRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ScalingRuleAri": scaling_rule_ari,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "BreachThreshold": breach_threshold,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "MetricValue": metric_value}
        return self._handle_request(api_request).result

    def enable_scaling_group(
            self,
            load_balancer_weight6=None,
            load_balancer_weight11=None,
            load_balancer_weight7=None,
            load_balancer_weight12=None,
            resource_owner_id=None,
            load_balancer_weight8=None,
            load_balancer_weight9=None,
            load_balancer_weight10=None,
            load_balancer_weight2=None,
            load_balancer_weight15=None,
            load_balancer_weight3=None,
            load_balancer_weight16=None,
            load_balancer_weight4=None,
            load_balancer_weight13=None,
            load_balancer_weight5=None,
            load_balancer_weight14=None,
            active_scaling_configuration_id=None,
            load_balancer_weight1=None,
            instance_id1=None,
            load_balancer_weight20=None,
            instance_id3=None,
            launch_template_id=None,
            instance_id2=None,
            instance_id5=None,
            instance_id4=None,
            instance_id7=None,
            instance_id6=None,
            instance_id9=None,
            instance_id8=None,
            owner_id=None,
            load_balancer_weight19=None,
            load_balancer_weight17=None,
            load_balancer_weight18=None,
            instance_id10=None,
            instance_id12=None,
            instance_id11=None,
            scaling_group_id=None,
            instance_id20=None,
            resource_owner_account=None,
            owner_account=None,
            launch_template_version=None,
            instance_id18=None,
            instance_id17=None,
            instance_id19=None,
            instance_id14=None,
            instance_id13=None,
            instance_id16=None,
            instance_id15=None):
        api_request = APIRequest('EnableScalingGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LoadBalancerWeight.6": load_balancer_weight6,
            "LoadBalancerWeight.11": load_balancer_weight11,
            "LoadBalancerWeight.7": load_balancer_weight7,
            "LoadBalancerWeight.12": load_balancer_weight12,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerWeight.8": load_balancer_weight8,
            "LoadBalancerWeight.9": load_balancer_weight9,
            "LoadBalancerWeight.10": load_balancer_weight10,
            "LoadBalancerWeight.2": load_balancer_weight2,
            "LoadBalancerWeight.15": load_balancer_weight15,
            "LoadBalancerWeight.3": load_balancer_weight3,
            "LoadBalancerWeight.16": load_balancer_weight16,
            "LoadBalancerWeight.4": load_balancer_weight4,
            "LoadBalancerWeight.13": load_balancer_weight13,
            "LoadBalancerWeight.5": load_balancer_weight5,
            "LoadBalancerWeight.14": load_balancer_weight14,
            "ActiveScalingConfigurationId": active_scaling_configuration_id,
            "LoadBalancerWeight.1": load_balancer_weight1,
            "InstanceId.1": instance_id1,
            "LoadBalancerWeight.20": load_balancer_weight20,
            "InstanceId.3": instance_id3,
            "LaunchTemplateId": launch_template_id,
            "InstanceId.2": instance_id2,
            "InstanceId.5": instance_id5,
            "InstanceId.4": instance_id4,
            "InstanceId.7": instance_id7,
            "InstanceId.6": instance_id6,
            "InstanceId.9": instance_id9,
            "InstanceId.8": instance_id8,
            "OwnerId": owner_id,
            "LoadBalancerWeight.19": load_balancer_weight19,
            "LoadBalancerWeight.17": load_balancer_weight17,
            "LoadBalancerWeight.18": load_balancer_weight18,
            "InstanceId.10": instance_id10,
            "InstanceId.12": instance_id12,
            "InstanceId.11": instance_id11,
            "ScalingGroupId": scaling_group_id,
            "InstanceId.20": instance_id20,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "LaunchTemplateVersion": launch_template_version,
            "InstanceId.18": instance_id18,
            "InstanceId.17": instance_id17,
            "InstanceId.19": instance_id19,
            "InstanceId.14": instance_id14,
            "InstanceId.13": instance_id13,
            "InstanceId.16": instance_id16,
            "InstanceId.15": instance_id15}
        return self._handle_request(api_request).result

    def disable_scaling_group(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            scaling_group_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DisableScalingGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def detach_instances(
            self,
            resource_owner_id=None,
            list_of_instance_id=None,
            resource_owner_account=None,
            scaling_group_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DetachInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": list_of_instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        repeat_info = {"InstanceId": ('InstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_scheduled_tasks(
            self,
            resource_owner_id=None,
            scheduled_action2=None,
            scheduled_action1=None,
            scheduled_action6=None,
            scheduled_action5=None,
            scheduled_action4=None,
            scheduled_action3=None,
            scheduled_action9=None,
            scheduled_action8=None,
            scheduled_action7=None,
            owner_id=None,
            scheduled_task_name20=None,
            scheduled_task_name19=None,
            scheduled_task_name18=None,
            scheduled_task_id20=None,
            scheduled_task_name13=None,
            scheduled_task_name12=None,
            scheduled_task_name11=None,
            scheduled_task_name10=None,
            scheduled_task_name17=None,
            scheduled_task_name16=None,
            page_number=None,
            scheduled_task_name15=None,
            scheduled_task_name14=None,
            scheduled_task_id2=None,
            scheduled_task_id1=None,
            scheduled_task_id4=None,
            scheduled_task_id18=None,
            scheduled_task_id3=None,
            scheduled_task_id19=None,
            scheduled_task_id6=None,
            region_id=None,
            scheduled_task_id5=None,
            scheduled_task_id8=None,
            scheduled_task_name9=None,
            scheduled_action20=None,
            scheduled_task_id7=None,
            page_size=None,
            scheduled_task_id12=None,
            scheduled_task_name7=None,
            scheduled_task_id9=None,
            scheduled_task_id13=None,
            scheduled_task_name8=None,
            scheduled_task_id10=None,
            scheduled_task_name5=None,
            scheduled_task_id11=None,
            scheduled_task_name6=None,
            scheduled_task_id16=None,
            scheduled_task_name3=None,
            scheduled_task_id17=None,
            scheduled_task_name4=None,
            scheduled_task_id14=None,
            scheduled_task_name1=None,
            scheduled_task_id15=None,
            scheduled_task_name2=None,
            resource_owner_account=None,
            owner_account=None,
            scheduled_action18=None,
            scheduled_action19=None,
            scheduled_action16=None,
            scheduled_action17=None,
            scheduled_action14=None,
            scheduled_action15=None,
            scheduled_action12=None,
            scheduled_action13=None,
            scheduled_action10=None,
            scheduled_action11=None):
        api_request = APIRequest('DescribeScheduledTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ScheduledAction.2": scheduled_action2,
            "ScheduledAction.1": scheduled_action1,
            "ScheduledAction.6": scheduled_action6,
            "ScheduledAction.5": scheduled_action5,
            "ScheduledAction.4": scheduled_action4,
            "ScheduledAction.3": scheduled_action3,
            "ScheduledAction.9": scheduled_action9,
            "ScheduledAction.8": scheduled_action8,
            "ScheduledAction.7": scheduled_action7,
            "OwnerId": owner_id,
            "ScheduledTaskName.20": scheduled_task_name20,
            "ScheduledTaskName.19": scheduled_task_name19,
            "ScheduledTaskName.18": scheduled_task_name18,
            "ScheduledTaskId.20": scheduled_task_id20,
            "ScheduledTaskName.13": scheduled_task_name13,
            "ScheduledTaskName.12": scheduled_task_name12,
            "ScheduledTaskName.11": scheduled_task_name11,
            "ScheduledTaskName.10": scheduled_task_name10,
            "ScheduledTaskName.17": scheduled_task_name17,
            "ScheduledTaskName.16": scheduled_task_name16,
            "PageNumber": page_number,
            "ScheduledTaskName.15": scheduled_task_name15,
            "ScheduledTaskName.14": scheduled_task_name14,
            "ScheduledTaskId.2": scheduled_task_id2,
            "ScheduledTaskId.1": scheduled_task_id1,
            "ScheduledTaskId.4": scheduled_task_id4,
            "ScheduledTaskId.18": scheduled_task_id18,
            "ScheduledTaskId.3": scheduled_task_id3,
            "ScheduledTaskId.19": scheduled_task_id19,
            "ScheduledTaskId.6": scheduled_task_id6,
            "RegionId": region_id,
            "ScheduledTaskId.5": scheduled_task_id5,
            "ScheduledTaskId.8": scheduled_task_id8,
            "ScheduledTaskName.9": scheduled_task_name9,
            "ScheduledAction.20": scheduled_action20,
            "ScheduledTaskId.7": scheduled_task_id7,
            "PageSize": page_size,
            "ScheduledTaskId.12": scheduled_task_id12,
            "ScheduledTaskName.7": scheduled_task_name7,
            "ScheduledTaskId.9": scheduled_task_id9,
            "ScheduledTaskId.13": scheduled_task_id13,
            "ScheduledTaskName.8": scheduled_task_name8,
            "ScheduledTaskId.10": scheduled_task_id10,
            "ScheduledTaskName.5": scheduled_task_name5,
            "ScheduledTaskId.11": scheduled_task_id11,
            "ScheduledTaskName.6": scheduled_task_name6,
            "ScheduledTaskId.16": scheduled_task_id16,
            "ScheduledTaskName.3": scheduled_task_name3,
            "ScheduledTaskId.17": scheduled_task_id17,
            "ScheduledTaskName.4": scheduled_task_name4,
            "ScheduledTaskId.14": scheduled_task_id14,
            "ScheduledTaskName.1": scheduled_task_name1,
            "ScheduledTaskId.15": scheduled_task_id15,
            "ScheduledTaskName.2": scheduled_task_name2,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ScheduledAction.18": scheduled_action18,
            "ScheduledAction.19": scheduled_action19,
            "ScheduledAction.16": scheduled_action16,
            "ScheduledAction.17": scheduled_action17,
            "ScheduledAction.14": scheduled_action14,
            "ScheduledAction.15": scheduled_action15,
            "ScheduledAction.12": scheduled_action12,
            "ScheduledAction.13": scheduled_action13,
            "ScheduledAction.10": scheduled_action10,
            "ScheduledAction.11": scheduled_action11}
        return self._handle_request(api_request).result

    def describe_scaling_rules(
            self,
            scaling_rule_name1=None,
            resource_owner_id=None,
            scaling_rule_name2=None,
            scaling_rule_name3=None,
            scaling_rule_name4=None,
            scaling_rule_name5=None,
            scaling_group_id=None,
            scaling_rule_name6=None,
            scaling_rule_name7=None,
            scaling_rule_name8=None,
            scaling_rule_ari9=None,
            scaling_rule_name9=None,
            page_number=None,
            region_id=None,
            page_size=None,
            scaling_rule_type=None,
            scaling_rule_id10=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            scaling_rule_ari1=None,
            scaling_rule_ari2=None,
            scaling_rule_name10=None,
            scaling_rule_ari3=None,
            scaling_rule_ari4=None,
            scaling_rule_id8=None,
            scaling_rule_ari5=None,
            scaling_rule_id9=None,
            scaling_rule_ari6=None,
            scaling_rule_ari7=None,
            scaling_rule_ari10=None,
            scaling_rule_ari8=None,
            scaling_rule_id4=None,
            show_alarm_rules=None,
            scaling_rule_id5=None,
            scaling_rule_id6=None,
            scaling_rule_id7=None,
            scaling_rule_id1=None,
            scaling_rule_id2=None,
            scaling_rule_id3=None):
        api_request = APIRequest('DescribeScalingRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ScalingRuleName.1": scaling_rule_name1,
            "ResourceOwnerId": resource_owner_id,
            "ScalingRuleName.2": scaling_rule_name2,
            "ScalingRuleName.3": scaling_rule_name3,
            "ScalingRuleName.4": scaling_rule_name4,
            "ScalingRuleName.5": scaling_rule_name5,
            "ScalingGroupId": scaling_group_id,
            "ScalingRuleName.6": scaling_rule_name6,
            "ScalingRuleName.7": scaling_rule_name7,
            "ScalingRuleName.8": scaling_rule_name8,
            "ScalingRuleAri.9": scaling_rule_ari9,
            "ScalingRuleName.9": scaling_rule_name9,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "ScalingRuleType": scaling_rule_type,
            "ScalingRuleId.10": scaling_rule_id10,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ScalingRuleAri.1": scaling_rule_ari1,
            "ScalingRuleAri.2": scaling_rule_ari2,
            "ScalingRuleName.10": scaling_rule_name10,
            "ScalingRuleAri.3": scaling_rule_ari3,
            "ScalingRuleAri.4": scaling_rule_ari4,
            "ScalingRuleId.8": scaling_rule_id8,
            "ScalingRuleAri.5": scaling_rule_ari5,
            "ScalingRuleId.9": scaling_rule_id9,
            "ScalingRuleAri.6": scaling_rule_ari6,
            "ScalingRuleAri.7": scaling_rule_ari7,
            "ScalingRuleAri.10": scaling_rule_ari10,
            "ScalingRuleAri.8": scaling_rule_ari8,
            "ScalingRuleId.4": scaling_rule_id4,
            "ShowAlarmRules": show_alarm_rules,
            "ScalingRuleId.5": scaling_rule_id5,
            "ScalingRuleId.6": scaling_rule_id6,
            "ScalingRuleId.7": scaling_rule_id7,
            "ScalingRuleId.1": scaling_rule_id1,
            "ScalingRuleId.2": scaling_rule_id2,
            "ScalingRuleId.3": scaling_rule_id3}
        return self._handle_request(api_request).result

    def describe_scaling_instances(
            self,
            instance_id10=None,
            resource_owner_id=None,
            instance_id12=None,
            instance_id11=None,
            scaling_group_id=None,
            lifecycle_state=None,
            creation_type=None,
            page_number=None,
            region_id=None,
            page_size=None,
            instance_id20=None,
            instance_id1=None,
            instance_id3=None,
            resource_owner_account=None,
            instance_id2=None,
            instance_id5=None,
            instance_id4=None,
            owner_account=None,
            instance_id7=None,
            instance_id6=None,
            instance_id9=None,
            instance_id8=None,
            owner_id=None,
            scaling_configuration_id=None,
            health_status=None,
            instance_id18=None,
            instance_id17=None,
            instance_id19=None,
            instance_id14=None,
            instance_id13=None,
            instance_id16=None,
            instance_id15=None):
        api_request = APIRequest('DescribeScalingInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId.10": instance_id10,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId.12": instance_id12,
            "InstanceId.11": instance_id11,
            "ScalingGroupId": scaling_group_id,
            "LifecycleState": lifecycle_state,
            "CreationType": creation_type,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "InstanceId.20": instance_id20,
            "InstanceId.1": instance_id1,
            "InstanceId.3": instance_id3,
            "ResourceOwnerAccount": resource_owner_account,
            "InstanceId.2": instance_id2,
            "InstanceId.5": instance_id5,
            "InstanceId.4": instance_id4,
            "OwnerAccount": owner_account,
            "InstanceId.7": instance_id7,
            "InstanceId.6": instance_id6,
            "InstanceId.9": instance_id9,
            "InstanceId.8": instance_id8,
            "OwnerId": owner_id,
            "ScalingConfigurationId": scaling_configuration_id,
            "HealthStatus": health_status,
            "InstanceId.18": instance_id18,
            "InstanceId.17": instance_id17,
            "InstanceId.19": instance_id19,
            "InstanceId.14": instance_id14,
            "InstanceId.13": instance_id13,
            "InstanceId.16": instance_id16,
            "InstanceId.15": instance_id15}
        return self._handle_request(api_request).result

    def describe_scaling_groups(
            self,
            resource_owner_id=None,
            scaling_group_id10=None,
            scaling_group_id12=None,
            scaling_group_id13=None,
            scaling_group_id14=None,
            scaling_group_id15=None,
            owner_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            scaling_group_name20=None,
            scaling_group_name19=None,
            scaling_group_id20=None,
            scaling_group_name18=None,
            scaling_group_name17=None,
            scaling_group_name16=None,
            resource_owner_account=None,
            scaling_group_name=None,
            owner_account=None,
            scaling_group_name1=None,
            scaling_group_name2=None,
            scaling_group_id2=None,
            scaling_group_id1=None,
            scaling_group_id6=None,
            scaling_group_id16=None,
            scaling_group_name7=None,
            scaling_group_name11=None,
            scaling_group_id5=None,
            scaling_group_id17=None,
            scaling_group_name8=None,
            scaling_group_name10=None,
            scaling_group_id4=None,
            scaling_group_id18=None,
            scaling_group_name9=None,
            scaling_group_id3=None,
            scaling_group_id19=None,
            scaling_group_name3=None,
            scaling_group_name15=None,
            scaling_group_id9=None,
            scaling_group_name4=None,
            scaling_group_name14=None,
            scaling_group_id8=None,
            scaling_group_name5=None,
            scaling_group_name13=None,
            scaling_group_id7=None,
            scaling_group_name6=None,
            scaling_group_name12=None):
        api_request = APIRequest('DescribeScalingGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ScalingGroupId.10": scaling_group_id10,
            "ScalingGroupId.12": scaling_group_id12,
            "ScalingGroupId.13": scaling_group_id13,
            "ScalingGroupId.14": scaling_group_id14,
            "ScalingGroupId.15": scaling_group_id15,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "ScalingGroupName.20": scaling_group_name20,
            "ScalingGroupName.19": scaling_group_name19,
            "ScalingGroupId.20": scaling_group_id20,
            "ScalingGroupName.18": scaling_group_name18,
            "ScalingGroupName.17": scaling_group_name17,
            "ScalingGroupName.16": scaling_group_name16,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupName": scaling_group_name,
            "OwnerAccount": owner_account,
            "ScalingGroupName.1": scaling_group_name1,
            "ScalingGroupName.2": scaling_group_name2,
            "ScalingGroupId.2": scaling_group_id2,
            "ScalingGroupId.1": scaling_group_id1,
            "ScalingGroupId.6": scaling_group_id6,
            "ScalingGroupId.16": scaling_group_id16,
            "ScalingGroupName.7": scaling_group_name7,
            "ScalingGroupName.11": scaling_group_name11,
            "ScalingGroupId.5": scaling_group_id5,
            "ScalingGroupId.17": scaling_group_id17,
            "ScalingGroupName.8": scaling_group_name8,
            "ScalingGroupName.10": scaling_group_name10,
            "ScalingGroupId.4": scaling_group_id4,
            "ScalingGroupId.18": scaling_group_id18,
            "ScalingGroupName.9": scaling_group_name9,
            "ScalingGroupId.3": scaling_group_id3,
            "ScalingGroupId.19": scaling_group_id19,
            "ScalingGroupName.3": scaling_group_name3,
            "ScalingGroupName.15": scaling_group_name15,
            "ScalingGroupId.9": scaling_group_id9,
            "ScalingGroupName.4": scaling_group_name4,
            "ScalingGroupName.14": scaling_group_name14,
            "ScalingGroupId.8": scaling_group_id8,
            "ScalingGroupName.5": scaling_group_name5,
            "ScalingGroupName.13": scaling_group_name13,
            "ScalingGroupId.7": scaling_group_id7,
            "ScalingGroupName.6": scaling_group_name6,
            "ScalingGroupName.12": scaling_group_name12}
        return self._handle_request(api_request).result

    def describe_scaling_configurations(
            self,
            scaling_configuration_id6=None,
            scaling_configuration_id7=None,
            resource_owner_id=None,
            scaling_configuration_id4=None,
            scaling_configuration_id5=None,
            scaling_group_id=None,
            scaling_configuration_id8=None,
            scaling_configuration_id9=None,
            scaling_configuration_id10=None,
            page_number=None,
            scaling_configuration_name2=None,
            region_id=None,
            scaling_configuration_name3=None,
            scaling_configuration_name1=None,
            page_size=None,
            scaling_configuration_id2=None,
            scaling_configuration_id3=None,
            scaling_configuration_id1=None,
            resource_owner_account=None,
            owner_account=None,
            scaling_configuration_name6=None,
            scaling_configuration_name7=None,
            scaling_configuration_name4=None,
            scaling_configuration_name5=None,
            owner_id=None,
            scaling_configuration_name8=None,
            scaling_configuration_name9=None,
            scaling_configuration_name10=None):
        api_request = APIRequest('DescribeScalingConfigurations', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ScalingConfigurationId.6": scaling_configuration_id6,
            "ScalingConfigurationId.7": scaling_configuration_id7,
            "ResourceOwnerId": resource_owner_id,
            "ScalingConfigurationId.4": scaling_configuration_id4,
            "ScalingConfigurationId.5": scaling_configuration_id5,
            "ScalingGroupId": scaling_group_id,
            "ScalingConfigurationId.8": scaling_configuration_id8,
            "ScalingConfigurationId.9": scaling_configuration_id9,
            "ScalingConfigurationId.10": scaling_configuration_id10,
            "PageNumber": page_number,
            "ScalingConfigurationName.2": scaling_configuration_name2,
            "RegionId": region_id,
            "ScalingConfigurationName.3": scaling_configuration_name3,
            "ScalingConfigurationName.1": scaling_configuration_name1,
            "PageSize": page_size,
            "ScalingConfigurationId.2": scaling_configuration_id2,
            "ScalingConfigurationId.3": scaling_configuration_id3,
            "ScalingConfigurationId.1": scaling_configuration_id1,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ScalingConfigurationName.6": scaling_configuration_name6,
            "ScalingConfigurationName.7": scaling_configuration_name7,
            "ScalingConfigurationName.4": scaling_configuration_name4,
            "ScalingConfigurationName.5": scaling_configuration_name5,
            "OwnerId": owner_id,
            "ScalingConfigurationName.8": scaling_configuration_name8,
            "ScalingConfigurationName.9": scaling_configuration_name9,
            "ScalingConfigurationName.10": scaling_configuration_name10}
        return self._handle_request(api_request).result

    def describe_scaling_activities(
            self,
            scaling_activity_id9=None,
            resource_owner_id=None,
            scaling_activity_id5=None,
            scaling_activity_id6=None,
            scaling_group_id=None,
            scaling_activity_id7=None,
            scaling_activity_id8=None,
            scaling_activity_id1=None,
            scaling_activity_id2=None,
            scaling_activity_id3=None,
            scaling_activity_id4=None,
            page_number=None,
            status_code=None,
            region_id=None,
            page_size=None,
            scaling_activity_id11=None,
            scaling_activity_id10=None,
            scaling_activity_id13=None,
            scaling_activity_id12=None,
            scaling_activity_id15=None,
            scaling_activity_id14=None,
            scaling_activity_id17=None,
            scaling_activity_id16=None,
            scaling_activity_id19=None,
            resource_owner_account=None,
            scaling_activity_id18=None,
            owner_account=None,
            owner_id=None,
            scaling_activity_id20=None):
        api_request = APIRequest('DescribeScalingActivities', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ScalingActivityId.9": scaling_activity_id9,
            "ResourceOwnerId": resource_owner_id,
            "ScalingActivityId.5": scaling_activity_id5,
            "ScalingActivityId.6": scaling_activity_id6,
            "ScalingGroupId": scaling_group_id,
            "ScalingActivityId.7": scaling_activity_id7,
            "ScalingActivityId.8": scaling_activity_id8,
            "ScalingActivityId.1": scaling_activity_id1,
            "ScalingActivityId.2": scaling_activity_id2,
            "ScalingActivityId.3": scaling_activity_id3,
            "ScalingActivityId.4": scaling_activity_id4,
            "PageNumber": page_number,
            "StatusCode": status_code,
            "RegionId": region_id,
            "PageSize": page_size,
            "ScalingActivityId.11": scaling_activity_id11,
            "ScalingActivityId.10": scaling_activity_id10,
            "ScalingActivityId.13": scaling_activity_id13,
            "ScalingActivityId.12": scaling_activity_id12,
            "ScalingActivityId.15": scaling_activity_id15,
            "ScalingActivityId.14": scaling_activity_id14,
            "ScalingActivityId.17": scaling_activity_id17,
            "ScalingActivityId.16": scaling_activity_id16,
            "ScalingActivityId.19": scaling_activity_id19,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingActivityId.18": scaling_activity_id18,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ScalingActivityId.20": scaling_activity_id20}
        return self._handle_request(api_request).result

    def delete_scheduled_task(
            self,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            scheduled_task_id=None):
        api_request = APIRequest('DeleteScheduledTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ScheduledTaskId": scheduled_task_id}
        return self._handle_request(api_request).result

    def delete_scaling_rule(
            self,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            scaling_rule_id=None):
        api_request = APIRequest('DeleteScalingRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ScalingRuleId": scaling_rule_id}
        return self._handle_request(api_request).result

    def delete_scaling_group(
            self,
            resource_owner_account=None,
            scaling_group_id=None,
            force_delete=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteScalingGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupId": scaling_group_id,
            "ForceDelete": force_delete,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_scaling_configuration(
            self,
            scaling_configuration_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteScalingConfiguration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ScalingConfigurationId": scaling_configuration_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_scheduled_task(
            self,
            launch_time=None,
            scheduled_action=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            owner_id=None,
            recurrence_value=None,
            launch_expiration_time=None,
            recurrence_end_time=None,
            region_id=None,
            scheduled_task_name=None,
            task_enabled=None,
            recurrence_type=None):
        api_request = APIRequest('CreateScheduledTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LaunchTime": launch_time,
            "ScheduledAction": scheduled_action,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "RecurrenceValue": recurrence_value,
            "LaunchExpirationTime": launch_expiration_time,
            "RecurrenceEndTime": recurrence_end_time,
            "RegionId": region_id,
            "ScheduledTaskName": scheduled_task_name,
            "TaskEnabled": task_enabled,
            "RecurrenceType": recurrence_type}
        return self._handle_request(api_request).result

    def create_scaling_rule(
            self,
            resource_owner_account=None,
            adjustment_value=None,
            list_of_step_adjustment=None,
            scaling_group_id=None,
            estimated_instance_warmup=None,
            owner_account=None,
            predictive_task_buffer_time=None,
            adjustment_type=None,
            disable_scale_in=None,
            owner_id=None,
            initial_max_size=None,
            predictive_value_buffer=None,
            scaling_rule_name=None,
            cooldown=None,
            min_adjustment_magnitude=None,
            predictive_value_behavior=None,
            target_value=None,
            scaling_rule_type=None,
            metric_name=None,
            predictive_scaling_mode=None):
        api_request = APIRequest('CreateScalingRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerAccount": resource_owner_account,
            "AdjustmentValue": adjustment_value,
            "StepAdjustment": list_of_step_adjustment,
            "ScalingGroupId": scaling_group_id,
            "EstimatedInstanceWarmup": estimated_instance_warmup,
            "OwnerAccount": owner_account,
            "PredictiveTaskBufferTime": predictive_task_buffer_time,
            "AdjustmentType": adjustment_type,
            "DisableScaleIn": disable_scale_in,
            "OwnerId": owner_id,
            "InitialMaxSize": initial_max_size,
            "PredictiveValueBuffer": predictive_value_buffer,
            "ScalingRuleName": scaling_rule_name,
            "Cooldown": cooldown,
            "MinAdjustmentMagnitude": min_adjustment_magnitude,
            "PredictiveValueBehavior": predictive_value_behavior,
            "TargetValue": target_value,
            "ScalingRuleType": scaling_rule_type,
            "MetricName": metric_name,
            "PredictiveScalingMode": predictive_scaling_mode}
        repeat_info = {"StepAdjustment": ('StepAdjustment',
                                          'list',
                                          'dict',
                                          [('MetricIntervalLowerBound',
                                            'str',
                                            None,
                                            None),
                                           ('MetricIntervalUpperBound',
                                            'str',
                                            None,
                                            None),
                                              ('ScalingAdjustment',
                                               'str',
                                               None,
                                               None),
                                           ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_scaling_group(
            self,
            load_balancer_ids=None,
            client_token=None,
            list_of_vswitch_ids=None,
            on_demand_base_capacity=None,
            on_demand_percentage_above_base_capacity=None,
            spot_instance_remedy=None,
            region_id=None,
            default_cooldown=None,
            removal_policy1=None,
            removal_policy2=None,
            multi_az_policy=None,
            db_instance_ids=None,
            launch_template_id=None,
            health_check_type=None,
            resource_owner_account=None,
            scaling_group_name=None,
            owner_account=None,
            spot_instance_pools=None,
            min_size=None,
            owner_id=None,
            launch_template_version=None,
            scaling_policy=None,
            vswitch_id=None,
            max_size=None,
            list_of_lifecycle_hook=None,
            list_of_vserver_group=None):
        api_request = APIRequest('CreateScalingGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LoadBalancerIds": load_balancer_ids,
            "ClientToken": client_token,
            "VSwitchIds": list_of_vswitch_ids,
            "OnDemandBaseCapacity": on_demand_base_capacity,
            "OnDemandPercentageAboveBaseCapacity": on_demand_percentage_above_base_capacity,
            "SpotInstanceRemedy": spot_instance_remedy,
            "RegionId": region_id,
            "DefaultCooldown": default_cooldown,
            "RemovalPolicy.1": removal_policy1,
            "RemovalPolicy.2": removal_policy2,
            "MultiAZPolicy": multi_az_policy,
            "DBInstanceIds": db_instance_ids,
            "LaunchTemplateId": launch_template_id,
            "HealthCheckType": health_check_type,
            "ResourceOwnerAccount": resource_owner_account,
            "ScalingGroupName": scaling_group_name,
            "OwnerAccount": owner_account,
            "SpotInstancePools": spot_instance_pools,
            "MinSize": min_size,
            "OwnerId": owner_id,
            "LaunchTemplateVersion": launch_template_version,
            "ScalingPolicy": scaling_policy,
            "VSwitchId": vswitch_id,
            "MaxSize": max_size,
            "LifecycleHook": list_of_lifecycle_hook,
            "VServerGroup": list_of_vserver_group}
        repeat_info = {"VSwitchIds": ('VSwitchIds', 'list', 'str', None),
                       "LifecycleHook": ('LifecycleHook', 'list', 'dict', [('DefaultResult', 'str', None, None),
                                                                           ('LifecycleHookName', 'str', None, None),
                                                                           ('HeartbeatTimeout', 'str', None, None),
                                                                           ('NotificationArn', 'str', None, None),
                                                                           ('NotificationMetadata', 'str', None, None),
                                                                           ('LifecycleTransition', 'str', None, None),
                                                                           ]),
                       "VServerGroup": ('VServerGroup', 'list', 'dict', [('LoadBalancerId', 'str', None, None),
                                                                         ('VServerGroupAttribute', 'list', 'dict', [('VServerGroupId', 'str', None, None),
                                                                                                                    ('Port', 'str', None, None),
                                                                                                                    ('Weight', 'str', None, None),
                                                                                                                    ],),]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_scaling_configuration(
            self,
            image_id=None,
            memory=None,
            hpc_cluster_id=None,
            client_token=None,
            scaling_group_id=None,
            list_of_instance_types=None,
            io_optimized=None,
            security_group_id=None,
            internet_max_bandwidth_out=None,
            security_enhancement_strategy=None,
            key_pair_name=None,
            list_of_spot_price_limit=None,
            system_disk_category=None,
            user_data=None,
            resource_group_id=None,
            host_name=None,
            password=None,
            password_inherit=None,
            image_name=None,
            instance_description=None,
            instance_type=None,
            deployment_set_id=None,
            resource_owner_account=None,
            owner_account=None,
            cpu=None,
            system_disk_disk_name=None,
            ram_role_name=None,
            owner_id=None,
            list_of_security_group_ids=None,
            list_of_data_disk=None,
            scaling_configuration_name=None,
            tags=None,
            spot_strategy=None,
            load_balancer_weight=None,
            instance_name=None,
            system_disk_size=None,
            internet_charge_type=None,
            internet_max_bandwidth_in=None,
            system_disk_description=None):
        api_request = APIRequest('CreateScalingConfiguration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageId": image_id,
            "Memory": memory,
            "HpcClusterId": hpc_cluster_id,
            "ClientToken": client_token,
            "ScalingGroupId": scaling_group_id,
            "InstanceTypes": list_of_instance_types,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "InternetMaxBandwidthOut": internet_max_bandwidth_out,
            "SecurityEnhancementStrategy": security_enhancement_strategy,
            "KeyPairName": key_pair_name,
            "SpotPriceLimit": list_of_spot_price_limit,
            "SystemDisk.Category": system_disk_category,
            "UserData": user_data,
            "ResourceGroupId": resource_group_id,
            "HostName": host_name,
            "Password": password,
            "PasswordInherit": password_inherit,
            "ImageName": image_name,
            "InstanceDescription": instance_description,
            "InstanceType": instance_type,
            "DeploymentSetId": deployment_set_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Cpu": cpu,
            "SystemDisk.DiskName": system_disk_disk_name,
            "RamRoleName": ram_role_name,
            "OwnerId": owner_id,
            "SecurityGroupIds": list_of_security_group_ids,
            "DataDisk": list_of_data_disk,
            "ScalingConfigurationName": scaling_configuration_name,
            "Tags": tags,
            "SpotStrategy": spot_strategy,
            "LoadBalancerWeight": load_balancer_weight,
            "InstanceName": instance_name,
            "SystemDisk.Size": system_disk_size,
            "InternetChargeType": internet_charge_type,
            "InternetMaxBandwidthIn": internet_max_bandwidth_in,
            "SystemDisk.Description": system_disk_description}
        repeat_info = {"InstanceTypes": ('InstanceTypes', 'list', 'str', None),
                       "SpotPriceLimit": ('SpotPriceLimit', 'list', 'dict', [('InstanceType', 'str', None, None),
                                                                             ('PriceLimit', 'str', None, None),
                                                                             ]),
                       "SecurityGroupIds": ('SecurityGroupIds', 'list', 'str', None),
                       "DataDisk": ('DataDisk', 'list', 'dict', [('DiskName', 'str', None, None),
                                                                 ('SnapshotId', 'str', None, None),
                                                                 ('Size', 'str', None, None),
                                                                 ('Encrypted', 'str', None, None),
                                                                 ('Description', 'str', None, None),
                                                                 ('Category', 'str', None, None),
                                                                 ('KMSKeyId', 'str', None, None),
                                                                 ('Device', 'str', None, None),
                                                                 ('DeleteWithInstance', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def attach_instances(
            self,
            instance_id10=None,
            load_balancer_weight6=None,
            load_balancer_weight11=None,
            load_balancer_weight7=None,
            load_balancer_weight12=None,
            resource_owner_id=None,
            instance_id12=None,
            load_balancer_weight8=None,
            instance_id11=None,
            load_balancer_weight9=None,
            load_balancer_weight10=None,
            load_balancer_weight2=None,
            load_balancer_weight15=None,
            load_balancer_weight3=None,
            load_balancer_weight16=None,
            scaling_group_id=None,
            load_balancer_weight4=None,
            load_balancer_weight13=None,
            load_balancer_weight5=None,
            load_balancer_weight14=None,
            load_balancer_weight1=None,
            instance_id20=None,
            instance_id1=None,
            load_balancer_weight20=None,
            instance_id3=None,
            resource_owner_account=None,
            instance_id2=None,
            instance_id5=None,
            instance_id4=None,
            owner_account=None,
            instance_id7=None,
            instance_id6=None,
            instance_id9=None,
            instance_id8=None,
            owner_id=None,
            instance_id18=None,
            load_balancer_weight19=None,
            instance_id17=None,
            load_balancer_weight17=None,
            instance_id19=None,
            load_balancer_weight18=None,
            instance_id14=None,
            instance_id13=None,
            instance_id16=None,
            instance_id15=None):
        api_request = APIRequest('AttachInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId.10": instance_id10,
            "LoadBalancerWeight.6": load_balancer_weight6,
            "LoadBalancerWeight.11": load_balancer_weight11,
            "LoadBalancerWeight.7": load_balancer_weight7,
            "LoadBalancerWeight.12": load_balancer_weight12,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId.12": instance_id12,
            "LoadBalancerWeight.8": load_balancer_weight8,
            "InstanceId.11": instance_id11,
            "LoadBalancerWeight.9": load_balancer_weight9,
            "LoadBalancerWeight.10": load_balancer_weight10,
            "LoadBalancerWeight.2": load_balancer_weight2,
            "LoadBalancerWeight.15": load_balancer_weight15,
            "LoadBalancerWeight.3": load_balancer_weight3,
            "LoadBalancerWeight.16": load_balancer_weight16,
            "ScalingGroupId": scaling_group_id,
            "LoadBalancerWeight.4": load_balancer_weight4,
            "LoadBalancerWeight.13": load_balancer_weight13,
            "LoadBalancerWeight.5": load_balancer_weight5,
            "LoadBalancerWeight.14": load_balancer_weight14,
            "LoadBalancerWeight.1": load_balancer_weight1,
            "InstanceId.20": instance_id20,
            "InstanceId.1": instance_id1,
            "LoadBalancerWeight.20": load_balancer_weight20,
            "InstanceId.3": instance_id3,
            "ResourceOwnerAccount": resource_owner_account,
            "InstanceId.2": instance_id2,
            "InstanceId.5": instance_id5,
            "InstanceId.4": instance_id4,
            "OwnerAccount": owner_account,
            "InstanceId.7": instance_id7,
            "InstanceId.6": instance_id6,
            "InstanceId.9": instance_id9,
            "InstanceId.8": instance_id8,
            "OwnerId": owner_id,
            "InstanceId.18": instance_id18,
            "LoadBalancerWeight.19": load_balancer_weight19,
            "InstanceId.17": instance_id17,
            "LoadBalancerWeight.17": load_balancer_weight17,
            "InstanceId.19": instance_id19,
            "LoadBalancerWeight.18": load_balancer_weight18,
            "InstanceId.14": instance_id14,
            "InstanceId.13": instance_id13,
            "InstanceId.16": instance_id16,
            "InstanceId.15": instance_id15}
        return self._handle_request(api_request).result
