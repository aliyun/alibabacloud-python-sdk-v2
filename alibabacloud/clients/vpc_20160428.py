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


class VpcClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Vpc'
        self.api_version = '2016-04-28'
        self.location_service_code = 'vpc'
        self.location_endpoint_type = 'openAPI'

    def describe_eip_gateway_info(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            instance_id=None,
            region_id=None):
        api_request = APIRequest('DescribeEipGatewayInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "RegionId": region_id}
        return self._handle_request(api_request).result

    def modify_bgp_peer_attribute(
            self,
            resource_owner_id=None,
            enable_bfd=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            bgp_group_id=None,
            bgp_peer_id=None,
            owner_id=None,
            peer_ip_address=None):
        api_request = APIRequest('ModifyBgpPeerAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "EnableBfd": enable_bfd,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "BgpGroupId": bgp_group_id,
            "BgpPeerId": bgp_peer_id,
            "OwnerId": owner_id,
            "PeerIpAddress": peer_ip_address}
        return self._handle_request(api_request).result

    def describe_vpn_ssl_server_logs(
            self,
            resource_owner_id=None,
            minute_period=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            vpn_ssl_server_id=None,
            from_=None,
            to=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeVpnSslServerLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "MinutePeriod": minute_period,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "VpnSslServerId": vpn_ssl_server_id,
            "From": from_,
            "To": to,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_express_cloud_connection_bandwidth(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            bandwidth=None,
            owner_account=None,
            owner_id=None,
            ecc_id=None):
        api_request = APIRequest('ModifyExpressCloudConnectionBandwidth',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "EccId": ecc_id}
        return self._handle_request(api_request).result

    def modify_express_cloud_connection_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            description=None,
            owner_id=None,
            ecc_id=None):
        api_request = APIRequest('ModifyExpressCloudConnectionAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id,
            "EccId": ecc_id}
        return self._handle_request(api_request).result

    def describe_express_cloud_connections(
            self,
            list_of_filter_=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeExpressCloudConnections', 'GET', 'http', 'RPC', 'query')
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

    def create_express_cloud_connection(
            self,
            resource_owner_id=None,
            peer_location=None,
            port_type=None,
            resource_owner_account=None,
            bandwidth=None,
            owner_account=None,
            description=None,
            peer_city=None,
            id_card_no=None,
            redundant_ecc_id=None,
            owner_id=None,
            contact_mail=None,
            contact_tel=None,
            idc_sp=None,
            region_id=None,
            name=None):
        api_request = APIRequest('CreateExpressCloudConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PeerLocation": peer_location,
            "PortType": port_type,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "Description": description,
            "PeerCity": peer_city,
            "IDCardNo": id_card_no,
            "RedundantEccId": redundant_ecc_id,
            "OwnerId": owner_id,
            "ContactMail": contact_mail,
            "ContactTel": contact_tel,
            "IdcSP": idc_sp,
            "RegionId": region_id,
            "Name": name}
        return self._handle_request(api_request).result

    def update_network_acl_entries(
            self,
            resource_owner_id=None,
            list_of_egress_acl_entries=None,
            client_token=None,
            region_id=None,
            network_acl_id=None,
            update_ingress_acl_entries=None,
            resource_owner_account=None,
            update_egress_acl_entries=None,
            owner_id=None,
            list_of_ingress_acl_entries=None):
        api_request = APIRequest('UpdateNetworkAclEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "EgressAclEntries": list_of_egress_acl_entries,
            "ClientToken": client_token,
            "RegionId": region_id,
            "NetworkAclId": network_acl_id,
            "UpdateIngressAclEntries": update_ingress_acl_entries,
            "ResourceOwnerAccount": resource_owner_account,
            "UpdateEgressAclEntries": update_egress_acl_entries,
            "OwnerId": owner_id,
            "IngressAclEntries": list_of_ingress_acl_entries}
        repeat_info = {"EgressAclEntries": ('EgressAclEntries',
                                            'list',
                                            'dict',
                                            [('NetworkAclEntryName',
                                              'str',
                                              None,
                                              None),
                                             ('NetworkAclEntryId',
                                              'str',
                                              None,
                                              None),
                                                ('Policy',
                                                 'str',
                                                 None,
                                                 None),
                                                ('Protocol',
                                                 'str',
                                                 None,
                                                 None),
                                                ('DestinationCidrIp',
                                                 'str',
                                                 None,
                                                 None),
                                                ('Port',
                                                 'str',
                                                 None,
                                                 None),
                                                ('EntryType',
                                                 'str',
                                                 None,
                                                 None),
                                                ('Description',
                                                 'str',
                                                 None,
                                                 None),
                                             ]),
                       "IngressAclEntries": ('IngressAclEntries',
                                             'list',
                                             'dict',
                                             [('NetworkAclEntryName',
                                               'str',
                                               None,
                                               None),
                                              ('NetworkAclEntryId',
                                                 'str',
                                                 None,
                                                 None),
                                                 ('Policy',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('Protocol',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('SourceCidrIp',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('Port',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('EntryType',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('Description',
                                                  'str',
                                                  None,
                                                  None),
                                              ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def unassociate_network_acl(
            self,
            resource_owner_id=None,
            client_token=None,
            region_id=None,
            network_acl_id=None,
            list_of_resource=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('UnassociateNetworkAcl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "RegionId": region_id,
            "NetworkAclId": network_acl_id,
            "Resource": list_of_resource,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        repeat_info = {
            "Resource": (
                'Resource', 'list', 'dict', [
                    ('ResourceType', 'str', None, None), ('ResourceId', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_network_acl_attributes(
            self,
            resource_owner_id=None,
            client_token=None,
            description=None,
            region_id=None,
            network_acl_id=None,
            resource_owner_account=None,
            network_acl_name=None,
            owner_id=None):
        api_request = APIRequest('ModifyNetworkAclAttributes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "Description": description,
            "RegionId": region_id,
            "NetworkAclId": network_acl_id,
            "ResourceOwnerAccount": resource_owner_account,
            "NetworkAclName": network_acl_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_network_acls(
            self,
            resource_owner_id=None,
            client_token=None,
            page_number=None,
            region_id=None,
            page_size=None,
            network_acl_id=None,
            resource_id=None,
            resource_owner_account=None,
            network_acl_name=None,
            owner_id=None,
            resource_type=None,
            vpc_id=None):
        api_request = APIRequest('DescribeNetworkAcls', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "NetworkAclId": network_acl_id,
            "ResourceId": resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "NetworkAclName": network_acl_name,
            "OwnerId": owner_id,
            "ResourceType": resource_type,
            "VpcId": vpc_id}
        return self._handle_request(api_request).result

    def describe_network_acl_attributes(
            self,
            resource_owner_id=None,
            client_token=None,
            region_id=None,
            network_acl_id=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeNetworkAclAttributes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "RegionId": region_id,
            "NetworkAclId": network_acl_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_network_acl(
            self,
            resource_owner_id=None,
            client_token=None,
            region_id=None,
            network_acl_id=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteNetworkAcl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "RegionId": region_id,
            "NetworkAclId": network_acl_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_network_acl(
            self,
            resource_owner_id=None,
            client_token=None,
            description=None,
            region_id=None,
            resource_owner_account=None,
            network_acl_name=None,
            owner_id=None,
            vpc_id=None):
        api_request = APIRequest('CreateNetworkAcl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "Description": description,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "NetworkAclName": network_acl_name,
            "OwnerId": owner_id,
            "VpcId": vpc_id}
        return self._handle_request(api_request).result

    def copy_network_acl_entries(
            self,
            resource_owner_id=None,
            client_token=None,
            region_id=None,
            network_acl_id=None,
            source_network_acl_id=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('CopyNetworkAclEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "RegionId": region_id,
            "NetworkAclId": network_acl_id,
            "SourceNetworkAclId": source_network_acl_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def associate_network_acl(
            self,
            resource_owner_id=None,
            client_token=None,
            region_id=None,
            network_acl_id=None,
            list_of_resource=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('AssociateNetworkAcl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "RegionId": region_id,
            "NetworkAclId": network_acl_id,
            "Resource": list_of_resource,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        repeat_info = {
            "Resource": (
                'Resource', 'list', 'dict', [
                    ('ResourceType', 'str', None, None), ('ResourceId', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_common_bandwidth_package_ip_bandwidth(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            bandwidth=None,
            owner_account=None,
            eip_id=None,
            owner_id=None):
        api_request = APIRequest(
            'ModifyCommonBandwidthPackageIpBandwidth',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "EipId": eip_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def cancel_common_bandwidth_package_ip_bandwidth(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            eip_id=None,
            owner_id=None):
        api_request = APIRequest(
            'CancelCommonBandwidthPackageIpBandwidth',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "EipId": eip_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_vpn_pbr_route_entry(
            self,
            route_source=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            weight=None,
            description=None,
            vpn_gateway_id=None,
            owner_id=None,
            route_dest=None,
            next_hop=None,
            publish_vpc=None,
            region_id=None,
            overlay_mode=None):
        api_request = APIRequest('CreateVpnPbrRouteEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RouteSource": route_source,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Weight": weight,
            "Description": description,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "RouteDest": route_dest,
            "NextHop": next_hop,
            "PublishVpc": publish_vpc,
            "RegionId": region_id,
            "OverlayMode": overlay_mode}
        return self._handle_request(api_request).result

    def create_vpn_route_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            weight=None,
            description=None,
            vpn_gateway_id=None,
            owner_id=None,
            route_dest=None,
            next_hop=None,
            publish_vpc=None,
            region_id=None,
            overlay_mode=None):
        api_request = APIRequest('CreateVpnRouteEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Weight": weight,
            "Description": description,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "RouteDest": route_dest,
            "NextHop": next_hop,
            "PublishVpc": publish_vpc,
            "RegionId": region_id,
            "OverlayMode": overlay_mode}
        return self._handle_request(api_request).result

    def delete_vpn_pbr_route_entry(
            self,
            route_source=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            weight=None,
            vpn_gateway_id=None,
            owner_id=None,
            route_dest=None,
            next_hop=None,
            region_id=None,
            overlay_mode=None):
        api_request = APIRequest('DeleteVpnPbrRouteEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RouteSource": route_source,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Weight": weight,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "RouteDest": route_dest,
            "NextHop": next_hop,
            "RegionId": region_id,
            "OverlayMode": overlay_mode}
        return self._handle_request(api_request).result

    def delete_vpn_route_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            weight=None,
            vpn_gateway_id=None,
            owner_id=None,
            route_dest=None,
            next_hop=None,
            overlay_mode=None):
        api_request = APIRequest('DeleteVpnRouteEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Weight": weight,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "RouteDest": route_dest,
            "NextHop": next_hop,
            "OverlayMode": overlay_mode}
        return self._handle_request(api_request).result

    def describe_vpn_route_entries(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            vpn_gateway_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeVpnRouteEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_vpn_pbr_route_entries(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            vpn_gateway_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeVpnPbrRouteEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def publish_vpn_route_entry(
            self,
            resource_owner_id=None,
            publish_vpc=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            vpn_gateway_id=None,
            owner_id=None,
            route_dest=None,
            next_hop=None,
            route_type=None):
        api_request = APIRequest('PublishVpnRouteEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PublishVpc": publish_vpc,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "RouteDest": route_dest,
            "NextHop": next_hop,
            "RouteType": route_type}
        return self._handle_request(api_request).result

    def modify_vpn_route_entry_weight(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            weight=None,
            vpn_gateway_id=None,
            owner_id=None,
            new_weight=None,
            route_dest=None,
            next_hop=None,
            region_id=None,
            overlay_mode=None):
        api_request = APIRequest('ModifyVpnRouteEntryWeight', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Weight": weight,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "NewWeight": new_weight,
            "RouteDest": route_dest,
            "NextHop": next_hop,
            "RegionId": region_id,
            "OverlayMode": overlay_mode}
        return self._handle_request(api_request).result

    def modify_vpn_pbr_route_entry_weight(
            self,
            route_source=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            weight=None,
            vpn_gateway_id=None,
            owner_id=None,
            new_weight=None,
            route_dest=None,
            next_hop=None,
            region_id=None,
            overlay_mode=None):
        api_request = APIRequest('ModifyVpnPbrRouteEntryWeight', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RouteSource": route_source,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Weight": weight,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "NewWeight": new_weight,
            "RouteDest": route_dest,
            "NextHop": next_hop,
            "RegionId": region_id,
            "OverlayMode": overlay_mode}
        return self._handle_request(api_request).result

    def describe_physical_connection_loa(
            self,
            resource_owner_id=None,
            instance_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribePhysicalConnectionLOA', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_physical_connection_setup_order(
            self,
            access_point_id=None,
            redundant_physical_connection_id=None,
            resource_owner_id=None,
            port_type=None,
            auto_pay=None,
            region_id=None,
            client_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            line_operator=None):
        api_request = APIRequest('CreatePhysicalConnectionSetupOrder',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccessPointId": access_point_id,
            "RedundantPhysicalConnectionId": redundant_physical_connection_id,
            "ResourceOwnerId": resource_owner_id,
            "PortType": port_type,
            "AutoPay": auto_pay,
            "RegionId": region_id,
            "ClientToken": client_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "LineOperator": line_operator}
        return self._handle_request(api_request).result

    def create_physical_connection_occupancy_order(
            self,
            period=None,
            resource_owner_id=None,
            auto_pay=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            physical_connection_id=None,
            owner_account=None,
            owner_id=None,
            instance_charge_type=None,
            pricing_cycle=None):
        api_request = APIRequest('CreatePhysicalConnectionOccupancyOrder',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "PhysicalConnectionId": physical_connection_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceChargeType": instance_charge_type,
            "PricingCycle": pricing_cycle}
        return self._handle_request(api_request).result

    def complete_physical_connection_loa(
            self,
            line_label=None,
            line_code=None,
            resource_owner_id=None,
            instance_id=None,
            client_token=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CompletePhysicalConnectionLOA', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LineLabel": line_label,
            "LineCode": line_code,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ClientToken": client_token,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def apply_physical_connection_loa(
            self,
            resource_owner_id=None,
            peer_location=None,
            client_token=None,
            resource_owner_account=None,
            bandwidth=None,
            line_type=None,
            owner_account=None,
            construction_time=None,
            owner_id=None,
            instance_id=None,
            region_id=None,
            company_name=None,
            si=None,
            list_of_pm_info=None):
        api_request = APIRequest('ApplyPhysicalConnectionLOA', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PeerLocation": peer_location,
            "ClientToken": client_token,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "LineType": line_type,
            "OwnerAccount": owner_account,
            "ConstructionTime": construction_time,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "RegionId": region_id,
            "CompanyName": company_name,
            "Si": si,
            "PMInfo": list_of_pm_info}
        repeat_info = {"PMInfo": ('PMInfo',
                                  'list',
                                  'dict',
                                  [('PMCertificateNo',
                                    'str',
                                    None,
                                    None),
                                   ('PMName',
                                    'str',
                                    None,
                                    None),
                                      ('PMCertificateType',
                                       'str',
                                       None,
                                       None),
                                      ('PMContactInfo',
                                       'str',
                                       None,
                                       None),
                                      ('PMGender',
                                       'str',
                                       None,
                                       None),
                                   ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def convert_bandwidth_package(
            self,
            resource_owner_id=None,
            client_token=None,
            region_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('ConvertBandwidthPackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "RegionId": region_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_route_entry(
            self,
            route_entry_name=None,
            region_id=None,
            route_entry_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyRouteEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RouteEntryName": route_entry_name,
            "RegionId": region_id,
            "RouteEntryId": route_entry_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_route_entry_list(
            self,
            resource_owner_id=None,
            route_entry_name=None,
            region_id=None,
            next_token=None,
            route_entry_type=None,
            ip_version=None,
            next_hop_id=None,
            next_hop_type=None,
            route_table_id=None,
            resource_owner_account=None,
            destination_cidr_block=None,
            owner_account=None,
            owner_id=None,
            max_result=None,
            route_entry_id=None):
        api_request = APIRequest('DescribeRouteEntryList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RouteEntryName": route_entry_name,
            "RegionId": region_id,
            "NextToken": next_token,
            "RouteEntryType": route_entry_type,
            "IpVersion": ip_version,
            "NextHopId": next_hop_id,
            "NextHopType": next_hop_type,
            "RouteTableId": route_table_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DestinationCidrBlock": destination_cidr_block,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "MaxResult": max_result,
            "RouteEntryId": route_entry_id}
        return self._handle_request(api_request).result

    def create_ipv6_translator_acl_list(
            self,
            resource_owner_id=None,
            acl_name=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CreateIPv6TranslatorAclList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AclName": acl_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_ipv6_translator_acl_list(
            self,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteIPv6TranslatorAclList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_ipv6_translator_acl_list_entry(
            self,
            acl_id=None,
            resource_owner_id=None,
            acl_entry_ip=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            acl_entry_comment=None,
            owner_id=None):
        api_request = APIRequest('AddIPv6TranslatorAclListEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "AclEntryIp": acl_entry_ip,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "AclEntryComment": acl_entry_comment,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_ipv6_translator_acl_lists(
            self,
            acl_id=None,
            resource_owner_id=None,
            acl_name=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeIPv6TranslatorAclLists', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "AclName": acl_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_ipv6_translator_acl_attribute(
            self,
            acl_id=None,
            resource_owner_id=None,
            acl_name=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyIPv6TranslatorAclAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "AclName": acl_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def remove_ipv6_translator_acl_list_entry(
            self,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            acl_entry_id=None):
        api_request = APIRequest('RemoveIPv6TranslatorAclListEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AclEntryId": acl_entry_id}
        return self._handle_request(api_request).result

    def describe_ipv6_translator_acl_list_attributes(
            self,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest(
            'DescribeIPv6TranslatorAclListAttributes',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_ipv6_translator_acl_list_entry(
            self,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            acl_entry_comment=None,
            owner_id=None,
            acl_entry_id=None):
        api_request = APIRequest('ModifyIPv6TranslatorAclListEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "AclEntryComment": acl_entry_comment,
            "OwnerId": owner_id,
            "AclEntryId": acl_entry_id}
        return self._handle_request(api_request).result

    def un_tag_resources(
            self,
            list_of_resource_id=None,
            region_id=None,
            list_of_tag_key=None,
            resource_type=None):
        api_request = APIRequest('UnTagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceId": list_of_resource_id,
            "RegionId": region_id,
            "TagKey": list_of_tag_key,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "TagKey": ('TagKey', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def tag_resources(
            self,
            list_of_resource_id=None,
            region_id=None,
            list_of_tag=None,
            resource_type=None):
        api_request = APIRequest('TagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceId": list_of_resource_id,
            "RegionId": region_id,
            "Tag": list_of_tag,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_tag_resources(
            self,
            list_of_resource_id=None,
            region_id=None,
            next_token=None,
            list_of_tag=None,
            resource_type=None):
        api_request = APIRequest('ListTagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceId": list_of_resource_id,
            "RegionId": region_id,
            "NextToken": next_token,
            "Tag": list_of_tag,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_ipv6_internet_bandwidth(
            self,
            resource_owner_id=None,
            client_token=None,
            ipv6_internet_bandwidth_id=None,
            region_id=None,
            bandwidth=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            ipv6_address_id=None):
        api_request = APIRequest('ModifyIpv6InternetBandwidth', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "Ipv6InternetBandwidthId": ipv6_internet_bandwidth_id,
            "RegionId": region_id,
            "Bandwidth": bandwidth,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Ipv6AddressId": ipv6_address_id}
        return self._handle_request(api_request).result

    def modify_ipv6_gateway_spec(
            self,
            resource_owner_id=None,
            client_token=None,
            spec=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            ipv6_gateway_id=None):
        api_request = APIRequest('ModifyIpv6GatewaySpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "Spec": spec,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Ipv6GatewayId": ipv6_gateway_id}
        return self._handle_request(api_request).result

    def modify_ipv6_gateway_attribute(
            self,
            resource_owner_id=None,
            description=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            ipv6_gateway_id=None,
            name=None):
        api_request = APIRequest('ModifyIpv6GatewayAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Description": description,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Ipv6GatewayId": ipv6_gateway_id,
            "Name": name}
        return self._handle_request(api_request).result

    def modify_ipv6_address_attribute(
            self,
            resource_owner_id=None,
            description=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            ipv6_address_id=None,
            name=None):
        api_request = APIRequest('ModifyIpv6AddressAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Description": description,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Ipv6AddressId": ipv6_address_id,
            "Name": name}
        return self._handle_request(api_request).result

    def describe_ipv6_gateways(
            self,
            resource_owner_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            vpc_id=None,
            ipv6_gateway_id=None,
            name=None):
        api_request = APIRequest('DescribeIpv6Gateways', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "VpcId": vpc_id,
            "Ipv6GatewayId": ipv6_gateway_id,
            "Name": name}
        return self._handle_request(api_request).result

    def describe_ipv6_gateway_attribute(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            ipv6_gateway_id=None):
        api_request = APIRequest('DescribeIpv6GatewayAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Ipv6GatewayId": ipv6_gateway_id}
        return self._handle_request(api_request).result

    def describe_ipv6_egress_only_rules(
            self,
            resource_owner_id=None,
            page_number=None,
            ipv6_egress_only_rule_id=None,
            region_id=None,
            page_size=None,
            instance_type=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            instance_id=None,
            ipv6_gateway_id=None,
            name=None):
        api_request = APIRequest('DescribeIpv6EgressOnlyRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "PageNumber": page_number,
            "Ipv6EgressOnlyRuleId": ipv6_egress_only_rule_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "InstanceType": instance_type,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "Ipv6GatewayId": ipv6_gateway_id,
            "Name": name}
        return self._handle_request(api_request).result

    def describe_ipv6_addresses(
            self,
            resource_owner_id=None,
            ipv6_internet_bandwidth_id=None,
            network_type=None,
            page_number=None,
            region_id=None,
            associated_instance_type=None,
            page_size=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            vswitch_id=None,
            ipv6_address_id=None,
            vpc_id=None,
            name=None,
            ipv6_address=None,
            associated_instance_id=None):
        api_request = APIRequest('DescribeIpv6Addresses', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Ipv6InternetBandwidthId": ipv6_internet_bandwidth_id,
            "NetworkType": network_type,
            "PageNumber": page_number,
            "RegionId": region_id,
            "AssociatedInstanceType": associated_instance_type,
            "PageSize": page_size,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "VSwitchId": vswitch_id,
            "Ipv6AddressId": ipv6_address_id,
            "VpcId": vpc_id,
            "Name": name,
            "Ipv6Address": ipv6_address,
            "AssociatedInstanceId": associated_instance_id}
        return self._handle_request(api_request).result

    def delete_ipv6_internet_bandwidth(
            self,
            resource_owner_id=None,
            ipv6_internet_bandwidth_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            ipv6_address_id=None):
        api_request = APIRequest('DeleteIpv6InternetBandwidth', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Ipv6InternetBandwidthId": ipv6_internet_bandwidth_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Ipv6AddressId": ipv6_address_id}
        return self._handle_request(api_request).result

    def delete_ipv6_gateway(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            ipv6_gateway_id=None):
        api_request = APIRequest('DeleteIpv6Gateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Ipv6GatewayId": ipv6_gateway_id}
        return self._handle_request(api_request).result

    def delete_ipv6_egress_only_rule(
            self,
            resource_owner_id=None,
            client_token=None,
            ipv6_egress_only_rule_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteIpv6EgressOnlyRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "Ipv6EgressOnlyRuleId": ipv6_egress_only_rule_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_ipv6_gateway(
            self,
            resource_owner_id=None,
            client_token=None,
            description=None,
            spec=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            vpc_id=None,
            name=None):
        api_request = APIRequest('CreateIpv6Gateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "Description": description,
            "Spec": spec,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "VpcId": vpc_id,
            "Name": name}
        return self._handle_request(api_request).result

    def create_ipv6_egress_only_rule(
            self,
            resource_owner_id=None,
            client_token=None,
            description=None,
            region_id=None,
            instance_type=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            instance_id=None,
            ipv6_gateway_id=None,
            name=None):
        api_request = APIRequest('CreateIpv6EgressOnlyRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "Description": description,
            "RegionId": region_id,
            "InstanceType": instance_type,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "Ipv6GatewayId": ipv6_gateway_id,
            "Name": name}
        return self._handle_request(api_request).result

    def allocate_ipv6_internet_bandwidth(
            self,
            resource_owner_id=None,
            client_token=None,
            region_id=None,
            bandwidth=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            ipv6_address_id=None,
            internet_charge_type=None,
            ipv6_gateway_id=None):
        api_request = APIRequest('AllocateIpv6InternetBandwidth', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "RegionId": region_id,
            "Bandwidth": bandwidth,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Ipv6AddressId": ipv6_address_id,
            "InternetChargeType": internet_charge_type,
            "Ipv6GatewayId": ipv6_gateway_id}
        return self._handle_request(api_request).result

    def delete_express_connect(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            force=None,
            router_interface_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteExpressConnect', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Force": force,
            "RouterInterfaceId": router_interface_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_ipv6_translator(
            self,
            resource_owner_id=None,
            auto_pay=None,
            resource_owner_account=None,
            client_token=None,
            bandwidth=None,
            owner_account=None,
            owner_id=None,
            spec=None,
            duration=None,
            region_id=None,
            name=None,
            pay_type=None,
            pricing_cycle=None):
        api_request = APIRequest('CreateIPv6Translator', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Spec": spec,
            "Duration": duration,
            "RegionId": region_id,
            "Name": name,
            "PayType": pay_type,
            "PricingCycle": pricing_cycle}
        return self._handle_request(api_request).result

    def describe_ipv6_translators(
            self,
            business_status=None,
            resource_owner_id=None,
            resource_owner_account=None,
            allocate_ipv6_addr=None,
            owner_account=None,
            allocate_ipv4_addr=None,
            owner_id=None,
            spec=None,
            page_number=None,
            region_id=None,
            name=None,
            page_size=None,
            ipv6_translator_id=None,
            pay_type=None,
            status=None):
        api_request = APIRequest('DescribeIPv6Translators', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BusinessStatus": business_status,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "AllocateIpv6Addr": allocate_ipv6_addr,
            "OwnerAccount": owner_account,
            "AllocateIpv4Addr": allocate_ipv4_addr,
            "OwnerId": owner_id,
            "Spec": spec,
            "PageNumber": page_number,
            "RegionId": region_id,
            "Name": name,
            "PageSize": page_size,
            "Ipv6TranslatorId": ipv6_translator_id,
            "PayType": pay_type,
            "Status": status}
        return self._handle_request(api_request).result

    def modify_ipv6_translator_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            name=None,
            description=None,
            ipv6_translator_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyIPv6TranslatorAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "Ipv6TranslatorId": ipv6_translator_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_ipv6_translator_bandwidth(
            self,
            resource_owner_id=None,
            auto_pay=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            bandwidth=None,
            owner_account=None,
            ipv6_translator_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyIPv6TranslatorBandwidth', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "Ipv6TranslatorId": ipv6_translator_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_ipv6_translator_entry(
            self,
            backend_ipv4_port=None,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            entry_name=None,
            owner_account=None,
            owner_id=None,
            acl_status=None,
            entry_bandwidth=None,
            acl_type=None,
            allocate_ipv6_port=None,
            entry_description=None,
            region_id=None,
            backend_ipv4_addr=None,
            trans_protocol=None,
            ipv6_translator_id=None):
        api_request = APIRequest('CreateIPv6TranslatorEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BackendIpv4Port": backend_ipv4_port,
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "EntryName": entry_name,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AclStatus": acl_status,
            "EntryBandwidth": entry_bandwidth,
            "AclType": acl_type,
            "AllocateIpv6Port": allocate_ipv6_port,
            "EntryDescription": entry_description,
            "RegionId": region_id,
            "BackendIpv4Addr": backend_ipv4_addr,
            "TransProtocol": trans_protocol,
            "Ipv6TranslatorId": ipv6_translator_id}
        return self._handle_request(api_request).result

    def delete_ipv6_translator_entry(
            self,
            resource_owner_id=None,
            ipv6_translator_entry_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            ipv6_translator_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteIPv6TranslatorEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Ipv6TranslatorEntryId": ipv6_translator_entry_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Ipv6TranslatorId": ipv6_translator_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_ipv6_translator_entry(
            self,
            backend_ipv4_port=None,
            acl_id=None,
            resource_owner_id=None,
            ipv6_translator_entry_id=None,
            resource_owner_account=None,
            entry_name=None,
            owner_account=None,
            owner_id=None,
            acl_status=None,
            entry_bandwidth=None,
            acl_type=None,
            allocate_ipv6_port=None,
            entry_description=None,
            region_id=None,
            backend_ipv4_addr=None,
            trans_protocol=None):
        api_request = APIRequest('ModifyIPv6TranslatorEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BackendIpv4Port": backend_ipv4_port,
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "Ipv6TranslatorEntryId": ipv6_translator_entry_id,
            "ResourceOwnerAccount": resource_owner_account,
            "EntryName": entry_name,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AclStatus": acl_status,
            "EntryBandwidth": entry_bandwidth,
            "AclType": acl_type,
            "AllocateIpv6Port": allocate_ipv6_port,
            "EntryDescription": entry_description,
            "RegionId": region_id,
            "BackendIpv4Addr": backend_ipv4_addr,
            "TransProtocol": trans_protocol}
        return self._handle_request(api_request).result

    def describe_ipv6_translator_entries(
            self,
            backend_ipv4_port=None,
            acl_id=None,
            resource_owner_id=None,
            ipv6_translator_entry_id=None,
            resource_owner_account=None,
            entry_name=None,
            allocate_ipv6_addr=None,
            client_token=None,
            owner_account=None,
            owner_id=None,
            acl_status=None,
            page_number=None,
            acl_type=None,
            allocate_ipv6_port=None,
            region_id=None,
            page_size=None,
            backend_ipv4_addr=None,
            trans_protocol=None,
            ipv6_translator_id=None):
        api_request = APIRequest('DescribeIPv6TranslatorEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BackendIpv4Port": backend_ipv4_port,
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "Ipv6TranslatorEntryId": ipv6_translator_entry_id,
            "ResourceOwnerAccount": resource_owner_account,
            "EntryName": entry_name,
            "AllocateIpv6Addr": allocate_ipv6_addr,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AclStatus": acl_status,
            "PageNumber": page_number,
            "AclType": acl_type,
            "AllocateIpv6Port": allocate_ipv6_port,
            "RegionId": region_id,
            "PageSize": page_size,
            "BackendIpv4Addr": backend_ipv4_addr,
            "TransProtocol": trans_protocol,
            "Ipv6TranslatorId": ipv6_translator_id}
        return self._handle_request(api_request).result

    def delete_ipv6_translator(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            ipv6_translator_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteIPv6Translator', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Ipv6TranslatorId": ipv6_translator_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_flow_log_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            description=None,
            owner_id=None,
            flow_log_id=None,
            flow_log_name=None):
        api_request = APIRequest('ModifyFlowLogAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id,
            "FlowLogName": flow_log_name}
        return self._handle_request(api_request).result

    def describe_flow_logs(
            self,
            resource_owner_id=None,
            resource_id=None,
            project_name=None,
            log_store_name=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            owner_id=None,
            resource_type=None,
            page_number=None,
            region_id=None,
            page_size=None,
            traffic_type=None,
            flow_log_id=None,
            flow_log_name=None,
            status=None):
        api_request = APIRequest('DescribeFlowLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "ProjectName": project_name,
            "LogStoreName": log_store_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "ResourceType": resource_type,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "TrafficType": traffic_type,
            "FlowLogId": flow_log_id,
            "FlowLogName": flow_log_name,
            "Status": status}
        return self._handle_request(api_request).result

    def delete_flow_log(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            flow_log_id=None):
        api_request = APIRequest('DeleteFlowLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id}
        return self._handle_request(api_request).result

    def deactive_flow_log(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            flow_log_id=None):
        api_request = APIRequest('DeactiveFlowLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id}
        return self._handle_request(api_request).result

    def create_flow_log(
            self,
            resource_owner_id=None,
            resource_id=None,
            project_name=None,
            log_store_name=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            owner_id=None,
            resource_type=None,
            region_id=None,
            traffic_type=None,
            flow_log_name=None):
        api_request = APIRequest('CreateFlowLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "ProjectName": project_name,
            "LogStoreName": log_store_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "ResourceType": resource_type,
            "RegionId": region_id,
            "TrafficType": traffic_type,
            "FlowLogName": flow_log_name}
        return self._handle_request(api_request).result

    def active_flow_log(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            flow_log_id=None):
        api_request = APIRequest('ActiveFlowLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id}
        return self._handle_request(api_request).result

    def unassociate_route_table(
            self,
            resource_owner_id=None,
            client_token=None,
            region_id=None,
            route_table_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            vswitch_id=None):
        api_request = APIRequest('UnassociateRouteTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "RegionId": region_id,
            "RouteTableId": route_table_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "VSwitchId": vswitch_id}
        return self._handle_request(api_request).result

    def delete_route_table(
            self,
            resource_owner_id=None,
            region_id=None,
            route_table_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteRouteTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "RouteTableId": route_table_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_route_table(
            self,
            resource_owner_id=None,
            client_token=None,
            description=None,
            route_table_name=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            vpc_id=None):
        api_request = APIRequest('CreateRouteTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "Description": description,
            "RouteTableName": route_table_name,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "VpcId": vpc_id}
        return self._handle_request(api_request).result

    def associate_route_table(
            self,
            resource_owner_id=None,
            client_token=None,
            region_id=None,
            route_table_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            vswitch_id=None):
        api_request = APIRequest('AssociateRouteTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "RegionId": region_id,
            "RouteTableId": route_table_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "VSwitchId": vswitch_id}
        return self._handle_request(api_request).result

    def create_vpn_gateway(
            self,
            resource_owner_id=None,
            period=None,
            auto_pay=None,
            resource_owner_account=None,
            bandwidth=None,
            enable_ipsec=None,
            owner_account=None,
            owner_id=None,
            enable_ssl=None,
            ssl_connections=None,
            region_id=None,
            vpc_id=None,
            name=None,
            instance_charge_type=None):
        api_request = APIRequest('CreateVpnGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "EnableIpsec": enable_ipsec,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "EnableSsl": enable_ssl,
            "SslConnections": ssl_connections,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "Name": name,
            "InstanceChargeType": instance_charge_type}
        return self._handle_request(api_request).result

    def move_resource_group(
            self,
            resource_owner_id=None,
            resource_id=None,
            new_resource_group_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('MoveResourceGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": resource_id,
            "NewResourceGroupId": new_resource_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        return self._handle_request(api_request).result

    def revoke_instance_from_cen(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            cen_id=None,
            client_token=None,
            owner_account=None,
            instance_type=None,
            cen_owner_id=None,
            owner_id=None):
        api_request = APIRequest('RevokeInstanceFromCen', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "CenId": cen_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "InstanceType": instance_type,
            "CenOwnerId": cen_owner_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def grant_instance_to_cen(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            cen_id=None,
            client_token=None,
            owner_account=None,
            instance_type=None,
            cen_owner_id=None,
            owner_id=None):
        api_request = APIRequest('GrantInstanceToCen', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "CenId": cen_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "InstanceType": instance_type,
            "CenOwnerId": cen_owner_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_grant_rules_to_cen(
            self,
            resource_group_id=None,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            instance_type=None,
            owner_id=None):
        api_request = APIRequest('DescribeGrantRulesToCen', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "InstanceType": instance_type,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_ssl_vpn_server(
            self,
            cipher=None,
            resource_owner_id=None,
            client_ip_pool=None,
            resource_owner_account=None,
            client_token=None,
            compress=None,
            owner_account=None,
            owner_id=None,
            ssl_vpn_server_id=None,
            local_subnet=None,
            region_id=None,
            port=None,
            proto=None,
            name=None):
        api_request = APIRequest('ModifySslVpnServer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Cipher": cipher,
            "ResourceOwnerId": resource_owner_id,
            "ClientIpPool": client_ip_pool,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Compress": compress,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "SslVpnServerId": ssl_vpn_server_id,
            "LocalSubnet": local_subnet,
            "RegionId": region_id,
            "Port": port,
            "Proto": proto,
            "Name": name}
        return self._handle_request(api_request).result

    def modify_ssl_vpn_client_cert(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            name=None,
            owner_id=None,
            ssl_vpn_client_cert_id=None):
        api_request = APIRequest('ModifySslVpnClientCert', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "OwnerId": owner_id,
            "SslVpnClientCertId": ssl_vpn_client_cert_id}
        return self._handle_request(api_request).result

    def describe_ssl_vpn_servers(
            self,
            ssl_vpn_server_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            page_size=None,
            vpn_gateway_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeSslVpnServers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SslVpnServerId": ssl_vpn_server_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "PageSize": page_size,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_ssl_vpn_client_certs(
            self,
            ssl_vpn_server_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            page_size=None,
            owner_id=None,
            ssl_vpn_client_cert_id=None,
            page_number=None):
        api_request = APIRequest('DescribeSslVpnClientCerts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SslVpnServerId": ssl_vpn_server_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "SslVpnClientCertId": ssl_vpn_client_cert_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_ssl_vpn_client_cert(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            ssl_vpn_client_cert_id=None):
        api_request = APIRequest('DescribeSslVpnClientCert', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "SslVpnClientCertId": ssl_vpn_client_cert_id}
        return self._handle_request(api_request).result

    def delete_ssl_vpn_server(
            self,
            ssl_vpn_server_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteSslVpnServer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SslVpnServerId": ssl_vpn_server_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_ssl_vpn_client_cert(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            owner_id=None,
            ssl_vpn_client_cert_id=None):
        api_request = APIRequest('DeleteSslVpnClientCert', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "SslVpnClientCertId": ssl_vpn_client_cert_id}
        return self._handle_request(api_request).result

    def create_ssl_vpn_server(
            self,
            cipher=None,
            resource_owner_id=None,
            client_ip_pool=None,
            resource_owner_account=None,
            client_token=None,
            compress=None,
            owner_account=None,
            vpn_gateway_id=None,
            owner_id=None,
            local_subnet=None,
            region_id=None,
            port=None,
            proto=None,
            name=None):
        api_request = APIRequest('CreateSslVpnServer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Cipher": cipher,
            "ResourceOwnerId": resource_owner_id,
            "ClientIpPool": client_ip_pool,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Compress": compress,
            "OwnerAccount": owner_account,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "LocalSubnet": local_subnet,
            "RegionId": region_id,
            "Port": port,
            "Proto": proto,
            "Name": name}
        return self._handle_request(api_request).result

    def create_ssl_vpn_client_cert(
            self,
            ssl_vpn_server_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            name=None,
            owner_id=None):
        api_request = APIRequest('CreateSslVpnClientCert', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SslVpnServerId": ssl_vpn_server_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def remove_global_acceleration_instance_ip(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            ip_instance_id=None,
            owner_id=None,
            global_acceleration_instance_id=None):
        api_request = APIRequest('RemoveGlobalAccelerationInstanceIp',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "IpInstanceId": ip_instance_id,
            "OwnerId": owner_id,
            "GlobalAccelerationInstanceId": global_acceleration_instance_id}
        return self._handle_request(api_request).result

    def add_global_acceleration_instance_ip(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            ip_instance_id=None,
            owner_id=None,
            global_acceleration_instance_id=None):
        api_request = APIRequest('AddGlobalAccelerationInstanceIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "IpInstanceId": ip_instance_id,
            "OwnerId": owner_id,
            "GlobalAccelerationInstanceId": global_acceleration_instance_id}
        return self._handle_request(api_request).result

    def describe_route_table_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            page_number=None,
            router_type=None,
            resource_group_id=None,
            route_table_name=None,
            region_id=None,
            router_id=None,
            vpc_id=None,
            page_size=None,
            list_of_tag=None,
            route_table_id=None):
        api_request = APIRequest('DescribeRouteTableList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "RouterType": router_type,
            "ResourceGroupId": resource_group_id,
            "RouteTableName": route_table_name,
            "RegionId": region_id,
            "RouterId": router_id,
            "VpcId": vpc_id,
            "PageSize": page_size,
            "Tag": list_of_tag,
            "RouteTableId": route_table_id}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_route_table_attributes(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            bandwidth=None,
            owner_account=None,
            description=None,
            owner_id=None,
            kbps_bandwidth=None,
            route_table_name=None,
            region_id=None,
            resource_uid=None,
            resource_bid=None,
            route_table_id=None):
        api_request = APIRequest('ModifyRouteTableAttributes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "KbpsBandwidth": kbps_bandwidth,
            "RouteTableName": route_table_name,
            "RegionId": region_id,
            "ResourceUid": resource_uid,
            "ResourceBid": resource_bid,
            "RouteTableId": route_table_id}
        return self._handle_request(api_request).result

    def describe_bgp_networks(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            router_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeBgpNetworks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "RouterId": router_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_common_bandwidth_package_pay_type(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            auto_pay=None,
            resource_owner_account=None,
            bandwidth=None,
            owner_account=None,
            owner_id=None,
            duration=None,
            kbps_bandwidth=None,
            region_id=None,
            resource_uid=None,
            resource_bid=None,
            pay_type=None,
            pricing_cycle=None):
        api_request = APIRequest('ModifyCommonBandwidthPackagePayType',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Duration": duration,
            "KbpsBandwidth": kbps_bandwidth,
            "RegionId": region_id,
            "ResourceUid": resource_uid,
            "ResourceBid": resource_bid,
            "PayType": pay_type,
            "PricingCycle": pricing_cycle}
        return self._handle_request(api_request).result

    def unassociate_global_acceleration_instance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            instance_type=None,
            owner_id=None,
            global_acceleration_instance_id=None):
        api_request = APIRequest('UnassociateGlobalAccelerationInstance',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "InstanceType": instance_type,
            "OwnerId": owner_id,
            "GlobalAccelerationInstanceId": global_acceleration_instance_id}
        return self._handle_request(api_request).result

    def modify_global_acceleration_instance_spec(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            bandwidth=None,
            owner_account=None,
            owner_id=None,
            global_acceleration_instance_id=None):
        api_request = APIRequest('ModifyGlobalAccelerationInstanceSpec',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "GlobalAccelerationInstanceId": global_acceleration_instance_id}
        return self._handle_request(api_request).result

    def modify_global_acceleration_instance_attributes(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            description=None,
            owner_id=None,
            global_acceleration_instance_id=None):
        api_request = APIRequest(
            'ModifyGlobalAccelerationInstanceAttributes',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id,
            "GlobalAccelerationInstanceId": global_acceleration_instance_id}
        return self._handle_request(api_request).result

    def describe_server_related_global_acceleration_instances(
            self,
            resource_owner_id=None,
            server_type=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            server_id=None):
        api_request = APIRequest(
            'DescribeServerRelatedGlobalAccelerationInstances',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ServerType": server_type,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ServerId": server_id}
        return self._handle_request(api_request).result

    def describe_global_acceleration_instances(
            self,
            ip_address=None,
            resource_owner_id=None,
            bandwidth_type=None,
            resource_owner_account=None,
            service_location=None,
            owner_account=None,
            owner_id=None,
            include_reservation_data=None,
            global_acceleration_instance_id=None,
            server_id=None,
            page_number=None,
            region_id=None,
            name=None,
            page_size=None,
            status=None):
        api_request = APIRequest('DescribeGlobalAccelerationInstances',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IpAddress": ip_address,
            "ResourceOwnerId": resource_owner_id,
            "BandwidthType": bandwidth_type,
            "ResourceOwnerAccount": resource_owner_account,
            "ServiceLocation": service_location,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "IncludeReservationData": include_reservation_data,
            "GlobalAccelerationInstanceId": global_acceleration_instance_id,
            "ServerId": server_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "Name": name,
            "PageSize": page_size,
            "Status": status}
        return self._handle_request(api_request).result

    def delete_global_acceleration_instance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            global_acceleration_instance_id=None):
        api_request = APIRequest('DeleteGlobalAccelerationInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "GlobalAccelerationInstanceId": global_acceleration_instance_id}
        return self._handle_request(api_request).result

    def create_global_acceleration_instance(
            self,
            resource_owner_id=None,
            bandwidth_type=None,
            resource_owner_account=None,
            service_location=None,
            bandwidth=None,
            client_token=None,
            owner_account=None,
            description=None,
            owner_id=None,
            region_id=None,
            internet_charge_type=None,
            name=None):
        api_request = APIRequest('CreateGlobalAccelerationInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthType": bandwidth_type,
            "ResourceOwnerAccount": resource_owner_account,
            "ServiceLocation": service_location,
            "Bandwidth": bandwidth,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "RegionId": region_id,
            "InternetChargeType": internet_charge_type,
            "Name": name}
        return self._handle_request(api_request).result

    def associate_global_acceleration_instance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            backend_server_id=None,
            owner_id=None,
            global_acceleration_instance_id=None,
            backend_server_region_id=None,
            backend_server_type=None):
        api_request = APIRequest('AssociateGlobalAccelerationInstance',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "BackendServerId": backend_server_id,
            "OwnerId": owner_id,
            "GlobalAccelerationInstanceId": global_acceleration_instance_id,
            "BackendServerRegionId": backend_server_region_id,
            "BackendServerType": backend_server_type}
        return self._handle_request(api_request).result

    def describe_vswitch_attributes(
            self,
            vswitch_id=None,
            resource_owner_id=None,
            dry_run=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeVSwitchAttributes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "ResourceOwnerId": resource_owner_id,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def remove_common_bandwidth_package_ip(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            ip_instance_id=None,
            owner_id=None):
        api_request = APIRequest('RemoveCommonBandwidthPackageIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "IpInstanceId": ip_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_common_bandwidth_package_spec(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            bandwidth=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyCommonBandwidthPackageSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_common_bandwidth_package_attribute(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('ModifyCommonBandwidthPackageAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_common_bandwidth_packages(
            self,
            resource_group_id=None,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            page_size=None,
            owner_id=None,
            include_reservation_data=None,
            page_number=None):
        api_request = APIRequest('DescribeCommonBandwidthPackages', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "IncludeReservationData": include_reservation_data,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_common_bandwidth_package(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            force=None,
            owner_id=None):
        api_request = APIRequest('DeleteCommonBandwidthPackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Force": force,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_common_bandwidth_package(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            bandwidth=None,
            owner_account=None,
            isp=None,
            description=None,
            owner_id=None,
            resource_group_id=None,
            region_id=None,
            zone=None,
            internet_charge_type=None,
            name=None,
            ratio=None):
        api_request = APIRequest('CreateCommonBandwidthPackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "ISP": isp,
            "Description": description,
            "OwnerId": owner_id,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "Zone": zone,
            "InternetChargeType": internet_charge_type,
            "Name": name,
            "Ratio": ratio}
        return self._handle_request(api_request).result

    def add_common_bandwidth_package_ip(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            ip_instance_id=None,
            owner_id=None):
        api_request = APIRequest('AddCommonBandwidthPackageIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "IpInstanceId": ip_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_vpn_gateway_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            name=None,
            description=None,
            vpn_gateway_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyVpnGatewayAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_vpn_connection_attribute(
            self,
            ike_config=None,
            resource_owner_id=None,
            remote_subnet=None,
            effect_immediately=None,
            auto_config_route=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            ipsec_config=None,
            owner_id=None,
            health_check_config=None,
            local_subnet=None,
            region_id=None,
            vpn_connection_id=None,
            name=None):
        api_request = APIRequest('ModifyVpnConnectionAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IkeConfig": ike_config,
            "ResourceOwnerId": resource_owner_id,
            "RemoteSubnet": remote_subnet,
            "EffectImmediately": effect_immediately,
            "AutoConfigRoute": auto_config_route,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "IpsecConfig": ipsec_config,
            "OwnerId": owner_id,
            "HealthCheckConfig": health_check_config,
            "LocalSubnet": local_subnet,
            "RegionId": region_id,
            "VpnConnectionId": vpn_connection_id,
            "Name": name}
        return self._handle_request(api_request).result

    def modify_customer_gateway_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            name=None,
            description=None,
            owner_id=None,
            customer_gateway_id=None):
        api_request = APIRequest('ModifyCustomerGatewayAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id,
            "CustomerGatewayId": customer_gateway_id}
        return self._handle_request(api_request).result

    def download_vpn_connection_config(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            vpn_connection_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DownloadVpnConnectionConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VpnConnectionId": vpn_connection_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vpn_gateways(
            self,
            business_status=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            vpc_id=None,
            page_size=None,
            vpn_gateway_id=None,
            owner_id=None,
            page_number=None,
            status=None):
        api_request = APIRequest('DescribeVpnGateways', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BusinessStatus": business_status,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "VpcId": vpc_id,
            "PageSize": page_size,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_vpn_gateway(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            vpn_gateway_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeVpnGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vpn_connections(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            vpn_connection_id=None,
            owner_account=None,
            page_size=None,
            vpn_gateway_id=None,
            owner_id=None,
            customer_gateway_id=None,
            page_number=None):
        api_request = APIRequest('DescribeVpnConnections', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VpnConnectionId": vpn_connection_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "CustomerGatewayId": customer_gateway_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_vpn_connection(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            vpn_connection_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeVpnConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VpnConnectionId": vpn_connection_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_customer_gateways(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            customer_gateway_id=None,
            page_number=None):
        api_request = APIRequest('DescribeCustomerGateways', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "CustomerGatewayId": customer_gateway_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_customer_gateway(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            customer_gateway_id=None):
        api_request = APIRequest('DescribeCustomerGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "CustomerGatewayId": customer_gateway_id}
        return self._handle_request(api_request).result

    def delete_vpn_gateway(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            vpn_gateway_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteVpnGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_vpn_connection(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            vpn_connection_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteVpnConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "VpnConnectionId": vpn_connection_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_customer_gateway(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            owner_id=None,
            customer_gateway_id=None):
        api_request = APIRequest('DeleteCustomerGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "CustomerGatewayId": customer_gateway_id}
        return self._handle_request(api_request).result

    def create_vpn_connection(
            self,
            ike_config=None,
            resource_owner_id=None,
            remote_subnet=None,
            effect_immediately=None,
            auto_config_route=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            ipsec_config=None,
            vpn_gateway_id=None,
            owner_id=None,
            health_check_config=None,
            customer_gateway_id=None,
            local_subnet=None,
            region_id=None,
            name=None):
        api_request = APIRequest('CreateVpnConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IkeConfig": ike_config,
            "ResourceOwnerId": resource_owner_id,
            "RemoteSubnet": remote_subnet,
            "EffectImmediately": effect_immediately,
            "AutoConfigRoute": auto_config_route,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "IpsecConfig": ipsec_config,
            "VpnGatewayId": vpn_gateway_id,
            "OwnerId": owner_id,
            "HealthCheckConfig": health_check_config,
            "CustomerGatewayId": customer_gateway_id,
            "LocalSubnet": local_subnet,
            "RegionId": region_id,
            "Name": name}
        return self._handle_request(api_request).result

    def create_customer_gateway(
            self,
            ip_address=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            name=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('CreateCustomerGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IpAddress": ip_address,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_bgp_group_attribute(
            self,
            auth_key=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            bgp_group_id=None,
            description=None,
            owner_id=None,
            peer_asn=None,
            is_fake_asn=None,
            region_id=None,
            name=None):
        api_request = APIRequest('ModifyBgpGroupAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AuthKey": auth_key,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "BgpGroupId": bgp_group_id,
            "Description": description,
            "OwnerId": owner_id,
            "PeerAsn": peer_asn,
            "IsFakeAsn": is_fake_asn,
            "RegionId": region_id,
            "Name": name}
        return self._handle_request(api_request).result

    def describe_bgp_peers(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            router_id=None,
            owner_account=None,
            page_size=None,
            bgp_group_id=None,
            bgp_peer_id=None,
            is_default=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeBgpPeers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "RouterId": router_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "BgpGroupId": bgp_group_id,
            "BgpPeerId": bgp_peer_id,
            "IsDefault": is_default,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_bgp_groups(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            router_id=None,
            owner_account=None,
            page_size=None,
            bgp_group_id=None,
            is_default=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeBgpGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "RouterId": router_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "BgpGroupId": bgp_group_id,
            "IsDefault": is_default,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_bgp_peer(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            bgp_peer_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteBgpPeer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "BgpPeerId": bgp_peer_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_bgp_network(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            router_id=None,
            owner_account=None,
            owner_id=None,
            dst_cidr_block=None):
        api_request = APIRequest('DeleteBgpNetwork', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "RouterId": router_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "DstCidrBlock": dst_cidr_block}
        return self._handle_request(api_request).result

    def delete_bgp_group(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            bgp_group_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteBgpGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "BgpGroupId": bgp_group_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_bgp_peer(
            self,
            resource_owner_id=None,
            enable_bfd=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            bgp_group_id=None,
            owner_id=None,
            peer_ip_address=None):
        api_request = APIRequest('CreateBgpPeer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "EnableBfd": enable_bfd,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "BgpGroupId": bgp_group_id,
            "OwnerId": owner_id,
            "PeerIpAddress": peer_ip_address}
        return self._handle_request(api_request).result

    def create_bgp_group(
            self,
            auth_key=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            description=None,
            owner_id=None,
            peer_asn=None,
            is_fake_asn=None,
            region_id=None,
            router_id=None,
            name=None):
        api_request = APIRequest('CreateBgpGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AuthKey": auth_key,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "PeerAsn": peer_asn,
            "IsFakeAsn": is_fake_asn,
            "RegionId": region_id,
            "RouterId": router_id,
            "Name": name}
        return self._handle_request(api_request).result

    def add_bgp_network(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            router_id=None,
            vpc_id=None,
            owner_account=None,
            owner_id=None,
            dst_cidr_block=None):
        api_request = APIRequest('AddBgpNetwork', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "RouterId": router_id,
            "VpcId": vpc_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "DstCidrBlock": dst_cidr_block}
        return self._handle_request(api_request).result

    def enable_vpc_classic_link(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            vpc_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('EnableVpcClassicLink', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "VpcId": vpc_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def disable_vpc_classic_link(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            vpc_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DisableVpcClassicLink', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "VpcId": vpc_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vpc_attribute(
            self,
            resource_owner_id=None,
            dry_run=None,
            resource_owner_account=None,
            region_id=None,
            vpc_id=None,
            owner_account=None,
            is_default=None,
            owner_id=None):
        api_request = APIRequest('DescribeVpcAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "OwnerAccount": owner_account,
            "IsDefault": is_default,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def unassociate_physical_connection_from_virtual_border_router(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            physical_connection_id=None,
            owner_account=None,
            vbr_id=None,
            owner_id=None):
        api_request = APIRequest(
            'UnassociatePhysicalConnectionFromVirtualBorderRouter',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "PhysicalConnectionId": physical_connection_id,
            "OwnerAccount": owner_account,
            "VbrId": vbr_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def associate_physical_connection_to_virtual_border_router(
            self,
            resource_owner_id=None,
            circuit_code=None,
            vlan_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            vbr_id=None,
            owner_id=None,
            peer_gateway_ip=None,
            peering_subnet_mask=None,
            region_id=None,
            physical_connection_id=None,
            local_gateway_ip=None):
        api_request = APIRequest(
            'AssociatePhysicalConnectionToVirtualBorderRouter',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "CircuitCode": circuit_code,
            "VlanId": vlan_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "VbrId": vbr_id,
            "OwnerId": owner_id,
            "PeerGatewayIp": peer_gateway_ip,
            "PeeringSubnetMask": peering_subnet_mask,
            "RegionId": region_id,
            "PhysicalConnectionId": physical_connection_id,
            "LocalGatewayIp": local_gateway_ip}
        return self._handle_request(api_request).result

    def modify_snat_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            snat_entry_name=None,
            snat_table_id=None,
            snat_entry_id=None,
            owner_id=None,
            snat_ip=None):
        api_request = APIRequest('ModifySnatEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SnatEntryName": snat_entry_name,
            "SnatTableId": snat_table_id,
            "SnatEntryId": snat_entry_id,
            "OwnerId": owner_id,
            "SnatIp": snat_ip}
        return self._handle_request(api_request).result

    def modify_nat_gateway_spec(
            self,
            resource_owner_id=None,
            auto_pay=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            nat_gateway_id=None,
            owner_id=None,
            spec=None):
        api_request = APIRequest('ModifyNatGatewaySpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "NatGatewayId": nat_gateway_id,
            "OwnerId": owner_id,
            "Spec": spec}
        return self._handle_request(api_request).result

    def modify_nat_gateway_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            description=None,
            nat_gateway_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyNatGatewayAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "NatGatewayId": nat_gateway_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_bandwidth_package_attribute(
            self,
            resource_owner_id=None,
            bandwidth_package_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('ModifyBandwidthPackageAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_snat_table_entries(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            source_cidr=None,
            snat_table_id=None,
            owner_id=None,
            snat_ip=None,
            page_number=None,
            source_vswitch_id=None,
            region_id=None,
            snat_entry_name=None,
            page_size=None,
            snat_entry_id=None):
        api_request = APIRequest('DescribeSnatTableEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SourceCIDR": source_cidr,
            "SnatTableId": snat_table_id,
            "OwnerId": owner_id,
            "SnatIp": snat_ip,
            "PageNumber": page_number,
            "SourceVSwitchId": source_vswitch_id,
            "RegionId": region_id,
            "SnatEntryName": snat_entry_name,
            "PageSize": page_size,
            "SnatEntryId": snat_entry_id}
        return self._handle_request(api_request).result

    def delete_snat_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            snat_table_id=None,
            snat_entry_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteSnatEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SnatTableId": snat_table_id,
            "SnatEntryId": snat_entry_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_snat_entry(
            self,
            resource_owner_id=None,
            source_vswitch_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            snat_entry_name=None,
            source_cidr=None,
            snat_table_id=None,
            owner_id=None,
            snat_ip=None):
        api_request = APIRequest('CreateSnatEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceVSwitchId": source_vswitch_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SnatEntryName": snat_entry_name,
            "SourceCIDR": source_cidr,
            "SnatTableId": snat_table_id,
            "OwnerId": owner_id,
            "SnatIp": snat_ip}
        return self._handle_request(api_request).result

    def create_bandwidth_package(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            bandwidth=None,
            owner_account=None,
            isp=None,
            description=None,
            owner_id=None,
            region_id=None,
            zone=None,
            internet_charge_type=None,
            name=None,
            nat_gateway_id=None,
            ip_count=None):
        api_request = APIRequest('CreateBandwidthPackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "ISP": isp,
            "Description": description,
            "OwnerId": owner_id,
            "RegionId": region_id,
            "Zone": zone,
            "InternetChargeType": internet_charge_type,
            "Name": name,
            "NatGatewayId": nat_gateway_id,
            "IpCount": ip_count}
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

    def unassociate_eip_address(
            self,
            private_ip_address=None,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            instance_type=None,
            force=None,
            allocation_id=None,
            owner_id=None):
        api_request = APIRequest('UnassociateEipAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PrivateIpAddress": private_ip_address,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "InstanceType": instance_type,
            "Force": force,
            "AllocationId": allocation_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def terminate_virtual_border_router(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            vbr_id=None,
            owner_id=None):
        api_request = APIRequest('TerminateVirtualBorderRouter', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
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
            owner_id=None):
        api_request = APIRequest('TerminatePhysicalConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "PhysicalConnectionId": physical_connection_id,
            "OwnerAccount": owner_account,
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

    def recover_virtual_border_router(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            vbr_id=None,
            owner_id=None):
        api_request = APIRequest('RecoverVirtualBorderRouter', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "VbrId": vbr_id,
            "OwnerId": owner_id}
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
            owner_id=None,
            ipv6_cidr_block=None):
        api_request = APIRequest('ModifyVSwitchAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "VSwitchName": vswitch_name,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "Ipv6CidrBlock": ipv6_cidr_block}
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
            enable_ipv6=None,
            description=None,
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
            "EnableIPv6": enable_ipv6,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_virtual_border_router_attribute(
            self,
            resource_owner_id=None,
            circuit_code=None,
            associated_physical_connections=None,
            vlan_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            description=None,
            vbr_id=None,
            owner_id=None,
            min_rx_interval=None,
            peer_gateway_ip=None,
            detect_multiplier=None,
            peering_subnet_mask=None,
            region_id=None,
            name=None,
            local_gateway_ip=None,
            min_tx_interval=None):
        api_request = APIRequest('ModifyVirtualBorderRouterAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "CircuitCode": circuit_code,
            "AssociatedPhysicalConnections": associated_physical_connections,
            "VlanId": vlan_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Description": description,
            "VbrId": vbr_id,
            "OwnerId": owner_id,
            "MinRxInterval": min_rx_interval,
            "PeerGatewayIp": peer_gateway_ip,
            "DetectMultiplier": detect_multiplier,
            "PeeringSubnetMask": peering_subnet_mask,
            "RegionId": region_id,
            "Name": name,
            "LocalGatewayIp": local_gateway_ip,
            "MinTxInterval": min_tx_interval}
        return self._handle_request(api_request).result

    def modify_router_interface_spec(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
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
            "RouterInterfaceId": router_interface_id,
            "OwnerId": owner_id,
            "Spec": spec}
        return self._handle_request(api_request).result

    def modify_router_interface_attribute(
            self,
            opposite_router_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            delete_health_check_ip=None,
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
            "DeleteHealthCheckIp": delete_health_check_ip,
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
            name=None):
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
            "Name": name}
        return self._handle_request(api_request).result

    def modify_ha_vip_attribute(
            self,
            ha_vip_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            name=None,
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
            "Name": name,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_forward_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            ip_protocol=None,
            forward_entry_name=None,
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
            "ForwardEntryName": forward_entry_name,
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

    def modify_eip_address_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            bandwidth=None,
            region_id=None,
            owner_account=None,
            name=None,
            description=None,
            allocation_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyEipAddressAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "AllocationId": allocation_id,
            "OwnerId": owner_id}
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

    def enable_physical_connection(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            physical_connection_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('EnablePhysicalConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "PhysicalConnectionId": physical_connection_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_zones(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeZones', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vswitches(
            self,
            resource_owner_id=None,
            dry_run=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            page_number=None,
            vswitch_id=None,
            resource_group_id=None,
            region_id=None,
            vpc_id=None,
            vswitch_name=None,
            page_size=None,
            zone_id=None,
            list_of_tag=None,
            is_default=None,
            route_table_id=None):
        api_request = APIRequest('DescribeVSwitches', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "VSwitchId": vswitch_id,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "VSwitchName": vswitch_name,
            "PageSize": page_size,
            "ZoneId": zone_id,
            "Tag": list_of_tag,
            "IsDefault": is_default,
            "RouteTableId": route_table_id}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
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
            dry_run=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            page_number=None,
            vpc_name=None,
            resource_group_id=None,
            region_id=None,
            vpc_id=None,
            page_size=None,
            list_of_tag=None,
            is_default=None):
        api_request = APIRequest('DescribeVpcs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "VpcName": vpc_name,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "PageSize": page_size,
            "Tag": list_of_tag,
            "IsDefault": is_default}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
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

    def describe_route_tables(
            self,
            resource_owner_id=None,
            vrouter_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            type_=None,
            page_number=None,
            router_type=None,
            resource_group_id=None,
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
            "Type": type_,
            "PageNumber": page_number,
            "RouterType": router_type,
            "ResourceGroupId": resource_group_id,
            "RouteTableName": route_table_name,
            "RegionId": region_id,
            "RouterId": router_id,
            "PageSize": page_size,
            "RouteTableId": route_table_id}
        return self._handle_request(api_request).result

    def describe_router_interfaces(
            self,
            list_of_filter_=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            page_size=None,
            owner_id=None,
            include_reservation_data=None,
            page_number=None):
        api_request = APIRequest('DescribeRouterInterfaces', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Filter": list_of_filter_,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "IncludeReservationData": include_reservation_data,
            "PageNumber": page_number}
        repeat_info = {"Filter": ('Filter', 'list', 'dict', [('Value', 'list', 'str', None),
                                                             ('Key', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_regions(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            accept_language=None,
            owner_id=None,
            product_type=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AcceptLanguage": accept_language,
            "OwnerId": owner_id,
            "ProductType": product_type}
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
            owner_id=None,
            include_reservation_data=None,
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
            "OwnerId": owner_id,
            "IncludeReservationData": include_reservation_data,
            "PageNumber": page_number}
        repeat_info = {"Filter": ('Filter', 'list', 'dict', [('Value', 'list', 'str', None),
                                                             ('Key', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_nat_gateways(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            spec=None,
            page_number=None,
            region_id=None,
            vpc_id=None,
            name=None,
            page_size=None,
            nat_gateway_id=None,
            instance_charge_type=None):
        api_request = APIRequest('DescribeNatGateways', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Spec": spec,
            "PageNumber": page_number,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "Name": name,
            "PageSize": page_size,
            "NatGatewayId": nat_gateway_id,
            "InstanceChargeType": instance_charge_type}
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

    def describe_forward_table_entries(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            ip_protocol=None,
            forward_entry_name=None,
            owner_account=None,
            forward_table_id=None,
            owner_id=None,
            internal_ip=None,
            page_number=None,
            region_id=None,
            forward_entry_id=None,
            internal_port=None,
            page_size=None,
            external_ip=None,
            external_port=None):
        api_request = APIRequest('DescribeForwardTableEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "ForwardEntryName": forward_entry_name,
            "OwnerAccount": owner_account,
            "ForwardTableId": forward_table_id,
            "OwnerId": owner_id,
            "InternalIp": internal_ip,
            "PageNumber": page_number,
            "RegionId": region_id,
            "ForwardEntryId": forward_entry_id,
            "InternalPort": internal_port,
            "PageSize": page_size,
            "ExternalIp": external_ip,
            "ExternalPort": external_port}
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
            include_reservation_data=None,
            eip_address=None,
            page_number=None,
            resource_group_id=None,
            lock_reason=None,
            filter1_key=None,
            region_id=None,
            associated_instance_type=None,
            page_size=None,
            list_of_tag=None,
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
            "IncludeReservationData": include_reservation_data,
            "EipAddress": eip_address,
            "PageNumber": page_number,
            "ResourceGroupId": resource_group_id,
            "LockReason": lock_reason,
            "Filter.1.Key": filter1_key,
            "RegionId": region_id,
            "AssociatedInstanceType": associated_instance_type,
            "PageSize": page_size,
            "Tag": list_of_tag,
            "ChargeType": charge_type,
            "AssociatedInstanceId": associated_instance_id,
            "Status": status}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
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

    def describe_access_points(
            self,
            list_of_filter_=None,
            resource_owner_id=None,
            host_operator=None,
            resource_owner_account=None,
            region_id=None,
            name=None,
            page_size=None,
            owner_id=None,
            type_=None,
            page_number=None):
        api_request = APIRequest('DescribeAccessPoints', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Filter": list_of_filter_,
            "ResourceOwnerId": resource_owner_id,
            "HostOperator": host_operator,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "Name": name,
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

    def delete_virtual_border_router(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            vbr_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteVirtualBorderRouter', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "VbrId": vbr_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_router_interface(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            router_interface_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteRouterInterface', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "RouterInterfaceId": router_interface_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_route_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            route_entry_id=None,
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
            "RouteEntryId": route_entry_id,
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

    def delete_physical_connection(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            physical_connection_id=None,
            owner_account=None,
            user_cidr=None,
            owner_id=None):
        api_request = APIRequest('DeletePhysicalConnection', 'GET', 'http', 'RPC', 'query')
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

    def delete_nat_gateway(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            force=None,
            nat_gateway_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteNatGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Force": force,
            "NatGatewayId": nat_gateway_id,
            "OwnerId": owner_id}
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
            force=None,
            owner_id=None):
        api_request = APIRequest('DeleteBandwidthPackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthPackageId": bandwidth_package_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Force": force,
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

    def create_vswitch(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            description=None,
            owner_id=None,
            ipv6_cidr_block=None,
            region_id=None,
            vpc_id=None,
            vswitch_name=None,
            cidr_block=None,
            zone_id=None):
        api_request = APIRequest('CreateVSwitch', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "Ipv6CidrBlock": ipv6_cidr_block,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "VSwitchName": vswitch_name,
            "CidrBlock": cidr_block,
            "ZoneId": zone_id}
        return self._handle_request(api_request).result

    def create_vpc(
            self,
            resource_owner_id=None,
            dry_run=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            enable_ipv6=None,
            description=None,
            owner_id=None,
            ipv6_cidr_block=None,
            vpc_name=None,
            resource_group_id=None,
            region_id=None,
            cidr_block=None,
            user_cidr=None):
        api_request = APIRequest('CreateVpc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DryRun": dry_run,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "EnableIpv6": enable_ipv6,
            "Description": description,
            "OwnerId": owner_id,
            "Ipv6CidrBlock": ipv6_cidr_block,
            "VpcName": vpc_name,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "CidrBlock": cidr_block,
            "UserCidr": user_cidr}
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
            "VbrOwnerId": vbr_owner_id}
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

    def create_route_entry(
            self,
            resource_owner_id=None,
            route_entry_name=None,
            resource_owner_account=None,
            client_token=None,
            destination_cidr_block=None,
            owner_account=None,
            owner_id=None,
            private_ip_address=None,
            region_id=None,
            next_hop_id=None,
            next_hop_type=None,
            list_of_next_hop_list=None,
            route_table_id=None):
        api_request = APIRequest('CreateRouteEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RouteEntryName": route_entry_name,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "DestinationCidrBlock": destination_cidr_block,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PrivateIpAddress": private_ip_address,
            "RegionId": region_id,
            "NextHopId": next_hop_id,
            "NextHopType": next_hop_type,
            "NextHopList": list_of_next_hop_list,
            "RouteTableId": route_table_id}
        repeat_info = {"NextHopList": ('NextHopList', 'list', 'dict', [('Weight', 'str', None, None),
                                                                       ('NextHopId', 'str', None, None),
                                                                       ('NextHopType', 'str', None, None),
                                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
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
            name=None):
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
            "Name": name}
        return self._handle_request(api_request).result

    def create_nat_gateway(
            self,
            resource_owner_id=None,
            auto_pay=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            description=None,
            owner_id=None,
            spec=None,
            duration=None,
            region_id=None,
            vpc_id=None,
            name=None,
            list_of_bandwidth_package=None,
            instance_charge_type=None,
            pricing_cycle=None):
        api_request = APIRequest('CreateNatGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "Spec": spec,
            "Duration": duration,
            "RegionId": region_id,
            "VpcId": vpc_id,
            "Name": name,
            "BandwidthPackage": list_of_bandwidth_package,
            "InstanceChargeType": instance_charge_type,
            "PricingCycle": pricing_cycle}
        repeat_info = {"BandwidthPackage": ('BandwidthPackage',
                                            'list',
                                            'dict',
                                            [('Bandwidth',
                                              'str',
                                              None,
                                              None),
                                             ('Zone',
                                              'str',
                                              None,
                                              None),
                                                ('InternetChargeType',
                                                 'str',
                                                 None,
                                                 None),
                                                ('ISP',
                                                 'str',
                                                 None,
                                                 None),
                                                ('IpCount',
                                                 'str',
                                                 None,
                                                 None),
                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
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
            name=None,
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
            "Name": name,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_forward_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            ip_protocol=None,
            forward_entry_name=None,
            owner_account=None,
            forward_table_id=None,
            owner_id=None,
            internal_ip=None,
            region_id=None,
            internal_port=None,
            external_ip=None,
            external_port=None):
        api_request = APIRequest('CreateForwardEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "ForwardEntryName": forward_entry_name,
            "OwnerAccount": owner_account,
            "ForwardTableId": forward_table_id,
            "OwnerId": owner_id,
            "InternalIp": internal_ip,
            "RegionId": region_id,
            "InternalPort": internal_port,
            "ExternalIp": external_ip,
            "ExternalPort": external_port}
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

    def cancel_physical_connection(
            self,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            client_token=None,
            physical_connection_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CancelPhysicalConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "PhysicalConnectionId": physical_connection_id,
            "OwnerAccount": owner_account,
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

    def associate_eip_address(
            self,
            private_ip_address=None,
            mode=None,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            instance_region_id=None,
            owner_account=None,
            instance_type=None,
            allocation_id=None,
            owner_id=None):
        api_request = APIRequest('AssociateEipAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PrivateIpAddress": private_ip_address,
            "Mode": mode,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "InstanceRegionId": instance_region_id,
            "OwnerAccount": owner_account,
            "InstanceType": instance_type,
            "AllocationId": allocation_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def allocate_eip_address(
            self,
            resource_owner_id=None,
            period=None,
            auto_pay=None,
            resource_owner_account=None,
            bandwidth=None,
            client_token=None,
            isp=None,
            owner_account=None,
            owner_id=None,
            activity_id=None,
            resource_group_id=None,
            region_id=None,
            internet_charge_type=None,
            netmode=None,
            pricing_cycle=None,
            instance_charge_type=None):
        api_request = APIRequest('AllocateEipAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "ClientToken": client_token,
            "ISP": isp,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ActivityId": activity_id,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "InternetChargeType": internet_charge_type,
            "Netmode": netmode,
            "PricingCycle": pricing_cycle,
            "InstanceChargeType": instance_charge_type}
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
