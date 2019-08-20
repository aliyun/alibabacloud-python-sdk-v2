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


class LinkWANClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'LinkWAN'
        self.api_version = '2018-12-30'
        self.location_service_code = 'linkwan'
        self.location_endpoint_type = 'openAPI'

    def update_embedded_ns_auto_sync_enabling_state(self, instance_id=None, enabled=None):
        api_request = APIRequest('UpdateEmbeddedNsAutoSyncEnablingState',
                                 'GET', 'https', 'RPC', 'body')
        api_request._params = {"InstanceId": instance_id, "Enabled": enabled}
        return self._handle_request(api_request).result

    def submit_external_nodes_adding_task(self, node_group_id=None, list_of_nodes=None):
        api_request = APIRequest('SubmitExternalNodesAddingTask', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"NodeGroupId": node_group_id, "Nodes": list_of_nodes}
        repeat_info = {"Nodes": ('Nodes', 'list', 'dict', [('DevEui', 'str', None, None),
                                                           ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_external_node_tuples(self, list_of_dev_eui_list=None):
        api_request = APIRequest('DeleteExternalNodeTuples', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEuiList": list_of_dev_eui_list}
        repeat_info = {"DevEuiList": ('DevEuiList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_custom_local_join_permission(
            self,
            class_mode=None,
            freq_band_plan_group_id=None,
            join_eui=None,
            join_permission_name=None):
        api_request = APIRequest('CreateCustomLocalJoinPermission', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "ClassMode": class_mode,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "JoinEui": join_eui,
            "JoinPermissionName": join_permission_name}
        return self._handle_request(api_request).result

    def submit_external_node_tuples_importing_task(self, list_of_node_tuples=None):
        api_request = APIRequest('SubmitExternalNodeTuplesImportingTask',
                                 'GET', 'https', 'RPC', 'body')
        api_request._params = {"NodeTuples": list_of_node_tuples}
        repeat_info = {"NodeTuples": ('NodeTuples', 'list', 'dict', [('AppSKey', 'str', None, None),
                                                                     ('NwkSKey', 'str', None, None),
                                                                     ('LoraVer', 'str', None, None),
                                                                     ('DevEui', 'str', None, None),
                                                                     ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_node_transfer_packet_paths(
            self,
            page_number=None,
            page_size=None,
            dev_eui=None,
            base64_encoded_mac_payload=None,
            log_millis=None):
        api_request = APIRequest('ListNodeTransferPacketPaths', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "PageNumber": page_number,
            "PageSize": page_size,
            "DevEui": dev_eui,
            "Base64EncodedMacPayload": base64_encoded_mac_payload,
            "LogMillis": log_millis}
        return self._handle_request(api_request).result

    def update_roaming_join_permission(self, join_permission_id=None, join_permission_name=None):
        api_request = APIRequest('UpdateRoamingJoinPermission', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "JoinPermissionId": join_permission_id,
            "JoinPermissionName": join_permission_name}
        return self._handle_request(api_request).result

    def update_owned_local_join_permission(
            self,
            class_mode=None,
            join_permission_id=None,
            freq_band_plan_group_id=None,
            join_permission_name=None):
        api_request = APIRequest('UpdateOwnedLocalJoinPermission', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "ClassMode": class_mode,
            "JoinPermissionId": join_permission_id,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "JoinPermissionName": join_permission_name}
        return self._handle_request(api_request).result

    def update_owned_local_join_permission_enabling_state(
            self, join_permission_id=None, enabled=None):
        api_request = APIRequest(
            'UpdateOwnedLocalJoinPermissionEnablingState',
            'GET',
            'https',
            'RPC',
            'body')
        api_request._params = {"JoinPermissionId": join_permission_id, "Enabled": enabled}
        return self._handle_request(api_request).result

    def update_roaming_join_permission_enabling_state(self, join_permission_id=None, enabled=None):
        api_request = APIRequest(
            'UpdateRoamingJoinPermissionEnablingState',
            'GET',
            'https',
            'RPC',
            'body')
        api_request._params = {"JoinPermissionId": join_permission_id, "Enabled": enabled}
        return self._handle_request(api_request).result

    def count_nodes_by_owned_join_permission_id(self, join_permission_id=None, fuzzy_dev_eui=None):
        api_request = APIRequest('CountNodesByOwnedJoinPermissionId', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"JoinPermissionId": join_permission_id, "FuzzyDevEui": fuzzy_dev_eui}
        return self._handle_request(api_request).result

    def list_nodes_by_node_group_id(
            self,
            offset=None,
            node_group_id=None,
            fuzzy_dev_eui=None,
            limit=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListNodesByNodeGroupId', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "Offset": offset,
            "NodeGroupId": node_group_id,
            "FuzzyDevEui": fuzzy_dev_eui,
            "Limit": limit,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def list_nodes_by_owned_join_permission_id(
            self,
            offset=None,
            join_permission_id=None,
            fuzzy_dev_eui=None,
            limit=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListNodesByOwnedJoinPermissionId', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "Offset": offset,
            "JoinPermissionId": join_permission_id,
            "FuzzyDevEui": fuzzy_dev_eui,
            "Limit": limit,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def count_nodes_by_node_group_id(self, node_group_id=None, fuzzy_dev_eui=None):
        api_request = APIRequest('CountNodesByNodeGroupId', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"NodeGroupId": node_group_id, "FuzzyDevEui": fuzzy_dev_eui}
        return self._handle_request(api_request).result

    def get_user_license(self,):
        api_request = APIRequest('GetUserLicense', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def create_gateway(
            self,
            city=None,
            latitude=None,
            description=None,
            address_code=None,
            gis_coordinate_system=None,
            longitude=None,
            pin_code=None,
            address=None,
            gw_eui=None,
            freq_band_plan_group_id=None,
            district=None,
            name=None,
            communication_mode=None):
        api_request = APIRequest('CreateGateway', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "City": city,
            "Latitude": latitude,
            "Description": description,
            "AddressCode": address_code,
            "GisCoordinateSystem": gis_coordinate_system,
            "Longitude": longitude,
            "PinCode": pin_code,
            "Address": address,
            "GwEui": gw_eui,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "District": district,
            "Name": name,
            "CommunicationMode": communication_mode}
        return self._handle_request(api_request).result

    def list_gateway_transfer_packets(
            self,
            end_millis=None,
            page_number=None,
            page_size=None,
            gw_eui=None,
            dev_eui=None,
            category=None,
            begin_millis=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListGatewayTransferPackets', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "EndMillis": end_millis,
            "PageNumber": page_number,
            "PageSize": page_size,
            "GwEui": gw_eui,
            "DevEui": dev_eui,
            "Category": category,
            "BeginMillis": begin_millis,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def delete_gateway(self, gw_eui=None):
        api_request = APIRequest('DeleteGateway', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui}
        return self._handle_request(api_request).result

    def get_gateway(self, gw_eui=None):
        api_request = APIRequest('GetGateway', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui}
        return self._handle_request(api_request).result

    def get_gateway_transfer_packets_download_url(
            self,
            gw_eui=None,
            end_millis=None,
            dev_eui=None,
            category=None,
            begin_millis=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('GetGatewayTransferPacketsDownloadUrl',
                                 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "GwEui": gw_eui,
            "EndMillis": end_millis,
            "DevEui": dev_eui,
            "Category": category,
            "BeginMillis": begin_millis,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def list_gateway_transfer_flow_stats(
            self,
            end_millis=None,
            begin_millis=None,
            gw_eui=None,
            time_interval_unit=None):
        api_request = APIRequest('ListGatewayTransferFlowStats', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "EndMillis": end_millis,
            "BeginMillis": begin_millis,
            "GwEui": gw_eui,
            "TimeIntervalUnit": time_interval_unit}
        return self._handle_request(api_request).result

    def list_node_group_transfer_flow_stats(
            self,
            end_millis=None,
            begin_millis=None,
            node_group_id=None,
            time_interval_unit=None):
        api_request = APIRequest('ListNodeGroupTransferFlowStats', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "EndMillis": end_millis,
            "BeginMillis": begin_millis,
            "NodeGroupId": node_group_id,
            "TimeIntervalUnit": time_interval_unit}
        return self._handle_request(api_request).result

    def list_gateway_online_records(
            self,
            off_set=None,
            limit=None,
            gw_eui=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListGatewayOnlineRecords', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "OffSet": off_set,
            "Limit": limit,
            "GwEui": gw_eui,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def list_active_gateways(self,):
        api_request = APIRequest('ListActiveGateways', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def get_gateway_status_stat(self, gw_eui=None):
        api_request = APIRequest('GetGatewayStatusStat', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui}
        return self._handle_request(api_request).result

    def get_freq_band_plan_group(self, group_id=None):
        api_request = APIRequest('GetFreqBandPlanGroup', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GroupId": group_id}
        return self._handle_request(api_request).result

    def count_notifications(
            self,
            end_millis=None,
            handle_state=None,
            list_of_category=None,
            begin_millis=None):
        api_request = APIRequest('CountNotifications', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "EndMillis": end_millis,
            "HandleState": handle_state,
            "Category": list_of_category,
            "BeginMillis": begin_millis}
        repeat_info = {"Category": ('Category', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_freq_band_plan_groups(self,):
        api_request = APIRequest('ListFreqBandPlanGroups', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def get_notification(self, notification_id=None):
        api_request = APIRequest('GetNotification', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"NotificationId": notification_id}
        return self._handle_request(api_request).result

    def list_notifications(
            self,
            offset=None,
            end_millis=None,
            handle_state=None,
            limit=None,
            list_of_category=None,
            begin_millis=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListNotifications', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "Offset": offset,
            "EndMillis": end_millis,
            "HandleState": handle_state,
            "Limit": limit,
            "Category": list_of_category,
            "BeginMillis": begin_millis,
            "SortingField": sorting_field,
            "Ascending": ascending}
        repeat_info = {"Category": ('Category', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def count_gateway_tuple_orders(self, list_of_states=None):
        api_request = APIRequest('CountGatewayTupleOrders', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"States": list_of_states}
        repeat_info = {"States": ('States', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def submit_node_tuple_order(self, lora_version=None, required_count=None):
        api_request = APIRequest('SubmitNodeTupleOrder', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"LoraVersion": lora_version, "RequiredCount": required_count}
        return self._handle_request(api_request).result

    def count_node_tuple_orders(self, is_kpm=None, list_of_states=None):
        api_request = APIRequest('CountNodeTupleOrders', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"IsKpm": is_kpm, "States": list_of_states}
        repeat_info = {"States": ('States', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def update_notifications_handle_state(
            self,
            list_of_notification_id=None,
            target_handle_state=None):
        api_request = APIRequest('UpdateNotificationsHandleState', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "NotificationId": list_of_notification_id,
            "TargetHandleState": target_handle_state}
        repeat_info = {"NotificationId": ('NotificationId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def submit_gateway_tuple_order(self, required_count=None):
        api_request = APIRequest('SubmitGatewayTupleOrder', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"RequiredCount": required_count}
        return self._handle_request(api_request).result

    def get_gateway_tuple_order(self, order_id=None):
        api_request = APIRequest('GetGatewayTupleOrder', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"OrderId": order_id}
        return self._handle_request(api_request).result

    def list_gateway_tuple_orders(
            self,
            offset=None,
            limit=None,
            list_of_state=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListGatewayTupleOrders', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "Offset": offset,
            "Limit": limit,
            "State": list_of_state,
            "SortingField": sorting_field,
            "Ascending": ascending}
        repeat_info = {"State": ('State', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_gateway_tuples_download_url(self, order_id=None):
        api_request = APIRequest('GetGatewayTuplesDownloadUrl', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"OrderId": order_id}
        return self._handle_request(api_request).result

    def get_node_tuple_order(self, order_id=None):
        api_request = APIRequest('GetNodeTupleOrder', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"OrderId": order_id}
        return self._handle_request(api_request).result

    def list_node_tuple_orders(
            self,
            is_kpm=None,
            offset=None,
            limit=None,
            list_of_state=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListNodeTupleOrders', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "IsKpm": is_kpm,
            "Offset": offset,
            "Limit": limit,
            "State": list_of_state,
            "SortingField": sorting_field,
            "Ascending": ascending}
        repeat_info = {"State": ('State', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def update_gateway(
            self,
            city=None,
            latitude=None,
            description=None,
            address_code=None,
            gis_coordinate_system=None,
            longitude=None,
            address=None,
            gw_eui=None,
            freq_band_plan_group_id=None,
            district=None,
            name=None,
            communication_mode=None):
        api_request = APIRequest('UpdateGateway', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "City": city,
            "Latitude": latitude,
            "Description": description,
            "AddressCode": address_code,
            "GisCoordinateSystem": gis_coordinate_system,
            "Longitude": longitude,
            "Address": address,
            "GwEui": gw_eui,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "District": district,
            "Name": name,
            "CommunicationMode": communication_mode}
        return self._handle_request(api_request).result

    def get_lab_gateway(self, gw_eui=None):
        api_request = APIRequest('GetLabGateway', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui}
        return self._handle_request(api_request).result

    def get_node_tuples_download_url(self, order_id=None):
        api_request = APIRequest('GetNodeTuplesDownloadUrl', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"OrderId": order_id}
        return self._handle_request(api_request).result

    def list_gateways(
            self,
            fuzzy_gw_eui=None,
            limit=None,
            fuzzy_city=None,
            online_state=None,
            is_enabled=None,
            fuzzy_name=None,
            offset=None,
            freq_band_plan_group_id=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListGateways', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "FuzzyGwEui": fuzzy_gw_eui,
            "Limit": limit,
            "FuzzyCity": fuzzy_city,
            "OnlineState": online_state,
            "IsEnabled": is_enabled,
            "FuzzyName": fuzzy_name,
            "Offset": offset,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def count_gateways(
            self,
            fuzzy_name=None,
            fuzzy_gw_eui=None,
            freq_band_plan_group_id=None,
            fuzzy_city=None,
            online_state=None,
            is_enabled=None):
        api_request = APIRequest('CountGateways', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "FuzzyName": fuzzy_name,
            "FuzzyGwEui": fuzzy_gw_eui,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "FuzzyCity": fuzzy_city,
            "OnlineState": online_state,
            "IsEnabled": is_enabled}
        return self._handle_request(api_request).result

    def list_gateways_gis_info(self,):
        api_request = APIRequest('ListGatewaysGisInfo', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def create_lab_gateway(self, freq_band_plan_group_id=None, name=None):
        api_request = APIRequest('CreateLabGateway', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"FreqBandPlanGroupId": freq_band_plan_group_id, "Name": name}
        return self._handle_request(api_request).result

    def delete_lab_gateway(self, gw_eui=None):
        api_request = APIRequest('DeleteLabGateway', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui}
        return self._handle_request(api_request).result

    def count_lab_gateways(
            self,
            fuzzy_name=None,
            fuzzy_gw_eui=None,
            freq_band_plan_group_id=None,
            online_state=None):
        api_request = APIRequest('CountLabGateways', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "FuzzyName": fuzzy_name,
            "FuzzyGwEui": fuzzy_gw_eui,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "OnlineState": online_state}
        return self._handle_request(api_request).result

    def list_lab_gateways(
            self,
            fuzzy_name=None,
            offset=None,
            fuzzy_gw_eui=None,
            freq_band_plan_group_id=None,
            limit=None,
            online_state=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListLabGateways', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "FuzzyName": fuzzy_name,
            "Offset": offset,
            "FuzzyGwEui": fuzzy_gw_eui,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "Limit": limit,
            "OnlineState": online_state,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def update_gateway_enabling_state(self, gw_eui=None, enabled=None):
        api_request = APIRequest('UpdateGatewayEnablingState', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui, "Enabled": enabled}
        return self._handle_request(api_request).result

    def create_lab_node(
            self,
            class_mode=None,
            lora_version=None,
            freq_band_plan_group_id=None,
            name=None):
        api_request = APIRequest('CreateLabNode', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "ClassMode": class_mode,
            "LoraVersion": lora_version,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "Name": name}
        return self._handle_request(api_request).result

    def delete_lab_node(self, dev_eui=None):
        api_request = APIRequest('DeleteLabNode', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui}
        return self._handle_request(api_request).result

    def bind_lab_node_to_lab_gateway(self, dev_eui=None, gw_eui=None):
        api_request = APIRequest('BindLabNodeToLabGateway', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui, "GwEui": gw_eui}
        return self._handle_request(api_request).result

    def list_lab_gateway_logs(
            self,
            gw_eui=None,
            end_millis=None,
            page_number=None,
            dev_eui=None,
            page_size=None,
            begin_millis=None):
        api_request = APIRequest('ListLabGatewayLogs', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "GwEui": gw_eui,
            "EndMillis": end_millis,
            "PageNumber": page_number,
            "DevEui": dev_eui,
            "PageSize": page_size,
            "BeginMillis": begin_millis}
        return self._handle_request(api_request).result

    def unbind_lab_node_from_lab_gateway(self, dev_eui=None, gw_eui=None):
        api_request = APIRequest('UnbindLabNodeFromLabGateway', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui, "GwEui": gw_eui}
        return self._handle_request(api_request).result

    def get_lab_node(self, dev_eui=None):
        api_request = APIRequest('GetLabNode', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui}
        return self._handle_request(api_request).result

    def count_lab_nodes(
            self,
            fuzzy_name=None,
            activation_state=None,
            freq_band_plan_group_id=None,
            fuzzy_dev_eui=None):
        api_request = APIRequest('CountLabNodes', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "FuzzyName": fuzzy_name,
            "ActivationState": activation_state,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "FuzzyDevEui": fuzzy_dev_eui}
        return self._handle_request(api_request).result

    def list_lab_nodes(
            self,
            fuzzy_name=None,
            offset=None,
            freq_band_plan_group_id=None,
            fuzzy_dev_eui=None,
            limit=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListLabNodes', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "FuzzyName": fuzzy_name,
            "Offset": offset,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "FuzzyDevEui": fuzzy_dev_eui,
            "Limit": limit,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def list_bound_lab_gateways(self, dev_eui=None):
        api_request = APIRequest('ListBoundLabGateways', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui}
        return self._handle_request(api_request).result

    def list_lab_node_logs(
            self,
            end_millis=None,
            page_number=None,
            dev_eui=None,
            page_size=None,
            begin_millis=None):
        api_request = APIRequest('ListLabNodeLogs', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "EndMillis": end_millis,
            "PageNumber": page_number,
            "DevEui": dev_eui,
            "PageSize": page_size,
            "BeginMillis": begin_millis}
        return self._handle_request(api_request).result

    def get_lab_gateway_gwmp_config(self, gw_eui=None):
        api_request = APIRequest('GetLabGatewayGwmpConfig', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui}
        return self._handle_request(api_request).result

    def update_lab_gateway_gwmp_config(self, gw_eui=None, gwmp_config=None):
        api_request = APIRequest('UpdateLabGatewayGwmpConfig', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui, "GwmpConfig": gwmp_config}
        return self._handle_request(api_request).result

    def trigger_lab_gateway_config_report(self, gw_eui=None):
        api_request = APIRequest('TriggerLabGatewayConfigReport', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui}
        return self._handle_request(api_request).result

    def trigger_lab_gateway_device_info_report(self, gw_eui=None):
        api_request = APIRequest('TriggerLabGatewayDeviceInfoReport', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui}
        return self._handle_request(api_request).result

    def trigger_lab_gateway_log_report(self, gw_eui=None):
        api_request = APIRequest('TriggerLabGatewayLogReport', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui}
        return self._handle_request(api_request).result

    def reboot_lab_gateway(self, gw_eui=None):
        api_request = APIRequest('RebootLabGateway', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui}
        return self._handle_request(api_request).result

    def update_lab_gateway_ssh_ctrl(self, gw_eui=None, enabled=None):
        api_request = APIRequest('UpdateLabGatewaySshCtrl', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui, "Enabled": enabled}
        return self._handle_request(api_request).result

    def update_lab_gateway_uart_ctrl(self, gw_eui=None, enabled=None):
        api_request = APIRequest('UpdateLabGatewayUartCtrl', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui, "Enabled": enabled}
        return self._handle_request(api_request).result

    def get_lab_node_debug_config(self, dev_eui=None):
        api_request = APIRequest('GetLabNodeDebugConfig', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui}
        return self._handle_request(api_request).result

    def update_lab_node_debug_config(self, dev_eui=None, debug_config_json=None):
        api_request = APIRequest('UpdateLabNodeDebugConfig', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui, "DebugConfigJson": debug_config_json}
        return self._handle_request(api_request).result

    def get_lab_node_downlink_config(self, dev_eui=None):
        api_request = APIRequest('GetLabNodeDownlinkConfig', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui}
        return self._handle_request(api_request).result

    def get_lab_node_join_accept_config(self, dev_eui=None):
        api_request = APIRequest('GetLabNodeJoinAcceptConfig', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui}
        return self._handle_request(api_request).result

    def send_mac_command_to_lab_node(self, dev_eui=None, debug_config=None, mac_command=None):
        api_request = APIRequest('SendMacCommandToLabNode', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "DevEui": dev_eui,
            "DebugConfig": debug_config,
            "MacCommand": mac_command}
        return self._handle_request(api_request).result

    def send_business_command_to_lab_node(
            self,
            dev_eui=None,
            debug_config=None,
            business_command=None):
        api_request = APIRequest('SendBusinessCommandToLabNode', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "DevEui": dev_eui,
            "DebugConfig": debug_config,
            "BusinessCommand": business_command}
        return self._handle_request(api_request).result

    def delete_local_join_permission(self, join_permission_id=None):
        api_request = APIRequest('DeleteLocalJoinPermission', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"JoinPermissionId": join_permission_id}
        return self._handle_request(api_request).result

    def create_local_join_permission(
            self,
            class_mode=None,
            freq_band_plan_group_id=None,
            use_default_join_eui=None,
            join_permission_name=None):
        api_request = APIRequest('CreateLocalJoinPermission', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "ClassMode": class_mode,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "UseDefaultJoinEui": use_default_join_eui,
            "JoinPermissionName": join_permission_name}
        return self._handle_request(api_request).result

    def update_lab_gateway(self, gw_eui=None, name=None):
        api_request = APIRequest('UpdateLabGateway', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui, "Name": name}
        return self._handle_request(api_request).result

    def list_bound_lab_nodes(self, gw_eui=None):
        api_request = APIRequest('ListBoundLabNodes', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"GwEui": gw_eui}
        return self._handle_request(api_request).result

    def update_lab_node(self, class_mode=None, dev_eui=None, lora_version=None, name=None):
        api_request = APIRequest('UpdateLabNode', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "ClassMode": class_mode,
            "DevEui": dev_eui,
            "LoraVersion": lora_version,
            "Name": name}
        return self._handle_request(api_request).result

    def get_owned_join_permission(self, join_permission_id=None):
        api_request = APIRequest('GetOwnedJoinPermission', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"JoinPermissionId": join_permission_id}
        return self._handle_request(api_request).result

    def check_cloud_product_open_status(self, service_code=None):
        api_request = APIRequest('CheckCloudProductOpenStatus', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"ServiceCode": service_code}
        return self._handle_request(api_request).result

    def get_rented_join_permission(self, join_permission_id=None):
        api_request = APIRequest('GetRentedJoinPermission', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"JoinPermissionId": join_permission_id}
        return self._handle_request(api_request).result

    def list_owned_join_permissions(
            self,
            fuzzy_join_permission_name=None,
            offset=None,
            fuzzy_renter_aliyun_id=None,
            enabled=None,
            fuzzy_join_eui=None,
            limit=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListOwnedJoinPermissions', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "FuzzyJoinPermissionName": fuzzy_join_permission_name,
            "Offset": offset,
            "FuzzyRenterAliyunId": fuzzy_renter_aliyun_id,
            "Enabled": enabled,
            "FuzzyJoinEui": fuzzy_join_eui,
            "Limit": limit,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def list_rented_join_permissions(
            self,
            type_=None,
            enabled=None,
            fuzzy_join_eui=None,
            limit=None,
            fuzzy_join_permission_name=None,
            offset=None,
            bound_node_group=None,
            fuzzy_owner_aliyun_id=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListRentedJoinPermissions', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "Type": type_,
            "Enabled": enabled,
            "FuzzyJoinEui": fuzzy_join_eui,
            "Limit": limit,
            "FuzzyJoinPermissionName": fuzzy_join_permission_name,
            "Offset": offset,
            "BoundNodeGroup": bound_node_group,
            "FuzzyOwnerAliyunId": fuzzy_owner_aliyun_id,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def count_owned_join_permissions(
            self,
            fuzzy_join_permission_name=None,
            fuzzy_renter_aliyun_id=None,
            enabled=None,
            fuzzy_join_eui=None):
        api_request = APIRequest('CountOwnedJoinPermissions', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "FuzzyJoinPermissionName": fuzzy_join_permission_name,
            "FuzzyRenterAliyunId": fuzzy_renter_aliyun_id,
            "Enabled": enabled,
            "FuzzyJoinEui": fuzzy_join_eui}
        return self._handle_request(api_request).result

    def count_rented_join_permissions(
            self,
            fuzzy_join_permission_name=None,
            type_=None,
            enabled=None,
            bound_node_group=None,
            fuzzy_join_eui=None,
            fuzzy_owner_aliyun_id=None):
        api_request = APIRequest('CountRentedJoinPermissions', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "FuzzyJoinPermissionName": fuzzy_join_permission_name,
            "Type": type_,
            "Enabled": enabled,
            "BoundNodeGroup": bound_node_group,
            "FuzzyJoinEui": fuzzy_join_eui,
            "FuzzyOwnerAliyunId": fuzzy_owner_aliyun_id}
        return self._handle_request(api_request).result

    def apply_roaming_join_permission(
            self,
            class_mode=None,
            freq_band_plan_group_id=None,
            join_permission_name=None):
        api_request = APIRequest('ApplyRoamingJoinPermission', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "ClassMode": class_mode,
            "FreqBandPlanGroupId": freq_band_plan_group_id,
            "JoinPermissionName": join_permission_name}
        return self._handle_request(api_request).result

    def return_join_permission(self, join_permission_id=None, join_permission_type=None):
        api_request = APIRequest('ReturnJoinPermission', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "JoinPermissionId": join_permission_id,
            "JoinPermissionType": join_permission_type}
        return self._handle_request(api_request).result

    def submit_join_permission_auth_order(self, join_permission_id=None, renter_aliyun_id=None):
        api_request = APIRequest('SubmitJoinPermissionAuthOrder', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "JoinPermissionId": join_permission_id,
            "RenterAliyunId": renter_aliyun_id}
        return self._handle_request(api_request).result

    def accept_join_permission_auth_order(self, order_id=None):
        api_request = APIRequest('AcceptJoinPermissionAuthOrder', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"OrderId": order_id}
        return self._handle_request(api_request).result

    def cancel_join_permission_auth_order(self, order_id=None):
        api_request = APIRequest('CancelJoinPermissionAuthOrder', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"OrderId": order_id}
        return self._handle_request(api_request).result

    def reject_join_permission_auth_order(self, order_id=None):
        api_request = APIRequest('RejectJoinPermissionAuthOrder', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"OrderId": order_id}
        return self._handle_request(api_request).result

    def get_join_permission_auth_order(self, order_id=None):
        api_request = APIRequest('GetJoinPermissionAuthOrder', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"OrderId": order_id}
        return self._handle_request(api_request).result

    def create_node_group(self, node_group_name=None, join_permission_id=None):
        api_request = APIRequest('CreateNodeGroup', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "NodeGroupName": node_group_name,
            "JoinPermissionId": join_permission_id}
        return self._handle_request(api_request).result

    def register_kpm_public_key(self, public_key=None):
        api_request = APIRequest('RegisterKpmPublicKey', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"PublicKey": public_key}
        return self._handle_request(api_request).result

    def unregister_kpm_public_key(self,):
        api_request = APIRequest('UnregisterKpmPublicKey', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def get_kpm_public_key(self,):
        api_request = APIRequest('GetKpmPublicKey', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def delete_node_group(self, node_group_id=None):
        api_request = APIRequest('DeleteNodeGroup', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"NodeGroupId": node_group_id}
        return self._handle_request(api_request).result

    def update_node_group(self, node_group_name=None, node_group_id=None):
        api_request = APIRequest('UpdateNodeGroup', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"NodeGroupName": node_group_name, "NodeGroupId": node_group_id}
        return self._handle_request(api_request).result

    def get_node_group(self, node_group_id=None):
        api_request = APIRequest('GetNodeGroup', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"NodeGroupId": node_group_id}
        return self._handle_request(api_request).result

    def list_node_groups(
            self,
            fuzzy_name=None,
            offset=None,
            fuzzy_join_eui=None,
            fuzzy_dev_eui=None,
            limit=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListNodeGroups', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "FuzzyName": fuzzy_name,
            "Offset": offset,
            "FuzzyJoinEui": fuzzy_join_eui,
            "FuzzyDevEui": fuzzy_dev_eui,
            "Limit": limit,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def count_node_groups(self, fuzzy_name=None, fuzzy_join_eui=None, fuzzy_dev_eui=None):
        api_request = APIRequest('CountNodeGroups', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "FuzzyName": fuzzy_name,
            "FuzzyJoinEui": fuzzy_join_eui,
            "FuzzyDevEui": fuzzy_dev_eui}
        return self._handle_request(api_request).result

    def bind_join_permission_to_node_group(self, node_group_id=None, join_permission_id=None):
        api_request = APIRequest('BindJoinPermissionToNodeGroup', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"NodeGroupId": node_group_id, "JoinPermissionId": join_permission_id}
        return self._handle_request(api_request).result

    def update_data_dispatch_config(
            self,
            uplink_topic=None,
            product_key=None,
            product_type=None,
            product_name=None,
            uplink_region_name=None,
            node_group_id=None,
            data_dispatch_destination=None):
        api_request = APIRequest('UpdateDataDispatchConfig', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "UplinkTopic": uplink_topic,
            "ProductKey": product_key,
            "ProductType": product_type,
            "ProductName": product_name,
            "UplinkRegionName": uplink_region_name,
            "NodeGroupId": node_group_id,
            "DataDispatchDestination": data_dispatch_destination}
        return self._handle_request(api_request).result

    def update_data_dispatch_enabling_state(self, node_group_id=None, data_dispatch_enabled=None):
        api_request = APIRequest('UpdateDataDispatchEnablingState', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "NodeGroupId": node_group_id,
            "DataDispatchEnabled": data_dispatch_enabled}
        return self._handle_request(api_request).result

    def add_node_to_group(self, dev_eui=None, pin_code=None, node_group_id=None):
        api_request = APIRequest('AddNodeToGroup', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui, "PinCode": pin_code, "NodeGroupId": node_group_id}
        return self._handle_request(api_request).result

    def remove_node_from_group(self, dev_eui=None, node_group_id=None):
        api_request = APIRequest('RemoveNodeFromGroup', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui, "NodeGroupId": node_group_id}
        return self._handle_request(api_request).result

    def get_node(self, dev_eui=None):
        api_request = APIRequest('GetNode', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui}
        return self._handle_request(api_request).result

    def list_activated_features(self,):
        api_request = APIRequest('ListActivatedFeatures', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def describe_regions(self,):
        api_request = APIRequest('DescribeRegions', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def update_lab_node_downlink_config(
            self,
            dev_eui=None,
            debug_config=None,
            downlink_config=None):
        api_request = APIRequest('UpdateLabNodeDownlinkConfig', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "DevEui": dev_eui,
            "DebugConfig": debug_config,
            "DownlinkConfig": downlink_config}
        return self._handle_request(api_request).result

    def update_lab_node_join_accept_config(
            self,
            dev_eui=None,
            debug_config=None,
            join_accept_config=None):
        api_request = APIRequest('UpdateLabNodeJoinAcceptConfig', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "DevEui": dev_eui,
            "DebugConfig": debug_config,
            "JoinAcceptConfig": join_accept_config}
        return self._handle_request(api_request).result

    def get_gateway_packet_stat(self, end_millis=None, begin_millis=None, gw_eui=None):
        api_request = APIRequest('GetGatewayPacketStat', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "EndMillis": end_millis,
            "BeginMillis": begin_millis,
            "GwEui": gw_eui}
        return self._handle_request(api_request).result

    def send_unicast_command(
            self,
            dev_eui=None,
            max_retries=None,
            clean_up=None,
            fport=None,
            comfirmed=None,
            content=None):
        api_request = APIRequest('SendUnicastCommand', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "DevEui": dev_eui,
            "MaxRetries": max_retries,
            "CleanUp": clean_up,
            "FPort": fport,
            "Comfirmed": comfirmed,
            "Content": content}
        return self._handle_request(api_request).result

    def list_node_group_transfer_packets(
            self,
            end_millis=None,
            page_number=None,
            page_size=None,
            dev_eui=None,
            node_group_id=None,
            category=None,
            begin_millis=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('ListNodeGroupTransferPackets', 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "EndMillis": end_millis,
            "PageNumber": page_number,
            "PageSize": page_size,
            "DevEui": dev_eui,
            "NodeGroupId": node_group_id,
            "Category": category,
            "BeginMillis": begin_millis,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def get_node_group_transfer_packets_download_url(
            self,
            end_millis=None,
            dev_eui=None,
            node_group_id=None,
            category=None,
            begin_millis=None,
            sorting_field=None,
            ascending=None):
        api_request = APIRequest('GetNodeGroupTransferPacketsDownloadUrl',
                                 'GET', 'https', 'RPC', 'body')
        api_request._params = {
            "EndMillis": end_millis,
            "DevEui": dev_eui,
            "NodeGroupId": node_group_id,
            "Category": category,
            "BeginMillis": begin_millis,
            "SortingField": sorting_field,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def unbind_join_permission_from_node_group(self, node_group_id=None, join_permission_id=None):
        api_request = APIRequest('UnbindJoinPermissionFromNodeGroup', 'GET', 'https', 'RPC', 'body')
        api_request._params = {"NodeGroupId": node_group_id, "JoinPermissionId": join_permission_id}
        return self._handle_request(api_request).result

    def create_multicast_group(
            self,
            class_mode=None,
            frequency=None,
            lora_version=None,
            periodicity=None,
            data_rate=None):
        api_request = APIRequest('CreateMulticastGroup', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "ClassMode": class_mode,
            "Frequency": frequency,
            "LoraVersion": lora_version,
            "Periodicity": periodicity,
            "DataRate": data_rate}
        return self._handle_request(api_request).result

    def delete_multicast_group(self, mc_address=None):
        api_request = APIRequest('DeleteMulticastGroup', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"McAddress": mc_address}
        return self._handle_request(api_request).result

    def bind_nodes_to_multicast_group(self, mc_address=None, list_of_dev_eui_list=None):
        api_request = APIRequest('BindNodesToMulticastGroup', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"McAddress": mc_address, "DevEuiList": list_of_dev_eui_list}
        repeat_info = {"DevEuiList": ('DevEuiList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def unbind_nodes_from_multicast_group(self, mc_address=None, list_of_dev_eui_list=None):
        api_request = APIRequest('UnbindNodesFromMulticastGroup', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"McAddress": mc_address, "DevEuiList": list_of_dev_eui_list}
        repeat_info = {"DevEuiList": ('DevEuiList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_multicast_group(self, mc_address=None):
        api_request = APIRequest('GetMulticastGroup', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"McAddress": mc_address}
        return self._handle_request(api_request).result

    def get_node_multicast_config(self, dev_eui=None):
        api_request = APIRequest('GetNodeMulticastConfig', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"DevEui": dev_eui}
        return self._handle_request(api_request).result

    def list_bound_nodes_by_mc_address(self, offset=None, limit=None, mc_address=None):
        api_request = APIRequest('ListBoundNodesByMcAddress', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"Offset": offset, "Limit": limit, "McAddress": mc_address}
        return self._handle_request(api_request).result

    def send_multicast_command(self, mc_address=None, fport=None, content=None):
        api_request = APIRequest('SendMulticastCommand', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"McAddress": mc_address, "FPort": fport, "Content": content}
        return self._handle_request(api_request).result
