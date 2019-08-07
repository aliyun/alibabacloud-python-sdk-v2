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
from alibabacloud.services._ens import _ENSInstanceResource


class ENSInstanceResource(_ENSInstanceResource):

    STATUS_TRANSFERRING = 'Transferring'
    STATUS_PENDING = 'Pending'
    STATUS_RUNNING = 'Running'
    STATUS_STARTING = 'Starting'
    STATUS_STOPPING = 'Stopping'
    STATUS_STOPPED = 'Stopped'
    STATUS_DELETED = 'Deleted'
    STATUS_RESETTING = 'Resetting'

    def __init__(self, instance_id, _client=None):
        _ENSInstanceResource.__init__(self, instance_id, _client=_client)

    def wait_until_transferring(self):
        self.wait_until(self.STATUS_TRANSFERRING)

    def wait_until_pending(self):
        self.wait_until(self.STATUS_PENDING)

    def wait_until_running(self):
        self.wait_until(self.STATUS_RUNNING)

    def wait_until_starting(self):
        self.wait_until(self.STATUS_STARTING)

    def wait_until_stopping(self):
        self.wait_until(self.STATUS_STOPPING)

    def wait_until_stopped(self):
        self.wait_until(self.STATUS_STOPPED)

    def wait_until_deleted(self):
        self.wait_until(self.STATUS_DELETED)

    def wait_until_resetting(self):
        self.wait_until(self.STATUS_RESETTING)

