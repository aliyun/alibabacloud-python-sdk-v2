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
from alibabacloud.resources.collection import _create_resource_collection
from alibabacloud.resources.collection import _create_default_resource_collection
from alibabacloud.utils.utils import _assert_is_not_none, _new_get_key_in_response, _transfer_params


class _CDNResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'cdn', _client=_client)
class _CDNConfigResource(ServiceResource):

    def __init__(self, config_id, _client=None):
        ServiceResource.__init__(self, "cdn.config", _client=_client)
        self.config_id = config_id


    def delete_specific(self, **params):
        _params = _transfer_params(params)
        self._client.delete_specific_config(config_id=self.config_id, **_params)

    def describe_custom_log(self, **params):
        _params = _transfer_params(params)
        self._client.describe_custom_log_config(config_id=self.config_id, **_params)

    def modify_domain_custom_log(self, **params):
        _params = _transfer_params(params)
        self._client.modify_domain_custom_log_config(config_id=self.config_id, **_params)

    def modify_user_custom_log(self, **params):
        _params = _transfer_params(params)
        self._client.modify_user_custom_log_config(config_id=self.config_id, **_params)

class _CDNTaskResource(ServiceResource):

    def __init__(self, task_id, _client=None):
        ServiceResource.__init__(self, "cdn.task", _client=_client)
        self.task_id = task_id


    def delete_usage_detail_data_export(self, **params):
        _params = _transfer_params(params)
        self._client.delete_usage_detail_data_export_task(task_id=self.task_id, **_params)

    def delete_user_usage_data_export(self, **params):
        _params = _transfer_params(params)
        self._client.delete_user_usage_data_export_task(task_id=self.task_id, **_params)
