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

from alibabacloud import ClientConfig
from alibabacloud.exceptions import HttpErrorException, ServerException
from clients.ecs_20140526 import EcsClient
from tests.base import SDKTestBase


class EcsResourceTest(SDKTestBase):

    def setUp(self):
        super(EcsResourceTest, self).setUp()

    def test_private_ip_address(self):
        # 测试一台机器的私有IP地址,PrivateIpAddress
        ecs = self._get_ecs_resource()
        ecs_instance = list(ecs.instances.all())[0]
        private_ip_address = ecs_instance.vpc_attributes.search("PrivateIpAddress.IpAddress")
        if private_ip_address:
            pattern = re.compile(
                r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
            self.assertTrue(pattern.search(private_ip_address).group())
        else:
            assert False

    def test_logger_request_id(self):
        tempdir = tempfile.mkdtemp()

        temp_file = os.path.join(tempdir, 'file_logger')

        # client.add_rotating_file_log_handler(log_level=logging.DEBUG, path=temp_file)
        ecs = self._get_ecs_resource(enable_file_logger=True, file_logger_path=temp_file)
        for item in list(ecs.instances.all()):
            pass

        self.assertTrue(os.path.isfile(temp_file))
        with open(temp_file) as logfile:
            s = logfile.read()
        self.assertTrue('RequestId' in s)

    def test_ecs_tags(self):
        # ECS实例的tags属性的读取
        pass

    def test_modify(self):
        # instance.modify_attributes(InstanceName='web1')的正确性
        # 服务端确定，网页端确定
        ecs = self._get_ecs_resource()

        ecs_instance = list(ecs.instances.all())[0]
        ecs_instance.modify_attribute(InstanceName='web1')
        ecs_instance.refresh()
        self.assertEqual(ecs_instance.instance_name, "web1")

    def test_filter_inner_ip_address(self):
        your_inner_ip_list = ["123", "234"]
        ecs = self._get_ecs_resource()
        ecs_instance = ecs.instances.filter(InnerIpAddresses=json.dumps(your_inner_ip_list))
        self.assertEqual(len(list(ecs_instance)), 0)

    def test_vpc_search(self):
        ecs = self._get_ecs_resource()
        ecs_instance = list(ecs.instances.all())[0]
        ret = ecs_instance.vpc_attributes.search('PrivateIpAddress.IpAddress')
        self.assertEqual(len(ret), 0)

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

        from alibabacloud.services._ecs import _ECSResource

        with patch.object(client.handlers[-1], "handle_request",
                          wraps=client.handlers[-1].handle_request) as monkey:
            ecs_resource = _ECSResource(_client=client)
            try:
                ecs_resource.create_instance(image_id=image_id, instance_type="ecs.n2.small")
                assert False
            except HttpErrorException as e:
                pass
        self.assertEqual(4, monkey.call_count)

    def test_timeout_to_create_instance(self):
        image_id = "coreos_1745_7_0_64_30G_alibase_20180705.vhd"
        # 测试超时
        ecs_resource = self._get_ecs_resource()
        ecs_instance = ecs_resource.create_instance(image_id=image_id, instance_type="ecs.n2.small")
        start_time = time.time()
        ecs_instance.wait_until_stopped()
        end_time = time.time()
        self.assertTrue((end_time - start_time) <= 86)

    def test_events(self):
        # TODO 一直为None
        ecs = self._get_ecs_resource()
        ecs_instances = list(ecs.instances.all())
        cur = time.localtime(time.time())
        cur_time = time.strftime('%Y-%m-%dT%H:%M:%SZ', cur)

        system_events = ecs.create_simulated_system_events(event_type="SystemMaintenance.Reboot",
                                                           list_of_instance_id=[instance.instance_id for instance in ecs_instances],
                                                           NotBefore=cur_time)
        for event in system_events:
            # print(event.event_id)
            event.refresh()
            # print(event.event_finish_time)

    def test_sys_events(self):
        # TODO 一直为None
        ecs = self._get_ecs_resource()
        ecs_instance = list(ecs.instances.all())[0]
        cur = time.localtime(time.time())
        cur_time = time.strftime('%Y-%m-%dT%H:%M:%SZ', cur)

        system_events = ecs.create_simulated_system_events(event_type="SystemMaintenance.Reboot",
                                                           InstanceId=[ecs_instance.instance_id, ],
                                                           NotBefore=cur_time)
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

    def get_vpc_resource(self, **kwargs):
        return self._get_resource("vpc", **kwargs)

    def test_vpc(self):
        vpc = self.get_vpc_resource()
        print(len(list(vpc.eip_addresses.filter(Status='InUse').all())))
        for eip in vpc.eip_addresses.filter(Status='InUse').all():
            print(eip)
            self.assertTrue(eip, [])

    def test_eip_associate(self):
        # 测试eip address等,需要缓解准备
        ecs_resource = self._get_ecs_resource()
        ecs_instance = list(ecs_resource.instances.all())[0]

        vpc = self.get_vpc_resource()

        eip = vpc.allocate_eip_address(Bandwidth=5, InstanceChargeType="PostPaid")
        self.assertEqual(eip.ip_address, "123")
        try:
            eip.associate(instance_id=ecs_instance.instance_id)
        except ServerException as e:
            self.assertEqual(e.error_message, "OperationDenied Specified instance is not in VPC.")

    def test_eip_address(self):
        pass
