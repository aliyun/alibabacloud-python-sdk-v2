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
from alibabacloud.exceptions import ClientException
from alibabacloud.resources.collection import _create_resource_collection
from alibabacloud.services._vpc import _VPCResource
from alibabacloud.services._vpc import _VPCEipAddressResource
from alibabacloud.utils.utils import transfer, _new_get_key_in_response


class VPCEipAddressResource(_VPCEipAddressResource):

    def __init__(self, allocation_id, _client=None):
        _VPCEipAddressResource.__init__(self, allocation_id, _client=_client)
        self.allocation_id = allocation_id

    @transfer({"Tags": "list_of_tags"})
    def refresh(self):
        response = self._client.describe_eip_addresses(allocation_id=self.allocation_id)
        items = _new_get_key_in_response(response, 'EipAddresses.EipAddress')
        if not items:
            raise ClientException(msg="Failed to find EIP Address data from DescribeEipAddresses "
                                  "response. "
                                  "AllocationId = {0}".format(self.allocation_id))
        self._assign_attributes(items[0])


class VPCResource(_VPCResource):

    def __init__(self, _client=None):
        _VPCResource.__init__(self, _client=_client)
        self.eip_addresses = _create_resource_collection(
            VPCEipAddressResource, _client, _client.describe_eip_addresses,
            'EipAddresses.EipAddress', 'AllocationId',
            param_aliases={"Tags": "list_of_tags"}
        )
