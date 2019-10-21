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


class _CSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'cs', _client=_client)
class _CSClusterResource(ServiceResource):

    def __init__(self, cluster_id, _client=None):
        ServiceResource.__init__(self, "cs.cluster", _client=_client)
        self.cluster_id = cluster_id
        

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_cluster(cluster_id=self.cluster_id, **_params)

    def delete_nodes(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_cluster_nodes(cluster_id=self.cluster_id, **_params)

    def describe_user_kubeconfig(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cluster_user_kubeconfig(cluster_id=self.cluster_id, **_params)

    def describe_v2_user_kubeconfig(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cluster_v2_user_kubeconfig(cluster_id=self.cluster_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_cluster(cluster_id=self.cluster_id, **_params)

    def scale(self, **params):
        _params = _transfer_params(params)
        return self._client.scale_cluster(cluster_id=self.cluster_id, **_params)
