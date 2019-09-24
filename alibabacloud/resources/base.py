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
from alibabacloud.vendored.six import iteritems
from alibabacloud.utils.utils import _convert_name_from_camel_case_to_snake_case


class ServiceResource(object):

    def __init__(self, service_name, _client=None):
        self._service_name = service_name
        self._client = _client

    def _assign_attributes(self, attrs):
        for key, value in iteritems(attrs):
            setattr(self, _convert_name_from_camel_case_to_snake_case(key), value)
