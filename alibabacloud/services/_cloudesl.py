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
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _CLOUDESLResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'cloudesl', _client=_client)
        self.alarms = _create_resource_collection(
            _CLOUDESLAlarmResource, _client, _client.describe_alarms,
            'Alarms.AlarmInfo', 'AlarmId',
        )
        self.items = _create_resource_collection(
            _CLOUDESLItemResource, _client, _client.describe_items,
            'Items.ItemInfo', 'ItemId',
        )
        self.stores = _create_resource_collection(
            _CLOUDESLStoreResource, _client, _client.describe_stores,
            'Stores.StoreInfo', 'StoreId',
        )

    def create_store(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_store(**_params)
        store_id = _new_get_key_in_response(response, 'StoreId')
        return _CLOUDESLStoreResource(store_id, _client=self._client)


class _CLOUDESLAlarmResource(ServiceResource):

    def __init__(self, alarm_id, _client=None):
        ServiceResource.__init__(self, "cloudesl.alarm", _client=_client)
        self.alarm_id = alarm_id

        self.alarm_status = None
        self.alarm_time = None
        self.alarm_type = None
        self.company_id = None
        self.deal_time = None
        self.deal_user_id = None
        self.device_bar_code = None
        self.device_mac = None
        self.device_type = None
        self.error_type = None
        self.item_bar_code = None
        self.item_title = None
        self.model = None
        self.store_id = None
        self.vendor = None


class _CLOUDESLItemResource(ServiceResource):

    def __init__(self, item_id, _client=None):
        ServiceResource.__init__(self, "cloudesl.item", _client=_client)
        self.item_id = item_id

        self.action_price = None
        self.be_promotion = None
        self.be_source_code = None
        self.brand_name = None
        self.category_name = None
        self.company_id = None
        self.customize_featurea = None
        self.customize_featureb = None
        self.customize_featurec = None
        self.customize_featured = None
        self.customize_featuree = None
        self.customize_featuref = None
        self.customize_featureg = None
        self.customize_featureh = None
        self.customize_featurei = None
        self.customize_featurej = None
        self.energy_efficiency = None
        self.extra_attribute = None
        self.forest_first_id = None
        self.forest_second_id = None
        self.item_bar_code = None
        self.item_qr_code = None
        self.item_short_title = None
        self.item_title = None
        self.member_price = None
        self.model_number = None
        self.option_groups = None
        self.original_price = None
        self.position_code = None
        self.price_unit = None
        self.production_place = None
        self.promotion_end = None
        self.promotion_reason = None
        self.promotion_start = None
        self.promotion_text = None
        self.rank = None
        self.sale_spec = None
        self.sku_id = None
        self.source_code = None
        self.store_id = None
        self.suggest_price = None


class _CLOUDESLStoreResource(ServiceResource):

    def __init__(self, store_id, _client=None):
        ServiceResource.__init__(self, "cloudesl.store", _client=_client)
        self.store_id = store_id

        self.brand = None
        self.comments = None
        self.company_id = None
        self.gmt_create = None
        self.gmt_modified = None
        self.groups = None
        self.level = None
        self.out_id = None
        self.parent_id = None
        self.phone = None
        self.store_name = None

    def batch_insert_items(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_insert_items(store_id=self.store_id, **_params)

    def activate_ap_service(self, **params):
        _params = _transfer_params(params)
        return self._client.activate_ap_service(store_id=self.store_id, **_params)

    def activate_ap_service2(self, **params):
        _params = _transfer_params(params)
        return self._client.activate_ap_service2(store_id=self.store_id, **_params)

    def bind_ap_store_service(self, **params):
        _params = _transfer_params(params)
        return self._client.bind_ap_store_service(store_id=self.store_id, **_params)

    def bind_esl_device(self, **params):
        _params = _transfer_params(params)
        return self._client.bind_esl_device(store_id=self.store_id, **_params)

    def bind_esl_device_shelf(self, **params):
        _params = _transfer_params(params)
        return self._client.bind_esl_device_shelf(store_id=self.store_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_store(store_id=self.store_id, **_params)

    def delete_ap_service(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_ap_service(store_id=self.store_id, **_params)

    def delete_esl_device(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_esl_device(store_id=self.store_id, **_params)

    def delete_item(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_item(store_id=self.store_id, **_params)

    def delete_item_by_sku_id(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_item_by_sku_id(store_id=self.store_id, **_params)

    def describe_esl_devices(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_esl_devices(store_id=self.store_id, **_params)

    def describe_user_operation_log(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_user_operation_log(store_id=self.store_id, **_params)

    def search_ap_service(self, **params):
        _params = _transfer_params(params)
        return self._client.search_ap_service(store_id=self.store_id, **_params)

    def unbind_esl_device(self, **params):
        _params = _transfer_params(params)
        return self._client.unbind_esl_device(store_id=self.store_id, **_params)

    def unbind_esl_device_shelf(self, **params):
        _params = _transfer_params(params)
        return self._client.unbind_esl_device_shelf(store_id=self.store_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_store(store_id=self.store_id, **_params)
