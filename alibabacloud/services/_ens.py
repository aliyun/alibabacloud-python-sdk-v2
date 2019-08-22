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


class _ENSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ens', _client=_client)
        self.ens_regions = _create_special_resource_collection(
            _ENSEnsRegionResource, _client, _client.describe_ens_regions,
            'EnsRegions.EnsRegions', 'EnsRegionId',
        )
        self.images = _create_resource_collection(
            _ENSImageResource, _client, _client.describe_images,
            'Images.Image', 'ImageId',
        )
        self.instances = _create_resource_collection(
            _ENSInstanceResource, _client, _client.describe_instances,
            'Instances.Instance', 'InstanceId',
        )
        self.instance_types = _create_special_resource_collection(
            _ENSInstanceTypeResource, _client, _client.describe_instance_types,
            'InstanceTypes.InstanceType', 'InstanceTypeId',
        )

    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_ids = _new_get_key_in_response(response, 'None')
        instances = []
        for instance_id in instance_ids:
            instance = _ENSInstanceResource(instance_id, _client=self._client)
            instances.append(instance)
        return instances


class _ENSEnsRegionResource(ServiceResource):

    def __init__(self, ens_region_id, _client=None):
        ServiceResource.__init__(self, "ens.ens_region", _client=_client)
        self.ens_region_id = ens_region_id

        self.area = None
        self.en_name = None
        self.name = None
        self.province = None

    def refresh(self):
        result = self._client.describe_ens_regions(ens_region_id=self.ens_region_id)
        items = _new_get_key_in_response(result, 'EnsRegions.EnsRegions')
        if not items:
            raise ClientException(
                msg="Failed to find ens_region data from DescribeEnsRegions response. "
                "EnsRegionId = {0}".format(
                    self.ens_region_id))
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
        result = self._client.describe_images(image_id=self.image_id)
        items = _new_get_key_in_response(result, 'Images.Image')
        if not items:
            raise ClientException(msg="Failed to find image data from DescribeImages response. "
                                  "ImageId = {0}".format(self.image_id))
        self._assign_attributes(items[0])


class _ENSInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "ens.instance", _client=_client)
        self.instance_id = instance_id

        self.auto_release_time = None
        self.cluster_id = None
        self.cpu = None
        self.creation_time = None
        self.credit_specification = None
        self.dedicated_host_attribute = None
        self.dedicated_instance_attribute = None
        self.deletion_protection = None
        self.deployment_set_id = None
        self.description = None
        self.device_available = None
        self.ecs_capacity_reservation_attr = None
        self.eip_address = None
        self.expired_time = None
        self.gpu_amount = None
        self.gpu_spec = None
        self.host_name = None
        self.hpc_cluster_id = None
        self.image_id = None
        self.inner_ip_address = None
        self.instance_charge_type = None
        self.instance_name = None
        self.instance_network_type = None
        self.instance_type = None
        self.instance_type_family = None
        self.internet_charge_type = None
        self.internet_max_bandwidth_in = None
        self.internet_max_bandwidth_out = None
        self.io_optimized = None
        self.key_pair_name = None
        self.local_storage_amount = None
        self.local_storage_capacity = None
        self.memory = None
        self.network_interfaces = None
        self.os_name = None
        self.os_name_en = None
        self.os_type = None
        self.operation_locks = None
        self.public_ip_address = None
        self.rdma_ip_address = None
        self.recyclable = None
        self.region_id = None
        self.resource_group_id = None
        self.sale_cycle = None
        self.security_group_ids = None
        self.serial_number = None
        self.spot_price_limit = None
        self.spot_strategy = None
        self.start_time = None
        self.status = None
        self.stopped_mode = None
        self.tags = None
        self.vlan_id = None
        self.vpc_attributes = None
        self.zone_id = None

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_attribute(instance_id=self.instance_id, **_params)

    def reboot(self, **params):
        _params = _transfer_params(params)
        self._client.reboot_instance(instance_id=self.instance_id, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        self._client.start_instance(instance_id=self.instance_id, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        self._client.stop_instance(instance_id=self.instance_id, **_params)

    def refresh(self):
        result = self._client.describe_instances(instance_ids=self.instance_id)
        items = _new_get_key_in_response(result, 'Instances.Instance')
        if not items:
            raise ClientException(
                msg="Failed to find instance data from DescribeInstances response. "
                "InstanceId = {0}".format(
                    self.instance_id))
        self._assign_attributes(items[0])

    def wait_until(self, target_status, timeout=120):
        start_time = time.time()
        while True:
            end_time = time.time()
            if end_time - start_time >= timeout:
                raise Exception("Timed out: no {0} status after {1} seconds.".format(
                    target_status, timeout))

            self.refresh()
            if self.status == target_status:
                return
            time.sleep(1)


class _ENSInstanceTypeResource(ServiceResource):

    def __init__(self, instance_type_id, _client=None):
        ServiceResource.__init__(self, "ens.instance_type", _client=_client)
        self.instance_type_id = instance_type_id

        self.baseline_credit = None
        self.cpu_core_count = None
        self.eni_private_ip_address_quantity = None
        self.eni_quantity = None
        self.gpu_amount = None
        self.gpu_spec = None
        self.initial_credit = None
        self.instance_bandwidth_rx = None
        self.instance_bandwidth_tx = None
        self.instance_family_level = None
        self.instance_pps_rx = None
        self.instance_pps_tx = None
        self.instance_type_family = None
        self.local_storage_amount = None
        self.local_storage_capacity = None
        self.local_storage_category = None
        self.memory_size = None
