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
import copy
import json

from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.CreateInstanceRequest import CreateInstanceRequest
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.StartInstanceRequest import StartInstanceRequest
from aliyunsdkecs.request.v20140526.StopInstanceRequest import StopInstanceRequest
from aliyunsdkecs.request.v20140526.DeleteInstanceRequest import DeleteInstanceRequest
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from aliyunsdkecs.request.v20140526.RebootInstanceRequest import RebootInstanceRequest
from aliyunsdkecs.request.v20140526.RenewInstanceRequest import RenewInstanceRequest


class ECSInstanceResource:

    def __init__(self, client=None, **kwargs):
        self.client = client
        self.instance_id = kwargs.get('InstanceId', None)

    def start(self):
        request = StartInstanceRequest()
        request.set_InstanceId(self.instance_id)
        response = self.client.do_action_with_exception(request)
        return response

    def stop(self):
        request = StopInstanceRequest()
        request.set_InstanceId(self.instance_id)
        response = self.client.do_action_with_exception(request)
        return response

    def reboot(self):
        request = RebootInstanceRequest()
        request.set_InstanceId(self.instance_id)
        response = self.client.do_action_with_exception(request)
        return response

    def delete(self):
        request = DeleteInstanceRequest()
        request.set_InstanceId(self.instance_id)
        response = self.client.do_action_with_exception(request)
        return response

    def renew(self, **kwargs):
        request = RenewInstanceRequest()
        request.set_InstanceId(self.instance_id)
        for key, value in kwargs.items():
            if hasattr(request, 'set_'+key):
                func = getattr(request, 'set_' + key)
                func(value)
        response = self.client.do_action_with_exception(request)
        return response

    def reactivate(self, **kwargs):
        request = RenewInstanceRequest()
        request.set_InstanceId(self.instance_id)
        for key, value in kwargs.items():
            if hasattr(request, 'set_' + key):
                func = getattr(request, 'set_' + key)
                func(value)
        response = self.client.do_action_with_exception(request)
        return response


class ResourceCollection(object):

    def __init__(self, client=None, **kwargs):
        self.client = client
        self._params = kwargs

    def __iter__(self):
        params = copy.deepcopy(self._params)
        query = params.get('query', None)
        if query is not None:
            for item in self.elements():
                if query == item.instance_id:
                    yield item
            return
        limit = params.get('limit', None)
        count = 0
        for item in self.elements():
            yield item
            count += 1
            if limit is not None and count >= limit:
                return

    def elements(self):
        request = DescribeInstancesRequest()
        response = self.client.do_action_with_exception(request)
        response_obj = json.loads(response.decode('utf-8'))
        instances = response_obj.get('Instances')['Instance']
        for instance in instances:
            ecs_obj = ECSInstanceResource(client=self.client, **instance)
            yield ecs_obj

    def _clone(self):
        params = copy.deepcopy(self._params)
        clone = self.__class__(self.client, **params)
        return clone

    def all(self):
        return self._clone()

    def filter(self, instance_id):
        return self._clone(query=instance_id)

    def limit(self, count):
        return self._clone(limit=count)

    def page_size(self):
        pass


class ECSInstancesResource:
    _collection_cls = ResourceCollection

    def __init__(self, client, **kwargs):
        self.client = client
        self._params = kwargs

    def iterator(self, **kwargs):
        return self._collection_cls(self.client, **kwargs)

    def all(self):
        return self.iterator()

    def filter(self, instance_id):
        self.iterator(query=instance_id)

    # def get(self, instance_id):
    #     request = DescribeInstancesRequest()
    #     response = self.client.do_action_with_exception(request)
    #     response_obj = json.loads(response.decode('utf-8'))
    #     instances = response_obj.get('Instances')['Instance']
    #     for instance in instances:
    #         if instance.get('InstanceId') == instance_id:
    #             ecs_obj = ECSInstanceResource(client=self.client, **instance)
    #             return ecs_obj
    #     return

    def limit(self, count):
        return self.iterator(limit=count)

    def page_size(self, count):
        pass


class ECSClient:

    # TODO decide whether we actually need a client level like this

    def create_instance(self, **kwargs):
        request = CreateInstanceRequest()
        param = kwargs.get('ResourceOwnerId')
        if param is not None:
            request.set_ResourceOwnerId(param)
        self.do_request(request)

    def do_request(self, request):
        pass


class ECSResource:

    def __init__(self, ak=None, secret=None, region_id=None):
        self._raw_client = AcsClient(ak, secret, region_id)
        self.instances = ECSInstancesResource(self._raw_client)
        # self.client = ECSClient()

    def create_instance(self, **kwargs):
        request = CreateInstanceRequest()
        for key, value in kwargs.items():
            if hasattr(request, 'set_'+key):
                func = getattr(request, 'set_' + key)
                func(value)
        response = self._raw_client.do_action_with_exception(request)
        return response

    def run_instances(self, **kwargs):
        request = RunInstancesRequest()
        for key, value in kwargs.items():
            if hasattr(request, 'set_'+key):
                func = getattr(request, 'set_' + key)
                func(value)
        response = self._raw_client.do_action_with_exception(request)
        return response

