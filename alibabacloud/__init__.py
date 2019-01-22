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
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.client import AcsClient
from alibabacloud.services.ecs import ECSResource, ECSInstanceResource, ECSSystemEventResource
import alibabacloud.errors
from alibabacloud.utils import _assert_is_not_none


def _get_param_from_args(args, index, name):
    if len(args) <= index:
        raise ClientException(alibabacloud.errors.ERROR_INVALID_PARAMETER,
                              "Parameter {0} required.".format(name))
    return args[index]


def get_resource(*args, access_key_id=None, access_key_secret=None, region_id=None,
                 resource_id=None):
    resource_name = _get_param_from_args(args, 0, "resource_name")

    if resource_name.lower() == "ecs":
        client = AcsClient(access_key_id, access_key_secret, region_id)
        return ECSResource(_client=client)

    elif resource_name.lower() == "ecs.instance":
        instance_id = _get_param_from_args(args, 1, "instance_id")
        client = AcsClient(access_key_id, access_key_secret, region_id)
        return ECSInstanceResource(instance_id, _client=client)

    elif resource_name.lower() == "ecs.system_event":
        event_id = _get_param_from_args(args, 1, "event_id")
        client = AcsClient(access_key_id, access_key_secret, region_id)
        return ECSSystemEventResource(event_id, _client=client)

    else:
        raise ClientException(alibabacloud.errors.ERROR_CODE_SERVICE_NOT_SUPPORTED,
                              "Resource '{0}' is not currently supported.".format(resource_name))
