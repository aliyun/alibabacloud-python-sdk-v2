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


class NetanaClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Netana'
        self.api_version = '2018-10-18'
        self.location_service_code = 'Netana'
        self.location_endpoint_type = 'openAPI'

    def describe_ipv6_location_and_isp(
            self,
            ip_address=None,
            resource_owner_id=None,
            resource_owner_account=None):
        api_request = APIRequest('DescribeIpv6LocationAndIsp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IpAddress": ip_address,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account}
        return self._handle_request(api_request).result

    def create_network_diagnostic(
            self,
            resource_owner_id=None,
            request_params=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            user_request_id=None,
            type_=None,
            request_api_name=None,
            error_code=None,
            product_type=None,
            response_params=None):
        api_request = APIRequest('CreateNetworkDiagnostic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RequestParams": request_params,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "UserRequestId": user_request_id,
            "Type": type_,
            "RequestApiName": request_api_name,
            "ErrorCode": error_code,
            "ProductType": product_type,
            "ResponseParams": response_params}
        return self._handle_request(api_request).result

    def describe_diagnostic_config(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            product_type=None):
        api_request = APIRequest('DescribeDiagnosticConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ProductType": product_type}
        return self._handle_request(api_request).result

    def describe_ip_location_and_isp(
            self,
            ip_address=None,
            resource_owner_id=None,
            resource_owner_account=None):
        api_request = APIRequest('DescribeIpLocationAndIsp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IpAddress": ip_address,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account}
        return self._handle_request(api_request).result

    def describe_network_analytics_packet_loss(
            self,
            country=None,
            resource_owner_id=None,
            product=None,
            period=None,
            resource_owner_account=None,
            ip=None,
            end_time=None,
            start_time=None,
            page_number=None,
            carrier=None,
            instance_id=None,
            province=None,
            region_id=None,
            internet_charge_type=None,
            grade=None,
            page_size=None,
            direction=None):
        api_request = APIRequest('DescribeNetworkAnalyticsPacketLoss',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "ResourceOwnerId": resource_owner_id,
            "Product": product,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "Ip": ip,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNumber": page_number,
            "Carrier": carrier,
            "InstanceId": instance_id,
            "Province": province,
            "RegionId": region_id,
            "InternetChargeType": internet_charge_type,
            "Grade": grade,
            "PageSize": page_size,
            "Direction": direction}
        return self._handle_request(api_request).result

    def describe_network_analytics_latency(
            self,
            country=None,
            resource_owner_id=None,
            product=None,
            period=None,
            resource_owner_account=None,
            ip=None,
            end_time=None,
            start_time=None,
            page_number=None,
            carrier=None,
            instance_id=None,
            province=None,
            region_id=None,
            internet_charge_type=None,
            grade=None,
            page_size=None):
        api_request = APIRequest('DescribeNetworkAnalyticsLatency', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "ResourceOwnerId": resource_owner_id,
            "Product": product,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "Ip": ip,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNumber": page_number,
            "Carrier": carrier,
            "InstanceId": instance_id,
            "Province": province,
            "RegionId": region_id,
            "InternetChargeType": internet_charge_type,
            "Grade": grade,
            "PageSize": page_size}
        return self._handle_request(api_request).result

    def describe_network_analytics_data_transfer(
            self,
            country=None,
            resource_owner_id=None,
            product=None,
            period=None,
            resource_owner_account=None,
            ip=None,
            end_time=None,
            start_time=None,
            page_number=None,
            carrier=None,
            instance_id=None,
            province=None,
            region_id=None,
            internet_charge_type=None,
            grade=None,
            page_size=None,
            direction=None):
        api_request = APIRequest('DescribeNetworkAnalyticsDataTransfer',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "ResourceOwnerId": resource_owner_id,
            "Product": product,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "Ip": ip,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNumber": page_number,
            "Carrier": carrier,
            "InstanceId": instance_id,
            "Province": province,
            "RegionId": region_id,
            "InternetChargeType": internet_charge_type,
            "Grade": grade,
            "PageSize": page_size,
            "Direction": direction}
        return self._handle_request(api_request).result

    def describe_network_analytics_net_quality(
            self,
            country=None,
            resource_owner_id=None,
            period=None,
            resource_owner_account=None,
            end_time=None,
            start_time=None,
            page_number=None,
            carrier=None,
            province=None,
            region_id=None,
            grade=None,
            page_size=None):
        api_request = APIRequest('DescribeNetworkAnalyticsNetQuality',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNumber": page_number,
            "Carrier": carrier,
            "Province": province,
            "RegionId": region_id,
            "Grade": grade,
            "PageSize": page_size}
        return self._handle_request(api_request).result

    def describe_network_quotas(
            self,
            resource_owner_id=None,
            product=None,
            quota_publicity_name=None,
            resource_owner_account=None,
            region_id=None,
            resource_type=None):
        api_request = APIRequest('DescribeNetworkQuotas', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Product": product,
            "QuotaPublicityName": quota_publicity_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ResourceType": resource_type}
        return self._handle_request(api_request).result

    def describe_network_quota_request_result(
            self,
            resource_owner_id=None,
            product=None,
            quota_publicity_name=None,
            quota_request_id=None,
            resource_owner_account=None,
            region_id=None,
            page_no=None,
            page_size=None,
            resource_type=None):
        api_request = APIRequest('DescribeNetworkQuotaRequestResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Product": product,
            "QuotaPublicityName": quota_publicity_name,
            "QuotaRequestId": quota_request_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "PageNo": page_no,
            "PageSize": page_size,
            "ResourceType": resource_type}
        return self._handle_request(api_request).result

    def create_network_quota_request(
            self,
            request_reason=None,
            resource_owner_id=None,
            product=None,
            quota_publicity_name=None,
            resource_owner_account=None,
            region_id=None,
            request_quantity=None,
            mobile_phone=None,
            resource_type=None,
            email=None):
        api_request = APIRequest('CreateNetworkQuotaRequest', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RequestReason": request_reason,
            "ResourceOwnerId": resource_owner_id,
            "Product": product,
            "QuotaPublicityName": quota_publicity_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "RequestQuantity": request_quantity,
            "MobilePhone": mobile_phone,
            "ResourceType": resource_type,
            "Email": email}
        return self._handle_request(api_request).result
