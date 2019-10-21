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


class _QUALITYCHECKResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'qualitycheck', _client=_client)
        self.users = _create_special_resource_collection(
            _QUALITYCHECKUserResource, _client, _client.list_users,
            'Data.User', 'UserName', 
        )
class _QUALITYCHECKUserResource(ServiceResource):

    def __init__(self, user_name, _client=None):
        ServiceResource.__init__(self, "qualitycheck.user", _client=_client)
        self.user_name = user_name
        
        self.ali_uid = None
        self.create_time = None
        self.description = None
        self.display_name = None
        self.id_ = None
        self.login_user_type = None
        self.role_name = None
        self.update_time = None
