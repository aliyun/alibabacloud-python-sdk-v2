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


class _HTTPDNSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'httpdns', _client=_client)
        self.domains = _create_resource_collection(
            _HTTPDNSDomainResource, _client, _client.list_domains,
            'DomainInfos.DomainInfo', 'DomainName', 
        )
        self.domains = _create_resource_collection(
            _HTTPDNSDomainResource, _client, _client.list_domains,
            'DomainInfos.DomainInfo', 'DomainName', 
        )
    def add_domain(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_domain(**_params)
        domain_name = _new_get_key_in_response(response, 'DomainName')
        return _HTTPDNSDomainResource(domain_name, _client=self._client)

    def delete_domain(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_domain(**_params)
        domain_name = _new_get_key_in_response(response, 'DomainName')
        return _HTTPDNSDomainResource(domain_name, _client=self._client)

class _HTTPDNSDomainResource(ServiceResource):

    def __init__(self, domain_name, _client=None):
        ServiceResource.__init__(self, "httpdns.domain", _client=_client)
        self.domain_name = domain_name
        

    def get_resolve_statistics(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_resolve_statistics(domain_name=self.domain_name, **_params)
        return response
