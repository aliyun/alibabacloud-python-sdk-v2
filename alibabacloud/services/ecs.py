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
from alibabacloud.services._ecs import _ECSDedicatedHostResource
from alibabacloud.services._ecs import _ECSInstanceResource
from alibabacloud.services._ecs import _ECSSystemEventResource
from alibabacloud.utils.utils import _assert_is_not_none


class ECSDedicatedHostResource(_ECSDedicatedHostResource):

    PermanentFailure = 'PermanentFailure'
    Released = 'Released'
    Creating = 'Creating'
    Available = 'Available'
    UnderAssessment = 'UnderAssessment'

    def __init__(self, dedicatedhost_id, _client=None):
        _ECSDedicatedHostResource.__init__(self, dedicatedhost_id, _client=_client)

    def wait_until_permanentfailure(self):
        self.wait_until(self.PermanentFailure)

    def wait_until_released(self):
        self.wait_until(self.Released)

    def wait_until_creating(self):
        self.wait_until(self.Creating)

    def wait_until_available(self):
        self.wait_until(self.Available)

    def wait_until_underassessment(self):
        self.wait_until(self.UnderAssessment)


class ECSInstanceResource(_ECSInstanceResource):

    Stopping = 'Stopping'
    Stopped = 'Stopped'
    Transferring = 'Transferring'
    Running = 'Running'
    Starting = 'Starting'
    Pending = 'Pending'
    Deleted = 'Deleted'
    Resetting = 'Resetting'

    def __init__(self, instance_id, _client=None):
        _ECSInstanceResource.__init__(self, instance_id, _client=_client)

    def wait_until_stopping(self):
        self.wait_until(self.Stopping)

    def wait_until_stopped(self):
        self.wait_until(self.Stopped)

    def wait_until_transferring(self):
        self.wait_until(self.Transferring)

    def wait_until_running(self):
        self.wait_until(self.Running)

    def wait_until_starting(self):
        self.wait_until(self.Starting)

    def wait_until_pending(self):
        self.wait_until(self.Pending)

    def wait_until_deleted(self):
        self.wait_until(self.Deleted)

    def wait_until_resetting(self):
        self.wait_until(self.Resetting)


class ECSSystemEventResource(_ECSSystemEventResource):
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
        _ECSSystemEventResource.__init__(self, "ecs.system_event", _client=_client)
        self.event_id = event_id
        self.event_finish_time = None
        _assert_is_not_none(event_id, "event_id")


