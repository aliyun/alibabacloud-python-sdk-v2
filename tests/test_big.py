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
import os
import re
import tempfile
import time

from mock import patch

from alibabacloud import ClientConfig, get_resource
from alibabacloud.clients.ecs_20140526 import EcsClient
from alibabacloud.exceptions import HttpErrorException
from tests.base import SDKTestBase


class EcsResourceTest(SDKTestBase):
    _created = False
    proprietary_instance = ""
    classics_instance = ""

    def __init__(self, *args, **kwargs):
        SDKTestBase.__init__(self, *args, **kwargs)
        self.image_id = "coreos_1745_7_0_64_30G_alibase_20180705.vhd"

    def setUp(self):
        if not EcsResourceTest._created:
            self._create_instances()
            EcsResourceTest._created = True

    def _env_clean_up(self):
        print("clean up all instances if any")
        ecs = self._get_ecs_resource()

        has_instance = False
        for inst in ecs.instances.all():
            has_instance = True
            if inst.status != inst.STATUS_STOPPED:
                if inst.status == inst.STATUS_STARTING:
                    inst.wait_until(inst.STATUS_RUNNING)
                    inst.stop()
                elif inst.status == inst.STATUS_RUNNING:
                    inst.stop()

        if has_instance:
            print("wait 60 seconds, in instance_clean_up()")
            time.sleep(60)

        for inst in list(ecs.instances.all()):
            inst.wait_until(inst.STATUS_STOPPED)
            inst.delete()

    def _create_instances(self):
        instances = self.ecs.instances.all()
        if instances:
            self._env_clean_up()
        # 创建一台专有网络
        tags = [
            {
                "Key": "python",
                "Value": "sdk",
            },
        ]
        ecs = get_resource("ecs")
        launch_template = list(ecs.launch_templates.all())[0]

        EcsResourceTest.proprietary_instance = \
            ecs.run_instances(launch_template_id=launch_template.launch_template_id,
                              list_of_tag=tags)[0]
        # 创建一台经典网络
        instance_type = "ecs.n2.small"
        EcsResourceTest.classics_instance = self.ecs.create_instance(ImageId=self.image_id,
                                                                     InstanceType=instance_type, )

        time.sleep(90)

    def test_private_ip_address_and_tags(self):
        instance = EcsResourceTest.proprietary_instance
        instance.refresh()
        # 测试一台机器的私有IP地址,PrivateIpAddress以及ECS实例的tags属性的读取, 测试search
        private_ip_address = instance.vpc_attributes.search("PrivateIpAddress.IpAddress")[0]
        pattern = re.compile(
            r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
        self.assertTrue(pattern.search(private_ip_address).group())
        tags_1 = [
            {
                "Key": "python",
                "Value": "sdk",
            },
        ]

        tags = instance.tags
        self.assertTrue(tags, tags_1)

    def test_logger_request_id(self):
        tempdir = tempfile.mkdtemp()

        temp_file = os.path.join(tempdir, 'file_logger')

        ecs = self._get_ecs_resource(enable_file_logger=True, file_logger_path=temp_file)
        for _ in list(ecs.instances.all()):
            pass

        self.assertTrue(os.path.isfile(temp_file))
        with open(temp_file) as logfile:
            s = logfile.read()
        self.assertTrue('RequestId' in s)

    def test_modify(self):
        # instance.modify_attributes(InstanceName='web1')的正确性
        # 服务端确定，网页端确定
        ecs = self._get_ecs_resource()

        ecs_instance = list(ecs.instances.all())[0]
        ecs_instance.modify_attribute(InstanceName='web1')
        ecs_instance.refresh()
        self.assertEqual(ecs_instance.instance_name, "web1")

    def test_filter_inner_ip_address(self):
        # inner_ip_address 必须是经典网络下的ecs 才有此属性
        instance = EcsResourceTest.classics_instance
        your_inner_ip_list = [instance.inner_ip_address, ]

        ecs = self._get_ecs_resource()

        ecs_instance = ecs.instances.filter(InnerIpAddresses=json.dumps(your_inner_ip_list))
        self.assertTrue(len(list(ecs_instance)))

    def init_credentials_provider(self):
        from alibabacloud.credentials import AccessKeyCredentials

        credentials = AccessKeyCredentials(self.access_key_id,
                                           self.access_key_secret)
        from alibabacloud.credentials.provider import StaticCredentialsProvider
        credentials_provider = StaticCredentialsProvider(credentials)
        return credentials_provider

    def test_retry_to_create_instance(self):

        # 测试重试
        config = ClientConfig(region_id=self.region_id, connection_timeout=120, endpoint="nowhere")
        client = EcsClient(config, self.init_credentials_provider())

        from alibabacloud.services.ecs import ECSResource

        with patch.object(client.handlers[-1], "handle_request",
                          wraps=client.handlers[-1].handle_request) as monkey:
            ecs_resource = ECSResource(_client=client)
            try:
                ecs_resource.create_instance(image_id=self.image_id, instance_type="ecs.n2.small")
                assert False
            except HttpErrorException as e:
                pass
        self.assertEqual(4, monkey.call_count)

    # def test_events(self):
    #     # TODO 一直为None
    #     ecs = self._get_ecs_resource()
    #     ecs_instances = list(ecs.instances.all())
    #     cur = time.localtime(time.time())
    #     cur_time = time.strftime('%Y-%m-%dT%H:%M:%SZ', cur)
    #
    #     system_events = ecs.create_simulated_system_events(event_type="SystemMaintenance.Reboot",
    #                                                        list_of_instance_id=[instance.instance_id
    #                                                                             for instance in
    #                                                                             ecs_instances],
    #                                                        NotBefore=cur_time)
    #     for event in system_events:
    #         # print(event.event_id)
    #         event.refresh()
    #         # print(event.event_finish_time)

    # def test_sys_events(self):
    #     # TODO 一直为None
    #     ecs = self._get_ecs_resource()
    #     ecs_instance = list(ecs.instances.all())[0]
    #     cur = time.localtime(time.time())
    #     cur_time = time.strftime('%Y-%m-%dT%H:%M:%SZ', cur)
    #
    #     system_events = ecs.create_simulated_system_events(event_type="SystemMaintenance.Reboot",
    #                                                        InstanceId=[ecs_instance.instance_id, ],
    #                                                        NotBefore=cur_time)
    #     for event in system_events:
    #         # print(event.event_id)
    #         event.refresh()
    #         self.assertTrue(event.event_id)
    #         self.assertTrue(event.instance_id)
    #         self.assertTrue(event.event_type)
    #         self.assertTrue(event.event_cycle_status)
    #         self.assertTrue(event.event_publish_time)
    #         self.assertTrue(event.event_finish_time)
    #         self.assertTrue(event.not_before)
    #         # print(event.event_finish_time)

    def test_ecs_agree_from_ecs(self):
        pass

    def test_init(self):
        ecs = self._get_ecs_resource()
        for instance in ecs.instances.all():
            self.assertTrue(instance.instance_id)
            self.assertTrue(instance.image_id)
            self.assertTrue(instance.creation_time)


class VPCResourceTest(SDKTestBase):
    def __init__(self, *args, **kwargs):
        SDKTestBase.__init__(self, *args, **kwargs)

    def get_vpc_resource(self, **kwargs):
        return self._get_resource("vpc", **kwargs)

    def test_eip_associate(self):
        slb = self._get_resource("slb")
        load_balancer = list(slb.load_balancers.filter(load_balancer_status="active"))[0]

        # 测试eip address等,需要缓解准备
        vpc = self.get_vpc_resource()
        # 先全部解绑
        for eip in vpc.eip_addresses.filter(status="InUse"):
            eip.unassociate(instance_id=load_balancer.load_balancer_id, instance_type="SlbInstance")
            eip.refresh()

        # allocation_id 是 eip_address 的identifer, instance_id 是绑定的实例的id
        eip_address = list(vpc.eip_addresses.filter(status="Available"))[0]
        self.assertEqual(eip_address.instance_id, "")
        self.assertEqual(eip_address.status, "Available")

        eip_address.associate(instance_id=load_balancer.load_balancer_id,
                              instance_type="SlbInstance")
        eip_address.refresh()
        while eip_address.status == "Associating":
            time.sleep(5)
            eip_address.refresh()

        self.assertEqual(eip_address.instance_id, load_balancer.load_balancer_id)
        self.assertEqual(eip_address.status, "InUse")

        eip_address.unassociate(instance_id=load_balancer.load_balancer_id,
                                instance_type="SlbInstance")
        eip_address.refresh()

        while eip_address.status == "Unassociating":
            time.sleep(5)
            eip_address.refresh()

        self.assertEqual(eip_address.instance_id, "")
        self.assertEqual(eip_address.status, "Available")

        self.assertTrue(eip_address.ip_address)
