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


class EnsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Ens'
        self.api_version = '2017-11-10'
        self.location_service_code = 'ens'
        self.location_endpoint_type = 'openAPI'

    def describe_reserved_resource(self, version=None):
        api_request = APIRequest('DescribeReservedResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Version": version}
        return self._handle_request(api_request).result

    def describe_instance_types(self, version=None):
        api_request = APIRequest('DescribeInstanceTypes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Version": version}
        return self._handle_request(api_request).result

    def modify_image_attribute(self, product=None, image_id=None, image_name=None, version=None):
        api_request = APIRequest('ModifyImageAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "product": product,
            "ImageId": image_id,
            "ImageName": image_name,
            "Version": version}
        return self._handle_request(api_request).result

    def describe_instance_spec(self, version=None):
        api_request = APIRequest('DescribeInstanceSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Version": version}
        return self._handle_request(api_request).result

    def describe_instance_auto_renew_attribute(self, instance_ids=None, version=None):
        api_request = APIRequest('DescribeInstanceAutoRenewAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceIds": instance_ids, "Version": version}
        return self._handle_request(api_request).result

    def describe_available_resource(self, version=None):
        api_request = APIRequest('DescribeAvailableResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Version": version}
        return self._handle_request(api_request).result

    def create_instance(
            self,
            auto_renew_period=None,
            period=None,
            image_id=None,
            quantity=None,
            version=None,
            password=None,
            system_disk_size=None,
            auto_renew=None,
            internet_charge_type=None,
            ens_region_id=None,
            instance_type=None,
            data_disk1_size=None):
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AutoRenewPeriod": auto_renew_period,
            "Period": period,
            "ImageId": image_id,
            "Quantity": quantity,
            "Version": version,
            "Password": password,
            "SystemDisk.Size": system_disk_size,
            "AutoRenew": auto_renew,
            "InternetChargeType": internet_charge_type,
            "EnsRegionId": ens_region_id,
            "InstanceType": instance_type,
            "DataDisk.1.Size": data_disk1_size}
        return self._handle_request(api_request).result

    def describe_image_infos(self, os_type=None, version=None):
        api_request = APIRequest('DescribeImageInfos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OsType": os_type, "Version": version}
        return self._handle_request(api_request).result

    def describe_user_band_width_data(
            self,
            period=None,
            instance_id=None,
            ens_region_id=None,
            end_time=None,
            start_time=None,
            version=None):
        api_request = APIRequest('DescribeUserBandWidthData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "InstanceId": instance_id,
            "EnsRegionId": ens_region_id,
            "EndTime": end_time,
            "StartTime": start_time,
            "Version": version}
        return self._handle_request(api_request).result

    def ens_add_consumer_api(self, version=None):
        api_request = APIRequest('EnsAddConsumerApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Version": version}
        return self._handle_request(api_request).result

    def reboot_instance(self, instance_id=None, version=None, force_stop=None):
        api_request = APIRequest('RebootInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Version": version,
            "ForceStop": force_stop}
        return self._handle_request(api_request).result

    def describe_ens_regions(self, ens_region_id=None, version=None):
        api_request = APIRequest('DescribeEnsRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"EnsRegionId": ens_region_id, "Version": version}
        return self._handle_request(api_request).result

    def start_instance(self, instance_id=None, version=None):
        api_request = APIRequest('StartInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Version": version}
        return self._handle_request(api_request).result

    def describe_instance_monitor_data(
            self,
            period=None,
            instance_id=None,
            end_time=None,
            start_time=None,
            version=None):
        api_request = APIRequest('DescribeInstanceMonitorData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "InstanceId": instance_id,
            "EndTime": end_time,
            "StartTime": start_time,
            "Version": version}
        return self._handle_request(api_request).result

    def describe_instances(
            self,
            image_id=None,
            ens_service_id=None,
            search_key=None,
            version=None,
            page_number=None,
            order_by_params=None,
            instance_id=None,
            instance_name=None,
            instance_ids=None,
            ens_region_id=None,
            page_size=None,
            ens_region_ids=None,
            instance_resource_type=None,
            status=None):
        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageId": image_id,
            "EnsServiceId": ens_service_id,
            "SearchKey": search_key,
            "Version": version,
            "PageNumber": page_number,
            "OrderByParams": order_by_params,
            "InstanceId": instance_id,
            "InstanceName": instance_name,
            "InstanceIds": instance_ids,
            "EnsRegionId": ens_region_id,
            "PageSize": page_size,
            "EnsRegionIds": ens_region_ids,
            "InstanceResourceType": instance_resource_type,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_images(
            self,
            product=None,
            image_id=None,
            image_name=None,
            ens_region_id=None,
            page_size=None,
            version=None,
            page_number=None,
            status=None):
        api_request = APIRequest('DescribeImages', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "product": product,
            "ImageId": image_id,
            "ImageName": image_name,
            "EnsRegionId": ens_region_id,
            "PageSize": page_size,
            "Version": version,
            "PageNumber": page_number,
            "Status": status}
        return self._handle_request(api_request).result

    def stop_instance(self, instance_id=None, version=None, force_stop=None):
        api_request = APIRequest('StopInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Version": version,
            "ForceStop": force_stop}
        return self._handle_request(api_request).result

    def modify_instance_attribute(
            self,
            password=None,
            instance_id=None,
            instance_name=None,
            version=None):
        api_request = APIRequest('ModifyInstanceAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Password": password,
            "InstanceId": instance_id,
            "InstanceName": instance_name,
            "Version": version}
        return self._handle_request(api_request).result
