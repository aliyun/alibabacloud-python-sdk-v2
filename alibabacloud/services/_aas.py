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


class _AASResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'aas', _client=_client)
        self.aliyun_accounts = _create_special_resource_collection(
            _AASAliyunAccountResource, _client, _client.list_aliyun_account,
            'Accounts.Account', 'AliyunId',
        )

    def create_aliyun_account(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_aliyun_account(**_params)
        aliyun_id = _new_get_key_in_response(response, 'AliyunId')
        return _AASAliyunAccountResource(aliyun_id, _client=self._client)


class _AASAliyunAccountResource(ServiceResource):

    def __init__(self, aliyun_id, _client=None):
        ServiceResource.__init__(self, "aas.aliyun_account", _client=_client)
        self.aliyun_id = aliyun_id

        self.account_status = None
        self.last_login_date = None
        self.pk = None
