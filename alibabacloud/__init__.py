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
import os

__version__ = '0.0.4'

from functools import wraps
from alibabacloud.exceptions import ClientException

import alibabacloud.errors
from alibabacloud.client import ClientConfig
from alibabacloud.exceptions import NoModuleException, ServiceNameInvalidException, \
    ApiVersionInvalidException
from alibabacloud.services.ecs import ECSResource, ECSInstanceResource, ECSSystemEventResource, \
    ECSImageResource, ECSDiskResource
from alibabacloud.services.slb import SLBResource, LoadBalancerResource
from alibabacloud.services.vpc import VPCResource, VPCEipAddressResource
from alibabacloud.utils.client_supports import _list_available_client_services
from alibabacloud.utils.utils import _assert_is_not_none


def _get_param_from_args(args, index, name):
    if len(args) <= index:
        raise ClientException(msg="Parameter {0} required.".format(name))
    return args[index]

# Client


def instance_cache(function):
    cache = {}
    @wraps(function)
    def wrapper(**kwargs):
        key = kwargs.get('service_name')+"@"+kwargs.get("api_version", 'latest')
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


@instance_cache
def get_client(service_name, api_version=None, **kwargs):
    """
    :param service_name: Ecs or ECS or eCS
    :param api_version: 2018-06-09
    :param kwargs:
    :return:
    """
    client_config = ClientConfig(**kwargs)
    module_name, client_name = _prepare_module(service_name, api_version)  # ecs_20180909

    try:
        client_module = __import__(
            '.'.join(['alibabacloud', 'clients', module_name]), globals(), locals(),
            ['clients', module_name], 0)

    except ImportError:
        raise NoModuleException(name='.'.join(module_name))
    credentials_provider = kwargs.get('credentials_provider')
    retry_policy = kwargs.get('retry_policy')
    endpoint_resolver = kwargs.get('endpoint_resolver')
    return getattr(client_module, client_name)(client_config,
                                               credentials_provider=credentials_provider,
                                               retry_policy=retry_policy,
                                               endpoint_resolver=endpoint_resolver)


# resource

def get_resource(*args, **kwargs):

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

    if resource_name.lower() in service_resources:
        temp_client = get_client(service_name=resource_name.lower(), **kwargs)
        return service_resources[resource_name](_client=temp_client)

    elif resource_name.lower() in normal_resources:
        instance_id = _get_param_from_args(args, 1, "resource_id")
        service_name = resource_name.split('.')[0]
        temp_client = get_client(service_name=service_name, **kwargs)
        return normal_resources[resource_name](instance_id, _client=temp_client)

    else:
        raise ClientException(msg=
                              "Resource '{0}' is not currently supported.".format(resource_name))