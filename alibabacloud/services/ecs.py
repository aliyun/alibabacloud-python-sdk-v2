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

import re

from aliyunsdkecs.request.v20140526.CreateInstanceRequest import CreateInstanceRequest
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.StartInstanceRequest import StartInstanceRequest
from aliyunsdkecs.request.v20140526.StopInstanceRequest import StopInstanceRequest
from aliyunsdkecs.request.v20140526.DeleteInstanceRequest import DeleteInstanceRequest
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from aliyunsdkecs.request.v20140526.RebootInstanceRequest import RebootInstanceRequest
from aliyunsdkecs.request.v20140526.RenewInstanceRequest import RenewInstanceRequest
from aliyunsdkecs.request.v20140526.ReActivateInstancesRequest import ReActivateInstancesRequest
from aliyunsdkcore.vendored.six import iteritems

from alibabacloud.services import ServiceResource
from alibabacloud.services import ResourceCollection


class ECSInstanceResource(ServiceResource):

    def __init__(self, instance_id, client=None):
        ServiceResource.__init__(self, client)
        self.instance_id = instance_id
        self.region_id = None
        self.inner_ip_address = None
        self.creation_time = None
        self.expired_time = None
        self.io_optimized = None
        self.public_ip_address = None
        self.internet_charge_type = None
        self.vpc_attributes = None
        self.status = None
        self.host_name = None
        self.image_id = None
        self.instance_charge_type = None
        self.instance_network_type = None
        self.instance_type = None
        self.eip_address = None
        self.serial_number = None
        self.operation_locks = None
        self.security_group_ids = None
        self.internet_max_bandwidth_out = None
        self.zone_id = None
        self.instance_name = None
        self.internet_max_bandwidth_in = None
        self.device_available = None

    def set_instance_attributes(self, attrs):

        def convert(name):
            # covert name from camel case to snake case
            # e.g: InstanceName -> instance_name
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
            return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

        for key, value in iteritems(attrs):
            setattr(self, convert(key), value)

    def start(self):
        request = StartInstanceRequest()
        request.set_InstanceId(self.instance_id)
        self._client.do_action_with_exception(request)

    def stop(self):
        request = StopInstanceRequest()
        request.set_InstanceId(self.instance_id)
        self._client.do_action_with_exception(request)

    def reboot(self):
        request = RebootInstanceRequest()
        request.set_InstanceId(self.instance_id)
        self._client.do_action_with_exception(request)

    def delete(self):
        request = DeleteInstanceRequest()
        request.set_InstanceId(self.instance_id)
        self._client.do_action_with_exception(request)

    def renew(self, **params):
        request = RenewInstanceRequest()
        request.set_InstanceId(self.instance_id)
        self._do_request(request, params)

    def reactivate(self, **params):
        request = ReActivateInstancesRequest()
        request.set_InstanceId(self.instance_id)
        self._do_request(request, params)


class ECSResource(ServiceResource):

    def __init__(self, client=None):
        ServiceResource.__init__(self, client=client)
        self.instances = self._init_instances()

    def _init_instances(self):

        def describe_instances_handler(params):
            request = DescribeInstancesRequest()
            response = self._do_request(request, params)
            self._check_server_response(response, 'TotalCount')
            self._check_server_response(response, 'PageSize')
            self._check_server_response(response, 'PageNumber')
            self._check_server_response(response, 'Instances')
            self._check_server_response(response['Instances'], 'Instance')
            return (
                response['TotalCount'],
                response['PageSize'],
                response['PageNumber'],
                response['Instances']['Instance'],
            )

        def instance_creator(instance_data):
            self._check_server_response(instance_data, 'InstanceId')
            instance_id = instance_data['InstanceId']
            del instance_data['InstanceId']
            inst = ECSInstanceResource(self._client, instance_id)
            inst.set_instance_attributes(instance_data)
            return inst

        return ResourceCollection(
            describe_instances_handler,
            instance_creator,
        )

    def create_instance(self, **params):
        request = CreateInstanceRequest()
        instance_id = self._get_respone(request, params, key='InstanceId')
        return ECSInstanceResource(instance_id, client=self._client)

    def run_instances(self, **params):
        request = RunInstancesRequest()
        instance_ids = self._get_respone(request, params, keys=['InstanceIdSets', 'InstanceIdSet'])

        instances = []
        for instance_id in instance_ids:
            instance = ECSInstanceResource(instance_id, client=self._client)
            instances.append(instance)
        return instances
