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


class _ARMSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'arms', _client=_client)
    def create_alert_contact(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_alert_contact(**_params)
        contact_id = _new_get_key_in_response(response, 'ContactId')
        return _ARMSAlertContactResource(contact_id, _client=self._client)

    def create_alert_contact_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_alert_contact_group(**_params)
        contact_group_id = _new_get_key_in_response(response, 'ContactGroupId')
        return _ARMSAlertContactGroupResource(contact_group_id, _client=self._client)

    def create_retcode_app(self, **params):
        _params = _transfer_params(params)
        self._client.create_retcode_app(**_params)
        retcode_app_name = _params.get("retcode_app_name")
        return _ARMSRetcodeAppResource(retcode_app_name, _client=self._client)

class _ARMSAlertContactResource(ServiceResource):

    def __init__(self, contact_id, _client=None):
        ServiceResource.__init__(self, "arms.alert_contact", _client=_client)
        self.contact_id = contact_id
        

class _ARMSAlertContactGroupResource(ServiceResource):

    def __init__(self, contact_group_id, _client=None):
        ServiceResource.__init__(self, "arms.alert_contact_group", _client=_client)
        self.contact_group_id = contact_group_id
        

class _ARMSRetcodeAppResource(ServiceResource):

    def __init__(self, retcode_app_name, _client=None):
        ServiceResource.__init__(self, "arms.retcode_app", _client=_client)
        self.retcode_app_name = retcode_app_name
        
