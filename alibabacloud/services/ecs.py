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

from aliyunsdkcore.acs_exception.exceptions import ClientException

from aliyunsdkecs.request.v20140526.CreateInstanceRequest import CreateInstanceRequest
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.StartInstanceRequest import StartInstanceRequest
from aliyunsdkecs.request.v20140526.StopInstanceRequest import StopInstanceRequest
from aliyunsdkecs.request.v20140526.DeleteInstanceRequest import DeleteInstanceRequest
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from aliyunsdkecs.request.v20140526.RebootInstanceRequest import RebootInstanceRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceAttributeRequest \
    import ModifyInstanceAttributeRequest
from aliyunsdkecs.request.v20140526.DescribeInstanceHistoryEventsRequest \
    import DescribeInstanceHistoryEventsRequest
from aliyunsdkecs.request.v20140526.CreateSimulatedSystemEventsRequest \
    import CreateSimulatedSystemEventsRequest
from aliyunsdkecs.request.v20140526.CancelSimulatedSystemEventsRequest \
    import CancelSimulatedSystemEventsRequest
from aliyunsdkecs.request.v20140526.DescribeInstancesFullStatusRequest \
    import DescribeInstancesFullStatusRequest
from aliyunsdkecs.request.v20140526.RedeployInstanceRequest import RedeployInstanceRequest
from aliyunsdkecs.request.v20140526.ModifyInstanceVncPasswdRequest \
    import ModifyInstanceVncPasswdRequest

from aliyunsdkecs.request.v20140526.DescribeDisksRequest import DescribeDisksRequest
from aliyunsdkecs.request.v20140526.DeleteDiskRequest import DeleteDiskRequest
from aliyunsdkecs.request.v20140526.AttachDiskRequest import AttachDiskRequest
from aliyunsdkecs.request.v20140526.DetachDiskRequest import DetachDiskRequest
from aliyunsdkecs.request.v20140526.ReInitDiskRequest import ReInitDiskRequest
from aliyunsdkecs.request.v20140526.ResizeDiskRequest import ResizeDiskRequest
from aliyunsdkecs.request.v20140526.ResetDiskRequest import ResetDiskRequest
from aliyunsdkecs.request.v20140526.ModifyDiskAttributeRequest import ModifyDiskAttributeRequest
from aliyunsdkecs.request.v20140526.ReplaceSystemDiskRequest import ReplaceSystemDiskRequest
from aliyunsdkecs.request.v20140526.CreateDiskRequest import CreateDiskRequest

from aliyunsdkecs.request.v20140526.DescribeTagsRequest import DescribeTagsRequest
from aliyunsdkecs.request.v20140526.AddTagsRequest import AddTagsRequest
from aliyunsdkecs.request.v20140526.RemoveTagsRequest import RemoveTagsRequest

from aliyunsdkecs.request.v20140526.CreateImageRequest import CreateImageRequest
from aliyunsdkecs.request.v20140526.DeleteImageRequest import DeleteImageRequest
from aliyunsdkecs.request.v20140526.DescribeImagesRequest import DescribeImagesRequest
from aliyunsdkecs.request.v20140526.ModifyImageAttributeRequest import ModifyImageAttributeRequest

from aliyunsdkecs.request.v20140526.DescribeDemandsRequest import DescribeDemandsRequest

from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection
from alibabacloud.resources.collection import _create_default_resource_collection
from alibabacloud.utils import _do_request, _get_response, _assert_is_not_none
import alibabacloud.errors as errors


