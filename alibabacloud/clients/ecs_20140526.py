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


class EcsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Ecs'
        self.api_version = '2014-05-26'
        self.location_service_code = 'ecs'
        self.location_endpoint_type = 'openAPI'

    def delete_instances(
            self,
            resource_owner_id=None,
            list_of_instance_id=None,
            dry_run=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            terminate_subscription=None,
            force=None,
            owner_id=None):
        api_request = APIRequest('DeleteInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": list_of_instance_id,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "TerminateSubscription": terminate_subscription,
            "Force": force,
            "OwnerId": owner_id}
        repeat_info = {"InstanceId": ('InstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_storage_set_attribute(
            self,
            resource_owner_id=None,
            client_token=None,
            description=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            storage_set_id=None,
            storage_set_name=None):
        api_request = APIRequest('ModifyStorageSetAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "Description": description,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "StorageSetId": storage_set_id,
            "StorageSetName": storage_set_name}
        return self._handle_request(api_request).result

    def describe_storage_sets(
            self,
            resource_owner_id=None,
            client_token=None,
            storage_set_ids=None,
            page_number=None,
            region_id=None,
            page_size=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            zone_id=None,
            storage_set_name=None):
        api_request = APIRequest('DescribeStorageSets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "StorageSetIds": storage_set_ids,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ZoneId": zone_id,
            "StorageSetName": storage_set_name}
        return self._handle_request(api_request).result

    def describe_storage_set_details(
            self,
            resource_owner_id=None,
            client_token=None,
            page_number=None,
            region_id=None,
            page_size=None,
            storage_set_partition_number=None,
            disk_ids=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            storage_set_id=None):
        api_request = APIRequest('DescribeStorageSetDetails', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "StorageSetPartitionNumber": storage_set_partition_number,
            "DiskIds": disk_ids,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "StorageSetId": storage_set_id}
        return self._handle_request(api_request).result

    def delete_storage_set(
            self,
            resource_owner_id=None,
            client_token=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            storage_set_id=None):
        api_request = APIRequest('DeleteStorageSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "StorageSetId": storage_set_id}
        return self._handle_request(api_request).result

    def create_storage_set(
            self,
            resource_owner_id=None,
            client_token=None,
            max_partition_number=None,
            description=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            zone_id=None,
            storage_set_name=None):
        api_request = APIRequest('CreateStorageSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "MaxPartitionNumber": max_partition_number,
            "Description": description,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ZoneId": zone_id,
            "StorageSetName": storage_set_name}
        return self._handle_request(api_request).result

    def modify_disk_spec(
            self,
            resource_owner_id=None,
            disk_id=None,
            resource_owner_account=None,
            performance_level=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyDiskSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DiskId": disk_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PerformanceLevel": performance_level,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_auto_provisioning_group(
            self,
            resource_owner_id=None,
            terminate_instances_with_expiration=None,
            region_id=None,
            default_target_capacity_type=None,
            excess_capacity_termination_policy=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            auto_provisioning_group_id=None,
            pay_as_you_go_target_capacity=None,
            total_target_capacity=None,
            spot_target_capacity=None,
            max_spot_price=None,
            auto_provisioning_group_name=None):
        api_request = APIRequest('ModifyAutoProvisioningGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TerminateInstancesWithExpiration": terminate_instances_with_expiration,
            "RegionId": region_id,
            "DefaultTargetCapacityType": default_target_capacity_type,
            "ExcessCapacityTerminationPolicy": excess_capacity_termination_policy,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AutoProvisioningGroupId": auto_provisioning_group_id,
            "PayAsYouGoTargetCapacity": pay_as_you_go_target_capacity,
            "TotalTargetCapacity": total_target_capacity,
            "SpotTargetCapacity": spot_target_capacity,
            "MaxSpotPrice": max_spot_price,
            "AutoProvisioningGroupName": auto_provisioning_group_name}
        return self._handle_request(api_request).result

    def describe_auto_provisioning_groups(
            self,
            resource_owner_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            list_of_auto_provisioning_group_status=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            list_of_auto_provisioning_group_id=None,
            auto_provisioning_group_name=None):
        api_request = APIRequest('DescribeAutoProvisioningGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "AutoProvisioningGroupStatus": list_of_auto_provisioning_group_status,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AutoProvisioningGroupId": list_of_auto_provisioning_group_id,
            "AutoProvisioningGroupName": auto_provisioning_group_name}
        repeat_info = {
            "AutoProvisioningGroupStatus": (
                'AutoProvisioningGroupStatus',
                'list',
                'str',
                None),
            "AutoProvisioningGroupId": (
                'AutoProvisioningGroupId',
                'list',
                'str',
                None),
             }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_auto_provisioning_group_instances(
            self,
            resource_owner_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            auto_provisioning_group_id=None):
        api_request = APIRequest('DescribeAutoProvisioningGroupInstances',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AutoProvisioningGroupId": auto_provisioning_group_id}
        return self._handle_request(api_request).result

    def delete_auto_provisioning_group(
            self,
            resource_owner_id=None,
            region_id=None,
            terminate_instances=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            auto_provisioning_group_id=None):
        api_request = APIRequest('DeleteAutoProvisioningGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "TerminateInstances": terminate_instances,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AutoProvisioningGroupId": auto_provisioning_group_id}
        return self._handle_request(api_request).result

    def create_auto_provisioning_group(
            self,
            resource_owner_id=None,
            auto_provisioning_group_type=None,
            description=None,
            terminate_instances_with_expiration=None,
            resource_group_id=None,
            spot_allocation_strategy=None,
            region_id=None,
            terminate_instances=None,
            pay_as_you_go_allocation_strategy=None,
            default_target_capacity_type=None,
            excess_capacity_termination_policy=None,
            list_of_launch_template_config=None,
            valid_until=None,
            spot_instance_interruption_behavior=None,
            launch_template_id=None,
            resource_owner_account=None,
            owner_account=None,
            spot_instance_pools_to_use_count=None,
            owner_id=None,
            launch_template_version=None,
            pay_as_you_go_target_capacity=None,
            total_target_capacity=None,
            spot_target_capacity=None,
            valid_from=None,
            auto_provisioning_group_name=None,
            max_spot_price=None):
        api_request = APIRequest('CreateAutoProvisioningGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AutoProvisioningGroupType": auto_provisioning_group_type,
            "Description": description,
            "TerminateInstancesWithExpiration": terminate_instances_with_expiration,
            "ResourceGroupId": resource_group_id,
            "SpotAllocationStrategy": spot_allocation_strategy,
            "RegionId": region_id,
            "TerminateInstances": terminate_instances,
            "PayAsYouGoAllocationStrategy": pay_as_you_go_allocation_strategy,
            "DefaultTargetCapacityType": default_target_capacity_type,
            "ExcessCapacityTerminationPolicy": excess_capacity_termination_policy,
            "LaunchTemplateConfig": list_of_launch_template_config,
            "ValidUntil": valid_until,
            "SpotInstanceInterruptionBehavior": spot_instance_interruption_behavior,
            "LaunchTemplateId": launch_template_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SpotInstancePoolsToUseCount": spot_instance_pools_to_use_count,
            "OwnerId": owner_id,
            "LaunchTemplateVersion": launch_template_version,
            "PayAsYouGoTargetCapacity": pay_as_you_go_target_capacity,
            "TotalTargetCapacity": total_target_capacity,
            "SpotTargetCapacity": spot_target_capacity,
            "ValidFrom": valid_from,
            "AutoProvisioningGroupName": auto_provisioning_group_name,
            "MaxSpotPrice": max_spot_price}
        repeat_info = {
            "LaunchTemplateConfig": (
                'LaunchTemplateConfig',
                'list',
                'dict',
                [
                    ('InstanceType',
                     'str',
                     None,
                     None),
                    ('MaxPrice',
                     'str',
                     None,
                     None),
                    ('VSwitchId',
                     'str',
                     None,
                     None),
                    ('WeightedCapacity',
                     'str',
                     None,
                     None),
                    ('Priority',
                     'str',
                     None,
                     None),
                    ]),
             }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_auto_provisioning_group_history(
            self,
            resource_owner_id=None,
            start_time=None,
            page_number=None,
            region_id=None,
            page_size=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            owner_id=None,
            auto_provisioning_group_id=None):
        api_request = APIRequest('DescribeAutoProvisioningGroupHistory',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "StartTime": start_time,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "AutoProvisioningGroupId": auto_provisioning_group_id}
        return self._handle_request(api_request).result

    def report_instances_status(
            self,
            reason=None,
            resource_owner_id=None,
            description=None,
            start_time=None,
            region_id=None,
            list_of_disk_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            owner_id=None,
            list_of_instance_id=None,
            list_of_device=None):
        api_request = APIRequest('ReportInstancesStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Reason": reason,
            "ResourceOwnerId": resource_owner_id,
            "Description": description,
            "StartTime": start_time,
            "RegionId": region_id,
            "DiskId": list_of_disk_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "InstanceId": list_of_instance_id,
            "Device": list_of_device}
        repeat_info = {"DiskId": ('DiskId', 'list', 'str', None),
                       "InstanceId": ('InstanceId', 'list', 'str', None),
                       "Device": ('Device', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_fleet(
            self,
            resource_owner_id=None,
            terminate_instances_with_expiration=None,
            on_demand_target_capacity=None,
            region_id=None,
            default_target_capacity_type=None,
            excess_capacity_termination_policy=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            fleet_id=None,
            total_target_capacity=None,
            spot_target_capacity=None,
            max_spot_price=None):
        api_request = APIRequest('ModifyFleet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TerminateInstancesWithExpiration": terminate_instances_with_expiration,
            "OnDemandTargetCapacity": on_demand_target_capacity,
            "RegionId": region_id,
            "DefaultTargetCapacityType": default_target_capacity_type,
            "ExcessCapacityTerminationPolicy": excess_capacity_termination_policy,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FleetId": fleet_id,
            "TotalTargetCapacity": total_target_capacity,
            "SpotTargetCapacity": spot_target_capacity,
            "MaxSpotPrice": max_spot_price}
        return self._handle_request(api_request).result

    def describe_fleets(
            self,
            resource_owner_id=None,
            page_number=None,
            fleet_name=None,
            list_of_fleet_status=None,
            region_id=None,
            page_size=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            list_of_fleet_id=None):
        api_request = APIRequest('DescribeFleets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageNumber": page_number,
            "FleetName": fleet_name,
            "FleetStatus": list_of_fleet_status,
            "RegionId": region_id,
            "PageSize": page_size,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FleetId": list_of_fleet_id}
        repeat_info = {"FleetStatus": ('FleetStatus', 'list', 'str', None),
                       "FleetId": ('FleetId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_fleet_instances(
            self,
            resource_owner_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            fleet_id=None):
        api_request = APIRequest('DescribeFleetInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FleetId": fleet_id}
        return self._handle_request(api_request).result

    def describe_fleet_history(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            fleet_id=None):
        api_request = APIRequest('DescribeFleetHistory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FleetId": fleet_id}
        return self._handle_request(api_request).result

    def delete_fleet(
            self,
            resource_owner_id=None,
            region_id=None,
            terminate_instances=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            fleet_id=None):
        api_request = APIRequest('DeleteFleet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "TerminateInstances": terminate_instances,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FleetId": fleet_id}
        return self._handle_request(api_request).result

    def create_fleet(
            self,
            resource_owner_id=None,
            fleet_type=None,
            description=None,
            terminate_instances_with_expiration=None,
            on_demand_target_capacity=None,
            fleet_name=None,
            spot_allocation_strategy=None,
            region_id=None,
            terminate_instances=None,
            default_target_capacity_type=None,
            excess_capacity_termination_policy=None,
            list_of_launch_template_config=None,
            valid_until=None,
            fill_gap_with_on_demand=None,
            spot_instance_interruption_behavior=None,
            launch_template_id=None,
            resource_owner_account=None,
            owner_account=None,
            spot_instance_pools_to_use_count=None,
            owner_id=None,
            launch_template_version=None,
            total_target_capacity=None,
            on_demand_allocation_strategy=None,
            spot_target_capacity=None,
            valid_from=None,
            max_spot_price=None):
        api_request = APIRequest('CreateFleet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "FleetType": fleet_type,
            "Description": description,
            "TerminateInstancesWithExpiration": terminate_instances_with_expiration,
            "OnDemandTargetCapacity": on_demand_target_capacity,
            "FleetName": fleet_name,
            "SpotAllocationStrategy": spot_allocation_strategy,
            "RegionId": region_id,
            "TerminateInstances": terminate_instances,
            "DefaultTargetCapacityType": default_target_capacity_type,
            "ExcessCapacityTerminationPolicy": excess_capacity_termination_policy,
            "LaunchTemplateConfig": list_of_launch_template_config,
            "ValidUntil": valid_until,
            "FillGapWithOnDemand": fill_gap_with_on_demand,
            "SpotInstanceInterruptionBehavior": spot_instance_interruption_behavior,
            "LaunchTemplateId": launch_template_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SpotInstancePoolsToUseCount": spot_instance_pools_to_use_count,
            "OwnerId": owner_id,
            "LaunchTemplateVersion": launch_template_version,
            "TotalTargetCapacity": total_target_capacity,
            "OnDemandAllocationStrategy": on_demand_allocation_strategy,
            "SpotTargetCapacity": spot_target_capacity,
            "ValidFrom": valid_from,
            "MaxSpotPrice": max_spot_price}
        repeat_info = {
            "LaunchTemplateConfig": (
                'LaunchTemplateConfig',
                'list',
                'dict',
                [
                    ('InstanceType',
                     'str',
                     None,
                     None),
                    ('MaxPrice',
                     'str',
                     None,
                     None),
                    ('VSwitchId',
                     'str',
                     None,
                     None),
                    ('WeightedCapacity',
                     'str',
                     None,
                     None),
                    ('Priority',
                     'str',
                     None,
                     None),
                    ]),
             }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_reserved_instance_attribute(
            self,
            resource_owner_id=None,
            description=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            reserved_instance_id=None,
            reserved_instance_name=None):
        api_request = APIRequest('ModifyReservedInstanceAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Description": description,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ReservedInstanceId": reserved_instance_id,
            "ReservedInstanceName": reserved_instance_name}
        return self._handle_request(api_request).result

    def purchase_reserved_instances_offering(
            self,
            resource_owner_id=None,
            client_token=None,
            description=None,
            resource_group_id=None,
            region_id=None,
            scope=None,
            instance_type=None,
            period=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            period_unit=None,
            offering_type=None,
            zone_id=None,
            reserved_instance_name=None,
            instance_amount=None):
        api_request = APIRequest('PurchaseReservedInstancesOffering', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "Description": description,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "Scope": scope,
            "InstanceType": instance_type,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PeriodUnit": period_unit,
            "OfferingType": offering_type,
            "ZoneId": zone_id,
            "ReservedInstanceName": reserved_instance_name,
            "InstanceAmount": instance_amount}
        return self._handle_request(api_request).result

    def modify_reserved_instances(
            self,
            resource_owner_id=None,
            list_of_configuration=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            list_of_reserved_instance_id=None):
        api_request = APIRequest('ModifyReservedInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Configuration": list_of_configuration,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ReservedInstanceId": list_of_reserved_instance_id}
        repeat_info = {"Configuration": ('Configuration',
                                         'list',
                                         'dict',
                                         [('ZoneId',
                                           'str',
                                           None,
                                           None),
                                          ('ReservedInstanceName',
                                           'str',
                                           None,
                                           None),
                                             ('InstanceType',
                                              'str',
                                              None,
                                              None),
                                             ('Scope',
                                              'str',
                                              None,
                                              None),
                                             ('InstanceAmount',
                                              'str',
                                              None,
                                              None),
                                          ]),
                       "ReservedInstanceId": ('ReservedInstanceId',
                                              'list',
                                              'str',
                                              None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_reserved_instances(
            self,
            resource_owner_id=None,
            page_number=None,
            lock_reason=None,
            region_id=None,
            scope=None,
            page_size=None,
            instance_type=None,
            resource_owner_account=None,
            owner_account=None,
            instance_type_family=None,
            owner_id=None,
            list_of_reserved_instance_id=None,
            offering_type=None,
            zone_id=None,
            reserved_instance_name=None,
            list_of_status=None):
        api_request = APIRequest('DescribeReservedInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageNumber": page_number,
            "LockReason": lock_reason,
            "RegionId": region_id,
            "Scope": scope,
            "PageSize": page_size,
            "InstanceType": instance_type,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "InstanceTypeFamily": instance_type_family,
            "OwnerId": owner_id,
            "ReservedInstanceId": list_of_reserved_instance_id,
            "OfferingType": offering_type,
            "ZoneId": zone_id,
            "ReservedInstanceName": reserved_instance_name,
            "Status": list_of_status}
        repeat_info = {"ReservedInstanceId": ('ReservedInstanceId', 'list', 'str', None),
                       "Status": ('Status', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_demands(
            self,
            resource_owner_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            instance_type=None,
            list_of_tag=None,
            instance_charge_type=None,
            dry_run=None,
            resource_owner_account=None,
            owner_account=None,
            instance_type_family=None,
            owner_id=None,
            list_of_demand_status=None,
            zone_id=None):
        api_request = APIRequest('DescribeDemands', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "InstanceType": instance_type,
            "Tag": list_of_tag,
            "InstanceChargeType": instance_charge_type,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "InstanceTypeFamily": instance_type_family,
            "OwnerId": owner_id,
            "DemandStatus": list_of_demand_status,
            "ZoneId": zone_id}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       "DemandStatus": ('DemandStatus', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def import_snapshot(
            self,
            resource_owner_id=None,
            snapshot_name=None,
            oss_object=None,
            region_id=None,
            oss_bucket=None,
            resource_owner_account=None,
            role_name=None,
            owner_id=None):
        api_request = APIRequest('ImportSnapshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SnapshotName": snapshot_name,
            "OssObject": oss_object,
            "RegionId": region_id,
            "OssBucket": oss_bucket,
            "ResourceOwnerAccount": resource_owner_account,
            "RoleName": role_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def export_snapshot(
            self,
            resource_owner_id=None,
            snapshot_id=None,
            region_id=None,
            oss_bucket=None,
            resource_owner_account=None,
            role_name=None,
            owner_id=None):
        api_request = APIRequest('ExportSnapshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SnapshotId": snapshot_id,
            "RegionId": region_id,
            "OssBucket": oss_bucket,
            "ResourceOwnerAccount": resource_owner_account,
            "RoleName": role_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def untag_resources(
            self,
            resource_owner_id=None,
            region_id=None,
            all_=None,
            list_of_resource_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            resource_type=None,
            list_of_tag_key=None):
        api_request = APIRequest('UntagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "All": all_,
            "ResourceId": list_of_resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ResourceType": resource_type,
            "TagKey": list_of_tag_key}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "TagKey": ('TagKey', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def tag_resources(
            self,
            region_id=None,
            list_of_tag=None,
            list_of_resource_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('TagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "Tag": list_of_tag,
            "ResourceId": list_of_resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       "ResourceId": ('ResourceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_tag_resources(
            self,
            resource_owner_id=None,
            region_id=None,
            next_token=None,
            list_of_tag=None,
            list_of_resource_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('ListTagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "NextToken": next_token,
            "Tag": list_of_tag,
            "ResourceId": list_of_resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       "ResourceId": ('ResourceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def accept_inquired_system_event(
            self,
            event_id=None,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('AcceptInquiredSystemEvent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EventId": event_id,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def redeploy_instance(
            self,
            resource_owner_id=None,
            force_stop=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            instance_id=None):
        api_request = APIRequest('RedeployInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ForceStop": force_stop,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def unassign_ipv6_addresses(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            network_interface_id=None,
            list_of_ipv6_address=None):
        api_request = APIRequest('UnassignIpv6Addresses', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NetworkInterfaceId": network_interface_id,
            "Ipv6Address": list_of_ipv6_address}
        repeat_info = {"Ipv6Address": ('Ipv6Address', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def assign_ipv6_addresses(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            ipv6_address_count=None,
            owner_account=None,
            owner_id=None,
            network_interface_id=None,
            list_of_ipv6_address=None):
        api_request = APIRequest('AssignIpv6Addresses', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Ipv6AddressCount": ipv6_address_count,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NetworkInterfaceId": network_interface_id,
            "Ipv6Address": list_of_ipv6_address}
        repeat_info = {"Ipv6Address": ('Ipv6Address', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_instance_topology(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            instance_ids=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceTopology', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "InstanceIds": instance_ids,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def renew_dedicated_hosts(
            self,
            dedicated_host_ids=None,
            resource_owner_id=None,
            client_token=None,
            region_id=None,
            period=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            period_unit=None):
        api_request = APIRequest('RenewDedicatedHosts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DedicatedHostIds": dedicated_host_ids,
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "RegionId": region_id,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PeriodUnit": period_unit}
        return self._handle_request(api_request).result

    def release_dedicated_host(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            dedicated_host_id=None,
            owner_id=None):
        api_request = APIRequest('ReleaseDedicatedHost', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DedicatedHostId": dedicated_host_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_instance_deployment(
            self,
            resource_owner_id=None,
            region_id=None,
            deployment_set_id=None,
            resource_owner_account=None,
            owner_account=None,
            tenancy=None,
            dedicated_host_id=None,
            owner_id=None,
            instance_id=None,
            force=None,
            migration_type=None,
            affinity=None):
        api_request = APIRequest('ModifyInstanceDeployment', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "DeploymentSetId": deployment_set_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Tenancy": tenancy,
            "DedicatedHostId": dedicated_host_id,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "Force": force,
            "MigrationType": migration_type,
            "Affinity": affinity}
        return self._handle_request(api_request).result

    def modify_dedicated_host_auto_renew_attribute(
            self,
            duration=None,
            dedicated_host_ids=None,
            resource_owner_id=None,
            period_unit=None,
            auto_renew=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            renewal_status=None,
            owner_id=None):
        api_request = APIRequest('ModifyDedicatedHostAutoRenewAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "DedicatedHostIds": dedicated_host_ids,
            "ResourceOwnerId": resource_owner_id,
            "PeriodUnit": period_unit,
            "AutoRenew": auto_renew,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "RenewalStatus": renewal_status,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_dedicated_host_auto_release_time(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            auto_release_time=None,
            dedicated_host_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyDedicatedHostAutoReleaseTime',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "AutoReleaseTime": auto_release_time,
            "DedicatedHostId": dedicated_host_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_dedicated_host_attribute(
            self,
            resource_owner_id=None,
            description=None,
            region_id=None,
            action_on_maintenance=None,
            dedicated_host_name=None,
            resource_owner_account=None,
            owner_account=None,
            dedicated_host_id=None,
            owner_id=None,
            network_attributes_slb_udp_timeout=None,
            auto_placement=None,
            network_attributes_udp_timeout=None):
        api_request = APIRequest('ModifyDedicatedHostAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Description": description,
            "RegionId": region_id,
            "ActionOnMaintenance": action_on_maintenance,
            "DedicatedHostName": dedicated_host_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DedicatedHostId": dedicated_host_id,
            "OwnerId": owner_id,
            "NetworkAttributes.SlbUdpTimeout": network_attributes_slb_udp_timeout,
            "AutoPlacement": auto_placement,
            "NetworkAttributes.UdpTimeout": network_attributes_udp_timeout}
        return self._handle_request(api_request).result

    def describe_dedicated_hosts(
            self,
            dedicated_host_ids=None,
            resource_owner_id=None,
            dedicated_host_name=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            page_number=None,
            resource_group_id=None,
            lock_reason=None,
            region_id=None,
            page_size=None,
            zone_id=None,
            dedicated_host_type=None,
            list_of_tag=None,
            status=None):
        api_request = APIRequest('DescribeDedicatedHosts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DedicatedHostIds": dedicated_host_ids,
            "ResourceOwnerId": resource_owner_id,
            "DedicatedHostName": dedicated_host_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "ResourceGroupId": resource_group_id,
            "LockReason": lock_reason,
            "RegionId": region_id,
            "PageSize": page_size,
            "ZoneId": zone_id,
            "DedicatedHostType": dedicated_host_type,
            "Tag": list_of_tag,
            "Status": status}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_dedicated_host_types(
            self,
            resource_owner_id=None,
            supported_instance_type_family=None,
            region_id=None,
            dedicated_host_type=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeDedicatedHostTypes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SupportedInstanceTypeFamily": supported_instance_type_family,
            "RegionId": region_id,
            "DedicatedHostType": dedicated_host_type,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dedicated_host_auto_renew(
            self,
            dedicated_host_ids=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeDedicatedHostAutoRenew', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DedicatedHostIds": dedicated_host_ids,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def allocate_dedicated_hosts(
            self,
            resource_owner_id=None,
            client_token=None,
            description=None,
            resource_group_id=None,
            region_id=None,
            action_on_maintenance=None,
            list_of_tag=None,
            dedicated_host_type=None,
            auto_renew_period=None,
            period=None,
            quantity=None,
            dedicated_host_name=None,
            resource_owner_account=None,
            owner_account=None,
            auto_release_time=None,
            owner_id=None,
            period_unit=None,
            auto_renew=None,
            network_attributes_slb_udp_timeout=None,
            zone_id=None,
            auto_placement=None,
            charge_type=None,
            network_attributes_udp_timeout=None):
        api_request = APIRequest('AllocateDedicatedHosts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "Description": description,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "ActionOnMaintenance": action_on_maintenance,
            "Tag": list_of_tag,
            "DedicatedHostType": dedicated_host_type,
            "AutoRenewPeriod": auto_renew_period,
            "Period": period,
            "Quantity": quantity,
            "DedicatedHostName": dedicated_host_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AutoReleaseTime": auto_release_time,
            "OwnerId": owner_id,
            "PeriodUnit": period_unit,
            "AutoRenew": auto_renew,
            "NetworkAttributes.SlbUdpTimeout": network_attributes_slb_udp_timeout,
            "ZoneId": zone_id,
            "AutoPlacement": auto_placement,
            "ChargeType": charge_type,
            "NetworkAttributes.UdpTimeout": network_attributes_udp_timeout}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_simulated_system_events(
            self,
            resource_owner_id=None,
            not_before=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            list_of_instance_id=None,
            event_type=None):
        api_request = APIRequest('CreateSimulatedSystemEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "NotBefore": not_before,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": list_of_instance_id,
            "EventType": event_type}
        repeat_info = {"InstanceId": ('InstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def cancel_simulated_system_events(
            self,
            list_of_event_id=None,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CancelSimulatedSystemEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EventId": list_of_event_id,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        repeat_info = {"EventId": ('EventId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_eni_monitor_data(
            self,
            resource_owner_id=None,
            start_time=None,
            region_id=None,
            period=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            owner_id=None,
            instance_id=None,
            eni_id=None):
        api_request = APIRequest('DescribeEniMonitorData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "StartTime": start_time,
            "RegionId": region_id,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "EniId": eni_id}
        return self._handle_request(api_request).result

    def describe_account_attributes(
            self,
            resource_owner_id=None,
            list_of_attribute_name=None,
            region_id=None,
            resource_owner_account=None,
            owner_id=None,
            zone_id=None):
        api_request = APIRequest('DescribeAccountAttributes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AttributeName": list_of_attribute_name,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "ZoneId": zone_id}
        repeat_info = {"AttributeName": ('AttributeName', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_launch_template_default_version(
            self,
            launch_template_name=None,
            resource_owner_id=None,
            region_id=None,
            launch_template_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            default_version_number=None):
        api_request = APIRequest('ModifyLaunchTemplateDefaultVersion',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LaunchTemplateName": launch_template_name,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "LaunchTemplateId": launch_template_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "DefaultVersionNumber": default_version_number}
        return self._handle_request(api_request).result

    def describe_launch_templates(
            self,
            list_of_launch_template_name=None,
            resource_owner_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            list_of_template_tag=None,
            list_of_launch_template_id=None,
            resource_owner_account=None,
            owner_account=None,
            template_resource_group_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeLaunchTemplates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LaunchTemplateName": list_of_launch_template_name,
            "ResourceOwnerId": resource_owner_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "TemplateTag": list_of_template_tag,
            "LaunchTemplateId": list_of_launch_template_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "TemplateResourceGroupId": template_resource_group_id,
            "OwnerId": owner_id}
        repeat_info = {"LaunchTemplateName": ('LaunchTemplateName', 'list', 'str', None),
                       "TemplateTag": ('TemplateTag', 'list', 'dict', [('Key', 'str', None, None),
                                                                       ('Value', 'str', None, None),
                                                                       ]),
                       "LaunchTemplateId": ('LaunchTemplateId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_launch_template_versions(
            self,
            launch_template_name=None,
            max_version=None,
            resource_owner_id=None,
            default_version=None,
            min_version=None,
            page_number=None,
            region_id=None,
            page_size=None,
            launch_template_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            list_of_launch_template_version=None,
            detail_flag=None):
        api_request = APIRequest('DescribeLaunchTemplateVersions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LaunchTemplateName": launch_template_name,
            "MaxVersion": max_version,
            "ResourceOwnerId": resource_owner_id,
            "DefaultVersion": default_version,
            "MinVersion": min_version,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "LaunchTemplateId": launch_template_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "LaunchTemplateVersion": list_of_launch_template_version,
            "DetailFlag": detail_flag}
        repeat_info = {"LaunchTemplateVersion": ('LaunchTemplateVersion', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_launch_template_version(
            self,
            launch_template_name=None,
            resource_owner_id=None,
            list_of_delete_version=None,
            region_id=None,
            launch_template_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteLaunchTemplateVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LaunchTemplateName": launch_template_name,
            "ResourceOwnerId": resource_owner_id,
            "DeleteVersion": list_of_delete_version,
            "RegionId": region_id,
            "LaunchTemplateId": launch_template_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        repeat_info = {"DeleteVersion": ('DeleteVersion', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_launch_template(
            self,
            launch_template_name=None,
            resource_owner_id=None,
            region_id=None,
            launch_template_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteLaunchTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LaunchTemplateName": launch_template_name,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "LaunchTemplateId": launch_template_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_launch_template_version(
            self,
            launch_template_name=None,
            resource_owner_id=None,
            security_enhancement_strategy=None,
            network_type=None,
            key_pair_name=None,
            spot_price_limit=None,
            image_owner_alias=None,
            resource_group_id=None,
            host_name=None,
            system_disk_iops=None,
            list_of_tag=None,
            period=None,
            launch_template_id=None,
            owner_id=None,
            vswitch_id=None,
            spot_strategy=None,
            instance_name=None,
            internet_charge_type=None,
            zone_id=None,
            internet_max_bandwidth_in=None,
            version_description=None,
            image_id=None,
            io_optimized=None,
            security_group_id=None,
            internet_max_bandwidth_out=None,
            description=None,
            system_disk_category=None,
            user_data=None,
            password_inherit=None,
            region_id=None,
            instance_type=None,
            instance_charge_type=None,
            enable_vm_os_config=None,
            list_of_network_interface=None,
            resource_owner_account=None,
            owner_account=None,
            system_disk_disk_name=None,
            ram_role_name=None,
            auto_release_time=None,
            spot_duration=None,
            list_of_data_disk=None,
            system_disk_size=None,
            vpc_id=None,
            system_disk_description=None):
        api_request = APIRequest('CreateLaunchTemplateVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LaunchTemplateName": launch_template_name,
            "ResourceOwnerId": resource_owner_id,
            "SecurityEnhancementStrategy": security_enhancement_strategy,
            "NetworkType": network_type,
            "KeyPairName": key_pair_name,
            "SpotPriceLimit": spot_price_limit,
            "ImageOwnerAlias": image_owner_alias,
            "ResourceGroupId": resource_group_id,
            "HostName": host_name,
            "SystemDisk.Iops": system_disk_iops,
            "Tag": list_of_tag,
            "Period": period,
            "LaunchTemplateId": launch_template_id,
            "OwnerId": owner_id,
            "VSwitchId": vswitch_id,
            "SpotStrategy": spot_strategy,
            "InstanceName": instance_name,
            "InternetChargeType": internet_charge_type,
            "ZoneId": zone_id,
            "InternetMaxBandwidthIn": internet_max_bandwidth_in,
            "VersionDescription": version_description,
            "ImageId": image_id,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "InternetMaxBandwidthOut": internet_max_bandwidth_out,
            "Description": description,
            "SystemDisk.Category": system_disk_category,
            "UserData": user_data,
            "PasswordInherit": password_inherit,
            "RegionId": region_id,
            "InstanceType": instance_type,
            "InstanceChargeType": instance_charge_type,
            "EnableVmOsConfig": enable_vm_os_config,
            "NetworkInterface": list_of_network_interface,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SystemDisk.DiskName": system_disk_disk_name,
            "RamRoleName": ram_role_name,
            "AutoReleaseTime": auto_release_time,
            "SpotDuration": spot_duration,
            "DataDisk": list_of_data_disk,
            "SystemDisk.Size": system_disk_size,
            "VpcId": vpc_id,
            "SystemDisk.Description": system_disk_description}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       "NetworkInterface": ('NetworkInterface', 'list', 'dict', [('PrimaryIpAddress', 'str', None, None),
                                                                                 ('VSwitchId', 'str', None, None),
                                                                                 ('SecurityGroupId', 'str', None, None),
                                                                                 ('NetworkInterfaceName', 'str', None, None),
                                                                                 ('Description', 'str', None, None),
                                                                                 ]),
                       "DataDisk": ('DataDisk', 'list', 'dict', [('Size', 'str', None, None),
                                                                 ('SnapshotId', 'str', None, None),
                                                                 ('Category', 'str', None, None),
                                                                 ('Encrypted', 'str', None, None),
                                                                 ('DiskName', 'str', None, None),
                                                                 ('Description', 'str', None, None),
                                                                 ('DeleteWithInstance', 'str', None, None),
                                                                 ('Device', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_launch_template(
            self,
            launch_template_name=None,
            resource_owner_id=None,
            security_enhancement_strategy=None,
            network_type=None,
            key_pair_name=None,
            spot_price_limit=None,
            image_owner_alias=None,
            resource_group_id=None,
            host_name=None,
            system_disk_iops=None,
            list_of_template_tag=None,
            list_of_tag=None,
            period=None,
            template_resource_group_id=None,
            owner_id=None,
            vswitch_id=None,
            spot_strategy=None,
            instance_name=None,
            internet_charge_type=None,
            zone_id=None,
            internet_max_bandwidth_in=None,
            version_description=None,
            image_id=None,
            io_optimized=None,
            security_group_id=None,
            internet_max_bandwidth_out=None,
            description=None,
            system_disk_category=None,
            user_data=None,
            password_inherit=None,
            region_id=None,
            instance_type=None,
            instance_charge_type=None,
            enable_vm_os_config=None,
            list_of_network_interface=None,
            resource_owner_account=None,
            owner_account=None,
            system_disk_disk_name=None,
            ram_role_name=None,
            auto_release_time=None,
            spot_duration=None,
            list_of_data_disk=None,
            system_disk_size=None,
            vpc_id=None,
            system_disk_description=None):
        api_request = APIRequest('CreateLaunchTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LaunchTemplateName": launch_template_name,
            "ResourceOwnerId": resource_owner_id,
            "SecurityEnhancementStrategy": security_enhancement_strategy,
            "NetworkType": network_type,
            "KeyPairName": key_pair_name,
            "SpotPriceLimit": spot_price_limit,
            "ImageOwnerAlias": image_owner_alias,
            "ResourceGroupId": resource_group_id,
            "HostName": host_name,
            "SystemDisk.Iops": system_disk_iops,
            "TemplateTag": list_of_template_tag,
            "Tag": list_of_tag,
            "Period": period,
            "TemplateResourceGroupId": template_resource_group_id,
            "OwnerId": owner_id,
            "VSwitchId": vswitch_id,
            "SpotStrategy": spot_strategy,
            "InstanceName": instance_name,
            "InternetChargeType": internet_charge_type,
            "ZoneId": zone_id,
            "InternetMaxBandwidthIn": internet_max_bandwidth_in,
            "VersionDescription": version_description,
            "ImageId": image_id,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "InternetMaxBandwidthOut": internet_max_bandwidth_out,
            "Description": description,
            "SystemDisk.Category": system_disk_category,
            "UserData": user_data,
            "PasswordInherit": password_inherit,
            "RegionId": region_id,
            "InstanceType": instance_type,
            "InstanceChargeType": instance_charge_type,
            "EnableVmOsConfig": enable_vm_os_config,
            "NetworkInterface": list_of_network_interface,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SystemDisk.DiskName": system_disk_disk_name,
            "RamRoleName": ram_role_name,
            "AutoReleaseTime": auto_release_time,
            "SpotDuration": spot_duration,
            "DataDisk": list_of_data_disk,
            "SystemDisk.Size": system_disk_size,
            "VpcId": vpc_id,
            "SystemDisk.Description": system_disk_description}
        repeat_info = {"TemplateTag": ('TemplateTag', 'list', 'dict', [('Key', 'str', None, None),
                                                                       ('Value', 'str', None, None),
                                                                       ]),
                       "Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       "NetworkInterface": ('NetworkInterface', 'list', 'dict', [('PrimaryIpAddress', 'str', None, None),
                                                                                 ('VSwitchId', 'str', None, None),
                                                                                 ('SecurityGroupId', 'str', None, None),
                                                                                 ('NetworkInterfaceName', 'str', None, None),
                                                                                 ('Description', 'str', None, None),
                                                                                 ]),
                       "DataDisk": ('DataDisk', 'list', 'dict', [('Size', 'str', None, None),
                                                                 ('SnapshotId', 'str', None, None),
                                                                 ('Category', 'str', None, None),
                                                                 ('Encrypted', 'str', None, None),
                                                                 ('DiskName', 'str', None, None),
                                                                 ('Description', 'str', None, None),
                                                                 ('DeleteWithInstance', 'str', None, None),
                                                                 ('Device', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def install_cloud_assistant(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            list_of_instance_id=None):
        api_request = APIRequest('InstallCloudAssistant', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": list_of_instance_id}
        repeat_info = {"InstanceId": ('InstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_cloud_assistant_status(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            list_of_instance_id=None):
        api_request = APIRequest('DescribeCloudAssistantStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": list_of_instance_id}
        repeat_info = {"InstanceId": ('InstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def unassign_private_ip_addresses(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            list_of_private_ip_address=None,
            network_interface_id=None):
        api_request = APIRequest('UnassignPrivateIpAddresses', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PrivateIpAddress": list_of_private_ip_address,
            "NetworkInterfaceId": network_interface_id}
        repeat_info = {"PrivateIpAddress": ('PrivateIpAddress', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def assign_private_ip_addresses(
            self,
            resource_owner_id=None,
            secondary_private_ip_address_count=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            list_of_private_ip_address=None,
            network_interface_id=None):
        api_request = APIRequest('AssignPrivateIpAddresses', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecondaryPrivateIpAddressCount": secondary_private_ip_address_count,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PrivateIpAddress": list_of_private_ip_address,
            "NetworkInterfaceId": network_interface_id}
        repeat_info = {"PrivateIpAddress": ('PrivateIpAddress', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_network_interface_permissions(
            self,
            resource_owner_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            list_of_network_interface_permission_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            network_interface_id=None):
        api_request = APIRequest('DescribeNetworkInterfacePermissions',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "NetworkInterfacePermissionId": list_of_network_interface_permission_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NetworkInterfaceId": network_interface_id}
        repeat_info = {
            "NetworkInterfacePermissionId": (
                'NetworkInterfacePermissionId',
                'list',
                'str',
                None),
         }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_network_interface_permission(
            self,
            resource_owner_id=None,
            region_id=None,
            network_interface_permission_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            force=None):
        api_request = APIRequest('DeleteNetworkInterfacePermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "NetworkInterfacePermissionId": network_interface_permission_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Force": force}
        return self._handle_request(api_request).result

    def create_network_interface_permission(
            self,
            resource_owner_id=None,
            account_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            permission=None,
            owner_id=None,
            network_interface_id=None):
        api_request = APIRequest('CreateNetworkInterfacePermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountId": account_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Permission": permission,
            "OwnerId": owner_id,
            "NetworkInterfaceId": network_interface_id}
        return self._handle_request(api_request).result

    def get_instance_screenshot(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            wake_up=None,
            owner_account=None,
            owner_id=None,
            instance_id=None):
        api_request = APIRequest('GetInstanceScreenshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "WakeUp": wake_up,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def get_instance_console_output(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            instance_id=None):
        api_request = APIRequest('GetInstanceConsoleOutput', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def describe_resources_modification(
            self,
            resource_owner_id=None,
            memory=None,
            cores=None,
            region_id=None,
            migrate_across_zone=None,
            instance_type=None,
            resource_id=None,
            resource_owner_account=None,
            owner_account=None,
            operation_type=None,
            owner_id=None,
            destination_resource=None):
        api_request = APIRequest('DescribeResourcesModification', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Memory": memory,
            "Cores": cores,
            "RegionId": region_id,
            "MigrateAcrossZone": migrate_across_zone,
            "InstanceType": instance_type,
            "ResourceId": resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OperationType": operation_type,
            "OwnerId": owner_id,
            "DestinationResource": destination_resource}
        return self._handle_request(api_request).result

    def describe_bandwidth_limitation(
            self,
            resource_owner_id=None,
            region_id=None,
            instance_type=None,
            instance_charge_type=None,
            resource_id=None,
            resource_owner_account=None,
            owner_account=None,
            operation_type=None,
            owner_id=None,
            spot_strategy=None):
        api_request = APIRequest('DescribeBandwidthLimitation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "InstanceType": instance_type,
            "InstanceChargeType": instance_charge_type,
            "ResourceId": resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OperationType": operation_type,
            "OwnerId": owner_id,
            "SpotStrategy": spot_strategy}
        return self._handle_request(api_request).result

    def describe_available_resource(
            self,
            resource_owner_id=None,
            memory=None,
            io_optimized=None,
            data_disk_category=None,
            cores=None,
            region_id=None,
            system_disk_category=None,
            scope=None,
            instance_type=None,
            network_category=None,
            instance_charge_type=None,
            resource_owner_account=None,
            owner_account=None,
            dedicated_host_id=None,
            owner_id=None,
            resource_type=None,
            spot_strategy=None,
            destination_resource=None,
            zone_id=None):
        api_request = APIRequest('DescribeAvailableResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Memory": memory,
            "IoOptimized": io_optimized,
            "DataDiskCategory": data_disk_category,
            "Cores": cores,
            "RegionId": region_id,
            "SystemDiskCategory": system_disk_category,
            "Scope": scope,
            "InstanceType": instance_type,
            "NetworkCategory": network_category,
            "InstanceChargeType": instance_charge_type,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DedicatedHostId": dedicated_host_id,
            "OwnerId": owner_id,
            "ResourceType": resource_type,
            "SpotStrategy": spot_strategy,
            "DestinationResource": destination_resource,
            "ZoneId": zone_id}
        return self._handle_request(api_request).result

    def reactivate_instances(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ReActivateInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instances_full_status(
            self,
            list_of_event_id=None,
            resource_owner_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            event_publish_time_end=None,
            list_of_instance_event_type=None,
            resource_owner_account=None,
            owner_account=None,
            not_before_start=None,
            owner_id=None,
            event_publish_time_start=None,
            list_of_instance_id=None,
            not_before_end=None,
            health_status=None,
            event_type=None,
            status=None):
        api_request = APIRequest('DescribeInstancesFullStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EventId": list_of_event_id,
            "ResourceOwnerId": resource_owner_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "EventPublishTime.End": event_publish_time_end,
            "InstanceEventType": list_of_instance_event_type,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "NotBefore.Start": not_before_start,
            "OwnerId": owner_id,
            "EventPublishTime.Start": event_publish_time_start,
            "InstanceId": list_of_instance_id,
            "NotBefore.End": not_before_end,
            "HealthStatus": health_status,
            "EventType": event_type,
            "Status": status}
        repeat_info = {"EventId": ('EventId', 'list', 'str', None),
                       "InstanceEventType": ('InstanceEventType', 'list', 'str', None),
                       "InstanceId": ('InstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_instance_history_events(
            self,
            list_of_event_id=None,
            resource_owner_id=None,
            event_cycle_status=None,
            page_number=None,
            region_id=None,
            page_size=None,
            list_of_instance_event_cycle_status=None,
            event_publish_time_end=None,
            list_of_instance_event_type=None,
            resource_owner_account=None,
            owner_account=None,
            not_before_start=None,
            owner_id=None,
            event_publish_time_start=None,
            instance_id=None,
            not_before_end=None,
            event_type=None):
        api_request = APIRequest('DescribeInstanceHistoryEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EventId": list_of_event_id,
            "ResourceOwnerId": resource_owner_id,
            "EventCycleStatus": event_cycle_status,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "InstanceEventCycleStatus": list_of_instance_event_cycle_status,
            "EventPublishTime.End": event_publish_time_end,
            "InstanceEventType": list_of_instance_event_type,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "NotBefore.Start": not_before_start,
            "OwnerId": owner_id,
            "EventPublishTime.Start": event_publish_time_start,
            "InstanceId": instance_id,
            "NotBefore.End": not_before_end,
            "EventType": event_type}
        repeat_info = {
            "EventId": (
                'EventId', 'list', 'str', None), "InstanceEventCycleStatus": (
                'InstanceEventCycleStatus', 'list', 'str', None), "InstanceEventType": (
                'InstanceEventType', 'list', 'str', None), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_disks_full_status(
            self,
            list_of_event_id=None,
            resource_owner_id=None,
            page_number=None,
            event_time_start=None,
            region_id=None,
            page_size=None,
            list_of_disk_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            event_time_end=None,
            health_status=None,
            event_type=None,
            status=None):
        api_request = APIRequest('DescribeDisksFullStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EventId": list_of_event_id,
            "ResourceOwnerId": resource_owner_id,
            "PageNumber": page_number,
            "EventTime.Start": event_time_start,
            "RegionId": region_id,
            "PageSize": page_size,
            "DiskId": list_of_disk_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "EventTime.End": event_time_end,
            "HealthStatus": health_status,
            "EventType": event_type,
            "Status": status}
        repeat_info = {"EventId": ('EventId', 'list', 'str', None),
                       "DiskId": ('DiskId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_user_business_behavior(
            self,
            resource_owner_id=None,
            region_id=None,
            status_value=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            status_key=None):
        api_request = APIRequest('ModifyUserBusinessBehavior', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "statusValue": status_value,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "statusKey": status_key}
        return self._handle_request(api_request).result

    def describe_user_business_behavior(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            status_key=None):
        api_request = APIRequest('DescribeUserBusinessBehavior', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "statusKey": status_key}
        return self._handle_request(api_request).result

    def run_instances(
            self,
            launch_template_name=None,
            resource_owner_id=None,
            unique_suffix=None,
            hpc_cluster_id=None,
            security_enhancement_strategy=None,
            key_pair_name=None,
            min_amount=None,
            spot_price_limit=None,
            deletion_protection=None,
            resource_group_id=None,
            host_name=None,
            password=None,
            storage_set_partition_number=None,
            list_of_tag=None,
            auto_renew_period=None,
            period=None,
            dry_run=None,
            launch_template_id=None,
            ipv6_address_count=None,
            owner_id=None,
            capacity_reservation_preference=None,
            vswitch_id=None,
            spot_strategy=None,
            private_ip_address=None,
            period_unit=None,
            instance_name=None,
            auto_renew=None,
            internet_charge_type=None,
            zone_id=None,
            list_of_ipv6_address=None,
            internet_max_bandwidth_in=None,
            affinity=None,
            image_id=None,
            spot_interruption_behavior=None,
            client_token=None,
            io_optimized=None,
            security_group_id=None,
            internet_max_bandwidth_out=None,
            description=None,
            system_disk_category=None,
            capacity_reservation_id=None,
            system_disk_performance_level=None,
            user_data=None,
            password_inherit=None,
            region_id=None,
            instance_type=None,
            hibernation_configured=None,
            instance_charge_type=None,
            list_of_network_interface=None,
            deployment_set_id=None,
            amount=None,
            resource_owner_account=None,
            owner_account=None,
            tenancy=None,
            system_disk_disk_name=None,
            ram_role_name=None,
            auto_release_time=None,
            dedicated_host_id=None,
            credit_specification=None,
            list_of_security_group_ids=None,
            list_of_data_disk=None,
            launch_template_version=None,
            storage_set_id=None,
            system_disk_size=None,
            system_disk_description=None):
        api_request = APIRequest('RunInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LaunchTemplateName": launch_template_name,
            "ResourceOwnerId": resource_owner_id,
            "UniqueSuffix": unique_suffix,
            "HpcClusterId": hpc_cluster_id,
            "SecurityEnhancementStrategy": security_enhancement_strategy,
            "KeyPairName": key_pair_name,
            "MinAmount": min_amount,
            "SpotPriceLimit": spot_price_limit,
            "DeletionProtection": deletion_protection,
            "ResourceGroupId": resource_group_id,
            "HostName": host_name,
            "Password": password,
            "StorageSetPartitionNumber": storage_set_partition_number,
            "Tag": list_of_tag,
            "AutoRenewPeriod": auto_renew_period,
            "Period": period,
            "DryRun": dry_run,
            "LaunchTemplateId": launch_template_id,
            "Ipv6AddressCount": ipv6_address_count,
            "OwnerId": owner_id,
            "CapacityReservationPreference": capacity_reservation_preference,
            "VSwitchId": vswitch_id,
            "SpotStrategy": spot_strategy,
            "PrivateIpAddress": private_ip_address,
            "PeriodUnit": period_unit,
            "InstanceName": instance_name,
            "AutoRenew": auto_renew,
            "InternetChargeType": internet_charge_type,
            "ZoneId": zone_id,
            "Ipv6Address": list_of_ipv6_address,
            "InternetMaxBandwidthIn": internet_max_bandwidth_in,
            "Affinity": affinity,
            "ImageId": image_id,
            "SpotInterruptionBehavior": spot_interruption_behavior,
            "ClientToken": client_token,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "InternetMaxBandwidthOut": internet_max_bandwidth_out,
            "Description": description,
            "SystemDisk.Category": system_disk_category,
            "CapacityReservationId": capacity_reservation_id,
            "SystemDisk.PerformanceLevel": system_disk_performance_level,
            "UserData": user_data,
            "PasswordInherit": password_inherit,
            "RegionId": region_id,
            "InstanceType": instance_type,
            "HibernationConfigured": hibernation_configured,
            "InstanceChargeType": instance_charge_type,
            "NetworkInterface": list_of_network_interface,
            "DeploymentSetId": deployment_set_id,
            "Amount": amount,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Tenancy": tenancy,
            "SystemDisk.DiskName": system_disk_disk_name,
            "RamRoleName": ram_role_name,
            "AutoReleaseTime": auto_release_time,
            "DedicatedHostId": dedicated_host_id,
            "CreditSpecification": credit_specification,
            "SecurityGroupIds": list_of_security_group_ids,
            "DataDisk": list_of_data_disk,
            "LaunchTemplateVersion": launch_template_version,
            "StorageSetId": storage_set_id,
            "SystemDisk.Size": system_disk_size,
            "SystemDisk.Description": system_disk_description}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       "Ipv6Address": ('Ipv6Address', 'list', 'str', None),
                       "NetworkInterface": ('NetworkInterface', 'list', 'dict', [('PrimaryIpAddress', 'str', None, None),
                                                                                 ('VSwitchId', 'str', None, None),
                                                                                 ('SecurityGroupId', 'str', None, None),
                                                                                 ('NetworkInterfaceName', 'str', None, None),
                                                                                 ('Description', 'str', None, None),
                                                                                 ]),
                       "SecurityGroupIds": ('SecurityGroupIds', 'list', 'str', None),
                       "DataDisk": ('DataDisk', 'list', 'dict', [('Size', 'str', None, None),
                                                                 ('SnapshotId', 'str', None, None),
                                                                 ('Category', 'str', None, None),
                                                                 ('Encrypted', 'str', None, None),
                                                                 ('KMSKeyId', 'str', None, None),
                                                                 ('DiskName', 'str', None, None),
                                                                 ('Description', 'str', None, None),
                                                                 ('Device', 'str', None, None),
                                                                 ('DeleteWithInstance', 'str', None, None),
                                                                 ('PerformanceLevel', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def convert_nat_public_ip_to_eip(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_id=None,
            instance_id=None):
        api_request = APIRequest('ConvertNatPublicIpToEip', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def modify_hpc_cluster_attribute(
            self,
            resource_owner_id=None,
            hpc_cluster_id=None,
            client_token=None,
            description=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            name=None):
        api_request = APIRequest('ModifyHpcClusterAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HpcClusterId": hpc_cluster_id,
            "ClientToken": client_token,
            "Description": description,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Name": name}
        return self._handle_request(api_request).result

    def describe_hpc_clusters(
            self,
            resource_owner_id=None,
            client_token=None,
            page_number=None,
            region_id=None,
            page_size=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            hpc_cluster_ids=None):
        api_request = APIRequest('DescribeHpcClusters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "HpcClusterIds": hpc_cluster_ids}
        return self._handle_request(api_request).result

    def delete_hpc_cluster(
            self,
            resource_owner_id=None,
            hpc_cluster_id=None,
            client_token=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteHpcCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HpcClusterId": hpc_cluster_id,
            "ClientToken": client_token,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_hpc_cluster(
            self,
            resource_owner_id=None,
            client_token=None,
            description=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            name=None):
        api_request = APIRequest('CreateHpcCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "Description": description,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Name": name}
        return self._handle_request(api_request).result

    def describe_snapshots_usage(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeSnapshotsUsage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_spot_price_history(
            self,
            resource_owner_id=None,
            io_optimized=None,
            network_type=None,
            start_time=None,
            region_id=None,
            instance_type=None,
            offset=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            os_type=None,
            owner_id=None,
            zone_id=None):
        api_request = APIRequest('DescribeSpotPriceHistory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "IoOptimized": io_optimized,
            "NetworkType": network_type,
            "StartTime": start_time,
            "RegionId": region_id,
            "InstanceType": instance_type,
            "Offset": offset,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "OSType": os_type,
            "OwnerId": owner_id,
            "ZoneId": zone_id}
        return self._handle_request(api_request).result

    def stop_invocation(
            self,
            resource_owner_id=None,
            region_id=None,
            invoke_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            list_of_instance_id=None):
        api_request = APIRequest('StopInvocation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "InvokeId": invoke_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": list_of_instance_id}
        repeat_info = {"InstanceId": ('InstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_command(
            self,
            resource_owner_id=None,
            working_dir=None,
            description=None,
            command_id=None,
            command_content=None,
            timeout=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            name=None):
        api_request = APIRequest('ModifyCommand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "WorkingDir": working_dir,
            "Description": description,
            "CommandId": command_id,
            "CommandContent": command_content,
            "Timeout": timeout,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Name": name}
        return self._handle_request(api_request).result

    def invoke_command(
            self,
            resource_owner_id=None,
            command_id=None,
            frequency=None,
            region_id=None,
            timed=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            list_of_instance_id=None,
            parameters=None):
        api_request = APIRequest('InvokeCommand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "CommandId": command_id,
            "Frequency": frequency,
            "RegionId": region_id,
            "Timed": timed,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": list_of_instance_id,
            "Parameters": parameters}
        repeat_info = {"InstanceId": ('InstanceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_invocations(
            self,
            resource_owner_id=None,
            invoke_status=None,
            command_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            invoke_id=None,
            timed=None,
            command_name=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            command_type=None,
            instance_id=None):
        api_request = APIRequest('DescribeInvocations', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InvokeStatus": invoke_status,
            "CommandId": command_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "InvokeId": invoke_id,
            "Timed": timed,
            "CommandName": command_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "CommandType": command_type,
            "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def describe_invocation_results(
            self,
            resource_owner_id=None,
            command_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            invoke_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            instance_id=None,
            invoke_record_status=None,
            include_history=None):
        api_request = APIRequest('DescribeInvocationResults', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "CommandId": command_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "InvokeId": invoke_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "InvokeRecordStatus": invoke_record_status,
            "IncludeHistory": include_history}
        return self._handle_request(api_request).result

    def describe_commands(
            self,
            resource_owner_id=None,
            description=None,
            type_=None,
            command_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            name=None):
        api_request = APIRequest('DescribeCommands', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Description": description,
            "Type": type_,
            "CommandId": command_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Name": name}
        return self._handle_request(api_request).result

    def delete_command(
            self,
            resource_owner_id=None,
            command_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteCommand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "CommandId": command_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_command(
            self,
            resource_owner_id=None,
            working_dir=None,
            description=None,
            type_=None,
            command_content=None,
            timeout=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            name=None,
            enable_parameter=None):
        api_request = APIRequest('CreateCommand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "WorkingDir": working_dir,
            "Description": description,
            "Type": type_,
            "CommandContent": command_content,
            "Timeout": timeout,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Name": name,
            "EnableParameter": enable_parameter}
        return self._handle_request(api_request).result

    def modify_security_group_egress_rule(
            self,
            nic_type=None,
            resource_owner_id=None,
            source_port_range=None,
            client_token=None,
            security_group_id=None,
            description=None,
            region_id=None,
            ipv6_dest_cidr_ip=None,
            ipv6_source_cidr_ip=None,
            policy=None,
            port_range=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            source_cidr_ip=None,
            dest_group_id=None,
            owner_id=None,
            dest_group_owner_account=None,
            priority=None,
            dest_cidr_ip=None,
            dest_group_owner_id=None):
        api_request = APIRequest('ModifySecurityGroupEgressRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NicType": nic_type,
            "ResourceOwnerId": resource_owner_id,
            "SourcePortRange": source_port_range,
            "ClientToken": client_token,
            "SecurityGroupId": security_group_id,
            "Description": description,
            "RegionId": region_id,
            "Ipv6DestCidrIp": ipv6_dest_cidr_ip,
            "Ipv6SourceCidrIp": ipv6_source_cidr_ip,
            "Policy": policy,
            "PortRange": port_range,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "SourceCidrIp": source_cidr_ip,
            "DestGroupId": dest_group_id,
            "OwnerId": owner_id,
            "DestGroupOwnerAccount": dest_group_owner_account,
            "Priority": priority,
            "DestCidrIp": dest_cidr_ip,
            "DestGroupOwnerId": dest_group_owner_id}
        return self._handle_request(api_request).result

    def modify_disk_charge_type(
            self,
            resource_owner_id=None,
            disk_charge_type=None,
            instance_id=None,
            auto_pay=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            disk_ids=None,
            owner_id=None):
        api_request = APIRequest('ModifyDiskChargeType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DiskChargeType": disk_charge_type,
            "InstanceId": instance_id,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DiskIds": disk_ids,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_network_interface_attribute(
            self,
            resource_owner_id=None,
            list_of_security_group_id=None,
            description=None,
            region_id=None,
            network_interface_name=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            network_interface_id=None):
        api_request = APIRequest('ModifyNetworkInterfaceAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityGroupId": list_of_security_group_id,
            "Description": description,
            "RegionId": region_id,
            "NetworkInterfaceName": network_interface_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NetworkInterfaceId": network_interface_id}
        repeat_info = {"SecurityGroupId": ('SecurityGroupId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def detach_network_interface(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            instance_id=None,
            network_interface_id=None):
        api_request = APIRequest('DetachNetworkInterface', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "NetworkInterfaceId": network_interface_id}
        return self._handle_request(api_request).result

    def describe_network_interfaces(
            self,
            resource_owner_id=None,
            service_managed=None,
            security_group_id=None,
            type_=None,
            page_number=None,
            resource_group_id=None,
            region_id=None,
            page_size=None,
            list_of_tag=None,
            network_interface_name=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            vswitch_id=None,
            list_of_private_ip_address=None,
            instance_id=None,
            vpc_id=None,
            primary_ip_address=None,
            list_of_network_interface_id=None):
        api_request = APIRequest('DescribeNetworkInterfaces', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ServiceManaged": service_managed,
            "SecurityGroupId": security_group_id,
            "Type": type_,
            "PageNumber": page_number,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "Tag": list_of_tag,
            "NetworkInterfaceName": network_interface_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": list_of_private_ip_address,
            "InstanceId": instance_id,
            "VpcId": vpc_id,
            "PrimaryIpAddress": primary_ip_address,
            "NetworkInterfaceId": list_of_network_interface_id}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       "PrivateIpAddress": ('PrivateIpAddress', 'list', 'str', None),
                       "NetworkInterfaceId": ('NetworkInterfaceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_network_interface(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            network_interface_id=None):
        api_request = APIRequest('DeleteNetworkInterface', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NetworkInterfaceId": network_interface_id}
        return self._handle_request(api_request).result

    def create_network_interface(
            self,
            resource_owner_id=None,
            client_token=None,
            security_group_id=None,
            description=None,
            business_type=None,
            resource_group_id=None,
            region_id=None,
            list_of_tag=None,
            network_interface_name=None,
            visible=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            vswitch_id=None,
            primary_ip_address=None):
        api_request = APIRequest('CreateNetworkInterface', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "SecurityGroupId": security_group_id,
            "Description": description,
            "BusinessType": business_type,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "Tag": list_of_tag,
            "NetworkInterfaceName": network_interface_name,
            "Visible": visible,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "VSwitchId": vswitch_id,
            "PrimaryIpAddress": primary_ip_address}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def attach_network_interface(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            instance_id=None,
            network_interface_id=None):
        api_request = APIRequest('AttachNetworkInterface', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "NetworkInterfaceId": network_interface_id}
        return self._handle_request(api_request).result

    def describe_recommend_instance_type(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            channel=None,
            network_type=None,
            owner_id=None,
            operator=None,
            token=None,
            scene=None,
            region_id=None,
            instance_type=None,
            proxy_id=None):
        api_request = APIRequest('DescribeRecommendInstanceType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "channel": channel,
            "NetworkType": network_type,
            "OwnerId": owner_id,
            "operator": operator,
            "token": token,
            "Scene": scene,
            "RegionId": region_id,
            "InstanceType": instance_type,
            "proxyId": proxy_id}
        return self._handle_request(api_request).result

    def modify_prepay_instance_spec(
            self,
            resource_owner_id=None,
            auto_pay=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            end_time=None,
            owner_id=None,
            operator_type=None,
            system_disk_category=None,
            reboot_time=None,
            instance_id=None,
            region_id=None,
            migrate_across_zone=None,
            instance_type=None):
        api_request = APIRequest('ModifyPrepayInstanceSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "OperatorType": operator_type,
            "SystemDisk.Category": system_disk_category,
            "RebootTime": reboot_time,
            "InstanceId": instance_id,
            "RegionId": region_id,
            "MigrateAcrossZone": migrate_across_zone,
            "InstanceType": instance_type}
        return self._handle_request(api_request).result

    def modify_instance_charge_type(
            self,
            resource_owner_id=None,
            period=None,
            dry_run=None,
            auto_pay=None,
            include_data_disks=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            owner_id=None,
            period_unit=None,
            instance_ids=None,
            region_id=None,
            is_detail_fee=None,
            instance_charge_type=None):
        api_request = APIRequest('ModifyInstanceChargeType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "DryRun": dry_run,
            "AutoPay": auto_pay,
            "IncludeDataDisks": include_data_disks,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PeriodUnit": period_unit,
            "InstanceIds": instance_ids,
            "RegionId": region_id,
            "IsDetailFee": is_detail_fee,
            "InstanceChargeType": instance_charge_type}
        return self._handle_request(api_request).result

    def join_resource_group(
            self,
            resource_group_id=None,
            resource_owner_id=None,
            resource_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('JoinResourceGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        return self._handle_request(api_request).result

    def modify_security_group_policy(
            self,
            resource_owner_id=None,
            region_id=None,
            client_token=None,
            resource_owner_account=None,
            owner_account=None,
            security_group_id=None,
            owner_id=None,
            inner_access_policy=None):
        api_request = APIRequest('ModifySecurityGroupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ClientToken": client_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SecurityGroupId": security_group_id,
            "OwnerId": owner_id,
            "InnerAccessPolicy": inner_access_policy}
        return self._handle_request(api_request).result

    def describe_security_group_references(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            list_of_security_group_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeSecurityGroupReferences', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SecurityGroupId": list_of_security_group_id,
            "OwnerId": owner_id}
        repeat_info = {"SecurityGroupId": ('SecurityGroupId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def detach_classic_link_vpc(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            vpc_id=None,
            owner_id=None):
        api_request = APIRequest('DetachClassicLinkVpc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_classic_link_instances(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            vpc_id=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeClassicLinkInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def attach_classic_link_vpc(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            vpc_id=None,
            owner_id=None):
        api_request = APIRequest('AttachClassicLinkVpc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def detach_instance_ram_role(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            instance_ids=None,
            ram_role_name=None,
            owner_id=None):
        api_request = APIRequest('DetachInstanceRamRole', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "InstanceIds": instance_ids,
            "RamRoleName": ram_role_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instance_ram_role(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            instance_ids=None,
            page_size=None,
            ram_role_name=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeInstanceRamRole', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "InstanceIds": instance_ids,
            "PageSize": page_size,
            "RamRoleName": ram_role_name,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def attach_instance_ram_role(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            instance_ids=None,
            ram_role_name=None,
            owner_id=None):
        api_request = APIRequest('AttachInstanceRamRole', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "InstanceIds": instance_ids,
            "RamRoleName": ram_role_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_snapshot_package(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeSnapshotPackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_security_group_rule(
            self,
            nic_type=None,
            resource_owner_id=None,
            source_port_range=None,
            client_token=None,
            security_group_id=None,
            description=None,
            source_group_owner_id=None,
            source_group_owner_account=None,
            region_id=None,
            ipv6_source_cidr_ip=None,
            ipv6_dest_cidr_ip=None,
            policy=None,
            port_range=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            source_cidr_ip=None,
            owner_id=None,
            priority=None,
            dest_cidr_ip=None,
            source_group_id=None):
        api_request = APIRequest('ModifySecurityGroupRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NicType": nic_type,
            "ResourceOwnerId": resource_owner_id,
            "SourcePortRange": source_port_range,
            "ClientToken": client_token,
            "SecurityGroupId": security_group_id,
            "Description": description,
            "SourceGroupOwnerId": source_group_owner_id,
            "SourceGroupOwnerAccount": source_group_owner_account,
            "RegionId": region_id,
            "Ipv6SourceCidrIp": ipv6_source_cidr_ip,
            "Ipv6DestCidrIp": ipv6_dest_cidr_ip,
            "Policy": policy,
            "PortRange": port_range,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "SourceCidrIp": source_cidr_ip,
            "OwnerId": owner_id,
            "Priority": priority,
            "DestCidrIp": dest_cidr_ip,
            "SourceGroupId": source_group_id}
        return self._handle_request(api_request).result

    def describe_snapshot_monitor_data(
            self,
            resource_owner_id=None,
            period=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeSnapshotMonitorData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_renewal_price(
            self,
            resource_owner_id=None,
            resource_id=None,
            period=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            price_unit=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('DescribeRenewalPrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PriceUnit": price_unit,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        return self._handle_request(api_request).result

    def describe_price(
            self,
            data_disk3_performance_level=None,
            data_disk3_size=None,
            resource_owner_id=None,
            image_id=None,
            data_disk3_category=None,
            io_optimized=None,
            internet_max_bandwidth_out=None,
            system_disk_category=None,
            system_disk_performance_level=None,
            data_disk4_category=None,
            data_disk4_performance_level=None,
            region_id=None,
            data_disk4_size=None,
            price_unit=None,
            instance_type=None,
            data_disk2_category=None,
            data_disk1_size=None,
            period=None,
            amount=None,
            resource_owner_account=None,
            owner_account=None,
            data_disk2_size=None,
            data_disk1_performance_level=None,
            owner_id=None,
            resource_type=None,
            data_disk1_category=None,
            data_disk2_performance_level=None,
            system_disk_size=None,
            internet_charge_type=None,
            instance_network_type=None):
        api_request = APIRequest('DescribePrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataDisk.3.PerformanceLevel": data_disk3_performance_level,
            "DataDisk.3.Size": data_disk3_size,
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "DataDisk.3.Category": data_disk3_category,
            "IoOptimized": io_optimized,
            "InternetMaxBandwidthOut": internet_max_bandwidth_out,
            "SystemDisk.Category": system_disk_category,
            "SystemDisk.PerformanceLevel": system_disk_performance_level,
            "DataDisk.4.Category": data_disk4_category,
            "DataDisk.4.PerformanceLevel": data_disk4_performance_level,
            "RegionId": region_id,
            "DataDisk.4.Size": data_disk4_size,
            "PriceUnit": price_unit,
            "InstanceType": instance_type,
            "DataDisk.2.Category": data_disk2_category,
            "DataDisk.1.Size": data_disk1_size,
            "Period": period,
            "Amount": amount,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DataDisk.2.Size": data_disk2_size,
            "DataDisk.1.PerformanceLevel": data_disk1_performance_level,
            "OwnerId": owner_id,
            "ResourceType": resource_type,
            "DataDisk.1.Category": data_disk1_category,
            "DataDisk.2.PerformanceLevel": data_disk2_performance_level,
            "SystemDisk.Size": system_disk_size,
            "InternetChargeType": internet_charge_type,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def modify_deployment_set_attribute(
            self,
            deployment_set_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            description=None,
            deployment_set_name=None,
            owner_id=None):
        api_request = APIRequest('ModifyDeploymentSetAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DeploymentSetId": deployment_set_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Description": description,
            "DeploymentSetName": deployment_set_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_deployment_sets(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            network_type=None,
            deployment_set_name=None,
            owner_id=None,
            page_number=None,
            deployment_set_ids=None,
            region_id=None,
            granularity=None,
            domain=None,
            page_size=None,
            strategy=None):
        api_request = APIRequest('DescribeDeploymentSets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "NetworkType": network_type,
            "DeploymentSetName": deployment_set_name,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "DeploymentSetIds": deployment_set_ids,
            "RegionId": region_id,
            "Granularity": granularity,
            "Domain": domain,
            "PageSize": page_size,
            "Strategy": strategy}
        return self._handle_request(api_request).result

    def delete_deployment_set(
            self,
            deployment_set_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteDeploymentSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DeploymentSetId": deployment_set_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_deployment_set(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            description=None,
            deployment_set_name=None,
            owner_id=None,
            region_id=None,
            on_unable_to_redeploy_failed_instance=None,
            granularity=None,
            domain=None,
            strategy=None):
        api_request = APIRequest('CreateDeploymentSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Description": description,
            "DeploymentSetName": deployment_set_name,
            "OwnerId": owner_id,
            "RegionId": region_id,
            "OnUnableToRedeployFailedInstance": on_unable_to_redeploy_failed_instance,
            "Granularity": granularity,
            "Domain": domain,
            "Strategy": strategy}
        return self._handle_request(api_request).result

    def import_key_pair(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            public_key_body=None,
            key_pair_name=None,
            owner_id=None):
        api_request = APIRequest('ImportKeyPair', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "PublicKeyBody": public_key_body,
            "KeyPairName": key_pair_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def detach_key_pair(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            instance_ids=None,
            key_pair_name=None,
            owner_id=None):
        api_request = APIRequest('DetachKeyPair', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "InstanceIds": instance_ids,
            "KeyPairName": key_pair_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_key_pairs(
            self,
            resource_group_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            key_pair_finger_print=None,
            page_size=None,
            key_pair_name=None,
            list_of_tag=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeKeyPairs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "KeyPairFingerPrint": key_pair_finger_print,
            "PageSize": page_size,
            "KeyPairName": key_pair_name,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_key_pairs(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            key_pair_names=None,
            owner_id=None):
        api_request = APIRequest('DeleteKeyPairs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "KeyPairNames": key_pair_names,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_key_pair(
            self,
            resource_group_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            key_pair_name=None,
            list_of_tag=None,
            owner_id=None):
        api_request = APIRequest('CreateKeyPair', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "KeyPairName": key_pair_name,
            "Tag": list_of_tag,
            "OwnerId": owner_id}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def attach_key_pair(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            instance_ids=None,
            key_pair_name=None,
            owner_id=None):
        api_request = APIRequest('AttachKeyPair', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "InstanceIds": instance_ids,
            "KeyPairName": key_pair_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_instance_auto_renew_attribute(
            self,
            duration=None,
            resource_owner_id=None,
            period_unit=None,
            instance_id=None,
            auto_renew=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            renewal_status=None,
            owner_id=None):
        api_request = APIRequest('ModifyInstanceAutoRenewAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "ResourceOwnerId": resource_owner_id,
            "PeriodUnit": period_unit,
            "InstanceId": instance_id,
            "AutoRenew": auto_renew,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "RenewalStatus": renewal_status,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instance_auto_renew_attribute(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            renewal_status=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeInstanceAutoRenewAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "RenewalStatus": renewal_status,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_snapshot_links(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            disk_ids=None,
            snapshot_link_ids=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeSnapshotLinks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "DiskIds": disk_ids,
            "SnapshotLinkIds": snapshot_link_ids,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_instance_auto_release_time(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            auto_release_time=None,
            owner_id=None):
        api_request = APIRequest('ModifyInstanceAutoReleaseTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "AutoReleaseTime": auto_release_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_new_project_eip_monitor_data(
            self,
            resource_owner_id=None,
            period=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            end_time=None,
            allocation_id=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeNewProjectEipMonitorData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "AllocationId": allocation_id,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_user_data(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeUserData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def remove_bandwidth_package_ips(
            self,
            list_of_removed_ip_addresses=None,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('RemoveBandwidthPackageIps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RemovedIpAddresses": list_of_removed_ip_addresses,
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        repeat_info = {"RemovedIpAddresses": ('RemovedIpAddresses', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_forward_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            forward_table_id=None,
            owner_id=None,
            internal_ip=None,
            region_id=None,
            forward_entry_id=None,
            internal_port=None,
            external_ip=None,
            external_port=None):
        api_request = APIRequest('ModifyForwardEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "ForwardTableId": forward_table_id,
            "OwnerId": owner_id,
            "InternalIp": internal_ip,
            "RegionId": region_id,
            "ForwardEntryId": forward_entry_id,
            "InternalPort": internal_port,
            "ExternalIp": external_ip,
            "ExternalPort": external_port}
        return self._handle_request(api_request).result

    def modify_bandwidth_package_spec(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            bandwidth=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyBandwidthPackageSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_nat_gateways(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            vpc_id=None,
            page_size=None,
            nat_gateway_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeNatGateways', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "VpcId": vpc_id,
            "PageSize": page_size,
            "NatGatewayId": nat_gateway_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_forward_table_entries(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            forward_entry_id=None,
            owner_account=None,
            forward_table_id=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeForwardTableEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ForwardEntryId": forward_entry_id,
            "OwnerAccount": owner_account,
            "ForwardTableId": forward_table_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_bandwidth_packages(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            nat_gateway_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeBandwidthPackages', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "NatGatewayId": nat_gateway_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_nat_gateway(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            nat_gateway_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteNatGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "NatGatewayId": nat_gateway_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_forward_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            forward_entry_id=None,
            owner_account=None,
            forward_table_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteForwardEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ForwardEntryId": forward_entry_id,
            "OwnerAccount": owner_account,
            "ForwardTableId": forward_table_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_bandwidth_package(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteBandwidthPackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_nat_gateway(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            vpc_id=None,
            name=None,
            description=None,
            owner_id=None,
            list_of_bandwidth_package=None):
        api_request = APIRequest('CreateNatGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "VpcId": vpc_id,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id,
            "BandwidthPackage": list_of_bandwidth_package}
        repeat_info = {
            "BandwidthPackage": (
                'BandwidthPackage', 'list', 'dict', [
                    ('Bandwidth', 'str', None, None), ('Zone', 'str', None, None), ('IpCount', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_forward_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            ip_protocol=None,
            internal_port=None,
            owner_account=None,
            forward_table_id=None,
            owner_id=None,
            external_ip=None,
            external_port=None,
            internal_ip=None):
        api_request = APIRequest('CreateForwardEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "IpProtocol": ip_protocol,
            "InternalPort": internal_port,
            "OwnerAccount": owner_account,
            "ForwardTableId": forward_table_id,
            "OwnerId": owner_id,
            "ExternalIp": external_ip,
            "ExternalPort": external_port,
            "InternalIp": internal_ip}
        return self._handle_request(api_request).result

    def add_bandwidth_package_ips(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            owner_id=None,
            ip_count=None):
        api_request = APIRequest('AddBandwidthPackageIps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "IpCount": ip_count}
        return self._handle_request(api_request).result

    def eip_fill_product(
            self,
            resource_owner_id=None,
            data=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            user_cidr=None,
            owner_id=None):
        api_request = APIRequest('EipFillProduct', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "data": data,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "UserCidr": user_cidr,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def eip_notify_paid(
            self,
            resource_owner_id=None,
            data=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            user_cidr=None,
            owner_id=None):
        api_request = APIRequest('EipNotifyPaid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "data": data,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "UserCidr": user_cidr,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def eip_fill_params(
            self,
            resource_owner_id=None,
            data=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            user_cidr=None,
            owner_id=None):
        api_request = APIRequest('EipFillParams', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "data": data,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "UserCidr": user_cidr,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_auto_snapshot_policy_ex(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            auto_snapshot_policy_id=None,
            time_points=None,
            retention_days=None,
            owner_id=None,
            repeat_weekdays=None,
            auto_snapshot_policy_name=None):
        api_request = APIRequest('ModifyAutoSnapshotPolicyEx', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "regionId": region_id,
            "autoSnapshotPolicyId": auto_snapshot_policy_id,
            "timePoints": time_points,
            "retentionDays": retention_days,
            "OwnerId": owner_id,
            "repeatWeekdays": repeat_weekdays,
            "autoSnapshotPolicyName": auto_snapshot_policy_name}
        return self._handle_request(api_request).result

    def describe_auto_snapshot_policy_ex(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            auto_snapshot_policy_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeAutoSnapshotPolicyEx', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "AutoSnapshotPolicyId": auto_snapshot_policy_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_auto_snapshot_policy(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            auto_snapshot_policy_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteAutoSnapshotPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "regionId": region_id,
            "autoSnapshotPolicyId": auto_snapshot_policy_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_auto_snapshot_policy(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            time_points=None,
            retention_days=None,
            owner_id=None,
            repeat_weekdays=None,
            auto_snapshot_policy_name=None):
        api_request = APIRequest('CreateAutoSnapshotPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "regionId": region_id,
            "timePoints": time_points,
            "retentionDays": retention_days,
            "OwnerId": owner_id,
            "repeatWeekdays": repeat_weekdays,
            "autoSnapshotPolicyName": auto_snapshot_policy_name}
        return self._handle_request(api_request).result

    def cancel_auto_snapshot_policy(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            disk_ids=None,
            owner_id=None):
        api_request = APIRequest('CancelAutoSnapshotPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "regionId": region_id,
            "diskIds": disk_ids,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def apply_auto_snapshot_policy(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            auto_snapshot_policy_id=None,
            disk_ids=None,
            owner_id=None):
        api_request = APIRequest('ApplyAutoSnapshotPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "regionId": region_id,
            "autoSnapshotPolicyId": auto_snapshot_policy_id,
            "diskIds": disk_ids,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_image_support_instance_types(
            self,
            action_type=None,
            list_of_filter_=None,
            resource_owner_id=None,
            image_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeImageSupportInstanceTypes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ActionType": action_type,
            "Filter": list_of_filter_,
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerId": owner_id}
        repeat_info = {"Filter": ('Filter', 'list', 'dict', [('Value', 'str', None, None),
                                                             ('Key', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def terminate_virtual_border_router(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            user_cidr=None,
            vbr_id=None,
            owner_id=None):
        api_request = APIRequest('TerminateVirtualBorderRouter', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "UserCidr": user_cidr,
            "VbrId": vbr_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def terminate_physical_connection(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            physical_connection_id=None,
            owner_account=None,
            user_cidr=None,
            owner_id=None):
        api_request = APIRequest('TerminatePhysicalConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "PhysicalConnectionId": physical_connection_id,
            "OwnerAccount": owner_account,
            "UserCidr": user_cidr,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def recover_virtual_border_router(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            user_cidr=None,
            vbr_id=None,
            owner_id=None):
        api_request = APIRequest('RecoverVirtualBorderRouter', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "UserCidr": user_cidr,
            "VbrId": vbr_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_virtual_border_router_attribute(
            self,
            resource_owner_id=None,
            circuit_code=None,
            vlan_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            description=None,
            vbr_id=None,
            owner_id=None,
            peer_gateway_ip=None,
            peering_subnet_mask=None,
            region_id=None,
            name=None,
            local_gateway_ip=None,
            user_cidr=None):
        api_request = APIRequest('ModifyVirtualBorderRouterAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "CircuitCode": circuit_code,
            "VlanId": vlan_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Description": description,
            "VbrId": vbr_id,
            "OwnerId": owner_id,
            "PeerGatewayIp": peer_gateway_ip,
            "PeeringSubnetMask": peering_subnet_mask,
            "RegionId": region_id,
            "Name": name,
            "LocalGatewayIp": local_gateway_ip,
            "UserCidr": user_cidr}
        return self._handle_request(api_request).result

    def modify_physical_connection_attribute(
            self,
            redundant_physical_connection_id=None,
            peer_location=None,
            resource_owner_id=None,
            port_type=None,
            circuit_code=None,
            bandwidth=None,
            client_token=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            owner_id=None,
            line_operator=None,
            region_id=None,
            physical_connection_id=None,
            name=None,
            user_cidr=None):
        api_request = APIRequest('ModifyPhysicalConnectionAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RedundantPhysicalConnectionId": redundant_physical_connection_id,
            "PeerLocation": peer_location,
            "ResourceOwnerId": resource_owner_id,
            "PortType": port_type,
            "CircuitCode": circuit_code,
            "bandwidth": bandwidth,
            "ClientToken": client_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "LineOperator": line_operator,
            "RegionId": region_id,
            "PhysicalConnectionId": physical_connection_id,
            "Name": name,
            "UserCidr": user_cidr}
        return self._handle_request(api_request).result

    def enable_physical_connection(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            physical_connection_id=None,
            owner_account=None,
            user_cidr=None,
            owner_id=None):
        api_request = APIRequest('EnablePhysicalConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "PhysicalConnectionId": physical_connection_id,
            "OwnerAccount": owner_account,
            "UserCidr": user_cidr,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_virtual_border_routers_for_physical_connection(
            self,
            list_of_filter_=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            physical_connection_id=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest(
            'DescribeVirtualBorderRoutersForPhysicalConnection',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "Filter": list_of_filter_,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "PhysicalConnectionId": physical_connection_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        repeat_info = {"Filter": ('Filter', 'list', 'dict', [('Value', 'list', 'str', None),
                                                             ('Key', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_virtual_border_routers(
            self,
            list_of_filter_=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeVirtualBorderRouters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Filter": list_of_filter_,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        repeat_info = {"Filter": ('Filter', 'list', 'dict', [('Value', 'list', 'str', None),
                                                             ('Key', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_physical_connections(
            self,
            list_of_filter_=None,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            page_size=None,
            user_cidr=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribePhysicalConnections', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Filter": list_of_filter_,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "UserCidr": user_cidr,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        repeat_info = {"Filter": ('Filter', 'list', 'dict', [('Value', 'list', 'str', None),
                                                             ('Key', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_access_points(
            self,
            list_of_filter_=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            page_size=None,
            owner_id=None,
            type_=None,
            page_number=None):
        api_request = APIRequest('DescribeAccessPoints', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Filter": list_of_filter_,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "Type": type_,
            "PageNumber": page_number}
        repeat_info = {"Filter": ('Filter', 'list', 'dict', [('Value', 'list', 'str', None),
                                                             ('Key', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_virtual_border_router(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            user_cidr=None,
            vbr_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteVirtualBorderRouter', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "UserCidr": user_cidr,
            "VbrId": vbr_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_physical_connection(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            physical_connection_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeletePhysicalConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "PhysicalConnectionId": physical_connection_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_virtual_border_router(
            self,
            resource_owner_id=None,
            circuit_code=None,
            vlan_id=None,
            client_token=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            owner_id=None,
            peer_gateway_ip=None,
            peering_subnet_mask=None,
            region_id=None,
            physical_connection_id=None,
            name=None,
            local_gateway_ip=None,
            user_cidr=None,
            vbr_owner_id=None):
        api_request = APIRequest('CreateVirtualBorderRouter', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "CircuitCode": circuit_code,
            "VlanId": vlan_id,
            "ClientToken": client_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "PeerGatewayIp": peer_gateway_ip,
            "PeeringSubnetMask": peering_subnet_mask,
            "RegionId": region_id,
            "PhysicalConnectionId": physical_connection_id,
            "Name": name,
            "LocalGatewayIp": local_gateway_ip,
            "UserCidr": user_cidr,
            "VbrOwnerId": vbr_owner_id}
        return self._handle_request(api_request).result

    def create_physical_connection(
            self,
            access_point_id=None,
            redundant_physical_connection_id=None,
            peer_location=None,
            resource_owner_id=None,
            port_type=None,
            circuit_code=None,
            bandwidth=None,
            client_token=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            type_=None,
            owner_id=None,
            line_operator=None,
            region_id=None,
            name=None,
            user_cidr=None):
        api_request = APIRequest('CreatePhysicalConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccessPointId": access_point_id,
            "RedundantPhysicalConnectionId": redundant_physical_connection_id,
            "PeerLocation": peer_location,
            "ResourceOwnerId": resource_owner_id,
            "PortType": port_type,
            "CircuitCode": circuit_code,
            "bandwidth": bandwidth,
            "ClientToken": client_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "Type": type_,
            "OwnerId": owner_id,
            "LineOperator": line_operator,
            "RegionId": region_id,
            "Name": name,
            "UserCidr": user_cidr}
        return self._handle_request(api_request).result

    def cancel_physical_connection(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            physical_connection_id=None,
            owner_account=None,
            user_cidr=None,
            owner_id=None):
        api_request = APIRequest('CancelPhysicalConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "PhysicalConnectionId": physical_connection_id,
            "OwnerAccount": owner_account,
            "UserCidr": user_cidr,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def import_image(
            self,
            list_of_disk_device_mapping=None,
            resource_owner_id=None,
            license_type=None,
            resource_owner_account=None,
            role_name=None,
            description=None,
            os_type=None,
            owner_id=None,
            platform=None,
            region_id=None,
            image_name=None,
            architecture=None):
        api_request = APIRequest('ImportImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DiskDeviceMapping": list_of_disk_device_mapping,
            "ResourceOwnerId": resource_owner_id,
            "LicenseType": license_type,
            "ResourceOwnerAccount": resource_owner_account,
            "RoleName": role_name,
            "Description": description,
            "OSType": os_type,
            "OwnerId": owner_id,
            "Platform": platform,
            "RegionId": region_id,
            "ImageName": image_name,
            "Architecture": architecture}
        repeat_info = {"DiskDeviceMapping": ('DiskDeviceMapping',
                                             'list',
                                             'dict',
                                             [('OSSBucket',
                                               'str',
                                               None,
                                               None),
                                              ('DiskImSize',
                                               'str',
                                               None,
                                               None),
                                                 ('Format',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('Device',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('OSSObject',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('DiskImageSize',
                                                  'str',
                                                  None,
                                                  None),
                                              ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def export_image(
            self,
            resource_owner_id=None,
            image_id=None,
            oss_bucket=None,
            resource_owner_account=None,
            region_id=None,
            oss_prefix=None,
            role_name=None,
            owner_id=None,
            image_format=None):
        api_request = APIRequest('ExportImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "OSSBucket": oss_bucket,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OSSPrefix": oss_prefix,
            "RoleName": role_name,
            "OwnerId": owner_id,
            "ImageFormat": image_format}
        return self._handle_request(api_request).result

    def describe_tasks(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            task_ids=None,
            page_number=None,
            task_status=None,
            region_id=None,
            page_size=None,
            task_action=None):
        api_request = APIRequest('DescribeTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "TaskIds": task_ids,
            "PageNumber": page_number,
            "TaskStatus": task_status,
            "RegionId": region_id,
            "PageSize": page_size,
            "TaskAction": task_action}
        return self._handle_request(api_request).result

    def describe_task_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_id=None,
            task_id=None):
        api_request = APIRequest('DescribeTaskAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerId": owner_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def cancel_task(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_id=None,
            task_id=None):
        api_request = APIRequest('CancelTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerId": owner_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def describe_instance_type_families(
            self,
            generation=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceTypeFamilies', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Generation": generation,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_router_interface_spec(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            user_cidr=None,
            router_interface_id=None,
            owner_id=None,
            spec=None):
        api_request = APIRequest('ModifyRouterInterfaceSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "UserCidr": user_cidr,
            "RouterInterfaceId": router_interface_id,
            "OwnerId": owner_id,
            "Spec": spec}
        return self._handle_request(api_request).result

    def modify_router_interface_attribute(
            self,
            opposite_router_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            description=None,
            health_check_target_ip=None,
            owner_id=None,
            router_interface_id=None,
            opposite_interface_owner_id=None,
            region_id=None,
            health_check_source_ip=None,
            name=None,
            opposite_router_type=None,
            opposite_interface_id=None):
        api_request = APIRequest('ModifyRouterInterfaceAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OppositeRouterId": opposite_router_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Description": description,
            "HealthCheckTargetIp": health_check_target_ip,
            "OwnerId": owner_id,
            "RouterInterfaceId": router_interface_id,
            "OppositeInterfaceOwnerId": opposite_interface_owner_id,
            "RegionId": region_id,
            "HealthCheckSourceIp": health_check_source_ip,
            "Name": name,
            "OppositeRouterType": opposite_router_type,
            "OppositeInterfaceId": opposite_interface_id}
        return self._handle_request(api_request).result

    def describe_router_interfaces(
            self,
            list_of_filter_=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeRouterInterfaces', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Filter": list_of_filter_,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        repeat_info = {"Filter": ('Filter', 'list', 'dict', [('Value', 'list', 'str', None),
                                                             ('Key', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_router_interface(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            user_cidr=None,
            router_interface_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteRouterInterface', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "UserCidr": user_cidr,
            "RouterInterfaceId": router_interface_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def deactivate_router_interface(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_id=None,
            router_interface_id=None):
        api_request = APIRequest('DeactivateRouterInterface', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerId": owner_id,
            "RouterInterfaceId": router_interface_id}
        return self._handle_request(api_request).result

    def create_router_interface(
            self,
            access_point_id=None,
            opposite_router_id=None,
            opposite_access_point_id=None,
            resource_owner_id=None,
            role=None,
            client_token=None,
            health_check_target_ip=None,
            description=None,
            spec=None,
            region_id=None,
            user_cidr=None,
            opposite_interface_id=None,
            instance_charge_type=None,
            period=None,
            auto_pay=None,
            resource_owner_account=None,
            opposite_region_id=None,
            owner_account=None,
            owner_id=None,
            opposite_interface_owner_id=None,
            router_type=None,
            health_check_source_ip=None,
            router_id=None,
            opposite_router_type=None,
            name=None,
            pricing_cycle=None):
        api_request = APIRequest('CreateRouterInterface', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccessPointId": access_point_id,
            "OppositeRouterId": opposite_router_id,
            "OppositeAccessPointId": opposite_access_point_id,
            "ResourceOwnerId": resource_owner_id,
            "Role": role,
            "ClientToken": client_token,
            "HealthCheckTargetIp": health_check_target_ip,
            "Description": description,
            "Spec": spec,
            "RegionId": region_id,
            "UserCidr": user_cidr,
            "OppositeInterfaceId": opposite_interface_id,
            "InstanceChargeType": instance_charge_type,
            "Period": period,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "OppositeRegionId": opposite_region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "OppositeInterfaceOwnerId": opposite_interface_owner_id,
            "RouterType": router_type,
            "HealthCheckSourceIp": health_check_source_ip,
            "RouterId": router_id,
            "OppositeRouterType": opposite_router_type,
            "Name": name,
            "PricingCycle": pricing_cycle}
        return self._handle_request(api_request).result

    def connect_router_interface(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_id=None,
            router_interface_id=None):
        api_request = APIRequest('ConnectRouterInterface', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerId": owner_id,
            "RouterInterfaceId": router_interface_id}
        return self._handle_request(api_request).result

    def activate_router_interface(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_id=None,
            router_interface_id=None):
        api_request = APIRequest('ActivateRouterInterface', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerId": owner_id,
            "RouterInterfaceId": router_interface_id}
        return self._handle_request(api_request).result

    def unassociate_ha_vip(
            self,
            ha_vip_id=None,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            force=None,
            owner_id=None):
        api_request = APIRequest('UnassociateHaVip', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HaVipId": ha_vip_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Force": force,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_ha_vip_attribute(
            self,
            ha_vip_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('ModifyHaVipAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HaVipId": ha_vip_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_ha_vips(
            self,
            list_of_filter_=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeHaVips', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Filter": list_of_filter_,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        repeat_info = {"Filter": ('Filter', 'list', 'dict', [('Value', 'list', 'str', None),
                                                             ('Key', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_ha_vip(
            self,
            ha_vip_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteHaVip', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HaVipId": ha_vip_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_ha_vip(
            self,
            vswitch_id=None,
            ip_address=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('CreateHaVip', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "IpAddress": ip_address,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def associate_ha_vip(
            self,
            ha_vip_id=None,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('AssociateHaVip', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HaVipId": ha_vip_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def renew_instance(
            self,
            resource_owner_id=None,
            period=None,
            period_unit=None,
            instance_id=None,
            client_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('RenewInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "PeriodUnit": period_unit,
            "InstanceId": instance_id,
            "ClientToken": client_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def remove_tags(
            self,
            resource_owner_id=None,
            resource_id=None,
            resource_owner_account=None,
            region_id=None,
            list_of_tag=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('RemoveTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_tags(
            self,
            resource_owner_id=None,
            resource_id=None,
            resource_owner_account=None,
            region_id=None,
            page_size=None,
            list_of_tag=None,
            owner_id=None,
            category=None,
            resource_type=None,
            page_number=None):
        api_request = APIRequest('DescribeTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "PageSize": page_size,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "Category": category,
            "ResourceType": resource_type,
            "PageNumber": page_number}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_resource_by_tags(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            page_size=None,
            list_of_tag=None,
            owner_id=None,
            resource_type=None,
            page_number=None):
        api_request = APIRequest('DescribeResourceByTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "PageSize": page_size,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "ResourceType": resource_type,
            "PageNumber": page_number}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def add_tags(
            self,
            resource_owner_id=None,
            resource_id=None,
            resource_owner_account=None,
            region_id=None,
            list_of_tag=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('AddTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def unassociate_eip_address(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            instance_type=None,
            allocation_id=None,
            owner_id=None):
        api_request = APIRequest('UnassociateEipAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "InstanceType": instance_type,
            "AllocationId": allocation_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            dry_run=None,
            resource_owner_account=None,
            confirm_stop=None,
            owner_account=None,
            stopped_mode=None,
            owner_id=None,
            hibernate=None,
            force_stop=None):
        api_request = APIRequest('StopInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "ConfirmStop": confirm_stop,
            "OwnerAccount": owner_account,
            "StoppedMode": stopped_mode,
            "OwnerId": owner_id,
            "Hibernate": hibernate,
            "ForceStop": force_stop}
        return self._handle_request(api_request).result

    def start_instance(
            self,
            source_region_id=None,
            init_local_disk=None,
            resource_owner_id=None,
            instance_id=None,
            dry_run=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('StartInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceRegionId": source_region_id,
            "InitLocalDisk": init_local_disk,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def revoke_security_group_egress(
            self,
            nic_type=None,
            resource_owner_id=None,
            source_port_range=None,
            client_token=None,
            security_group_id=None,
            description=None,
            region_id=None,
            ipv6_dest_cidr_ip=None,
            ipv6_source_cidr_ip=None,
            policy=None,
            port_range=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            source_cidr_ip=None,
            dest_group_id=None,
            owner_id=None,
            dest_group_owner_account=None,
            priority=None,
            dest_cidr_ip=None,
            dest_group_owner_id=None):
        api_request = APIRequest('RevokeSecurityGroupEgress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NicType": nic_type,
            "ResourceOwnerId": resource_owner_id,
            "SourcePortRange": source_port_range,
            "ClientToken": client_token,
            "SecurityGroupId": security_group_id,
            "Description": description,
            "RegionId": region_id,
            "Ipv6DestCidrIp": ipv6_dest_cidr_ip,
            "Ipv6SourceCidrIp": ipv6_source_cidr_ip,
            "Policy": policy,
            "PortRange": port_range,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "SourceCidrIp": source_cidr_ip,
            "DestGroupId": dest_group_id,
            "OwnerId": owner_id,
            "DestGroupOwnerAccount": dest_group_owner_account,
            "Priority": priority,
            "DestCidrIp": dest_cidr_ip,
            "DestGroupOwnerId": dest_group_owner_id}
        return self._handle_request(api_request).result

    def revoke_security_group(
            self,
            nic_type=None,
            resource_owner_id=None,
            source_port_range=None,
            client_token=None,
            security_group_id=None,
            description=None,
            source_group_owner_id=None,
            source_group_owner_account=None,
            region_id=None,
            ipv6_dest_cidr_ip=None,
            ipv6_source_cidr_ip=None,
            policy=None,
            port_range=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            source_cidr_ip=None,
            owner_id=None,
            priority=None,
            dest_cidr_ip=None,
            source_group_id=None):
        api_request = APIRequest('RevokeSecurityGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NicType": nic_type,
            "ResourceOwnerId": resource_owner_id,
            "SourcePortRange": source_port_range,
            "ClientToken": client_token,
            "SecurityGroupId": security_group_id,
            "Description": description,
            "SourceGroupOwnerId": source_group_owner_id,
            "SourceGroupOwnerAccount": source_group_owner_account,
            "RegionId": region_id,
            "Ipv6DestCidrIp": ipv6_dest_cidr_ip,
            "Ipv6SourceCidrIp": ipv6_source_cidr_ip,
            "Policy": policy,
            "PortRange": port_range,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "SourceCidrIp": source_cidr_ip,
            "OwnerId": owner_id,
            "Priority": priority,
            "DestCidrIp": dest_cidr_ip,
            "SourceGroupId": source_group_id}
        return self._handle_request(api_request).result

    def resize_disk(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            new_size=None,
            disk_id=None,
            owner_id=None,
            type_=None):
        api_request = APIRequest('ResizeDisk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "NewSize": new_size,
            "DiskId": disk_id,
            "OwnerId": owner_id,
            "Type": type_}
        return self._handle_request(api_request).result

    def reset_disk(
            self,
            resource_owner_id=None,
            snapshot_id=None,
            resource_owner_account=None,
            owner_account=None,
            disk_id=None,
            owner_id=None):
        api_request = APIRequest('ResetDisk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SnapshotId": snapshot_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DiskId": disk_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def replace_system_disk(
            self,
            resource_owner_id=None,
            image_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            security_enhancement_strategy=None,
            key_pair_name=None,
            owner_id=None,
            platform=None,
            password=None,
            instance_id=None,
            password_inherit=None,
            system_disk_size=None,
            disk_id=None,
            use_additional_service=None,
            architecture=None):
        api_request = APIRequest('ReplaceSystemDisk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "SecurityEnhancementStrategy": security_enhancement_strategy,
            "KeyPairName": key_pair_name,
            "OwnerId": owner_id,
            "Platform": platform,
            "Password": password,
            "InstanceId": instance_id,
            "PasswordInherit": password_inherit,
            "SystemDisk.Size": system_disk_size,
            "DiskId": disk_id,
            "UseAdditionalService": use_additional_service,
            "Architecture": architecture}
        return self._handle_request(api_request).result

    def release_public_ip_address(
            self,
            resource_owner_id=None,
            public_ip_address=None,
            instance_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ReleasePublicIpAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PublicIpAddress": public_ip_address,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def release_eip_address(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            allocation_id=None,
            owner_id=None):
        api_request = APIRequest('ReleaseEipAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "AllocationId": allocation_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def reinit_disk(
            self,
            resource_owner_id=None,
            password=None,
            resource_owner_account=None,
            auto_start_instance=None,
            owner_account=None,
            disk_id=None,
            security_enhancement_strategy=None,
            key_pair_name=None,
            owner_id=None):
        api_request = APIRequest('ReInitDisk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Password": password,
            "ResourceOwnerAccount": resource_owner_account,
            "AutoStartInstance": auto_start_instance,
            "OwnerAccount": owner_account,
            "DiskId": disk_id,
            "SecurityEnhancementStrategy": security_enhancement_strategy,
            "KeyPairName": key_pair_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def reboot_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            dry_run=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            force_stop=None):
        api_request = APIRequest('RebootInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ForceStop": force_stop}
        return self._handle_request(api_request).result

    def modify_vswitch_attribute(
            self,
            vswitch_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            vswitch_name=None,
            owner_account=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('ModifyVSwitchAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VSwitchName": vswitch_name,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_vrouter_attribute(
            self,
            vrouter_name=None,
            resource_owner_id=None,
            vrouter_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('ModifyVRouterAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VRouterName": vrouter_name,
            "ResourceOwnerId": resource_owner_id,
            "VRouterId": vrouter_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_vpc_attribute(
            self,
            vpc_name=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            vpc_id=None,
            owner_account=None,
            cidr_block=None,
            description=None,
            user_cidr=None,
            owner_id=None):
        api_request = APIRequest('ModifyVpcAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VpcName": vpc_name,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "OwnerAccount": owner_account,
            "CidrBlock": cidr_block,
            "Description": description,
            "UserCidr": user_cidr,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_snapshot_attribute(
            self,
            resource_owner_id=None,
            snapshot_id=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            snapshot_name=None,
            owner_id=None):
        api_request = APIRequest('ModifySnapshotAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SnapshotId": snapshot_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "SnapshotName": snapshot_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_security_group_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            security_group_id=None,
            description=None,
            owner_id=None,
            security_group_name=None):
        api_request = APIRequest('ModifySecurityGroupAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SecurityGroupId": security_group_id,
            "Description": description,
            "OwnerId": owner_id,
            "SecurityGroupName": security_group_name}
        return self._handle_request(api_request).result

    def modify_instance_vpc_attribute(
            self,
            vswitch_id=None,
            private_ip_address=None,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyInstanceVpcAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_instance_vnc_passwd(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            vnc_password=None):
        api_request = APIRequest('ModifyInstanceVncPasswd', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "VncPassword": vnc_password}
        return self._handle_request(api_request).result

    def modify_instance_spec(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            allow_migrate_across_zone=None,
            owner_account=None,
            internet_max_bandwidth_out=None,
            owner_id=None,
            temporary_internet_max_bandwidth_out=None,
            system_disk_category=None,
            temporary_start_time=None,
            async_=None,
            instance_id=None,
            instance_type=None,
            temporary_end_time=None,
            internet_max_bandwidth_in=None):
        api_request = APIRequest('ModifyInstanceSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "AllowMigrateAcrossZone": allow_migrate_across_zone,
            "OwnerAccount": owner_account,
            "InternetMaxBandwidthOut": internet_max_bandwidth_out,
            "OwnerId": owner_id,
            "Temporary.InternetMaxBandwidthOut": temporary_internet_max_bandwidth_out,
            "SystemDisk.Category": system_disk_category,
            "Temporary.StartTime": temporary_start_time,
            "Async": async_,
            "InstanceId": instance_id,
            "InstanceType": instance_type,
            "Temporary.EndTime": temporary_end_time,
            "InternetMaxBandwidthIn": internet_max_bandwidth_in}
        return self._handle_request(api_request).result

    def modify_instance_network_spec(
            self,
            resource_owner_id=None,
            auto_pay=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            internet_max_bandwidth_out=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            instance_id=None,
            network_charge_type=None,
            internet_max_bandwidth_in=None,
            allocate_public_ip=None):
        api_request = APIRequest('ModifyInstanceNetworkSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "InternetMaxBandwidthOut": internet_max_bandwidth_out,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "NetworkChargeType": network_charge_type,
            "InternetMaxBandwidthIn": internet_max_bandwidth_in,
            "AllocatePublicIp": allocate_public_ip}
        return self._handle_request(api_request).result

    def modify_instance_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            recyclable=None,
            owner_account=None,
            description=None,
            credit_specification=None,
            owner_id=None,
            deletion_protection=None,
            user_data=None,
            password=None,
            host_name=None,
            instance_id=None,
            instance_name=None):
        api_request = APIRequest('ModifyInstanceAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Recyclable": recyclable,
            "OwnerAccount": owner_account,
            "Description": description,
            "CreditSpecification": credit_specification,
            "OwnerId": owner_id,
            "DeletionProtection": deletion_protection,
            "UserData": user_data,
            "Password": password,
            "HostName": host_name,
            "InstanceId": instance_id,
            "InstanceName": instance_name}
        return self._handle_request(api_request).result

    def modify_image_share_permission(
            self,
            resource_owner_id=None,
            image_id=None,
            list_of_add_account=None,
            resource_owner_account=None,
            region_id=None,
            list_of_remove_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyImageSharePermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "AddAccount": list_of_add_account,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "RemoveAccount": list_of_remove_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        repeat_info = {"AddAccount": ('AddAccount', 'list', 'str', None),
                       "RemoveAccount": ('RemoveAccount', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_image_share_group_permission(
            self,
            resource_owner_id=None,
            image_id=None,
            add_group1=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            remove_group1=None,
            owner_id=None):
        api_request = APIRequest('ModifyImageShareGroupPermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "AddGroup.1": add_group1,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "RemoveGroup.1": remove_group1,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_image_attribute(
            self,
            resource_owner_id=None,
            image_id=None,
            resource_owner_account=None,
            region_id=None,
            image_name=None,
            owner_account=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('ModifyImageAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ImageName": image_name,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_eip_address_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            bandwidth=None,
            owner_account=None,
            allocation_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyEipAddressAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "AllocationId": allocation_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_disk_attribute(
            self,
            disk_name=None,
            delete_auto_snapshot=None,
            resource_owner_id=None,
            enable_auto_snapshot=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            disk_id=None,
            owner_id=None,
            delete_with_instance=None):
        api_request = APIRequest('ModifyDiskAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DiskName": disk_name,
            "DeleteAutoSnapshot": delete_auto_snapshot,
            "ResourceOwnerId": resource_owner_id,
            "EnableAutoSnapshot": enable_auto_snapshot,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "DiskId": disk_id,
            "OwnerId": owner_id,
            "DeleteWithInstance": delete_with_instance}
        return self._handle_request(api_request).result

    def modify_auto_snapshot_policy(
            self,
            data_disk_policy_enabled=None,
            resource_owner_id=None,
            data_disk_policy_retention_days=None,
            resource_owner_account=None,
            system_disk_policy_retention_last_week=None,
            owner_account=None,
            system_disk_policy_time_period=None,
            owner_id=None,
            data_disk_policy_retention_last_week=None,
            system_disk_policy_retention_days=None,
            data_disk_policy_time_period=None,
            system_disk_policy_enabled=None):
        api_request = APIRequest('ModifyAutoSnapshotPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataDiskPolicyEnabled": data_disk_policy_enabled,
            "ResourceOwnerId": resource_owner_id,
            "DataDiskPolicyRetentionDays": data_disk_policy_retention_days,
            "ResourceOwnerAccount": resource_owner_account,
            "SystemDiskPolicyRetentionLastWeek": system_disk_policy_retention_last_week,
            "OwnerAccount": owner_account,
            "SystemDiskPolicyTimePeriod": system_disk_policy_time_period,
            "OwnerId": owner_id,
            "DataDiskPolicyRetentionLastWeek": data_disk_policy_retention_last_week,
            "SystemDiskPolicyRetentionDays": system_disk_policy_retention_days,
            "DataDiskPolicyTimePeriod": data_disk_policy_time_period,
            "SystemDiskPolicyEnabled": system_disk_policy_enabled}
        return self._handle_request(api_request).result

    def leave_security_group(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            owner_account=None,
            security_group_id=None,
            owner_id=None):
        api_request = APIRequest('LeaveSecurityGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SecurityGroupId": security_group_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def join_security_group(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            owner_account=None,
            security_group_id=None,
            owner_id=None):
        api_request = APIRequest('JoinSecurityGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SecurityGroupId": security_group_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def detach_disk(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            owner_account=None,
            disk_id=None,
            owner_id=None):
        api_request = APIRequest('DetachDisk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DiskId": disk_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_zones(
            self,
            spot_strategy=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            accept_language=None,
            owner_id=None,
            instance_charge_type=None,
            verbose=None):
        api_request = APIRequest('DescribeZones', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SpotStrategy": spot_strategy,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "AcceptLanguage": accept_language,
            "OwnerId": owner_id,
            "InstanceChargeType": instance_charge_type,
            "Verbose": verbose}
        return self._handle_request(api_request).result

    def describe_vswitches(
            self,
            vswitch_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            vpc_id=None,
            owner_account=None,
            page_size=None,
            zone_id=None,
            is_default=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeVSwitches', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "ZoneId": zone_id,
            "IsDefault": is_default,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_vrouters(
            self,
            resource_owner_id=None,
            vrouter_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeVRouters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "VRouterId": vrouter_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_vpcs(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            vpc_id=None,
            owner_account=None,
            page_size=None,
            is_default=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeVpcs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "IsDefault": is_default,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_snapshots(
            self,
            resource_owner_id=None,
            filter2_value=None,
            snapshot_ids=None,
            usage=None,
            snapshot_link_id=None,
            snapshot_name=None,
            page_number=None,
            resource_group_id=None,
            filter1_key=None,
            region_id=None,
            page_size=None,
            disk_id=None,
            list_of_tag=None,
            dry_run=None,
            resource_owner_account=None,
            owner_account=None,
            source_disk_type=None,
            filter1_value=None,
            filter2_key=None,
            owner_id=None,
            instance_id=None,
            encrypted=None,
            snapshot_type=None,
            kms_key_id=None,
            status=None):
        api_request = APIRequest('DescribeSnapshots', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Filter.2.Value": filter2_value,
            "SnapshotIds": snapshot_ids,
            "Usage": usage,
            "SnapshotLinkId": snapshot_link_id,
            "SnapshotName": snapshot_name,
            "PageNumber": page_number,
            "ResourceGroupId": resource_group_id,
            "Filter.1.Key": filter1_key,
            "RegionId": region_id,
            "PageSize": page_size,
            "DiskId": disk_id,
            "Tag": list_of_tag,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SourceDiskType": source_disk_type,
            "Filter.1.Value": filter1_value,
            "Filter.2.Key": filter2_key,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "Encrypted": encrypted,
            "SnapshotType": snapshot_type,
            "KMSKeyId": kms_key_id,
            "Status": status}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_security_groups(
            self,
            resource_owner_id=None,
            dry_run=None,
            fuzzy_query=None,
            resource_owner_account=None,
            owner_account=None,
            security_group_id=None,
            is_query_ecs_count=None,
            network_type=None,
            owner_id=None,
            security_group_ids=None,
            security_group_name=None,
            page_number=None,
            resource_group_id=None,
            region_id=None,
            vpc_id=None,
            page_size=None,
            list_of_tag=None):
        api_request = APIRequest('DescribeSecurityGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DryRun": dry_run,
            "FuzzyQuery": fuzzy_query,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SecurityGroupId": security_group_id,
            "IsQueryEcsCount": is_query_ecs_count,
            "NetworkType": network_type,
            "OwnerId": owner_id,
            "SecurityGroupIds": security_group_ids,
            "SecurityGroupName": security_group_name,
            "PageNumber": page_number,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "PageSize": page_size,
            "Tag": list_of_tag}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_security_group_attribute(
            self,
            nic_type=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            security_group_id=None,
            owner_id=None,
            direction=None):
        api_request = APIRequest('DescribeSecurityGroupAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NicType": nic_type,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SecurityGroupId": security_group_id,
            "OwnerId": owner_id,
            "Direction": direction}
        return self._handle_request(api_request).result

    def describe_route_tables(
            self,
            resource_owner_id=None,
            vrouter_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            page_number=None,
            router_type=None,
            route_table_name=None,
            region_id=None,
            router_id=None,
            page_size=None,
            route_table_id=None):
        api_request = APIRequest('DescribeRouteTables', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "VRouterId": vrouter_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "RouterType": router_type,
            "RouteTableName": route_table_name,
            "RegionId": region_id,
            "RouterId": router_id,
            "PageSize": page_size,
            "RouteTableId": route_table_id}
        return self._handle_request(api_request).result

    def describe_regions(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            accept_language=None,
            owner_id=None,
            instance_charge_type=None,
            resource_type=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AcceptLanguage": accept_language,
            "OwnerId": owner_id,
            "InstanceChargeType": instance_charge_type,
            "ResourceType": resource_type}
        return self._handle_request(api_request).result

    def describe_limitation(
            self,
            limitation=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeLimitation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Limitation": limitation,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instance_vnc_url(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceVncUrl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instance_vnc_passwd(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceVncPasswd', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instance_types(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            instance_type_family=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceTypes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "InstanceTypeFamily": instance_type_family,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instance_status(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            zone_id=None,
            cluster_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeInstanceStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "ZoneId": zone_id,
            "ClusterId": cluster_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_instances(
            self,
            inner_ip_addresses=None,
            resource_owner_id=None,
            image_id=None,
            private_ip_addresses=None,
            hpc_cluster_id=None,
            filter2_value=None,
            filter4_value=None,
            io_optimized=None,
            security_group_id=None,
            key_pair_name=None,
            filter4_key=None,
            page_number=None,
            resource_group_id=None,
            lock_reason=None,
            filter1_key=None,
            region_id=None,
            rdma_ip_addresses=None,
            device_available=None,
            page_size=None,
            public_ip_addresses=None,
            instance_type=None,
            list_of_tag=None,
            instance_charge_type=None,
            filter3_value=None,
            dry_run=None,
            resource_owner_account=None,
            owner_account=None,
            instance_type_family=None,
            filter1_value=None,
            need_sale_cycle=None,
            filter2_key=None,
            owner_id=None,
            vswitch_id=None,
            eip_addresses=None,
            instance_name=None,
            instance_ids=None,
            internet_charge_type=None,
            vpc_id=None,
            zone_id=None,
            filter3_key=None,
            instance_network_type=None,
            status=None):
        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InnerIpAddresses": inner_ip_addresses,
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "PrivateIpAddresses": private_ip_addresses,
            "HpcClusterId": hpc_cluster_id,
            "Filter.2.Value": filter2_value,
            "Filter.4.Value": filter4_value,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "KeyPairName": key_pair_name,
            "Filter.4.Key": filter4_key,
            "PageNumber": page_number,
            "ResourceGroupId": resource_group_id,
            "LockReason": lock_reason,
            "Filter.1.Key": filter1_key,
            "RegionId": region_id,
            "RdmaIpAddresses": rdma_ip_addresses,
            "DeviceAvailable": device_available,
            "PageSize": page_size,
            "PublicIpAddresses": public_ip_addresses,
            "InstanceType": instance_type,
            "Tag": list_of_tag,
            "InstanceChargeType": instance_charge_type,
            "Filter.3.Value": filter3_value,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "InstanceTypeFamily": instance_type_family,
            "Filter.1.Value": filter1_value,
            "NeedSaleCycle": need_sale_cycle,
            "Filter.2.Key": filter2_key,
            "OwnerId": owner_id,
            "VSwitchId": vswitch_id,
            "EipAddresses": eip_addresses,
            "InstanceName": instance_name,
            "InstanceIds": instance_ids,
            "InternetChargeType": internet_charge_type,
            "VpcId": vpc_id,
            "ZoneId": zone_id,
            "Filter.3.Key": filter3_key,
            "InstanceNetworkType": instance_network_type,
            "Status": status}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_instance_physical_attribute(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstancePhysicalAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instance_monitor_data(
            self,
            resource_owner_id=None,
            start_time=None,
            period=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            owner_id=None,
            instance_id=None):
        api_request = APIRequest('DescribeInstanceMonitorData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "StartTime": start_time,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def describe_instance_attribute(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_image_share_permission(
            self,
            resource_owner_id=None,
            image_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeImageSharePermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_images(
            self,
            action_type=None,
            resource_owner_id=None,
            image_id=None,
            snapshot_id=None,
            usage=None,
            page_number=None,
            image_owner_alias=None,
            resource_group_id=None,
            is_support_io_optimized=None,
            region_id=None,
            image_name=None,
            is_support_cloudinit=None,
            page_size=None,
            instance_type=None,
            list_of_tag=None,
            architecture=None,
            dry_run=None,
            resource_owner_account=None,
            owner_account=None,
            show_expired=None,
            os_type=None,
            owner_id=None,
            list_of_filter_=None,
            status=None):
        api_request = APIRequest('DescribeImages', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ActionType": action_type,
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "SnapshotId": snapshot_id,
            "Usage": usage,
            "PageNumber": page_number,
            "ImageOwnerAlias": image_owner_alias,
            "ResourceGroupId": resource_group_id,
            "IsSupportIoOptimized": is_support_io_optimized,
            "RegionId": region_id,
            "ImageName": image_name,
            "IsSupportCloudinit": is_support_cloudinit,
            "PageSize": page_size,
            "InstanceType": instance_type,
            "Tag": list_of_tag,
            "Architecture": architecture,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ShowExpired": show_expired,
            "OSType": os_type,
            "OwnerId": owner_id,
            "Filter": list_of_filter_,
            "Status": status}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       "Filter": ('Filter', 'list', 'dict', [('Value', 'str', None, None),
                                                             ('Key', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_eip_monitor_data(
            self,
            resource_owner_id=None,
            period=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            end_time=None,
            allocation_id=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeEipMonitorData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "AllocationId": allocation_id,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_eip_addresses(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            filter2_value=None,
            isp=None,
            owner_account=None,
            allocation_id=None,
            filter1_value=None,
            filter2_key=None,
            owner_id=None,
            eip_address=None,
            page_number=None,
            lock_reason=None,
            filter1_key=None,
            region_id=None,
            associated_instance_type=None,
            page_size=None,
            charge_type=None,
            associated_instance_id=None,
            status=None):
        api_request = APIRequest('DescribeEipAddresses', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Filter.2.Value": filter2_value,
            "ISP": isp,
            "OwnerAccount": owner_account,
            "AllocationId": allocation_id,
            "Filter.1.Value": filter1_value,
            "Filter.2.Key": filter2_key,
            "OwnerId": owner_id,
            "EipAddress": eip_address,
            "PageNumber": page_number,
            "LockReason": lock_reason,
            "Filter.1.Key": filter1_key,
            "RegionId": region_id,
            "AssociatedInstanceType": associated_instance_type,
            "PageSize": page_size,
            "ChargeType": charge_type,
            "AssociatedInstanceId": associated_instance_id,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_disks(
            self,
            resource_owner_id=None,
            snapshot_id=None,
            filter2_value=None,
            auto_snapshot_policy_id=None,
            page_number=None,
            disk_name=None,
            delete_auto_snapshot=None,
            resource_group_id=None,
            disk_charge_type=None,
            lock_reason=None,
            filter1_key=None,
            region_id=None,
            page_size=None,
            disk_ids=None,
            list_of_tag=None,
            delete_with_instance=None,
            enable_auto_snapshot=None,
            dry_run=None,
            resource_owner_account=None,
            owner_account=None,
            filter1_value=None,
            portable=None,
            enable_automated_snapshot_policy=None,
            filter2_key=None,
            owner_id=None,
            disk_type=None,
            list_of_additional_attributes=None,
            enable_shared=None,
            instance_id=None,
            encrypted=None,
            zone_id=None,
            category=None,
            kms_key_id=None,
            status=None):
        api_request = APIRequest('DescribeDisks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SnapshotId": snapshot_id,
            "Filter.2.Value": filter2_value,
            "AutoSnapshotPolicyId": auto_snapshot_policy_id,
            "PageNumber": page_number,
            "DiskName": disk_name,
            "DeleteAutoSnapshot": delete_auto_snapshot,
            "ResourceGroupId": resource_group_id,
            "DiskChargeType": disk_charge_type,
            "LockReason": lock_reason,
            "Filter.1.Key": filter1_key,
            "RegionId": region_id,
            "PageSize": page_size,
            "DiskIds": disk_ids,
            "Tag": list_of_tag,
            "DeleteWithInstance": delete_with_instance,
            "EnableAutoSnapshot": enable_auto_snapshot,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Filter.1.Value": filter1_value,
            "Portable": portable,
            "EnableAutomatedSnapshotPolicy": enable_automated_snapshot_policy,
            "Filter.2.Key": filter2_key,
            "OwnerId": owner_id,
            "DiskType": disk_type,
            "AdditionalAttributes": list_of_additional_attributes,
            "EnableShared": enable_shared,
            "InstanceId": instance_id,
            "Encrypted": encrypted,
            "ZoneId": zone_id,
            "Category": category,
            "KMSKeyId": kms_key_id,
            "Status": status}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       "AdditionalAttributes": ('AdditionalAttributes', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_disk_monitor_data(
            self,
            resource_owner_id=None,
            start_time=None,
            disk_id=None,
            period=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeDiskMonitorData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "StartTime": start_time,
            "DiskId": disk_id,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_clusters(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeClusters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_vswitch(
            self,
            vswitch_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteVSwitch', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_vpc(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            vpc_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteVpc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_snapshot(
            self,
            resource_owner_id=None,
            snapshot_id=None,
            resource_owner_account=None,
            owner_account=None,
            force=None,
            owner_id=None):
        api_request = APIRequest('DeleteSnapshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SnapshotId": snapshot_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Force": force,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_security_group(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            security_group_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteSecurityGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SecurityGroupId": security_group_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_route_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            destination_cidr_block=None,
            owner_account=None,
            next_hop_id=None,
            owner_id=None,
            list_of_next_hop_list=None,
            route_table_id=None):
        api_request = APIRequest('DeleteRouteEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "DestinationCidrBlock": destination_cidr_block,
            "OwnerAccount": owner_account,
            "NextHopId": next_hop_id,
            "OwnerId": owner_id,
            "NextHopList": list_of_next_hop_list,
            "RouteTableId": route_table_id}
        repeat_info = {
            "NextHopList": (
                'NextHopList', 'list', 'dict', [
                    ('NextHopId', 'str', None, None), ('NextHopType', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            owner_account=None,
            terminate_subscription=None,
            force=None,
            owner_id=None):
        api_request = APIRequest('DeleteInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "TerminateSubscription": terminate_subscription,
            "Force": force,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_image(
            self,
            resource_owner_id=None,
            image_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            force=None,
            owner_id=None):
        api_request = APIRequest('DeleteImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Force": force,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_disk(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            disk_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteDisk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DiskId": disk_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_vswitch(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            vpc_id=None,
            vswitch_name=None,
            owner_account=None,
            cidr_block=None,
            zone_id=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('CreateVSwitch', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "VpcId": vpc_id,
            "VSwitchName": vswitch_name,
            "OwnerAccount": owner_account,
            "CidrBlock": cidr_block,
            "ZoneId": zone_id,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_vpc(
            self,
            vpc_name=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            cidr_block=None,
            description=None,
            user_cidr=None,
            owner_id=None):
        api_request = APIRequest('CreateVpc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VpcName": vpc_name,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "CidrBlock": cidr_block,
            "Description": description,
            "UserCidr": user_cidr,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_snapshot(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            description=None,
            disk_id=None,
            snapshot_name=None,
            retention_days=None,
            list_of_tag=None,
            owner_id=None):
        api_request = APIRequest('CreateSnapshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Description": description,
            "DiskId": disk_id,
            "SnapshotName": snapshot_name,
            "RetentionDays": retention_days,
            "Tag": list_of_tag,
            "OwnerId": owner_id}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_security_group(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            description=None,
            owner_id=None,
            security_group_name=None,
            security_group_type=None,
            resource_group_id=None,
            region_id=None,
            vpc_id=None,
            list_of_tag=None):
        api_request = APIRequest('CreateSecurityGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "SecurityGroupName": security_group_name,
            "SecurityGroupType": security_group_type,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "Tag": list_of_tag}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_route_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            destination_cidr_block=None,
            owner_account=None,
            next_hop_id=None,
            owner_id=None,
            next_hop_type=None,
            list_of_next_hop_list=None,
            route_table_id=None):
        api_request = APIRequest('CreateRouteEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "DestinationCidrBlock": destination_cidr_block,
            "OwnerAccount": owner_account,
            "NextHopId": next_hop_id,
            "OwnerId": owner_id,
            "NextHopType": next_hop_type,
            "NextHopList": list_of_next_hop_list,
            "RouteTableId": route_table_id}
        repeat_info = {
            "NextHopList": (
                'NextHopList', 'list', 'dict', [
                    ('NextHopId', 'str', None, None), ('NextHopType', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_instance(
            self,
            resource_owner_id=None,
            hpc_cluster_id=None,
            security_enhancement_strategy=None,
            key_pair_name=None,
            spot_price_limit=None,
            deletion_protection=None,
            resource_group_id=None,
            host_name=None,
            password=None,
            storage_set_partition_number=None,
            list_of_tag=None,
            auto_renew_period=None,
            node_controller_id=None,
            period=None,
            dry_run=None,
            owner_id=None,
            capacity_reservation_preference=None,
            vswitch_id=None,
            private_ip_address=None,
            spot_strategy=None,
            period_unit=None,
            instance_name=None,
            auto_renew=None,
            internet_charge_type=None,
            zone_id=None,
            internet_max_bandwidth_in=None,
            use_additional_service=None,
            affinity=None,
            image_id=None,
            client_token=None,
            vlan_id=None,
            spot_interruption_behavior=None,
            io_optimized=None,
            security_group_id=None,
            internet_max_bandwidth_out=None,
            description=None,
            system_disk_category=None,
            capacity_reservation_id=None,
            system_disk_performance_level=None,
            user_data=None,
            password_inherit=None,
            region_id=None,
            instance_type=None,
            list_of_arn=None,
            instance_charge_type=None,
            deployment_set_id=None,
            inner_ip_address=None,
            resource_owner_account=None,
            owner_account=None,
            tenancy=None,
            system_disk_disk_name=None,
            ram_role_name=None,
            dedicated_host_id=None,
            cluster_id=None,
            credit_specification=None,
            list_of_data_disk=None,
            storage_set_id=None,
            system_disk_size=None,
            system_disk_description=None):
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "HpcClusterId": hpc_cluster_id,
            "SecurityEnhancementStrategy": security_enhancement_strategy,
            "KeyPairName": key_pair_name,
            "SpotPriceLimit": spot_price_limit,
            "DeletionProtection": deletion_protection,
            "ResourceGroupId": resource_group_id,
            "HostName": host_name,
            "Password": password,
            "StorageSetPartitionNumber": storage_set_partition_number,
            "Tag": list_of_tag,
            "AutoRenewPeriod": auto_renew_period,
            "NodeControllerId": node_controller_id,
            "Period": period,
            "DryRun": dry_run,
            "OwnerId": owner_id,
            "CapacityReservationPreference": capacity_reservation_preference,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "SpotStrategy": spot_strategy,
            "PeriodUnit": period_unit,
            "InstanceName": instance_name,
            "AutoRenew": auto_renew,
            "InternetChargeType": internet_charge_type,
            "ZoneId": zone_id,
            "InternetMaxBandwidthIn": internet_max_bandwidth_in,
            "UseAdditionalService": use_additional_service,
            "Affinity": affinity,
            "ImageId": image_id,
            "ClientToken": client_token,
            "VlanId": vlan_id,
            "SpotInterruptionBehavior": spot_interruption_behavior,
            "IoOptimized": io_optimized,
            "SecurityGroupId": security_group_id,
            "InternetMaxBandwidthOut": internet_max_bandwidth_out,
            "Description": description,
            "SystemDisk.Category": system_disk_category,
            "CapacityReservationId": capacity_reservation_id,
            "SystemDisk.PerformanceLevel": system_disk_performance_level,
            "UserData": user_data,
            "PasswordInherit": password_inherit,
            "RegionId": region_id,
            "InstanceType": instance_type,
            "Arn": list_of_arn,
            "InstanceChargeType": instance_charge_type,
            "DeploymentSetId": deployment_set_id,
            "InnerIpAddress": inner_ip_address,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Tenancy": tenancy,
            "SystemDisk.DiskName": system_disk_disk_name,
            "RamRoleName": ram_role_name,
            "DedicatedHostId": dedicated_host_id,
            "ClusterId": cluster_id,
            "CreditSpecification": credit_specification,
            "DataDisk": list_of_data_disk,
            "StorageSetId": storage_set_id,
            "SystemDisk.Size": system_disk_size,
            "SystemDisk.Description": system_disk_description}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       "Arn": ('Arn', 'list', 'dict', [('Rolearn', 'str', None, None),
                                                       ('RoleType', 'str', None, None),
                                                       ('AssumeRoleFor', 'str', None, None),
                                                       ]),
                       "DataDisk": ('DataDisk', 'list', 'dict', [('DiskName', 'str', None, None),
                                                                 ('SnapshotId', 'str', None, None),
                                                                 ('Size', 'str', None, None),
                                                                 ('Encrypted', 'str', None, None),
                                                                 ('PerformanceLevel', 'str', None, None),
                                                                 ('Description', 'str', None, None),
                                                                 ('Category', 'str', None, None),
                                                                 ('KMSKeyId', 'str', None, None),
                                                                 ('Device', 'str', None, None),
                                                                 ('DeleteWithInstance', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_image(
            self,
            list_of_disk_device_mapping=None,
            resource_owner_id=None,
            snapshot_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            description=None,
            owner_id=None,
            platform=None,
            resource_group_id=None,
            instance_id=None,
            region_id=None,
            image_name=None,
            image_version=None,
            list_of_tag=None,
            architecture=None):
        api_request = APIRequest('CreateImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DiskDeviceMapping": list_of_disk_device_mapping,
            "ResourceOwnerId": resource_owner_id,
            "SnapshotId": snapshot_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "Platform": platform,
            "ResourceGroupId": resource_group_id,
            "InstanceId": instance_id,
            "RegionId": region_id,
            "ImageName": image_name,
            "ImageVersion": image_version,
            "Tag": list_of_tag,
            "Architecture": architecture}
        repeat_info = {"DiskDeviceMapping": ('DiskDeviceMapping', 'list', 'dict', [('SnapshotId', 'str', None, None),
                                                                                   ('Size', 'str', None, None),
                                                                                   ('DiskType', 'str', None, None),
                                                                                   ('Device', 'str', None, None),
                                                                                   ]),
                       "Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_disk(
            self,
            resource_owner_id=None,
            snapshot_id=None,
            resource_owner_account=None,
            client_token=None,
            performance_level=None,
            owner_account=None,
            description=None,
            owner_id=None,
            disk_name=None,
            resource_group_id=None,
            instance_id=None,
            storage_set_id=None,
            size=None,
            encrypted=None,
            region_id=None,
            disk_category=None,
            zone_id=None,
            storage_set_partition_number=None,
            list_of_tag=None,
            list_of_arn=None,
            kms_key_id=None,
            advanced_features=None):
        api_request = APIRequest('CreateDisk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SnapshotId": snapshot_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "PerformanceLevel": performance_level,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "DiskName": disk_name,
            "ResourceGroupId": resource_group_id,
            "InstanceId": instance_id,
            "StorageSetId": storage_set_id,
            "Size": size,
            "Encrypted": encrypted,
            "RegionId": region_id,
            "DiskCategory": disk_category,
            "ZoneId": zone_id,
            "StorageSetPartitionNumber": storage_set_partition_number,
            "Tag": list_of_tag,
            "Arn": list_of_arn,
            "KMSKeyId": kms_key_id,
            "AdvancedFeatures": advanced_features}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       "Arn": ('Arn', 'list', 'dict', [('Rolearn', 'str', None, None),
                                                       ('RoleType', 'str', None, None),
                                                       ('AssumeRoleFor', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def copy_image(
            self,
            resource_owner_id=None,
            image_id=None,
            resource_owner_account=None,
            destination_image_name=None,
            destination_region_id=None,
            owner_account=None,
            owner_id=None,
            encrypted=None,
            region_id=None,
            list_of_tag=None,
            kms_key_id=None,
            destination_description=None):
        api_request = APIRequest('CopyImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DestinationImageName": destination_image_name,
            "DestinationRegionId": destination_region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Encrypted": encrypted,
            "RegionId": region_id,
            "Tag": list_of_tag,
            "KMSKeyId": kms_key_id,
            "DestinationDescription": destination_description}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def cancel_copy_image(
            self,
            resource_owner_id=None,
            image_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CancelCopyImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def authorize_security_group_egress(
            self,
            nic_type=None,
            resource_owner_id=None,
            source_port_range=None,
            client_token=None,
            security_group_id=None,
            description=None,
            region_id=None,
            ipv6_dest_cidr_ip=None,
            ipv6_source_cidr_ip=None,
            policy=None,
            port_range=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            source_cidr_ip=None,
            dest_group_id=None,
            owner_id=None,
            dest_group_owner_account=None,
            priority=None,
            dest_cidr_ip=None,
            dest_group_owner_id=None):
        api_request = APIRequest('AuthorizeSecurityGroupEgress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NicType": nic_type,
            "ResourceOwnerId": resource_owner_id,
            "SourcePortRange": source_port_range,
            "ClientToken": client_token,
            "SecurityGroupId": security_group_id,
            "Description": description,
            "RegionId": region_id,
            "Ipv6DestCidrIp": ipv6_dest_cidr_ip,
            "Ipv6SourceCidrIp": ipv6_source_cidr_ip,
            "Policy": policy,
            "PortRange": port_range,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "SourceCidrIp": source_cidr_ip,
            "DestGroupId": dest_group_id,
            "OwnerId": owner_id,
            "DestGroupOwnerAccount": dest_group_owner_account,
            "Priority": priority,
            "DestCidrIp": dest_cidr_ip,
            "DestGroupOwnerId": dest_group_owner_id}
        return self._handle_request(api_request).result

    def authorize_security_group(
            self,
            nic_type=None,
            resource_owner_id=None,
            source_port_range=None,
            client_token=None,
            security_group_id=None,
            description=None,
            source_group_owner_id=None,
            source_group_owner_account=None,
            region_id=None,
            ipv6_source_cidr_ip=None,
            ipv6_dest_cidr_ip=None,
            policy=None,
            port_range=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            source_cidr_ip=None,
            owner_id=None,
            priority=None,
            dest_cidr_ip=None,
            source_group_id=None):
        api_request = APIRequest('AuthorizeSecurityGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NicType": nic_type,
            "ResourceOwnerId": resource_owner_id,
            "SourcePortRange": source_port_range,
            "ClientToken": client_token,
            "SecurityGroupId": security_group_id,
            "Description": description,
            "SourceGroupOwnerId": source_group_owner_id,
            "SourceGroupOwnerAccount": source_group_owner_account,
            "RegionId": region_id,
            "Ipv6SourceCidrIp": ipv6_source_cidr_ip,
            "Ipv6DestCidrIp": ipv6_dest_cidr_ip,
            "Policy": policy,
            "PortRange": port_range,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "SourceCidrIp": source_cidr_ip,
            "OwnerId": owner_id,
            "Priority": priority,
            "DestCidrIp": dest_cidr_ip,
            "SourceGroupId": source_group_id}
        return self._handle_request(api_request).result

    def attach_disk(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            owner_account=None,
            disk_id=None,
            owner_id=None,
            device=None,
            delete_with_instance=None):
        api_request = APIRequest('AttachDisk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DiskId": disk_id,
            "OwnerId": owner_id,
            "Device": device,
            "DeleteWithInstance": delete_with_instance}
        return self._handle_request(api_request).result

    def associate_eip_address(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            instance_type=None,
            allocation_id=None,
            owner_id=None):
        api_request = APIRequest('AssociateEipAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "InstanceType": instance_type,
            "AllocationId": allocation_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def allocate_public_ip_address(
            self,
            ip_address=None,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            vlan_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('AllocatePublicIpAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IpAddress": ip_address,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "VlanId": vlan_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def allocate_eip_address(
            self,
            activity_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            bandwidth=None,
            client_token=None,
            internet_charge_type=None,
            isp=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('AllocateEipAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ActivityId": activity_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "Bandwidth": bandwidth,
            "ClientToken": client_token,
            "InternetChargeType": internet_charge_type,
            "ISP": isp,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result
