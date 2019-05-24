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
__version__ = '0.0.4'

import os

from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.client import AcsClient

import alibabacloud.errors
from alibabacloud.client import ClientConfig
from alibabacloud.exceptions import NoModuleException
from alibabacloud.services.ecs import ECSResource, ECSInstanceResource, ECSSystemEventResource, \
    ECSImageResource, ECSDiskResource
from alibabacloud.services.slb import SLBResource, LoadBalancerResource
from alibabacloud.services.vpc import VPCResource, VPCEipAddressResource
from alibabacloud.utils.utils import _assert_is_not_none

ALIBABACLOUD_ROOT = os.path.dirname(os.path.abspath(__file__))


def _get_param_from_args(args, index, name):
    if len(args) <= index:
        raise ClientException(alibabacloud.errors.ERROR_INVALID_PARAMETER,
                              "Parameter {0} required.".format(name))
    return args[index]


def get_resource(*args, **kwargs):
    resource_name = _get_param_from_args(args, 0, "resource_name")

    # FIXME more checks
    access_key_id = kwargs.get('access_key_id')
    access_key_secret = kwargs.get('access_key_secret')
    region_id = kwargs.get('region_id')

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
        client = AcsClient(access_key_id, access_key_secret, region_id)
        return service_resources[resource_name](_client=client)

    elif resource_name.lower() in normal_resources:
        instance_id = _get_param_from_args(args, 1, "resource_id")
        client = AcsClient(access_key_id, access_key_secret, region_id)
        return normal_resources[resource_name](instance_id, _client=client)

    else:
        raise ClientException(alibabacloud.errors.ERROR_CODE_SERVICE_NOT_SUPPORTED,
                              "Resource '{0}' is not currently supported.".format(resource_name))


def prepare_module(service_name, api_version):
    """
    :param service_name: Ecs or ECS or eCS
    :param api_version: 2018-06-09
    :return:
    """
    module_name = ['alibabacloud', 'clients']
    module_prefix = service_name.lower() + '_' + api_version.replace('-', '')
    client_name = service_name.upper() + 'Client'
    module_name.extend([module_prefix, client_name])
    return module_name


def client(service_name, api_version, **kwargs):
    """

    :param service_name: Ecs or ECS or eCS
    :param api_version: 2018-06-09
    :param kwargs:
    :return:
    """
    client_config = ClientConfig(**kwargs)
    module_name = prepare_module(service_name, api_version)
    print(module_name)

    try:
        client_module = __import__(
            '.'.join(module_name[:3]), globals(), locals(),
            [module_name[1], module_name[2]], 0).__dict__.get(module_name[3])

    except ImportError:
        raise NoModuleException(name='.'.join(module_name))

    return client_module(client_config)
