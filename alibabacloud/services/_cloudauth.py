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


class _CLOUDAUTHResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'cloudauth', _client=_client)
        self.verify_settings = _create_special_resource_collection(
            _CLOUDAUTHVerifySettingResource, _client, _client.describe_verify_setting,
            'VerifySettingList.VerifySetting', 'BizName',
        )

    def create_rpsdk(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_rpsdk(**_params)
        task_id = _new_get_key_in_response(response, 'TaskId')
        return _CLOUDAUTHRPSDKResource(task_id, _client=self._client)

    def create_verify_setting(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_verify_setting(**_params)
        biz_name = _new_get_key_in_response(response, 'BizName')
        return _CLOUDAUTHVerifySettingResource(biz_name, _client=self._client)

    def update_verify_setting(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_verify_setting(**_params)
        biz_name = _new_get_key_in_response(response, 'BizName')
        return _CLOUDAUTHVerifySettingResource(biz_name, _client=self._client)


class _CLOUDAUTHRPSDKResource(ServiceResource):

    def __init__(self, task_id, _client=None):
        ServiceResource.__init__(self, "cloudauth.rpsdk", _client=_client)
        self.task_id = task_id

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_rpsdk(task_id=self.task_id, **_params)

    def describe_verify_sdk(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_verify_sdk(task_id=self.task_id, **_params)


class _CLOUDAUTHVerifySettingResource(ServiceResource):

    def __init__(self, biz_name, _client=None):
        ServiceResource.__init__(self, "cloudauth.verify_setting", _client=_client)
        self.biz_name = biz_name

        self.biz_type = None
        self.solution = None
        self.step_list = None
