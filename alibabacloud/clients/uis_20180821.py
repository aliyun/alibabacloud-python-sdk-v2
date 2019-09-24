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


class UisClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Uis'
        self.api_version = '2018-08-21'
        self.location_service_code = 'uis'
        self.location_endpoint_type = 'openAPI'

    def describe_regions(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_white_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            uis_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "UisId": uis_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_white_list(
            self,
            resource_owner_id=None,
            modify_mode=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            uis_id=None,
            whitelist=None,
            owner_id=None):
        api_request = APIRequest('ModifyWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ModifyMode": modify_mode,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "UisId": uis_id,
            "Whitelist": whitelist,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_sub_connection(
            self,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            owner_account=None,
            ip=None,
            name=None,
            description=None,
            owner_id=None,
            gre_config=None):
        api_request = APIRequest('CreateSubConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Ip": ip,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id,
            "GreConfig": gre_config}
        return self._handle_request(api_request).result

    def delete_sub_connection(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            uis_sub_connection_id=None):
        api_request = APIRequest('DeleteSubConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "UisSubConnectionId": uis_sub_connection_id}
        return self._handle_request(api_request).result

    def modify_sub_connection(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            description=None,
            owner_id=None,
            uis_sub_connection_id=None,
            gre_config=None):
        api_request = APIRequest('ModifySubConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id,
            "UisSubConnectionId": uis_sub_connection_id,
            "GreConfig": gre_config}
        return self._handle_request(api_request).result

    def describe_sub_connections(
            self,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            owner_account=None,
            ip=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeSubConnections', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "IP": ip,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_sub_connection(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            uis_sub_connection_id=None):
        api_request = APIRequest('DescribeSubConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "UisSubConnectionId": uis_sub_connection_id}
        return self._handle_request(api_request).result

    def describe_high_priority_ips(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            uis_id=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeHighPriorityIps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "UisId": uis_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_uise_node_status(
            self,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            owner_account=None,
            ip=None,
            owner_id=None):
        api_request = APIRequest('DescribeUiseNodeStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Ip": ip,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_dnat_entry(
            self,
            destination_ip=None,
            destination_port=None,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            name=None,
            original_port=None,
            owner_id=None,
            original_ip=None):
        api_request = APIRequest('CreateDnatEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DestinationIp": destination_ip,
            "DestinationPort": destination_port,
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "Name": name,
            "OriginalPort": original_port,
            "OwnerId": owner_id,
            "OriginalIp": original_ip}
        return self._handle_request(api_request).result

    def delete_dnat_entry(
            self,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            owner_account=None,
            uis_dnat_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteDnatEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "UisDnatId": uis_dnat_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_dnat_entries(
            self,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            uis_dnat_id=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeDnatEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "UisDnatId": uis_dnat_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_dnat_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            original_port=None,
            owner_id=None,
            original_ip=None,
            destination_ip=None,
            destination_port=None,
            uis_node_id=None,
            region_id=None,
            uis_dnat_id=None,
            name=None):
        api_request = APIRequest('ModifyDnatEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "OriginalPort": original_port,
            "OwnerId": owner_id,
            "OriginalIp": original_ip,
            "DestinationIp": destination_ip,
            "DestinationPort": destination_port,
            "UisNodeId": uis_node_id,
            "RegionId": region_id,
            "UisDnatId": uis_dnat_id,
            "Name": name}
        return self._handle_request(api_request).result

    def create_uis_network_interface(
            self,
            vswitch_id=None,
            ip_address=None,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            owner_account=None,
            security_group_id=None,
            name=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('CreateUisNetworkInterface', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VswitchId": vswitch_id,
            "IpAddress": ip_address,
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SecurityGroupId": security_group_id,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_uis_network_interface(
            self,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            owner_account=None,
            uis_eni_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteUisNetworkInterface', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "UisEniId": uis_eni_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_uis_network_interfaces(
            self,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            uis_eni_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeUisNetworkInterfaces', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "UisEniId": uis_eni_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_areas(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeAreas', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_dropped_ip_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            uis_id=None,
            chart_date=None,
            owner_id=None):
        api_request = APIRequest('GetDroppedIpList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "UisId": uis_id,
            "ChartDate": chart_date,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_uis_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            uis_id=None,
            name=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('ModifyUisAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "UisId": uis_id,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_uis(
            self,
            resource_owner_id=None,
            bandwidth_type=None,
            access_type=None,
            auto_pay=None,
            connection_count=None,
            resource_owner_account=None,
            client_token=None,
            bandwidth=None,
            owner_account=None,
            description=None,
            owner_id=None,
            service_region=None,
            duration=None,
            region_id=None,
            internet_charge_type=None,
            name=None,
            uis_protocol=None,
            instance_charge_type=None,
            pricing_cycle=None,
            connection_bandwidth=None):
        api_request = APIRequest('CreateUis', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BandwidthType": bandwidth_type,
            "AccessType": access_type,
            "AutoPay": auto_pay,
            "ConnectionCount": connection_count,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "ServiceRegion": service_region,
            "Duration": duration,
            "RegionId": region_id,
            "InternetChargeType": internet_charge_type,
            "Name": name,
            "UisProtocol": uis_protocol,
            "InstanceChargeType": instance_charge_type,
            "PricingCycle": pricing_cycle,
            "ConnectionBandwidth": connection_bandwidth}
        return self._handle_request(api_request).result

    def delete_uis(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            uis_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteUis', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "UisId": uis_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_uis_node(
            self,
            resource_owner_id=None,
            uis_node_bandwidth=None,
            resource_owner_account=None,
            region_id=None,
            uis_node_area_id=None,
            owner_account=None,
            uis_id=None,
            name=None,
            description=None,
            ip_addrs_num=None,
            owner_id=None):
        api_request = APIRequest('CreateUisNode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeBandwidth": uis_node_bandwidth,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "UisNodeAreaId": uis_node_area_id,
            "OwnerAccount": owner_account,
            "UisId": uis_id,
            "Name": name,
            "Description": description,
            "IpAddrsNum": ip_addrs_num,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_uis_node(
            self,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            uis_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteUisNode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "UisId": uis_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_uis_node_attribute(
            self,
            resource_owner_id=None,
            uis_node_bandwidth=None,
            uis_node_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            uis_id=None,
            name=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('ModifyUisNodeAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeBandwidth": uis_node_bandwidth,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "UisId": uis_id,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_uis_nodes(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            owner_id=None,
            page_number=None,
            uis_node_id=None,
            region_id=None,
            uis_id=None,
            name=None,
            page_size=None,
            status=None):
        api_request = APIRequest('DescribeUisNodes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "UisNodeId": uis_node_id,
            "RegionId": region_id,
            "UisId": uis_id,
            "Name": name,
            "PageSize": page_size,
            "Status": status}
        return self._handle_request(api_request).result

    def create_uis_connection(
            self,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            description=None,
            uis_protocol=None,
            ssl_config=None,
            owner_id=None,
            gre_config=None):
        api_request = APIRequest('CreateUisConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "UisProtocol": uis_protocol,
            "SslConfig": ssl_config,
            "OwnerId": owner_id,
            "GreConfig": gre_config}
        return self._handle_request(api_request).result

    def delete_uis_connection(
            self,
            resource_owner_id=None,
            uis_connection_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteUisConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisConnectionId": uis_connection_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_uis_connection_attribute(
            self,
            resource_owner_id=None,
            uis_connection_id=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            ssl_config=None,
            owner_id=None,
            uis_node_id=None,
            region_id=None,
            name=None,
            uis_protocol=None,
            gre_config=None):
        api_request = APIRequest('ModifyUisConnectionAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisConnectionId": uis_connection_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "SslConfig": ssl_config,
            "OwnerId": owner_id,
            "UisNodeId": uis_node_id,
            "RegionId": region_id,
            "Name": name,
            "UisProtocol": uis_protocol,
            "GreConfig": gre_config}
        return self._handle_request(api_request).result

    def describe_uis_connections(
            self,
            resource_owner_id=None,
            uis_node_id=None,
            uis_connection_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeUisConnections', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "UisConnectionId": uis_connection_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def add_high_priority_ip(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            high_priority_ip=None,
            uis_id=None,
            owner_id=None):
        api_request = APIRequest('AddHighPriorityIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "HighPriorityIp": high_priority_ip,
            "UisId": uis_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_high_priority_ip(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            high_priority_ip=None,
            uis_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteHighPriorityIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "HighPriorityIp": high_priority_ip,
            "UisId": uis_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_high_priority_ip(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            high_priority_ip=None,
            uis_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyHighPriorityIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "HighPriorityIp": high_priority_ip,
            "UisId": uis_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_high_priority_ip(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            high_priority_ip=None,
            uis_id=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeHighPriorityIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "HighPriorityIp": high_priority_ip,
            "UisId": uis_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def add_uis_node_ip(
            self,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            ip_addrs_num=None,
            owner_id=None):
        api_request = APIRequest('AddUisNodeIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "IpAddrsNum": ip_addrs_num,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_uis_node_ip(
            self,
            resource_owner_id=None,
            uis_node_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            uis_node_ip_address=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteUisNodeIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UisNodeId": uis_node_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "UisNodeIpAddress": uis_node_ip_address,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_uises(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            uis_id=None,
            name=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeUises', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "UisId": uis_id,
            "Name": name,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result
