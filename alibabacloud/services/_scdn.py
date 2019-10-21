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


class _SCDNResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'scdn', _client=_client)
    def add_scdn_domain(self, **params):
        _params = _transfer_params(params)
        self._client.add_scdn_domain(**_params)
        scdn_domain_name = _params.get("scdn_domain_name")
        return _SCDNScdnDomainResource(scdn_domain_name, _client=self._client)

class _SCDNScdnDomainResource(ServiceResource):

    def __init__(self, scdn_domain_name, _client=None):
        ServiceResource.__init__(self, "scdn.scdn_domain", _client=_client)
        self.scdn_domain_name = scdn_domain_name
        

    def batch_delete_scdn_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_delete_scdn_domain_configs(scdn_domain_name=self.scdn_domain_name, **_params)

    def batch_set_scdn_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_set_scdn_domain_configs(scdn_domain_name=self.scdn_domain_name, **_params)

    def batch_update(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_update_scdn_domain(scdn_domain_name=self.scdn_domain_name, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_scdn_domain(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_certificate_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_certificate_info(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_cname(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_cname(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_configs(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_detail(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_log(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_log(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_pv_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_pv_data(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_real_time_bps_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_real_time_bps_data(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_real_time_byte_hit_rate_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_real_time_byte_hit_rate_data(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_real_time_http_code_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_real_time_http_code_data(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_real_time_qps_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_real_time_qps_data(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_real_time_req_hit_rate_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_real_time_req_hit_rate_data(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_real_time_src_bps_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_real_time_src_bps_data(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_real_time_src_traffic_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_real_time_src_traffic_data(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_real_time_traffic_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_real_time_traffic_data(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_top_refer_visit(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_top_refer_visit(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_top_url_visit(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_top_url_visit(scdn_domain_name=self.scdn_domain_name, **_params)

    def describe_scdn_domain_uv_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_scdn_domain_uv_data(scdn_domain_name=self.scdn_domain_name, **_params)

    def set_domain_server_certificate(self, **params):
        _params = _transfer_params(params)
        return self._client.set_domain_server_certificate(scdn_domain_name=self.scdn_domain_name, **_params)

    def set_scdn_domain_certificate(self, **params):
        _params = _transfer_params(params)
        return self._client.set_scdn_domain_certificate(scdn_domain_name=self.scdn_domain_name, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        return self._client.start_scdn_domain(scdn_domain_name=self.scdn_domain_name, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_scdn_domain(scdn_domain_name=self.scdn_domain_name, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_scdn_domain(scdn_domain_name=self.scdn_domain_name, **_params)
