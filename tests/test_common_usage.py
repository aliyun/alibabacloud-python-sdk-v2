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
from alibabacloud.exceptions import ClientException, ServiceNameInvalidException


class CommonTest(SDKTestBase):

    def test_get_resource_with_invalid_resource_name(self):
        try:
            ecs = alibabacloud.get_resource("blah")
            assert False
        except ServiceNameInvalidException as e:
            self.assertTrue(e.error_message.startswith("No such service_name 'blah'. Please check your Service Name."))

    def test_get_resource(self):
        alibabacloud.get_resource("ecs",
                                  access_key_id=self.access_key_id,
                                  access_key_secret=self.access_key_secret,
                                  region_id=self.region_id)
        alibabacloud.get_resource("ecs.instance", "i-instance-id",
                                  access_key_id=self.access_key_id,
                                  access_key_secret=self.access_key_secret,
                                  region_id=self.region_id)
        alibabacloud.get_resource("ecs.system_event", "e-event-id",
                                  access_key_id=self.access_key_id,
                                  access_key_secret=self.access_key_secret,
                                  region_id=self.region_id)

    def test_get_resource_failed(self):
        try:
            alibabacloud.get_resource("ecs.instance",
                                      access_key_id=self.access_key_id,
                                      access_key_secret=self.access_key_secret,
                                      region_id=self.region_id)
            assert False
        except ClientException as e:
            self.assertEqual(e.error_message, "Parameter resource_id required.")


if __name__ == '__main__':
    unittest.main()
