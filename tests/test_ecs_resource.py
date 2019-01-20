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
import json
import datetime
from tests.base import SDKTestBase
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkcore.vendored.six import iteritems
from alibabacloud.services.ecs import ECSInstanceResource


class EcsResourceTest(SDKTestBase):

    def __init__(self, *args, **kwargs):
        SDKTestBase.__init__(self, *args, **kwargs)
        self.image_id = "coreos_1745_7_0_64_30G_alibase_20180705.vhd"
        self._created = False

    def setUp(self):
        if not self._created:
            self._create_a_lot_instances(4)
            self._created = True

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

    def _create_instance_helper(self, **params):
        instance = self.ecs.create_instance(**params)
        return instance

    def status_verify(self, instance):
        request = DescribeInstancesRequest()
        request.set_InstanceIds(json.dumps([instance.instance_id]))
        response = self.client.do_action_with_exception(request)
        obj = json.loads(response.decode('utf-8'))['Instances']['Instance'][0]
        for key, value in iteritems(obj):
            attr_name = self._convert_camel_to_snake(key)
            self.assertTrue(hasattr(instance, attr_name), "instance has no " + attr_name)
            self.assertEqual(obj[key], getattr(instance, attr_name))

    def _find_instance(self, count, status, instance_type, to_delete=None):
        instances = []
        for instance in self.ecs.instances.filter(Status=status, ImageId=self.image_id,
                                                  InstanceType=instance_type):
            if to_delete:
                create_time = time.mktime(datetime.datetime.strptime(
                    instance.creation_time, "%Y-%m-%dT%H:%MZ"
                ).timetuple()) + time.timezone
                time_diff = time.time() - create_time
                if time_diff > 65:
                    instances.append(instance)
            else:
                instances.append(instance)
        self.assertGreaterEqual(len(instances), count, "Failed to find enough instances.")
        return instances

    def _refresh_and_assert(self, instance, status, instance_type):
        instance.refresh()
        self.assertEqual(self.image_id, instance.image_id)
        self.assertEqual(instance_type, instance.instance_type)
        self.assertEqual(status, instance.status)

    def test_basic_instance_op(self):

        # test create_instance
        instance = self._find_instance(1, "Stopped", "ecs.n2.small", to_delete=True)[0]
        instance.delete()
        instance = self.ecs.create_instance(
            ImageId=self.image_id,
            InstanceType="ecs.n2.small",
        )
        self._refresh_and_assert(instance, "Stopped", "ecs.n2.small")
        sg_id = instance.security_group_ids['SecurityGroupId'][0]

        # test reboot, stop, start, and wait_until()
        instance_to_reboot = self._find_instance(1, "Running", "ecs.n2.large")[0]
        instance_to_reboot.reboot()
        instance_to_stop = self._find_instance(1, "Running", "ecs.n2.large")[0]
        instance_to_stop.stop()

        instance_to_start = self._find_instance(1, "Stopped", "ecs.n2.large")[0]
        instance_to_start.start()

        instance_to_reboot.wait_until_running()
        instance_to_stop.wait_until_stopped()
        instance_to_start.wait_until_running()

    def test_empty_instances(self):
        ecs = self._get_ecs_resource()
        self.assertEqual([], list(ecs.instances.filter(InstanceType='ABC')))
        self.assertEqual([], list(ecs.instances.limit(10).filter(InstanceType="ABC")))
        self.assertEqual([], list(ecs.instances.page_size(5).filter(InstanceType="ABC")))

    def _create_a_lot_instances(self, num):

        instances = list(self.ecs.instances.all())

        if num * 4 == len(instances) and \
                num * 4 == sum([i.image_id == self.image_id for i in instances]) and \
                num * 2 == sum([i.instance_type == "ecs.n2.large" for i in instances]) and \
                num * 2 == sum([i.instance_type == "ecs.n2.small" for i in instances]) and \
                num * 2 == sum([i.status == "Running" for i in instances]) and \
                num * 2 == sum([i.status == "Stopped" for i in instances]):
            return
        else:
            self._env_clean_up()

        to_wait = []
        instance_ids = []
        for instance_type in ['ecs.n2.large', 'ecs.n2.small']:
            for i in range(num):
                instance = self._create_instance_helper(
                    ImageId=self.image_id,
                    InstanceType=instance_type,
                )
                instance_ids.append(instance)
                instance = self._create_instance_helper(
                    ImageId=self.image_id,
                    InstanceType=instance_type,
                )
                instance_ids.append(instance)
                instance.start()
                to_wait.append(instance)

        for instance in to_wait:
            instance.wait_until_running()

    def _get_ids(self, instance_iterable):
        return [i.instance_id for i in instance_iterable]

    def test_all(self):
        ecs = self._get_ecs_resource()
        instances = list(ecs.instances.all())
        self.assertEqual(16, len(instances))
        instance_ids = self._get_ids(instances)
        self.assertEqual(16, len(set(instance_ids)))   # make sure all instance ids are identical
        for instance in instances:
            self.status_verify(instance)

    def test_filter(self):
        ecs = self._get_ecs_resource()
        count = 0
        for instance in ecs.instances.filter(InstanceType='ecs.n2.large'):
            self.assertEqual(instance.instance_type, 'ecs.n2.large')
            count += 1
        self.assertEqual(8, count)

        count = 0
        for instance in ecs.instances.filter(Status=ECSInstanceResource.STATUS_RUNNING):
            self.assertEqual(instance.status, instance.STATUS_RUNNING)
            count += 1
        self.assertEqual(8, count)

        count = 0
        for instance in ecs.instances.filter(InstanceType='ecs.n2.large',
                                             Status=ECSInstanceResource.STATUS_RUNNING):
            self.assertEqual(instance.instance_type, 'ecs.n2.large')
            self.assertEqual(instance.status, instance.STATUS_RUNNING)
            count += 1
        self.assertEqual(4, count)

        all_ids = self._get_ids(ecs.instances.all())
        instance_id = all_ids[-1]
        instances = list(ecs.instances.filter(instance_id=instance_id))
        self.assertEqual(1, len(instances))
        self.assertEqual(instance_id, instances[0].instance_id)

        instance_ids = all_ids[:2]
        instances = list(ecs.instances.filter(instance_ids=instance_ids))
        self.assertEqual(2, len(instances))
        self.assertEqual(set(instance_ids), set(self._get_ids(instances)))

        # test next()
        instance_ids = all_ids[:2]
        filter = ecs.instances.filter(instance_ids=instance_ids)
        instances = []
        instances.append(next(filter))
        instances.append(next(filter))
        self.assertEqual(2, len(instances))
        self.assertEqual(set(instance_ids), set(self._get_ids(instances)))

    def test_limit(self):
        ecs = self._get_ecs_resource()
        self.assertEqual(7, len(list(ecs.instances.limit(7))))
        self.assertEqual(10, len(list(ecs.instances.limit(10))))
        self.assertEqual(13, len(list(ecs.instances.limit(13))))

        all_ids = self._get_ids(ecs.instances.all())
        self.assertEqual(all_ids[:7], self._get_ids(ecs.instances.limit(7)))

        for inst in ecs.instances.limit(7):
            self.status_verify(inst)

    def test_page_size(self):
        ecs = self._get_ecs_resource()

        try:
            for i in ecs.instances.page_size(101):
                pass
            assert False
        except ServerException as e:
            self.assertEqual("InvalidParameter", e.get_error_code())

        all_ids = self._get_ids(ecs.instances.all())
        instances = list(ecs.instances.page_size(100))
        self.assertEqual(16, len(instances))
        self.assertEqual(all_ids, self._get_ids(instances))

        self.assertEqual(16, len(list(ecs.instances.page_size(16))))
        self.assertEqual(16, len(list(ecs.instances.page_size(7))))
        self.assertEqual(16, len(list(ecs.instances.page_size(13))))

    def test_iterator_joint(self):
        ecs = self._get_ecs_resource()
        self.assertEqual(10, len(list(ecs.instances.page_size(16).limit(10))))
        self.assertEqual(16, len(list(ecs.instances.page_size(16).limit(30))))
        self.assertEqual(10, len(list(ecs.instances.limit(10).page_size(19))))
        self.assertEqual(16, len(list(ecs.instances.limit(30).page_size(2))))

        self.assertEqual(10, len(list(ecs.instances.limit(20).limit(10))))
        self.assertEqual(16, len(list(ecs.instances.page_size(28).page_size(100))))

        count = 0
        for inst in ecs.instances.page_size(5).limit(7).filter(InstanceType='ecs.n2.small'):
            count += 1
            self.assertEqual('ecs.n2.small', inst.instance_type)
        self.assertEqual(7, count)

        count = 0
        for inst in ecs.instances.filter(InstanceType='ecs.n2.large').filter(
                Status=ECSInstanceResource.STATUS_STOPPED):
            count += 1
            self.assertEqual('ecs.n2.large', inst.instance_type)
            self.assertEqual(ECSInstanceResource.STATUS_STOPPED, inst.status)
        self.assertEqual(4, count)

    def test_next(self):

        def _get_iterator():
            return self.ecs.instances.filter(InstanceType='ecs.n2.large',
                                             ImageId=self.image_id,
                                             Status="Running")

        iterator = _get_iterator()
        for i in range(4):
            item = next(iterator)
            self.assertTrue(hasattr(item, "instance_id"))
        try:
            next(iterator)
            assert False
        except StopIteration as e:
            pass

        iterator = _get_iterator()
        for i in range(4):
            item = iterator.__next__()
            self.assertTrue(hasattr(item, "instance_id"))
        try:
            iterator.__next__()
            assert False
        except StopIteration as e:
            pass

    def test_jmespath_search(self):
        instance = self._find_instance(1, "Running", "ecs.n2.large")[0]
        ip_address = instance.inner_ip_address['IpAddress'][0]
        self.assertEqual(ip_address, instance.inner_ip_address.search('IpAddress[0]'))

    def test_modify_attributes(self):
        import random
        seed = random.randint(1000, 9999)
        name = "RandomName" + str(seed)
        instance = self._find_instance(1, "Running", "ecs.n2.small")[0]
        instance.modify_attributes(InstanceName=name)
        self.assertEqual(name, instance.instance_name)

    def test_invalid_parameter(self):

        ecs = self._get_ecs_resource()

        def test_func(func, error_message):
            try:
                func()
                assert False
            except ClientException as e:
                self.assertEqual("SDK.InvalidParameter", e.get_error_code())
                self.assertEqual(error_message, e.get_error_msg())

        def bad_filter_param():
            for i in ecs.instances.filter(InvalidParameter=1):
                pass

        test_func(bad_filter_param,
                  "DescribeInstancesRequest has no parameter named InvalidParameter.")
        test_func(lambda: ecs.instances.limit(0),
                  "count must be a positive integer.")
        test_func(lambda: ecs.instances.page_size(0),
                  "count must be a positive integer.")
        test_func(lambda: ecs.instances.page_size("blah"),
                  "count must be a positive integer.")
        test_func(lambda: ecs.run_instances(ImageId="blah", InvalidParameter=1),
                  "RunInstancesRequest has no parameter named InvalidParameter.")
        test_func(lambda: ecs.create_instance(InvalidParameter=1),
                  "CreateInstanceRequest has no parameter named InvalidParameter.")

    def test_resource_refresh_failed(self):
        res = self._get_resource("ecs.instance", "BadId")
        res.refresh()


if __name__ == '__main__':
    unittest.main()

