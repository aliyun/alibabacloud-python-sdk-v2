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


class _PVTZResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'pvtz', _client=_client)
        self.regions = _create_special_resource_collection(
            _PVTZRegionResource, _client, _client.describe_regions,
            'Regions.Region', 'RegionId', 
        )
        self.zones = _create_special_resource_collection(
            _PVTZZoneResource, _client, _client.describe_zones,
            'Zones.Zone', 'ZoneId', 
        )
        self.zone_records = _create_special_resource_collection(
            _PVTZZoneRecordResource, _client, _client.describe_zone_records,
            'Records.Record', 'RecordId', 
        )
    def add_zone(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_zone(**_params)
        zone_id = _new_get_key_in_response(response, 'ZoneId')
        return _PVTZZoneResource(zone_id, _client=self._client)

    def delete_zone(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_zone(**_params)
        zone_id = _new_get_key_in_response(response, 'ZoneId')
        return _PVTZZoneResource(zone_id, _client=self._client)

    def add_zone_record(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_zone_record(**_params)
        record_id = _new_get_key_in_response(response, 'RecordId')
        return _PVTZZoneRecordResource(record_id, _client=self._client)

    def delete_zone_record(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_zone_record(**_params)
        record_id = _new_get_key_in_response(response, 'RecordId')
        return _PVTZZoneRecordResource(record_id, _client=self._client)

    def update_zone_record(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_zone_record(**_params)
        record_id = _new_get_key_in_response(response, 'RecordId')
        return _PVTZZoneRecordResource(record_id, _client=self._client)

class _PVTZRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "pvtz.region", _client=_client)
        self.region_id = region_id
        
        self.local_name = None
        self.region_endpoint = None
        self.region_name = None

class _PVTZZoneResource(ServiceResource):

    def __init__(self, zone_id, _client=None):
        ServiceResource.__init__(self, "pvtz.zone", _client=_client)
        self.zone_id = zone_id
        
        self.create_time = None
        self.create_timestamp = None
        self.is_ptr = None
        self.proxy_pattern = None
        self.record_count = None
        self.remark = None
        self.update_time = None
        self.update_timestamp = None
        self.zone_name = None

    def bind_zone_vpc(self, **params):
        _params = _transfer_params(params)
        return self._client.bind_zone_vpc(zone_id=self.zone_id, **_params)

    def set_proxy_pattern(self, **params):
        _params = _transfer_params(params)
        return self._client.set_proxy_pattern(zone_id=self.zone_id, **_params)

    def update_zone_remark(self, **params):
        _params = _transfer_params(params)
        return self._client.update_zone_remark(zone_id=self.zone_id, **_params)

class _PVTZZoneRecordResource(ServiceResource):

    def __init__(self, record_id, _client=None):
        ServiceResource.__init__(self, "pvtz.zone_record", _client=_client)
        self.record_id = record_id
        
        self.priority = None
        self.rr = None
        self.status = None
        self.ttl = None
        self.type_ = None
        self.value = None

    def set_zone_record_status(self, **params):
        _params = _transfer_params(params)
        return self._client.set_zone_record_status(record_id=self.record_id, **_params)
