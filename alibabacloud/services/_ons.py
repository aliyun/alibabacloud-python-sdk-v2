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
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _ONSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ons', _client=_client)

    def ons_instance_create(self, **params):
        _params = _transfer_params(params)
        response = self._client.ons_instance_create(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _ONSceCreateResource(instance_id, _client=self._client)


class _ONSceCreateResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "ons.ce_create", _client=_client)
        self.instance_id = instance_id

    def group_sub_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.ons_group_sub_detail(instance_id=self.instance_id, **_params)

    def instance_base_info(self, **params):
        _params = _transfer_params(params)
        return self._client.ons_instance_base_info(instance_id=self.instance_id, **_params)

    def instance_delete(self, **params):
        _params = _transfer_params(params)
        return self._client.ons_instance_delete(instance_id=self.instance_id, **_params)

    def instance_update(self, **params):
        _params = _transfer_params(params)
        return self._client.ons_instance_update(instance_id=self.instance_id, **_params)

    def topic_sub_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.ons_topic_sub_detail(instance_id=self.instance_id, **_params)
