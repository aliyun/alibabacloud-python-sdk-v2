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
from alibabacloud.resources.collection import _create_special_resource_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _TRADEMARKResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'trademark', _client=_client)
        self.notary_orders = _create_special_resource_collection(
            _TRADEMARKNotaryOrderResource, _client, _client.list_notary_orders,
            'Data.NotaryOrder', 'NotaryOrderId',
        )

    def create_trademark_order(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_trademark_order(**_params)
        order_id = _new_get_key_in_response(response, 'OrderId')
        return _TRADEMARKOrderResource(order_id, _client=self._client)

    def generate_upload_file_policy(self, **params):
        _params = _transfer_params(params)
        response = self._client.generate_upload_file_policy(**_params)
        access_id = _new_get_key_in_response(response, 'AccessId')
        return _TRADEMARKUploadFilePolicyResource(access_id, _client=self._client)


class _TRADEMARKNotaryOrderResource(ServiceResource):

    def __init__(self, notary_order_id, _client=None):
        ServiceResource.__init__(self, "trademark.notary_order", _client=_client)
        self.notary_order_id = notary_order_id

        self.aliyun_order_id = None
        self.apply_post_status = None
        self.biz_id = None
        self.gmt_modified = None
        self.notary_certificate = None
        self.notary_platform_name = None
        self.notary_status = None
        self.notary_type = None
        self.order_date = None
        self.order_price = None
        self.tm_classification = None
        self.tm_image = None
        self.tm_name = None
        self.tm_register_no = None

    def apply_notary_post(self, **params):
        _params = _transfer_params(params)
        return self._client.apply_notary_post(notary_order_id=self.notary_order_id, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_notary_order(notary_order_id=self.notary_order_id, **_params)

    def start_notary(self, **params):
        _params = _transfer_params(params)
        return self._client.start_notary(notary_order_id=self.notary_order_id, **_params)


class _TRADEMARKOrderResource(ServiceResource):

    def __init__(self, order_id, _client=None):
        ServiceResource.__init__(self, "trademark.order", _client=_client)
        self.order_id = order_id


class _TRADEMARKUploadFilePolicyResource(ServiceResource):

    def __init__(self, access_id, _client=None):
        ServiceResource.__init__(self, "trademark.upload_file_policy", _client=_client)
        self.access_id = access_id
