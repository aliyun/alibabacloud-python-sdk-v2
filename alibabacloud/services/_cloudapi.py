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


class _CLOUDAPIResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'cloudapi', _client=_client)
        self.apis = _create_resource_collection(
            _CLOUDAPIApiResource, _client, _client.describe_apis,
            'ApiSummarys.ApiSummary', 'ApiId',
        )
        self.api_groups = _create_resource_collection(
            _CLOUDAPIApiGroupResource, _client, _client.describe_api_groups,
            'ApiGroupAttributes.ApiGroupAttribute', 'GroupId',
        )
        self.apps = _create_resource_collection(
            _CLOUDAPIAppResource, _client, _client.describe_apps,
            'Apps.AppItem', 'AppId',
        )
        self.ip_controls = _create_resource_collection(
            _CLOUDAPIIpControlResource, _client, _client.describe_ip_controls,
            'IpControlInfos.IpControlInfo', 'IpControlId',
        )
        self.regions = _create_special_resource_collection(
            _CLOUDAPIRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId',
        )
        self.signatures = _create_resource_collection(
            _CLOUDAPISignatureResource, _client, _client.describe_signatures,
            'SignatureInfos.SignatureInfo', 'SignatureId',
        )
        self.traffic_controls = _create_resource_collection(
            _CLOUDAPITrafficControlResource, _client, _client.describe_traffic_controls,
            'TrafficControls.TrafficControl', 'TrafficControlId',
        )

    def create_api(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_api(**_params)
        api_id = _new_get_key_in_response(response, 'ApiId')
        return _CLOUDAPIApiResource(api_id, _client=self._client)

    def create_api_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_api_group(**_params)
        group_id = _new_get_key_in_response(response, 'GroupId')
        return _CLOUDAPIApiGroupResource(group_id, _client=self._client)

    def create_app(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_app(**_params)
        app_id = _new_get_key_in_response(response, 'AppId')
        return _CLOUDAPIAppResource(app_id, _client=self._client)

    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _CLOUDAPIInstanceResource(instance_id, _client=self._client)

    def create_ip_control(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ip_control(**_params)
        ip_control_id = _new_get_key_in_response(response, 'IpControlId')
        return _CLOUDAPIIpControlResource(ip_control_id, _client=self._client)

    def create_signature(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_signature(**_params)
        signature_id = _new_get_key_in_response(response, 'SignatureId')
        return _CLOUDAPISignatureResource(signature_id, _client=self._client)

    def create_traffic_control(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_traffic_control(**_params)
        traffic_control_id = _new_get_key_in_response(response, 'TrafficControlId')
        return _CLOUDAPITrafficControlResource(traffic_control_id, _client=self._client)


class _CLOUDAPIApiResource(ServiceResource):

    def __init__(self, api_id, _client=None):
        ServiceResource.__init__(self, "cloudapi.api", _client=_client)
        self.api_id = api_id

        self.api_name = None
        self.created_time = None
        self.description = None
        self.group_id = None
        self.group_name = None
        self.modified_time = None
        self.region_id = None
        self.visibility = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_api(api_id=self.api_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api(api_id=self.api_id, **_params)

    def describe_api_doc(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api_doc(api_id=self.api_id, **_params)

    def describe_api_error_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api_error_data(api_id=self.api_id, **_params)

    def describe_api_history(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api_history(api_id=self.api_id, **_params)

    def describe_api_latency_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api_latency_data(api_id=self.api_id, **_params)

    def describe_api_qps_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api_qps_data(api_id=self.api_id, **_params)

    def describe_api_traffic_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api_traffic_data(api_id=self.api_id, **_params)

    def describe_authorized_apps(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_authorized_apps(api_id=self.api_id, **_params)

    def describe_deployed(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_deployed_api(api_id=self.api_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_api(api_id=self.api_id, **_params)

    def remove_apps_authorities(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_apps_authorities(api_id=self.api_id, **_params)

    def set_apps_authorities(self, **params):
        _params = _transfer_params(params)
        return self._client.set_apps_authorities(api_id=self.api_id, **_params)

    def abolish(self, **params):
        _params = _transfer_params(params)
        return self._client.abolish_api(api_id=self.api_id, **_params)

    def deploy(self, **params):
        _params = _transfer_params(params)
        return self._client.deploy_api(api_id=self.api_id, **_params)

    def switch(self, **params):
        _params = _transfer_params(params)
        return self._client.switch_api(api_id=self.api_id, **_params)


class _CLOUDAPIApiGroupResource(ServiceResource):

    def __init__(self, group_id, _client=None):
        ServiceResource.__init__(self, "cloudapi.api_group", _client=_client)
        self.group_id = group_id

        self.billing_status = None
        self.created_time = None
        self.description = None
        self.group_name = None
        self.https_policy = None
        self.illegal_status = None
        self.instance_id = None
        self.instance_type = None
        self.modified_time = None
        self.region_id = None
        self.sub_domain = None
        self.traffic_limit = None

    def create_api_stage_variable(self, **params):
        _params = _transfer_params(params)
        return self._client.create_api_stage_variable(group_id=self.group_id, **_params)

    def create_intranet_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.create_intranet_domain(group_id=self.group_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_api_group(group_id=self.group_id, **_params)

    def delete_api_stage_variable(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_api_stage_variable(group_id=self.group_id, **_params)

    def delete_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_domain(group_id=self.group_id, **_params)

    def delete_domain_certificate(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_domain_certificate(group_id=self.group_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api_group(group_id=self.group_id, **_params)

    def describe_api_histories(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api_histories(group_id=self.group_id, **_params)

    def describe_api_ip_controls(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api_ip_controls(group_id=self.group_id, **_params)

    def describe_api_signatures(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api_signatures(group_id=self.group_id, **_params)

    def describe_api_stage(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api_stage(group_id=self.group_id, **_params)

    def describe_api_traffic_controls(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_api_traffic_controls(group_id=self.group_id, **_params)

    def describe_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_domain(group_id=self.group_id, **_params)

    def describe_domains_resolution(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_domains_resolution(group_id=self.group_id, **_params)

    def describe_history_apis(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_history_apis(group_id=self.group_id, **_params)

    def describe_purchased(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_purchased_api_group(group_id=self.group_id, **_params)

    def describe_signatures_by_api(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_signatures_by_api(group_id=self.group_id, **_params)

    def describe_traffic_controls_by_api(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_traffic_controls_by_api(group_id=self.group_id, **_params)

    def import_swagger(self, **params):
        _params = _transfer_params(params)
        return self._client.import_swagger(group_id=self.group_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_api_group(group_id=self.group_id, **_params)

    def reactivate_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.reactivate_domain(group_id=self.group_id, **_params)

    def sdk_generate_by_group(self, **params):
        _params = _transfer_params(params)
        return self._client.sdk_generate_by_group(group_id=self.group_id, **_params)

    def set_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.set_domain(group_id=self.group_id, **_params)

    def set_domain_certificate(self, **params):
        _params = _transfer_params(params)
        return self._client.set_domain_certificate(group_id=self.group_id, **_params)

    def set_domain_web_socket_status(self, **params):
        _params = _transfer_params(params)
        return self._client.set_domain_web_socket_status(group_id=self.group_id, **_params)


class _CLOUDAPIAppResource(ServiceResource):

    def __init__(self, app_id, _client=None):
        ServiceResource.__init__(self, "cloudapi.app", _client=_client)
        self.app_id = app_id

        self.app_name = None
        self.description = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_app(app_id=self.app_id, **_params)

    def describe_apis_by(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_apis_by_app(app_id=self.app_id, **_params)

    def describe_app_security(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_app_security(app_id=self.app_id, **_params)

    def describe_authorized_apis(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_authorized_apis(app_id=self.app_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_app(app_id=self.app_id, **_params)

    def remove_apis_authorities(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_apis_authorities(app_id=self.app_id, **_params)

    def sdk_generate_by(self, **params):
        _params = _transfer_params(params)
        return self._client.sdk_generate_by_app(app_id=self.app_id, **_params)

    def set_apis_authorities(self, **params):
        _params = _transfer_params(params)
        return self._client.set_apis_authorities(app_id=self.app_id, **_params)


class _CLOUDAPIInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "cloudapi.instance", _client=_client)
        self.instance_id = instance_id

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_instance(instance_id=self.instance_id, **_params)

    def remove_vpc_access(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_vpc_access(instance_id=self.instance_id, **_params)

    def set_vpc_access(self, **params):
        _params = _transfer_params(params)
        return self._client.set_vpc_access(instance_id=self.instance_id, **_params)


class _CLOUDAPIIpControlResource(ServiceResource):

    def __init__(self, ip_control_id, _client=None):
        ServiceResource.__init__(self, "cloudapi.ip_control", _client=_client)
        self.ip_control_id = ip_control_id

        self.create_time = None
        self.description = None
        self.ip_control_name = None
        self.ip_control_type = None
        self.modified_time = None
        self.region_id = None

        self.ip_control_policy_items = _create_sub_resource_without_page_collection(
            _CLOUDAPIIpControlPolicyItemResource, _client, _client.describe_ip_control_policy_items,
            'IpControlPolicyItems.IpControlPolicyItem', 'PolicyItemId',
            parent_identifier="IpControlId", parent_identifier_value=self.ip_control_id
        )

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_ip_control(ip_control_id=self.ip_control_id, **_params)

    def describe_apis_by(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_apis_by_ip_control(ip_control_id=self.ip_control_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_ip_control(ip_control_id=self.ip_control_id, **_params)

    def remove_ip_control_apis(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_ip_control_apis(ip_control_id=self.ip_control_id, **_params)

    def set_ip_control_apis(self, **params):
        _params = _transfer_params(params)
        return self._client.set_ip_control_apis(ip_control_id=self.ip_control_id, **_params)

    def add_ip_control_policy_item(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_ip_control_policy_item(ip_control_id=self.ip_control_id,
                                                           **_params)
        policy_item_id = _new_get_key_in_response(response, 'PolicyItemId')
        return _CLOUDAPIIpControlPolicyItemResource(policy_item_id, self.ip_control_id,
                                                    _client=self._client)


class _CLOUDAPIIpControlPolicyItemResource(ServiceResource):

    def __init__(self, policy_item_id, ip_control_id, _client=None):
        ServiceResource.__init__(self, "cloudapi.ip_control_policy_item", _client=_client)
        self.policy_item_id = policy_item_id
        self.ip_control_id = ip_control_id
        self.app_id = None
        self.cidr_ip = None
        self.create_time = None
        self.modified_time = None

    def remove(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_ip_control_policy_item(policy_item_id=self.policy_item_id,
                                                          ip_control_id=self.ip_control_id,
                                                          **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_ip_control_policy_item(policy_item_id=self.policy_item_id,
                                                          ip_control_id=self.ip_control_id,
                                                          **_params)


class _CLOUDAPIRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "cloudapi.region", _client=_client)
        self.region_id = region_id

        self.local_name = None
        self.region_endpoint = None


class _CLOUDAPISignatureResource(ServiceResource):

    def __init__(self, signature_id, _client=None):
        ServiceResource.__init__(self, "cloudapi.signature", _client=_client)
        self.signature_id = signature_id

        self.created_time = None
        self.modified_time = None
        self.region_id = None
        self.signature_key = None
        self.signature_name = None
        self.signature_secret = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_signature(signature_id=self.signature_id, **_params)

    def describe_apis_by(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_apis_by_signature(signature_id=self.signature_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_signature(signature_id=self.signature_id, **_params)

    def remove_signature_apis(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_signature_apis(signature_id=self.signature_id, **_params)

    def set_signature_apis(self, **params):
        _params = _transfer_params(params)
        return self._client.set_signature_apis(signature_id=self.signature_id, **_params)


class _CLOUDAPITrafficControlResource(ServiceResource):

    def __init__(self, traffic_control_id, _client=None):
        ServiceResource.__init__(self, "cloudapi.traffic_control", _client=_client)
        self.traffic_control_id = traffic_control_id

        self.api_default = None
        self.app_default = None
        self.created_time = None
        self.description = None
        self.modified_time = None
        self.special_policies = None
        self.traffic_control_name = None
        self.traffic_control_unit = None
        self.user_default = None

    def add_traffic_special_control(self, **params):
        _params = _transfer_params(params)
        return self._client.add_traffic_special_control(traffic_control_id=self.traffic_control_id,
                                                        **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_traffic_control(traffic_control_id=self.traffic_control_id,
                                                   **_params)

    def delete_all_traffic_special_control(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_all_traffic_special_control(
            traffic_control_id=self.traffic_control_id, **_params)

    def delete_traffic_special_control(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_traffic_special_control(
            traffic_control_id=self.traffic_control_id, **_params)

    def describe_apis_by(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_apis_by_traffic_control(
            traffic_control_id=self.traffic_control_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_traffic_control(traffic_control_id=self.traffic_control_id,
                                                   **_params)

    def remove_traffic_control_apis(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_traffic_control_apis(traffic_control_id=self.traffic_control_id,
                                                        **_params)

    def set_traffic_control_apis(self, **params):
        _params = _transfer_params(params)
        return self._client.set_traffic_control_apis(traffic_control_id=self.traffic_control_id,
                                                     **_params)
