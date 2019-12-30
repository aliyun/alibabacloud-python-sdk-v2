# -*- coding: utf-8 -*-
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

import logging

__version__ = '1.0.6'

from alibabacloud.client import ClientConfig
from alibabacloud.exceptions import ClientException
from alibabacloud.exceptions import NoModuleException, ServiceNameInvalidException, \
    ApiVersionInvalidException
from alibabacloud.utils.client_supports import _list_available_client_services, \
    _list_available_resource_services
from alibabacloud.credentials import AccessKeyCredentials
from alibabacloud.credentials.provider import StaticCredentialsProvider
from alibabacloud.credentials.provider import DefaultChainedCredentialsProvider


def _get_param_from_args(args, index, name):
    if len(args) <= index:
        raise ClientException(msg="Parameter {0} required.".format(name))
    return args[index]


# Client

def get_services(service_name, available_services):
    if service_name.lower() in available_services:
        return available_services[service_name.lower()]
    raise ServiceNameInvalidException(service_name=service_name,
                                      more=','.join([item for item in available_services.keys()]))


def _check_and_get_service(service_name, service="client"):
    if service == "client":
        available_services = _list_available_client_services()
    elif service == "resource":
        available_services = _list_available_resource_services()
    else:
        raise
    return get_services(service_name, available_services)


def _prepare_module(service_name, api_version):
    """
    :param service_name: Ecs or ECS or eCS
    :param api_version: 2018-06-09
    :return: 比如ecs_20140526, 比如EcsClient
    """
    client_name, client_versions = _check_and_get_service(service_name)
    if api_version is None:
        api_version = max(client_versions)
    elif api_version not in client_versions:
        raise ApiVersionInvalidException(service_name=service_name, api_version=api_version,
                                         api_versions=','.join([item for item in client_versions]))

    module_name = service_name.lower() + '_' + api_version.replace('-', '')
    return module_name, client_name


def get_client(service_name, api_version=None, region_id=None, endpoint=None, access_key_id=None,
               access_key_secret=None, credentials_provider=None, retry_policy=None,
               endpoint_resolver=None, config=None):
    """
    获取 `Alibaba Cloud Python SDK` 某个产品某个Version的client

    :param service_name: 产品的product_code，比如Ecs
    :type service_name: str

    :param api_version: 产品的version，格式：2018-06-09
    :type api_version: str

    :param region_id: 参照 `可用区 <https://help.aliyun.com/document_detail/40654.html>`_
    :type region_id: str

    :param endpoint: 自定义的endpoint，不经过endpoint的解析流程
    :type endpoint: str

    :param access_key_id: 秘钥AccessKeyID
    :type access_key_id: str

    :param access_key_secret: 秘钥AccessKeySecret
    :type access_key_secret: str

    :param credentials_provider: 自定义的credentials_provider，如果用户自定义
        credentials_provider,使用用户自定义的
    :type credentials_provider: 一个具备provide接口的对象

    :param retry_policy: 用户自定义的重试策略
    :type retry_policy:

    :param endpoint_resolver: 用户自定义的endpoint_resolver，如果用户自定义
        endpoint_resolver,使用用户自定义的
    :type endpoint_resolver: 一个具备resolve接口的对象

    :param config: 如果用户自定义ClientConfig，使用用户自定义的，否则初始化一个ClientConfig。
        如果用户在 `get_client()` 指定region_id ,则会覆盖config当中的region_id
    :type config: ClientConfig

    :return: client
    :rtype: AlibabaCloudClient

    """
    module_name, client_name = _prepare_module(service_name, api_version)  # ecs_20180909, EcsClient
    if region_id is not None and config:
        config.region_id = region_id
    if endpoint is not None and config:
        config.endpoint = endpoint
    client_config = config if config else ClientConfig(region_id=region_id, endpoint=endpoint)

    try:
        client_module = __import__(
            '.'.join(['alibabacloud', 'clients', module_name]), globals(), locals(),
            ['clients', module_name], 0)

    except ImportError:
        raise NoModuleException(name='.'.join(module_name))

    if credentials_provider is not None:
        custom_credentials_provider = credentials_provider

    elif access_key_id and access_key_secret:
        custom_credentials_provider = StaticCredentialsProvider(
            AccessKeyCredentials(access_key_id, access_key_secret))
    else:
        custom_credentials_provider = DefaultChainedCredentialsProvider(client_config)

    return getattr(client_module, client_name)(client_config,
                                               retry_policy=retry_policy,
                                               credentials_provider=custom_credentials_provider,
                                               endpoint_resolver=endpoint_resolver)


# resource


