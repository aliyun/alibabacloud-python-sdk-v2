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

import sys
import os
import json
from unittest import TestCase

if sys.version_info[0] == 2:
    from collections import Iterable
else:
    from collections.abc import Iterable


class SDKTestBase(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        if sys.version_info[0] == 2:
            self.assertRegex = self.assertRegexpMatches

        self._sdk_config = self._init_sdk_config()
        self.access_key_id = self._read_key_from_env_or_config("ACCESS_KEY_ID")
        self.access_key_secret = self._read_key_from_env_or_config("ACCESS_KEY_SECRET")
        self.region_id = self._read_key_from_env_or_config("REGION_ID")

    def _init_sdk_config(self):
        sdk_config_path = os.path.join(os.path.expanduser("~"), "aliyun_sdk_config.json")
        if os.path.isfile(sdk_config_path):
            with open(sdk_config_path) as fp:
                return json.loads(fp.read())

    def _read_key_from_env_or_config(self, key_name):
        if key_name.upper() in os.environ:
            return os.environ.get(key_name.upper())
        if key_name.lower() in self._sdk_config:
            return self._sdk_config[key_name.lower()]

        raise Exception("Failed to find sdk config: " + key_name)
