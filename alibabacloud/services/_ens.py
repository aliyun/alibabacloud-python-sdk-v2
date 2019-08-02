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
from alibabacloud.resources.collection import _create_resource_collection
from alibabacloud.resources.collection import _create_default_resource_collection
from alibabacloud.utils.utils import _assert_is_not_none, _new_get_key_in_response, _transfer_params


class _ENSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ens', _client=_client)
        self.ens_regions = _create_resource_collection(
            _ENSEnsRegionResource, _client, _client.describe_ens_regions,
            'EnsRegions.EnsRegions', 'EnsRegionId',
        )
        self.images = _create_resource_collection(
            _ENSImageResource, _client, _client.describe_images,
            'Images.Image', 'ImageId',
        )
class _ENSEnsRegionResource(ServiceResource):

    def __init__(self, ens_region_id, _client=None):
        ServiceResource.__init__(self, "ens.ens_region", _client=_client)
        self.ens_region_id = ens_region_id

        self.area = None
        self.en_name = None
        self.name = None
        self.province = None

    def refresh(self):
        result = self._client.describe_ens_regions(ens_region_id=json.dumps([self.ens_region_id],))
        items = _new_get_key_in_response(result, 'EnsRegions.EnsRegions')
        if not items:
            raise ClientException(msg=
                                  "Failed to find ens_region data from DescribeEnsRegions response. "
                                  "EnsRegionId = {0}".format(self.ens_region_id))
        self._assign_attributes(items[0])

class _ENSImageResource(ServiceResource):

    def __init__(self, image_id, _client=None):
        ServiceResource.__init__(self, "ens.image", _client=_client)
        self.image_id = image_id

        self.architecture = None
        self.creation_time = None
        self.description = None
        self.disk_device_mappings = None
        self.image_name = None
        self.image_owner_alias = None
        self.image_version = None
        self.is_copied = None
        self.is_self_shared = None
        self.is_subscribed = None
        self.is_support_cloudinit = None
        self.is_support_io_optimized = None
        self.os_name = None
        self.os_name_en = None
        self.os_type = None
        self.platform = None
        self.product_code = None
        self.progress = None
        self.resource_group_id = None
        self.size = None
        self.status = None
        self.tags = None
        self.usage = None

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_image_attribute(image_id=self.image_id, **_params)

    def refresh(self):
        result = self._client.describe_images(image_id=json.dumps([self.image_id],))
        items = _new_get_key_in_response(result, 'Images.Image')
        if not items:
            raise ClientException(msg=
                                  "Failed to find image data from DescribeImages response. "
                                  "ImageId = {0}".format(self.image_id))
        self._assign_attributes(items[0])

class _ENSInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "ens.instance", _client=_client)
        self.instance_id = instance_id


    def create(self, **params):
        _params = _transfer_params(params)
        self._client.create_instance(instance_id=self.instance_id, **_params)

    def reboot(self, **params):
        _params = _transfer_params(params)
        self._client.reboot_instance(instance_id=self.instance_id, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        self._client.start_instance(instance_id=self.instance_id, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        self._client.stop_instance(instance_id=self.instance_id, **_params)
