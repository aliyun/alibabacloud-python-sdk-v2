# -*- coding: utf-8 -*-
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

import json
import os
import time

from alibabacloud.credentials import AccessKeyCredentials
from alibabacloud.credentials import BearerTokenCredentials
from alibabacloud.credentials import SecurityCredentials
from alibabacloud.credentials.assume_role_caller import AssumeRoleCaller
from alibabacloud.exceptions import ClientException, PartialCredentialsException, \
    ConnectionUsingEcsRamRoleException, ConfigNotFoundException
from alibabacloud.utils.ini_helper import load_config
from alibabacloud.vendored import requests


class CredentialsProvider(object):

    def provide(self):
        raise NotImplementedError


class StaticCredentialsProvider(CredentialsProvider):

    def __init__(self, credentials):
        self.credentials = credentials

    def provide(self):
        return self.credentials


class CachedCredentialsProvider(CredentialsProvider):

    def __init__(self):
        self._cached_credentials = None

    def provide(self):
        return self._cached_credentials


class RotatingCredentialsProvider(CachedCredentialsProvider):

    def __init__(self, period, refresh_factor):
        self._period = period
        self._refresh_factor = refresh_factor
        self._last_update_time = 0
        self._expiration = 0
        CachedCredentialsProvider.__init__(self)

    @property
    def is_expiring(self):
        now = time.time()
        return self._expiration - now < self._period * (1 - self._refresh_factor)

    def rotate_credentials(self):
        raise NotImplementedError

    def provide(self):
        if self._cached_credentials is None or self.is_expiring:
            self._expiration = 0
            self._cached_credentials = self.rotate_credentials()
            self._last_update_time = time.time()
            if not self._expiration:
                self._expiration = self._last_update_time + self._period
        return self._cached_credentials


class RamRoleCredentialsProvider(RotatingCredentialsProvider):
    SESSION_PERIOD = 3600
    REFRESH_FACTOR = 0.8

    def __init__(self, client_config, access_key_credentials, role_arn,
                 role_session_name='DefaultSessionName'):
        self.client_config = client_config
        self.access_key_credentials = access_key_credentials
        self.role_arn = role_arn
        self.role_session_name = role_session_name
        self._fetcher = AssumeRoleCaller(client_config,
                                         StaticCredentialsProvider(access_key_credentials))
        RotatingCredentialsProvider.__init__(self, self.SESSION_PERIOD, self.REFRESH_FACTOR)

    def rotate_credentials(self):
        context = self._fetcher.fetch(self.role_arn, self.role_session_name,
                                      self.SESSION_PERIOD)
        response = json.loads(context.http_response.text)
        return SecurityCredentials(
            response.get("Credentials").get("AccessKeyId"),
            response.get("Credentials").get("AccessKeySecret"),
            response.get("Credentials").get("SecurityToken"),
        )


class ProfileCredentialsProvider(CredentialsProvider):
    """
    文件配置 `Alibaba Cloud Python SDK` 凭证
    """
    ENV_NAME_FOR_CREDENTIALS_FILE = 'ALIBABA_CLOUD_CREDENTIALS_FILE'
    DEFAULT_NAME_FOR_CREDENTIALS_FILE = '~/.alibabacloud/credentials.ini'

    def __init__(self, client_config, profile_name):
        self.environ = os.environ
        profile = self._load_profile(profile_name)
        self.client_config = client_config
        self._inner_provider = self._get_provider_by_profile(profile)

    def _load_profile(self, profile_name):
        if self.environ.get(self.ENV_NAME_FOR_CREDENTIALS_FILE) is not None:
            config_file_name = self.environ.get(self.ENV_NAME_FOR_CREDENTIALS_FILE)
            if config_file_name:
                full_path = os.path.expanduser(config_file_name)
                try:
                    config = load_config(full_path)
                except ConfigNotFoundException as e:
                    raise e
                else:
                    if profile_name not in config:
                        raise PartialCredentialsException(provider='profile',
                                                          cred_var='%s section' % (profile_name))
                    return config[profile_name]
            raise ClientException(
                msg='Found profile in env, but %s is empty' % self.ENV_NAME_FOR_CREDENTIALS_FILE)
        # read the default credentials file

        full_path = os.path.expanduser(self.DEFAULT_NAME_FOR_CREDENTIALS_FILE)
        try:
            config = load_config(full_path)
        except ConfigNotFoundException:
            # Move on to the next potential config file name.
            return None
        else:
            if profile_name in config:
                return config[profile_name]

    def _get_provider_by_profile(self, profile):

        def _get_value(key):
            if key not in profile:
                raise PartialCredentialsException(provider='profile', cred_var=key)
            return profile[key]

        if profile:
            type_ = profile.get('type')
            if not type_:
                type_ = 'access_key'  # use access_key for default type

            if type_ == 'access_key':
                return StaticCredentialsProvider(AccessKeyCredentials(
                    _get_value('access_key_id'),
                    _get_value('access_key_secret'),
                ))

            elif type_ == 'ecs_ram_role':
                return InstanceProfileCredentialsProvider(_get_value('role_name'))

            elif type_ == 'ram_role_arn':
                return RamRoleCredentialsProvider(
                    self.client_config,
                    AccessKeyCredentials(
                        _get_value('access_key_id'),
                        _get_value('access_key_secret'),
                    ), _get_value('role_arn'), role_session_name=_get_value('role_session_name'))

            elif type_ == 'bearer_token':
                return StaticCredentialsProvider(BearerTokenCredentials(
                    _get_value('bearer_token'),
                ))

            elif type_ == 'rsa_key_pair':
                raise ClientException(msg="RSA Key Pair credentials are not supported.")

            elif type_ == 'sts_token':
                return StaticCredentialsProvider(SecurityCredentials(
                    _get_value('access_key_id'),
                    _get_value('access_key_secret'),
                    _get_value('security_token'),
                ))

            else:
                raise Exception("Unexpected credentials type: {}".format(type_))

    def provide(self):
        if self._inner_provider:
            return self._inner_provider.provide()


