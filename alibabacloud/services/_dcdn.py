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


class _DCDNResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'dcdn', _client=_client)
    def add_dcdn_domain(self, **params):
        _params = _transfer_params(params)
        self._client.add_dcdn_domain(**_params)
        dcdn_domain_name = _params.get("dcdn_domain_name")
        return _DCDNDcdnDomainResource(dcdn_domain_name, _client=self._client)

class _DCDNDcdnDomainResource(ServiceResource):

    def __init__(self, dcdn_domain_name, _client=None):
        ServiceResource.__init__(self, "dcdn.dcdn_domain", _client=_client)
        self.dcdn_domain_name = dcdn_domain_name
        

    def batch_delete_dcdn_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_delete_dcdn_domain_configs(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def batch_set_dcdn_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_set_dcdn_domain_configs(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def batch_set_dcdn_ipa_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_set_dcdn_ipa_domain_configs(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def batch_start(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_start_dcdn_domain(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def batch_stop(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_stop_dcdn_domain(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def add_dcdn_ipa_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.add_dcdn_ipa_domain(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_dcdn_domain(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def delete_dcdn_ipa_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_dcdn_ipa_domain(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def delete_dcdn_specific_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_dcdn_specific_config(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_certificate_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_certificate_info(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_cname(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_cname(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_configs(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_detail(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_http_code_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_http_code_data(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_log(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_log(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_pv_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_pv_data(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_real_time_bps_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_real_time_bps_data(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_real_time_byte_hit_rate_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_real_time_byte_hit_rate_data(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_real_time_http_code_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_real_time_http_code_data(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_real_time_qps_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_real_time_qps_data(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_real_time_req_hit_rate_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_real_time_req_hit_rate_data(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_real_time_src_bps_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_real_time_src_bps_data(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_real_time_src_traffic_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_real_time_src_traffic_data(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_top_refer_visit(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_top_refer_visit(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_top_url_visit(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_top_url_visit(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_uv_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_uv_data(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_domain_websocket_http_code_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_domain_websocket_http_code_data(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_ipa_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_ipa_domain_configs(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def describe_dcdn_ipa_domain_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dcdn_ipa_domain_detail(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def modify_dcdn_domain_schdm_by_property(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_dcdn_domain_schdm_by_property(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def set_dcdn_domain_certificate(self, **params):
        _params = _transfer_params(params)
        return self._client.set_dcdn_domain_certificate(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        return self._client.start_dcdn_domain(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def start_dcdn_ipa_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.start_dcdn_ipa_domain(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_dcdn_domain(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def stop_dcdn_ipa_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_dcdn_ipa_domain(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_dcdn_domain(dcdn_domain_name=self.dcdn_domain_name, **_params)

    def update_dcdn_ipa_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.update_dcdn_ipa_domain(dcdn_domain_name=self.dcdn_domain_name, **_params)
