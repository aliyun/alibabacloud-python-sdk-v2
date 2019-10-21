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


class _RTCResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'rtc', _client=_client)
class _RTCTaskResource(ServiceResource):

    def __init__(self, task_id, _client=None):
        ServiceResource.__init__(self, "rtc.task", _client=_client)
        self.task_id = task_id
        

    def get_mpu_task_status(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_mpu_task_status(task_id=self.task_id, **_params)
        return response

    def get_task_param(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_task_param(task_id=self.task_id, **_params)
        return response

    def stop_mpu(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_mpu_task(task_id=self.task_id, **_params)
