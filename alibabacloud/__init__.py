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

__version__ = "0.1.0"

from aliyunsdkcore.acs_exception.exceptions import ClientException
from alibabacloud.services.ecs import ECSResource
import alibabacloud.errors


def get_resource(service_name, **kwargs):
    if service_name.lower() == "ecs":
        return ECSResource(**kwargs)
    else:
        raise ClientException(alibabacloud.errors.ERROR_CODE_SERVICE_NOT_SUPPORTED,
                              "Service '{0}' is not currently supported.".format(service_name))
