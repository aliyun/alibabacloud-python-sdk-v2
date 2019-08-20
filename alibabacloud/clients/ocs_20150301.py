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


class OcsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Ocs'
        self.api_version = '2015-03-01'
        self.location_service_code = 'ocs'
        self.location_endpoint_type = 'openAPI'

    def modify_network_type(
            self,
            vswitch_id=None,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            vpc_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyNetworkType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "VpcId": vpc_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_hot_key_switch_mode(
            self,
            expire_time=None,
            resource_owner_id=None,
            instance_id=None,
            key_number=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            switch_mode=None):
        api_request = APIRequest('ModifyHotKeySwitchMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ExpireTime": expire_time,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "KeyNumber": key_number,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "SwitchMode": switch_mode}
        return self._handle_request(api_request).result

    def describe_zones(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            zone_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeZones', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ZoneId": zone_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def activate_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ActivateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_authentic_ip(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            authentic_ip=None,
            owner_id=None):
        api_request = APIRequest('AddAuthenticIP', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AuthenticIP": authentic_ip,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_instance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            network_type=None,
            owner_id=None,
            capacity=None,
            token=None,
            vswitch_id=None,
            private_ip_address=None,
            password=None,
            instance_name=None,
            security_token=None,
            vpc_id=None,
            zone_id=None):
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "NetworkType": network_type,
            "OwnerId": owner_id,
            "Capacity": capacity,
            "Token": token,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "Password": password,
            "InstanceName": instance_name,
            "SecurityToken": security_token,
            "VpcId": vpc_id,
            "ZoneId": zone_id}
        return self._handle_request(api_request).result

    def deactivate_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeactivateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instances(
            self,
            resource_owner_id=None,
            instance_status=None,
            private_ip_addresses=None,
            resource_owner_account=None,
            owner_account=None,
            network_type=None,
            owner_id=None,
            page_number=None,
            vswitch_id=None,
            security_token=None,
            instance_ids=None,
            vpc_id=None,
            page_size=None):
        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceStatus": instance_status,
            "PrivateIpAddresses": private_ip_addresses,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "NetworkType": network_type,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "VSwitchId": vswitch_id,
            "SecurityToken": security_token,
            "InstanceIds": instance_ids,
            "VpcId": vpc_id,
            "PageSize": page_size}
        return self._handle_request(api_request).result

    def describe_history_monitor_values(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            instance_id=None,
            security_token=None,
            interval_for_history=None,
            monitor_keys=None):
        api_request = APIRequest('DescribeHistoryMonitorValues', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "IntervalForHistory": interval_for_history,
            "MonitorKeys": monitor_keys}
        return self._handle_request(api_request).result

    def describe_authentic_ip(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeAuthenticIP', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_security_ips(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeSecurityIps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_regions(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_monitor_values(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            instance_ids=None,
            owner_account=None,
            owner_id=None,
            monitor_keys=None):
        api_request = APIRequest('DescribeMonitorValues', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "InstanceIds": instance_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "MonitorKeys": monitor_keys}
        return self._handle_request(api_request).result

    def describe_monitor_items(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeMonitorItems', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_security_ips(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            security_ips=None,
            owner_id=None):
        api_request = APIRequest('ModifySecurityIps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SecurityIps": security_ips,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_instance_capacity(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            capacity=None):
        api_request = APIRequest('ModifyInstanceCapacity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Capacity": capacity}
        return self._handle_request(api_request).result

    def modify_instance_attribute(
            self,
            resource_owner_id=None,
            instance_id=None,
            instance_name=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            new_password=None):
        api_request = APIRequest('ModifyInstanceAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "InstanceName": instance_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "NewPassword": new_password}
        return self._handle_request(api_request).result

    def flush_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('FlushInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def verify_password(
            self,
            resource_owner_id=None,
            password=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('VerifyPassword', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Password": password,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def replace_authentic_ip(
            self,
            new_authentic_ip=None,
            resource_owner_id=None,
            instance_id=None,
            old_authentic_ip=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ReplaceAuthenticIP', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NewAuthenticIP": new_authentic_ip,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "OldAuthenticIP": old_authentic_ip,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def remove_authentic_ip(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            authentic_ip=None,
            owner_id=None):
        api_request = APIRequest('RemoveAuthenticIP', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AuthenticIP": authentic_ip,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def data_operate(
            self,
            resource_owner_id=None,
            instance_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            command=None):
        api_request = APIRequest('DataOperate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Command": command}
        return self._handle_request(api_request).result
