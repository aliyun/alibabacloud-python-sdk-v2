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

from aliyunsdkslb.request.v20140515.DescribeLoadBalancersRequest import DescribeLoadBalancersRequest
from aliyunsdkslb.request.v20140515.CreateLoadBalancerRequest import CreateLoadBalancerRequest
from aliyunsdkslb.request.v20140515.DeleteLoadBalancerRequest import DeleteLoadBalancerRequest
from aliyunsdkslb.request.v20140515.SetLoadBalancerNameRequest import SetLoadBalancerNameRequest
from aliyunsdkslb.request.v20140515.SetLoadBalancerStatusRequest import SetLoadBalancerStatusRequest


class LoadBalancerResource(ServiceResource):

    def __init__(self, load_balancer_id, _client=None):
        ServiceResource.__init__(self, 'slb.load_balancer', _client=_client)
        self.load_balancer_id = load_balancer_id

    def delete(self):
        request = DeleteLoadBalancerRequest()
        request.set_LoadBalancerId(self.load_balancer_id)
        _do_request(self._client, request, {})

    def set_status(self, **params):
        request = SetLoadBalancerStatusRequest()
        request.set_LoadBalancerId(self.load_balancer_id)
        _do_request(self._client, request, params)

    def set_name(self, **params):
        request = SetLoadBalancerNameRequest()
        request.set_LoadBalancerId(self.load_balancer_id)
        _do_request(self._client, request, params)

    def refresh(self):
        request = DescribeLoadBalancersRequest()
        request.set_LoadBalancerId(self.load_balancer_id)
        items = _get_response(self._client, request, {}, 'LoadBalancers.LoadBalancer')
        if not items:
            raise ClientException(errors.ERROR_INVALID_SERVER_RESPONSE,
                                  "Failed to find load balancer data from DescribeLoadBalancers "
                                  "response. "
                                  "LoadBalancerId = {0}".format(self.load_balancer_id))
        self._assign_attributes(items[0])


class SLBResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'vpc', _client=_client)
        self.load_balancers = _create_resource_collection(
            LoadBalancerResource, _client, DescribeLoadBalancersRequest,
            'LoadBalancers.LoadBalancer', 'LoadBalancerId'
        )

    def create_load_balancer(self, **params):
        request = CreateLoadBalancerRequest()
        load_balancer_id = _get_response(self._client, request, params, key='LoadBalancerId')
        return LoadBalancerResource(load_balancer_id, _client=self._client)
