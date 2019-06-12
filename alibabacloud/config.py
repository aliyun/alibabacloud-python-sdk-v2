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

import logging
import os
import time
from logging.handlers import RotatingFileHandler

import alibabacloud.retry.retry_policy as retry_policy
from alibabacloud.credentials import AccessKeyCredentials
from alibabacloud.exceptions import ParamTypeInvalidException, ConfigNotFoundException
from alibabacloud.handlers import RequestContext
from alibabacloud.handlers.api_protocol_handler import APIProtocolHandler
from alibabacloud.handlers.credentials_handler import CredentialsHandler
from alibabacloud.handlers.endpoint_handler import EndpointHandler
from alibabacloud.handlers.http_handler import HttpHandler
from alibabacloud.handlers.retry_handler import RetryHandler
from alibabacloud.handlers.server_error_handler import ServerErrorHandler
from alibabacloud.handlers.signer_handler import SignerHandler
from alibabacloud.handlers.timeout_config_reader import TimeoutConfigReader
from alibabacloud.request import HTTPRequest
from alibabacloud.utils.ini_helper import load_config

DEFAULT_CONFIG_VARIABLES = {
    'max_retry_times': 3,
    'enable_retry': True,
    'enable_http_debug': False,
    'enable_https': True,
    'http_port': 80,
    'https_port': 443,
}


class ClientConfig(object):
    """
    handle client config
    Configuration priority:custom > file > env > default
    """

    ENV_NAME_FOR_CONFIG_FILE = 'ALIBABA_CLOUD_CONFIG_FILE'
    DEFAULT_NAME_FOR_CONFIG_FILE = '~/.alibabacloud/config'

    def __init__(self,
                 # access_key_id=None, access_key_secret=None, region_id=None, endpoint=None,
                 max_retry_times=None, user_agent=None, extra_user_agent=None,
                 enable_https=None, http_port=None, https_port=None,
                 connection_timeout=None, read_timeout=None, enable_http_debug=None,
                 http_proxy=None, https_proxy=None, enable_stream_logger=None,
                 config_file=None, enable_retry=None):

        # credentials
        # self.access_key_id = access_key_id
        # self.access_key_secret = access_key_secret
        # self.endpoint = endpoint
        # self.region_id = region_id

        # config
        self.enable_retry = enable_retry
        self.max_retry_times = max_retry_times

        # user-agent, user define ua
        self.user_agent = user_agent
        self.extra_user_agent = extra_user_agent

        # https
        self.enable_https = enable_https
        self.http_port = http_port
        self.https_port = https_port

        # timeout
        self.connection_timeout = connection_timeout
        self.read_timeout = read_timeout
        self.enable_stream_logger = enable_stream_logger
        # TODO credentials profile, profile_name
        # self.profile_name = profile_name
        # config file, Specify the configuration file location
        self.config_file = config_file
        self.enable_http_debug = enable_http_debug
        # proxy provider: client  env
        self.http_proxy = http_proxy
        self.https_proxy = https_proxy
        self._proxy = {
            'http': self.http_proxy,
            'https': self.https_proxy,
        }

    @property
    def proxy(self):
        return self._proxy

    def read_from_env(self):
        env_vars = {'HTTPS_PROXY', 'HTTP_PROXY'}
        for item in env_vars:
            if getattr(self, item.lower()) is None:
                setattr(self, item.lower(), os.environ.get(item) or os.environ.get(item.lower()))
        self._proxy['http'] = self.http_proxy
        self._proxy['https'] = self.https_proxy

        if self.enable_http_debug is None:
            self.enable_http_debug = os.environ.get('DEBUG') in ('sdk', 'SDK')

    def read_from_file(self):
        profile = {}
        # TODO read from profile
        if self.config_file is None:
            if self.ENV_NAME_FOR_CONFIG_FILE in os.environ:
                env_config_file_path = os.environ.get(self.ENV_NAME_FOR_CONFIG_FILE)
                if env_config_file_path is not None:
                    full_path = os.path.expanduser(env_config_file_path)
                    loaded_config = load_config(full_path)
                    profile = loaded_config.get('default', {})
            else:
                filename = self.DEFAULT_NAME_FOR_CONFIG_FILE
                try:
                    loaded_config = load_config(filename)
                    profile = loaded_config.get('default', {})
                except ConfigNotFoundException:
                    pass

        else:
            profile = load_config(self.config_file)

        for key in dir(self):
            if profile.get(key) is not None and getattr(self, key) is None:
                setattr(self, key, profile.get(key))

    def read_from_default(self):
        for (key, value) in DEFAULT_CONFIG_VARIABLES.items():
            if getattr(self, key) is None:
                setattr(self, key, value)


def get_merged_client_config(config):
    config.read_from_env()
    config.read_from_file()
    config.read_from_default()
    return config


