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


class _SMARTAGResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'smartag', _client=_client)
        self.acls = _create_resource_collection(
            _SMARTAGACLResource, _client, _client.describe_ac_ls,
            'Acls.Acl', 'AclId',
        )
        self.cloud_connect_networks = _create_resource_collection(
            _SMARTAGCloudConnectNetworkResource, _client, _client.describe_cloud_connect_networks,
            'CloudConnectNetworks.CloudConnectNetwork', 'CcnId',
        )
        self.flow_logs = _create_resource_collection(
            _SMARTAGFlowLogResource, _client, _client.describe_flow_logs,
            'FlowLogs.FlowLogSetType', 'FlowLogId',
        )
        self.grant_rules = _create_resource_collection(
            _SMARTAGGrantRuleResource, _client, _client.describe_grant_rules,
            'GrantRules.GrantRule', 'GrantRuleId',
        )
        self.qoses = _create_resource_collection(
            _SMARTAGQosResource, _client, _client.describe_qoses,
            'Qoses.Qos', 'QosId',
        )
        self.regions = _create_special_resource_collection(
            _SMARTAGRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId',
        )

    def create_acl(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_acl(**_params)
        acl_id = _new_get_key_in_response(response, 'AclId')
        return _SMARTAGACLResource(acl_id, _client=self._client)

    def create_cloud_connect_network(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_cloud_connect_network(**_params)
        ccn_id = _new_get_key_in_response(response, 'CcnId')
        return _SMARTAGCloudConnectNetworkResource(ccn_id, _client=self._client)

    def create_flow_log(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_flow_log(**_params)
        flow_log_id = _new_get_key_in_response(response, 'FlowLogId')
        return _SMARTAGFlowLogResource(flow_log_id, _client=self._client)

    def create_network_optimization(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_network_optimization(**_params)
        network_opt_id = _new_get_key_in_response(response, 'NetworkOptId')
        return _SMARTAGNetworkOptimizationResource(network_opt_id, _client=self._client)

    def create_qos(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_qos(**_params)
        qos_id = _new_get_key_in_response(response, 'QosId')
        return _SMARTAGQosResource(qos_id, _client=self._client)


class _SMARTAGACLResource(ServiceResource):

    def __init__(self, acl_id, _client=None):
        ServiceResource.__init__(self, "smartag.acl", _client=_client)
        self.acl_id = acl_id

        self.name = None
        self.sag_count = None

    def add_acl_rule(self, **params):
        _params = _transfer_params(params)
        return self._client.add_acl_rule(acl_id=self.acl_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_acl(acl_id=self.acl_id, **_params)

    def describe_acl_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_acl_attribute(acl_id=self.acl_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_acl(acl_id=self.acl_id, **_params)

    def modify_rule(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_acl_rule(acl_id=self.acl_id, **_params)

    def associate(self, **params):
        _params = _transfer_params(params)
        return self._client.associate_acl(acl_id=self.acl_id, **_params)

    def delete_acl_rule(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_acl_rule(acl_id=self.acl_id, **_params)

    def disassociate(self, **params):
        _params = _transfer_params(params)
        return self._client.disassociate_acl(acl_id=self.acl_id, **_params)


class _SMARTAGCloudConnectNetworkResource(ServiceResource):

    def __init__(self, ccn_id, _client=None):
        ServiceResource.__init__(self, "smartag.cloud_connect_network", _client=_client)
        self.ccn_id = ccn_id

        self.associated_cen_id = None
        self.associated_cen_owner_id = None
        self.associated_cloud_box_count = None
        self.available_cloud_box_count = None
        self.cidr_block = None
        self.create_time = None
        self.description = None
        self.interworking_status = None
        self.is_default = None
        self.name = None
        self.snat_cidr_block = None
        self.tags = None

    def bind_smart_access_gateway(self, **params):
        _params = _transfer_params(params)
        return self._client.bind_smart_access_gateway(ccn_id=self.ccn_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_cloud_connect_network(ccn_id=self.ccn_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_cloud_connect_network(ccn_id=self.ccn_id, **_params)

    def unbind_smart_access_gateway(self, **params):
        _params = _transfer_params(params)
        return self._client.unbind_smart_access_gateway(ccn_id=self.ccn_id, **_params)


class _SMARTAGFlowLogResource(ServiceResource):

    def __init__(self, flow_log_id, _client=None):
        ServiceResource.__init__(self, "smartag.flow_log", _client=_client)
        self.flow_log_id = flow_log_id

        self.active_aging = None
        self.description = None
        self.inactive_aging = None
        self.logstore_name = None
        self.name = None
        self.netflow_server_ip = None
        self.netflow_server_port = None
        self.netflow_version = None
        self.output_type = None
        self.project_name = None
        self.sls_region_id = None
        self.status = None
        self.total_sag_num = None

    def active(self, **params):
        _params = _transfer_params(params)
        return self._client.active_flow_log(flow_log_id=self.flow_log_id, **_params)

    def deactive(self, **params):
        _params = _transfer_params(params)
        return self._client.deactive_flow_log(flow_log_id=self.flow_log_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_flow_log(flow_log_id=self.flow_log_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_flow_log_attribute(flow_log_id=self.flow_log_id, **_params)

    def associate(self, **params):
        _params = _transfer_params(params)
        return self._client.associate_flow_log(flow_log_id=self.flow_log_id, **_params)

    def disassociate(self, **params):
        _params = _transfer_params(params)
        return self._client.disassociate_flow_log(flow_log_id=self.flow_log_id, **_params)


class _SMARTAGGrantRuleResource(ServiceResource):

    def __init__(self, grant_rule_id, _client=None):
        ServiceResource.__init__(self, "smartag.grant_rule", _client=_client)
        self.grant_rule_id = grant_rule_id

        self.ccn_instance_id = None
        self.ccn_uid = None
        self.cen_instance_id = None
        self.cen_uid = None
        self.gmt_create = None
        self.gmt_modified = None
        self.region_id = None


class _SMARTAGNetworkOptimizationResource(ServiceResource):

    def __init__(self, network_opt_id, _client=None):
        ServiceResource.__init__(self, "smartag.network_optimization", _client=_client)
        self.network_opt_id = network_opt_id

    def add_network_optimization_setting(self, **params):
        _params = _transfer_params(params)
        return self._client.add_network_optimization_setting(network_opt_id=self.network_opt_id,
                                                             **_params)

    def attach_network_optimization_sags(self, **params):
        _params = _transfer_params(params)
        return self._client.attach_network_optimization_sags(network_opt_id=self.network_opt_id,
                                                             **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_network_optimization(network_opt_id=self.network_opt_id,
                                                        **_params)

    def delete_network_optimization_setting(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_network_optimization_setting(network_opt_id=self.network_opt_id,
                                                                **_params)

    def describe_network_optimization_sags(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_network_optimization_sags(network_opt_id=self.network_opt_id,
                                                               **_params)

    def describe_network_optimization_settings(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_network_optimization_settings(
            network_opt_id=self.network_opt_id, **_params)

    def detach_network_optimization_sags(self, **params):
        _params = _transfer_params(params)
        return self._client.detach_network_optimization_sags(network_opt_id=self.network_opt_id,
                                                             **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_network_optimization(network_opt_id=self.network_opt_id,
                                                        **_params)


class _SMARTAGQosResource(ServiceResource):

    def __init__(self, qos_id, _client=None):
        ServiceResource.__init__(self, "smartag.qos", _client=_client)
        self.qos_id = qos_id

        self.qos_name = None
        self.sag_count = None
        self.smart_ag_ids = None

        self.qos_cars = _create_sub_resource_without_page_collection(
            _SMARTAGQosCarResource, _client, _client.describe_qos_cars,
            'QosCars.QosCar', 'QosCarId', parent_identifier="QosId",
            parent_identifier_value=self.qos_id
        )
        self.qos_policies = _create_sub_resource_without_page_collection(
            _SMARTAGQosPolicyResource, _client, _client.describe_qos_policies,
            'QosPolicies.QosPolicy', 'QosPolicyId', parent_identifier="QosId",
            parent_identifier_value=self.qos_id
        )

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_qos(qos_id=self.qos_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_qos(qos_id=self.qos_id, **_params)

    def associate(self, **params):
        _params = _transfer_params(params)
        return self._client.associate_qos(qos_id=self.qos_id, **_params)

    def disassociate(self, **params):
        _params = _transfer_params(params)
        return self._client.disassociate_qos(qos_id=self.qos_id, **_params)

    def create_qos_car(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_qos_car(qos_id=self.qos_id, **_params)
        qos_car_id = _new_get_key_in_response(response, 'QosCarId')
        return _SMARTAGQosCarResource(qos_car_id, self.qos_id, _client=self._client)

    def create_qos_policy(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_qos_policy(qos_id=self.qos_id, **_params)
        qos_policy_id = _new_get_key_in_response(response, 'QosPolicyId')
        return _SMARTAGQosPolicyResource(qos_policy_id, self.qos_id, _client=self._client)


class _SMARTAGQosCarResource(ServiceResource):

    def __init__(self, qos_car_id, qos_id, _client=None):
        ServiceResource.__init__(self, "smartag.qos_car", _client=_client)
        self.qos_car_id = qos_car_id
        self.qos_id = qos_id
        self.description = None
        self.limit_type = None
        self.max_bandwidth_abs = None
        self.max_bandwidth_percent = None
        self.min_bandwidth_abs = None
        self.min_bandwidth_percent = None
        self.percent_source_type = None
        self.priority = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_qos_car(qos_car_id=self.qos_car_id, qos_id=self.qos_id,
                                           **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_qos_car(qos_car_id=self.qos_car_id, qos_id=self.qos_id,
                                           **_params)


class _SMARTAGQosPolicyResource(ServiceResource):

    def __init__(self, qos_policy_id, qos_id, _client=None):
        ServiceResource.__init__(self, "smartag.qos_policy", _client=_client)
        self.qos_policy_id = qos_policy_id
        self.qos_id = qos_id
        self.description = None
        self.dest_cidr = None
        self.dest_port_range = None
        self.end_time = None
        self.ip_protocol = None
        self.priority = None
        self.source_cidr = None
        self.source_port_range = None
        self.start_time = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_qos_policy(qos_policy_id=self.qos_policy_id, qos_id=self.qos_id,
                                              **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_qos_policy(qos_policy_id=self.qos_policy_id, qos_id=self.qos_id,
                                              **_params)


class _SMARTAGRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "smartag.region", _client=_client)
        self.region_id = region_id

        self.local_name = None
        self.region_endpoint = None
