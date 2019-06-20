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

import os
import shutil
import tempfile
from alibabacloud import get_client, ClientConfig, DefaultChainedCredentialsProvider
from alibabacloud.exceptions import PartialCredentialsException, ClientException, \
    NoCredentialsException, ConnectionUsingEcsRamRoleException, ServerException, \
    ConfigNotFoundException
from base import SDKTestBase


class CredentialsTest(SDKTestBase):

    def setUp(self):
        super(CredentialsTest, self).setUp()
        self.tempdir = tempfile.mkdtemp()
        self.credentials_file = os.path.join(self.tempdir, 'credentials')
        os.environ['ALIBABA_CLOUD_CREDENTIALS_FILE'] = self.credentials_file

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def write_config(self, credential):
        with open(self.credentials_file, 'w') as f:
            f.write(credential)

    def test_empty(self):
        # TODO：有任何的配置会报错，没有任何的配置 反而是执行才报错
        os.environ.pop('ALIBABA_CLOUD_CREDENTIALS_FILE')
        try:
            client = get_client('ecs')
        except NoCredentialsException as e:
            self.assertEqual(e.error_message, 'Unable to locate credentials')

    # env not enough
    def test_env_default_client_1(self):
        os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'] = ""
        os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'] = ""
        try:
            client = get_client('ecs')
        except PartialCredentialsException as e:
            self.assertEqual(e.error_message,
                             'Partial credentials found in env, ALIBABA_CLOUD_ACCESS_KEY_ID is empty')

        os.environ.pop("ALIBABA_CLOUD_ACCESS_KEY_ID")
        os.environ.pop("ALIBABA_CLOUD_ACCESS_KEY_SECRET")

    def test_env_default_client_2(self):
        os.environ.setdefault("ALIBABA_CLOUD_ACCESS_KEY_ID", "123")
        try:
            client = get_client('ecs')
        except PartialCredentialsException as e:
            self.assertEqual(e.error_message,
                             'Partial credentials found in env, ALIBABA_CLOUD_ACCESS_KEY_SECRET is empty')

        os.environ.pop("ALIBABA_CLOUD_ACCESS_KEY_ID")

    def test_file_ak(self):
        # 有credentials file  但是没有default, 应该抛出PartialCredentialsException
        credentials_file = (
            '[default1]\n'
            'enable = true\n'
            'type = access_key\n'
        )
        self.write_config(credentials_file)
        try:
            client = get_client('ecs')
        except PartialCredentialsException as e:
            self.assertEqual(e.error_message,
                             'Partial credentials found in profile, default section is empty')

    def test_file_ak_1(self):
        # 有credentials file  有default,但是文件格式错误
        credentials_file = (
            '[default]\n'
            'enable\n'
        )
        self.write_config(credentials_file)
        try:
            client = get_client('ecs')
        except ClientException as e:
            self.assertTrue(e.error_message.startswith('Credentials file'))
            self.assertTrue(e.error_message.endswith('format is incorrect.'))

    def test_file_ak_2(self):
        # 有credentials file  有default,但是没有type
        credentials_file = (
            '[default]\n'
            'enable=false\n'
        )
        self.write_config(credentials_file)
        try:
            client = get_client('ecs')
        except PartialCredentialsException as e:
            self.assertEqual(e.error_message,
                             'Partial credentials found in profile, access_key_id is empty')

    def test_file_ak_3(self):
        # 有credentials file  有default,有type 但是没有具体的ak,
        credentials_file = (
            '[default]\n'
            'type = access_key\n'
        )
        self.write_config(credentials_file)
        try:
            client = get_client('ecs')
        except PartialCredentialsException as e:
            self.assertEqual(e.error_message,
                             'Partial credentials found in profile, access_key_id is empty')

    def test_file_ecs_ram_role(self):
        # 有credentials file  有default,有type 测试ecs
        credentials_file = (
            '[default]\n'
            'type = ecs_ram_role\n'
            'role_name = EcsRamRoleTest\n'
        )
        self.write_config(credentials_file)
        client = get_client('ecs')
        try:
            client.describe_regions()
        except ConnectionUsingEcsRamRoleException as e:
            self.assertEqual(e.error_message,
                             'Max number of attempts exceeded when attempting to retrieve data from metadata service.May you need to check your ecs instance')

    def test_file_ram_role_arn(self):
        # 有credentials file  有default,有type 但是没有具体的ak,
        credentials_file = (
                               '[default]\n'
                               'type = ram_role_arn\n'
                               'access_key_id = %s\n'
                               'access_key_secret = %s\n'
                               'role_arn = %s\n'
                               'role_session_name = alice\n'
                           ) % (self.access_key_id, self.access_key_secret, self.ram_role_arn)
        self.write_config(credentials_file)
        client = get_client('ecs', region_id='cn-hangzhou')
        try:
            client.describe_regions()
        except ServerException as e:
            self.assertEqual(e.error_code, 'NoPermission')
            self.assertEqual(e.http_status, 403)
            self.assertEqual(e.endpoint, 'sts.aliyuncs.com')
            self.assertEqual(e.error_message,
                             'You are not authorized to do this action. You should be authorized by RAM.')

    def test_file_beartoken(self):
        # 有credentials file  有default,有type 但是没有具体的ak,
        credentials_file = (
            '[default]\n'
            'type = bearer_token\n'
            'bearer_token = bearer_token\n'
        )
        self.write_config(credentials_file)
        client = get_client('ecs', region_id='cn-hangzhou')
        try:
            client.describe_regions()
        except ServerException as e:
            self.assertEqual(e.error_code, 'UnsupportedSignatureType')
            self.assertEqual(e.error_message, 'This signature type is not supported.')

    def test_file_rsa_key_pair(self):
        # 有credentials file  有default,有type 但是没有具体的ak,
        credentials_file = (
            '[default]\n'
            'type = rsa_key_pair\n'
            'rsa_key_pair = rsa_key_pair\n'
        )
        self.write_config(credentials_file)
        try:
            client = get_client('ecs', region_id='cn-hangzhou')
        except ClientException as e:
            self.assertEqual(e.error_message, 'RSA Key Pair credentials are not supported.')

    def test_file_sts_token(self):
        # 有credentials file  有default,有type 但是没有具体的ak,
        credentials_file = (
                               '[default]\n'
                               'type = sts_token\n'
                               'access_key_id = %s\n'
                               'access_key_secret = %s\n'
                               'user_name = alice\n'
                               'role_arn = role_arn\n'
                               'role_session_name = role_session_name\n'
                           ) % (self.access_key_id, self.access_key_secret)
        self.write_config(credentials_file)
        try:
            client = get_client('ecs')
        except ServerException as e:
            self.assertEqual(e.http_status, 409)
            self.assertEqual(e.error_code, 'LimitExceeded.User.AccessKey')
            self.assertEqual(e.error_message, 'Too many access keys')

    def test_local_file_default_config_with_none_error(self):
        credentials_file = (
            '[default]\n'
            'type = rsa_key_pair\n'
            'rsa_key_pair = rsa_key_pair\n'
        )
        self.write_config(credentials_file)
        client_config = ClientConfig(region_id=self.region_id)
        with self.assertRaises(PartialCredentialsException) as e:
            DefaultChainedCredentialsProvider(client_config, profile_name="abc")
        self.assertEqual(e.exception.error_message, "Partial credentials found in profile, abc section is empty")

    def test_instance_env(self):
        # 有ecs ram role 在环境变量
        os.environ.pop('ALIBABA_CLOUD_CREDENTIALS_FILE')
        os.environ['ALIBABA_CLOUD_ROLE_NAME'] = 'EcsRamRoleTest'
        try:
            client = get_client('ecs')
        except ConnectionUsingEcsRamRoleException as e:
            self.assertEqual(e.error_message,
                             'Max number of attempts exceeded when attempting to retrieve data from metadata service.May you need to check your ecs instance')
        os.environ.pop('ALIBABA_CLOUD_ROLE_NAME')

    def test_local_file_default_config_with_provider_pair_error(self):
        credentials_file = (
            '[client4]\n'
            'type = rsa_key_pair\n'
            'rsa_key_pair = rsa_key_pair\n'
        )
        self.write_config(credentials_file)
        client_config = ClientConfig(region_id=self.region_id)
        with self.assertRaises(ClientException) as e:
            DefaultChainedCredentialsProvider(client_config, profile_name="client4")
        self.assertEqual(e.exception.error_message, "RSA Key Pair credentials are not supported.")

    def test_local_file_default_config_with_path_error(self):
        os.environ['ALIBABA_CLOUD_CREDENTIALS_FILE'] = 'abc'
        client_config = ClientConfig(region_id=self.region_id)
        with self.assertRaises(ConfigNotFoundException) as e:
            DefaultChainedCredentialsProvider(client_config)
        self.assertEqual(e.exception.error_message, "The specified config file (abc) could not be found.")
        os.environ.pop("ALIBABA_CLOUD_CREDENTIALS_FILE")