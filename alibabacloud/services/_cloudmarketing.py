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


class _CLOUDMARKETINGResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'cloudmarketing', _client=_client)
        self.crowds = _create_special_resource_collection(
            _CLOUDMARKETINGCrowdResource, _client, _client.describe_crowd,
            'Crowds.Crowds', 'CrowdId', 
        )
        self.files = _create_special_resource_collection(
            _CLOUDMARKETINGFileResource, _client, _client.describe_file,
            'Files.Files', 'FileId', 
        )
        self.tags = _create_special_resource_collection(
            _CLOUDMARKETINGTagResource, _client, _client.describe_tag,
            'CategoryTagCounts.CategoryTagCounts', 'TagId', 
        )
    def create_brand(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_brand(**_params)
        brand_id = _new_get_key_in_response(response, 'BrandId')
        return _CLOUDMARKETINGBrandResource(brand_id, _client=self._client)

    def create_category(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_category(**_params)
        category_id = _new_get_key_in_response(response, 'CategoryId')
        return _CLOUDMARKETINGCategoryResource(category_id, _client=self._client)

    def fetch_crowd(self, **params):
        _params = _transfer_params(params)
        response = self._client.fetch_crowd(**_params)
        crowd_id = _new_get_key_in_response(response, 'CrowdId')
        return _CLOUDMARKETINGCrowdResource(crowd_id, _client=self._client)

    def define_tag(self, **params):
        _params = _transfer_params(params)
        response = self._client.define_tag(**_params)
        tag_id = _new_get_key_in_response(response, 'TagId')
        return _CLOUDMARKETINGTagResource(tag_id, _client=self._client)

class _CLOUDMARKETINGBrandResource(ServiceResource):

    def __init__(self, brand_id, _client=None):
        ServiceResource.__init__(self, "cloudmarketing.brand", _client=_client)
        self.brand_id = brand_id
        

class _CLOUDMARKETINGCategoryResource(ServiceResource):

    def __init__(self, category_id, _client=None):
        ServiceResource.__init__(self, "cloudmarketing.category", _client=_client)
        self.category_id = category_id
        

class _CLOUDMARKETINGCrowdResource(ServiceResource):

    def __init__(self, crowd_id, _client=None):
        ServiceResource.__init__(self, "cloudmarketing.crowd", _client=_client)
        self.crowd_id = crowd_id
        
        self.can_analysis = None
        self.can_download_analysis = None
        self.can_download_crowd = None
        self.can_sync_ud = None
        self.can_update = None
        self.crowd_desc = None
        self.crowd_name = None
        self.crowd_scale = None
        self.progress = None
        self.progress_flag = None
        self.sync_channel = None
        self.sync_progress = None
        self.sync_progress_flag = None
        self.unix_valid_time = None
        self.valid_time = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_crowd(crowd_id=self.crowd_id, **_params)

    def fetch_crowd_define(self, **params):
        _params = _transfer_params(params)
        return self._client.fetch_crowd_define(crowd_id=self.crowd_id, **_params)

class _CLOUDMARKETINGFileResource(ServiceResource):

    def __init__(self, file_id, _client=None):
        ServiceResource.__init__(self, "cloudmarketing.file", _client=_client)
        self.file_id = file_id
        
        self.file_format = None
        self.file_name = None
        self.file_size = None
        self.progress = None
        self.progress_flag = None
        self.unix_valid_time = None
        self.upload_time = None

class _CLOUDMARKETINGTagResource(ServiceResource):

    def __init__(self, tag_id, _client=None):
        ServiceResource.__init__(self, "cloudmarketing.tag", _client=_client)
        self.tag_id = tag_id
        
        self.category_id = None
        self.category_name = None
        self.leaf = None
        self.tag_count = None
