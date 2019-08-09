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
from alibabacloud.resources.collection import _create_resource_collection
from alibabacloud.utils.utils import _transfer_params, _new_get_key_in_response
from alibabacloud.exceptions import ClientException


class VPCEipAddressResource(ServiceResource):

    def __init__(self, allocation_id, _client=None):
        ServiceResource.__init__(self, 'vpc.eip_address', _client=_client)
        self.allocation_id = allocation_id

    def release(self):
        self._client.release_eip_address(allocation_id=self.allocation_id)

    def associate(self, **params):
        _params = _transfer_params(params)
        self._client.associate_eip_address(allocation_id=self.allocation_id, **_params)

    def unassociate(self, **params):
        _params = _transfer_params(params)
        self._client.unassociate_eip_address(allocation_id=self.allocation_id, **_params)

    def modify_attributes(self, **params):
        _params = _transfer_params(params)
        self._client.modify_eip_address_attribute(allocation_id=self.allocation_id, **_params)
        self.refresh()
    @transfer({"Tags": "list_of_tags"})
    def refresh(self):
        response = self._client.describe_eip_addresses(allocation_id=self.allocation_id)
        items = _new_get_key_in_response(response, 'EipAddresses.EipAddress')
        if not items:
            raise ClientException(msg=
                                  "Failed to find EIP Address data from DescribeEipAddresses "
                                  "response. "
                                  "AllocationId = {0}".format(self.allocation_id))
        self._assign_attributes(items[0])


class VPCResource(ServiceResource):
    """
    VPC 资源类

    :param _client:  Alibaba Cloud Client
    :type _client: alibaba.client.AlibabaCloudClient

    """

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'vpc', _client=_client)
        self.eip_addresses = _create_resource_collection(
            VPCEipAddressResource, _client, _client.describe_eip_addresses,
            'EipAddresses.EipAddress', 'AllocationId',
            param_aliases={"Tags": "list_of_tags"}
        )

    def allocate_eip_address(self, **params):
        _params = _transfer_params(params)
        response = self._client.allocate_eip_address(**_params)
        allocate_id = _new_get_key_in_response(response, 'AllocationId')
        return VPCEipAddressResource(allocate_id, _client=self._client)
