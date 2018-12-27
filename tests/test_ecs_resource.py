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

import unittest
import time
from tests.base import SDKTestBase
import alibabacloud
from aliyunsdkcore.acs_exception.exceptions import ClientException


class EcsResourceTest(SDKTestBase):

    def _get_ecs_resource(self):
        return alibabacloud.get_resource(
            'ecs',
            self.access_key_id,
            self.access_key_secret,
            self.region_id,
        )

    def test_create_instance(self):

        ecs = self._get_ecs_resource()
        instance = ecs.create_instance(
            ImageId="coreos_1745_7_0_64_30G_alibase_20180705.vhd",
            InstanceType="ecs.n2.small",
        )
        instance.start()
        instance.wait_until("Running")
        instance.stop()
        instance.wait_until("Stopped")

    def test_get_all(self):
        ecs = self._get_ecs_resource()
        for inst in ecs.instances.all():
            print(inst.instance_id)
            print(inst.instance_type)

        print("===============================")
        for inst in ecs.instances.filter(InstanceType='ecs.g5.large'):
            print(inst.instance_id)

        print("===============================")
        for inst in ecs.instances.filter(InstanceType='ecs.n2.small').limit(3):
            print(inst.instance_id)


if __name__ == '__main__':
    inst = EcsResourceTest()
    inst.test_get_all()

