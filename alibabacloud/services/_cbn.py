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
from alibabacloud.resources.collection import _create_resource_collection
from alibabacloud.resources.collection import _create_sub_resource_without_page_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _CBNResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'cbn', _client=_client)
        self.cens = _create_resource_collection(
            _CBNCenResource, _client, _client.describe_cens,
            'Cens.Cen', 'CenId',
        )
        self.cen_bandwidth_packages = _create_resource_collection(
            _CBNCenBandwidthPackageResource, _client, _client.describe_cen_bandwidth_packages,
            'CenBandwidthPackages.CenBandwidthPackage', 'CenBandwidthPackageId',
        )
        self.cen_route_maps = _create_resource_collection(
            _CBNCenRouteMapResource, _client, _client.describe_cen_route_maps,
            'RouteMaps.RouteMap', 'RouteMapId',
        )

    def create_cen(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_cen(**_params)
        cen_id = _new_get_key_in_response(response, 'CenId')
        return _CBNCenResource(cen_id, _client=self._client)

    def create_cen_bandwidth_package(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_cen_bandwidth_package(**_params)
        cen_bandwidth_package_id = _new_get_key_in_response(response, 'CenBandwidthPackageId')
        return _CBNCenBandwidthPackageResource(cen_bandwidth_package_id, _client=self._client)

    def create_cen_route_map(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_cen_route_map(**_params)
        route_map_id = _new_get_key_in_response(response, 'RouteMapId')
        return _CBNCenRouteMapResource(route_map_id, _client=self._client)


class _CBNCenResource(ServiceResource):

    def __init__(self, cen_id, _client=None):
        ServiceResource.__init__(self, "cbn.cen", _client=_client)
        self.cen_id = cen_id

        self.cen_bandwidth_package_ids = None
        self.creation_time = None
        self.description = None
        self.name = None
        self.protection_level = None
        self.status = None
        self.tags = None

        self.flowlogs = _create_sub_resource_without_page_collection(
            _CBNFlowlogResource, _client, _client.describe_flowlogs,
            'FlowLogs.FlowLog', 'FlowLogId', parent_identifier="CenId",
            parent_identifier_value=self.cen_id
        )

    def attach_cen_child_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.attach_cen_child_instance(cen_id=self.cen_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_cen(cen_id=self.cen_id, **_params)

    def delete_route_service_in(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_route_service_in_cen(cen_id=self.cen_id, **_params)

    def describe_cen_attached_child_instance_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cen_attached_child_instance_attribute(cen_id=self.cen_id,
                                                                           **_params)

    def describe_cen_attached_child_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cen_attached_child_instances(cen_id=self.cen_id, **_params)

    def describe_cen_child_instance_route_entries(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cen_child_instance_route_entries(cen_id=self.cen_id, **_params)

    def describe_cen_geographic_span_remaining_bandwidth(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cen_geographic_span_remaining_bandwidth(cen_id=self.cen_id,
                                                                             **_params)

    def describe_cen_private_zone_routes(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cen_private_zone_routes(cen_id=self.cen_id, **_params)

    def describe_grant_rules_to(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_grant_rules_to_cen(cen_id=self.cen_id, **_params)

    def describe_published_route_entries(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_published_route_entries(cen_id=self.cen_id, **_params)

    def detach_cen_child_instance(self, **params):
        _params = _transfer_params(params)
        return self._client.detach_cen_child_instance(cen_id=self.cen_id, **_params)

    def disable_cen_vbr_health_check(self, **params):
        _params = _transfer_params(params)
        return self._client.disable_cen_vbr_health_check(cen_id=self.cen_id, **_params)

    def enable_cen_vbr_health_check(self, **params):
        _params = _transfer_params(params)
        return self._client.enable_cen_vbr_health_check(cen_id=self.cen_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_cen_attribute(cen_id=self.cen_id, **_params)

    def publish_route_entries(self, **params):
        _params = _transfer_params(params)
        return self._client.publish_route_entries(cen_id=self.cen_id, **_params)

    def resolve_and_route_service_in(self, **params):
        _params = _transfer_params(params)
        return self._client.resolve_and_route_service_in_cen(cen_id=self.cen_id, **_params)

    def route_private_zone_in_cen_to_vpc(self, **params):
        _params = _transfer_params(params)
        return self._client.route_private_zone_in_cen_to_vpc(cen_id=self.cen_id, **_params)

    def set_cen_inter_region_bandwidth_limit(self, **params):
        _params = _transfer_params(params)
        return self._client.set_cen_inter_region_bandwidth_limit(cen_id=self.cen_id, **_params)

    def unroute_private_zone_in_cen_to_vpc(self, **params):
        _params = _transfer_params(params)
        return self._client.unroute_private_zone_in_cen_to_vpc(cen_id=self.cen_id, **_params)

    def withdraw_published_route_entries(self, **params):
        _params = _transfer_params(params)
        return self._client.withdraw_published_route_entries(cen_id=self.cen_id, **_params)

    def describe_cen_region_domain_route_entries(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cen_region_domain_route_entries(cen_id=self.cen_id, **_params)

    def create_flowlog(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_flowlog(cen_id=self.cen_id, **_params)
        flow_log_id = _new_get_key_in_response(response, 'FlowLogId')
        return _CBNFlowlogResource(flow_log_id, self.cen_id, _client=self._client)


class _CBNFlowlogResource(ServiceResource):

    def __init__(self, flow_log_id, cen_id, _client=None):
        ServiceResource.__init__(self, "cbn.flowlog", _client=_client)
        self.flow_log_id = flow_log_id
        self.cen_id = cen_id
        self.creation_time = None
        self.description = None
        self.flow_log_name = None
        self.log_store_name = None
        self.project_name = None
        self.region_id = None
        self.status = None

    def active_flow_log(self, **params):
        _params = _transfer_params(params)
        return self._client.active_flow_log(flow_log_id=self.flow_log_id, cen_id=self.cen_id,
                                            **_params)

    def deactive_flow_log(self, **params):
        _params = _transfer_params(params)
        return self._client.deactive_flow_log(flow_log_id=self.flow_log_id, cen_id=self.cen_id,
                                              **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_flowlog(flow_log_id=self.flow_log_id, cen_id=self.cen_id,
                                           **_params)

    def modify_flow_log_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_flow_log_attribute(flow_log_id=self.flow_log_id,
                                                      cen_id=self.cen_id, **_params)


class _CBNCenBandwidthPackageResource(ServiceResource):

    def __init__(self, cen_bandwidth_package_id, _client=None):
        ServiceResource.__init__(self, "cbn.cen_bandwidth_package", _client=_client)
        self.cen_bandwidth_package_id = cen_bandwidth_package_id

        self.bandwidth = None
        self.bandwidth_package_charge_type = None
        self.business_status = None
        self.cen_ids = None
        self.creation_time = None
        self.description = None
        self.expired_time = None
        self.geographic_region_aid = None
        self.geographic_region_bid = None
        self.geographic_span_id = None
        self.has_reservation_data = None
        self.is_cross_border = None
        self.name = None
        self.orgin_inter_region_bandwidth_limits = None
        self.ratio = None
        self.reservation_active_time = None
        self.reservation_bandwidth = None
        self.reservation_internet_charge_type = None
        self.reservation_order_type = None
        self.status = None
        self.type_for95 = None

    def associate(self, **params):
        _params = _transfer_params(params)
        return self._client.associate_cen_bandwidth_package(
            cen_bandwidth_package_id=self.cen_bandwidth_package_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_cen_bandwidth_package(
            cen_bandwidth_package_id=self.cen_bandwidth_package_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_cen_bandwidth_package_attribute(
            cen_bandwidth_package_id=self.cen_bandwidth_package_id, **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_cen_bandwidth_package_spec(
            cen_bandwidth_package_id=self.cen_bandwidth_package_id, **_params)

    def unassociate(self, **params):
        _params = _transfer_params(params)
        return self._client.unassociate_cen_bandwidth_package(
            cen_bandwidth_package_id=self.cen_bandwidth_package_id, **_params)


class _CBNCenRouteMapResource(ServiceResource):

    def __init__(self, route_map_id, _client=None):
        ServiceResource.__init__(self, "cbn.cen_route_map", _client=_client)
        self.route_map_id = route_map_id

        self.as_path_match_mode = None
        self.cen_id = None
        self.cen_region_id = None
        self.cidr_match_mode = None
        self.community_match_mode = None
        self.community_operate_mode = None
        self.description = None
        self.destination_child_instance_types = None
        self.destination_cidr_blocks = None
        self.destination_instance_ids = None
        self.destination_instance_ids_reverse_match = None
        self.destination_route_table_ids = None
        self.map_result = None
        self.match_asns = None
        self.match_community_set = None
        self.next_priority = None
        self.operate_community_set = None
        self.preference = None
        self.priority = None
        self.route_types = None
        self.source_child_instance_types = None
        self.source_instance_ids = None
        self.source_instance_ids_reverse_match = None
        self.source_region_ids = None
        self.source_route_table_ids = None
        self.status = None
        self.transmit_direction = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_cen_route_map(route_map_id=self.route_map_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_cen_route_map(route_map_id=self.route_map_id, **_params)
