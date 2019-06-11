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
    """

    ENV_NAME_FOR_CONFIG_FILE = 'ALIBABA_CLOUD_CONFIG_FILE'
    DEFAULT_NAME_FOR_CONFIG_FILE = '~/.alibabacloud/config'

    def __init__(self, access_key_id=None, access_key_secret=None, region_id=None,
                 max_retry_times=None, user_agent=None, extra_user_agent=None,
                 enable_https=None, http_port=None, https_port=None,
                 connection_timeout=None, read_timeout=None, enable_http_debug=None,
                 http_proxy=None, https_proxy=None, enable_stream_logger=None,
                 config_file=None, enable_retry=None, endpoint=None):

        # credentials
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.region_id = region_id

        self.enable_retry = enable_retry
        self.max_retry_times = max_retry_times
        self.endpoint = endpoint

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
        # config file
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


class AlibabaCloudClient(object):
    LOG_FORMAT = '%(thread)d %(asctime)s %(name)s %(levelname)s %(message)s'

    def __init__(self, client_config, credentials_provider=None,
                 custom_retry_policy=None, endpoint_resolver=None):
        self.product_code = None
        self.location_service_code = None
        self.api_version = None
        self.location_endpoint_type = None

        self.logger = self._init_logger()  # TODO initialize
        self.handlers = [
            RetryHandler(),
            APIProtocolHandler(),
            CredentialsHandler(),
            SignerHandler(),
            TimeoutConfigReader(),
            EndpointHandler(),
            HttpHandler(),
            ServerErrorHandler(),
        ]

        # client_config:ClientConfig,TODO
        self.config = get_merged_client_config(client_config)

        if credentials_provider is not None:
            self.credentials_provider = credentials_provider

        elif self.config.access_key_id and self.config.access_key_secret:
            credentials = AccessKeyCredentials(self.config.access_key_id,
                                               self.config.access_key_secret)
            from alibabacloud.credentials.provider import StaticCredentialsProvider
            self.credentials_provider = StaticCredentialsProvider(credentials)

        else:
            from alibabacloud.credentials.provider import DefaultChainedCredentialsProvider
            self.credentials_provider = DefaultChainedCredentialsProvider(self.config)

        self._init_endpoint_resolve(endpoint_resolver)
        self._init_retry(custom_retry_policy)

    def _handle_config(self, client_config):
        self.config = get_merged_client_config(client_config)
        self._init_endpoint_resolve(endpoint_resolver=None)
        self._init_retry(custom_retry_policy=None)

    def _handle_request(self, api_request, _config=None, _raise_exception=True):
        if _config is not None:
            # for compat
            self._handle_config(_config)
        http_request = HTTPRequest()
        context = RequestContext(api_request=api_request, http_request=http_request,
                                 config=self.config, client=self)
        handler_index = 0
        while 1:
            for handler in self.handlers[handler_index:]:
                handler.handle_request(context)

            for handler in reversed(self.handlers[handler_index:]):
                handler.handle_response(context)
                if context.retry_flag:
                    time.sleep(context.retry_backoff / float(1000))
                    handler_index = self.handlers.index(handler)
                    break
            if not context.retry_flag:
                break
        if context.exception and _raise_exception:
            raise context.exception
        # body
        return context

    def _init_endpoint_resolve(self, endpoint_resolver):
        from alibabacloud.endpoint.default_endpoint_resolver import DefaultEndpointResolver

        self.endpoint_resolver = DefaultEndpointResolver(self.config,
                                                         self.credentials_provider) \
            if endpoint_resolver is None else endpoint_resolver

    def _init_retry(self, custom_retry_policy):
        # TODO initialize
        # retry
        if custom_retry_policy is not None:
            self.retry_policy = custom_retry_policy
        elif self.config.enable_retry:
            try:
                max_retry_times = int(self.config.max_retry_times)
            except ValueError:
                raise ParamTypeInvalidException(param='max_retry_times', param_type='int')
            else:
                self.retry_policy = retry_policy.get_default_retry_policy(
                    max_retry_times=max_retry_times)
        else:
            self.retry_policy = retry_policy.NO_RETRY_POLICY

    def _init_logger(self):
        logger_name = 'alibabacloud-{}'.format(str(id(self)))
        logger = logging.getLogger(logger_name)
        return logger

    def add_rotating_file_log_handler(self, path, log_level=logging.DEBUG, logger_name=None,
                                      maxBytes=10485760, backupCount=5):
        log = logging.getLogger(logger_name) if logger_name else self.logger
        log.setLevel(log_level)
        fh = RotatingFileHandler(path, maxBytes=maxBytes, backupCount=backupCount)
        fh.setLevel(log_level)
        formatter = logging.Formatter(self.LOG_FORMAT)
        fh.setFormatter(formatter)
        if fh not in log.handlers:
            log.addHandler(fh)

    def add_stream_log_handler(self, log_level=logging.DEBUG, logger_name=None, stream=None,
                               format_string=None):
        log = logging.getLogger(logger_name) if logger_name else self.logger
        log.setLevel(log_level)
        ch = logging.StreamHandler(stream)
        ch.setLevel(log_level)
        if format_string is None:
            format_string = self.LOG_FORMAT
        formatter = logging.Formatter(format_string)
        ch.setFormatter(formatter)
        if ch not in log.handlers:
            log.addHandler(ch)