class EnvCredentialsProvider(CachedCredentialsProvider):
    """
    环境变量配置 `Alibaba Cloud Python SDK` 凭证
    """
    ENV_NAME_FOR_ACCESS_KEY_ID = 'ALIBABA_CLOUD_ACCESS_KEY_ID'
    ENV_NAME_FOR_ACCESS_KEY_SECRET = 'ALIBABA_CLOUD_ACCESS_KEY_SECRET'

    def __init__(self):
        CachedCredentialsProvider.__init__(self)

        if self.ENV_NAME_FOR_ACCESS_KEY_ID in os.environ:
            access_key_id = os.environ.get(self.ENV_NAME_FOR_ACCESS_KEY_ID)
            if not access_key_id:
                raise PartialCredentialsException(provider='env',
                                                  cred_var=self.ENV_NAME_FOR_ACCESS_KEY_ID)
            access_key_secret = os.environ.get(self.ENV_NAME_FOR_ACCESS_KEY_SECRET)
            if not access_key_secret:
                raise PartialCredentialsException(provider='env',
                                                  cred_var=self.ENV_NAME_FOR_ACCESS_KEY_SECRET)
            # context.client.logger.info('Found credentials in environment variables.')
            self._cached_credentials = AccessKeyCredentials(
                access_key_id=access_key_id,
                access_key_secret=access_key_secret)


class InstanceProfileCredentialsProvider(RotatingCredentialsProvider):
    """
    环境变量配置role_name, 获取 `Alibaba Cloud Python SDK` 凭证
    """
    REFRESH_FACTOR = 0.8
    DEFAULT_ECS_SESSION_TOKEN_DURATION = 3600 * 6
    URL_PATH = 'http://100.100.100.200/latest/meta-data/ram/security-credentials/'

    def __init__(self, role_name):
        self.role_name = role_name
        RotatingCredentialsProvider.__init__(self, self.DEFAULT_ECS_SESSION_TOKEN_DURATION,
                                             self.REFRESH_FACTOR)

    def rotate_credentials(self):

        try:
            r = requests.get(url=self.URL_PATH + self.role_name)
        except requests.exceptions.ConnectionError:
            raise ConnectionUsingEcsRamRoleException()
        data = json.loads(r.text)
        if data.get("Code") != "Success":
            message = "Failed to get instance profile. Code={}".format(+ data.get("Code"))
            raise ClientException(msg=message)

        expiration = data.get("Expiration")
        if expiration:
            self._expiration = time.mktime(time.strptime(expiration, '%Y-%m-%dT%H:%M:%SZ'))
        else:
            # FIXME Why?
            self._expiration = expiration

        return SecurityCredentials(
            data['AccessKeyId'],
            data['AccessKeySecret'],
            data['SecurityToken'],
        )


class ChainedCredentialsProvider(CredentialsProvider):

    def __init__(self, provider_chain):
        self._provider_chain = provider_chain

    def provide(self):
        for provider in self._provider_chain:
            credentials = provider.provide()
            if credentials:
                return credentials


class PredefinedChainCredentialsProvider(ChainedCredentialsProvider):
    """
    Alibaba Cloud Python 默认的CredentialsProvider链,按照以下顺序读取

    - 环境变量
    - profile文件
    - 配置了RAMRole的ECSInstance

    """

    def __init__(self, client_config, profile_name, role_name):
        provider_chain = [
            EnvCredentialsProvider(),
            ProfileCredentialsProvider(client_config, profile_name),
        ]
        if role_name:
            provider_chain.append(InstanceProfileCredentialsProvider(role_name))

        ChainedCredentialsProvider.__init__(self, provider_chain)


class DefaultChainedCredentialsProvider(PredefinedChainCredentialsProvider):
    ENV_NAME_FOR_CREDENTIALS_FILE = 'ALIBABA_CLOUD_CREDENTIALS_FILE'
    DEFAULT_NAME_FOR_CREDENTIALS_FILE = '~/.alibabacloud/credentials'

    def __init__(self, client_config, profile_name='default'):
        role_name = self._get_config('role_name')
        PredefinedChainCredentialsProvider.__init__(self, client_config,
                                                    profile_name, role_name)

    @staticmethod
    def _get_config(config_name):
        env_name = 'ALIBABA_CLOUD_' + config_name.upper()
        if env_name in os.environ:
            return os.environ.get(env_name)
