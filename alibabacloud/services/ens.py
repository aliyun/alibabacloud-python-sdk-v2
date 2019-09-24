# Copyright 2019 Alibaba Cloud Inc. All rights reserved.
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

from alibabacloud import ClientException
from alibabacloud.services._ens import _ENSInstanceResource
from alibabacloud.utils.utils import _new_get_key_in_response


class ENSInstanceResource(_ENSInstanceResource):

    def __init__(self, instance_id, _client=None):
        _ENSInstanceResource.__init__(self, instance_id, _client=_client)

    def refresh(self):
        result = self._client.describe_instances(instance_ids=json.dumps([self.instance_id, ]))
        items = _new_get_key_in_response(result, 'Instances.Instance')
        if not items:
            raise ClientException(
                msg="Failed to find instance data from DescribeInstances response. "
                "InstanceId = {0}".format(
                    self.instance_id))
        self._assign_attributes(items[0])
