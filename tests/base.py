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

import json
import os
import re
import sys
import alibabacloud
import alibabacloud.utils


# The unittest module got a significant overhaul
# in 2.7, so if we're in 2.6 we can use the backported
# version unittest2.
if sys.version_info[:2] == (2, 6):
    from unittest2 import TestCase
else:
    from unittest import TestCase


class SDKTestBase(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        alibabacloud.utils._test_flag = True
        if sys.version_info[0] == 2:
            self.assertRegex = self.assertRegexpMatches

        self._sdk_config = self._init_sdk_config()
        self.access_key_id = self._read_key_from_env_or_config("ACCESS_KEY_ID")
        self.access_key_secret = self._read_key_from_env_or_config("ACCESS_KEY_SECRET")
        self.region_id = self._read_key_from_env_or_config("REGION_ID")
        self.ecs = self._get_ecs_resource()

    def _convert_camel_to_snake(self, name):
        # covert name from camel case to snake case
        # e.g: InstanceName -> instance_name
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def _init_sdk_config(self):
        sdk_config_path = os.path.join(os.path.expanduser("~"), "aliyun_sdk_config.json")
        if os.path.isfile(sdk_config_path):
            with open(sdk_config_path) as fp:
                return json.loads(fp.read())

    def _read_key_from_env_or_config(self, key_name):
        # if key_name.upper() in os.environ:
        #     return os.environ.get(key_name.upper())
        if self._sdk_config is not None and key_name.lower() in self._sdk_config:
            return self._sdk_config[key_name.lower()]

        raise Exception("Failed to find sdk config: " + key_name)

    def _get_resource(self, *args, **kwargs):
        ecs_resource = alibabacloud.get_resource(*args, access_key_id=self.access_key_id,
                                                 access_key_secret=self.access_key_secret,
                                                 region_id=self.region_id, **kwargs)
        return ecs_resource

    def _get_ecs_resource(self, **kwargs):
        return self._get_resource("ecs", **kwargs)

    def create_simple_instance(self):
        instance = self.ecs.create_instance(
            ImageId="coreos_1745_7_0_64_30G_alibase_20180705.vhd",
            InstanceType="ecs.n2.small",
        )

        return instance
