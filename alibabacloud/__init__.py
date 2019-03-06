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
from alibabacloud.session import Session


def _get_param_from_args(args, index, name):
    if len(args) <= index:
        raise ClientException(alibabacloud.errors.ERROR_INVALID_PARAMETER,
                              "Parameter {0} required.".format(name))
    return args[index]


_sessions = {}


def _get_session(**kwargs):
    # FIXME more checks
    # TODO using sessions to manage credentials
    access_key_id = kwargs.get('access_key_id')
    access_key_secret = kwargs.get('access_key_secret')
    region_id = kwargs.get('region_id')

    key = access_key_id + '@' + region_id
    if key not in _sessions:
        s = Session(**kwargs)
        _sessions[key] = s

    return _sessions[key]


def get_service(service_name, **kwargs):
    s = _get_session(**kwargs)
    return s.get_service(service_name)


def get_resource(*args, **kwargs):
    resource_type = _get_param_from_args(args, 0, "resource_type")

    if resource_type == "ecs":
        # For backward compatibility
        return get_service("ecs", **kwargs)

    resource_type = _get_param_from_args(args, 0, "resource_type")
    resource_id = _get_param_from_args(args, 1, "resource_id")

    s = _get_session(**kwargs)
    return s.get_resource(resource_type, resource_id)
