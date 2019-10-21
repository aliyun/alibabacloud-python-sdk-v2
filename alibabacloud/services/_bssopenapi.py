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


class _BSSOPENAPIResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'bssopenapi', _client=_client)
        self.cash_coupons = _create_special_resource_collection(
            _BSSOPENAPICashCouponResource, _client, _client.query_cash_coupons,
            'Data.CashCoupon', 'CashCouponId', 
        )
        self.prepaid_cards = _create_special_resource_collection(
            _BSSOPENAPIPrepaidCardResource, _client, _client.query_prepaid_cards,
            'Data.PrepaidCard', 'PrepaidCardId', 
        )
    def create_ag_account(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ag_account(**_params)
        ram_admin_role_name = _new_get_key_in_response(response, 'RamAdminRoleName')
        return _BSSOPENAPIAgAccountResource(ram_admin_role_name, _client=self._client)

    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _BSSOPENAPIInstanceResource(instance_id, _client=self._client)

class _BSSOPENAPIAgAccountResource(ServiceResource):

    def __init__(self, ram_admin_role_name, _client=None):
        ServiceResource.__init__(self, "bssopenapi.ag_account", _client=_client)
        self.ram_admin_role_name = ram_admin_role_name
        

class _BSSOPENAPICashCouponResource(ServiceResource):

    def __init__(self, cash_coupon_id, _client=None):
        ServiceResource.__init__(self, "bssopenapi.cash_coupon", _client=_client)
        self.cash_coupon_id = cash_coupon_id
        
        self.applicable_products = None
        self.applicable_scenarios = None
        self.balance = None
        self.cash_coupon_no = None
        self.effective_time = None
        self.expiry_time = None
        self.granted_time = None
        self.nominal_value = None
        self.status = None

class _BSSOPENAPIInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "bssopenapi.instance", _client=_client)
        self.instance_id = instance_id
        

    def convert_charge_type(self, **params):
        _params = _transfer_params(params)
        return self._client.convert_charge_type(instance_id=self.instance_id, **_params)

    def renew(self, **params):
        _params = _transfer_params(params)
        return self._client.renew_instance(instance_id=self.instance_id, **_params)

    def renew_resource_package(self, **params):
        _params = _transfer_params(params)
        return self._client.renew_resource_package(instance_id=self.instance_id, **_params)

class _BSSOPENAPIPrepaidCardResource(ServiceResource):

    def __init__(self, prepaid_card_id, _client=None):
        ServiceResource.__init__(self, "bssopenapi.prepaid_card", _client=_client)
        self.prepaid_card_id = prepaid_card_id
        
        self.applicable_products = None
        self.applicable_scenarios = None
        self.balance = None
        self.effective_time = None
        self.expiry_time = None
        self.granted_time = None
        self.nominal_value = None
        self.prepaid_card_no = None
        self.status = None
