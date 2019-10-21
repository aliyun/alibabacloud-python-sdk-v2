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


class _BATCHCOMPUTEResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'batchcompute', _client=_client)
class _BATCHCOMPUTEJobResource(ServiceResource):

    def __init__(self, resource_name, _client=None):
        ServiceResource.__init__(self, "batchcompute.job", _client=_client)
        self.resource_name = resource_name
        

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_job(resource_name=self.resource_name, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_job(resource_name=self.resource_name, **_params)

    def get_description(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_job_description(resource_name=self.resource_name, **_params)
        return response

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_job(resource_name=self.resource_name, **_params)

    def put(self, **params):
        _params = _transfer_params(params)
        return self._client.put_job(resource_name=self.resource_name, **_params)

    def release(self, **params):
        _params = _transfer_params(params)
        return self._client.release_job(resource_name=self.resource_name, **_params)
