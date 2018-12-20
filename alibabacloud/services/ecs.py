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

from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.CreateInstanceRequest import CreateInstanceRequest


class ECSInstanceResource:

    def __init__(self, id, instance_type):
        self.id = id
        self.instance_type = instance_type

    def start(self):
        pass

    def stop(self):
        pass

    def reboot(self):
        pass

    def delete(self):
        pass

    def renew(self):
        pass

    def reactivate(self):
        pass


class ECSInstancesResouce:

    def filter(self, **kwargs):
        pass

    def all(self):
        pass

    def limit(self, count):
        pass

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

    def __init__(self, **kwargs):
        self._raw_client = AcsClient()
        self.instances = ECSInstancesResouce()
        self.client = ECSClient()

    def create_instance(self):
        pass

    def run_instances(self):
        pass
