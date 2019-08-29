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
from alibabacloud.clients.edas_20170801 import EdasClient
from alibabacloud.exceptions import ServerException
from base import SDKTestBase


class AlibabaCloudEdasTest(SDKTestBase):

    def test_api_request_post(self):
        config = self.client_config
        config.endpoint = 'edas.cn-hangzhou.aliyuncs.com'
        client = EdasClient(config, self.init_credentials_provider())
        try:
            response = client.list_application()
            self.assertEqual(response.get("Message"), "success")
            self.assertIsInstance(response.get("ApplicationList"), dict)
            self.assertEqual(response.get("Code"), 200)
        except ServerException as e:
            self.assertEqual(e.http_status, 503)
            self.assertEqual(e.error_code, "ServiceUnavailable")
            self.assertEqual(e.error_message,
                             "The request has failed due to a temporary failure of the server.")

    def test_api_request_get(self):
        config = self.client_config
        config.endpoint = 'edas.cn-hangzhou.aliyuncs.com'
        client = EdasClient(config, self.init_credentials_provider())
        try:
            response = client.list_slb()
            self.assertEqual(response.get("Message"), "success")
            self.assertEqual(response.get("Code"), 200)
            self.assertIsInstance(response.get("SlbList"), dict)
        except ServerException as e:
            self.assertEqual(e.http_status, 503)
            self.assertEqual(e.error_code, "ServiceUnavailable")
            self.assertEqual(e.error_message,
                             "The request has failed due to a temporary failure of the server.")

    def test_api_request_put(self):
        config = self.client_config
        config.endpoint = 'edas.cn-hangzhou.aliyuncs.com'
        client = EdasClient(config, self.init_credentials_provider())

        response = client.disable_degrade_control(app_id='123', rule_id='456')
        self.assertEqual(response.get("Message"), "No permissions")
        self.assertTrue(response.get("Code") == 401 or response.get("Code") == 500)

    def test_api_request_delete(self):
        config = self.client_config
        config.endpoint = 'edas.cn-hangzhou.aliyuncs.com'
        client = EdasClient(config, self.init_credentials_provider())

        response = client.delete_cluster(cluster_id='123')
        self.assertTrue(response.get("Code") == 401 or response.get("Code") == "601")
        self.assertTrue(response.get("Message") == "Edas.errorcode.User.Invalid.message"
                        or response.get("Message") == "Cluster(123) does not exist")
