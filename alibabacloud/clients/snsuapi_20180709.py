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


class SnsuapiClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Snsuapi'
        self.api_version = '2018-07-09'
        self.location_service_code = 'snsuapi'
        self.location_endpoint_type = 'openAPI'

    def mobile_start_speed_up(
            self,
            duration=None,
            resource_owner_id=None,
            resource_owner_account=None,
            ip=None,
            destination_ip_address=None,
            public_ip=None,
            public_port=None,
            owner_id=None,
            token=None):
        api_request = APIRequest('MobileStartSpeedUp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Ip": ip,
            "DestinationIpAddress": destination_ip_address,
            "PublicIp": public_ip,
            "PublicPort": public_port,
            "OwnerId": owner_id,
            "Token": token}
        return self._handle_request(api_request).result

    def mobile_stop_speed_up(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            correlation_id=None,
            owner_id=None):
        api_request = APIRequest('MobileStopSpeedUp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CorrelationId": correlation_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def mobile_status_query(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            correlation_id=None,
            owner_id=None):
        api_request = APIRequest('MobileStatusQuery', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CorrelationId": correlation_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def band_offer_order(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            band_id=None,
            offer_id=None,
            owner_id=None):
        api_request = APIRequest('BandOfferOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "BandId": band_id,
            "OfferId": offer_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def band_start_speed_up(
            self,
            ip_address=None,
            resource_owner_id=None,
            resource_owner_account=None,
            port=None,
            band_id=None,
            owner_id=None,
            target_bandwidth=None,
            band_scene=None,
            direction=None):
        api_request = APIRequest('BandStartSpeedUp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IpAddress": ip_address,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Port": port,
            "BandId": band_id,
            "OwnerId": owner_id,
            "TargetBandwidth": target_bandwidth,
            "BandScene": band_scene,
            "Direction": direction}
        return self._handle_request(api_request).result

    def band_stop_speed_up(
            self,
            ip_address=None,
            resource_owner_id=None,
            resource_owner_account=None,
            port=None,
            band_id=None,
            owner_id=None,
            direction=None):
        api_request = APIRequest('BandStopSpeedUp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IpAddress": ip_address,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Port": port,
            "BandId": band_id,
            "OwnerId": owner_id,
            "Direction": direction}
        return self._handle_request(api_request).result

    def band_precheck(
            self,
            ip_address=None,
            resource_owner_id=None,
            resource_owner_account=None,
            port=None,
            owner_id=None):
        api_request = APIRequest('BandPrecheck', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IpAddress": ip_address,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Port": port,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def band_status_query(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            band_id=None,
            owner_id=None):
        api_request = APIRequest('BandStatusQuery', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "BandId": band_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result
