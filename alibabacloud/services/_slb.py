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


class _SLBResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'slb', _client=_client)
        self.access_control_lists = _create_special_resource_collection(
            _SLBAccessControlListResource, _client, _client.describe_access_control_lists,
            'Acls.Acl', 'AclId',
        )
        self.ca_certificates = _create_special_resource_collection(
            _SLBCACertificateResource, _client, _client.describe_ca_certificates,
            'CACertificates.CACertificate', 'CACertificateId',
        )
        self.domain_extensions = _create_special_resource_collection(
            _SLBDomainExtensionResource, _client, _client.describe_domain_extensions,
            'DomainExtensions.DomainExtension', 'DomainExtensionId',
        )
        self.load_balancers = _create_resource_collection(
            _SLBLoadBalancerResource, _client, _client.describe_load_balancers,
            'LoadBalancers.LoadBalancer', 'LoadBalancerId',
        )
        self.master_slave_server_groups = _create_special_resource_collection(
            _SLBMasterSlaveServerGroupResource, _client,
            _client.describe_master_slave_server_groups,
            'MasterSlaveServerGroups.MasterSlaveServerGroup', 'MasterSlaveServerGroupId',
        )
        self.master_slave_vserver_groups = _create_special_resource_collection(
            _SLBMasterSlaveVServerGroupResource, _client,
            _client.describe_master_slave_vserver_groups,
            'MasterSlaveVServerGroups.MasterSlaveVServerGroup', 'MasterSlaveVServerGroupId',
        )
        self.regions = _create_special_resource_collection(
            _SLBRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId',
        )
        self.rules = _create_special_resource_collection(
            _SLBRuleResource, _client, _client.describe_rules,
            'Rules.Rule', 'RuleId',
        )
        self.server_certificates = _create_special_resource_collection(
            _SLBServerCertificateResource, _client, _client.describe_server_certificates,
            'ServerCertificates.ServerCertificate', 'ServerCertificateId',
        )
        self.vserver_groups = _create_special_resource_collection(
            _SLBVServerGroupResource, _client, _client.describe_vserver_groups,
            'VServerGroups.VServerGroup', 'VServerGroupId',
        )
        self.zones = _create_special_resource_collection(
            _SLBZoneResource, _client, _client.describe_zones,
            'Zones.Zone', 'ZoneId',
        )

    def create_access_control_list(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_access_control_list(**_params)
        acl_id = _new_get_key_in_response(response, 'AclId')
        return _SLBAccessControlListResource(acl_id, _client=self._client)

    def upload_ca_certificate(self, **params):
        _params = _transfer_params(params)
        response = self._client.upload_ca_certificate(**_params)
        ca_certificate_id = _new_get_key_in_response(response, 'CACertificateId')
        return _SLBCACertificateResource(ca_certificate_id, _client=self._client)

    def create_domain_extension(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_domain_extension(**_params)
        domain_extension_id = _new_get_key_in_response(response, 'DomainExtensionId')
        return _SLBDomainExtensionResource(domain_extension_id, _client=self._client)

    def create_load_balancer(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_load_balancer(**_params)
        load_balancer_id = _new_get_key_in_response(response, 'LoadBalancerId')
        return _SLBLoadBalancerResource(load_balancer_id, _client=self._client)

    def create_master_slave_server_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_master_slave_server_group(**_params)
        master_slave_server_group_id = _new_get_key_in_response(response,
                                                                'MasterSlaveServerGroupId')
        return _SLBMasterSlaveServerGroupResource(master_slave_server_group_id,
                                                  _client=self._client)

    def create_master_slave_vserver_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_master_slave_vserver_group(**_params)
        master_slave_vserver_group_id = _new_get_key_in_response(response,
                                                                 'MasterSlaveVServerGroupId')
        return _SLBMasterSlaveVServerGroupResource(master_slave_vserver_group_id,
                                                   _client=self._client)

    def upload_server_certificate(self, **params):
        _params = _transfer_params(params)
        response = self._client.upload_server_certificate(**_params)
        server_certificate_id = _new_get_key_in_response(response, 'ServerCertificateId')
        return _SLBServerCertificateResource(server_certificate_id, _client=self._client)

    def create_vserver_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_vserver_group(**_params)
        vserver_group_id = _new_get_key_in_response(response, 'VServerGroupId')
        return _SLBVServerGroupResource(vserver_group_id, _client=self._client)


class _SLBAccessControlListResource(ServiceResource):

    def __init__(self, acl_id, _client=None):
        ServiceResource.__init__(self, "slb.access_control_list", _client=_client)
        self.acl_id = acl_id

        self.acl_name = None
        self.address_ip_version = None
        self.resource_group_id = None
        self.tags = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_access_control_list(acl_id=self.acl_id, **_params)

    def describe_access_control_list_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_access_control_list_attribute(acl_id=self.acl_id, **_params)

    def remove_access_control_list_entry(self, **params):
        _params = _transfer_params(params)
        self._client.remove_access_control_list_entry(acl_id=self.acl_id, **_params)

    def set_access_control_list_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.set_access_control_list_attribute(acl_id=self.acl_id, **_params)


class _SLBCACertificateResource(ServiceResource):

    def __init__(self, ca_certificate_id, _client=None):
        ServiceResource.__init__(self, "slb.ca_certificate", _client=_client)
        self.ca_certificate_id = ca_certificate_id

        self.ca_certificate_name = None
        self.common_name = None
        self.create_time = None
        self.create_time_stamp = None
        self.expire_time = None
        self.expire_time_stamp = None
        self.fingerprint = None
        self.region_id = None
        self.resource_group_id = None
        self.tags = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_ca_certificate(ca_certificate_id=self.ca_certificate_id, **_params)

    def set_ca_certificate_name(self, **params):
        _params = _transfer_params(params)
        self._client.set_ca_certificate_name(ca_certificate_id=self.ca_certificate_id, **_params)

    def refresh(self):
        result = self._client.describe_ca_certificates(ca_certificate_id=self.ca_certificate_id)
        items = _new_get_key_in_response(result, 'CACertificates.CACertificate')
        if not items:
            raise ClientException(msg=
                                  "Failed to find ca_certificate data from DescribeCACertificates response. "
                                  "CACertificateId = {0}".format(self.ca_certificate_id))
        self._assign_attributes(items[0])


class _SLBDomainExtensionResource(ServiceResource):

    def __init__(self, domain_extension_id, _client=None):
        ServiceResource.__init__(self, "slb.domain_extension", _client=_client)
        self.domain_extension_id = domain_extension_id

        self.domain = None
        self.server_certificate_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_domain_extension(domain_extension_id=self.domain_extension_id,
                                             **_params)

    def set_domain_extension_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.set_domain_extension_attribute(domain_extension_id=self.domain_extension_id,
                                                    **_params)

    def refresh(self):
        result = self._client.describe_domain_extensions(
            domain_extension_id=self.domain_extension_id)
        items = _new_get_key_in_response(result, 'DomainExtensions.DomainExtension')
        if not items:
            raise ClientException(msg=
                                  "Failed to find domain_extension data from DescribeDomainExtensions response. "
                                  "DomainExtensionId = {0}".format(self.domain_extension_id))
        self._assign_attributes(items[0])


class _SLBLoadBalancerResource(ServiceResource):

    def __init__(self, load_balancer_id, _client=None):
        ServiceResource.__init__(self, "slb.load_balancer", _client=_client)
        self.load_balancer_id = load_balancer_id

        self.address = None
        self.address_ip_version = None
        self.address_type = None
        self.create_time = None
        self.create_time_stamp = None
        self.internet_charge_type = None
        self.load_balancer_name = None
        self.load_balancer_status = None
        self.master_zone_id = None
        self.network_type = None
        self.pay_type = None
        self.region_id = None
        self.region_id_alias = None
        self.resource_group_id = None
        self.slave_zone_id = None
        self.tags = None
        self.vswitch_id = None
        self.vpc_id = None

    def add_backend_servers(self, **params):
        _params = _transfer_params(params)
        self._client.add_backend_servers(load_balancer_id=self.load_balancer_id, **_params)

    def add_listener_white_list_item(self, **params):
        _params = _transfer_params(params)
        self._client.add_listener_white_list_item(load_balancer_id=self.load_balancer_id, **_params)

    def add_tags(self, **params):
        _params = _transfer_params(params)
        self._client.add_tags(load_balancer_id=self.load_balancer_id, **_params)

    def create_load_balancer_http_listener(self, **params):
        _params = _transfer_params(params)
        self._client.create_load_balancer_http_listener(load_balancer_id=self.load_balancer_id,
                                                        **_params)

    def create_load_balancer_tcp_listener(self, **params):
        _params = _transfer_params(params)
        self._client.create_load_balancer_tcp_listener(load_balancer_id=self.load_balancer_id,
                                                       **_params)

    def create_load_balancer_udp_listener(self, **params):
        _params = _transfer_params(params)
        self._client.create_load_balancer_udp_listener(load_balancer_id=self.load_balancer_id,
                                                       **_params)

    def create_rules(self, **params):
        _params = _transfer_params(params)
        self._client.create_rules(load_balancer_id=self.load_balancer_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_load_balancer(load_balancer_id=self.load_balancer_id, **_params)

    def delete_load_balancer_listener(self, **params):
        _params = _transfer_params(params)
        self._client.delete_load_balancer_listener(load_balancer_id=self.load_balancer_id,
                                                   **_params)

    def describe_health_status(self, **params):
        _params = _transfer_params(params)
        self._client.describe_health_status(load_balancer_id=self.load_balancer_id, **_params)

    def describe_listener_access_control_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_listener_access_control_attribute(
            load_balancer_id=self.load_balancer_id, **_params)

    def describe_load_balancer_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_load_balancer_attribute(load_balancer_id=self.load_balancer_id,
                                                      **_params)

    def describe_load_balancer_http_listener_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_load_balancer_http_listener_attribute(
            load_balancer_id=self.load_balancer_id, **_params)

    def describe_load_balancer_https_listener_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_load_balancer_https_listener_attribute(
            load_balancer_id=self.load_balancer_id, **_params)

    def describe_load_balancer_tcp_listener_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_load_balancer_tcp_listener_attribute(
            load_balancer_id=self.load_balancer_id, **_params)

    def describe_load_balancer_udp_listener_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_load_balancer_udp_listener_attribute(
            load_balancer_id=self.load_balancer_id, **_params)

    def modify_instance_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_load_balancer_instance_spec(load_balancer_id=self.load_balancer_id,
                                                        **_params)

    def modify_internet_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_load_balancer_internet_spec(load_balancer_id=self.load_balancer_id,
                                                        **_params)

    def modify_pay_type(self, **params):
        _params = _transfer_params(params)
        self._client.modify_load_balancer_pay_type(load_balancer_id=self.load_balancer_id,
                                                   **_params)

    def remove_backend_servers(self, **params):
        _params = _transfer_params(params)
        self._client.remove_backend_servers(load_balancer_id=self.load_balancer_id, **_params)

    def remove_listener_white_list_item(self, **params):
        _params = _transfer_params(params)
        self._client.remove_listener_white_list_item(load_balancer_id=self.load_balancer_id,
                                                     **_params)

    def remove_tags(self, **params):
        _params = _transfer_params(params)
        self._client.remove_tags(load_balancer_id=self.load_balancer_id, **_params)

    def set_backend_servers(self, **params):
        _params = _transfer_params(params)
        self._client.set_backend_servers(load_balancer_id=self.load_balancer_id, **_params)

    def set_listener_access_control_status(self, **params):
        _params = _transfer_params(params)
        self._client.set_listener_access_control_status(load_balancer_id=self.load_balancer_id,
                                                        **_params)

    def set_load_balancer_delete_protection(self, **params):
        _params = _transfer_params(params)
        self._client.set_load_balancer_delete_protection(load_balancer_id=self.load_balancer_id,
                                                         **_params)

    def set_load_balancer_http_listener_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.set_load_balancer_http_listener_attribute(
            load_balancer_id=self.load_balancer_id, **_params)

    def set_load_balancer_https_listener_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.set_load_balancer_https_listener_attribute(
            load_balancer_id=self.load_balancer_id, **_params)

    def set_load_balancer_name(self, **params):
        _params = _transfer_params(params)
        self._client.set_load_balancer_name(load_balancer_id=self.load_balancer_id, **_params)

    def set_load_balancer_status(self, **params):
        _params = _transfer_params(params)
        self._client.set_load_balancer_status(load_balancer_id=self.load_balancer_id, **_params)

    def set_load_balancer_tcp_listener_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.set_load_balancer_tcp_listener_attribute(
            load_balancer_id=self.load_balancer_id, **_params)

    def set_load_balancer_udp_listener_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.set_load_balancer_udp_listener_attribute(
            load_balancer_id=self.load_balancer_id, **_params)

    def start_load_balancer_listener(self, **params):
        _params = _transfer_params(params)
        self._client.start_load_balancer_listener(load_balancer_id=self.load_balancer_id, **_params)

    def stop_load_balancer_listener(self, **params):
        _params = _transfer_params(params)
        self._client.stop_load_balancer_listener(load_balancer_id=self.load_balancer_id, **_params)

    def create_load_balancer_https_listener(self, **params):
        _params = _transfer_params(params)
        self._client.create_load_balancer_https_listener(load_balancer_id=self.load_balancer_id,
                                                         **_params)

    def refresh(self):
        result = self._client.describe_load_balancers(load_balancer_id=self.load_balancer_id)
        items = _new_get_key_in_response(result, 'LoadBalancers.LoadBalancer')
        if not items:
            raise ClientException(msg=
                                  "Failed to find load_balancer data from DescribeLoadBalancers response. "
                                  "LoadBalancerId = {0}".format(self.load_balancer_id))
        self._assign_attributes(items[0])


class _SLBMasterSlaveServerGroupResource(ServiceResource):

    def __init__(self, master_slave_server_group_id, _client=None):
        ServiceResource.__init__(self, "slb.master_slave_server_group", _client=_client)
        self.master_slave_server_group_id = master_slave_server_group_id

        self.associated_objects = None
        self.master_slave_server_group_name = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_master_slave_server_group(
            master_slave_server_group_id=self.master_slave_server_group_id, **_params)

    def describe_master_slave_server_group_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_master_slave_server_group_attribute(
            master_slave_server_group_id=self.master_slave_server_group_id, **_params)


class _SLBMasterSlaveVServerGroupResource(ServiceResource):

    def __init__(self, master_slave_vserver_group_id, _client=None):
        ServiceResource.__init__(self, "slb.master_slave_vserver_group", _client=_client)
        self.master_slave_vserver_group_id = master_slave_vserver_group_id

        self.master_slave_vserver_group_name = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_master_slave_vserver_group(
            master_slave_vserver_group_id=self.master_slave_vserver_group_id, **_params)

    def describe_master_slave_vserver_group_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_master_slave_vserver_group_attribute(
            master_slave_vserver_group_id=self.master_slave_vserver_group_id, **_params)


class _SLBRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "slb.region", _client=_client)
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


class _SLBRuleResource(ServiceResource):

    def __init__(self, rule_id, _client=None):
        ServiceResource.__init__(self, "slb.rule", _client=_client)
        self.rule_id = rule_id

        self.cookie = None
        self.cookie_timeout = None
        self.domain = None
        self.health_check = None
        self.health_check_connect_port = None
        self.health_check_domain = None
        self.health_check_http_code = None
        self.health_check_interval = None
        self.health_check_timeout = None
        self.health_check_uri = None
        self.healthy_threshold = None
        self.listener_sync = None
        self.rule_name = None
        self.scheduler = None
        self.sticky_session = None
        self.sticky_session_type = None
        self.unhealthy_threshold = None
        self.url = None
        self.vserver_group_id = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_rules(rule_id=self.rule_id, **_params)

    def describe_rule_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_rule_attribute(rule_id=self.rule_id, **_params)

    def set(self, **params):
        _params = _transfer_params(params)
        self._client.set_rule(rule_id=self.rule_id, **_params)


class _SLBServerCertificateResource(ServiceResource):

    def __init__(self, server_certificate_id, _client=None):
        ServiceResource.__init__(self, "slb.server_certificate", _client=_client)
        self.server_certificate_id = server_certificate_id

        self.ali_cloud_certificate_id = None
        self.ali_cloud_certificate_name = None
        self.common_name = None
        self.create_time = None
        self.create_time_stamp = None
        self.expire_time = None
        self.expire_time_stamp = None
        self.fingerprint = None
        self.is_ali_cloud_certificate = None
        self.region_id = None
        self.region_id_alias = None
        self.resource_group_id = None
        self.server_certificate_name = None
        self.subject_alternative_names = None
        self.tags = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_server_certificate(server_certificate_id=self.server_certificate_id,
                                               **_params)

    def set_server_certificate_name(self, **params):
        _params = _transfer_params(params)
        self._client.set_server_certificate_name(server_certificate_id=self.server_certificate_id,
                                                 **_params)

    def refresh(self):
        result = self._client.describe_server_certificates(
            server_certificate_id=self.server_certificate_id)
        items = _new_get_key_in_response(result, 'ServerCertificates.ServerCertificate')
        if not items:
            raise ClientException(msg=
                                  "Failed to find server_certificate data from DescribeServerCertificates response. "
                                  "ServerCertificateId = {0}".format(self.server_certificate_id))
        self._assign_attributes(items[0])


class _SLBVServerGroupResource(ServiceResource):

    def __init__(self, vserver_group_id, _client=None):
        ServiceResource.__init__(self, "slb.vserver_group", _client=_client)
        self.vserver_group_id = vserver_group_id

        self.associated_objects = None
        self.vserver_group_name = None

    def add_vserver_group_backend_servers(self, **params):
        _params = _transfer_params(params)
        self._client.add_vserver_group_backend_servers(vserver_group_id=self.vserver_group_id,
                                                       **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_vserver_group(vserver_group_id=self.vserver_group_id, **_params)

    def describe_vserver_group_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.describe_vserver_group_attribute(vserver_group_id=self.vserver_group_id,
                                                      **_params)

    def modify_backend_servers(self, **params):
        _params = _transfer_params(params)
        self._client.modify_vserver_group_backend_servers(vserver_group_id=self.vserver_group_id,
                                                          **_params)

    def remove_vserver_group_backend_servers(self, **params):
        _params = _transfer_params(params)
        self._client.remove_vserver_group_backend_servers(vserver_group_id=self.vserver_group_id,
                                                          **_params)

    def set_vserver_group_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.set_vserver_group_attribute(vserver_group_id=self.vserver_group_id, **_params)


class _SLBZoneResource(ServiceResource):

    def __init__(self, zone_id, _client=None):
        ServiceResource.__init__(self, "slb.zone", _client=_client)
        self.zone_id = zone_id

        self.available_dedicated_host_types = None
        self.available_disk_categories = None
        self.available_instance_types = None
        self.available_resource_creation = None
        self.available_resources = None
        self.available_volume_categories = None
        self.dedicated_host_generations = None
        self.local_name = None
