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

from alibabacloud.exceptions import ClientException
from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, \
    _create_special_resource_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _VPCResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'vpc', _client=_client)
        self.access_points = _create_resource_collection(
            _VPCAccessPointResource, _client, _client.describe_access_points,
            'AccessPointSet.AccessPointType', 'AccessPointId',
        )
        self.bandwidth_packages = _create_resource_collection(
            _VPCBandwidthPackageResource, _client, _client.describe_bandwidth_packages,
            'BandwidthPackages.BandwidthPackage', 'BandwidthPackageId',
        )
        self.bgp_groups = _create_resource_collection(
            _VPCBgpGroupResource, _client, _client.describe_bgp_groups,
            'BgpGroups.BgpGroup', 'BgpGroupId',
        )
        self.bgp_peers = _create_resource_collection(
            _VPCBgpPeerResource, _client, _client.describe_bgp_peers,
            'BgpPeers.BgpPeer', 'BgpPeerId',
        )
        self.eip_addresses = _create_resource_collection(
            _VPCEipAddressResource, _client, _client.describe_eip_addresses,
            'EipAddresses.EipAddress', 'AllocationId',
        )
        self.flow_logs = _create_resource_collection(
            _VPCFlowLogResource, _client, _client.describe_flow_logs,
            'FlowLogs.FlowLog', 'FlowLogId',
        )
        self.global_acceleration_instances = _create_resource_collection(
            _VPCGlobalAccelerationInstanceResource, _client,
            _client.describe_global_acceleration_instances,
            'GlobalAccelerationInstances.GlobalAccelerationInstance',
            'GlobalAccelerationInstanceId',
        )
        self.ha_vips = _create_resource_collection(
            _VPCHaVipResource, _client, _client.describe_ha_vips,
            'HaVips.HaVip', 'HaVipId',
        )
        self.ipv6_translators = _create_resource_collection(
            _VPCIPv6TranslatorResource, _client, _client.describe_ipv6_translators,
            'Ipv6Translators.Ipv6Translator', 'Ipv6TranslatorId',
        )
        self.ipv6_translator_acl_lists = _create_resource_collection(
            _VPCIPv6TranslatorAclListResource, _client, _client.describe_ipv6_translator_acl_lists,
            'Ipv6TranslatorAcls.IPv6TranslatorAcl', 'AclId',
        )
        self.ipv6_translator_entries = _create_resource_collection(
            _VPCIPv6TranslatorEntryResource, _client, _client.describe_ipv6_translator_entries,
            'Ipv6TranslatorEntries.Ipv6TranslatorEntry', 'Ipv6TranslatorEntryId',
        )
        self.ipv6_addresses = _create_resource_collection(
            _VPCIpv6AddressResource, _client, _client.describe_ipv6_addresses,
            'Ipv6Addresses.Ipv6Address', 'Ipv6AddressId',
        )
        self.ipv6_egress_only_rules = _create_resource_collection(
            _VPCIpv6EgressOnlyRuleResource, _client, _client.describe_ipv6_egress_only_rules,
            'Ipv6EgressOnlyRules.Ipv6EgressOnlyRule', 'Ipv6EgressOnlyRuleId',
        )
        self.network_acls = _create_resource_collection(
            _VPCNetworkAclResource, _client, _client.describe_network_acls,
            'NetworkAcls.NetworkAcl', 'NetworkAclId',
        )
        self.physical_connections = _create_resource_collection(
            _VPCPhysicalConnectionResource, _client, _client.describe_physical_connections,
            'PhysicalConnectionSet.PhysicalConnectionType', 'PhysicalConnectionId',
        )
        self.regions = _create_special_resource_collection(
            _VPCRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId',
        )
        self.route_tables = _create_resource_collection(
            _VPCRouteTableResource, _client, _client.describe_route_tables,
            'RouteTables.RouteTable', 'RouteTableId',
        )
        self.router_interfaces = _create_resource_collection(
            _VPCRouterInterfaceResource, _client, _client.describe_router_interfaces,
            'RouterInterfaceSet.RouterInterfaceType', 'RouterInterfaceId',
        )
        self.ssl_vpn_client_certs = _create_resource_collection(
            _VPCSslVpnClientCertResource, _client, _client.describe_ssl_vpn_client_certs,
            'SslVpnClientCertKeys.SslVpnClientCertKey', 'SslVpnClientCertId',
        )
        self.ssl_vpn_servers = _create_resource_collection(
            _VPCSslVpnServerResource, _client, _client.describe_ssl_vpn_servers,
            'SslVpnServers.SslVpnServer', 'SslVpnServerId',
        )
        self.vrouters = _create_resource_collection(
            _VPCVRouterResource, _client, _client.describe_vrouters,
            'VRouters.VRouter', 'VRouterId',
        )
        self.vswitches = _create_resource_collection(
            _VPCVSwitchResource, _client, _client.describe_vswitches,
            'VSwitches.VSwitch', 'VSwitchId',
        )
        self.virtual_border_routers = _create_resource_collection(
            _VPCVirtualBorderRouterResource, _client, _client.describe_virtual_border_routers,
            'VirtualBorderRouterSet.VirtualBorderRouterType', 'VbrId',
        )
        self.vpcs = _create_resource_collection(
            _VPCVpcResource, _client, _client.describe_vpcs,
            'Vpcs.Vpc', 'VpcId',
        )
        self.vpn_connections = _create_resource_collection(
            _VPCVpnConnectionResource, _client, _client.describe_vpn_connections,
            'VpnConnections.VpnConnection', 'VpnConnectionId',
        )
        self.vpn_pbr_route_entries = _create_resource_collection(
            _VPCVpnPbrRouteEntryResource, _client, _client.describe_vpn_pbr_route_entries,
            'VpnPbrRouteEntries.VpnPbrRouteEntry', 'VpnInstanceId',
        )
        self.zones = _create_special_resource_collection(
            _VPCZoneResource, _client, _client.describe_zones,
            'Zones.Zone', 'ZoneId',
        )

    def create_bandwidth_package(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_bandwidth_package(**_params)
        bandwidth_package_id = _new_get_key_in_response(response, 'BandwidthPackageId')
        return _VPCBandwidthPackageResource(bandwidth_package_id, _client=self._client)

    def create_bgp_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_bgp_group(**_params)
        bgp_group_id = _new_get_key_in_response(response, 'BgpGroupId')
        return _VPCBgpGroupResource(bgp_group_id, _client=self._client)

    def create_bgp_peer(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_bgp_peer(**_params)
        bgp_peer_id = _new_get_key_in_response(response, 'BgpPeerId')
        return _VPCBgpPeerResource(bgp_peer_id, _client=self._client)

    def create_customer_gateway(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_customer_gateway(**_params)
        customer_gateway_id = _new_get_key_in_response(response, 'CustomerGatewayId')
        return _VPCCustomerGatewayResource(customer_gateway_id, _client=self._client)

    def allocate_eip_address(self, **params):
        _params = _transfer_params(params)
        response = self._client.allocate_eip_address(**_params)
        allocation_id = _new_get_key_in_response(response, 'AllocationId')
        return _VPCEipAddressResource(allocation_id, _client=self._client)

    def create_express_cloud_connection(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_express_cloud_connection(**_params)
        ecc_id = _new_get_key_in_response(response, 'EccId')
        return _VPCExpressCloudConnectionResource(ecc_id, _client=self._client)

    def create_flow_log(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_flow_log(**_params)
        flow_log_id = _new_get_key_in_response(response, 'FlowLogId')
        return _VPCFlowLogResource(flow_log_id, _client=self._client)

    def create_global_acceleration_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_global_acceleration_instance(**_params)
        global_acceleration_instance_id = _new_get_key_in_response(response,
                                                                   'GlobalAccelerationInstanceId')
        return _VPCGlobalAccelerationInstanceResource(global_acceleration_instance_id,
                                                      _client=self._client)

    def create_ha_vip(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ha_vip(**_params)
        ha_vip_id = _new_get_key_in_response(response, 'HaVipId')
        return _VPCHaVipResource(ha_vip_id, _client=self._client)

    def create_ipv6_translator(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ipv6_translator(**_params)
        ipv6_translator_id = _new_get_key_in_response(response, 'Ipv6TranslatorId')
        return _VPCIPv6TranslatorResource(ipv6_translator_id, _client=self._client)

    def create_ipv6_translator_acl_list(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ipv6_translator_acl_list(**_params)
        acl_id = _new_get_key_in_response(response, 'AclId')
        return _VPCIPv6TranslatorAclListResource(acl_id, _client=self._client)

    def create_ipv6_translator_entry(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ipv6_translator_entry(**_params)
        ipv6_translator_entry_id = _new_get_key_in_response(response, 'Ipv6TranslatorEntryId')
        return _VPCIPv6TranslatorEntryResource(ipv6_translator_entry_id, _client=self._client)

    def create_ipv6_gateway(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ipv6_gateway(**_params)
        ipv6_gateway_id = _new_get_key_in_response(response, 'Ipv6GatewayId')
        return _VPCIpv6GatewayResource(ipv6_gateway_id, _client=self._client)

    def create_nat_gateway(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_nat_gateway(**_params)
        nat_gateway_id = _new_get_key_in_response(response, 'NatGatewayId')
        return _VPCNatGatewayResource(nat_gateway_id, _client=self._client)

    def create_network_acl(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_network_acl(**_params)
        network_acl_id = _new_get_key_in_response(response, 'NetworkAclId')
        return _VPCNetworkAclResource(network_acl_id, _client=self._client)

    def create_physical_connection(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_physical_connection(**_params)
        physical_connection_id = _new_get_key_in_response(response, 'PhysicalConnectionId')
        return _VPCPhysicalConnectionResource(physical_connection_id, _client=self._client)

    def create_route_table(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_route_table(**_params)
        route_table_id = _new_get_key_in_response(response, 'RouteTableId')
        return _VPCRouteTableResource(route_table_id, _client=self._client)

    def create_router_interface(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_router_interface(**_params)
        router_interface_id = _new_get_key_in_response(response, 'RouterInterfaceId')
        return _VPCRouterInterfaceResource(router_interface_id, _client=self._client)

    def create_ssl_vpn_client_cert(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ssl_vpn_client_cert(**_params)
        ssl_vpn_client_cert_id = _new_get_key_in_response(response, 'SslVpnClientCertId')
        return _VPCSslVpnClientCertResource(ssl_vpn_client_cert_id, _client=self._client)

    def create_ssl_vpn_server(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ssl_vpn_server(**_params)
        ssl_vpn_server_id = _new_get_key_in_response(response, 'SslVpnServerId')
        return _VPCSslVpnServerResource(ssl_vpn_server_id, _client=self._client)

    def create_vswitch(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_vswitch(**_params)
        vswitch_id = _new_get_key_in_response(response, 'VSwitchId')
        return _VPCVSwitchResource(vswitch_id, _client=self._client)

    def create_virtual_border_router(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_virtual_border_router(**_params)
        vbr_id = _new_get_key_in_response(response, 'VbrId')
        return _VPCVirtualBorderRouterResource(vbr_id, _client=self._client)

    def create_vpc(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_vpc(**_params)
        vpc_id = _new_get_key_in_response(response, 'VpcId')
        return _VPCVpcResource(vpc_id, _client=self._client)

    def create_vpn_connection(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_vpn_connection(**_params)
        vpn_connection_id = _new_get_key_in_response(response, 'VpnConnectionId')
        return _VPCVpnConnectionResource(vpn_connection_id, _client=self._client)

    def create_vpn_gateway(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_vpn_gateway(**_params)
        vpn_gateway_id = _new_get_key_in_response(response, 'VpnGatewayId')
        return _VPCVpnGatewayResource(vpn_gateway_id, _client=self._client)

    def create_vpn_pbr_route_entry(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_vpn_pbr_route_entry(**_params)
        vpn_instance_id = _new_get_key_in_response(response, 'VpnInstanceId')
        return _VPCVpnPbrRouteEntryResource(vpn_instance_id, _client=self._client)


class _VPCAccessPointResource(ServiceResource):

    def __init__(self, access_point_id, _client=None):
        ServiceResource.__init__(self, "vpc.access_point", _client=_client)
        self.access_point_id = access_point_id

        self.attached_region_no = None
        self.description = None
        self.host_operator = None
        self.location = None
        self.name = None
        self.status = None
        self.type_ = None

    def create_physical_connection_setup_order(self, **params):
        _params = _transfer_params(params)
        self._client.create_physical_connection_setup_order(access_point_id=self.access_point_id,
                                                            **_params)


class _VPCBandwidthPackageResource(ServiceResource):

    def __init__(self, bandwidth_package_id, _client=None):
        ServiceResource.__init__(self, "vpc.bandwidth_package", _client=_client)
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

    def add_common_bandwidth_package_ip(self, **params):
        _params = _transfer_params(params)
        self._client.add_common_bandwidth_package_ip(bandwidth_package_id=self.bandwidth_package_id,
                                                     **_params)

    def cancel_common_bandwidth_package_ip_bandwidth(self, **params):
        _params = _transfer_params(params)
        self._client.cancel_common_bandwidth_package_ip_bandwidth(
            bandwidth_package_id=self.bandwidth_package_id, **_params)

    def convert(self, **params):
        _params = _transfer_params(params)
        self._client.convert_bandwidth_package(bandwidth_package_id=self.bandwidth_package_id,
                                               **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_bandwidth_package(bandwidth_package_id=self.bandwidth_package_id,
                                              **_params)

    def delete_common(self, **params):
        _params = _transfer_params(params)
        self._client.delete_common_bandwidth_package(bandwidth_package_id=self.bandwidth_package_id,
                                                     **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_bandwidth_package_attribute(
            bandwidth_package_id=self.bandwidth_package_id, **_params)

    def modify_common_bandwidth_package_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_common_bandwidth_package_attribute(
            bandwidth_package_id=self.bandwidth_package_id, **_params)

    def modify_common_bandwidth_package_ip_bandwidth(self, **params):
        _params = _transfer_params(params)
        self._client.modify_common_bandwidth_package_ip_bandwidth(
            bandwidth_package_id=self.bandwidth_package_id, **_params)

    def modify_common_bandwidth_package_pay_type(self, **params):
        _params = _transfer_params(params)
        self._client.modify_common_bandwidth_package_pay_type(
            bandwidth_package_id=self.bandwidth_package_id, **_params)

    def modify_common_bandwidth_package_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_common_bandwidth_package_spec(
            bandwidth_package_id=self.bandwidth_package_id, **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_bandwidth_package_spec(bandwidth_package_id=self.bandwidth_package_id,
                                                   **_params)

    def remove_bandwidth_package_ips(self, **params):
        _params = _transfer_params(params)
        self._client.remove_bandwidth_package_ips(bandwidth_package_id=self.bandwidth_package_id,
                                                  **_params)

    def remove_common_bandwidth_package_ip(self, **params):
        _params = _transfer_params(params)
        self._client.remove_common_bandwidth_package_ip(
            bandwidth_package_id=self.bandwidth_package_id, **_params)

    def refresh(self):
        result = self._client.describe_bandwidth_packages(
            bandwidth_package_id=self.bandwidth_package_id)
        items = _new_get_key_in_response(result, 'BandwidthPackages.BandwidthPackage')
        if not items:
            raise ClientException(msg=
                                  "Failed to find bandwidth_package data from DescribeBandwidthPackages response. "
                                  "BandwidthPackageId = {0}".format(self.bandwidth_package_id))
        self._assign_attributes(items[0])


class _VPCBgpGroupResource(ServiceResource):

    def __init__(self, bgp_group_id, _client=None):
        ServiceResource.__init__(self, "vpc.bgp_group", _client=_client)
        self.bgp_group_id = bgp_group_id

        self.auth_key = None
        self.description = None
        self.hold = None
        self.is_fake = None
        self.keepalive = None
        self.local_asn = None
        self.name = None
        self.peer_asn = None
        self.region_id = None
        self.route_limit = None
        self.router_id = None
        self.status = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_bgp_group(bgp_group_id=self.bgp_group_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_bgp_group_attribute(bgp_group_id=self.bgp_group_id, **_params)

    def refresh(self):
        result = self._client.describe_bgp_groups(bgp_group_id=self.bgp_group_id)
        items = _new_get_key_in_response(result, 'BgpGroups.BgpGroup')
        if not items:
            raise ClientException(msg=
                                  "Failed to find bgp_group data from DescribeBgpGroups response. "
                                  "BgpGroupId = {0}".format(self.bgp_group_id))
        self._assign_attributes(items[0])


class _VPCBgpPeerResource(ServiceResource):

    def __init__(self, bgp_peer_id, _client=None):
        ServiceResource.__init__(self, "vpc.bgp_peer", _client=_client)
        self.bgp_peer_id = bgp_peer_id

        self.auth_key = None
        self.bgp_group_id = None
        self.bgp_status = None
        self.description = None
        self.enable_bfd = None
        self.hold = None
        self.is_fake = None
        self.keepalive = None
        self.local_asn = None
        self.name = None
        self.peer_asn = None
        self.peer_ip_address = None
        self.region_id = None
        self.route_limit = None
        self.router_id = None
        self.status = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_bgp_peer(bgp_peer_id=self.bgp_peer_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_bgp_peer_attribute(bgp_peer_id=self.bgp_peer_id, **_params)

    def refresh(self):
        result = self._client.describe_bgp_peers(bgp_peer_id=self.bgp_peer_id)
        items = _new_get_key_in_response(result, 'BgpPeers.BgpPeer')
        if not items:
            raise ClientException(msg=
                                  "Failed to find bgp_peer data from DescribeBgpPeers response. "
                                  "BgpPeerId = {0}".format(self.bgp_peer_id))
        self._assign_attributes(items[0])


class _VPCCustomerGatewayResource(ServiceResource):

    def __init__(self, customer_gateway_id, _client=None):
        ServiceResource.__init__(self, "vpc.customer_gateway", _client=_client)
        self.customer_gateway_id = customer_gateway_id

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_customer_gateway(customer_gateway_id=self.customer_gateway_id,
                                             **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        self._client.describe_customer_gateway(customer_gateway_id=self.customer_gateway_id,
                                               **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_customer_gateway_attribute(customer_gateway_id=self.customer_gateway_id,
                                                       **_params)


class _VPCEipAddressResource(ServiceResource):

    def __init__(self, allocation_id, _client=None):
        ServiceResource.__init__(self, "vpc.eip_address", _client=_client)
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


class _VPCExpressCloudConnectionResource(ServiceResource):

    def __init__(self, ecc_id, _client=None):
        ServiceResource.__init__(self, "vpc.express_cloud_connection", _client=_client)
        self.ecc_id = ecc_id

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_express_cloud_connection_attribute(ecc_id=self.ecc_id, **_params)

    def modify_bandwidth(self, **params):
        _params = _transfer_params(params)
        self._client.modify_express_cloud_connection_bandwidth(ecc_id=self.ecc_id, **_params)


class _VPCFlowLogResource(ServiceResource):

    def __init__(self, flow_log_id, _client=None):
        ServiceResource.__init__(self, "vpc.flow_log", _client=_client)
        self.flow_log_id = flow_log_id

        self.creation_time = None
        self.description = None
        self.flow_log_name = None
        self.log_store_name = None
        self.project_name = None
        self.region_id = None
        self.resource_id = None
        self.resource_type = None
        self.status = None
        self.traffic_type = None

    def active(self, **params):
        _params = _transfer_params(params)
        self._client.active_flow_log(flow_log_id=self.flow_log_id, **_params)

    def deactive(self, **params):
        _params = _transfer_params(params)
        self._client.deactive_flow_log(flow_log_id=self.flow_log_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_flow_log(flow_log_id=self.flow_log_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_flow_log_attribute(flow_log_id=self.flow_log_id, **_params)

    def refresh(self):
        result = self._client.describe_flow_logs(flow_log_id=self.flow_log_id)
        items = _new_get_key_in_response(result, 'FlowLogs.FlowLog')
        if not items:
            raise ClientException(msg=
                                  "Failed to find flow_log data from DescribeFlowLogs response. "
                                  "FlowLogId = {0}".format(self.flow_log_id))
        self._assign_attributes(items[0])


class _VPCGlobalAccelerationInstanceResource(ServiceResource):

    def __init__(self, global_acceleration_instance_id, _client=None):
        ServiceResource.__init__(self, "vpc.global_acceleration_instance", _client=_client)
        self.global_acceleration_instance_id = global_acceleration_instance_id

        self.acceleration_location = None
        self.backend_servers = None
        self.bandwidth = None
        self.bandwidth_type = None
        self.charge_type = None
        self.creation_time = None
        self.description = None
        self.expired_time = None
        self.has_reservation_data = None
        self.internet_charge_type = None
        self.ip_address = None
        self.name = None
        self.operation_locks = None
        self.public_ip_addresses = None
        self.region_id = None
        self.reservation_active_time = None
        self.reservation_bandwidth = None
        self.reservation_internet_charge_type = None
        self.reservation_order_type = None
        self.service_location = None
        self.status = None

    def add_global_acceleration_instance_ip(self, **params):
        _params = _transfer_params(params)
        self._client.add_global_acceleration_instance_ip(
            global_acceleration_instance_id=self.global_acceleration_instance_id, **_params)

    def associate(self, **params):
        _params = _transfer_params(params)
        self._client.associate_global_acceleration_instance(
            global_acceleration_instance_id=self.global_acceleration_instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_global_acceleration_instance(
            global_acceleration_instance_id=self.global_acceleration_instance_id, **_params)

    def modify_attributes(self, **params):
        _params = _transfer_params(params)
        self._client.modify_global_acceleration_instance_attributes(
            global_acceleration_instance_id=self.global_acceleration_instance_id, **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_global_acceleration_instance_spec(
            global_acceleration_instance_id=self.global_acceleration_instance_id, **_params)

    def remove_global_acceleration_instance_ip(self, **params):
        _params = _transfer_params(params)
        self._client.remove_global_acceleration_instance_ip(
            global_acceleration_instance_id=self.global_acceleration_instance_id, **_params)

    def unassociate(self, **params):
        _params = _transfer_params(params)
        self._client.unassociate_global_acceleration_instance(
            global_acceleration_instance_id=self.global_acceleration_instance_id, **_params)

    def refresh(self):
        result = self._client.describe_global_acceleration_instances(
            global_acceleration_instance_id=self.global_acceleration_instance_id)
        items = _new_get_key_in_response(result,
                                         'GlobalAccelerationInstances.GlobalAccelerationInstance')
        if not items:
            raise ClientException(msg=
                                  "Failed to find global_acceleration_instance data from DescribeGlobalAccelerationInstances response. "
                                  "GlobalAccelerationInstanceId = {0}".format(
                                      self.global_acceleration_instance_id))
        self._assign_attributes(items[0])


class _VPCHaVipResource(ServiceResource):

    def __init__(self, ha_vip_id, _client=None):
        ServiceResource.__init__(self, "vpc.ha_vip", _client=_client)
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


class _VPCIPv6TranslatorResource(ServiceResource):

    def __init__(self, ipv6_translator_id, _client=None):
        ServiceResource.__init__(self, "vpc.ipv6_translator", _client=_client)
        self.ipv6_translator_id = ipv6_translator_id

        self.allocate_ipv4_addr = None
        self.allocate_ipv6_addr = None
        self.available_bandwidth = None
        self.bandwidth = None
        self.business_status = None
        self.create_time = None
        self.description = None
        self.end_time = None
        self.ipv6_translator_entry_ids = None
        self.name = None
        self.pay_type = None
        self.region_id = None
        self.spec = None
        self.status = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_ipv6_translator(ipv6_translator_id=self.ipv6_translator_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_ipv6_translator_attribute(ipv6_translator_id=self.ipv6_translator_id,
                                                      **_params)

    def modify_bandwidth(self, **params):
        _params = _transfer_params(params)
        self._client.modify_ipv6_translator_bandwidth(ipv6_translator_id=self.ipv6_translator_id,
                                                      **_params)

    def refresh(self):
        result = self._client.describe_ipv6_translators(ipv6_translator_id=self.ipv6_translator_id)
        items = _new_get_key_in_response(result, 'Ipv6Translators.Ipv6Translator')
        if not items:
            raise ClientException(msg=
                                  "Failed to find ipv6_translator data from DescribeIPv6Translators response. "
                                  "Ipv6TranslatorId = {0}".format(self.ipv6_translator_id))
        self._assign_attributes(items[0])


class _VPCIPv6TranslatorAclListResource(ServiceResource):

    def __init__(self, acl_id, _client=None):
        ServiceResource.__init__(self, "vpc.ipv6_translator_acl_list", _client=_client)
        self.acl_id = acl_id

        self.acl_name = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_ipv6_translator_acl_list(acl_id=self.acl_id, **_params)

    def describe_ipv6_translator_acl_list_attributes(self, **params):
        _params = _transfer_params(params)
        self._client.describe_ipv6_translator_acl_list_attributes(acl_id=self.acl_id, **_params)

    def modify_ipv6_translator_acl_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_ipv6_translator_acl_attribute(acl_id=self.acl_id, **_params)

    def add_ipv6_translator_acl_list_entry(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_ipv6_translator_acl_list_entry(acl_id=self.acl_id, **_params)
        acl_entry_id = _new_get_key_in_response(response, 'AclEntryId')
        return _VPCIPv6TranslatorAclListEntryResource(acl_entry_id, self.acl_id,
                                                      _client=self._client)

    def refresh(self):
        result = self._client.describe_ipv6_translator_acl_lists(acl_id=self.acl_id)
        items = _new_get_key_in_response(result, 'Ipv6TranslatorAcls.IPv6TranslatorAcl')
        if not items:
            raise ClientException(msg=
                                  "Failed to find ipv6_translator_acl_list data from DescribeIPv6TranslatorAclLists response. "
                                  "AclId = {0}".format(self.acl_id))
        self._assign_attributes(items[0])


class _VPCIPv6TranslatorAclListEntryResource(ServiceResource):

    def __init__(self, acl_entry_id, acl_id, _client=None):
        ServiceResource.__init__(self, "vpc.ipv6_translator_acl_list_entry", _client=_client)
        self.acl_entry_id = acl_entry_id
        self.acl_id = acl_id

    def modify(self, **params):
        _params = _transfer_params(params)
        self._client.modify_ipv6_translator_acl_list_entry(acl_entry_id=self.acl_entry_id,
                                                           acl_id=self.acl_id, **_params)

    def remove(self, **params):
        _params = _transfer_params(params)
        self._client.remove_ipv6_translator_acl_list_entry(acl_entry_id=self.acl_entry_id,
                                                           acl_id=self.acl_id, **_params)


class _VPCIPv6TranslatorEntryResource(ServiceResource):

    def __init__(self, ipv6_translator_entry_id, _client=None):
        ServiceResource.__init__(self, "vpc.ipv6_translator_entry", _client=_client)
        self.ipv6_translator_entry_id = ipv6_translator_entry_id

        self.acl_id = None
        self.acl_status = None
        self.acl_type = None
        self.allocate_ipv6_addr = None
        self.allocate_ipv6_port = None
        self.backend_ipv4_addr = None
        self.backend_ipv4_port = None
        self.entry_bandwidth = None
        self.entry_description = None
        self.entry_name = None
        self.entry_status = None
        self.ipv6_translator_id = None
        self.region_id = None
        self.trans_protocol = None

    def modify(self, **params):
        _params = _transfer_params(params)
        self._client.modify_ipv6_translator_entry(
            ipv6_translator_entry_id=self.ipv6_translator_entry_id, **_params)

    def refresh(self):
        result = self._client.describe_ipv6_translator_entries(
            ipv6_translator_entry_id=self.ipv6_translator_entry_id)
        items = _new_get_key_in_response(result, 'Ipv6TranslatorEntries.Ipv6TranslatorEntry')
        if not items:
            raise ClientException(msg=
                                  "Failed to find ipv6_translator_entry data from DescribeIPv6TranslatorEntries response. "
                                  "Ipv6TranslatorEntryId = {0}".format(
                                      self.ipv6_translator_entry_id))
        self._assign_attributes(items[0])


class _VPCIpv6AddressResource(ServiceResource):

    def __init__(self, ipv6_address_id, _client=None):
        ServiceResource.__init__(self, "vpc.ipv6_address", _client=_client)
        self.ipv6_address_id = ipv6_address_id

        self.allocation_time = None
        self.associated_instance_id = None
        self.associated_instance_type = None
        self.ipv6_address = None
        self.ipv6_address_name = None
        self.ipv6_gateway_id = None
        self.ipv6_internet_bandwidth = None
        self.network_type = None
        self.real_bandwidth = None
        self.status = None
        self.vswitch_id = None
        self.vpc_id = None

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_ipv6_address_attribute(ipv6_address_id=self.ipv6_address_id, **_params)

    def refresh(self):
        result = self._client.describe_ipv6_addresses(ipv6_address_id=self.ipv6_address_id)
        items = _new_get_key_in_response(result, 'Ipv6Addresses.Ipv6Address')
        if not items:
            raise ClientException(msg=
                                  "Failed to find ipv6_address data from DescribeIpv6Addresses response. "
                                  "Ipv6AddressId = {0}".format(self.ipv6_address_id))
        self._assign_attributes(items[0])


class _VPCIpv6EgressOnlyRuleResource(ServiceResource):

    def __init__(self, ipv6_egress_only_rule_id, _client=None):
        ServiceResource.__init__(self, "vpc.ipv6_egress_only_rule", _client=_client)
        self.ipv6_egress_only_rule_id = ipv6_egress_only_rule_id

        self.description = None
        self.instance_id = None
        self.instance_type = None
        self.name = None
        self.status = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_ipv6_egress_only_rule(
            ipv6_egress_only_rule_id=self.ipv6_egress_only_rule_id, **_params)

    def refresh(self):
        result = self._client.describe_ipv6_egress_only_rules(
            ipv6_egress_only_rule_id=self.ipv6_egress_only_rule_id)
        items = _new_get_key_in_response(result, 'Ipv6EgressOnlyRules.Ipv6EgressOnlyRule')
        if not items:
            raise ClientException(msg=
                                  "Failed to find ipv6_egress_only_rule data from DescribeIpv6EgressOnlyRules response. "
                                  "Ipv6EgressOnlyRuleId = {0}".format(
                                      self.ipv6_egress_only_rule_id))
        self._assign_attributes(items[0])


class _VPCIpv6GatewayResource(ServiceResource):

    def __init__(self, ipv6_gateway_id, _client=None):
        ServiceResource.__init__(self, "vpc.ipv6_gateway", _client=_client)
        self.ipv6_gateway_id = ipv6_gateway_id

    def allocate_ipv6_internet_bandwidth(self, **params):
        _params = _transfer_params(params)
        self._client.allocate_ipv6_internet_bandwidth(ipv6_gateway_id=self.ipv6_gateway_id,
                                                      **_params)

    def create_ipv6_egress_only_rule(self, **params):
        _params = _transfer_params(params)
        self._client.create_ipv6_egress_only_rule(ipv6_gateway_id=self.ipv6_gateway_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_ipv6_gateway(ipv6_gateway_id=self.ipv6_gateway_id, **_params)

    def describe_ipv6_gateway_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_ipv6_gateway_attribute(ipv6_gateway_id=self.ipv6_gateway_id,
                                                     **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_ipv6_gateway_attribute(ipv6_gateway_id=self.ipv6_gateway_id, **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_ipv6_gateway_spec(ipv6_gateway_id=self.ipv6_gateway_id, **_params)


class _VPCNatGatewayResource(ServiceResource):

    def __init__(self, nat_gateway_id, _client=None):
        ServiceResource.__init__(self, "vpc.nat_gateway", _client=_client)
        self.nat_gateway_id = nat_gateway_id

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_nat_gateway(nat_gateway_id=self.nat_gateway_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_nat_gateway_attribute(nat_gateway_id=self.nat_gateway_id, **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_nat_gateway_spec(nat_gateway_id=self.nat_gateway_id, **_params)


class _VPCNetworkAclResource(ServiceResource):

    def __init__(self, network_acl_id, _client=None):
        ServiceResource.__init__(self, "vpc.network_acl", _client=_client)
        self.network_acl_id = network_acl_id

        self.creation_time = None
        self.description = None
        self.egress_acl_entries = None
        self.ingress_acl_entries = None
        self.network_acl_name = None
        self.region_id = None
        self.resources = None
        self.status = None
        self.vpc_id = None

    def associate(self, **params):
        _params = _transfer_params(params)
        self._client.associate_network_acl(network_acl_id=self.network_acl_id, **_params)

    def copy_network_acl_entries(self, **params):
        _params = _transfer_params(params)
        self._client.copy_network_acl_entries(network_acl_id=self.network_acl_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_network_acl(network_acl_id=self.network_acl_id, **_params)

    def describe_network_acl_attributes(self, **params):
        _params = _transfer_params(params)
        self._client.describe_network_acl_attributes(network_acl_id=self.network_acl_id, **_params)

    def modify_attributes(self, **params):
        _params = _transfer_params(params)
        self._client.modify_network_acl_attributes(network_acl_id=self.network_acl_id, **_params)

    def unassociate(self, **params):
        _params = _transfer_params(params)
        self._client.unassociate_network_acl(network_acl_id=self.network_acl_id, **_params)

    def update_network_acl_entries(self, **params):
        _params = _transfer_params(params)
        self._client.update_network_acl_entries(network_acl_id=self.network_acl_id, **_params)

    def refresh(self):
        result = self._client.describe_network_acls(network_acl_id=self.network_acl_id)
        items = _new_get_key_in_response(result, 'NetworkAcls.NetworkAcl')
        if not items:
            raise ClientException(msg=
                                  "Failed to find network_acl data from DescribeNetworkAcls response. "
                                  "NetworkAclId = {0}".format(self.network_acl_id))
        self._assign_attributes(items[0])


class _VPCPhysicalConnectionResource(ServiceResource):

    def __init__(self, physical_connection_id, _client=None):
        ServiceResource.__init__(self, "vpc.physical_connection", _client=_client)
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

    def create_physical_connection_occupancy_order(self, **params):
        _params = _transfer_params(params)
        self._client.create_physical_connection_occupancy_order(
            physical_connection_id=self.physical_connection_id, **_params)

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


class _VPCRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "vpc.region", _client=_client)
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


class _VPCRouteTableResource(ServiceResource):

    def __init__(self, route_table_id, _client=None):
        ServiceResource.__init__(self, "vpc.route_table", _client=_client)
        self.route_table_id = route_table_id

        self.creation_time = None
        self.resource_group_id = None
        self.route_entrys = None
        self.route_table_type = None
        self.vrouter_id = None

    def create_route_entry(self, **params):
        _params = _transfer_params(params)
        self._client.create_route_entry(route_table_id=self.route_table_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_route_table(route_table_id=self.route_table_id, **_params)

    def modify_attributes(self, **params):
        _params = _transfer_params(params)
        self._client.modify_route_table_attributes(route_table_id=self.route_table_id, **_params)

    def associate(self, **params):
        _params = _transfer_params(params)
        self._client.associate_route_table(route_table_id=self.route_table_id, **_params)

    def unassociate(self, **params):
        _params = _transfer_params(params)
        self._client.unassociate_route_table(route_table_id=self.route_table_id, **_params)

    def refresh(self):
        result = self._client.describe_route_tables(route_table_id=self.route_table_id)
        items = _new_get_key_in_response(result, 'RouteTables.RouteTable')
        if not items:
            raise ClientException(msg=
                                  "Failed to find route_table data from DescribeRouteTables response. "
                                  "RouteTableId = {0}".format(self.route_table_id))
        self._assign_attributes(items[0])


class _VPCRouterInterfaceResource(ServiceResource):

    def __init__(self, router_interface_id, _client=None):
        ServiceResource.__init__(self, "vpc.router_interface", _client=_client)
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

    def delete_express_connect(self, **params):
        _params = _transfer_params(params)
        self._client.delete_express_connect(router_interface_id=self.router_interface_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_router_interface_attribute(router_interface_id=self.router_interface_id,
                                                       **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_router_interface_spec(router_interface_id=self.router_interface_id,
                                                  **_params)


class _VPCSslVpnClientCertResource(ServiceResource):

    def __init__(self, ssl_vpn_client_cert_id, _client=None):
        ServiceResource.__init__(self, "vpc.ssl_vpn_client_cert", _client=_client)
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id

        self.create_time = None
        self.end_time = None
        self.name = None
        self.region_id = None
        self.ssl_vpn_server_id = None
        self.status = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_ssl_vpn_client_cert(ssl_vpn_client_cert_id=self.ssl_vpn_client_cert_id,
                                                **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        self._client.describe_ssl_vpn_client_cert(
            ssl_vpn_client_cert_id=self.ssl_vpn_client_cert_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        self._client.modify_ssl_vpn_client_cert(ssl_vpn_client_cert_id=self.ssl_vpn_client_cert_id,
                                                **_params)

    def refresh(self):
        result = self._client.describe_ssl_vpn_client_certs(
            ssl_vpn_client_cert_id=self.ssl_vpn_client_cert_id)
        items = _new_get_key_in_response(result, 'SslVpnClientCertKeys.SslVpnClientCertKey')
        if not items:
            raise ClientException(msg=
                                  "Failed to find ssl_vpn_client_cert data from DescribeSslVpnClientCerts response. "
                                  "SslVpnClientCertId = {0}".format(self.ssl_vpn_client_cert_id))
        self._assign_attributes(items[0])


class _VPCSslVpnServerResource(ServiceResource):

    def __init__(self, ssl_vpn_server_id, _client=None):
        ServiceResource.__init__(self, "vpc.ssl_vpn_server", _client=_client)
        self.ssl_vpn_server_id = ssl_vpn_server_id

        self.cipher = None
        self.client_ip_pool = None
        self.compress = None
        self.connections = None
        self.create_time = None
        self.internet_ip = None
        self.local_subnet = None
        self.max_connections = None
        self.name = None
        self.port = None
        self.proto = None
        self.region_id = None
        self.vpn_gateway_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_ssl_vpn_server(ssl_vpn_server_id=self.ssl_vpn_server_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        self._client.modify_ssl_vpn_server(ssl_vpn_server_id=self.ssl_vpn_server_id, **_params)

    def refresh(self):
        result = self._client.describe_ssl_vpn_servers(ssl_vpn_server_id=self.ssl_vpn_server_id)
        items = _new_get_key_in_response(result, 'SslVpnServers.SslVpnServer')
        if not items:
            raise ClientException(msg=
                                  "Failed to find ssl_vpn_server data from DescribeSslVpnServers response. "
                                  "SslVpnServerId = {0}".format(self.ssl_vpn_server_id))
        self._assign_attributes(items[0])


class _VPCVRouterResource(ServiceResource):

    def __init__(self, vrouter_id, _client=None):
        ServiceResource.__init__(self, "vpc.vrouter", _client=_client)
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


class _VPCVSwitchResource(ServiceResource):

    def __init__(self, vswitch_id, _client=None):
        ServiceResource.__init__(self, "vpc.vswitch", _client=_client)
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

    def describe_vswitch_attributes(self, **params):
        _params = _transfer_params(params)
        self._client.describe_vswitch_attributes(vswitch_id=self.vswitch_id, **_params)

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


class _VPCVirtualBorderRouterResource(ServiceResource):

    def __init__(self, vbr_id, _client=None):
        ServiceResource.__init__(self, "vpc.virtual_border_router", _client=_client)
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

    def associate_physical_connection_to(self, **params):
        _params = _transfer_params(params)
        self._client.associate_physical_connection_to_virtual_border_router(vbr_id=self.vbr_id,
                                                                            **_params)

    def unassociate_physical_connection_from(self, **params):
        _params = _transfer_params(params)
        self._client.unassociate_physical_connection_from_virtual_border_router(vbr_id=self.vbr_id,
                                                                                **_params)


class _VPCVpcResource(ServiceResource):

    def __init__(self, vpc_id, _client=None):
        ServiceResource.__init__(self, "vpc.vpc", _client=_client)
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

    def describe_vpc_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_vpc_attribute(vpc_id=self.vpc_id, **_params)

    def disable_vpc_classic_link(self, **params):
        _params = _transfer_params(params)
        self._client.disable_vpc_classic_link(vpc_id=self.vpc_id, **_params)

    def enable_vpc_classic_link(self, **params):
        _params = _transfer_params(params)
        self._client.enable_vpc_classic_link(vpc_id=self.vpc_id, **_params)

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


class _VPCVpnConnectionResource(ServiceResource):

    def __init__(self, vpn_connection_id, _client=None):
        ServiceResource.__init__(self, "vpc.vpn_connection", _client=_client)
        self.vpn_connection_id = vpn_connection_id

        self.create_time = None
        self.customer_gateway_id = None
        self.effect_immediately = None
        self.ike_config = None
        self.ipsec_config = None
        self.local_subnet = None
        self.name = None
        self.remote_subnet = None
        self.status = None
        self.vco_health_check = None
        self.vpn_gateway_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_vpn_connection(vpn_connection_id=self.vpn_connection_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        self._client.describe_vpn_connection(vpn_connection_id=self.vpn_connection_id, **_params)

    def download_vpn_connection_config(self, **params):
        _params = _transfer_params(params)
        self._client.download_vpn_connection_config(vpn_connection_id=self.vpn_connection_id,
                                                    **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_vpn_connection_attribute(vpn_connection_id=self.vpn_connection_id,
                                                     **_params)

    def refresh(self):
        result = self._client.describe_vpn_connections(vpn_connection_id=self.vpn_connection_id)
        items = _new_get_key_in_response(result, 'VpnConnections.VpnConnection')
        if not items:
            raise ClientException(msg=
                                  "Failed to find vpn_connection data from DescribeVpnConnections response. "
                                  "VpnConnectionId = {0}".format(self.vpn_connection_id))
        self._assign_attributes(items[0])


class _VPCVpnGatewayResource(ServiceResource):

    def __init__(self, vpn_gateway_id, _client=None):
        ServiceResource.__init__(self, "vpc.vpn_gateway", _client=_client)
        self.vpn_gateway_id = vpn_gateway_id

    def create_vpn_route_entry(self, **params):
        _params = _transfer_params(params)
        self._client.create_vpn_route_entry(vpn_gateway_id=self.vpn_gateway_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_vpn_gateway(vpn_gateway_id=self.vpn_gateway_id, **_params)

    def delete_vpn_pbr_route_entry(self, **params):
        _params = _transfer_params(params)
        self._client.delete_vpn_pbr_route_entry(vpn_gateway_id=self.vpn_gateway_id, **_params)

    def delete_vpn_route_entry(self, **params):
        _params = _transfer_params(params)
        self._client.delete_vpn_route_entry(vpn_gateway_id=self.vpn_gateway_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        self._client.describe_vpn_gateway(vpn_gateway_id=self.vpn_gateway_id, **_params)

    def describe_vpn_route_entries(self, **params):
        _params = _transfer_params(params)
        self._client.describe_vpn_route_entries(vpn_gateway_id=self.vpn_gateway_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_vpn_gateway_attribute(vpn_gateway_id=self.vpn_gateway_id, **_params)

    def modify_vpn_pbr_route_entry_weight(self, **params):
        _params = _transfer_params(params)
        self._client.modify_vpn_pbr_route_entry_weight(vpn_gateway_id=self.vpn_gateway_id,
                                                       **_params)

    def modify_vpn_route_entry_weight(self, **params):
        _params = _transfer_params(params)
        self._client.modify_vpn_route_entry_weight(vpn_gateway_id=self.vpn_gateway_id, **_params)

    def publish_vpn_route_entry(self, **params):
        _params = _transfer_params(params)
        self._client.publish_vpn_route_entry(vpn_gateway_id=self.vpn_gateway_id, **_params)


class _VPCVpnPbrRouteEntryResource(ServiceResource):

    def __init__(self, vpn_instance_id, _client=None):
        ServiceResource.__init__(self, "vpc.vpn_pbr_route_entry", _client=_client)
        self.vpn_instance_id = vpn_instance_id

        self.create_time = None
        self.next_hop = None
        self.route_dest = None
        self.route_source = None
        self.state = None
        self.weight = None


class _VPCZoneResource(ServiceResource):

    def __init__(self, zone_id, _client=None):
        ServiceResource.__init__(self, "vpc.zone", _client=_client)
        self.zone_id = zone_id

        self.available_dedicated_host_types = None
        self.available_disk_categories = None
        self.available_instance_types = None
        self.available_resource_creation = None
        self.available_resources = None
        self.available_volume_categories = None
        self.dedicated_host_generations = None
        self.local_name = None
