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


class _UISResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'uis', _client=_client)
        self.areas = _create_special_resource_collection(
            _UISAreaResource, _client, _client.describe_areas,
            'Areas.Area', 'AreaId',
        )
        self.connections = _create_resource_collection(
            _UISConnectionResource, _client, _client.describe_uis_connections,
            'UisConnections.UisConnection', 'UisConnectionId',
        )
        self.network_interfaces = _create_resource_collection(
            _UISNetworkInterfaceResource, _client, _client.describe_uis_network_interfaces,
            'NetworkInterfaces.NetworkInterface', 'NetworkInterfaceId',
        )
        self.nodes = _create_resource_collection(
            _UISNodeResource, _client, _client.describe_uis_nodes,
            'UisNodeList.UisNode', 'UisNodeId',
        )
        self.regions = _create_special_resource_collection(
            _UISRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId',
        )
        self.sub_connections = _create_resource_collection(
            _UISSubConnectionResource, _client, _client.describe_sub_connections,
            'UisSubConnections.UisSubConnection', 'UisSubConnectionId',
        )

    def create_uis_connection(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_uis_connection(**_params)
        uis_connection_id = _new_get_key_in_response(response, 'UisConnectionId')
        return _UISConnectionResource(uis_connection_id, _client=self._client)

    def create_uis_node(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_uis_node(**_params)
        uis_node_id = _new_get_key_in_response(response, 'UisNodeId')
        return _UISNodeResource(uis_node_id, _client=self._client)

    def create_sub_connection(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_sub_connection(**_params)
        uis_sub_connection_id = _new_get_key_in_response(response, 'UisSubConnectionId')
        return _UISSubConnectionResource(uis_sub_connection_id, _client=self._client)


class _UISAreaResource(ServiceResource):

    def __init__(self, area_id, _client=None):
        ServiceResource.__init__(self, "uis.area", _client=_client)
        self.area_id = area_id

        self.local_name = None


class _UISConnectionResource(ServiceResource):

    def __init__(self, uis_connection_id, _client=None):
        ServiceResource.__init__(self, "uis.connection", _client=_client)
        self.uis_connection_id = uis_connection_id

        self.description = None
        self.gre_config = None
        self.name = None
        self.ssl_config = None
        self.state = None
        self.uis_id = None
        self.uis_node_id = None
        self.uis_protocol = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_uis_connection(uis_connection_id=self.uis_connection_id,
                                                  **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_uis_connection_attribute(
            uis_connection_id=self.uis_connection_id, **_params)


class _UISNetworkInterfaceResource(ServiceResource):

    def __init__(self, network_interface_id, _client=None):
        ServiceResource.__init__(self, "uis.network_interface", _client=_client)
        self.network_interface_id = network_interface_id

        self.description = None
        self.ip_address = None
        self.log = None
        self.name = None
        self.security_group_id = None
        self.state = None
        self.uis_eni_id = None
        self.uis_node_id = None
        self.vswitch_id = None


class _UISNodeResource(ServiceResource):

    def __init__(self, uis_node_id, _client=None):
        ServiceResource.__init__(self, "uis.node", _client=_client)
        self.uis_node_id = uis_node_id

        self.create_time = None
        self.description = None
        self.ip_addrs_num = None
        self.name = None
        self.status = None
        self.uis_eni_ips = None
        self.uis_id = None
        self.uis_node_active_ip = None
        self.uis_node_area_id = None
        self.uis_node_bandwidth = None
        self.uis_node_ips = None

        self.dnat_entries = _create_sub_resource_without_page_collection(
            _UISDnatEntryResource, _client, _client.describe_dnat_entries,
            'UisDnatEntries.UisDnatEntry', 'UisDnatId', parent_identifier="UisNodeId",
            parent_identifier_value=self.uis_node_id
        )

    def add_node_ip(self, **params):
        _params = _transfer_params(params)
        return self._client.add_uis_node_ip(uis_node_id=self.uis_node_id, **_params)

    def create_network_interface(self, **params):
        _params = _transfer_params(params)
        return self._client.create_uis_network_interface(uis_node_id=self.uis_node_id, **_params)

    def delete_network_interface(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_uis_network_interface(uis_node_id=self.uis_node_id, **_params)

    def delete_node_ip(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_uis_node_ip(uis_node_id=self.uis_node_id, **_params)

    def describee_node_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_uise_node_status(uis_node_id=self.uis_node_id, **_params)

    def modify_dnat_entry(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_dnat_entry(uis_node_id=self.uis_node_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_uis_node_attribute(uis_node_id=self.uis_node_id, **_params)

    def create_dnat_entry(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_dnat_entry(uis_node_id=self.uis_node_id, **_params)
        uis_dnat_id = _new_get_key_in_response(response, 'UisDnatId')
        return _UISDnatEntryResource(uis_dnat_id, self.uis_node_id, _client=self._client)


class _UISDnatEntryResource(ServiceResource):

    def __init__(self, uis_dnat_id, uis_node_id, _client=None):
        ServiceResource.__init__(self, "uis.dnat_entry", _client=_client)
        self.uis_dnat_id = uis_dnat_id
        self.uis_node_id = uis_node_id
        self.destination_ip = None
        self.destination_port = None
        self.ip_protocol = None
        self.original_ip = None
        self.original_port = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_dnat_entry(uis_dnat_id=self.uis_dnat_id,
                                              uis_node_id=self.uis_node_id, **_params)


class _UISRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "uis.region", _client=_client)
        self.region_id = region_id

        self.local_name = None


class _UISSubConnectionResource(ServiceResource):

    def __init__(self, uis_sub_connection_id, _client=None):
        ServiceResource.__init__(self, "uis.sub_connection", _client=_client)
        self.uis_sub_connection_id = uis_sub_connection_id

        self.create_time = None
        self.description = None
        self.ip = None
        self.name = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_sub_connection(uis_sub_connection_id=self.uis_sub_connection_id,
                                                  **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_sub_connection(
            uis_sub_connection_id=self.uis_sub_connection_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_sub_connection(uis_sub_connection_id=self.uis_sub_connection_id,
                                                  **_params)
