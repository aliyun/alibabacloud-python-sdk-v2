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
from alibabacloud.utils import _do_request, _get_response, _assert_is_not_none
import alibabacloud.errors as errors
from aliyunsdkcore.acs_exception.exceptions import ClientException


from aliyunsdkvpc.request.v20160428.DescribeEipAddressesRequest import DescribeEipAddressesRequest
from aliyunsdkvpc.request.v20160428.AllocateEipAddressRequest import AllocateEipAddressRequest
from aliyunsdkvpc.request.v20160428.ReleaseEipAddressRequest import ReleaseEipAddressRequest
from aliyunsdkvpc.request.v20160428.AssociateEipAddressRequest import AssociateEipAddressRequest
from aliyunsdkvpc.request.v20160428.UnassociateEipAddressRequest import UnassociateEipAddressRequest
from aliyunsdkvpc.request.v20160428.ModifyEipAddressAttributeRequest \
    import ModifyEipAddressAttributeRequest


class VPCEipAddressResource(ServiceResource):

    def __init__(self, allocation_id, _client=None):
        ServiceResource.__init__(self, 'vpc.eip_address', _client=_client)
        self.allocation_id = allocation_id

    def release(self):
        request = ReleaseEipAddressRequest()
        request.set_AllocationId(self.allocation_id)
        _do_request(self._client, request, {})

    def associate(self, **params):
        request = AssociateEipAddressRequest()
        request.set_AllocationId(self.allocation_id)
        _do_request(self._client, request, params)

    def unassociate(self, **params):
        request = UnassociateEipAddressRequest()
        request.set_AllocationId(self.allocation_id)
        _do_request(self._client, request, params)

    def modify_attributes(self, **params):
        request = ModifyEipAddressAttributeRequest()
        request.set_InstanceId(self.allocation_id)
        _do_request(self._client, request, params)
        self.refresh()

    def refresh(self):
        request = DescribeEipAddressesRequest()
        request.set_AllocationId(self.allocation_id)
        items = _get_response(self._client, request, {}, 'EipAddresses.EipAddress')
        if not items:
            raise ClientException(errors.ERROR_INVALID_SERVER_RESPONSE,
                                  "Failed to find EIP Address data from DescribeEipAddresses "
                                  "response. "
                                  "AllocationId = {0}".format(self.allocation_id))
        self._assign_attributes(items[0])


class VPCResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'vpc', _client=_client)
        self.eip_addresses = _create_resource_collection(
            VPCEipAddressResource, _client, DescribeEipAddressesRequest,
            'EipAddresses.EipAddress', 'AllocationId'
        )

    def allocate_eip_address(self, **params):
        request = AllocateEipAddressRequest()
        allocate_id = _get_response(self._client, request, params, key='AllocationId')
        return VPCEipAddressResource(allocate_id, _client=self._client)
