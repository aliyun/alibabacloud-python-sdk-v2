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


class SlbClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Slb'
        self.api_version = '2014-05-15'
        self.location_service_code = 'slb'
        self.location_endpoint_type = 'openAPI'

    def set_load_balancer_delete_protection(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            delete_protection=None,
            tags=None):
        api_request = APIRequest('SetLoadBalancerDeleteProtection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "DeleteProtection": delete_protection,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_available_resource(
            self,
            access_key_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            address_type=None,
            owner_id=None,
            address_ip_version=None):
        api_request = APIRequest('DescribeAvailableResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "AddressType": address_type,
            "OwnerId": owner_id,
            "AddressIPVersion": address_ip_version}
        return self._handle_request(api_request).result

    def set_domain_extension_attribute(
            self,
            access_key_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            server_certificate_id=None,
            tags=None,
            domain_extension_id=None):
        api_request = APIRequest('SetDomainExtensionAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ServerCertificateId": server_certificate_id,
            "Tags": tags,
            "DomainExtensionId": domain_extension_id}
        return self._handle_request(api_request).result

    def describe_domain_extensions(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None,
            domain_extension_id=None):
        api_request = APIRequest('DescribeDomainExtensions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags,
            "DomainExtensionId": domain_extension_id}
        return self._handle_request(api_request).result

    def delete_domain_extension(
            self,
            access_key_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None,
            domain_extension_id=None):
        api_request = APIRequest('DeleteDomainExtension', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags,
            "DomainExtensionId": domain_extension_id}
        return self._handle_request(api_request).result

    def create_domain_extension(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            domain=None,
            owner_id=None,
            server_certificate_id=None,
            tags=None):
        api_request = APIRequest('CreateDomainExtension', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Domain": domain,
            "OwnerId": owner_id,
            "ServerCertificateId": server_certificate_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def set_access_control_list_attribute(
            self,
            access_key_id=None,
            acl_id=None,
            resource_owner_id=None,
            acl_name=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('SetAccessControlListAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "AclName": acl_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def remove_access_control_list_entry(
            self,
            access_key_id=None,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            acl_entrys=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('RemoveAccessControlListEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "AclEntrys": acl_entrys,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_access_control_lists(
            self,
            access_key_id=None,
            resource_owner_id=None,
            acl_name=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            address_ip_version=None,
            page_number=None,
            tags=None,
            resource_group_id=None,
            region_id=None,
            page_size=None,
            list_of_tag=None):
        api_request = APIRequest('DescribeAccessControlLists', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "AclName": acl_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AddressIPVersion": address_ip_version,
            "PageNumber": page_number,
            "Tags": tags,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "PageSize": page_size,
            "Tag": list_of_tag}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_access_control_list_attribute(
            self,
            access_key_id=None,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            acl_entry_comment=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DescribeAccessControlListAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "AclEntryComment": acl_entry_comment,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def delete_access_control_list(
            self,
            access_key_id=None,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DeleteAccessControlList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def add_access_control_list_entry(
            self,
            access_key_id=None,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            acl_entrys=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('AddAccessControlListEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "AclEntrys": acl_entrys,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def create_access_control_list(
            self,
            access_key_id=None,
            resource_group_id=None,
            resource_owner_id=None,
            acl_name=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            address_ip_version=None,
            tags=None):
        api_request = APIRequest('CreateAccessControlList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceGroupId": resource_group_id,
            "ResourceOwnerId": resource_owner_id,
            "AclName": acl_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AddressIPVersion": address_ip_version,
            "Tags": tags}
        return self._handle_request(api_request).result

    def modify_load_balancer_pay_type(
            self,
            access_key_id=None,
            resource_owner_id=None,
            auto_pay=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            tags=None,
            duration=None,
            load_balancer_id=None,
            region_id=None,
            pay_type=None,
            pricing_cycle=None):
        api_request = APIRequest('ModifyLoadBalancerPayType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags,
            "Duration": duration,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "PayType": pay_type,
            "PricingCycle": pricing_cycle}
        return self._handle_request(api_request).result

    def modify_load_balancer_instance_spec(
            self,
            access_key_id=None,
            load_balancer_spec=None,
            resource_owner_id=None,
            load_balancer_id=None,
            auto_pay=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('ModifyLoadBalancerInstanceSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "LoadBalancerSpec": load_balancer_spec,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "AutoPay": auto_pay,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_master_slave_server_groups(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            include_listener=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DescribeMasterSlaveServerGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "IncludeListener": include_listener,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_master_slave_server_group_attribute(
            self,
            access_key_id=None,
            resource_owner_id=None,
            master_slave_server_group_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest(
            'DescribeMasterSlaveServerGroupAttribute',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "MasterSlaveServerGroupId": master_slave_server_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def delete_master_slave_server_group(
            self,
            access_key_id=None,
            resource_owner_id=None,
            master_slave_server_group_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DeleteMasterSlaveServerGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "MasterSlaveServerGroupId": master_slave_server_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def create_master_slave_server_group(
            self,
            access_key_id=None,
            resource_owner_id=None,
            master_slave_backend_servers=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            master_slave_server_group_name=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('CreateMasterSlaveServerGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "MasterSlaveBackendServers": master_slave_backend_servers,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "MasterSlaveServerGroupName": master_slave_server_group_name,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_master_slave_vserver_groups(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DescribeMasterSlaveVServerGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_master_slave_vserver_group_attribute(
            self,
            access_key_id=None,
            resource_owner_id=None,
            master_slave_vserver_group_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest(
            'DescribeMasterSlaveVServerGroupAttribute',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "MasterSlaveVServerGroupId": master_slave_vserver_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def delete_master_slave_vserver_group(
            self,
            access_key_id=None,
            resource_owner_id=None,
            master_slave_vserver_group_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DeleteMasterSlaveVServerGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "MasterSlaveVServerGroupId": master_slave_vserver_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def create_master_slave_vserver_group(
            self,
            access_key_id=None,
            resource_owner_id=None,
            master_slave_backend_servers=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            master_slave_vserver_group_name=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('CreateMasterSlaveVServerGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "MasterSlaveBackendServers": master_slave_backend_servers,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "MasterSlaveVServerGroupName": master_slave_vserver_group_name,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def upload_ca_certificate(
            self,
            access_key_id=None,
            resource_group_id=None,
            resource_owner_id=None,
            ca_certificate=None,
            ca_certificate_name=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('UploadCACertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceGroupId": resource_group_id,
            "ResourceOwnerId": resource_owner_id,
            "CACertificate": ca_certificate,
            "CACertificateName": ca_certificate_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_ca_certificate_name(
            self,
            access_key_id=None,
            resource_owner_id=None,
            ca_certificate_name=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            ca_certificate_id=None):
        api_request = APIRequest('SetCACertificateName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "CACertificateName": ca_certificate_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "CACertificateId": ca_certificate_id}
        return self._handle_request(api_request).result

    def describe_ca_certificates(
            self,
            access_key_id=None,
            resource_group_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            list_of_tag=None,
            owner_id=None,
            ca_certificate_id=None):
        api_request = APIRequest('DescribeCACertificates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceGroupId": resource_group_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "CACertificateId": ca_certificate_id}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_ca_certificate(
            self,
            access_key_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            ca_certificate_id=None):
        api_request = APIRequest('DeleteCACertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "CACertificateId": ca_certificate_id}
        return self._handle_request(api_request).result

    def remove_tags(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('RemoveTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_tags(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            distinct_key=None,
            owner_id=None,
            page_number=None,
            tags=None):
        api_request = APIRequest('DescribeTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "DistinctKey": distinct_key,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "Tags": tags}
        return self._handle_request(api_request).result

    def add_tags(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('AddTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def set_vserver_group_attribute(
            self,
            access_key_id=None,
            vserver_group_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            backend_servers=None,
            tags=None,
            vserver_group_name=None):
        api_request = APIRequest('SetVServerGroupAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "VServerGroupId": vserver_group_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "BackendServers": backend_servers,
            "Tags": tags,
            "VServerGroupName": vserver_group_name}
        return self._handle_request(api_request).result

    def set_rule(
            self,
            access_key_id=None,
            resource_owner_id=None,
            health_check_timeout=None,
            health_check_uri=None,
            rule_name=None,
            unhealthy_threshold=None,
            healthy_threshold=None,
            scheduler=None,
            health_check=None,
            region_id=None,
            listener_sync=None,
            cookie_timeout=None,
            sticky_session_type=None,
            vserver_group_id=None,
            cookie=None,
            resource_owner_account=None,
            sticky_session=None,
            health_check_domain=None,
            owner_account=None,
            owner_id=None,
            tags=None,
            health_check_interval=None,
            rule_id=None,
            health_check_connect_port=None,
            health_check_http_code=None):
        api_request = APIRequest('SetRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "HealthCheckTimeout": health_check_timeout,
            "HealthCheckURI": health_check_uri,
            "RuleName": rule_name,
            "UnhealthyThreshold": unhealthy_threshold,
            "HealthyThreshold": healthy_threshold,
            "Scheduler": scheduler,
            "HealthCheck": health_check,
            "RegionId": region_id,
            "ListenerSync": listener_sync,
            "CookieTimeout": cookie_timeout,
            "StickySessionType": sticky_session_type,
            "VServerGroupId": vserver_group_id,
            "Cookie": cookie,
            "ResourceOwnerAccount": resource_owner_account,
            "StickySession": sticky_session,
            "HealthCheckDomain": health_check_domain,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags,
            "HealthCheckInterval": health_check_interval,
            "RuleId": rule_id,
            "HealthCheckConnectPort": health_check_connect_port,
            "HealthCheckHttpCode": health_check_http_code}
        return self._handle_request(api_request).result

    def remove_vserver_group_backend_servers(
            self,
            access_key_id=None,
            vserver_group_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            backend_servers=None,
            tags=None):
        api_request = APIRequest('RemoveVServerGroupBackendServers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "VServerGroupId": vserver_group_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "BackendServers": backend_servers,
            "Tags": tags}
        return self._handle_request(api_request).result

    def modify_vserver_group_backend_servers(
            self,
            access_key_id=None,
            vserver_group_id=None,
            resource_owner_id=None,
            old_backend_servers=None,
            resource_owner_account=None,
            region_id=None,
            new_backend_servers=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('ModifyVServerGroupBackendServers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "VServerGroupId": vserver_group_id,
            "ResourceOwnerId": resource_owner_id,
            "OldBackendServers": old_backend_servers,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NewBackendServers": new_backend_servers,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_vserver_groups(
            self,
            access_key_id=None,
            include_rule=None,
            resource_owner_id=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            include_listener=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DescribeVServerGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "IncludeRule": include_rule,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "IncludeListener": include_listener,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_vserver_group_attribute(
            self,
            access_key_id=None,
            vserver_group_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DescribeVServerGroupAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "VServerGroupId": vserver_group_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_rules(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            listener_protocol=None,
            tags=None):
        api_request = APIRequest('DescribeRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ListenerProtocol": listener_protocol,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_rule_attribute(
            self,
            access_key_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            rule_id=None,
            tags=None):
        api_request = APIRequest('DescribeRuleAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "RuleId": rule_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def delete_vserver_group(
            self,
            access_key_id=None,
            vserver_group_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DeleteVServerGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "VServerGroupId": vserver_group_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def delete_rules(
            self,
            access_key_id=None,
            resource_owner_id=None,
            rule_ids=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DeleteRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "RuleIds": rule_ids,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def create_vserver_group(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            backend_servers=None,
            tags=None,
            vserver_group_name=None):
        api_request = APIRequest('CreateVServerGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "BackendServers": backend_servers,
            "Tags": tags,
            "VServerGroupName": vserver_group_name}
        return self._handle_request(api_request).result

    def create_rules(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            rule_list=None,
            owner_account=None,
            owner_id=None,
            listener_protocol=None,
            tags=None):
        api_request = APIRequest('CreateRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "RuleList": rule_list,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ListenerProtocol": listener_protocol,
            "Tags": tags}
        return self._handle_request(api_request).result

    def add_vserver_group_backend_servers(
            self,
            access_key_id=None,
            vserver_group_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            backend_servers=None,
            tags=None):
        api_request = APIRequest('AddVServerGroupBackendServers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "VServerGroupId": vserver_group_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "BackendServers": backend_servers,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_zones(
            self,
            access_key_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DescribeZones', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def set_load_balancer_udp_listener_attribute(
            self,
            access_key_id=None,
            health_check_connect_timeout=None,
            resource_owner_id=None,
            description=None,
            unhealthy_threshold=None,
            healthy_threshold=None,
            acl_status=None,
            scheduler=None,
            acl_type=None,
            master_slave_server_group=None,
            max_connection=None,
            region_id=None,
            persistence_timeout=None,
            vpc_ids=None,
            vserver_group_id=None,
            acl_id=None,
            listener_port=None,
            resource_owner_account=None,
            bandwidth=None,
            owner_account=None,
            owner_id=None,
            tags=None,
            load_balancer_id=None,
            master_slave_server_group_id=None,
            health_check_req=None,
            health_check_interval=None,
            health_check_exp=None,
            health_check_connect_port=None,
            vserver_group=None):
        api_request = APIRequest('SetLoadBalancerUDPListenerAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "HealthCheckConnectTimeout": health_check_connect_timeout,
            "ResourceOwnerId": resource_owner_id,
            "Description": description,
            "UnhealthyThreshold": unhealthy_threshold,
            "HealthyThreshold": healthy_threshold,
            "AclStatus": acl_status,
            "Scheduler": scheduler,
            "AclType": acl_type,
            "MasterSlaveServerGroup": master_slave_server_group,
            "MaxConnection": max_connection,
            "RegionId": region_id,
            "PersistenceTimeout": persistence_timeout,
            "VpcIds": vpc_ids,
            "VServerGroupId": vserver_group_id,
            "AclId": acl_id,
            "ListenerPort": listener_port,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags,
            "LoadBalancerId": load_balancer_id,
            "MasterSlaveServerGroupId": master_slave_server_group_id,
            "healthCheckReq": health_check_req,
            "HealthCheckInterval": health_check_interval,
            "healthCheckExp": health_check_exp,
            "HealthCheckConnectPort": health_check_connect_port,
            "VServerGroup": vserver_group}
        return self._handle_request(api_request).result

    def describe_load_balancer_udp_listener_attribute(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest(
            'DescribeLoadBalancerUDPListenerAttribute',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def create_load_balancer_udp_listener(
            self,
            access_key_id=None,
            health_check_connect_timeout=None,
            resource_owner_id=None,
            description=None,
            unhealthy_threshold=None,
            healthy_threshold=None,
            acl_status=None,
            scheduler=None,
            acl_type=None,
            max_connection=None,
            region_id=None,
            persistence_timeout=None,
            vpc_ids=None,
            vserver_group_id=None,
            acl_id=None,
            listener_port=None,
            resource_owner_account=None,
            bandwidth=None,
            owner_account=None,
            owner_id=None,
            tags=None,
            load_balancer_id=None,
            master_slave_server_group_id=None,
            health_check_req=None,
            backend_server_port=None,
            health_check_interval=None,
            health_check_exp=None,
            health_check_connect_port=None):
        api_request = APIRequest('CreateLoadBalancerUDPListener', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "HealthCheckConnectTimeout": health_check_connect_timeout,
            "ResourceOwnerId": resource_owner_id,
            "Description": description,
            "UnhealthyThreshold": unhealthy_threshold,
            "HealthyThreshold": healthy_threshold,
            "AclStatus": acl_status,
            "Scheduler": scheduler,
            "AclType": acl_type,
            "MaxConnection": max_connection,
            "RegionId": region_id,
            "PersistenceTimeout": persistence_timeout,
            "VpcIds": vpc_ids,
            "VServerGroupId": vserver_group_id,
            "AclId": acl_id,
            "ListenerPort": listener_port,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags,
            "LoadBalancerId": load_balancer_id,
            "MasterSlaveServerGroupId": master_slave_server_group_id,
            "healthCheckReq": health_check_req,
            "BackendServerPort": backend_server_port,
            "healthCheckInterval": health_check_interval,
            "healthCheckExp": health_check_exp,
            "HealthCheckConnectPort": health_check_connect_port}
        return self._handle_request(api_request).result

    def upload_server_certificate(
            self,
            access_key_id=None,
            resource_owner_id=None,
            server_certificate=None,
            resource_owner_account=None,
            owner_account=None,
            ali_cloud_certificate_name=None,
            ali_cloud_certificate_id=None,
            owner_id=None,
            tags=None,
            private_key=None,
            resource_group_id=None,
            region_id=None,
            server_certificate_name=None):
        api_request = APIRequest('UploadServerCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ServerCertificate": server_certificate,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AliCloudCertificateName": ali_cloud_certificate_name,
            "AliCloudCertificateId": ali_cloud_certificate_id,
            "OwnerId": owner_id,
            "Tags": tags,
            "PrivateKey": private_key,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "ServerCertificateName": server_certificate_name}
        return self._handle_request(api_request).result

    def stop_load_balancer_listener(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            listener_protocol=None,
            tags=None):
        api_request = APIRequest('StopLoadBalancerListener', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ListenerProtocol": listener_protocol,
            "Tags": tags}
        return self._handle_request(api_request).result

    def start_load_balancer_listener(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            listener_protocol=None,
            tags=None):
        api_request = APIRequest('StartLoadBalancerListener', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ListenerProtocol": listener_protocol,
            "Tags": tags}
        return self._handle_request(api_request).result

    def set_server_certificate_name(
            self,
            access_key_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            server_certificate_id=None,
            server_certificate_name=None,
            tags=None):
        api_request = APIRequest('SetServerCertificateName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ServerCertificateId": server_certificate_id,
            "ServerCertificateName": server_certificate_name,
            "Tags": tags}
        return self._handle_request(api_request).result

    def set_load_balancer_tcp_listener_attribute(
            self,
            access_key_id=None,
            health_check_connect_timeout=None,
            resource_owner_id=None,
            health_check_uri=None,
            description=None,
            unhealthy_threshold=None,
            healthy_threshold=None,
            acl_status=None,
            scheduler=None,
            acl_type=None,
            master_slave_server_group=None,
            established_timeout=None,
            max_connection=None,
            region_id=None,
            persistence_timeout=None,
            vpc_ids=None,
            vserver_group_id=None,
            acl_id=None,
            listener_port=None,
            health_check_type=None,
            resource_owner_account=None,
            bandwidth=None,
            health_check_method=None,
            health_check_domain=None,
            owner_account=None,
            syn_proxy=None,
            owner_id=None,
            tags=None,
            load_balancer_id=None,
            master_slave_server_group_id=None,
            health_check_interval=None,
            health_check_connect_port=None,
            health_check_http_code=None,
            vserver_group=None):
        api_request = APIRequest('SetLoadBalancerTCPListenerAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "HealthCheckConnectTimeout": health_check_connect_timeout,
            "ResourceOwnerId": resource_owner_id,
            "HealthCheckURI": health_check_uri,
            "Description": description,
            "UnhealthyThreshold": unhealthy_threshold,
            "HealthyThreshold": healthy_threshold,
            "AclStatus": acl_status,
            "Scheduler": scheduler,
            "AclType": acl_type,
            "MasterSlaveServerGroup": master_slave_server_group,
            "EstablishedTimeout": established_timeout,
            "MaxConnection": max_connection,
            "RegionId": region_id,
            "PersistenceTimeout": persistence_timeout,
            "VpcIds": vpc_ids,
            "VServerGroupId": vserver_group_id,
            "AclId": acl_id,
            "ListenerPort": listener_port,
            "HealthCheckType": health_check_type,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "HealthCheckMethod": health_check_method,
            "HealthCheckDomain": health_check_domain,
            "OwnerAccount": owner_account,
            "SynProxy": syn_proxy,
            "OwnerId": owner_id,
            "Tags": tags,
            "LoadBalancerId": load_balancer_id,
            "MasterSlaveServerGroupId": master_slave_server_group_id,
            "HealthCheckInterval": health_check_interval,
            "HealthCheckConnectPort": health_check_connect_port,
            "HealthCheckHttpCode": health_check_http_code,
            "VServerGroup": vserver_group}
        return self._handle_request(api_request).result

    def set_load_balancer_status(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            load_balancer_status=None,
            tags=None):
        api_request = APIRequest('SetLoadBalancerStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "LoadBalancerStatus": load_balancer_status,
            "Tags": tags}
        return self._handle_request(api_request).result

    def set_load_balancer_name(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_name=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('SetLoadBalancerName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerName": load_balancer_name,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def set_load_balancer_https_listener_attribute(
            self,
            access_key_id=None,
            resource_owner_id=None,
            health_check_timeout=None,
            xforwarded_for=None,
            health_check_uri=None,
            description=None,
            unhealthy_threshold=None,
            healthy_threshold=None,
            acl_status=None,
            scheduler=None,
            acl_type=None,
            health_check=None,
            max_connection=None,
            enable_http2=None,
            region_id=None,
            cookie_timeout=None,
            sticky_session_type=None,
            vpc_ids=None,
            vserver_group_id=None,
            acl_id=None,
            listener_port=None,
            cookie=None,
            health_check_type=None,
            resource_owner_account=None,
            bandwidth=None,
            sticky_session=None,
            health_check_method=None,
            health_check_domain=None,
            request_timeout=None,
            owner_account=None,
            gzip=None,
            tls_cipher_policy=None,
            owner_id=None,
            server_certificate_id=None,
            ca_certificate_id=None,
            backend_protocol=None,
            tags=None,
            idle_timeout=None,
            load_balancer_id=None,
            xforwarded_for__slbip=None,
            health_check_interval=None,
            xforwarded_for_proto=None,
            xforwarded_for__slbid=None,
            health_check_connect_port=None,
            health_check_http_code=None,
            vserver_group=None):
        api_request = APIRequest('SetLoadBalancerHTTPSListenerAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "HealthCheckTimeout": health_check_timeout,
            "XForwardedFor": xforwarded_for,
            "HealthCheckURI": health_check_uri,
            "Description": description,
            "UnhealthyThreshold": unhealthy_threshold,
            "HealthyThreshold": healthy_threshold,
            "AclStatus": acl_status,
            "Scheduler": scheduler,
            "AclType": acl_type,
            "HealthCheck": health_check,
            "MaxConnection": max_connection,
            "EnableHttp2": enable_http2,
            "RegionId": region_id,
            "CookieTimeout": cookie_timeout,
            "StickySessionType": sticky_session_type,
            "VpcIds": vpc_ids,
            "VServerGroupId": vserver_group_id,
            "AclId": acl_id,
            "ListenerPort": listener_port,
            "Cookie": cookie,
            "HealthCheckType": health_check_type,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "StickySession": sticky_session,
            "HealthCheckMethod": health_check_method,
            "HealthCheckDomain": health_check_domain,
            "RequestTimeout": request_timeout,
            "OwnerAccount": owner_account,
            "Gzip": gzip,
            "TLSCipherPolicy": tls_cipher_policy,
            "OwnerId": owner_id,
            "ServerCertificateId": server_certificate_id,
            "CACertificateId": ca_certificate_id,
            "BackendProtocol": backend_protocol,
            "Tags": tags,
            "IdleTimeout": idle_timeout,
            "LoadBalancerId": load_balancer_id,
            "XForwardedFor_SLBIP": xforwarded_for__slbip,
            "HealthCheckInterval": health_check_interval,
            "XForwardedFor_proto": xforwarded_for_proto,
            "XForwardedFor_SLBID": xforwarded_for__slbid,
            "HealthCheckConnectPort": health_check_connect_port,
            "HealthCheckHttpCode": health_check_http_code,
            "VServerGroup": vserver_group}
        return self._handle_request(api_request).result

    def set_load_balancer_http_listener_attribute(
            self,
            access_key_id=None,
            resource_owner_id=None,
            health_check_timeout=None,
            xforwarded_for=None,
            health_check_uri=None,
            description=None,
            unhealthy_threshold=None,
            healthy_threshold=None,
            acl_status=None,
            scheduler=None,
            acl_type=None,
            health_check=None,
            max_connection=None,
            region_id=None,
            cookie_timeout=None,
            sticky_session_type=None,
            vpc_ids=None,
            vserver_group_id=None,
            acl_id=None,
            listener_port=None,
            cookie=None,
            health_check_type=None,
            resource_owner_account=None,
            bandwidth=None,
            sticky_session=None,
            health_check_method=None,
            health_check_domain=None,
            request_timeout=None,
            owner_account=None,
            gzip=None,
            owner_id=None,
            tags=None,
            idle_timeout=None,
            load_balancer_id=None,
            xforwarded_for__slbip=None,
            health_check_interval=None,
            xforwarded_for_proto=None,
            xforwarded_for__slbid=None,
            health_check_connect_port=None,
            health_check_http_code=None,
            vserver_group=None):
        api_request = APIRequest('SetLoadBalancerHTTPListenerAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "HealthCheckTimeout": health_check_timeout,
            "XForwardedFor": xforwarded_for,
            "HealthCheckURI": health_check_uri,
            "Description": description,
            "UnhealthyThreshold": unhealthy_threshold,
            "HealthyThreshold": healthy_threshold,
            "AclStatus": acl_status,
            "Scheduler": scheduler,
            "AclType": acl_type,
            "HealthCheck": health_check,
            "MaxConnection": max_connection,
            "RegionId": region_id,
            "CookieTimeout": cookie_timeout,
            "StickySessionType": sticky_session_type,
            "VpcIds": vpc_ids,
            "VServerGroupId": vserver_group_id,
            "AclId": acl_id,
            "ListenerPort": listener_port,
            "Cookie": cookie,
            "HealthCheckType": health_check_type,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "StickySession": sticky_session,
            "HealthCheckMethod": health_check_method,
            "HealthCheckDomain": health_check_domain,
            "RequestTimeout": request_timeout,
            "OwnerAccount": owner_account,
            "Gzip": gzip,
            "OwnerId": owner_id,
            "Tags": tags,
            "IdleTimeout": idle_timeout,
            "LoadBalancerId": load_balancer_id,
            "XForwardedFor_SLBIP": xforwarded_for__slbip,
            "HealthCheckInterval": health_check_interval,
            "XForwardedFor_proto": xforwarded_for_proto,
            "XForwardedFor_SLBID": xforwarded_for__slbid,
            "HealthCheckConnectPort": health_check_connect_port,
            "HealthCheckHttpCode": health_check_http_code,
            "VServerGroup": vserver_group}
        return self._handle_request(api_request).result

    def set_listener_access_control_status(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            access_control_status=None,
            owner_id=None,
            listener_protocol=None,
            tags=None):
        api_request = APIRequest('SetListenerAccessControlStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AccessControlStatus": access_control_status,
            "OwnerId": owner_id,
            "ListenerProtocol": listener_protocol,
            "Tags": tags}
        return self._handle_request(api_request).result

    def set_backend_servers(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            backend_servers=None,
            tags=None):
        api_request = APIRequest('SetBackendServers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "BackendServers": backend_servers,
            "Tags": tags}
        return self._handle_request(api_request).result

    def remove_listener_white_list_item(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            source_items=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            listener_protocol=None,
            tags=None):
        api_request = APIRequest('RemoveListenerWhiteListItem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "SourceItems": source_items,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ListenerProtocol": listener_protocol,
            "Tags": tags}
        return self._handle_request(api_request).result

    def remove_backend_servers(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            backend_servers=None,
            tags=None):
        api_request = APIRequest('RemoveBackendServers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "BackendServers": backend_servers,
            "Tags": tags}
        return self._handle_request(api_request).result

    def modify_load_balancer_internet_spec(
            self,
            access_key_id=None,
            resource_owner_id=None,
            auto_pay=None,
            resource_owner_account=None,
            bandwidth=None,
            owner_account=None,
            owner_id=None,
            tags=None,
            load_balancer_id=None,
            region_id=None,
            internet_charge_type=None,
            ratio=None):
        api_request = APIRequest('ModifyLoadBalancerInternetSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "InternetChargeType": internet_charge_type,
            "Ratio": ratio}
        return self._handle_request(api_request).result

    def describe_server_certificates(
            self,
            access_key_id=None,
            resource_group_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            list_of_tag=None,
            owner_id=None,
            server_certificate_id=None,
            tags=None):
        api_request = APIRequest('DescribeServerCertificates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceGroupId": resource_group_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "ServerCertificateId": server_certificate_id,
            "Tags": tags}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_regions(
            self,
            access_key_id=None,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            accept_language=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AcceptLanguage": accept_language,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_load_balancer_tcp_listener_attribute(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest(
            'DescribeLoadBalancerTCPListenerAttribute',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_load_balancers(
            self,
            access_key_id=None,
            resource_owner_id=None,
            network_type=None,
            address_ip_version=None,
            master_zone_id=None,
            page_number=None,
            resource_group_id=None,
            load_balancer_name=None,
            region_id=None,
            page_size=None,
            address_type=None,
            slave_zone_id=None,
            list_of_tag=None,
            fuzzy=None,
            address=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            server_id=None,
            load_balancer_status=None,
            tags=None,
            server_intranet_address=None,
            vswitch_id=None,
            load_balancer_id=None,
            internet_charge_type=None,
            vpc_id=None,
            pay_type=None):
        api_request = APIRequest('DescribeLoadBalancers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "NetworkType": network_type,
            "AddressIPVersion": address_ip_version,
            "MasterZoneId": master_zone_id,
            "PageNumber": page_number,
            "ResourceGroupId": resource_group_id,
            "LoadBalancerName": load_balancer_name,
            "RegionId": region_id,
            "PageSize": page_size,
            "AddressType": address_type,
            "SlaveZoneId": slave_zone_id,
            "Tag": list_of_tag,
            "Fuzzy": fuzzy,
            "Address": address,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ServerId": server_id,
            "LoadBalancerStatus": load_balancer_status,
            "Tags": tags,
            "ServerIntranetAddress": server_intranet_address,
            "VSwitchId": vswitch_id,
            "LoadBalancerId": load_balancer_id,
            "InternetChargeType": internet_charge_type,
            "VpcId": vpc_id,
            "PayType": pay_type}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_load_balancer_https_listener_attribute(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest(
            'DescribeLoadBalancerHTTPSListenerAttribute',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_load_balancer_http_listener_attribute(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest(
            'DescribeLoadBalancerHTTPListenerAttribute',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_load_balancer_attribute(
            self,
            access_key_id=None,
            include_reserved_data=None,
            resource_owner_id=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DescribeLoadBalancerAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "IncludeReservedData": include_reserved_data,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_listener_access_control_attribute(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            listener_protocol=None,
            tags=None):
        api_request = APIRequest('DescribeListenerAccessControlAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ListenerProtocol": listener_protocol,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_health_status(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            listener_protocol=None,
            tags=None):
        api_request = APIRequest('DescribeHealthStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ListenerProtocol": listener_protocol,
            "Tags": tags}
        return self._handle_request(api_request).result

    def delete_server_certificate(
            self,
            access_key_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            server_certificate_id=None,
            tags=None):
        api_request = APIRequest('DeleteServerCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ServerCertificateId": server_certificate_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def delete_load_balancer_listener(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            listener_protocol=None,
            tags=None):
        api_request = APIRequest('DeleteLoadBalancerListener', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ListenerProtocol": listener_protocol,
            "Tags": tags}
        return self._handle_request(api_request).result

    def delete_load_balancer(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            tags=None):
        api_request = APIRequest('DeleteLoadBalancer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def create_load_balancer_tcp_listener(
            self,
            access_key_id=None,
            health_check_connect_timeout=None,
            resource_owner_id=None,
            health_check_uri=None,
            description=None,
            unhealthy_threshold=None,
            healthy_threshold=None,
            acl_status=None,
            scheduler=None,
            acl_type=None,
            established_timeout=None,
            max_connection=None,
            region_id=None,
            persistence_timeout=None,
            vpc_ids=None,
            vserver_group_id=None,
            acl_id=None,
            listener_port=None,
            health_check_type=None,
            resource_owner_account=None,
            bandwidth=None,
            health_check_method=None,
            health_check_domain=None,
            owner_account=None,
            owner_id=None,
            tags=None,
            load_balancer_id=None,
            master_slave_server_group_id=None,
            backend_server_port=None,
            health_check_interval=None,
            health_check_connect_port=None,
            health_check_http_code=None):
        api_request = APIRequest('CreateLoadBalancerTCPListener', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "HealthCheckConnectTimeout": health_check_connect_timeout,
            "ResourceOwnerId": resource_owner_id,
            "HealthCheckURI": health_check_uri,
            "Description": description,
            "UnhealthyThreshold": unhealthy_threshold,
            "HealthyThreshold": healthy_threshold,
            "AclStatus": acl_status,
            "Scheduler": scheduler,
            "AclType": acl_type,
            "EstablishedTimeout": established_timeout,
            "MaxConnection": max_connection,
            "RegionId": region_id,
            "PersistenceTimeout": persistence_timeout,
            "VpcIds": vpc_ids,
            "VServerGroupId": vserver_group_id,
            "AclId": acl_id,
            "ListenerPort": listener_port,
            "HealthCheckType": health_check_type,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "HealthCheckMethod": health_check_method,
            "HealthCheckDomain": health_check_domain,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags,
            "LoadBalancerId": load_balancer_id,
            "MasterSlaveServerGroupId": master_slave_server_group_id,
            "BackendServerPort": backend_server_port,
            "healthCheckInterval": health_check_interval,
            "HealthCheckConnectPort": health_check_connect_port,
            "HealthCheckHttpCode": health_check_http_code}
        return self._handle_request(api_request).result

    def create_load_balancer_https_listener(
            self,
            access_key_id=None,
            resource_owner_id=None,
            health_check_timeout=None,
            xforwarded_for=None,
            health_check_uri=None,
            description=None,
            unhealthy_threshold=None,
            healthy_threshold=None,
            acl_status=None,
            scheduler=None,
            acl_type=None,
            health_check=None,
            max_connection=None,
            enable_http2=None,
            region_id=None,
            cookie_timeout=None,
            sticky_session_type=None,
            vpc_ids=None,
            vserver_group_id=None,
            acl_id=None,
            listener_port=None,
            cookie=None,
            health_check_type=None,
            resource_owner_account=None,
            bandwidth=None,
            sticky_session=None,
            health_check_method=None,
            health_check_domain=None,
            request_timeout=None,
            owner_account=None,
            gzip=None,
            tls_cipher_policy=None,
            owner_id=None,
            server_certificate_id=None,
            ca_certificate_id=None,
            backend_protocol=None,
            tags=None,
            idle_timeout=None,
            load_balancer_id=None,
            xforwarded_for__slbip=None,
            backend_server_port=None,
            health_check_interval=None,
            xforwarded_for_proto=None,
            xforwarded_for__slbid=None,
            health_check_connect_port=None,
            health_check_http_code=None):
        api_request = APIRequest('CreateLoadBalancerHTTPSListener', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "HealthCheckTimeout": health_check_timeout,
            "XForwardedFor": xforwarded_for,
            "HealthCheckURI": health_check_uri,
            "Description": description,
            "UnhealthyThreshold": unhealthy_threshold,
            "HealthyThreshold": healthy_threshold,
            "AclStatus": acl_status,
            "Scheduler": scheduler,
            "AclType": acl_type,
            "HealthCheck": health_check,
            "MaxConnection": max_connection,
            "EnableHttp2": enable_http2,
            "RegionId": region_id,
            "CookieTimeout": cookie_timeout,
            "StickySessionType": sticky_session_type,
            "VpcIds": vpc_ids,
            "VServerGroupId": vserver_group_id,
            "AclId": acl_id,
            "ListenerPort": listener_port,
            "Cookie": cookie,
            "HealthCheckType": health_check_type,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "StickySession": sticky_session,
            "HealthCheckMethod": health_check_method,
            "HealthCheckDomain": health_check_domain,
            "RequestTimeout": request_timeout,
            "OwnerAccount": owner_account,
            "Gzip": gzip,
            "TLSCipherPolicy": tls_cipher_policy,
            "OwnerId": owner_id,
            "ServerCertificateId": server_certificate_id,
            "CACertificateId": ca_certificate_id,
            "BackendProtocol": backend_protocol,
            "Tags": tags,
            "IdleTimeout": idle_timeout,
            "LoadBalancerId": load_balancer_id,
            "XForwardedFor_SLBIP": xforwarded_for__slbip,
            "BackendServerPort": backend_server_port,
            "HealthCheckInterval": health_check_interval,
            "XForwardedFor_proto": xforwarded_for_proto,
            "XForwardedFor_SLBID": xforwarded_for__slbid,
            "HealthCheckConnectPort": health_check_connect_port,
            "HealthCheckHttpCode": health_check_http_code}
        return self._handle_request(api_request).result

    def create_load_balancer_http_listener(
            self,
            access_key_id=None,
            resource_owner_id=None,
            health_check_timeout=None,
            listener_forward=None,
            xforwarded_for=None,
            health_check_uri=None,
            description=None,
            unhealthy_threshold=None,
            healthy_threshold=None,
            acl_status=None,
            scheduler=None,
            acl_type=None,
            health_check=None,
            forward_port=None,
            max_connection=None,
            region_id=None,
            cookie_timeout=None,
            sticky_session_type=None,
            vpc_ids=None,
            vserver_group_id=None,
            acl_id=None,
            listener_port=None,
            cookie=None,
            health_check_type=None,
            resource_owner_account=None,
            bandwidth=None,
            sticky_session=None,
            health_check_method=None,
            health_check_domain=None,
            request_timeout=None,
            owner_account=None,
            gzip=None,
            owner_id=None,
            tags=None,
            idle_timeout=None,
            load_balancer_id=None,
            xforwarded_for__slbip=None,
            backend_server_port=None,
            health_check_interval=None,
            xforwarded_for_proto=None,
            xforwarded_for__slbid=None,
            health_check_connect_port=None,
            health_check_http_code=None):
        api_request = APIRequest('CreateLoadBalancerHTTPListener', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "HealthCheckTimeout": health_check_timeout,
            "ListenerForward": listener_forward,
            "XForwardedFor": xforwarded_for,
            "HealthCheckURI": health_check_uri,
            "Description": description,
            "UnhealthyThreshold": unhealthy_threshold,
            "HealthyThreshold": healthy_threshold,
            "AclStatus": acl_status,
            "Scheduler": scheduler,
            "AclType": acl_type,
            "HealthCheck": health_check,
            "ForwardPort": forward_port,
            "MaxConnection": max_connection,
            "RegionId": region_id,
            "CookieTimeout": cookie_timeout,
            "StickySessionType": sticky_session_type,
            "VpcIds": vpc_ids,
            "VServerGroupId": vserver_group_id,
            "AclId": acl_id,
            "ListenerPort": listener_port,
            "Cookie": cookie,
            "HealthCheckType": health_check_type,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "StickySession": sticky_session,
            "HealthCheckMethod": health_check_method,
            "HealthCheckDomain": health_check_domain,
            "RequestTimeout": request_timeout,
            "OwnerAccount": owner_account,
            "Gzip": gzip,
            "OwnerId": owner_id,
            "Tags": tags,
            "IdleTimeout": idle_timeout,
            "LoadBalancerId": load_balancer_id,
            "XForwardedFor_SLBIP": xforwarded_for__slbip,
            "BackendServerPort": backend_server_port,
            "HealthCheckInterval": health_check_interval,
            "XForwardedFor_proto": xforwarded_for_proto,
            "XForwardedFor_SLBID": xforwarded_for__slbid,
            "HealthCheckConnectPort": health_check_connect_port,
            "HealthCheckHttpCode": health_check_http_code}
        return self._handle_request(api_request).result

    def create_load_balancer(
            self,
            access_key_id=None,
            resource_owner_id=None,
            client_token=None,
            address_ip_version=None,
            master_zone_id=None,
            duration=None,
            resource_group_id=None,
            load_balancer_name=None,
            region_id=None,
            address_type=None,
            slave_zone_id=None,
            delete_protection=None,
            load_balancer_spec=None,
            auto_pay=None,
            address=None,
            resource_owner_account=None,
            bandwidth=None,
            owner_account=None,
            owner_id=None,
            tags=None,
            vswitch_id=None,
            enable_vpc_vip_flow=None,
            internet_charge_type=None,
            vpc_id=None,
            pay_type=None,
            pricing_cycle=None,
            ratio=None):
        api_request = APIRequest('CreateLoadBalancer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "AddressIPVersion": address_ip_version,
            "MasterZoneId": master_zone_id,
            "Duration": duration,
            "ResourceGroupId": resource_group_id,
            "LoadBalancerName": load_balancer_name,
            "RegionId": region_id,
            "AddressType": address_type,
            "SlaveZoneId": slave_zone_id,
            "DeleteProtection": delete_protection,
            "LoadBalancerSpec": load_balancer_spec,
            "AutoPay": auto_pay,
            "Address": address,
            "ResourceOwnerAccount": resource_owner_account,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tags": tags,
            "VSwitchId": vswitch_id,
            "EnableVpcVipFlow": enable_vpc_vip_flow,
            "InternetChargeType": internet_charge_type,
            "VpcId": vpc_id,
            "PayType": pay_type,
            "PricingCycle": pricing_cycle,
            "Ratio": ratio}
        return self._handle_request(api_request).result

    def add_listener_white_list_item(
            self,
            access_key_id=None,
            resource_owner_id=None,
            listener_port=None,
            load_balancer_id=None,
            source_items=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            listener_protocol=None,
            tags=None):
        api_request = APIRequest('AddListenerWhiteListItem', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "ListenerPort": listener_port,
            "LoadBalancerId": load_balancer_id,
            "SourceItems": source_items,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ListenerProtocol": listener_protocol,
            "Tags": tags}
        return self._handle_request(api_request).result

    def add_backend_servers(
            self,
            access_key_id=None,
            resource_owner_id=None,
            load_balancer_id=None,
            region_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            backend_servers=None,
            tags=None):
        api_request = APIRequest('AddBackendServers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "LoadBalancerId": load_balancer_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "BackendServers": backend_servers,
            "Tags": tags}
        return self._handle_request(api_request).result
