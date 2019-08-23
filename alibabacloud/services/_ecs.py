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

import time

from alibabacloud.exceptions import ClientException
from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, \
    _create_special_resource_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _ECSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ecs', _client=_client)
        self.access_points = _create_resource_collection(
            _ECSAccessPointResource, _client, _client.describe_access_points,
            'AccessPointSet.AccessPointType', 'AccessPointId',
        )
        self.auto_provisioning_groups = _create_resource_collection(
            _ECSAutoProvisioningGroupResource, _client, _client.describe_auto_provisioning_groups,
            'AutoProvisioningGroups.AutoProvisioningGroup', 'AutoProvisioningGroupId',
        )
        self.bandwidth_packages = _create_resource_collection(
            _ECSBandwidthPackageResource, _client, _client.describe_bandwidth_packages,
            'BandwidthPackages.BandwidthPackage', 'BandwidthPackageId',
        )
        self.clusters = _create_special_resource_collection(
            _ECSClusterResource, _client, _client.describe_clusters,
            'Clusters.Cluster', 'ClusterId',
        )
        self.commands = _create_resource_collection(
            _ECSCommandResource, _client, _client.describe_commands,
            'Commands.Command', 'CommandId',
        )
        self.dedicated_hosts = _create_resource_collection(
            _ECSDedicatedHostResource, _client, _client.describe_dedicated_hosts,
            'DedicatedHosts.DedicatedHost', 'DedicatedHostId',
        )
        self.deployment_sets = _create_resource_collection(
            _ECSDeploymentSetResource, _client, _client.describe_deployment_sets,
            'DeploymentSets.DeploymentSet', 'DeploymentSetId',
        )
        self.disks = _create_resource_collection(
            _ECSDiskResource, _client, _client.describe_disks,
            'Disks.Disk', 'DiskId',
        )
        self.eip_addresses = _create_resource_collection(
            _ECSEipAddressResource, _client, _client.describe_eip_addresses,
            'EipAddresses.EipAddress', 'AllocationId',
        )
        self.fleets = _create_resource_collection(
            _ECSFleetResource, _client, _client.describe_fleets,
            'Fleets.Fleet', 'FleetId',
        )
        self.ha_vips = _create_resource_collection(
            _ECSHaVipResource, _client, _client.describe_ha_vips,
            'HaVips.HaVip', 'HaVipId',
        )
        self.hpc_clusters = _create_resource_collection(
            _ECSHpcClusterResource, _client, _client.describe_hpc_clusters,
            'HpcClusters.HpcCluster', 'HpcClusterId',
        )
        self.images = _create_resource_collection(
            _ECSImageResource, _client, _client.describe_images,
            'Images.Image', 'ImageId',
        )
        self.instances = _create_resource_collection(
            _ECSInstanceResource, _client, _client.describe_instances,
            'Instances.Instance', 'InstanceId',
        )
        self.instance_types = _create_special_resource_collection(
            _ECSInstanceTypeResource, _client, _client.describe_instance_types,
            'InstanceTypes.InstanceType', 'InstanceTypeId',
        )
        self.key_pairs = _create_resource_collection(
            _ECSKeyPairResource, _client, _client.describe_key_pairs,
            'KeyPairs.KeyPair', 'KeyPairName',
        )
        self.launch_templates = _create_resource_collection(
            _ECSLaunchTemplateResource, _client, _client.describe_launch_templates,
            'LaunchTemplateSets.LaunchTemplateSet', 'LaunchTemplateId',
        )
        self.network_interfaces = _create_resource_collection(
            _ECSNetworkInterfaceResource, _client, _client.describe_network_interfaces,
            'NetworkInterfaceSets.NetworkInterfaceSet', 'NetworkInterfaceId',
        )
        self.network_interface_permissions = _create_resource_collection(
            _ECSNetworkInterfacePermissionResource, _client,
            _client.describe_network_interface_permissions,
            'NetworkInterfacePermissions.NetworkInterfacePermission',
            'NetworkInterfacePermissionId',
        )
        self.physical_connections = _create_resource_collection(
            _ECSPhysicalConnectionResource, _client, _client.describe_physical_connections,
            'PhysicalConnectionSet.PhysicalConnectionType', 'PhysicalConnectionId',
        )
        self.regions = _create_special_resource_collection(
            _ECSRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId',
        )
        self.reserved_instances = _create_resource_collection(
            _ECSReservedInstanceResource, _client, _client.describe_reserved_instances,
            'ReservedInstances.ReservedInstance', 'ReservedInstanceId',
        )
        self.route_tables = _create_resource_collection(
            _ECSRouteTableResource, _client, _client.describe_route_tables,
            'RouteTables.RouteTable', 'RouteTableId',
        )
        self.router_interfaces = _create_resource_collection(
            _ECSRouterInterfaceResource, _client, _client.describe_router_interfaces,
            'RouterInterfaceSet.RouterInterfaceType', 'RouterInterfaceId',
        )
        self.security_groups = _create_resource_collection(
            _ECSSecurityGroupResource, _client, _client.describe_security_groups,
            'SecurityGroups.SecurityGroup', 'SecurityGroupId',
        )
        self.snapshots = _create_resource_collection(
            _ECSSnapshotResource, _client, _client.describe_snapshots,
            'Snapshots.Snapshot', 'SnapshotId',
        )
        self.snapshot_links = _create_resource_collection(
            _ECSSnapshotLinkResource, _client, _client.describe_snapshot_links,
            'SnapshotLinks.SnapshotLink', 'SnapshotLinkId',
        )
        self.storage_sets = _create_resource_collection(
            _ECSStorageSetResource, _client, _client.describe_storage_sets,
            'StorageSets.StorageSet', 'StorageSetId',
        )
        self.system_events = _create_resource_collection(
            _ECSSystemEventResource, _client, _client.describe_instance_history_events,
            'InstanceSystemEventSet.InstanceSystemEventType', 'EventId',
        )
        self.tasks = _create_resource_collection(
            _ECSTaskResource, _client, _client.describe_tasks,
            'TaskSet.Task', 'TaskId',
        )
        self.vrouters = _create_resource_collection(
            _ECSVRouterResource, _client, _client.describe_vrouters,
            'VRouters.VRouter', 'VRouterId',
        )
        self.vswitches = _create_resource_collection(
            _ECSVSwitchResource, _client, _client.describe_vswitches,
            'VSwitches.VSwitch', 'VSwitchId',
        )
        self.virtual_border_routers = _create_resource_collection(
            _ECSVirtualBorderRouterResource, _client, _client.describe_virtual_border_routers,
            'VirtualBorderRouterSet.VirtualBorderRouterType', 'VbrId',
        )
        self.vpcs = _create_resource_collection(
            _ECSVpcResource, _client, _client.describe_vpcs,
            'Vpcs.Vpc', 'VpcId',
        )
        self.zones = _create_special_resource_collection(
            _ECSZoneResource, _client, _client.describe_zones,
            'Zones.Zone', 'ZoneId',
        )

    def create_auto_provisioning_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_auto_provisioning_group(**_params)
        auto_provisioning_group_id = _new_get_key_in_response(response, 'AutoProvisioningGroupId')
        return _ECSAutoProvisioningGroupResource(auto_provisioning_group_id, _client=self._client)

    def create_auto_snapshot_policy(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_auto_snapshot_policy(**_params)
        auto_snapshot_policy_id = _new_get_key_in_response(response, 'AutoSnapshotPolicyId')
        return _ECSAutoSnapshotPolicyResource(auto_snapshot_policy_id, _client=self._client)

    def create_command(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_command(**_params)
        command_id = _new_get_key_in_response(response, 'CommandId')
        return _ECSCommandResource(command_id, _client=self._client)

    def allocate_dedicated_hosts(self, **params):
        _params = _transfer_params(params)
        response = self._client.allocate_dedicated_hosts(**_params)
        dedicated_host_ids = _new_get_key_in_response(response,
                                                      'DedicatedHostIdSets.DedicatedHostId')
        dedicated_hosts = []
        for dedicated_host_id in dedicated_host_ids:
            dedicated_host = _ECSDedicatedHostResource(dedicated_host_id, _client=self._client)
            dedicated_hosts.append(dedicated_host)
        return dedicated_hosts

    def create_deployment_set(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_deployment_set(**_params)
        deployment_set_id = _new_get_key_in_response(response, 'DeploymentSetId')
        return _ECSDeploymentSetResource(deployment_set_id, _client=self._client)

    def create_disk(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_disk(**_params)
        disk_id = _new_get_key_in_response(response, 'DiskId')
        return _ECSDiskResource(disk_id, _client=self._client)

    def allocate_eip_address(self, **params):
        _params = _transfer_params(params)
        response = self._client.allocate_eip_address(**_params)
        allocation_id = _new_get_key_in_response(response, 'AllocationId')
        return _ECSEipAddressResource(allocation_id, _client=self._client)

    def create_fleet(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_fleet(**_params)
        fleet_id = _new_get_key_in_response(response, 'FleetId')
        return _ECSFleetResource(fleet_id, _client=self._client)

    def create_ha_vip(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ha_vip(**_params)
        ha_vip_id = _new_get_key_in_response(response, 'HaVipId')
        return _ECSHaVipResource(ha_vip_id, _client=self._client)

    def create_hpc_cluster(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_hpc_cluster(**_params)
        hpc_cluster_id = _new_get_key_in_response(response, 'HpcClusterId')
        return _ECSHpcClusterResource(hpc_cluster_id, _client=self._client)

    def copy_image(self, **params):
        _params = _transfer_params(params)
        response = self._client.copy_image(**_params)
        image_id = _new_get_key_in_response(response, 'ImageId')
        return _ECSImageResource(image_id, _client=self._client)

    def create_image(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_image(**_params)
        image_id = _new_get_key_in_response(response, 'ImageId')
        return _ECSImageResource(image_id, _client=self._client)

    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _ECSInstanceResource(instance_id, _client=self._client)

    def run_instances(self, **params):
        _params = _transfer_params(params)
        response = self._client.run_instances(**_params)
        instance_ids = _new_get_key_in_response(response, 'InstanceIdSets.InstanceIdSet')
        instances = []
        for instance_id in instance_ids:
            instance = _ECSInstanceResource(instance_id, _client=self._client)
            instances.append(instance)
        return instances

    def create_key_pair(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_key_pair(**_params)
        key_pair_name = _new_get_key_in_response(response, 'KeyPairName')
        return _ECSKeyPairResource(key_pair_name, _client=self._client)

    def import_key_pair(self, **params):
        _params = _transfer_params(params)
        response = self._client.import_key_pair(**_params)
        key_pair_name = _new_get_key_in_response(response, 'KeyPairName')
        return _ECSKeyPairResource(key_pair_name, _client=self._client)

    def create_launch_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_launch_template(**_params)
        launch_template_id = _new_get_key_in_response(response, 'LaunchTemplateId')
        return _ECSLaunchTemplateResource(launch_template_id, _client=self._client)

    def create_nat_gateway(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_nat_gateway(**_params)
        nat_gateway_id = _new_get_key_in_response(response, 'NatGatewayId')
        return _ECSNatGatewayResource(nat_gateway_id, _client=self._client)

    def create_network_interface(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_network_interface(**_params)
        network_interface_id = _new_get_key_in_response(response, 'NetworkInterfaceId')
        return _ECSNetworkInterfaceResource(network_interface_id, _client=self._client)

    def create_physical_connection(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_physical_connection(**_params)
        physical_connection_id = _new_get_key_in_response(response, 'PhysicalConnectionId')
        return _ECSPhysicalConnectionResource(physical_connection_id, _client=self._client)

    def create_router_interface(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_router_interface(**_params)
        router_interface_id = _new_get_key_in_response(response, 'RouterInterfaceId')
        return _ECSRouterInterfaceResource(router_interface_id, _client=self._client)

    def create_security_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_security_group(**_params)
        security_group_id = _new_get_key_in_response(response, 'SecurityGroupId')
        return _ECSSecurityGroupResource(security_group_id, _client=self._client)

    def create_snapshot(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_snapshot(**_params)
        snapshot_id = _new_get_key_in_response(response, 'SnapshotId')
        return _ECSSnapshotResource(snapshot_id, _client=self._client)

    def create_storage_set(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_storage_set(**_params)
        storage_set_id = _new_get_key_in_response(response, 'StorageSetId')
        return _ECSStorageSetResource(storage_set_id, _client=self._client)

    def create_vswitch(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_vswitch(**_params)
        vswitch_id = _new_get_key_in_response(response, 'VSwitchId')
        return _ECSVSwitchResource(vswitch_id, _client=self._client)

    def create_virtual_border_router(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_virtual_border_router(**_params)
        vbr_id = _new_get_key_in_response(response, 'VbrId')
        return _ECSVirtualBorderRouterResource(vbr_id, _client=self._client)

    def create_vpc(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_vpc(**_params)
        vpc_id = _new_get_key_in_response(response, 'VpcId')
        return _ECSVpcResource(vpc_id, _client=self._client)


class _ECSAccessPointResource(ServiceResource):

    def __init__(self, access_point_id, _client=None):
        ServiceResource.__init__(self, "ecs.access_point", _client=_client)
        self.access_point_id = access_point_id

        self.attached_region_no = None
        self.description = None
        self.host_operator = None
        self.location = None
        self.name = None
        self.status = None
        self.type_ = None


class _ECSAutoProvisioningGroupResource(ServiceResource):

    def __init__(self, auto_provisioning_group_id, _client=None):
        ServiceResource.__init__(self, "ecs.auto_provisioning_group", _client=_client)
        self.auto_provisioning_group_id = auto_provisioning_group_id

        self.auto_provisioning_group_name = None
        self.auto_provisioning_group_type = None
        self.creation_time = None
        self.excess_capacity_termination_policy = None
        self.launch_template_configs = None
        self.launch_template_id = None
        self.launch_template_version = None
        self.max_spot_price = None
        self.pay_as_you_go_options = None
        self.region_id = None
        self.spot_options = None
        self.state = None
        self.status = None
        self.target_capacity_specification = None
        self.terminate_instances = None
        self.terminate_instances_with_expiration = None
        self.valid_from = None
        self.valid_until = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_auto_provisioning_group(
            auto_provisioning_group_id=self.auto_provisioning_group_id, **_params)

    def describe_auto_provisioning_group_history(self, **params):
        _params = _transfer_params(params)
        self._client.describe_auto_provisioning_group_history(
            auto_provisioning_group_id=self.auto_provisioning_group_id, **_params)

    def describe_auto_provisioning_group_instances(self, **params):
        _params = _transfer_params(params)
        self._client.describe_auto_provisioning_group_instances(
            auto_provisioning_group_id=self.auto_provisioning_group_id, **_params)

    def refresh(self):
        result = self._client.describe_auto_provisioning_groups(
            list_of_auto_provisioning_group_id=[self.auto_provisioning_group_id, ])
        items = _new_get_key_in_response(result, 'AutoProvisioningGroups.AutoProvisioningGroup')
        if not items:
            raise ClientException(msg=
                                  "Failed to find auto_provisioning_group data from DescribeAutoProvisioningGroups response. "
                                  "AutoProvisioningGroupId = {0}".format(
                                      self.auto_provisioning_group_id))
        self._assign_attributes(items[0])

    def wait_until(self, target_status, timeout=120):
        start_time = time.time()
        while True:
            end_time = time.time()
            if end_time - start_time >= timeout:
                raise Exception("Timed out: no {0} status after {1} seconds.".format(
                    target_status, timeout))

            self.refresh()
            if self.status == target_status:
                return
            time.sleep(1)


class _ECSAutoSnapshotPolicyResource(ServiceResource):

    def __init__(self, auto_snapshot_policy_id, _client=None):
        ServiceResource.__init__(self, "ecs.auto_snapshot_policy", _client=_client)
        self.auto_snapshot_policy_id = auto_snapshot_policy_id

    def apply(self, **params):
        _params = _transfer_params(params)
        self._client.apply_auto_snapshot_policy(
            auto_snapshot_policy_id=self.auto_snapshot_policy_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_auto_snapshot_policy(
            auto_snapshot_policy_id=self.auto_snapshot_policy_id, **_params)

    def modify_ex(self, **params):
        _params = _transfer_params(params)
        self._client.modify_auto_snapshot_policy_ex(
            auto_snapshot_policy_id=self.auto_snapshot_policy_id, **_params)


class _ECSBandwidthPackageResource(ServiceResource):

    def __init__(self, bandwidth_package_id, _client=None):
        ServiceResource.__init__(self, "ecs.bandwidth_package", _client=_client)
        self.bandwidth_package_id = bandwidth_package_id

        self.bandwidth = None
        self.business_status = None
        self.creation_time = None
        self.description = None
        self.isp = None
        self.instance_charge_type = None
        self.internet_charge_type = None
        self.ip_count = None
        self.name = None
        self.nat_gateway_id = None
        self.public_ip_addresses = None
        self.region_id = None
        self.status = None
        self.zone_id = None

    def add_bandwidth_package_ips(self, **params):
        _params = _transfer_params(params)
        self._client.add_bandwidth_package_ips(bandwidth_package_id=self.bandwidth_package_id,
                                               **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_bandwidth_package(bandwidth_package_id=self.bandwidth_package_id,
                                              **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_bandwidth_package_spec(bandwidth_package_id=self.bandwidth_package_id,
                                                   **_params)

    def remove_bandwidth_package_ips(self, **params):
        _params = _transfer_params(params)
        self._client.remove_bandwidth_package_ips(bandwidth_package_id=self.bandwidth_package_id,
                                                  **_params)

    def refresh(self):
        result = self._client.describe_bandwidth_packages(
            bandwidth_package_id=self.bandwidth_package_id)
        items = _new_get_key_in_response(result, 'BandwidthPackages.BandwidthPackage')
        if not items:
            raise ClientException(msg=
                                  "Failed to find bandwidth_package data from DescribeBandwidthPackages response. "
                                  "BandwidthPackageId = {0}".format(self.bandwidth_package_id))
        self._assign_attributes(items[0])


class _ECSClusterResource(ServiceResource):

    def __init__(self, cluster_id, _client=None):
        ServiceResource.__init__(self, "ecs.cluster", _client=_client)
        self.cluster_id = cluster_id


class _ECSCommandResource(ServiceResource):

    def __init__(self, command_id, _client=None):
        ServiceResource.__init__(self, "ecs.command", _client=_client)
        self.command_id = command_id

        self.command_content = None
        self.creation_time = None
        self.description = None
        self.enable_parameter = None
        self.name = None
        self.parameter_names = None
        self.timeout = None
        self.type_ = None
        self.working_dir = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_command(command_id=self.command_id, **_params)

    def invoke(self, **params):
        _params = _transfer_params(params)
        self._client.invoke_command(command_id=self.command_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        self._client.modify_command(command_id=self.command_id, **_params)

    def refresh(self):
        result = self._client.describe_commands(command_id=self.command_id)
        items = _new_get_key_in_response(result, 'Commands.Command')
        if not items:
            raise ClientException(msg=
                                  "Failed to find command data from DescribeCommands response. "
                                  "CommandId = {0}".format(self.command_id))
        self._assign_attributes(items[0])


class _ECSDedicatedHostResource(ServiceResource):

    def __init__(self, dedicated_host_id, _client=None):
        ServiceResource.__init__(self, "ecs.dedicated_host", _client=_client)
        self.dedicated_host_id = dedicated_host_id

        self.action_on_maintenance = None
        self.auto_placement = None
        self.auto_release_time = None
        self.capacity = None
        self.charge_type = None
        self.cores = None
        self.creation_time = None
        self.dedicated_host_name = None
        self.dedicated_host_type = None
        self.description = None
        self.expired_time = None
        self.gpu_spec = None
        self.instances = None
        self.machine_id = None
        self.network_attributes = None
        self.operation_locks = None
        self.physical_gpus = None
        self.region_id = None
        self.resource_group_id = None
        self.sale_cycle = None
        self.sockets = None
        self.status = None
        self.supported_instance_type_families = None
        self.supported_instance_types_list = None
        self.tags = None
        self.zone_id = None

    def modify_auto_renew_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_dedicated_host_auto_renew_attribute(
            dedicated_host_id=self.dedicated_host_id, **_params)

    def renew(self, **params):
        _params = _transfer_params(params)
        self._client.renew_dedicated_hosts(dedicated_host_id=self.dedicated_host_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_dedicated_host_attribute(dedicated_host_id=self.dedicated_host_id,
                                                     **_params)

    def modify_auto_release_time(self, **params):
        _params = _transfer_params(params)
        self._client.modify_dedicated_host_auto_release_time(
            dedicated_host_id=self.dedicated_host_id, **_params)

    def release(self, **params):
        _params = _transfer_params(params)
        self._client.release_dedicated_host(dedicated_host_id=self.dedicated_host_id, **_params)

    def refresh(self):
        result = self._client.describe_dedicated_hosts(dedicated_host_ids=self.dedicated_host_id)
        items = _new_get_key_in_response(result, 'DedicatedHosts.DedicatedHost')
        if not items:
            raise ClientException(msg=
                                  "Failed to find dedicated_host data from DescribeDedicatedHosts response. "
                                  "DedicatedHostId = {0}".format(self.dedicated_host_id))
        self._assign_attributes(items[0])

    def wait_until(self, target_status, timeout=120):
        start_time = time.time()
        while True:
            end_time = time.time()
            if end_time - start_time >= timeout:
                raise Exception("Timed out: no {0} status after {1} seconds.".format(
                    target_status, timeout))

            self.refresh()
            if self.status == target_status:
                return
            time.sleep(1)


class _ECSDeploymentSetResource(ServiceResource):

    def __init__(self, deployment_set_id, _client=None):
        ServiceResource.__init__(self, "ecs.deployment_set", _client=_client)
        self.deployment_set_id = deployment_set_id

        self.creation_time = None
        self.deployment_set_description = None
        self.deployment_set_name = None
        self.deployment_strategy = None
        self.domain = None
        self.granularity = None
        self.instance_amount = None
        self.instance_ids = None
        self.strategy = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_deployment_set(deployment_set_id=self.deployment_set_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_deployment_set_attribute(deployment_set_id=self.deployment_set_id,
                                                     **_params)

    def refresh(self):
        result = self._client.describe_deployment_sets(deployment_set_ids=self.deployment_set_id)
        items = _new_get_key_in_response(result, 'DeploymentSets.DeploymentSet')
        if not items:
            raise ClientException(msg=
                                  "Failed to find deployment_set data from DescribeDeploymentSets response. "
                                  "DeploymentSetId = {0}".format(self.deployment_set_id))
        self._assign_attributes(items[0])


class _ECSDiskResource(ServiceResource):

    def __init__(self, disk_id, _client=None):
        ServiceResource.__init__(self, "ecs.disk", _client=_client)
        self.disk_id = disk_id

        self.attached_time = None
        self.auto_snapshot_policy_id = None
        self.bdf_id = None
        self.category = None
        self.creation_time = None
        self.delete_auto_snapshot = None
        self.delete_with_instance = None
        self.description = None
        self.detached_time = None
        self.device = None
        self.disk_charge_type = None
        self.disk_name = None
        self.enable_auto_snapshot = None
        self.enable_automated_snapshot_policy = None
        self.encrypted = None
        self.expired_time = None
        self.iops = None
        self.iops_read = None
        self.iops_write = None
        self.image_id = None
        self.instance_id = None
        self.kms_key_id = None
        self.mount_instance_num = None
        self.mount_instances = None
        self.operation_locks = None
        self.performance_level = None
        self.portable = None
        self.product_code = None
        self.region_id = None
        self.resource_group_id = None
        self.size = None
        self.source_snapshot_id = None
        self.status = None
        self.storage_set_id = None
        self.storage_set_partition_number = None
        self.tags = None
        self.type_ = None
        self.zone_id = None

    def cancel_auto_snapshot_policy(self, **params):
        _params = _transfer_params(params)
        self._client.cancel_auto_snapshot_policy(disk_id=self.disk_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_disk(disk_id=self.disk_id, **_params)

    def describe_disk_monitor_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_disk_monitor_data(disk_id=self.disk_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_disk_attribute(disk_id=self.disk_id, **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_disk_spec(disk_id=self.disk_id, **_params)

    def reinit(self, **params):
        _params = _transfer_params(params)
        self._client.reinit_disk(disk_id=self.disk_id, **_params)

    def resize(self, **params):
        _params = _transfer_params(params)
        self._client.resize_disk(disk_id=self.disk_id, **_params)

    def attach(self, **params):
        _params = _transfer_params(params)
        self._client.attach_disk(disk_id=self.disk_id, **_params)

    def detach(self, **params):
        _params = _transfer_params(params)
        self._client.detach_disk(disk_id=self.disk_id, **_params)

    def reset(self, **params):
        _params = _transfer_params(params)
        self._client.reset_disk(disk_id=self.disk_id, **_params)

    def refresh(self):
        result = self._client.describe_disks(disk_ids=self.disk_id)
        items = _new_get_key_in_response(result, 'Disks.Disk')
        if not items:
            raise ClientException(msg=
                                  "Failed to find disk data from DescribeDisks response. "
                                  "DiskId = {0}".format(self.disk_id))
        self._assign_attributes(items[0])


class _ECSEipAddressResource(ServiceResource):

    def __init__(self, allocation_id, _client=None):
        ServiceResource.__init__(self, "ecs.eip_address", _client=_client)
        self.allocation_id = allocation_id

        self.allocation_time = None
        self.bandwidth = None
        self.charge_type = None
        self.eip_bandwidth = None
        self.expired_time = None
        self.instance_id = None
        self.instance_type = None
        self.internet_charge_type = None
        self.ip_address = None
        self.operation_locks = None
        self.region_id = None
        self.status = None

    def describe_eip_monitor_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_eip_monitor_data(allocation_id=self.allocation_id, **_params)

    def describe_new_project_eip_monitor_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_new_project_eip_monitor_data(allocation_id=self.allocation_id,
                                                           **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_eip_address_attribute(allocation_id=self.allocation_id, **_params)

    def release(self, **params):
        _params = _transfer_params(params)
        self._client.release_eip_address(allocation_id=self.allocation_id, **_params)

    def associate(self, **params):
        _params = _transfer_params(params)
        self._client.associate_eip_address(allocation_id=self.allocation_id, **_params)

    def unassociate(self, **params):
        _params = _transfer_params(params)
        self._client.unassociate_eip_address(allocation_id=self.allocation_id, **_params)

    def refresh(self):
        result = self._client.describe_eip_addresses(allocation_id=self.allocation_id)
        items = _new_get_key_in_response(result, 'EipAddresses.EipAddress')
        if not items:
            raise ClientException(msg=
                                  "Failed to find eip_address data from DescribeEipAddresses response. "
                                  "AllocationId = {0}".format(self.allocation_id))
        self._assign_attributes(items[0])


class _ECSFleetResource(ServiceResource):

    def __init__(self, fleet_id, _client=None):
        ServiceResource.__init__(self, "ecs.fleet", _client=_client)
        self.fleet_id = fleet_id

        self.creation_time = None
        self.excess_capacity_termination_policy = None
        self.fleet_name = None
        self.fleet_type = None
        self.launch_template_id = None
        self.launch_template_version = None
        self.max_spot_price = None
        self.on_demand_options = None
        self.region_id = None
        self.spot_options = None
        self.state = None
        self.status = None
        self.target_capacity_specification = None
        self.terminate_instances = None
        self.terminate_instances_with_expiration = None
        self.valid_from = None
        self.valid_until = None
        self.launch_template_configs = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_fleet(fleet_id=self.fleet_id, **_params)

    def describe_fleet_history(self, **params):
        _params = _transfer_params(params)
        self._client.describe_fleet_history(fleet_id=self.fleet_id, **_params)

    def describe_fleet_instances(self, **params):
        _params = _transfer_params(params)
        self._client.describe_fleet_instances(fleet_id=self.fleet_id, **_params)

    def refresh(self):
        result = self._client.describe_fleets(list_of_fleet_id=[self.fleet_id, ])
        items = _new_get_key_in_response(result, 'Fleets.Fleet')
        if not items:
            raise ClientException(msg=
                                  "Failed to find fleet data from DescribeFleets response. "
                                  "FleetId = {0}".format(self.fleet_id))
        self._assign_attributes(items[0])


class _ECSHaVipResource(ServiceResource):

    def __init__(self, ha_vip_id, _client=None):
        ServiceResource.__init__(self, "ecs.ha_vip", _client=_client)
        self.ha_vip_id = ha_vip_id

        self.associated_eip_addresses = None
        self.associated_instances = None
        self.create_time = None
        self.description = None
        self.ip_address = None
        self.master_instance_id = None
        self.region_id = None
        self.status = None
        self.vswitch_id = None
        self.vpc_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_ha_vip(ha_vip_id=self.ha_vip_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_ha_vip_attribute(ha_vip_id=self.ha_vip_id, **_params)

    def associate(self, **params):
        _params = _transfer_params(params)
        self._client.associate_ha_vip(ha_vip_id=self.ha_vip_id, **_params)

    def unassociate(self, **params):
        _params = _transfer_params(params)
        self._client.unassociate_ha_vip(ha_vip_id=self.ha_vip_id, **_params)


class _ECSHpcClusterResource(ServiceResource):

    def __init__(self, hpc_cluster_id, _client=None):
        ServiceResource.__init__(self, "ecs.hpc_cluster", _client=_client)
        self.hpc_cluster_id = hpc_cluster_id

        self.description = None
        self.name = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_hpc_cluster(hpc_cluster_id=self.hpc_cluster_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_hpc_cluster_attribute(hpc_cluster_id=self.hpc_cluster_id, **_params)

    def refresh(self):
        result = self._client.describe_hpc_clusters(hpc_cluster_ids=self.hpc_cluster_id)
        items = _new_get_key_in_response(result, 'HpcClusters.HpcCluster')
        if not items:
            raise ClientException(msg=
                                  "Failed to find hpc_cluster data from DescribeHpcClusters response. "
                                  "HpcClusterId = {0}".format(self.hpc_cluster_id))
        self._assign_attributes(items[0])


class _ECSImageResource(ServiceResource):

    def __init__(self, image_id, _client=None):
        ServiceResource.__init__(self, "ecs.image", _client=_client)
        self.image_id = image_id

        self.architecture = None
        self.creation_time = None
        self.description = None
        self.disk_device_mappings = None
        self.image_name = None
        self.image_owner_alias = None
        self.image_version = None
        self.is_copied = None
        self.is_self_shared = None
        self.is_subscribed = None
        self.is_support_cloudinit = None
        self.is_support_io_optimized = None
        self.os_name = None
        self.os_name_en = None
        self.os_type = None
        self.platform = None
        self.product_code = None
        self.progress = None
        self.resource_group_id = None
        self.size = None
        self.status = None
        self.tags = None
        self.usage = None

    def cancel_copy(self, **params):
        _params = _transfer_params(params)
        self._client.cancel_copy_image(image_id=self.image_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_image(image_id=self.image_id, **_params)

    def describe_image_share_permission(self, **params):
        _params = _transfer_params(params)
        self._client.describe_image_share_permission(image_id=self.image_id, **_params)

    def export(self, **params):
        _params = _transfer_params(params)
        self._client.export_image(image_id=self.image_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_image_attribute(image_id=self.image_id, **_params)

    def modify_share_group_permission(self, **params):
        _params = _transfer_params(params)
        self._client.modify_image_share_group_permission(image_id=self.image_id, **_params)

    def modify_share_permission(self, **params):
        _params = _transfer_params(params)
        self._client.modify_image_share_permission(image_id=self.image_id, **_params)

    def refresh(self):
        result = self._client.describe_images(image_id=self.image_id)
        items = _new_get_key_in_response(result, 'Images.Image')
        if not items:
            raise ClientException(msg=
                                  "Failed to find image data from DescribeImages response. "
                                  "ImageId = {0}".format(self.image_id))
        self._assign_attributes(items[0])


class _ECSInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "ecs.instance", _client=_client)
        self.instance_id = instance_id

        self.auto_release_time = None
        self.cluster_id = None
        self.cpu = None
        self.creation_time = None
        self.credit_specification = None
        self.dedicated_host_attribute = None
        self.dedicated_instance_attribute = None
        self.deletion_protection = None
        self.deployment_set_id = None
        self.description = None
        self.device_available = None
        self.ecs_capacity_reservation_attr = None
        self.eip_address = None
        self.expired_time = None
        self.gpu_amount = None
        self.gpu_spec = None
        self.host_name = None
        self.hpc_cluster_id = None
        self.image_id = None
        self.inner_ip_address = None
        self.instance_charge_type = None
        self.instance_name = None
        self.instance_network_type = None
        self.instance_type = None
        self.instance_type_family = None
        self.internet_charge_type = None
        self.internet_max_bandwidth_in = None
        self.internet_max_bandwidth_out = None
        self.io_optimized = None
        self.key_pair_name = None
        self.local_storage_amount = None
        self.local_storage_capacity = None
        self.memory = None
        self.network_interfaces = None
        self.os_name = None
        self.os_name_en = None
        self.os_type = None
        self.operation_locks = None
        self.public_ip_address = None
        self.rdma_ip_address = None
        self.recyclable = None
        self.region_id = None
        self.resource_group_id = None
        self.sale_cycle = None
        self.security_group_ids = None
        self.serial_number = None
        self.spot_price_limit = None
        self.spot_strategy = None
        self.start_time = None
        self.status = None
        self.stopped_mode = None
        self.tags = None
        self.vlan_id = None
        self.vpc_attributes = None
        self.zone_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_instances(instance_id=self.instance_id, **_params)

    def install_cloud_assistant(self, **params):
        _params = _transfer_params(params)
        self._client.install_cloud_assistant(instance_id=self.instance_id, **_params)

    def report_instances_status(self, **params):
        _params = _transfer_params(params)
        self._client.report_instances_status(instance_id=self.instance_id, **_params)

    def allocate_public_ip_address(self, **params):
        _params = _transfer_params(params)
        self._client.allocate_public_ip_address(instance_id=self.instance_id, **_params)

    def attach_classic_link_vpc(self, **params):
        _params = _transfer_params(params)
        self._client.attach_classic_link_vpc(instance_id=self.instance_id, **_params)

    def convert_nat_public_ip_to_eip(self, **params):
        _params = _transfer_params(params)
        self._client.convert_nat_public_ip_to_eip(instance_id=self.instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_instance(instance_id=self.instance_id, **_params)

    def describe_eni_monitor_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_eni_monitor_data(instance_id=self.instance_id, **_params)

    def describe_instance_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_instance_attribute(instance_id=self.instance_id, **_params)

    def describe_instance_monitor_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_instance_monitor_data(instance_id=self.instance_id, **_params)

    def describe_instance_physical_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_instance_physical_attribute(instance_id=self.instance_id, **_params)

    def describe_instance_vnc_passwd(self, **params):
        _params = _transfer_params(params)
        self._client.describe_instance_vnc_passwd(instance_id=self.instance_id, **_params)

    def describe_instance_vnc_url(self, **params):
        _params = _transfer_params(params)
        self._client.describe_instance_vnc_url(instance_id=self.instance_id, **_params)

    def describe_user_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_user_data(instance_id=self.instance_id, **_params)

    def detach_classic_link_vpc(self, **params):
        _params = _transfer_params(params)
        self._client.detach_classic_link_vpc(instance_id=self.instance_id, **_params)

    def get_instance_console_output(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_instance_console_output(instance_id=self.instance_id, **_params)
        return response

    def get_instance_screenshot(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_instance_screenshot(instance_id=self.instance_id, **_params)
        return response

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_attribute(instance_id=self.instance_id, **_params)

    def modify_auto_release_time(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_auto_release_time(instance_id=self.instance_id, **_params)

    def modify_auto_renew_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_auto_renew_attribute(instance_id=self.instance_id, **_params)

    def modify_deployment(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_deployment(instance_id=self.instance_id, **_params)

    def modify_disk_charge_type(self, **params):
        _params = _transfer_params(params)
        self._client.modify_disk_charge_type(instance_id=self.instance_id, **_params)

    def modify_network_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_network_spec(instance_id=self.instance_id, **_params)

    def modify_prepay_instance_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_prepay_instance_spec(instance_id=self.instance_id, **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_spec(instance_id=self.instance_id, **_params)

    def modify_vnc_passwd(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_vnc_passwd(instance_id=self.instance_id, **_params)

    def reactivate(self, **params):
        _params = _transfer_params(params)
        self._client.reactivate_instances(instance_id=self.instance_id, **_params)

    def reboot(self, **params):
        _params = _transfer_params(params)
        self._client.reboot_instance(instance_id=self.instance_id, **_params)

    def redeploy(self, **params):
        _params = _transfer_params(params)
        self._client.redeploy_instance(instance_id=self.instance_id, **_params)

    def renew(self, **params):
        _params = _transfer_params(params)
        self._client.renew_instance(instance_id=self.instance_id, **_params)

    def replace_system_disk(self, **params):
        _params = _transfer_params(params)
        response = self._client.replace_system_disk(instance_id=self.instance_id, **_params)
        return response['DiskId']

    def start(self, **params):
        _params = _transfer_params(params)
        self._client.start_instance(instance_id=self.instance_id, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        self._client.stop_instance(instance_id=self.instance_id, **_params)

    def modify_vpc_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_vpc_attribute(instance_id=self.instance_id, **_params)

    def refresh(self):
        result = self._client.describe_instances(instance_ids=self.instance_id)
        items = _new_get_key_in_response(result, 'Instances.Instance')
        if not items:
            raise ClientException(msg=
                                  "Failed to find instance data from DescribeInstances response. "
                                  "InstanceId = {0}".format(self.instance_id))
        self._assign_attributes(items[0])

    def wait_until(self, target_status, timeout=120):
        start_time = time.time()
        while True:
            end_time = time.time()
            if end_time - start_time >= timeout:
                raise Exception("Timed out: no {0} status after {1} seconds.".format(
                    target_status, timeout))

            self.refresh()
            if self.status == target_status:
                return
            time.sleep(1)


class _ECSInstanceTypeResource(ServiceResource):

    def __init__(self, instance_type_id, _client=None):
        ServiceResource.__init__(self, "ecs.instance_type", _client=_client)
        self.instance_type_id = instance_type_id

        self.baseline_credit = None
        self.cpu_core_count = None
        self.eni_private_ip_address_quantity = None
        self.eni_quantity = None
        self.gpu_amount = None
        self.gpu_spec = None
        self.initial_credit = None
        self.instance_bandwidth_rx = None
        self.instance_bandwidth_tx = None
        self.instance_family_level = None
        self.instance_pps_rx = None
        self.instance_pps_tx = None
        self.instance_type_family = None
        self.local_storage_amount = None
        self.local_storage_capacity = None
        self.local_storage_category = None
        self.memory_size = None


class _ECSKeyPairResource(ServiceResource):

    def __init__(self, key_pair_name, _client=None):
        ServiceResource.__init__(self, "ecs.key_pair", _client=_client)
        self.key_pair_name = key_pair_name

        self.key_pair_finger_print = None
        self.resource_group_id = None
        self.tags = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_key_pairs(key_pair_name=self.key_pair_name, **_params)

    def attach(self, **params):
        _params = _transfer_params(params)
        self._client.attach_key_pair(key_pair_name=self.key_pair_name, **_params)

    def detach(self, **params):
        _params = _transfer_params(params)
        self._client.detach_key_pair(key_pair_name=self.key_pair_name, **_params)

    def refresh(self):
        result = self._client.describe_key_pairs(key_pair_name=self.key_pair_name)
        items = _new_get_key_in_response(result, 'KeyPairs.KeyPair')
        if not items:
            raise ClientException(msg=
                                  "Failed to find key_pair data from DescribeKeyPairs response. "
                                  "KeyPairName = {0}".format(self.key_pair_name))
        self._assign_attributes(items[0])


class _ECSLaunchTemplateResource(ServiceResource):

    def __init__(self, launch_template_id, _client=None):
        ServiceResource.__init__(self, "ecs.launch_template", _client=_client)
        self.launch_template_id = launch_template_id

        self.create_time = None
        self.created_by = None
        self.default_version_number = None
        self.latest_version_number = None
        self.launch_template_name = None
        self.modified_time = None
        self.resource_group_id = None
        self.tags = None

    def refresh(self):
        result = self._client.describe_launch_templates(
            list_of_launch_template_id=[self.launch_template_id, ])
        items = _new_get_key_in_response(result, 'LaunchTemplateSets.LaunchTemplateSet')
        if not items:
            raise ClientException(msg=
                                  "Failed to find launch_template data from DescribeLaunchTemplates response. "
                                  "LaunchTemplateId = {0}".format(self.launch_template_id))
        self._assign_attributes(items[0])


class _ECSNatGatewayResource(ServiceResource):

    def __init__(self, nat_gateway_id, _client=None):
        ServiceResource.__init__(self, "ecs.nat_gateway", _client=_client)
        self.nat_gateway_id = nat_gateway_id

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_nat_gateway(nat_gateway_id=self.nat_gateway_id, **_params)


class _ECSNetworkInterfaceResource(ServiceResource):

    def __init__(self, network_interface_id, _client=None):
        ServiceResource.__init__(self, "ecs.network_interface", _client=_client)
        self.network_interface_id = network_interface_id

        self.associated_public_ip = None
        self.creation_time = None
        self.description = None
        self.instance_id = None
        self.ipv6_sets = None
        self.mac_address = None
        self.network_interface_name = None
        self.private_ip_address = None
        self.private_ip_sets = None
        self.resource_group_id = None
        self.security_group_ids = None
        self.service_id = None
        self.service_managed = None
        self.status = None
        self.tags = None
        self.type_ = None
        self.vswitch_id = None
        self.vpc_id = None
        self.zone_id = None

    def assign_ipv6_addresses(self, **params):
        _params = _transfer_params(params)
        self._client.assign_ipv6_addresses(network_interface_id=self.network_interface_id,
                                           **_params)

    def assign_private_ip_addresses(self, **params):
        _params = _transfer_params(params)
        self._client.assign_private_ip_addresses(network_interface_id=self.network_interface_id,
                                                 **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_network_interface(network_interface_id=self.network_interface_id,
                                              **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_network_interface_attribute(
            network_interface_id=self.network_interface_id, **_params)

    def unassign_ipv6_addresses(self, **params):
        _params = _transfer_params(params)
        self._client.unassign_ipv6_addresses(network_interface_id=self.network_interface_id,
                                             **_params)

    def unassign_private_ip_addresses(self, **params):
        _params = _transfer_params(params)
        self._client.unassign_private_ip_addresses(network_interface_id=self.network_interface_id,
                                                   **_params)

    def attach(self, **params):
        _params = _transfer_params(params)
        self._client.attach_network_interface(network_interface_id=self.network_interface_id,
                                              **_params)

    def create_network_interface_permission(self, **params):
        _params = _transfer_params(params)
        self._client.create_network_interface_permission(
            network_interface_id=self.network_interface_id, **_params)

    def detach(self, **params):
        _params = _transfer_params(params)
        self._client.detach_network_interface(network_interface_id=self.network_interface_id,
                                              **_params)

    def refresh(self):
        result = self._client.describe_network_interfaces(
            list_of_network_interface_id=[self.network_interface_id, ])
        items = _new_get_key_in_response(result, 'NetworkInterfaceSets.NetworkInterfaceSet')
        if not items:
            raise ClientException(msg=
                                  "Failed to find network_interface data from DescribeNetworkInterfaces response. "
                                  "NetworkInterfaceId = {0}".format(self.network_interface_id))
        self._assign_attributes(items[0])


class _ECSNetworkInterfacePermissionResource(ServiceResource):

    def __init__(self, network_interface_permission_id, _client=None):
        ServiceResource.__init__(self, "ecs.network_interface_permission", _client=_client)
        self.network_interface_permission_id = network_interface_permission_id

        self.account_id = None
        self.network_interface_id = None
        self.permission = None
        self.permission_state = None
        self.service_name = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_network_interface_permission(
            network_interface_permission_id=self.network_interface_permission_id, **_params)

    def refresh(self):
        result = self._client.describe_network_interface_permissions(
            list_of_network_interface_permission_id=[self.network_interface_permission_id, ])
        items = _new_get_key_in_response(result,
                                         'NetworkInterfacePermissions.NetworkInterfacePermission')
        if not items:
            raise ClientException(msg=
                                  "Failed to find network_interface_permission data from DescribeNetworkInterfacePermissions response. "
                                  "NetworkInterfacePermissionId = {0}".format(
                                      self.network_interface_permission_id))
        self._assign_attributes(items[0])


class _ECSPhysicalConnectionResource(ServiceResource):

    def __init__(self, physical_connection_id, _client=None):
        ServiceResource.__init__(self, "ecs.physical_connection", _client=_client)
        self.physical_connection_id = physical_connection_id

        self.access_point_id = None
        self.ad_location = None
        self.bandwidth = None
        self.business_status = None
        self.circuit_code = None
        self.creation_time = None
        self.description = None
        self.enabled_time = None
        self.line_operator = None
        self.name = None
        self.peer_location = None
        self.port_number = None
        self.port_type = None
        self.redundant_physical_connection_id = None
        self.spec = None
        self.status = None
        self.type_ = None

    def cancel(self, **params):
        _params = _transfer_params(params)
        self._client.cancel_physical_connection(physical_connection_id=self.physical_connection_id,
                                                **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_physical_connection(physical_connection_id=self.physical_connection_id,
                                                **_params)

    def describe_virtual_border_routers_for(self, **params):
        _params = _transfer_params(params)
        self._client.describe_virtual_border_routers_for_physical_connection(
            physical_connection_id=self.physical_connection_id, **_params)

    def enable(self, **params):
        _params = _transfer_params(params)
        self._client.enable_physical_connection(physical_connection_id=self.physical_connection_id,
                                                **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_physical_connection_attribute(
            physical_connection_id=self.physical_connection_id, **_params)

    def terminate(self, **params):
        _params = _transfer_params(params)
        self._client.terminate_physical_connection(
            physical_connection_id=self.physical_connection_id, **_params)


class _ECSRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "ecs.region", _client=_client)
        self.region_id = region_id

        self.local_name = None
        self.region_endpoint = None
        self.status = None

    def refresh(self):
        result = self._client.describe_regions(region_id=self.region_id)
        items = _new_get_key_in_response(result, 'Regions.Region')
        if not items:
            raise ClientException(msg=
                                  "Failed to find region data from DescribeRegions response. "
                                  "RegionId = {0}".format(self.region_id))
        self._assign_attributes(items[0])


class _ECSReservedInstanceResource(ServiceResource):

    def __init__(self, reserved_instance_id, _client=None):
        ServiceResource.__init__(self, "ecs.reserved_instance", _client=_client)
        self.reserved_instance_id = reserved_instance_id

        self.creation_time = None
        self.description = None
        self.expired_time = None
        self.instance_amount = None
        self.instance_type = None
        self.offering_type = None
        self.operation_locks = None
        self.platform = None
        self.region_id = None
        self.reserved_instance_name = None
        self.resource_group_id = None
        self.scope = None
        self.start_time = None
        self.status = None
        self.zone_id = None

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_reserved_instance_attribute(
            reserved_instance_id=self.reserved_instance_id, **_params)

    def refresh(self):
        result = self._client.describe_reserved_instances(
            list_of_reserved_instance_id=[self.reserved_instance_id, ])
        items = _new_get_key_in_response(result, 'ReservedInstances.ReservedInstance')
        if not items:
            raise ClientException(msg=
                                  "Failed to find reserved_instance data from DescribeReservedInstances response. "
                                  "ReservedInstanceId = {0}".format(self.reserved_instance_id))
        self._assign_attributes(items[0])

    def wait_until(self, target_status, timeout=120):
        start_time = time.time()
        while True:
            end_time = time.time()
            if end_time - start_time >= timeout:
                raise Exception("Timed out: no {0} status after {1} seconds.".format(
                    target_status, timeout))

            self.refresh()
            if self.status == target_status:
                return
            time.sleep(1)


class _ECSRouteTableResource(ServiceResource):

    def __init__(self, route_table_id, _client=None):
        ServiceResource.__init__(self, "ecs.route_table", _client=_client)
        self.route_table_id = route_table_id

        self.creation_time = None
        self.resource_group_id = None
        self.route_entrys = None
        self.route_table_type = None
        self.vrouter_id = None

    def create_route_entry(self, **params):
        _params = _transfer_params(params)
        self._client.create_route_entry(route_table_id=self.route_table_id, **_params)

    def delete_route_entry(self, **params):
        _params = _transfer_params(params)
        self._client.delete_route_entry(route_table_id=self.route_table_id, **_params)

    def refresh(self):
        result = self._client.describe_route_tables(route_table_id=self.route_table_id)
        items = _new_get_key_in_response(result, 'RouteTables.RouteTable')
        if not items:
            raise ClientException(msg=
                                  "Failed to find route_table data from DescribeRouteTables response. "
                                  "RouteTableId = {0}".format(self.route_table_id))
        self._assign_attributes(items[0])


class _ECSRouterInterfaceResource(ServiceResource):

    def __init__(self, router_interface_id, _client=None):
        ServiceResource.__init__(self, "ecs.router_interface", _client=_client)
        self.router_interface_id = router_interface_id

        self.access_point_id = None
        self.business_status = None
        self.charge_type = None
        self.connected_time = None
        self.creation_time = None
        self.description = None
        self.end_time = None
        self.health_check_source_ip = None
        self.health_check_target_ip = None
        self.name = None
        self.opposite_access_point_id = None
        self.opposite_interface_business_status = None
        self.opposite_interface_id = None
        self.opposite_interface_owner_id = None
        self.opposite_interface_spec = None
        self.opposite_interface_status = None
        self.opposite_region_id = None
        self.opposite_router_id = None
        self.opposite_router_type = None
        self.role = None
        self.router_id = None
        self.router_type = None
        self.spec = None
        self.status = None

    def activate(self, **params):
        _params = _transfer_params(params)
        self._client.activate_router_interface(router_interface_id=self.router_interface_id,
                                               **_params)

    def connect(self, **params):
        _params = _transfer_params(params)
        self._client.connect_router_interface(router_interface_id=self.router_interface_id,
                                              **_params)

    def deactivate(self, **params):
        _params = _transfer_params(params)
        self._client.deactivate_router_interface(router_interface_id=self.router_interface_id,
                                                 **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_router_interface(router_interface_id=self.router_interface_id,
                                             **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_router_interface_attribute(router_interface_id=self.router_interface_id,
                                                       **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_router_interface_spec(router_interface_id=self.router_interface_id,
                                                  **_params)


class _ECSSecurityGroupResource(ServiceResource):

    def __init__(self, security_group_id, _client=None):
        ServiceResource.__init__(self, "ecs.security_group", _client=_client)
        self.security_group_id = security_group_id

        self.available_instance_amount = None
        self.creation_time = None
        self.description = None
        self.ecs_count = None
        self.resource_group_id = None
        self.security_group_name = None
        self.security_group_type = None
        self.tags = None
        self.vpc_id = None

    def authorize(self, **params):
        _params = _transfer_params(params)
        self._client.authorize_security_group(security_group_id=self.security_group_id, **_params)

    def authorize_security_group_egress(self, **params):
        _params = _transfer_params(params)
        self._client.authorize_security_group_egress(security_group_id=self.security_group_id,
                                                     **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_security_group(security_group_id=self.security_group_id, **_params)

    def describe_security_group_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_security_group_attribute(security_group_id=self.security_group_id,
                                                       **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_security_group_attribute(security_group_id=self.security_group_id,
                                                     **_params)

    def modify_egress_rule(self, **params):
        _params = _transfer_params(params)
        self._client.modify_security_group_egress_rule(security_group_id=self.security_group_id,
                                                       **_params)

    def modify_policy(self, **params):
        _params = _transfer_params(params)
        self._client.modify_security_group_policy(security_group_id=self.security_group_id,
                                                  **_params)

    def modify_rule(self, **params):
        _params = _transfer_params(params)
        self._client.modify_security_group_rule(security_group_id=self.security_group_id, **_params)

    def revoke(self, **params):
        _params = _transfer_params(params)
        self._client.revoke_security_group(security_group_id=self.security_group_id, **_params)

    def revoke_security_group_egress(self, **params):
        _params = _transfer_params(params)
        self._client.revoke_security_group_egress(security_group_id=self.security_group_id,
                                                  **_params)

    def join(self, **params):
        _params = _transfer_params(params)
        self._client.join_security_group(security_group_id=self.security_group_id, **_params)

    def leave(self, **params):
        _params = _transfer_params(params)
        self._client.leave_security_group(security_group_id=self.security_group_id, **_params)

    def refresh(self):
        result = self._client.describe_security_groups(security_group_ids=self.security_group_id)
        items = _new_get_key_in_response(result, 'SecurityGroups.SecurityGroup')
        if not items:
            raise ClientException(msg=
                                  "Failed to find security_group data from DescribeSecurityGroups response. "
                                  "SecurityGroupId = {0}".format(self.security_group_id))
        self._assign_attributes(items[0])


class _ECSSnapshotResource(ServiceResource):

    def __init__(self, snapshot_id, _client=None):
        ServiceResource.__init__(self, "ecs.snapshot", _client=_client)
        self.snapshot_id = snapshot_id

        self.creation_time = None
        self.description = None
        self.encrypted = None
        self.kms_key_id = None
        self.last_modified_time = None
        self.product_code = None
        self.progress = None
        self.remain_time = None
        self.resource_group_id = None
        self.retention_days = None
        self.snapshot_name = None
        self.source_disk_id = None
        self.source_disk_size = None
        self.source_disk_type = None
        self.source_storage_type = None
        self.status = None
        self.tags = None
        self.usage = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_snapshot(snapshot_id=self.snapshot_id, **_params)

    def export(self, **params):
        _params = _transfer_params(params)
        self._client.export_snapshot(snapshot_id=self.snapshot_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_snapshot_attribute(snapshot_id=self.snapshot_id, **_params)

    def refresh(self):
        result = self._client.describe_snapshots(snapshot_ids=self.snapshot_id)
        items = _new_get_key_in_response(result, 'Snapshots.Snapshot')
        if not items:
            raise ClientException(msg=
                                  "Failed to find snapshot data from DescribeSnapshots response. "
                                  "SnapshotId = {0}".format(self.snapshot_id))
        self._assign_attributes(items[0])


class _ECSSnapshotLinkResource(ServiceResource):

    def __init__(self, snapshot_link_id, _client=None):
        ServiceResource.__init__(self, "ecs.snapshot_link", _client=_client)
        self.snapshot_link_id = snapshot_link_id

        self.instance_id = None
        self.instance_name = None
        self.region_id = None
        self.source_disk_id = None
        self.source_disk_name = None
        self.source_disk_size = None
        self.source_disk_type = None
        self.total_count = None
        self.total_size = None

    def refresh(self):
        result = self._client.describe_snapshot_links(snapshot_link_ids=self.snapshot_link_id)
        items = _new_get_key_in_response(result, 'SnapshotLinks.SnapshotLink')
        if not items:
            raise ClientException(msg=
                                  "Failed to find snapshot_link data from DescribeSnapshotLinks response. "
                                  "SnapshotLinkId = {0}".format(self.snapshot_link_id))
        self._assign_attributes(items[0])


class _ECSStorageSetResource(ServiceResource):

    def __init__(self, storage_set_id, _client=None):
        ServiceResource.__init__(self, "ecs.storage_set", _client=_client)
        self.storage_set_id = storage_set_id

        self.creation_time = None
        self.description = None
        self.region_id = None
        self.storage_set_name = None
        self.storage_set_partition_number = None
        self.zone_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_storage_set(storage_set_id=self.storage_set_id, **_params)

    def describe_storage_set_details(self, **params):
        _params = _transfer_params(params)
        self._client.describe_storage_set_details(storage_set_id=self.storage_set_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_storage_set_attribute(storage_set_id=self.storage_set_id, **_params)

    def refresh(self):
        result = self._client.describe_storage_sets(storage_set_ids=self.storage_set_id)
        items = _new_get_key_in_response(result, 'StorageSets.StorageSet')
        if not items:
            raise ClientException(msg=
                                  "Failed to find storage_set data from DescribeStorageSets response. "
                                  "StorageSetId = {0}".format(self.storage_set_id))
        self._assign_attributes(items[0])


class _ECSSystemEventResource(ServiceResource):

    def __init__(self, event_id, _client=None):
        ServiceResource.__init__(self, "ecs.system_event", _client=_client)
        self.event_id = event_id

        self.event_cycle_status = None
        self.event_finish_time = None
        self.event_publish_time = None
        self.event_type = None
        self.extended_attribute = None
        self.instance_id = None
        self.not_before = None

    def cancel_simulated(self, **params):
        _params = _transfer_params(params)
        self._client.cancel_simulated_system_events(event_id=self.event_id, **_params)

    def accept_inquired(self, **params):
        _params = _transfer_params(params)
        self._client.accept_inquired_system_event(event_id=self.event_id, **_params)

    def refresh(self):
        result = self._client.describe_instance_history_events(list_of_event_id=[self.event_id, ])
        items = _new_get_key_in_response(result, 'InstanceSystemEventSet.InstanceSystemEventType')
        if not items:
            raise ClientException(msg=
                                  "Failed to find system_event data from DescribeInstanceHistoryEvents response. "
                                  "EventId = {0}".format(self.event_id))
        self._assign_attributes(items[0])


class _ECSTaskResource(ServiceResource):

    def __init__(self, task_id, _client=None):
        ServiceResource.__init__(self, "ecs.task", _client=_client)
        self.task_id = task_id

        self.creation_time = None
        self.finished_time = None
        self.support_cancel = None
        self.task_action = None
        self.task_status = None

    def cancel(self, **params):
        _params = _transfer_params(params)
        self._client.cancel_task(task_id=self.task_id, **_params)

    def describe_task_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_task_attribute(task_id=self.task_id, **_params)

    def refresh(self):
        result = self._client.describe_tasks(task_ids=self.task_id)
        items = _new_get_key_in_response(result, 'TaskSet.Task')
        if not items:
            raise ClientException(msg=
                                  "Failed to find task data from DescribeTasks response. "
                                  "TaskId = {0}".format(self.task_id))
        self._assign_attributes(items[0])


class _ECSVRouterResource(ServiceResource):

    def __init__(self, vrouter_id, _client=None):
        ServiceResource.__init__(self, "ecs.vrouter", _client=_client)
        self.vrouter_id = vrouter_id

        self.creation_time = None
        self.description = None
        self.region_id = None
        self.route_table_ids = None
        self.vrouter_name = None
        self.vpc_id = None

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_vrouter_attribute(vrouter_id=self.vrouter_id, **_params)

    def refresh(self):
        result = self._client.describe_vrouters(vrouter_id=self.vrouter_id)
        items = _new_get_key_in_response(result, 'VRouters.VRouter')
        if not items:
            raise ClientException(msg=
                                  "Failed to find vrouter data from DescribeVRouters response. "
                                  "VRouterId = {0}".format(self.vrouter_id))
        self._assign_attributes(items[0])


class _ECSVSwitchResource(ServiceResource):

    def __init__(self, vswitch_id, _client=None):
        ServiceResource.__init__(self, "ecs.vswitch", _client=_client)
        self.vswitch_id = vswitch_id

        self.available_ip_address_count = None
        self.cidr_block = None
        self.creation_time = None
        self.description = None
        self.is_default = None
        self.resource_group_id = None
        self.status = None
        self.vswitch_name = None
        self.vpc_id = None
        self.zone_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_vswitch(vswitch_id=self.vswitch_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_vswitch_attribute(vswitch_id=self.vswitch_id, **_params)

    def refresh(self):
        result = self._client.describe_vswitches(vswitch_id=self.vswitch_id)
        items = _new_get_key_in_response(result, 'VSwitches.VSwitch')
        if not items:
            raise ClientException(msg=
                                  "Failed to find vswitch data from DescribeVSwitches response. "
                                  "VSwitchId = {0}".format(self.vswitch_id))
        self._assign_attributes(items[0])


class _ECSVirtualBorderRouterResource(ServiceResource):

    def __init__(self, vbr_id, _client=None):
        ServiceResource.__init__(self, "ecs.virtual_border_router", _client=_client)
        self.vbr_id = vbr_id

        self.access_point_id = None
        self.activation_time = None
        self.circuit_code = None
        self.creation_time = None
        self.description = None
        self.local_gateway_ip = None
        self.name = None
        self.peer_gateway_ip = None
        self.peering_subnet_mask = None
        self.physical_connection_business_status = None
        self.physical_connection_id = None
        self.physical_connection_owner_uid = None
        self.physical_connection_status = None
        self.recovery_time = None
        self.route_table_id = None
        self.status = None
        self.termination_time = None
        self.vlan_id = None
        self.vlan_interface_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_virtual_border_router(vbr_id=self.vbr_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_virtual_border_router_attribute(vbr_id=self.vbr_id, **_params)

    def recover(self, **params):
        _params = _transfer_params(params)
        self._client.recover_virtual_border_router(vbr_id=self.vbr_id, **_params)

    def terminate(self, **params):
        _params = _transfer_params(params)
        self._client.terminate_virtual_border_router(vbr_id=self.vbr_id, **_params)


class _ECSVpcResource(ServiceResource):

    def __init__(self, vpc_id, _client=None):
        ServiceResource.__init__(self, "ecs.vpc", _client=_client)
        self.vpc_id = vpc_id

        self.cidr_block = None
        self.creation_time = None
        self.description = None
        self.is_default = None
        self.region_id = None
        self.status = None
        self.user_cidrs = None
        self.vrouter_id = None
        self.vswitch_ids = None
        self.vpc_name = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_vpc(vpc_id=self.vpc_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_vpc_attribute(vpc_id=self.vpc_id, **_params)

    def refresh(self):
        result = self._client.describe_vpcs(vpc_id=self.vpc_id)
        items = _new_get_key_in_response(result, 'Vpcs.Vpc')
        if not items:
            raise ClientException(msg=
                                  "Failed to find vpc data from DescribeVpcs response. "
                                  "VpcId = {0}".format(self.vpc_id))
        self._assign_attributes(items[0])


class _ECSZoneResource(ServiceResource):

    def __init__(self, zone_id, _client=None):
        ServiceResource.__init__(self, "ecs.zone", _client=_client)
        self.zone_id = zone_id

        self.available_dedicated_host_types = None
        self.available_disk_categories = None
        self.available_instance_types = None
        self.available_resource_creation = None
        self.available_resources = None
        self.available_volume_categories = None
        self.dedicated_host_generations = None
        self.local_name = None
