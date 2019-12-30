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
    _created = False

    def __init__(self, *args, **kwargs):
        SDKTestBase.__init__(self, *args, **kwargs)
        self.image_id = "coreos_1745_7_0_64_30G_alibase_20180705.vhd"

    def setUp(self):
        if not EcsResourceTest._created:
            self._create_a_lot_instances(4)
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

    def _create_instance_helper(self, **params):
        instance = self.ecs.create_instance(**params)
        return instance

    def status_verify(self, instance):
        client = alibabacloud.get_client(service_name='ecs', access_key_id=self.access_key_id,
                                         access_key_secret=self.access_key_secret,
                                         region_id=self.region_id)
        response = client.describe_instances(instance_ids=json.dumps([instance.instance_id]))
        obj = response['Instances']['Instance'][0]
        for key, value in iteritems(obj):
            attr_name = self._convert_camel_to_snake(key)
            self.assertTrue(hasattr(instance, attr_name), "instance has no " + attr_name)
            self.assertEqual(obj[key], getattr(instance, attr_name))

    def _find_instance(self, count, status, instance_type, to_delete=None):
        instances = []
        for instance in self.ecs.instances.filter(Status=status, ImageId=self.image_id,
                                                  InstanceType=instance_type):
            if to_delete:
                create_time = timestamp_to_epoch_time(instance.creation_time,
                                                      time_format="%Y-%m-%dT%H:%MZ")
                time_diff = time.time() - create_time
                if time_diff > 65:
                    instances.append(instance)
            else:
                instances.append(instance)
        self.assertGreaterEqual(len(instances), count, "Failed to find enough instances.")
        return instances[:count]

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

        print("Wait for 60 seconds to let instance can be deleted")
        time.sleep(60)

    def _get_ids(self, instance_iterable):
        return [i.instance_id for i in instance_iterable]

    def test_all(self):
        ecs = self._get_ecs_resource()
        instances = list(ecs.instances.all())
        self.assertEqual(16, len(instances))
        instance_ids = self._get_ids(instances)
        self.assertEqual(16, len(set(instance_ids)))  # make sure all instance ids are identical
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
        instances = list(ecs.instances.filter(instance_ids=[instance_id,]))
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
            self.assertEqual("InvalidParameter", e.error_code)

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
        instance.refresh()
        self.assertEqual(name, instance.instance_name)

    def test_instance_filter_params_alias(self):
        instances = list(self.ecs.instances.limit(2))
        instance_ids = [x.instance_id for x in instances]
        inner_ips = [x.inner_ip_address.search("IpAddress[0]") for x in instances]

        def _iterator_assert(iterator, expected_count, expected_instance_ids):
            items = list(iterator)
            self.assertEqual(expected_count, len(items))
            self.assertEqual(set(expected_instance_ids), set([x.instance_id for x in items]))

        _iterator_assert(
            self.ecs.instances.filter(instance_ids=[instance_ids[0],]),
            1, instance_ids[:1])
        _iterator_assert(
            self.ecs.instances.filter(instance_ids=instance_ids),
            2, instance_ids)
        _iterator_assert(
            self.ecs.instances.filter(list_of_instance_id=instance_ids),
            2, instance_ids)
        _iterator_assert(
            self.ecs.instances.filter(list_of_private_ip_address=['10.10.10.10']),
            0, [])
        _iterator_assert(
            self.ecs.instances.filter(list_of_inner_ip_address=inner_ips),
            2, instance_ids)
        _iterator_assert(
            self.ecs.instances.filter(list_of_public_ip_address=['10.10.10.10']),
            0, [])
        _iterator_assert(
            self.ecs.instances.filter(list_of_eip_address=['10.10.10.10']),
            0, [])

    def test_invalid_parameter(self):

        ecs = self._get_ecs_resource()

        def test_func(func, error_message):
            try:
                func()
                assert False
            except ClientException as e:
                self.assertEqual(error_message, e.error_message)

        def bad_filter_param():
            for i in ecs.instances.filter(InvalidParameter=1):
                pass

        def test_type_error(func, error_message):
            try:
                func()
                assert False
            except TypeError as e:
                self.assertEqual(error_message, e.args[0])

        # test_func(bad_filter_param,
        #           "DescribeInstancesRequest has no parameter named InvalidParameter.")
        test_type_error(bad_filter_param,
                        "describe_instances() got an unexpected keyword argument 'invalid_parameter'")

        test_func(lambda: ecs.instances.limit(0),
                  "count must be a positive integer.")
        test_func(lambda: ecs.instances.page_size(0),
                  "count must be a positive integer.")
        test_func(lambda: ecs.instances.page_size("blah"),
                  "count must be a positive integer.")

        # test_func(lambda: ecs.run_instances(ImageId="blah", InvalidParameter=1),
        #           "RunInstancesRequest has no parameter named InvalidParameter.")

        test_type_error(lambda: ecs.run_instances(ImageId="blah", InvalidParameter=1),
                        "run_instances() got an unexpected keyword argument 'invalid_parameter'")

        # test_func(lambda: ecs.create_instance(InvalidParameter=1),
        #           "CreateInstanceRequest has no parameter named InvalidParameter.")
        test_type_error(lambda: ecs.create_instance(InvalidParameter=1),
                        "create_instance() got an unexpected keyword argument 'invalid_parameter'")

    def test_resource_refresh_failed(self):
        res = self._get_resource("ecs.instance", "BadId")
        try:
            res.refresh()
            assert False
        except ClientException as e:
            self.assertEqual("Failed to find instance data from DescribeInstances response. "
                             "InstanceId = BadId",
                             e.error_message)

        res = self._get_resource("ecs.system_event", "BadId")
        try:
            res.refresh()
            assert False
        except ClientException as e:
            self.assertEqual("Failed to find event data from "
                             "DescribeInstanceHistoryEventsRequest response. EventId = BadId",
                             e.error_message)

    def test_events(self):
        # create simulated events
        start_time = time.time()
        start_time_str = epoch_time_to_timestamp(start_time)
        instances = self.ecs.instances.all()
        instance_ids = [x.instance_id for x in instances][:4]

        created_event_ids = []
        for event_type in ['SystemMaintenance.Reboot', 'SystemFailure.Reboot',
                           'InstanceFailure.Reboot']:
            time_str = epoch_time_to_timestamp(time.time() + 2)
            events = self.ecs.create_simulated_system_events(InstanceIds=instance_ids,
                                                             EventType=event_type,
                                                             NotBefore=time_str)
            created_event_ids.extend([x.event_id for x in events])
        print("wait 60 seconds to let events to be executed")
        time.sleep(60)

        end_time = time.time()
        end_time_str = epoch_time_to_timestamp(end_time)
        # test get all events
        event_ids = []
        for event in self.ecs.system_events.all().filter(NotBeforeStart=start_time_str,
                                                         NotBeforeEnd=end_time_str):
            if timestamp_to_epoch_time(event.not_before) > start_time:
                event_ids.append(event.event_id)
        self.assertEqual(set(created_event_ids), set(event_ids))

        # test page_size
        event_ids = []
        for event in self.ecs.system_events.page_size(100).filter(NotBeforeStart=start_time_str,
                                                                  NotBeforeEnd=end_time_str):
            if timestamp_to_epoch_time(event.not_before) > start_time:
                event_ids.append(event.event_id)
        self.assertEqual(set(created_event_ids), set(event_ids))

        # test limit
        self.assertEqual(11, len(list(self.ecs.system_events.limit(11))))

        # test get events by instance id
        instance_id = instance_ids[0]
        events = []
        for event in self.ecs.system_events.filter(InstanceId=instance_id,
                                                   NotBeforeStart=start_time_str,
                                                   NotBeforeEnd=end_time_str):
            events.append(event)
        self.assertEqual(3, len(events))
        for event in events:
            self.assertEqual(instance_id, event.instance_id)

        # test get events by region id
        event_ids = []
        for event in self.ecs.system_events.filter(NotBeforeStart=start_time_str,
                                                   RegionId=self.region_id,
                                                   NotBeforeEnd=end_time_str):
            event_ids.append(event.event_id)
        self.assertEqual(set(created_event_ids), set(event_ids))

        self.assertEqual(0, len(list(self.ecs.system_events.filter(NotBeforeStart=start_time_str,
                                                                   RegionId="cn-shanghai",
                                                                   NotBeforeEnd=end_time_str))))

        # test get event by id
        event_id = created_event_ids[0]
        event = alibabacloud.get_resource("ecs.system_event", event_id,
                                          access_key_id=self.access_key_id,
                                          access_key_secret=self.access_key_secret,
                                          region_id=self.region_id)
        event.refresh()
        self.assertEqual(event_id, event.event_id)
        self.assertEqual(event.EventType.SYSTEM_MAINTENANCE_REBOOT, event.get_event_type())
        self.assertEqual(event.EventCycleStatus.EXECUTED, event.get_event_cycle_status())

        # FIXME passed 3.7 but failed 2.7
        events = list(self.ecs.system_events.filter(list_of_event_id=[event_id]))
        self.assertEqual(1, len(events))
        event = events[0]
        self.assertEqual(event_id, event.event_id)
        self.assertEqual(event.EventType.SYSTEM_MAINTENANCE_REBOOT, event.get_event_type())
        self.assertEqual(event.EventCycleStatus.EXECUTED, event.get_event_cycle_status())

        # test param aliases

        # # test list_of_event_cycle_status
        count = 0
        list_of_status = [event.EventCycleStatus.AVOIDED,
                          event.EventCycleStatus.EXECUTED]
        for event in self.ecs.system_events.filter(list_of_event_cycle_status=list_of_status,
                                                   NotBeforeStart=start_time_str,
                                                   NotBeforeEnd=end_time_str):
            count += 1
            self.assertEqual(event.EventCycleStatus.EXECUTED, event.get_event_cycle_status())
        self.assertEqual(12, count)

        list_of_status = [event.EventCycleStatus.AVOIDED]
        events = list(self.ecs.system_events.filter(list_of_event_cycle_status=list_of_status,
                                                    NotBeforeStart=start_time_str,
                                                    NotBeforeEnd=end_time_str))
        self.assertEqual(0, len(events))

        # # test list_of_event_type
        count = 0
        list_of_type = [event.EventType.SYSTEM_MAINTENANCE_REBOOT,
                        event.EventType.SYSTEM_FAILURE_REBOOT]
        for event in self.ecs.system_events.filter(list_of_event_type=list_of_type,
                                                   NotBeforeStart=start_time_str,
                                                   NotBeforeEnd=end_time_str):
            count += 1
            self.assertIn(event.get_event_type(), list_of_type)
        self.assertEqual(8, count)

        # test instance full status
        count = 0
        statuses = list(self.ecs.instance_full_statuses.filter(InstanceIds=instance_ids))
        self.assertEqual(4, len(statuses))
        status = statuses[0]
        self.assertEqual(instance_ids[0], status.instance_id)
        self.assertEqual(0, len(status.system_events))  # TODO Simulate real events
        # self.assertEqual("SystemMaintenance.Reboot", status.system_events[0].get_event_type())


if __name__ == '__main__':
    import unittest

    unittest.main()
