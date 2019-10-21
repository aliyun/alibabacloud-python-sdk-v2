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


class _LINKWANResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'linkwan', _client=_client)
        self.regions = _create_special_resource_collection(
            _LINKWANRegionResource, _client, _client.describe_regions,
            'Data.Region', 'RegionId',
        )

    def create_lab_node(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_lab_node(**_params)
        freq_band_plan_group_id = _new_get_key_in_response(response, 'FreqBandPlanGroupId')
        return _LINKWANLabNodeResource(freq_band_plan_group_id, _client=self._client)

    def get_lab_node(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_lab_node(**_params)
        freq_band_plan_group_id = _new_get_key_in_response(response, 'FreqBandPlanGroupId')
        return _LINKWANLabNodeResource(freq_band_plan_group_id, _client=self._client)

    def get_notification(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_notification(**_params)
        notification_id = _new_get_key_in_response(response, 'NotificationId')
        return _LINKWANNotificationResource(notification_id, _client=self._client)


class _LINKWANLabNodeResource(ServiceResource):

    def __init__(self, freq_band_plan_group_id, _client=None):
        ServiceResource.__init__(self, "linkwan.lab_node", _client=_client)
        self.freq_band_plan_group_id = freq_band_plan_group_id

    def apply_roaming_join_permission(self, **params):
        _params = _transfer_params(params)
        return self._client.apply_roaming_join_permission(
            freq_band_plan_group_id=self.freq_band_plan_group_id, **_params)

    def create_custom_local_join_permission(self, **params):
        _params = _transfer_params(params)
        return self._client.create_custom_local_join_permission(
            freq_band_plan_group_id=self.freq_band_plan_group_id, **_params)

    def create_gateway(self, **params):
        _params = _transfer_params(params)
        return self._client.create_gateway(freq_band_plan_group_id=self.freq_band_plan_group_id,
                                           **_params)

    def create_lab_gateway(self, **params):
        _params = _transfer_params(params)
        return self._client.create_lab_gateway(freq_band_plan_group_id=self.freq_band_plan_group_id,
                                               **_params)

    def create_local_join_permission(self, **params):
        _params = _transfer_params(params)
        return self._client.create_local_join_permission(
            freq_band_plan_group_id=self.freq_band_plan_group_id, **_params)


class _LINKWANNotificationResource(ServiceResource):

    def __init__(self, notification_id, _client=None):
        ServiceResource.__init__(self, "linkwan.notification", _client=_client)
        self.notification_id = notification_id

    def update_notifications_handle_state(self, **params):
        _params = _transfer_params(params)
        return self._client.update_notifications_handle_state(notification_id=self.notification_id,
                                                              **_params)


class _LINKWANRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "linkwan.region", _client=_client)
        self.region_id = region_id

        self.local_name = None
