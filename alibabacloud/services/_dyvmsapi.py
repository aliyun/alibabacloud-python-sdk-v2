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


class _DYVMSAPIResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'dyvmsapi', _client=_client)
    def ivr_call(self, **params):
        _params = _transfer_params(params)
        response = self._client.ivr_call(**_params)
        call_id = _new_get_key_in_response(response, 'CallId')
        return _DYVMSAPICallResource(call_id, _client=self._client)

    def smart_call(self, **params):
        _params = _transfer_params(params)
        response = self._client.smart_call(**_params)
        call_id = _new_get_key_in_response(response, 'CallId')
        return _DYVMSAPICallResource(call_id, _client=self._client)

class _DYVMSAPICallResource(ServiceResource):

    def __init__(self, call_id, _client=None):
        ServiceResource.__init__(self, "dyvmsapi.call", _client=_client)
        self.call_id = call_id
        

    def cancel(self, **params):
        _params = _transfer_params(params)
        return self._client.cancel_call(call_id=self.call_id, **_params)

    def query_call_detail_by_call_id(self, **params):
        _params = _transfer_params(params)
        return self._client.query_call_detail_by_call_id(call_id=self.call_id, **_params)

    def smart_call_operate(self, **params):
        _params = _transfer_params(params)
        return self._client.smart_call_operate(call_id=self.call_id, **_params)
