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
from alibabacloud.services.ecs import ECSResource, ECSInstanceResource, ECSEventResource
import alibabacloud.errors
from alibabacloud.utils import _assert_is_not_none


def get_resource(resource_name, access_key_id=None, access_key_secret=None, region_id=None,
                 resource_id=None):
    if resource_name.lower() == "ecs":
        client = AcsClient(access_key_id, access_key_secret, region_id)
        return ECSResource(_client=client)
    elif resource_name.lower() == "ecs.instance":
        _assert_is_not_none(resource_id, "resource_id")
        client = AcsClient(access_key_id, access_key_secret, region_id)
        return ECSInstanceResource(resource_id, _client=client)
    elif resource_name.lower() == "ecs.event":
        _assert_is_not_none(resource_id, "resource_id")
        client = AcsClient(access_key_id, access_key_secret, region_id)
        return ECSEventResource(resource_id, _client=client)
    else:
        raise ClientException(alibabacloud.errors.ERROR_CODE_SERVICE_NOT_SUPPORTED,
                              "Resource '{0}' is not currently supported.".format(resource_name))
