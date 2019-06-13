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

__version__ = '0.0.4'

from functools import wraps

from alibabacloud.client import ClientConfig
from alibabacloud.exceptions import ClientException
from alibabacloud.exceptions import NoModuleException, ServiceNameInvalidException, \
    ApiVersionInvalidException
from alibabacloud.services.ecs import ECSResource, ECSInstanceResource, ECSSystemEventResource, \
    ECSImageResource, ECSDiskResource
from alibabacloud.services.slb import SLBResource, LoadBalancerResource
from alibabacloud.services.vpc import VPCResource, VPCEipAddressResource
from alibabacloud.utils.client_supports import _list_available_client_services
from alibabacloud.credentials import AccessKeyCredentials


def _get_param_from_args(args, index, name):
    if len(args) <= index:
        raise ClientException(msg="Parameter {0} required.".format(name))
    return args[index]


# Client


def instance_cache(function):
    cache = {}
    @wraps(function)
    def wrapper(**kwargs):
        key = kwargs.get('service_name') + "@" + kwargs.get('api_version') if kwargs.get(
            'api_version') else 'latest'
        if key in cache:
            return cache[key]
        else:
            rv = function(**kwargs)
            cache[key] = rv
            return rv

    return wrapper


def _check_client_service_name(service_name):
    available_clients = _list_available_client_services()
    if service_name.lower() in available_clients:
        return available_clients[service_name.lower()]
    raise ServiceNameInvalidException(service_name=service_name,
                                      more=','.join([item for item in available_clients.keys()]))


def _prepare_module(service_name, api_version):
    """
    :param service_name: Ecs or ECS or eCS
    :param api_version: 2018-06-09
    :return:
    """
    client_name, client_versions = _check_client_service_name(service_name)
    if api_version is None:
        api_version = max(client_versions)
    elif api_version not in client_versions:
        raise ApiVersionInvalidException(service_name=service_name, api_version=api_version,
                                         api_versions=','.join([item for item in client_versions]))

    module_name = service_name.lower() + '_' + api_version.replace('-', '')
    return module_name, client_name


# @instance_cache
def get_client(service_name, api_version=None, region_id=None, endpoint=None, access_key_id=None,
               access_key_secret=None, custom_credentials_provider=None, custom_retry_policy=None,
               endpoint_resolver=None, config=None):
    """
    :param service_name: Ecs or ECS or eCS
    :param api_version: 2018-06-09
    :param config: ClientConfig, if user define the config ,use config,else init a config
    :return:
    """
    module_name, client_name = _prepare_module(service_name, api_version)  # ecs_20180909
    client_config = config if config else ClientConfig(region_id=region_id, endpoint=endpoint)

    try:
        client_module = __import__(
            '.'.join(['alibabacloud', 'clients', module_name]), globals(), locals(),
            ['clients', module_name], 0)

    except ImportError:
        raise NoModuleException(name='.'.join(module_name))

    if custom_credentials_provider is not None:
        credentials_provider = custom_credentials_provider

    elif access_key_id and access_key_secret:
        credentials = AccessKeyCredentials(access_key_id, access_key_secret)
        from alibabacloud.credentials.provider import StaticCredentialsProvider
        credentials_provider = StaticCredentialsProvider(credentials)

    else:
        from alibabacloud.credentials.provider import DefaultChainedCredentialsProvider
        credentials_provider = DefaultChainedCredentialsProvider(client_config)

    return getattr(client_module, client_name)(client_config,
                                               custom_retry_policy=custom_retry_policy,
                                               credentials_provider=credentials_provider,
                                               custom_endpoint_resolver=endpoint_resolver)


# resource


def get_resource(*args, api_version=None, region_id=None, endpoint=None, access_key_id=None,
                 access_key_secret=None, custom_credentials_provider=None, custom_retry_policy=None,
                 endpoint_resolver=None, config=None, enable_stream_logger=None,
                 enable_file_logger=None, **kwargs):
    resource_name = _get_param_from_args(args, 0, "resource_name")

    service_resources = {
        "ecs": ECSResource,
        "vpc": VPCResource,
        "slb": SLBResource,
    }

    normal_resources = {
        "ecs.instance": ECSInstanceResource,
        "ecs.system_event": ECSSystemEventResource,
        "ecs.disk": ECSDiskResource,
        "ecs.image": ECSImageResource,
        "vpc.eip_address": VPCEipAddressResource,
        "slb.load_balancer": LoadBalancerResource,
    }
    stream_logger_handler = {
        "log_level": kwargs.pop('stream_log_level', logging.DEBUG),
        "logger_name": kwargs.pop('stream_log_name', None),
        "stream": kwargs.pop('stream', None),
        "format_string": kwargs.pop('stream_format_string', None)
    }

    file_logger_handler = {
        "log_level": kwargs.get('file_log_level', logging.DEBUG),
        "path": kwargs.get('file_logger_path', None),
        "logger_name": kwargs.get('file_log_name', None),
        "maxBytes": kwargs.get('file_maxBytes', 10485760),
        "backupCount": kwargs.get('file_backupCount', 5),
        "format_string": kwargs.get('file_logger_format_string', None)
    }

    def init_client(service_name):
        temp_client = get_client(service_name=service_name, api_version=api_version,
                                 region_id=region_id, endpoint=endpoint,
                                 access_key_id=access_key_id,
                                 access_key_secret=access_key_secret,
                                 custom_credentials_provider=custom_credentials_provider,
                                 custom_retry_policy=custom_retry_policy,
                                 endpoint_resolver=endpoint_resolver, config=config)
        if enable_stream_logger:
            temp_client.add_stream_log_handler(**stream_logger_handler)
        if enable_file_logger:
            if file_logger_handler.get('path') is None:
                raise ClientException(
                    msg="The params file_logger_path is needed. If you want add file logger handler.")
            temp_client.add_rotating_file_log_handler(**file_logger_handler)

        return temp_client

    if resource_name.lower() in service_resources:

        temp_client = init_client(resource_name.lower())

        return service_resources[resource_name](_client=temp_client)

    elif resource_name.lower() in normal_resources:
        instance_id = _get_param_from_args(args, 1, "resource_id")
        temp_client = init_client(resource_name.split('.')[0])

        return normal_resources[resource_name](instance_id, _client=temp_client)

    else:
        raise ClientException(msg=
                              "Resource '{0}' is not currently supported.".format(resource_name))
