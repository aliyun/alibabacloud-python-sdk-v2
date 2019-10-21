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


class _IVPDResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ivpd', _client=_client)
    def segment_image(self, **params):
        _params = _transfer_params(params)
        response = self._client.segment_image(**_params)
        url = _new_get_key_in_response(response, 'Url')
        return _IVPDImageResource(url, _client=self._client)

class _IVPDImageResource(ServiceResource):

    def __init__(self, url, _client=None):
        ServiceResource.__init__(self, "ivpd.image", _client=_client)
        self.url = url
        

    def change_image_size(self, **params):
        _params = _transfer_params(params)
        return self._client.change_image_size(url=self.url, **_params)

    def detect_image_elements(self, **params):
        _params = _transfer_params(params)
        return self._client.detect_image_elements(url=self.url, **_params)

    def make_super_resolution(self, **params):
        _params = _transfer_params(params)
        return self._client.make_super_resolution_image(url=self.url, **_params)

    def recognize_image_color(self, **params):
        _params = _transfer_params(params)
        return self._client.recognize_image_color(url=self.url, **_params)

    def recognize_image_style(self, **params):
        _params = _transfer_params(params)
        return self._client.recognize_image_style(url=self.url, **_params)

    def recolor(self, **params):
        _params = _transfer_params(params)
        return self._client.recolor_image(url=self.url, **_params)
