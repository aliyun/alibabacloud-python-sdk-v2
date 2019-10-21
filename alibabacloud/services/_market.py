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
from alibabacloud.resources.collection import _create_sub_resource_with_page_collection
from alibabacloud.resources.collection import _create_sub_resource_without_page_collection
from alibabacloud.utils.utils import _assert_is_not_none, _new_get_key_in_response, _transfer_params


class _MARKETResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'market', _client=_client)
        self.instances = _create_resource_collection(
            _MARKETInstanceResource, _client, _client.describe_instances,
            'InstanceItems.InstanceItem', 'InstanceId', 
        )
    def create_commodity(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_commodity(**_params)
        commodity_id = _new_get_key_in_response(response, 'CommodityId')
        return _MARKETCommodityResource(commodity_id, _client=self._client)

    def create_order(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_order(**_params)
        order_id = _new_get_key_in_response(response, 'OrderId')
        return _MARKETOrderResource(order_id, _client=self._client)

class _MARKETCommodityResource(ServiceResource):

    def __init__(self, commodity_id, _client=None):
        ServiceResource.__init__(self, "market.commodity", _client=_client)
        self.commodity_id = commodity_id
        

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_commodity(commodity_id=self.commodity_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_commodity(commodity_id=self.commodity_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_commodity(commodity_id=self.commodity_id, **_params)

class _MARKETInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "market.instance", _client=_client)
        self.instance_id = instance_id
        
        self.api_json = None
        self.app_json = None
        self.began_on = None
        self.created_on = None
        self.end_on = None
        self.extend_json = None
        self.host_json = None
        self.idaas_json = None
        self.image_json = None
        self.order_id = None
        self.product_code = None
        self.product_name = None
        self.product_sku_code = None
        self.product_type = None
        self.status = None
        self.supplier_name = None

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_instance(instance_id=self.instance_id, **_params)

class _MARKETOrderResource(ServiceResource):

    def __init__(self, order_id, _client=None):
        ServiceResource.__init__(self, "market.order", _client=_client)
        self.order_id = order_id
        

    def create_rate(self, **params):
        _params = _transfer_params(params)
        return self._client.create_rate(order_id=self.order_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_order(order_id=self.order_id, **_params)

    def describe_rate(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_rate(order_id=self.order_id, **_params)
