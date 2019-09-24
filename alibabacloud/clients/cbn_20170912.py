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


class CbnClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Cbn'
        self.api_version = '2017-09-12'
        self.location_service_code = 'cbn'
        self.location_endpoint_type = 'openAPI'

    def modify_flow_log_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            cen_id=None,
            owner_account=None,
            description=None,
            owner_id=None,
            flow_log_id=None,
            flow_log_name=None):
        api_request = APIRequest('ModifyFlowLogAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id,
            "FlowLogName": flow_log_name}
        return self._handle_request(api_request).result

    def describe_flowlogs(
            self,
            resource_owner_id=None,
            project_name=None,
            log_store_name=None,
            resource_owner_account=None,
            client_token=None,
            cen_id=None,
            owner_account=None,
            description=None,
            owner_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            flow_log_id=None,
            flow_log_name=None,
            status=None):
        api_request = APIRequest('DescribeFlowlogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ProjectName": project_name,
            "LogStoreName": log_store_name,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "FlowLogId": flow_log_id,
            "FlowLogName": flow_log_name,
            "Status": status}
        return self._handle_request(api_request).result

    def delete_flowlog(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            cen_id=None,
            owner_account=None,
            owner_id=None,
            flow_log_id=None):
        api_request = APIRequest('DeleteFlowlog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id}
        return self._handle_request(api_request).result

    def deactive_flow_log(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            cen_id=None,
            owner_account=None,
            owner_id=None,
            flow_log_id=None):
        api_request = APIRequest('DeactiveFlowLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id}
        return self._handle_request(api_request).result

    def create_flowlog(
            self,
            resource_owner_id=None,
            project_name=None,
            log_store_name=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            cen_id=None,
            owner_account=None,
            description=None,
            owner_id=None,
            flow_log_name=None):
        api_request = APIRequest('CreateFlowlog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ProjectName": project_name,
            "LogStoreName": log_store_name,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "FlowLogName": flow_log_name}
        return self._handle_request(api_request).result

    def active_flow_log(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            cen_id=None,
            owner_account=None,
            owner_id=None,
            flow_log_id=None):
        api_request = APIRequest('ActiveFlowLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id}
        return self._handle_request(api_request).result

    def create_cen_route_map(
            self,
            list_of_route_types=None,
            resource_owner_id=None,
            cidr_match_mode=None,
            community_match_mode=None,
            cen_id=None,
            map_result=None,
            as_path_length=None,
            description=None,
            source_instance_ids_reverse_match=None,
            next_priority=None,
            list_of_destination_cidr_blocks=None,
            list_of_destination_route_table_ids=None,
            list_of_source_instance_ids=None,
            list_of_source_region_ids=None,
            transmit_direction=None,
            list_of_destination_instance_ids=None,
            list_of_match_asns=None,
            resource_owner_account=None,
            owner_account=None,
            preference=None,
            destination_instance_ids_reverse_match=None,
            owner_id=None,
            priority=None,
            list_of_destination_child_instance_types=None,
            list_of_source_route_table_ids=None,
            as_path_match_mode=None,
            list_of_source_child_instance_types=None,
            list_of_match_community_set=None,
            community_operate_mode=None,
            cen_region_id=None,
            list_of_operate_community_set=None):
        api_request = APIRequest('CreateCenRouteMap', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RouteTypes": list_of_route_types,
            "ResourceOwnerId": resource_owner_id,
            "CidrMatchMode": cidr_match_mode,
            "CommunityMatchMode": community_match_mode,
            "CenId": cen_id,
            "MapResult": map_result,
            "AsPathLength": as_path_length,
            "Description": description,
            "SourceInstanceIdsReverseMatch": source_instance_ids_reverse_match,
            "NextPriority": next_priority,
            "DestinationCidrBlocks": list_of_destination_cidr_blocks,
            "DestinationRouteTableIds": list_of_destination_route_table_ids,
            "SourceInstanceIds": list_of_source_instance_ids,
            "SourceRegionIds": list_of_source_region_ids,
            "TransmitDirection": transmit_direction,
            "DestinationInstanceIds": list_of_destination_instance_ids,
            "MatchAsns": list_of_match_asns,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Preference": preference,
            "DestinationInstanceIdsReverseMatch": destination_instance_ids_reverse_match,
            "OwnerId": owner_id,
            "Priority": priority,
            "DestinationChildInstanceTypes": list_of_destination_child_instance_types,
            "SourceRouteTableIds": list_of_source_route_table_ids,
            "AsPathMatchMode": as_path_match_mode,
            "SourceChildInstanceTypes": list_of_source_child_instance_types,
            "MatchCommunitySet": list_of_match_community_set,
            "CommunityOperateMode": community_operate_mode,
            "CenRegionId": cen_region_id,
            "OperateCommunitySet": list_of_operate_community_set}
        repeat_info = {"RouteTypes": ('RouteTypes', 'list', 'str', None),
                       "DestinationCidrBlocks": ('DestinationCidrBlocks', 'list', 'str', None),
                       "DestinationRouteTableIds": ('DestinationRouteTableIds', 'list', 'str', None),
                       "SourceInstanceIds": ('SourceInstanceIds', 'list', 'str', None),
                       "SourceRegionIds": ('SourceRegionIds', 'list', 'str', None),
                       "DestinationInstanceIds": ('DestinationInstanceIds', 'list', 'str', None),
                       "MatchAsns": ('MatchAsns', 'list', 'str', None),
                       "DestinationChildInstanceTypes": ('DestinationChildInstanceTypes', 'list', 'str', None),
                       "SourceRouteTableIds": ('SourceRouteTableIds', 'list', 'str', None),
                       "SourceChildInstanceTypes": ('SourceChildInstanceTypes', 'list', 'str', None),
                       "MatchCommunitySet": ('MatchCommunitySet', 'list', 'str', None),
                       "OperateCommunitySet": ('OperateCommunitySet', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_cen_route_map(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            cen_region_id=None,
            route_map_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteCenRouteMap', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "CenRegionId": cen_region_id,
            "RouteMapId": route_map_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cen_route_maps(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            cen_region_id=None,
            page_size=None,
            route_map_id=None,
            owner_id=None,
            page_number=None,
            transmit_direction=None):
        api_request = APIRequest('DescribeCenRouteMaps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "CenRegionId": cen_region_id,
            "PageSize": page_size,
            "RouteMapId": route_map_id,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "TransmitDirection": transmit_direction}
        return self._handle_request(api_request).result

    def modify_cen_route_map(
            self,
            list_of_route_types=None,
            resource_owner_id=None,
            cidr_match_mode=None,
            community_match_mode=None,
            cen_id=None,
            map_result=None,
            as_path_length=None,
            description=None,
            source_instance_ids_reverse_match=None,
            next_priority=None,
            list_of_destination_cidr_blocks=None,
            list_of_destination_route_table_ids=None,
            list_of_source_instance_ids=None,
            list_of_source_region_ids=None,
            list_of_destination_instance_ids=None,
            list_of_match_asns=None,
            resource_owner_account=None,
            owner_account=None,
            preference=None,
            destination_instance_ids_reverse_match=None,
            route_map_id=None,
            owner_id=None,
            priority=None,
            list_of_destination_child_instance_types=None,
            list_of_source_route_table_ids=None,
            as_path_match_mode=None,
            list_of_source_child_instance_types=None,
            list_of_match_community_set=None,
            community_operate_mode=None,
            cen_region_id=None,
            list_of_operate_community_set=None):
        api_request = APIRequest('ModifyCenRouteMap', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RouteTypes": list_of_route_types,
            "ResourceOwnerId": resource_owner_id,
            "CidrMatchMode": cidr_match_mode,
            "CommunityMatchMode": community_match_mode,
            "CenId": cen_id,
            "MapResult": map_result,
            "AsPathLength": as_path_length,
            "Description": description,
            "SourceInstanceIdsReverseMatch": source_instance_ids_reverse_match,
            "NextPriority": next_priority,
            "DestinationCidrBlocks": list_of_destination_cidr_blocks,
            "DestinationRouteTableIds": list_of_destination_route_table_ids,
            "SourceInstanceIds": list_of_source_instance_ids,
            "SourceRegionIds": list_of_source_region_ids,
            "DestinationInstanceIds": list_of_destination_instance_ids,
            "MatchAsns": list_of_match_asns,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Preference": preference,
            "DestinationInstanceIdsReverseMatch": destination_instance_ids_reverse_match,
            "RouteMapId": route_map_id,
            "OwnerId": owner_id,
            "Priority": priority,
            "DestinationChildInstanceTypes": list_of_destination_child_instance_types,
            "SourceRouteTableIds": list_of_source_route_table_ids,
            "AsPathMatchMode": as_path_match_mode,
            "SourceChildInstanceTypes": list_of_source_child_instance_types,
            "MatchCommunitySet": list_of_match_community_set,
            "CommunityOperateMode": community_operate_mode,
            "CenRegionId": cen_region_id,
            "OperateCommunitySet": list_of_operate_community_set}
        repeat_info = {"RouteTypes": ('RouteTypes', 'list', 'str', None),
                       "DestinationCidrBlocks": ('DestinationCidrBlocks', 'list', 'str', None),
                       "DestinationRouteTableIds": ('DestinationRouteTableIds', 'list', 'str', None),
                       "SourceInstanceIds": ('SourceInstanceIds', 'list', 'str', None),
                       "SourceRegionIds": ('SourceRegionIds', 'list', 'str', None),
                       "DestinationInstanceIds": ('DestinationInstanceIds', 'list', 'str', None),
                       "MatchAsns": ('MatchAsns', 'list', 'str', None),
                       "DestinationChildInstanceTypes": ('DestinationChildInstanceTypes', 'list', 'str', None),
                       "SourceRouteTableIds": ('SourceRouteTableIds', 'list', 'str', None),
                       "SourceChildInstanceTypes": ('SourceChildInstanceTypes', 'list', 'str', None),
                       "MatchCommunitySet": ('MatchCommunitySet', 'list', 'str', None),
                       "OperateCommunitySet": ('OperateCommunitySet', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_cen_child_instance_route_entries(
            self,
            child_instance_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            child_instance_type=None,
            page_number=None,
            status=None,
            child_instance_region_id=None):
        api_request = APIRequest('DescribeCenChildInstanceRouteEntries',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ChildInstanceId": child_instance_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "ChildInstanceType": child_instance_type,
            "PageNumber": page_number,
            "Status": status,
            "ChildInstanceRegionId": child_instance_region_id}
        return self._handle_request(api_request).result

    def untag_resources(
            self,
            resource_owner_id=None,
            list_of_resource_id=None,
            resource_owner_account=None,
            owner_account=None,
            tag_owner_uid=None,
            tag_owner_bid=None,
            owner_id=None,
            list_of_tag_key=None,
            resource_type=None):
        api_request = APIRequest('UntagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": list_of_resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "TagOwnerUid": tag_owner_uid,
            "TagOwnerBid": tag_owner_bid,
            "OwnerId": owner_id,
            "TagKey": list_of_tag_key,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "TagKey": ('TagKey', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_cen_private_zone_routes(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            page_size=None,
            host_region_id=None,
            access_region_id=None,
            page_number=None):
        api_request = APIRequest('DescribeCenPrivateZoneRoutes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "PageSize": page_size,
            "HostRegionId": host_region_id,
            "AccessRegionId": access_region_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def route_private_zone_in_cen_to_vpc(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            host_region_id=None,
            access_region_id=None,
            owner_id=None,
            host_vpc_id=None):
        api_request = APIRequest('RoutePrivateZoneInCenToVpc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "HostRegionId": host_region_id,
            "AccessRegionId": access_region_id,
            "OwnerId": owner_id,
            "HostVpcId": host_vpc_id}
        return self._handle_request(api_request).result

    def unroute_private_zone_in_cen_to_vpc(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            access_region_id=None,
            owner_id=None):
        api_request = APIRequest('UnroutePrivateZoneInCenToVpc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "AccessRegionId": access_region_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_route_service_in_cen(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            host=None,
            host_region_id=None,
            access_region_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteRouteServiceInCen', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "Host": host,
            "HostRegionId": host_region_id,
            "AccessRegionId": access_region_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_route_services_in_cen(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            page_size=None,
            host=None,
            host_region_id=None,
            access_region_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeRouteServicesInCen', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "Host": host,
            "HostRegionId": host_region_id,
            "AccessRegionId": access_region_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def resolve_and_route_service_in_cen(
            self,
            resource_owner_id=None,
            list_of_access_region_ids=None,
            resource_owner_account=None,
            client_token=None,
            cen_id=None,
            owner_account=None,
            host=None,
            host_region_id=None,
            owner_id=None,
            update_interval=None):
        api_request = APIRequest('ResolveAndRouteServiceInCen', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccessRegionIds": list_of_access_region_ids,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "Host": host,
            "HostRegionId": host_region_id,
            "OwnerId": owner_id,
            "UpdateInterval": update_interval}
        repeat_info = {"AccessRegionIds": ('AccessRegionIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_grant_rules_to_cen(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            cen_id=None,
            owner_account=None,
            owner_id=None,
            product_type=None):
        api_request = APIRequest('DescribeGrantRulesToCen', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def describe_cen_attached_child_instance_attribute(
            self,
            child_instance_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            owner_id=None,
            child_instance_type=None,
            child_instance_region_id=None):
        api_request = APIRequest(
            'DescribeCenAttachedChildInstanceAttribute',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ChildInstanceId": child_instance_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ChildInstanceType": child_instance_type,
            "ChildInstanceRegionId": child_instance_region_id}
        return self._handle_request(api_request).result

    def publish_route_entries(
            self,
            child_instance_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            destination_cidr_block=None,
            child_instance_type=None,
            child_instance_route_table_id=None,
            child_instance_region_id=None):
        api_request = APIRequest('PublishRouteEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ChildInstanceId": child_instance_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "DestinationCidrBlock": destination_cidr_block,
            "ChildInstanceType": child_instance_type,
            "ChildInstanceRouteTableId": child_instance_route_table_id,
            "ChildInstanceRegionId": child_instance_region_id}
        return self._handle_request(api_request).result

    def withdraw_published_route_entries(
            self,
            child_instance_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            destination_cidr_block=None,
            child_instance_type=None,
            child_instance_route_table_id=None,
            child_instance_region_id=None):
        api_request = APIRequest('WithdrawPublishedRouteEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ChildInstanceId": child_instance_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "DestinationCidrBlock": destination_cidr_block,
            "ChildInstanceType": child_instance_type,
            "ChildInstanceRouteTableId": child_instance_route_table_id,
            "ChildInstanceRegionId": child_instance_region_id}
        return self._handle_request(api_request).result

    def describe_published_route_entries(
            self,
            child_instance_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            destination_cidr_block=None,
            page_size=None,
            child_instance_type=None,
            child_instance_route_table_id=None,
            page_number=None,
            child_instance_region_id=None):
        api_request = APIRequest('DescribePublishedRouteEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ChildInstanceId": child_instance_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "DestinationCidrBlock": destination_cidr_block,
            "PageSize": page_size,
            "ChildInstanceType": child_instance_type,
            "ChildInstanceRouteTableId": child_instance_route_table_id,
            "PageNumber": page_number,
            "ChildInstanceRegionId": child_instance_region_id}
        return self._handle_request(api_request).result

    def describe_cen_geographic_spans(
            self,
            resource_owner_id=None,
            geographic_span_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeCenGeographicSpans', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "GeographicSpanId": geographic_span_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_child_instance_regions(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            product_type=None):
        api_request = APIRequest('DescribeChildInstanceRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def unassociate_cen_bandwidth_package(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            cen_bandwidth_package_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('UnassociateCenBandwidthPackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "CenBandwidthPackageId": cen_bandwidth_package_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_cen_inter_region_bandwidth_limit(
            self,
            local_region_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            opposite_region_id=None,
            bandwidth_limit=None,
            owner_id=None):
        api_request = APIRequest('SetCenInterRegionBandwidthLimit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocalRegionId": local_region_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "OppositeRegionId": opposite_region_id,
            "BandwidthLimit": bandwidth_limit,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_cen_bandwidth_package_spec(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            bandwidth=None,
            cen_bandwidth_package_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ModifyCenBandwidthPackageSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "CenBandwidthPackageId": cen_bandwidth_package_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_cen_bandwidth_package_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_bandwidth_package_id=None,
            owner_account=None,
            name=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('ModifyCenBandwidthPackageAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenBandwidthPackageId": cen_bandwidth_package_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_cen_attribute(
            self,
            protection_level=None,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            name=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('ModifyCenAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProtectionLevel": protection_level,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def enable_cen_vbr_health_check(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            health_check_source_ip=None,
            vbr_instance_owner_id=None,
            owner_account=None,
            vbr_instance_id=None,
            health_check_target_ip=None,
            owner_id=None,
            vbr_instance_region_id=None):
        api_request = APIRequest('EnableCenVbrHealthCheck', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "HealthCheckSourceIp": health_check_source_ip,
            "VbrInstanceOwnerId": vbr_instance_owner_id,
            "OwnerAccount": owner_account,
            "VbrInstanceId": vbr_instance_id,
            "HealthCheckTargetIp": health_check_target_ip,
            "OwnerId": owner_id,
            "VbrInstanceRegionId": vbr_instance_region_id}
        return self._handle_request(api_request).result

    def disable_cen_vbr_health_check(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            vbr_instance_owner_id=None,
            owner_account=None,
            vbr_instance_id=None,
            owner_id=None,
            vbr_instance_region_id=None):
        api_request = APIRequest('DisableCenVbrHealthCheck', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "VbrInstanceOwnerId": vbr_instance_owner_id,
            "OwnerAccount": owner_account,
            "VbrInstanceId": vbr_instance_id,
            "OwnerId": owner_id,
            "VbrInstanceRegionId": vbr_instance_region_id}
        return self._handle_request(api_request).result

    def detach_cen_child_instance(
            self,
            child_instance_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            cen_owner_id=None,
            owner_id=None,
            child_instance_type=None,
            child_instance_owner_id=None,
            child_instance_region_id=None):
        api_request = APIRequest('DetachCenChildInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ChildInstanceId": child_instance_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "CenOwnerId": cen_owner_id,
            "OwnerId": owner_id,
            "ChildInstanceType": child_instance_type,
            "ChildInstanceOwnerId": child_instance_owner_id,
            "ChildInstanceRegionId": child_instance_region_id}
        return self._handle_request(api_request).result

    def describe_cen_vbr_health_check(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            vbr_instance_owner_id=None,
            owner_account=None,
            vbr_instance_id=None,
            page_size=None,
            owner_id=None,
            vbr_instance_region_id=None,
            page_number=None):
        api_request = APIRequest('DescribeCenVbrHealthCheck', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "VbrInstanceOwnerId": vbr_instance_owner_id,
            "OwnerAccount": owner_account,
            "VbrInstanceId": vbr_instance_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "VbrInstanceRegionId": vbr_instance_region_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_cens(
            self,
            list_of_filter_=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            list_of_tag=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeCens', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Filter": list_of_filter_,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        repeat_info = {"Filter": ('Filter', 'list', 'dict', [('Value', 'list', 'str', None),
                                                             ('Key', 'str', None, None),
                                                             ]),
                       "Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_cen_region_domain_route_entries(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            cen_region_id=None,
            page_size=None,
            owner_id=None,
            page_number=None,
            status=None):
        api_request = APIRequest('DescribeCenRegionDomainRouteEntries',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "CenRegionId": cen_region_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_cen_inter_region_bandwidth_limits(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeCenInterRegionBandwidthLimits',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_cen_geographic_span_remaining_bandwidth(
            self,
            geographic_region_bid=None,
            resource_owner_id=None,
            geographic_region_aid=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest(
            'DescribeCenGeographicSpanRemainingBandwidth',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "GeographicRegionBId": geographic_region_bid,
            "ResourceOwnerId": resource_owner_id,
            "GeographicRegionAId": geographic_region_aid,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_cen_bandwidth_packages(
            self,
            list_of_filter_=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None,
            is_or_key=None):
        api_request = APIRequest('DescribeCenBandwidthPackages', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Filter": list_of_filter_,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "IsOrKey": is_or_key}
        repeat_info = {"Filter": ('Filter', 'list', 'dict', [('Value', 'list', 'str', None),
                                                             ('Key', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_cen_attached_child_instances(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            child_instance_type=None,
            page_number=None,
            child_instance_region_id=None):
        api_request = APIRequest('DescribeCenAttachedChildInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "ChildInstanceType": child_instance_type,
            "PageNumber": page_number,
            "ChildInstanceRegionId": child_instance_region_id}
        return self._handle_request(api_request).result

    def delete_cen_bandwidth_package(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_bandwidth_package_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteCenBandwidthPackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenBandwidthPackageId": cen_bandwidth_package_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_cen(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteCen', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_cen_bandwidth_package(
            self,
            geographic_region_bid=None,
            resource_owner_id=None,
            period=None,
            geographic_region_aid=None,
            auto_pay=None,
            resource_owner_account=None,
            client_token=None,
            bandwidth=None,
            owner_account=None,
            description=None,
            owner_id=None,
            bandwidth_package_charge_type=None,
            name=None,
            pricing_cycle=None):
        api_request = APIRequest('CreateCenBandwidthPackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GeographicRegionBId": geographic_region_bid,
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "GeographicRegionAId": geographic_region_aid,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "BandwidthPackageChargeType": bandwidth_package_charge_type,
            "Name": name,
            "PricingCycle": pricing_cycle}
        return self._handle_request(api_request).result

    def create_cen(
            self,
            protection_level=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            name=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('CreateCen', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProtectionLevel": protection_level,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Name": name,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def attach_cen_child_instance(
            self,
            child_instance_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            owner_account=None,
            owner_id=None,
            child_instance_type=None,
            child_instance_owner_id=None,
            child_instance_region_id=None):
        api_request = APIRequest('AttachCenChildInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ChildInstanceId": child_instance_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ChildInstanceType": child_instance_type,
            "ChildInstanceOwnerId": child_instance_owner_id,
            "ChildInstanceRegionId": child_instance_region_id}
        return self._handle_request(api_request).result

    def associate_cen_bandwidth_package(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cen_id=None,
            cen_bandwidth_package_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('AssociateCenBandwidthPackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CenId": cen_id,
            "CenBandwidthPackageId": cen_bandwidth_package_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_route_conflict(
            self,
            child_instance_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            destination_cidr_block=None,
            page_size=None,
            owner_id=None,
            child_instance_type=None,
            child_instance_route_table_id=None,
            page_number=None,
            child_instance_region_id=None):
        api_request = APIRequest('DescribeRouteConflict', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ChildInstanceId": child_instance_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DestinationCidrBlock": destination_cidr_block,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "ChildInstanceType": child_instance_type,
            "ChildInstanceRouteTableId": child_instance_route_table_id,
            "PageNumber": page_number,
            "ChildInstanceRegionId": child_instance_region_id}
        return self._handle_request(api_request).result

    def describe_geographic_region_membership(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None,
            geographic_region_id=None):
        api_request = APIRequest('DescribeGeographicRegionMembership',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "GeographicRegionId": geographic_region_id}
        return self._handle_request(api_request).result
