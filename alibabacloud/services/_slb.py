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

import json
import time

from alibabacloud.exceptions import ClientException
from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, _create_special_resource_collection
from alibabacloud.resources.collection import _create_default_resource_collection
from alibabacloud.utils.utils import _assert_is_not_none, _new_get_key_in_response, _transfer_params


class _SLBResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'slb', _client=_client)

        self.load_balancers = _create_resource_collection(
            _SLBLoadBalancerResource, _client, _client.describe_load_balancers,
            'LoadBalancers.LoadBalancer', 'LoadBalancerId',
        )

    def create_load_balancer(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_load_balancer(**_params)
        load_balancer_id = _new_get_key_in_response(response, 'LoadBalancerId')
        return _SLBLoadBalancerResource(load_balancer_id, _client=self._client)


class _SLBLoadBalancerResource(ServiceResource):

    def __init__(self, load_balancer_id, _client=None):
        ServiceResource.__init__(self, "slb.load_balancer", _client=_client)
        self.load_balancer_id = load_balancer_id

        self.address = None
        self.address_ip_version = None
        self.address_type = None
        self.create_time = None
        self.create_time_stamp = None
        self.internet_charge_type = None
        self.load_balancer_name = None
        self.load_balancer_status = None
        self.master_zone_id = None
        self.network_type = None
        self.pay_type = None
        self.region_id = None
        self.region_id_alias = None
        self.resource_group_id = None
        self.slave_zone_id = None
        self.tags = None
        self.vswitch_id = None
        self.vpc_id = None

    def delete(self):
        self._client.delete_load_balancer(load_balancer_id=self.load_balancer_id)

    def set_status(self, **params):
        _params = _transfer_params(params)
        self._client.set_load_balancer_status(load_balancer_id=self.load_balancer_id, **_params)

    def set_name(self, **params):
        _params = _transfer_params(params)
        self._client.set_load_balancer_name(load_balancer_id=self.load_balancer_id, **_params)

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
