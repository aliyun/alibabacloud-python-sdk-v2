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


class OtsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Ots'
        self.api_version = '2016-06-20'
        self.location_service_code = 'ots'
        self.location_endpoint_type = 'openAPI'

    def update_instance(
            self,
            access_key_id=None,
            resource_owner_id=None,
            instance_name=None,
            network=None):
        api_request = APIRequest('UpdateInstance', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceName": instance_name,
            "Network": network}
        return self._handle_request(api_request).result

    def unbind_instance2_vpc(
            self,
            access_key_id=None,
            instance_vpc_name=None,
            resource_owner_id=None,
            instance_name=None,
            region_no=None):
        api_request = APIRequest('UnbindInstance2Vpc', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "InstanceVpcName": instance_vpc_name,
            "ResourceOwnerId": resource_owner_id,
            "InstanceName": instance_name,
            "RegionNo": region_no}
        return self._handle_request(api_request).result

    def list_vpc_info_by_vpc(
            self,
            access_key_id=None,
            resource_owner_id=None,
            vpc_id=None,
            page_size=None,
            page_num=None,
            list_of_tag_info=None):
        api_request = APIRequest('ListVpcInfoByVpc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "VpcId": vpc_id,
            "PageSize": page_size,
            "PageNum": page_num,
            "TagInfo": list_of_tag_info}
        repeat_info = {"TagInfo": ('TagInfo', 'list', 'dict', [('TagValue', 'str', None, None),
                                                               ('TagKey', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_vpc_info_by_instance(
            self,
            access_key_id=None,
            resource_owner_id=None,
            instance_name=None,
            page_size=None,
            page_num=None):
        api_request = APIRequest('ListVpcInfoByInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceName": instance_name,
            "PageSize": page_size,
            "PageNum": page_num}
        return self._handle_request(api_request).result

    def list_tags(
            self,
            access_key_id=None,
            resource_owner_id=None,
            instance_name=None,
            page_size=None,
            page_num=None,
            list_of_tag_info=None):
        api_request = APIRequest('ListTags', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceName": instance_name,
            "PageSize": page_size,
            "PageNum": page_num,
            "TagInfo": list_of_tag_info}
        repeat_info = {"TagInfo": ('TagInfo', 'list', 'dict', [('TagValue', 'str', None, None),
                                                               ('TagKey', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_instance(
            self,
            access_key_id=None,
            resource_owner_id=None,
            page_size=None,
            page_num=None,
            list_of_tag_info=None):
        api_request = APIRequest('ListInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "PageSize": page_size,
            "PageNum": page_num,
            "TagInfo": list_of_tag_info}
        repeat_info = {"TagInfo": ('TagInfo', 'list', 'dict', [('TagValue', 'str', None, None),
                                                               ('TagKey', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_cluster_type(self, access_key_id=None, resource_owner_id=None):
        api_request = APIRequest('ListClusterType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"access_key_id": access_key_id, "ResourceOwnerId": resource_owner_id}
        return self._handle_request(api_request).result

    def insert_tags(
            self,
            access_key_id=None,
            resource_owner_id=None,
            instance_name=None,
            list_of_tag_info=None):
        api_request = APIRequest('InsertTags', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceName": instance_name,
            "TagInfo": list_of_tag_info}
        repeat_info = {"TagInfo": ('TagInfo', 'list', 'dict', [('TagValue', 'str', None, None),
                                                               ('TagKey', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def insert_instance(
            self,
            access_key_id=None,
            cluster_type=None,
            resource_owner_id=None,
            instance_name=None,
            description=None,
            list_of_tag_info=None,
            network=None):
        api_request = APIRequest('InsertInstance', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ClusterType": cluster_type,
            "ResourceOwnerId": resource_owner_id,
            "InstanceName": instance_name,
            "Description": description,
            "TagInfo": list_of_tag_info,
            "Network": network}
        repeat_info = {"TagInfo": ('TagInfo', 'list', 'dict', [('TagValue', 'str', None, None),
                                                               ('TagKey', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_instance(self, access_key_id=None, resource_owner_id=None, instance_name=None):
        api_request = APIRequest('GetInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceName": instance_name}
        return self._handle_request(api_request).result

    def delete_tags(
            self,
            access_key_id=None,
            resource_owner_id=None,
            instance_name=None,
            list_of_tag_info=None):
        api_request = APIRequest('DeleteTags', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceName": instance_name,
            "TagInfo": list_of_tag_info}
        repeat_info = {"TagInfo": ('TagInfo', 'list', 'dict', [('TagValue', 'str', None, None),
                                                               ('TagKey', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_instance(self, access_key_id=None, resource_owner_id=None, instance_name=None):
        api_request = APIRequest('DeleteInstance', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "InstanceName": instance_name}
        return self._handle_request(api_request).result

    def bind_instance2_vpc(
            self,
            access_key_id=None,
            instance_vpc_name=None,
            resource_owner_id=None,
            instance_name=None,
            vpc_id=None,
            virtual_switch_id=None,
            region_no=None,
            network=None):
        api_request = APIRequest('BindInstance2Vpc', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "InstanceVpcName": instance_vpc_name,
            "ResourceOwnerId": resource_owner_id,
            "InstanceName": instance_name,
            "VpcId": vpc_id,
            "VirtualSwitchId": virtual_switch_id,
            "RegionNo": region_no,
            "Network": network}
        return self._handle_request(api_request).result
