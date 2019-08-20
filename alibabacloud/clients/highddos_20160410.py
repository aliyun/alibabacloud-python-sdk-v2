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


class HighDDosClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'HighDDos'
        self.api_version = '2016-04-10'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def upgrade_instance(
            self,
            instance_id=None,
            client_token=None,
            domain_count=None,
            package_code=None,
            business_bandwidth=None,
            owner_id=None):
        api_request = APIRequest('UpgradeInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "ClientToken": client_token,
            "DomainCount": domain_count,
            "PackageCode": package_code,
            "BusinessBandwidth": business_bandwidth,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def renew_instance(
            self,
            duration=None,
            instance_id=None,
            client_token=None,
            owner_id=None,
            pricing_cycle=None):
        api_request = APIRequest('RenewInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "InstanceId": instance_id,
            "ClientToken": client_token,
            "OwnerId": owner_id,
            "PricingCycle": pricing_cycle}
        return self._handle_request(api_request).result

    def release_instance(self, instance_id=None, owner_id=None):
        api_request = APIRequest('ReleaseInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_instance(
            self,
            duration=None,
            is_auto_renew=None,
            base_bandwidth=None,
            client_token=None,
            line=None,
            elastic_bandwidth=None,
            domain_count=None,
            package_code=None,
            business_bandwidth=None,
            owner_id=None,
            pricing_cycle=None,
            auto_renew_duration=None):
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "IsAutoRenew": is_auto_renew,
            "BaseBandwidth": base_bandwidth,
            "ClientToken": client_token,
            "Line": line,
            "ElasticBandwidth": elastic_bandwidth,
            "DomainCount": domain_count,
            "PackageCode": package_code,
            "BusinessBandwidth": business_bandwidth,
            "OwnerId": owner_id,
            "PricingCycle": pricing_cycle,
            "AutoRenewDuration": auto_renew_duration}
        return self._handle_request(api_request).result

    def create_order_instance(
            self,
            duration=None,
            base_bandwidth=None,
            amount=None,
            client_token=None,
            line=None,
            elastic_bandwidth=None,
            order_instance_id=None,
            duration_unit=None,
            commodity_code=None,
            owner_id=None,
            order_type=None):
        api_request = APIRequest('CreateOrderInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "BaseBandwidth": base_bandwidth,
            "Amount": amount,
            "ClientToken": client_token,
            "Line": line,
            "ElasticBandwidth": elastic_bandwidth,
            "OrderInstanceId": order_instance_id,
            "DurationUnit": duration_unit,
            "CommodityCode": commodity_code,
            "OwnerId": owner_id,
            "OrderType": order_type}
        return self._handle_request(api_request).result

    def modify_lay4_rule(self, instance_id=None, vip_port=None, source_ips=None):
        api_request = APIRequest('ModifyLay4Rule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "VipPort": vip_port,
            "SourceIps": source_ips}
        return self._handle_request(api_request).result

    def modify_domain(self, instance_id=None, source_ips=None, domain=None, protocols=None):
        api_request = APIRequest('ModifyDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SourceIps": source_ips,
            "Domain": domain,
            "Protocols": protocols}
        return self._handle_request(api_request).result

    def upload_https_key(self, instance_id=None, domain=None, key=None):
        api_request = APIRequest('UploadHttpsKey', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Domain": domain, "Key": key}
        return self._handle_request(api_request).result

    def upload_https_cert(self, instance_id=None, domain=None, cert=None):
        api_request = APIRequest('UploadHttpsCert', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Domain": domain, "Cert": cert}
        return self._handle_request(api_request).result

    def modify_waf_config(self, instance_id=None, enable=None, domain=None):
        api_request = APIRequest('ModifyWafConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Enable": enable, "Domain": domain}
        return self._handle_request(api_request).result

    def modify_cc_config(self, instance_id=None, enable=None, domain=None):
        api_request = APIRequest('ModifyCcConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Enable": enable, "Domain": domain}
        return self._handle_request(api_request).result

    def describe_waf_attack_url_stats(
            self,
            instance_id=None,
            page_size=None,
            end_time=None,
            domains=None,
            begin_time=None,
            page_number=None):
        api_request = APIRequest('DescribeWafAttackUrlStats', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "Domains": domains,
            "BeginTime": begin_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_waf_attack_type_stats(
            self,
            instance_id=None,
            end_time=None,
            domains=None,
            begin_time=None):
        api_request = APIRequest('DescribeWafAttackTypeStats', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "EndTime": end_time,
            "Domains": domains,
            "BeginTime": begin_time}
        return self._handle_request(api_request).result

    def describe_waf_attack_source_stats(
            self,
            instance_id=None,
            page_size=None,
            end_time=None,
            domains=None,
            begin_time=None,
            page_number=None):
        api_request = APIRequest('DescribeWafAttackSourceStats', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "Domains": domains,
            "BeginTime": begin_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_waf_attack_events(
            self,
            instance_id=None,
            page_size=None,
            end_time=None,
            domains=None,
            begin_time=None,
            page_number=None):
        api_request = APIRequest('DescribeWafAttackEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "Domains": domains,
            "BeginTime": begin_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_lay4_rules(self, instance_id=None, page_size=None, page_number=None):
        api_request = APIRequest('DescribeLay4Rules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_domains(self, instance_id=None, domain=None, page_size=None, page_number=None):
        api_request = APIRequest('DescribeDomains', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Domain": domain,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_ddos_flow(self, instance_id=None, end_time=None, begin_time=None):
        api_request = APIRequest('DescribeDdosFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "EndTime": end_time,
            "BeginTime": begin_time}
        return self._handle_request(api_request).result

    def describe_ddos_events(
            self,
            instance_id=None,
            page_size=None,
            end_time=None,
            begin_time=None,
            page_number=None):
        api_request = APIRequest('DescribeDdosEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "BeginTime": begin_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_cc_flow(self, instance_id=None, end_time=None, domains=None, begin_time=None):
        api_request = APIRequest('DescribeCcFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "EndTime": end_time,
            "Domains": domains,
            "BeginTime": begin_time}
        return self._handle_request(api_request).result

    def describe_cc_events(
            self,
            instance_id=None,
            page_size=None,
            end_time=None,
            domains=None,
            begin_time=None,
            page_number=None):
        api_request = APIRequest('DescribeCcEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "Domains": domains,
            "BeginTime": begin_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_lay4_rule(self, instance_id=None, vip_port=None):
        api_request = APIRequest('DeleteLay4Rule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "VipPort": vip_port}
        return self._handle_request(api_request).result

    def delete_domain(self, instance_id=None, domain=None):
        api_request = APIRequest('DeleteDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Domain": domain}
        return self._handle_request(api_request).result

    def create_lay4_rule(
            self,
            source_port=None,
            instance_id=None,
            vip_port=None,
            source_ips=None,
            protocol_type=None):
        api_request = APIRequest('CreateLay4Rule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourcePort": source_port,
            "InstanceId": instance_id,
            "VipPort": vip_port,
            "SourceIps": source_ips,
            "ProtocolType": protocol_type}
        return self._handle_request(api_request).result

    def create_domain(
            self,
            cc_enable=None,
            instance_id=None,
            source_ips=None,
            domain=None,
            protocols=None,
            waf_enable=None):
        api_request = APIRequest('CreateDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CcEnable": cc_enable,
            "InstanceId": instance_id,
            "SourceIps": source_ips,
            "Domain": domain,
            "Protocols": protocols,
            "WafEnable": waf_enable}
        return self._handle_request(api_request).result
