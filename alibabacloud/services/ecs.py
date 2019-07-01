# Copyright 2018 Alibaba Cloud Inc. All rights reserved.
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


class ECSInstanceResource(ServiceResource):
    """
    Ecs 实例资源类

    :param instance_id: 实例ID
    :type instance_id: str

    :param _client:  Alibaba Cloud Client
    :type _client: alibaba.client.AlibabaCloudClient

    """

    STATUS_RUNNING = "Running"
    STATUS_STARTING = "Starting"
    STATUS_STOPPING = "Stopping"
    STATUS_STOPPED = "Stopped"

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, 'ecs.instance', _client=_client)
        self.instance_id = instance_id
        _assert_is_not_none(instance_id, "instance_id")
        self.region_id = None
        self.inner_ip_address = None
        self.creation_time = None
        self.expired_time = None
        self.io_optimized = None
        self.public_ip_address = None
        self.internet_charge_type = None
        self.vpc_attributes = None
        self.status = None
        self.host_name = None
        self.image_id = None
        self.instance_charge_type = None
        self.instance_network_type = None
        self.instance_type = None
        self.eip_address = None
        self.serial_number = None
        self.operation_locks = None
        self.security_group_ids = None
        self.internet_max_bandwidth_out = None
        self.zone_id = None
        self.instance_name = None
        self.internet_max_bandwidth_in = None
        self.device_available = None

    def refresh(self):
        result = self._client.describe_instances(instance_ids=json.dumps([self.instance_id]))
        items = _new_get_key_in_response(result, 'Instances.Instance')
        if not items:
            raise ClientException(msg=
                                  "Failed to find instance data from DescribeInstances response. "
                                  "InstanceId = {0}".format(self.instance_id))
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

    def wait_until_running(self):
        self.wait_until(self.STATUS_RUNNING)

    def wait_until_starting(self):
        self.wait_until(self.STATUS_STARTING)

    def wait_until_stopping(self):
        self.wait_until(self.STATUS_STOPPING)

    def wait_until_stopped(self):
        self.wait_until(self.STATUS_STOPPED)

    def start(self):
        self._client.start_instance(instance_id=self.instance_id)

    def stop(self):
        self._client.stop_instance(instance_id=self.instance_id)

    def reboot(self):
        self._client.reboot_instance(instance_id=self.instance_id)

    def delete(self):
        self._client.delete_instance(instance_id=self.instance_id)

    def redeploy(self, **params):
        _params = _transfer_params(params)
        self._client.redeploy_instance(instance_id=self.instance_id, **_params)

    def modify_attributes(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_attribute(instance_id=self.instance_id, **_params)
        self.refresh()

    def replace_system_disk(self, **params):
        _params = _transfer_params(params)
        response = self._client.replace_system_disk(instance_id=self.instance_id, **_params)
        return response['DiskId']

    def modify_vnc_password(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_vnc_passwd(instance_id=self.instance_id, **_params)


class ECSSystemEventResource(ServiceResource):
    """
    ECS 系统事件资源类

    :param event_id: 事件id
    :type event_id: str

    :param _client:  Alibaba Cloud Client
    :type _client: alibaba.client.AlibabaCloudClient

    """

    class EventCycleStatus:
        """
        Scheduled: The event is waiting for processing.
        Avoided: You have fixed the event before it is complete.
        Executing: The event is in processing.
        Executed: Event progress is complete.
        Canceled: The event is canceled.
        Failed: Event progress failed.
        """
        SCHEDULED = "Scheduled"
        AVOIDED = "Avoided"
        EXECUTING = "Executing"
        EXECUTED = "Executed"
        CANCELED = "Canceled"
        FAILED = "Failed"

    class EventType:
        """
        SystemMaintenance.Reboot: Reboot due to system maintenance instance.
        SystemFailure.Reboot: Restart due to system error instance.
        InstanceFailure.Reboot: Restart due to instance error.
        InstanceExpiration.Stop: Subscription instances stop due to expiration.
        InstanceExpiration.Delete:
            Subscription instances are released after several days of expiration.
        AccountUnbalanced.Stop: Pay-As-You-Go instances stop due to expiration.
        AccountUnbalanced.Delete:
            Pay-As-You-Go instances are released after several days of expiration.
        """
        SYSTEM_MAINTENANCE_REBOOT = "SystemMaintenance.Reboot"
        SYSTEM_FAILURE_REBOOT = "SystemFailure.Reboot"
        INSTANCE_FAILURE_REBOOT = "InstanceFailure.Reboot"
        INSTANCE_EXPIRATION_STOP = "InstanceExpiration.Stop"
        INSTANCE_EXPIRATION_DELETE = "InstanceExpiration.Delete"
        ACCOUNT_UNBALANCED_STOP = "AccountUnbalanced.Stop"
        ACCOUNT_UNBALANCED_DELETE = "AccountUnbalanced.Delete"

    def __init__(self, event_id, _client=None):
        self.event_id = event_id
        self.event_finish_time = None
        _assert_is_not_none(event_id, "event_id")
        ServiceResource.__init__(self, "ecs.event", _client=_client)

    def refresh(self):
        response = self._client.describe_instance_history_events(event_id=[self.event_id, ])
        items = _new_get_key_in_response(response, 'InstanceSystemEventSet.InstanceSystemEventType')
        if not items:
            raise ClientException(msg=
                                  "Failed to find event data from "
                                  "DescribeInstanceHistoryEventsRequest response. "
                                  "EventId = {0}".format(self.event_id))
        self._assign_attributes(items[0])

    def get_event_type(self):
        if not hasattr(self, "event_type"):
            return None
        return self.event_type.search("Name")

    def get_event_cycle_status(self):
        if not hasattr(self, "event_cycle_status"):
            return None
        return self.event_cycle_status.search("Name")


class ECSInstanceFullStatus(ServiceResource):
    """ECS 实例状态资源类"""

    def _assign_attributes(self, attrs):
        ServiceResource._assign_attributes(self, attrs)
        self.system_events = []
        system_events_data = self.scheduled_system_event_set.search('ScheduledSystemEventType')
        for item in system_events_data:
            event_id = item.get('EventId')
            event = ECSSystemEventResource(event_id)
            event._assign_attributes(item)
            self.system_events.append(event)


class ECSDiskResource(ServiceResource):
    """
    ECS 硬盘资源类

    :param disk_id: 硬盘id
    :type disk_id: str

    :param _client:  Alibaba Cloud Client
    :type _client: alibaba.client.AlibabaCloudClient

    """

    def __init__(self, disk_id, _client=None):
        self.disk_id = disk_id
        _assert_is_not_none(disk_id, "disk_id")
        ServiceResource.__init__(self, "ecs.disk", _client=_client)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_disk(disk_id=self.disk_id, **_params)

    def attach(self, **params):
        _params = _transfer_params(params)
        self._client.attach_disk(disk_id=self.disk_id, **_params)

    def detach(self, **params):
        _params = _transfer_params(params)
        self._client.detach_disk(disk_id=self.disk_id, **_params)

    def modify_attributes(self, **params):
        _params = _transfer_params(params)
        self._client.modify_disk_attribute(disk_id=self.disk_id, **_params)
        self.refresh()

    def refresh(self):
        response = self._client.describe_disks(disk_ids=json.dumps([self.disk_id]))
        items = _new_get_key_in_response(response, 'Disks.Disk')
        if not items:
            raise ClientException(msg=
                                  "Failed to find disk data from DescribeDiks "
                                  "response. "
                                  "DiskId = {0}".format(self.disk_id))
        self._assign_attributes(items[0])

    def reinit(self, **params):
        _params = _transfer_params(params)
        self._client.re_init_disk(disk_id=self.disk_id, **_params)

    def resize(self, **params):
        _params = _transfer_params(params)
        self._client.resize_disk(disk_id=self.disk_id, **_params)

    def reset(self, **params):
        _params = _transfer_params(params)
        self._client.reset_disk(disk_id=self.disk_id, **_params)


class ECSImageResource(ServiceResource):
    """
    Ecs 镜像资源类

    :param image_id: 镜像id
    :type image_id:  str

    :param _client:  Alibaba Cloud Client
    :type _client: alibaba.client.AlibabaCloudClient

    """

    def __init__(self, image_id, _client=None):
        self.image_id = image_id
        _assert_is_not_none(image_id, "image_id")
        ServiceResource.__init__(self, "ecs.image", _client=_client)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_image(image_id=self.image_id, **_params)

    def modify_attributes(self, **params):
        _params = _transfer_params(params)
        self._client.modify_image_attribute(image_id=self.image_id, **_params)
        self.refresh()

    def refresh(self):
        response = self._client.describe_images(image_id=self.image_id)
        items = _new_get_key_in_response(response, 'Images.Image')
        if not items:
            raise ClientException(msg=
                                  "Failed to find image data from DescribeImages "
                                  "response. "
                                  "ImageId = {0}".format(self.image_id))
        self._assign_attributes(items[0])


class ECSTagResource(ServiceResource):
    pass


class ECSDemand(ServiceResource):
    pass


class ECSResource(ServiceResource):
    """
    ECS 资源类

    :param _client:  Alibaba Cloud Client
    :type _client: alibaba.client.AlibabaCloudClient

    """

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ecs', _client=_client)
        self.instances = _create_resource_collection(
            ECSInstanceResource, _client, _client.describe_instances,
            'Instances.Instance', 'InstanceId',
            singular_param_to_json={'instance_id': 'InstanceIds'},
            plural_param_to_json={
                'instance_ids': 'InstanceIds',
                'list_of_instance_id': 'InstanceIds',
                'list_of_private_ip_address': 'PrivateIpAddresses',
                'list_of_inner_ip_address': 'InnerIpAddresses',
                'list_of_public_ip_address': 'PublicIpAddresses',
                'list_of_eip_address': 'EipAddresses',
            }
        )
        self.system_events = _create_resource_collection(
            ECSSystemEventResource, _client, _client.describe_instance_history_events,
            'InstanceSystemEventSet.InstanceSystemEventType', 'EventId',
            param_aliases={
                'list_of_event_id': 'EventIds',
                'list_of_event_cycle_status': 'InstanceEventCycleStatuss',
                'list_of_event_type': 'InstanceEventTypes'
            }
        )

        self.instance_full_statuses = _create_default_resource_collection(
            ECSInstanceFullStatus, _client, _client.describe_instances_full_status,
            'InstanceFullStatusSet.InstanceFullStatusType',
        )

        self.disks = _create_resource_collection(
            ECSDiskResource, _client, _client.describe_disks,
            'Disks.Disk', 'DiskId',
            plural_param_to_json={
                'list_of_disk_id': 'DiskIds',
            }
        )

        self.images = _create_resource_collection(
            ECSImageResource, _client, _client.describe_images,
            'Images.Image', 'ImageId',
        )

        self.tags = _create_default_resource_collection(
            ECSTagResource, _client, _client.describe_tags,
            'Tags.Tag',
        )

        self.demands = _create_default_resource_collection(
            ECSDemand, _client, _client.describe_demands,
            'Demands.Demand',
        )

    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return ECSInstanceResource(instance_id, _client=self._client)

    def run_instances(self, **params):
        _params = _transfer_params(params)
        response = self._client.run_instances(**_params)
        instance_ids = _new_get_key_in_response(response, 'InstanceIdSets.InstanceIdSet')

        instances = []
        for instance_id in instance_ids:
            instance = ECSInstanceResource(instance_id, _client=self._client)
            instances.append(instance)
        return instances

    def create_simulated_system_events(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_simulated_system_events(**_params)
        event_ids = _new_get_key_in_response(response, 'EventIdSet.EventId')
        events = []
        for event_id in event_ids:
            event = ECSSystemEventResource(event_id, _client=self._client)
            events.append(event)
        return events

    def cancel_simulated_system_events(self, **params):
        _params = _transfer_params(params)
        self._client.cancel_simulated_system_events(**_params)

    def create_disk(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_disk(**params)
        disk_id = _new_get_key_in_response(response, 'DiskId')
        return ECSDiskResource(disk_id, _client=self._client)

    def create_image(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_image(**params)
        image_id = _new_get_key_in_response(response, 'ImageId')
        return ECSImageResource(image_id, _client=self._client)

    def add_tags(self, **params):
        _params = _transfer_params(params)
        self._client.add_tags(**_params)

    def remove_tags(self, **params):
        _params = _transfer_params(params)
        self._client.remove_tags(**_params)
