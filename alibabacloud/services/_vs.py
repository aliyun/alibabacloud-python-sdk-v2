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


class _VSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'vs', _client=_client)
    def bind_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.bind_template(**_params)
        template_id = _new_get_key_in_response(response, 'TemplateId')
        return _VSTemplateResource(template_id, _client=self._client)

    def unbind_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.unbind_template(**_params)
        template_id = _new_get_key_in_response(response, 'TemplateId')
        return _VSTemplateResource(template_id, _client=self._client)

class _VSTemplateResource(ServiceResource):

    def __init__(self, template_id, _client=None):
        ServiceResource.__init__(self, "vs.template", _client=_client)
        self.template_id = template_id
        

    def batch_bind(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_bind_templates(template_id=self.template_id, **_params)
