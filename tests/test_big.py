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
from alibabacloud.exceptions import HttpErrorException, ServerException
from clients.ecs_20140526 import EcsClient
from tests.base import SDKTestBase

tags = [
    {
        "Key": "python",
        "Value": "sdk",
    },
]
ecs = get_resource("ecs")
launch_template = list(ecs.launch_templates)[0]

instances = ecs.run_instances(launch_template_id=launch_template.launch_template_id,
                              list_of_tag=tags)

Instance = list(instances)[0]


class EcsResourceTest(SDKTestBase):
    def __init__(self, *args, **kwargs):
        SDKTestBase.__init__(self, *args, **kwargs)
        self.instance = Instance

    def test_private_ip_address_and_tags(self):
        # 测试一台机器的私有IP地址,PrivateIpAddress以及ECS实例的tags属性的读取
        print(1111111111111, self.instance.vpc_attributes)
        private_ip_address = self.instance.vpc_attributes.search("PrivateIpAddress.IpAddress")
        pattern = re.compile(
            r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
        self.assertTrue(pattern.search(private_ip_address).group())
        tags_1 = [
            {
                "Key": "python",
                "Value": "sdk",
            },
        ]

        tags = self.instance.tags
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
        your_inner_ip_list = [self.instance.inner_ip_address, ]
        ecs = self._get_ecs_resource()
        self.assertTrue(len(list(ecs.instances))>=1)
        ecs_instance = ecs.instances.filter(InnerIpAddresses=json.dumps(your_inner_ip_list))
        self.assertEqual(len(list(ecs_instance)), 1)

    def test_vpc_search(self):
        print(11111111, self.instance.vpc_attributes)
        ret = self.instance.vpc_attributes.search('PrivateIpAddress.IpAddress')
        self.assertEqual(len(ret), 1)

    def test_next(self):
        # __next__(iterator) 这样方式的使用，验证是否能获得下一个资源对象
        ecs = self._get_ecs_resource()
        ecs_instance = ecs.instances.all()
        ret1 = next(ecs_instance)
        ret2 = next(ecs_instance)
        self.assertNotEqual(ret1, ret2)
        self.assertTrue(ret2.instance_id)

    def init_credentials_provider(self):
        from alibabacloud.credentials import AccessKeyCredentials

        credentials = AccessKeyCredentials(self.access_key_id,
                                           self.access_key_secret)
        from alibabacloud.credentials.provider import StaticCredentialsProvider
        credentials_provider = StaticCredentialsProvider(credentials)
        return credentials_provider

    def test_retry_to_create_instance(self):
        image_id = "coreos_1745_7_0_64_30G_alibase_20180705.vhd"
        # 测试重试
        config = ClientConfig(region_id=self.region_id, connection_timeout=120, endpoint="nowhere")
        client = EcsClient(config, self.init_credentials_provider())

        from alibabacloud.services.ecs import ECSResource

        with patch.object(client.handlers[-1], "handle_request",
                          wraps=client.handlers[-1].handle_request) as monkey:
            ecs_resource = ECSResource(_client=client)
            try:
                ecs_resource.create_instance(image_id=image_id, instance_type="ecs.n2.small")
                assert False
            except HttpErrorException as e:
                pass
        self.assertEqual(4, monkey.call_count)

    def test_timeout_to_create_instance(self):
        image_id = "coreos_1745_7_0_64_30G_alibase_20180705.vhd"
        # 测试超时
        ecs_resource = self._get_ecs_resource(endpoint="nowhere")
        start_time = time.time()
        ecs_resource.create_instance(image_id=image_id, instance_type="ecs.n2.small")
        end_time = time.time()
        self.assertTrue((end_time - start_time) >= 86)

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
        pass

    def get_vpc_resource(self, **kwargs):
        return self._get_resource("vpc", **kwargs)

    def test_vpc(self):
        vpc = self.get_vpc_resource()
        eip_address = list(vpc.eip_addresses.filter(Status='Available', region_id="cn-hangzhou"))[0]
        eip_address.associate(instance_id=self.instance.instance_id)
        eip_address.refresh()
        self.assertTrue(len(list(vpc.eip_addresses.filter(status="InUse")))>=1)


    def test_eip_associate(self):
        # 测试eip address等,需要缓解准备
        vpc = self.get_vpc_resource()
        eip_address = list(vpc.eip_addresses.all())[0]

        try:
            eip_address.associate(instance_id=self.instance.instance_id)
        except ServerException as e:
            self.assertEqual(e.error_message, "OperationDenied Specified instance is not in VPC.")

    def test_eip_address(self):
        pass
