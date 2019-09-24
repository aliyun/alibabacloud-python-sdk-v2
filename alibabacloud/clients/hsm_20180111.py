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


class HsmClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'hsm'
        self.api_version = '2018-01-11'
        self.location_service_code = 'hsm'
        self.location_endpoint_type = 'openAPI'

    def renew_instance(
            self,
            period=None,
            period_unit=None,
            resource_owner_id=None,
            instance_id=None,
            client_token=None):
        api_request = APIRequest('RenewInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "PeriodUnit": period_unit,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ClientToken": client_token}
        return self._handle_request(api_request).result

    def release_instance(self, resource_owner_id=None, instance_id=None):
        api_request = APIRequest('ReleaseInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def modify_instance(
            self,
            resource_owner_id=None,
            instance_id=None,
            source_ip=None,
            remark=None):
        api_request = APIRequest('ModifyInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SourceIp": source_ip,
            "Remark": remark}
        return self._handle_request(api_request).result

    def describe_regions(self, resource_owner_id=None, source_ip=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_instances(
            self,
            resource_owner_id=None,
            instance_id=None,
            source_ip=None,
            page_size=None,
            current_page=None,
            hsm_status=None):
        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "HsmStatus": hsm_status}
        return self._handle_request(api_request).result

    def create_instance(
            self,
            period=None,
            period_unit=None,
            resource_owner_id=None,
            quantity=None,
            hsm_device_type=None,
            client_token=None,
            zone_id=None,
            hsm_oem=None):
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "PeriodUnit": period_unit,
            "ResourceOwnerId": resource_owner_id,
            "Quantity": quantity,
            "HsmDeviceType": hsm_device_type,
            "ClientToken": client_token,
            "ZoneId": zone_id,
            "HsmOem": hsm_oem}
        return self._handle_request(api_request).result

    def config_white_list(
            self,
            resource_owner_id=None,
            instance_id=None,
            source_ip=None,
            white_list=None):
        api_request = APIRequest('ConfigWhiteList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SourceIp": source_ip,
            "WhiteList": white_list}
        return self._handle_request(api_request).result

    def config_network(
            self,
            vswitch_id=None,
            resource_owner_id=None,
            instance_id=None,
            source_ip=None,
            vpc_id=None,
            ip=None):
        api_request = APIRequest('ConfigNetwork', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "SourceIp": source_ip,
            "VpcId": vpc_id,
            "Ip": ip}
        return self._handle_request(api_request).result
