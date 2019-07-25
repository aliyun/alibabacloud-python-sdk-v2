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

import alibabacloud
from alibabacloud.exceptions import ClientException
from alibabacloud.exceptions import ServerException
from alibabacloud.services.ecs import ECSInstanceResource
from alibabacloud.vendored.six import iteritems
from tests import epoch_time_to_timestamp, timestamp_to_epoch_time
from tests.base import SDKTestBase


class EcsResourceTest(SDKTestBase):

    def setUp(self):
        super(EcsResourceTest, self).setUp()

    def get_resource(self, resource):
        ecs_resource = alibabacloud.get_resource(resource)
        return ecs_resource

    def test_private_address(self):
        # 测试一台机器的私有IP地址,PrivateIpAddress
        ecs = self._get_ecs_resource()
        pass

    def test_requestid(self):
        # 查看请求日志，获知Request ID和其他信息
        pass

    def test_ecs_tags(self):
        # ECS实例的tags属性的读取
        pass

    def test_refresh(self):
        # refresh() 方法的功能正确性
        pass

    def test_modify(self):
        # instance.modify_attributes(InstanceName='web1')的正确性
        # 服务端确定，网页端确定
        ecs = self.get_resource("ecs")
        ecs_instance = list(ecs.instances.all())[0]
        ecs_instance.modify_attributes(InstanceName='web1')
        self.assertEqual(ecs_instance.instance_name, "web1")

    def test_filter_inner_ip_address(self):
        your_inner_ip_list = ["123", "234"]
        ecs = self.get_resource("ecs")
        ecs_instance = ecs.instances.filter(InnerIpAddresses=json.dumps(your_inner_ip_list))
        self.assertEqual(len(list(ecs_instance)), 0)

    def test_vpc_search(self):
        ecs = self.get_resource("ecs")
        ecs_instance = list(ecs.instances.all())[0]
        ret = ecs_instance.vpc_attributes.search('PrivateIpAddress.IpAddress')
        self.assertEqual(len(ret), 0)

    def test_next(self):
        # __next__(iterator) 这样方式的使用，验证是否能获得下一个资源对象
        ecs = self.get_resource("ecs")
        ecs_instance = ecs.instances.all()
        ret1 = next(ecs_instance)
        ret2 = next(ecs_instance)
        self.assertNotEqual(ret1, ret2)
        self.assertTrue(ret2.instance_id)

    def test_retry_timeout_to_creteinstance(self):
        pass

    def test_events(self):
        # TODO 一直为None
        ecs = self.get_resource("ecs")
        ecs_instances = list(ecs.instances.all())
        cur = time.localtime(time.time())
        cur_time = time.strftime('%Y-%m-%dT%H:%M:%SZ', cur)

        system_events = ecs.create_simulated_system_events(event_type="SystemMaintenance.Reboot", InstanceId=[instance.instance_id for instance in ecs_instances], NotBefore=cur_time)
        for event in system_events:
            # print(event.event_id)
            event.refresh()
            # print(event.event_finish_time)

    def test_sys_events(self):
        # TODO 一直为None
        ecs = self.get_resource("ecs")
        ecs_instance = list(ecs.instances.all())[0]
        cur = time.localtime(time.time())
        cur_time = time.strftime('%Y-%m-%dT%H:%M:%SZ', cur)

        system_events = ecs.create_simulated_system_events(event_type="SystemMaintenance.Reboot", InstanceId=[ecs_instance.instance_id, ], NotBefore=cur_time)
        for event in system_events:
            # print(event.event_id)
            event.refresh()
            self.assertTrue(event.event_id)
            self.assertTrue(event.instance_id)
            self.assertTrue(event.event_type)
            self.assertTrue(event.event_cycle_status)
            self.assertTrue(event.event_publish_time)
            self.assertTrue(event.event_finish_time)
            self.assertTrue(event.not_before)
            # print(event.event_finish_time)


    def test_ecs_agree_from_ecs(self):
        pass

    def test_init(self):
        pass

    def test_vpc(self):
        vpc = self.get_resource("vpc")
        print(len(list(vpc.eip_addresses.filter(Status='InUse').all())))
        for eip in vpc.eip_addresses.filter(Status='InUse').all():
            print(eip)
            self.assertTrue(eip,[])

    def test_eip_associate(self):
        vpc = self.get_resource("vpc")

        eip = vpc.allocate_eip_address(Bandwidth=5, InstanceChargeType="PostPaid")
        print(eip.allocation_id)
        self.assertTrue(eip.allocation_id)
        assert False

    def test_eip_address(self):
        pass














