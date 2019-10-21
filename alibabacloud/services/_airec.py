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


class _AIRECResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'airec', _client=_client)
        self.instances = _create_special_resource_collection(
            _AIRECInstanceResource, _client, _client.list_instance,
            'Result.Result', 'InstanceId',
        )
        self.regions = _create_special_resource_collection(
            _AIRECRegionResource, _client, _client.describe_regions,
            'Result.Item', 'RegionId',
        )

    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _AIRECInstanceResource(instance_id, _client=self._client)

    def upgrade_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.upgrade_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _AIRECInstanceResource(instance_id, _client=self._client)


class _AIRECInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "airec.instance", _client=_client)
        self.instance_id = instance_id

        self.charge_type = None
        self.commodity_code = None
        self.data_set_version = None
        self.expired_time = None
        self.gmt_create = None
        self.gmt_modified = None
        self.industry = None
        self.lock_mode = None
        self.name = None
        self.region_id = None
        self.scene = None
        self.status = None
        self.type_ = None

    def attach_dataset(self, **params):
        _params = _transfer_params(params)
        return self._client.attach_dataset(instance_id=self.instance_id, **_params)

    def create_diversify(self, **params):
        _params = _transfer_params(params)
        return self._client.create_diversify(instance_id=self.instance_id, **_params)

    def create_mix(self, **params):
        _params = _transfer_params(params)
        return self._client.create_mix(instance_id=self.instance_id, **_params)

    def delete_data_set(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_data_set(instance_id=self.instance_id, **_params)

    def delete_diversify(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_diversify(instance_id=self.instance_id, **_params)

    def delete_mix(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_mix(instance_id=self.instance_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_instance(instance_id=self.instance_id, **_params)

    def describe_data_set_message(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_data_set_message(instance_id=self.instance_id, **_params)

    def describe_data_set_report(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_data_set_report(instance_id=self.instance_id, **_params)

    def describe_diversify(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_diversify(instance_id=self.instance_id, **_params)

    def describe_exposure_settings(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_exposure_settings(instance_id=self.instance_id, **_params)

    def describe_mix(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_mix(instance_id=self.instance_id, **_params)

    def describe_quota(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_quota(instance_id=self.instance_id, **_params)

    def list_dashboard(self, **params):
        _params = _transfer_params(params)
        return self._client.list_dashboard(instance_id=self.instance_id, **_params)

    def list_dashboard_parameters(self, **params):
        _params = _transfer_params(params)
        return self._client.list_dashboard_parameters(instance_id=self.instance_id, **_params)

    def list_dashboard_uid(self, **params):
        _params = _transfer_params(params)
        return self._client.list_dashboard_uid(instance_id=self.instance_id, **_params)

    def list_data_set(self, **params):
        _params = _transfer_params(params)
        return self._client.list_data_set(instance_id=self.instance_id, **_params)

    def list_data_source(self, **params):
        _params = _transfer_params(params)
        return self._client.list_data_source(instance_id=self.instance_id, **_params)

    def list_diversify(self, **params):
        _params = _transfer_params(params)
        return self._client.list_diversify(instance_id=self.instance_id, **_params)

    def list_instance_task(self, **params):
        _params = _transfer_params(params)
        return self._client.list_instance_task(instance_id=self.instance_id, **_params)

    def list_mix(self, **params):
        _params = _transfer_params(params)
        return self._client.list_mix(instance_id=self.instance_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_instance(instance_id=self.instance_id, **_params)

    def modify_data_source(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_data_source(instance_id=self.instance_id, **_params)

    def modify_diversify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_diversify(instance_id=self.instance_id, **_params)

    def modify_exposure_settings(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_exposure_settings(instance_id=self.instance_id, **_params)

    def modify_mix(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_mix(instance_id=self.instance_id, **_params)

    def push_document(self, **params):
        _params = _transfer_params(params)
        return self._client.push_document(instance_id=self.instance_id, **_params)

    def push_intervention(self, **params):
        _params = _transfer_params(params)
        return self._client.push_intervention(instance_id=self.instance_id, **_params)

    def recommend(self, **params):
        _params = _transfer_params(params)
        return self._client.recommend(instance_id=self.instance_id, **_params)

    def stop_data_set(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_data_set(instance_id=self.instance_id, **_params)

    def validate(self, **params):
        _params = _transfer_params(params)
        return self._client.validate_instance(instance_id=self.instance_id, **_params)


class _AIRECRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "airec.region", _client=_client)
        self.region_id = region_id

        self.console_url = None
        self.endpoint = None
        self.local_name = None
        self.status = None
