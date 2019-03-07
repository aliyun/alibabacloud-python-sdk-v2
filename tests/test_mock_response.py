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
import os.path
from tests.base import SDKTestBase
import alibabacloud
from aliyunsdkcore.acs_exception.exceptions import ClientException
from mock import patch
import alibabacloud.utils as utils


class MockResponseTest(SDKTestBase):

    def _read_mock_data(self, file_name):
        file_path = os.path.join(os.path.dirname(__file__), "mock_data", file_name)
        with open(file_path) as fp:
            return json.loads(fp.read(), object_hook=utils._SearchableDict)

    def test_instance_full_status(self):

        def mock_do_request(client, request, params):
            return self._read_mock_data("instance_full_status.json")

        with patch.object(utils, "_do_request", mock_do_request):

            ecs = self._get_ecs_resource()
            statuses = list(ecs.instance_full_statuses.all())
            self.assertEqual(2, len(statuses))
            status = statuses[0]
            self.assertEqual("i-instance1", status.instance_id)
            self.assertEqual(2, len(status.system_events))
            self.assertEqual("e-event1", status.system_events[0].event_id)
            self.assertEqual("SystemMaintenance.Reboot", status.system_events[0].get_event_type())

    def test_vpc_resource(self):

        vpc = self._get_resource('vpc')

        for eip in vpc.eip_addresses.all():
            print(eip.allocation_id)
            print(eip.charge_type)
            eip.refresh()

    def test_slb_resource(self):

        slb = self._get_resource('slb')

        for lb in slb.load_balancers.all():
            print(lb.load_balancer_id)
            print(lb.load_balancer_name)
            lb.refresh()

    def test_disk_resource(self):
        ecs = self._get_resource('ecs')

        for disk in ecs.disks.all():
            print(disk.disk_id)
            print(disk.disk_name)
            disk.refresh()

    def test_image_resource(self):
        ecs = self._get_resource('ecs')

        for image in ecs.images.all():
            print(image.image_id)
            image.refresh()

    def test_tag_resource(self):
        ecs = self._get_resource('ecs')

        for tag in ecs.tags.all():
            print(tag.tag_key, tag.tag_value)

    def test_new_resource(self):

        names = [
            "ecs.instance",
            "ecs.system_event",
            "ecs.disk",
            "ecs.image",
            "vpc.eip_address",
            "slb.load_balancer",
        ]

        for name in names:
            self._get_resource(name, 'resource-id')