class ECSInstanceResource(ServiceResource):

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
        request = DescribeInstancesRequest()
        request.set_InstanceIds(json.dumps([self.instance_id]))
        items = _get_response(self._client, request, {}, 'Instances.Instance')
        if not items:
            raise ClientException(errors.ERROR_INVALID_SERVER_RESPONSE,
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
        request = StartInstanceRequest()
        request.set_InstanceId(self.instance_id)
        _do_request(self._client, request, {})

    def stop(self):
        request = StopInstanceRequest()
        request.set_InstanceId(self.instance_id)
        _do_request(self._client, request, {})

    def reboot(self):
        request = RebootInstanceRequest()
        request.set_InstanceId(self.instance_id)
        _do_request(self._client, request, {})

    def delete(self):
        request = DeleteInstanceRequest()
        request.set_InstanceId(self.instance_id)
        _do_request(self._client, request, {})

    def redeploy(self, **params):
        request = RedeployInstanceRequest()
        request.set_InstanceId(self.instance_id)
        _do_request(self._client, request, params)

    def modify_attributes(self, **params):
        request = ModifyInstanceAttributeRequest()
        request.set_InstanceId(self.instance_id)
        _do_request(self._client, request, params)
        self.refresh()

    def replace_system_disk(self, **params):
        request = ReplaceSystemDiskRequest()
        request.set_InstanceId(self.instance_id)
        response = _do_request(self._client, request, params)
        return response['DiskId']

    def modify_vnc_password(self, **params):
        request = ModifyInstanceVncPasswdRequest()
        request.set_InstanceId(self.instance_id)
        _do_request(self._client, request, params)


class ECSSystemEventResource(ServiceResource):

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
        request = DescribeInstanceHistoryEventsRequest()
        request.set_EventIds([self.event_id])
        items = _get_response(self._client, request, {},
                              'InstanceSystemEventSet.InstanceSystemEventType')
        if not items:
            raise ClientException(errors.ERROR_INVALID_SERVER_RESPONSE,
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

    def __init__(self, disk_id, _client=None):
        self.disk_id = disk_id
        _assert_is_not_none(disk_id, "disk_id")
        ServiceResource.__init__(self, "ecs.disk", _client=_client)

    def delete(self, **params):
        request = DeleteDiskRequest()
        request.set_DiskId(self.disk_id)
        _do_request(self._client, request, params)

    def attach(self, **params):
        request = AttachDiskRequest()
        request.set_DiskId(self.disk_id)
        _do_request(self._client, request, params)

    def detach(self, **params):
        request = DetachDiskRequest()
        request.set_DiskId(self.disk_id)
        _do_request(self._client, request, params)

    def modify_attributes(self, **params):
        request = ModifyDiskAttributeRequest()
        request.set_InstanceId(self.disk_id)
        _do_request(self._client, request, params)
        self.refresh()

    def refresh(self):
        request = DescribeDisksRequest()
        request.set_DiskIds(json.dumps([self.disk_id]))
        items = _get_response(self._client, request, {}, 'Disks.Disk')
        if not items:
            raise ClientException(errors.ERROR_INVALID_SERVER_RESPONSE,
                                  "Failed to find disk data from DescribeDiks "
                                  "response. "
                                  "DiskId = {0}".format(self.disk_id))
        self._assign_attributes(items[0])

    def reinit(self, **params):
        request = ReInitDiskRequest()
        request.set_DiskId(self.disk_id)
        _do_request(self._client, request, params)

    def resize(self, **params):
        request = ResizeDiskRequest()
        request.set_DiskId(self.disk_id)
        _do_request(self._client, request, params)

    def reset(self, **params):
        request = ResetDiskRequest()
        request.set_DiskId(self.disk_id)
        _do_request(self._client, request, params)


class ECSImageResource(ServiceResource):

    def __init__(self, image_id, _client=None):
        self.image_id = image_id
        _assert_is_not_none(image_id, "image_id")
        ServiceResource.__init__(self, "ecs.image", _client=_client)

    def delete(self, **params):
        request = DeleteImageRequest()
        request.set_ImageId(self.image_id)
        _do_request(self._client, request, params)

    def modify_attributes(self, **params):
        request = ModifyImageAttributeRequest()
        request.set_ImageId(self.image_id)
        _do_request(self._client, request, params)
        self.refresh()

    def refresh(self):
        request = DescribeImagesRequest()
        request.set_ImageId(self.image_id)
        items = _get_response(self._client, request, {}, 'Images.Image')
        if not items:
            raise ClientException(errors.ERROR_INVALID_SERVER_RESPONSE,
                                  "Failed to find image data from DescribeImages "
                                  "response. "
                                  "ImageId = {0}".format(self.image_id))
        self._assign_attributes(items[0])


class ECSTagResource(ServiceResource):
    pass


class ECSDemand(ServiceResource):
    pass


class ECSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ecs', _client=_client)
        self.instances = _create_resource_collection(
            ECSInstanceResource, _client, DescribeInstancesRequest,
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
            ECSSystemEventResource, _client, DescribeInstanceHistoryEventsRequest,
            'InstanceSystemEventSet.InstanceSystemEventType', 'EventId',
            param_aliases={
                'list_of_event_id': 'EventIds',
                'list_of_event_cycle_status': 'InstanceEventCycleStatuss',
                'list_of_event_type': 'InstanceEventTypes'
            }
        )

        self.instance_full_statuses = _create_default_resource_collection(
            ECSInstanceFullStatus, _client, DescribeInstancesFullStatusRequest,
            'InstanceFullStatusSet.InstanceFullStatusType',
        )

        self.disks = _create_resource_collection(
            ECSDiskResource, _client, DescribeDisksRequest,
            'Disks.Disk', 'DiskId',
            plural_param_to_json={
                'list_of_disk_id': 'DiskIds',
            }
        )

        self.images = _create_resource_collection(
            ECSImageResource, _client, DescribeImagesRequest,
            'Images.Image', 'ImageId',
        )

        self.tags = _create_default_resource_collection(
            ECSTagResource, _client, DescribeTagsRequest,
            'Tags.Tag',
        )

        self.demands = _create_default_resource_collection(
            ECSDemand, _client, DescribeDemandsRequest,
            'Demands',
        )

    def create_instance(self, **params):
        request = CreateInstanceRequest()
        instance_id = _get_response(self._client, request, params, key='InstanceId')
        return ECSInstanceResource(instance_id, _client=self._client)

    def run_instances(self, **params):
        request = RunInstancesRequest()
        instance_ids = _get_response(self._client, request, params, 'InstanceIdSets.InstanceIdSet')

        instances = []
        for instance_id in instance_ids:
            instance = ECSInstanceResource(instance_id, _client=self._client)
            instances.append(instance)
        return instances

    def create_simulated_system_events(self, **params):
        request = CreateSimulatedSystemEventsRequest()
        event_ids = _get_response(self._client, request, params, "EventIdSet.EventId")
        events = []
        for event_id in event_ids:
            event = ECSSystemEventResource(event_id, _client=self._client)
            events.append(event)
        return events

    def cancel_simulated_system_events(self, **params):
        request = CancelSimulatedSystemEventsRequest()
        _do_request(self._client, request, params)

    def create_disk(self, **params):
        request = CreateDiskRequest()
        disk_id = _get_response(self._client, request, params, key='DiskId')
        return ECSDiskResource(disk_id, _client=self._client)

    def create_image(self, **params):
        request = CreateImageRequest()
        image_id = _get_response(self._client, request, params, key='ImageId')
        return ECSImageResource(image_id, _client=self._client)

    def add_tags(self, **params):
        request = AddTagsRequest()
        _do_request(self._client, request, params)

    def remove_tags(self, **params):
        request = RemoveTagsRequest()
        _do_request(self._client, request, params)
