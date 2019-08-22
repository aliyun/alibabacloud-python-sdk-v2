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
from alibabacloud.services._slb import _SLBResource, _SLBLoadBalancerResource
from alibabacloud.utils.utils import transfer, _new_get_key_in_response


class LoadBalancerResource(_SLBLoadBalancerResource):

    def __init__(self, load_balancer_id, _client=None):
        _SLBLoadBalancerResource.__init__(self, load_balancer_id, _client=_client)
        self.load_balancer_id = load_balancer_id

    @transfer({"Tags": "list_of_tags",})
    def refresh(self):
        response = self._client.describe_load_balancers(load_balancer_id=self.load_balancer_id)
        items = _new_get_key_in_response(response, 'LoadBalancers.LoadBalancer')
        if not items:
            raise ClientException(
                msg="Failed to find load balancer data from DescribeLoadBalancers "
                "response. "
                "LoadBalancerId = {0}".format(
                    self.load_balancer_id))
        self._assign_attributes(items[0])


class SLBResource(_SLBResource):

    def __init__(self, _client=None):
        _SLBResource.__init__(self, _client=_client)
        self.load_balancers = _create_resource_collection(
            LoadBalancerResource, _client, _client.describe_load_balancers,
            'LoadBalancers.LoadBalancer', 'LoadBalancerId',
            param_aliases={
                "Tags": "list_of_tags",
            }
        )
