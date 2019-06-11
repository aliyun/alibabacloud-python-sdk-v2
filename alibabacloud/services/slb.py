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
from alibabacloud.utils.utils import _get_key_in_response
from alibabacloud.exceptions import ClientException


class LoadBalancerResource(ServiceResource):

    def __init__(self, load_balancer_id, _client=None):
        ServiceResource.__init__(self, 'slb.load_balancer', _client=_client)
        self.load_balancer_id = load_balancer_id

    def delete(self):
        self._client.delete_load_balancer(load_balancer_id=self.load_balancer_id)

    def set_status(self, **params):
        self._client.set_load_balancer_status(load_balancer_id=self.load_balancer_id, **params)

    def set_name(self, **params):
        self._client.set_load_balancer_name(load_balancer_id=self.load_balancer_id, **params)

    def refresh(self):
        response = self._client.set_load_balancer_name(load_balancer_id=self.load_balancer_id)
        items = _get_key_in_response(response, 'LoadBalancers.LoadBalancer')
        if not items:
            raise ClientException(msg=
                                  "Failed to find load balancer data from DescribeLoadBalancers "
                                  "response. "
                                  "LoadBalancerId = {0}".format(self.load_balancer_id))
        self._assign_attributes(items[0])


class SLBResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'vpc', _client=_client)
        self.load_balancers = _create_resource_collection(
            LoadBalancerResource, _client, _client.describe_load_balancers,
            'LoadBalancers.LoadBalancer', 'LoadBalancerId'
        )

    def create_load_balancer(self, **params):
        response = self._client.set_load_balancer_name(**params)
        load_balancer_id = _get_key_in_response(response, 'LoadBalancerId')
        return LoadBalancerResource(load_balancer_id, _client=self._client)
