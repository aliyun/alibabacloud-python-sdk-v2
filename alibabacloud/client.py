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

import logging
import os
import time
from logging.handlers import RotatingFileHandler

import alibabacloud.retry.retry_policy as retry_policy
from alibabacloud.exceptions import ParamTypeInvalidException, ConfigNotFoundException, \
    PartialCredentialsException, ClientException
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
    'enable_http_debug': None,
    'enable_https': True,
    'http_port': 80,
    'https_port': 443,
    'verify': True
}


class ClientConfig(object):
    """
    `Alibaba Cloud Python SDK`  Config 类
    读取Config的优先级:custom > file > env > default

    :param region_id: 参照 `可用区 <https://help.aliyun.com/document_detail/40654.html>`_
    :type region_id: str

    :param endpoint: 自定义的endpoint，不经过endpoint的解析流程
    :type endpoint: str

    :param enable_retry: 是否重试, 默认True
    :type enable_retry: bool

    :param max_retry_times: 请求最大重试次数，默认3次
    :type max_retry_times: int

    :param user_agent: 用户自定义的UA
    :type user_agent: str

    :param enable_https: 是否使用ssl，默认True
    :type enable_https: bool

    :param http_port: 指定 http 请求端口，默认80
    :type http_port: int

    :param https_port: 指定 https 请求端口，默认443
    :type https_port: int

    :param connection_timeout: 指定连接超时时间，默认5s
    :type connection_timeout: int

    :param read_timeout: 指定读取response超时时间，默认10s
    :type read_timeout: int

    :param enable_http_debug: 是否开启httpDEBUG功能，默认False
    :type enable_http_debug: bool

    :param http_proxy: http 代理地址
    :type http_proxy: str

    :param https_proxy: https 代理地址
    :type https_proxy: str

    """
    ENV_NAME_FOR_CONFIG_FILE = 'ALIBABA_CLOUD_CONFIG_FILE'
    DEFAULT_NAME_FOR_CONFIG_FILE = '~/.alibabacloud/config.ini'

    def __init__(self, region_id=None, endpoint=None, max_retry_times=None, user_agent=None,
                 enable_https=None, http_port=None, https_port=None, enable_retry=None,
                 connection_timeout=None, read_timeout=None, enable_http_debug=None,
                 http_proxy=None, https_proxy=None, verify=None):

        self.endpoint = endpoint
        self.region_id = region_id

        # config
        self.enable_retry = enable_retry
        self.max_retry_times = max_retry_times

        # user-agent, user define ua
        self.user_agent = user_agent

        # https
        self.enable_https = enable_https
        self.http_port = http_port
        self.https_port = https_port

        # timeout
        self.connection_timeout = connection_timeout
        self.read_timeout = read_timeout
        # TODO credentials profile, profile_name
        # self.profile_name = profile_name
        # config file, Specify the configuration file location
        self.enable_http_debug = enable_http_debug

        # proxy provider: client  env
        self.http_proxy = http_proxy
        self.https_proxy = https_proxy
        self._proxy = {
            'http': self.http_proxy,
            'https': self.https_proxy,
        }
        self.verify = verify
        self._read_from_env()
        self._read_from_file()
        self._read_from_default()

    @property
    def proxy(self):
        return self._proxy

    def _read_from_env(self):
        env_vars = {'HTTPS_PROXY', 'HTTP_PROXY'}
        for item in env_vars:
            if getattr(self, item.lower()) is None:
                setattr(self, item.lower(), os.environ.get(item) or os.environ.get(item.lower()))
        self._proxy['http'] = self.http_proxy
        self._proxy['https'] = self.https_proxy

        if self.enable_http_debug is None:
            self.enable_http_debug = os.environ.get('DEBUG') in ('sdk', 'SDK')

        if self.verify is None:
            self.verify = os.environ.get("ALIBABA_CLOUD_CA_BUNDLE")

    def _read_from_file(self):
        profile = {}
        if self.ENV_NAME_FOR_CONFIG_FILE in os.environ:
            config_file_name = os.environ.get(self.ENV_NAME_FOR_CONFIG_FILE)
            if not config_file_name:
                raise ClientException(
                    msg='Found config profile in env, but %s is empty' % self.ENV_NAME_FOR_CONFIG_FILE)
            full_path = os.path.expanduser(config_file_name)
            try:
                config = load_config(full_path)
            except ConfigNotFoundException as e:
                raise e
            else:
                # Alibaba Cloud only support default
                if 'default' not in config:
                    raise PartialCredentialsException(provider='profile',
                                                      cred_var='default section')
                profile = config['default']
        else:
            full_path = os.path.expanduser(self.DEFAULT_NAME_FOR_CONFIG_FILE)
            try:
                config = load_config(full_path)
            except ConfigNotFoundException:
                pass
            else:
                if 'default' in config:
                    profile = config['default']

        for key in dir(self):
            if profile.get(key) is not None and getattr(self, key) is None:
                setattr(self, key, profile.get(key))

    def _read_from_default(self):
        for (key, value) in DEFAULT_CONFIG_VARIABLES.items():
            if getattr(self, key) is None:
                setattr(self, key, value)


class AlibabaCloudClient(object):
    """
    `Alibaba Cloud Python` 创建Client的基类

    :param client_config: 创建client的配置
    :type client_config: alibabacloud.client.ClientConfig

    :param credentials_provider: 凭证链
    :type credentials_provider:

    :param retry_policy: 重试策略
    :type retry_policy:

    :param endpoint_resolver: endpoint 解析链
    :type endpoint_resolver:

    """
    LOG_FORMAT = '%(thread)d %(asctime)s %(name)s %(levelname)s %(message)s'

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):

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
        self.config = client_config

        self.credentials_provider = credentials_provider

        self._init_endpoint_resolve(endpoint_resolver)
        self._init_retry(retry_policy)

    def _handle_request(self, api_request, _raise_exception=True):
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
        context.client.logger.debug('Response received. Product:%s Response-body: %s',
                                    self.product_code, context.http_response.text)

        # TODO
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
                                      max_bytes=10485760, backup_count=5, format_string=None):
        log = logging.getLogger(logger_name) if logger_name else self.logger
        log.setLevel(log_level)
        fh = RotatingFileHandler(path, maxBytes=max_bytes, backupCount=backup_count)
        fh.setLevel(log_level)
        if format_string is None:
            format_string = self.LOG_FORMAT
        formatter = logging.Formatter(format_string)
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
