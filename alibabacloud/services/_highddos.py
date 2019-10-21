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


class _HIGHDDOSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'highddos', _client=_client)
    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _HIGHDDOSInstanceResource(instance_id, _client=self._client)

class _HIGHDDOSInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "highddos.instance", _client=_client)
        self.instance_id = instance_id
        

    def create_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.create_domain(instance_id=self.instance_id, **_params)

    def create_lay4_rule(self, **params):
        _params = _transfer_params(params)
        return self._client.create_lay4_rule(instance_id=self.instance_id, **_params)

    def delete_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_domain(instance_id=self.instance_id, **_params)

    def delete_lay4_rule(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_lay4_rule(instance_id=self.instance_id, **_params)

    def describe_cc_events(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cc_events(instance_id=self.instance_id, **_params)

    def describe_cc_flow(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cc_flow(instance_id=self.instance_id, **_params)

    def describe_ddos_events(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ddos_events(instance_id=self.instance_id, **_params)

    def describe_ddos_flow(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ddos_flow(instance_id=self.instance_id, **_params)

    def describe_domains(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_domains(instance_id=self.instance_id, **_params)

    def describe_lay4_rules(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_lay4_rules(instance_id=self.instance_id, **_params)

    def describe_waf_attack_events(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_waf_attack_events(instance_id=self.instance_id, **_params)

    def describe_waf_attack_source_stats(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_waf_attack_source_stats(instance_id=self.instance_id, **_params)

    def describe_waf_attack_type_stats(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_waf_attack_type_stats(instance_id=self.instance_id, **_params)

    def describe_waf_attack_url_stats(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_waf_attack_url_stats(instance_id=self.instance_id, **_params)

    def modify_cc_config(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_cc_config(instance_id=self.instance_id, **_params)

    def modify_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_domain(instance_id=self.instance_id, **_params)

    def modify_lay4_rule(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_lay4_rule(instance_id=self.instance_id, **_params)

    def modify_waf_config(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_waf_config(instance_id=self.instance_id, **_params)

    def release(self, **params):
        _params = _transfer_params(params)
        return self._client.release_instance(instance_id=self.instance_id, **_params)

    def renew(self, **params):
        _params = _transfer_params(params)
        return self._client.renew_instance(instance_id=self.instance_id, **_params)

    def upgrade(self, **params):
        _params = _transfer_params(params)
        return self._client.upgrade_instance(instance_id=self.instance_id, **_params)

    def upload_https_cert(self, **params):
        _params = _transfer_params(params)
        return self._client.upload_https_cert(instance_id=self.instance_id, **_params)

    def upload_https_key(self, **params):
        _params = _transfer_params(params)
        return self._client.upload_https_key(instance_id=self.instance_id, **_params)
