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


class _SAEResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'sae', _client=_client)
        self.regions = _create_special_resource_collection(
            _SAERegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId', 
        )
    def create_application(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_application(**_params)
        app_id = _new_get_key_in_response(response, 'AppId')
        return _SAEApplicationResource(app_id, _client=self._client)

    def create_namespace(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_namespace(**_params)
        namespace_id = _new_get_key_in_response(response, 'NamespaceId')
        return _SAENamespaceResource(namespace_id, _client=self._client)

class _SAEApplicationResource(ServiceResource):

    def __init__(self, app_id, _client=None):
        ServiceResource.__init__(self, "sae.application", _client=_client)
        self.app_id = app_id
        

    def bind_slb(self, **params):
        _params = _transfer_params(params)
        return self._client.bind_slb(app_id=self.app_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_application(app_id=self.app_id, **_params)

    def describe_application_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_application_config(app_id=self.app_id, **_params)

    def describe_application_groups(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_application_groups(app_id=self.app_id, **_params)

    def describe_application_image(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_application_image(app_id=self.app_id, **_params)

    def describe_application_instances(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_application_instances(app_id=self.app_id, **_params)

    def describe_application_slbs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_application_slbs(app_id=self.app_id, **_params)

    def describe_application_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_application_status(app_id=self.app_id, **_params)

    def list_change_orders(self, **params):
        _params = _transfer_params(params)
        return self._client.list_change_orders(app_id=self.app_id, **_params)

    def list_consumed_services(self, **params):
        _params = _transfer_params(params)
        return self._client.list_consumed_services(app_id=self.app_id, **_params)

    def list_log_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.list_log_configs(app_id=self.app_id, **_params)

    def list_published_services(self, **params):
        _params = _transfer_params(params)
        return self._client.list_published_services(app_id=self.app_id, **_params)

    def query_resource_statics(self, **params):
        _params = _transfer_params(params)
        return self._client.query_resource_statics(app_id=self.app_id, **_params)

    def rescale(self, **params):
        _params = _transfer_params(params)
        return self._client.rescale_application(app_id=self.app_id, **_params)

    def rescale_application_vertically(self, **params):
        _params = _transfer_params(params)
        return self._client.rescale_application_vertically(app_id=self.app_id, **_params)

    def restart(self, **params):
        _params = _transfer_params(params)
        return self._client.restart_application(app_id=self.app_id, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        return self._client.start_application(app_id=self.app_id, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_application(app_id=self.app_id, **_params)

    def unbind_slb(self, **params):
        _params = _transfer_params(params)
        return self._client.unbind_slb(app_id=self.app_id, **_params)

class _SAENamespaceResource(ServiceResource):

    def __init__(self, namespace_id, _client=None):
        ServiceResource.__init__(self, "sae.namespace", _client=_client)
        self.namespace_id = namespace_id
        

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_namespace(namespace_id=self.namespace_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_namespace(namespace_id=self.namespace_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_namespace(namespace_id=self.namespace_id, **_params)

class _SAERegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "sae.region", _client=_client)
        self.region_id = region_id
        
        self.local_name = None
        self.region_endpoint = None
