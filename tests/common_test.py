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

import unittest
from tests.base import SDKTestBase
import alibabacloud
from aliyunsdkcore.acs_exception.exceptions import ClientException


class CommonTest(SDKTestBase):

    def test_get_resource_with_invalid_service_name(self):
        try:
            ecs = alibabacloud.get_resource("blah")
            assert False
        except ClientException as e:
            self.assertEqual(e.error_code, "SDK.ServiceNotSupported")
            self.assertEqual(e.get_error_msg(), "Service 'blah' is not currently supported.")


if __name__ == '__main__':
    unittest.main()
