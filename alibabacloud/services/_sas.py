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


class _SASResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'sas', _client=_client)
        self.check_warnings = _create_special_resource_collection(
            _SASCheckWarningResource, _client, _client.describe_check_warnings,
            'CheckWarnings.CheckWarning', 'CheckWarningId', 
        )
class _SASCheckWarningResource(ServiceResource):

    def __init__(self, check_warning_id, _client=None):
        ServiceResource.__init__(self, "sas.check_warning", _client=_client)
        self.check_warning_id = check_warning_id
        
        self.check_id = None
        self.item = None
        self.level = None
        self.status = None
        self.type_ = None
        self.uuid = None

    def describe_check_warning_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_check_warning_detail(check_warning_id=self.check_warning_id, **_params)
