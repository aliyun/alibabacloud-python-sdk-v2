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
from functools import wraps

from alibabacloud import ClientException
from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, \
    _create_default_resource_collection
from alibabacloud.services._ecs import _ECSDedicatedHostResource
from alibabacloud.services._ecs import _ECSDiskResource
from alibabacloud.services._ecs import _ECSInstanceResource
from alibabacloud.services._ecs import _ECSResource
from alibabacloud.services._ecs import _ECSSystemEventResource
from alibabacloud.utils.utils import _transfer_params, _new_get_key_in_response, _assert_is_not_none


class ECSDedicatedHostResource(_ECSDedicatedHostResource):
    STATUS_PERMANENTFAILURE = 'PermanentFailure'
    STATUS_RELEASED = 'Released'
    STATUS_CREATING = 'Creating'
    STATUS_AVAILABLE = 'Available'
    STATUS_UNDERASSESSMENT = 'UnderAssessment'

    def __init__(self, dedicatedhost_id, _client=None):
        _ECSDedicatedHostResource.__init__(self, dedicatedhost_id, _client=_client)

    def wait_until_permanentfailure(self):
        self.wait_until(self.STATUS_PERMANENTFAILURE)

    def wait_until_released(self):
        self.wait_until(self.STATUS_RELEASED)

    def wait_until_creating(self):
        self.wait_until(self.STATUS_CREATING)

    def wait_until_available(self):
        self.wait_until(self.STATUS_AVAILABLE)

    def wait_until_underassessment(self):
        self.wait_until(self.STATUS_UNDERASSESSMENT)


class ECSInstanceResource(_ECSInstanceResource):
    STATUS_STOPPING = 'Stopping'
    STATUS_STOPPED = 'Stopped'
    STATUS_TRANSFERRING = 'Transferring'
    STATUS_RUNNING = 'Running'
    STATUS_STARTING = 'Starting'
    STATUS_PENDING = 'Pending'
    STATUS_DELETED = 'Deleted'
    STATUS_RESETTING = 'Resetting'

    def __init__(self, instance_id, _client=None):
        _ECSInstanceResource.__init__(self, instance_id, _client=_client)

    def wait_until_stopping(self):
        self.wait_until(self.STATUS_STOPPING)

    def wait_until_stopped(self):
        self.wait_until(self.STATUS_STOPPED)

    def wait_until_transferring(self):
        self.wait_until(self.STATUS_TRANSFERRING)

    def wait_until_running(self):
        self.wait_until(self.STATUS_RUNNING)

    def wait_until_starting(self):
        self.wait_until(self.STATUS_STARTING)

    def wait_until_pending(self):
        self.wait_until(self.STATUS_PENDING)

    def wait_until_deleted(self):
        self.wait_until(self.STATUS_DELETED)

    def wait_until_resetting(self):
        self.wait_until(self.STATUS_RESETTING)

    def modify_attributes(self, **params):
        self.modify_attribute(**params)

    def refresh(self):
        result = self._client.describe_instances(instance_ids=json.dumps([self.instance_id, ]))
        items = _new_get_key_in_response(result, 'Instances.Instance')
        if not items:
            raise ClientException(msg=
                                  "Failed to find instance data from DescribeInstances response. "
                                  "InstanceId = {0}".format(self.instance_id))
        self._assign_attributes(items[0])


# 人工补充部分
# 对list_of_instance_id 以及instance_ids 进行映射处理
def transfer(rules):
    def decorator(func):
        @wraps(func)
        def wrapper(self, **params):
            for key, value in rules.items():
                # key is like: InstanceIds or instance_ids
                # value is like: list_of_instance_id
                if key in params:
                    temp = params[key]
                    del params[key]

                    params[value] = temp
            return func(self, **params)
        return wrapper

    return decorator


class ECSSystemEventResource(_ECSSystemEventResource):
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
        _ECSSystemEventResource.__init__(self, event_id, _client=_client)

    def refresh(self):
        response = self._client.describe_instance_history_events(list_of_event_id=[self.event_id, ])
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


class ECSTagResource(ServiceResource):
    pass


class ECSDemand(ServiceResource):
    pass


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


class ECSDiskResource(_ECSDiskResource):

    def __init__(self, disk_id, _client=None):
        _ECSDiskResource.__init__(self, disk_id, _client=_client)
        self.disk_id = disk_id

    def refresh(self):
        result = self._client.describe_disks(disk_ids=json.dumps([self.disk_id, ]))
        items = _new_get_key_in_response(result, 'Disks.Disk')
        if not items:
            raise ClientException(msg=
                                  "Failed to find disk data from DescribeDisks response. "
                                  "DiskId = {0}".format(self.disk_id))
        self._assign_attributes(items[0])


class ECSResource(_ECSResource):
    def __init__(self, _client=None):
        _ECSResource.__init__(self, _client=_client)

        self.dedicated_hosts = _create_resource_collection(
            ECSDedicatedHostResource, _client, _client.describe_dedicated_hosts,
            'DedicatedHosts.DedicatedHost', 'DedicatedHostId',
        )

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

        self.instance_full_statuses = _create_default_resource_collection(
            ECSInstanceFullStatus, _client, _client.describe_instances_full_status,
            'InstanceFullStatusSet.InstanceFullStatusType',
        )

        self.disks = _create_resource_collection(
            ECSDiskResource, _client, _client.describe_disks,
            'Disks.Disk', 'DiskId',
            plural_param_to_json={
                'list_of_disk_id': 'DiskId',
            }
        )

        self.tags = _create_default_resource_collection(
            ECSTagResource, _client, _client.describe_tags,
            'Tags.Tag',
        )

        self.demands = _create_default_resource_collection(
            ECSDemand, _client, _client.describe_demands,
            'Demands.Demand',
        )

        self.system_events = _create_resource_collection(
            ECSSystemEventResource, _client, _client.describe_instance_history_events,
            'InstanceSystemEventSet.InstanceSystemEventType', 'EventId',
            param_aliases={
                'list_of_event_id': 'EventId',
                'list_of_event_cycle_status': 'InstanceEventCycleStatus',
                'list_of_event_type': 'InstanceEventType',
            }
        )

    def allocate_dedicated_hosts(self, **params):
        _params = _transfer_params(params)
        response = self._client.allocate_dedicated_hosts(**_params)
        dedicated_host_ids = _new_get_key_in_response(response, 'DedicatedHostIdSets.DedicatedHostId')
        dedicated_hosts = []
        for dedicated_host_id in dedicated_host_ids:
            dedicated_host = ECSDedicatedHostResource(dedicated_host_id, _client=self._client)
            dedicated_hosts.append(dedicated_host)
        return dedicated_hosts

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

    @transfer({"InstanceIds": "list_of_instance_id"})
    def create_simulated_system_events(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_simulated_system_events(**_params)
        event_ids = _new_get_key_in_response(response, 'EventIdSet.EventId')
        events = []
        for event_id in event_ids:
            event = ECSSystemEventResource(event_id, _client=self._client)
            events.append(event)
        return events