def get_resource(resource_name, resource_id=None, api_version=None, region_id=None, endpoint=None,
                 access_key_id=None,
                 access_key_secret=None, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None, config=None, enable_stream_logger=None,
                 enable_file_logger=None, **kwargs):
    """
    获取 `Alibaba Cloud Python SDK` 某个Resource

    :param resource_name: 资源类型，比如ecs/slb/vpc等等
    :type resource_name: str

    :param resource_id: 资源ID，比如ecs的InstanceId，用于操作具体的资源
    :type resource_id: str

    :param api_version: 产品的version，格式：2018-06-09
    :type api_version: str

    :param region_id: 参照 `可用区 <https://help.aliyun.com/document_detail/40654.html>`_
    :type region_id: str

    :param endpoint: 自定义的endpoint，不经过endpoint的解析流程
    :type endpoint: str

    :param access_key_id: 秘钥AccessKeyID
    :type access_key_id: str

    :param access_key_secret: 秘钥AccessKeySecret
    :type access_key_secret: str

    :param credentials_provider: 自定义的credentials_provider，如果用户自定义
        credentials_provider,使用用户自定义的
    :type credentials_provider: 一个具备provide接口的对象

    :param retry_policy: 用户自定义的重试策略
    :type retry_policy:

    :param endpoint_resolver: 用户自定义的endpoint_resolver，如果用户自定义
        endpoint_resolver,使用用户自定义的
    :type endpoint_resolver: 一个具备resolve接口的对象

    :param config: 如果用户自定义ClientConfig，使用用户自定义的，否则初始化一个ClientConfig。
        如果用户在 `get_client()` 指定region_id ,则会覆盖config当中的region_id
    :type config: ClientConfig

    :param enable_stream_logger: 是否开启控制台日志
    :type enable_stream_logger: bool

    :param enable_file_logger: 是否开启文件日志
    :type enable_file_logger: bool

    :param kwargs: 主要包含日志相关的参数，为可选参数，用法
    :type kwargs:

    **配置控制台日志如下**

     ::

        >>> import logging
        >>> from alibabacloud import get_resource
        >>> ecs_resource = get_resource('ecs', region_id='cn-hangzhou',
        >>>                    enable_stream_logger=True,
        >>>                    stream_log_level=logging.DEBUG)

    **配置文件日志如下**

     ::

        >>> import logging
        >>> from alibabacloud import get_resource
        >>> ecs_resource = get_resource('ecs', region_id='cn-hangzhou',
        >>>                    enable_stream_logger=True,
        >>>                    stream_log_level=logging.DEBUG,
        >>>                    file_logger_path='alibabacloud.log')

    :return: 资源对象
    :rtype:

    """

    class_name, service_module = _check_and_get_service(resource_name, service="resource")

    stream_logger_handler = {
        "log_level": kwargs.get('stream_log_level', logging.DEBUG),
        "logger_name": kwargs.get('stream_log_name', None),
        "stream": kwargs.get('stream', None),
        "format_string": kwargs.get('stream_format_string', None)
    }

    file_logger_handler = {
        "log_level": kwargs.get('file_log_level', logging.DEBUG),
        "path": kwargs.get('file_logger_path', None),
        "logger_name": kwargs.get('file_log_name', None),
        "max_bytes": kwargs.get('file_max_bytes', 10485760),
        "backup_count": kwargs.get('file_backup_count', 5),
        "format_string": kwargs.get('file_logger_format_string', None)
    }

    def init_client(service_name):
        temp_client = get_client(service_name=service_name, api_version=api_version,
                                 region_id=region_id, endpoint=endpoint,
                                 access_key_id=access_key_id,
                                 access_key_secret=access_key_secret,
                                 credentials_provider=credentials_provider,
                                 retry_policy=retry_policy,
                                 endpoint_resolver=endpoint_resolver, config=config)
        if enable_stream_logger:
            temp_client.add_stream_log_handler(**stream_logger_handler)
        if enable_file_logger:
            if file_logger_handler.get('path') is None:
                raise ClientException(
                    msg="The params file_logger_path is needed. If you want add file logger handler.")
            temp_client.add_rotating_file_log_handler(**file_logger_handler)

        return temp_client

    if len(resource_name.split(".")) == 1:
        _client = init_client(resource_name.lower())
        __import__(
            '.'.join(['alibabacloud', 'services', service_module]), globals(), locals(),
            ['services', service_module, class_name], 0)

        return class_name(_client=_client)
    elif len(resource_name.split(".")) == 2:
        _client = init_client(resource_name.split('.')[0])
        __import__(
            '.'.join(['alibabacloud', 'services', service_module]), globals(), locals(),
            ['clients', service_module, class_name], 0)
        if not resource_id:
            raise ClientException(msg="Parameter resource_id required.")

        return class_name(resource_id, _client=_client)

    else:
        raise ClientException(msg=
                              "Resource '{0}' is not currently supported.".format(resource_name))
