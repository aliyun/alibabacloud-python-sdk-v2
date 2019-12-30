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


import inspect
import os
import time

from alibabacloud.client import AlibabaCloudClient

ALIBABACLOUD_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIENTS_DATA_PATH = os.path.join(ALIBABACLOUD_ROOT, 'clients')
SERVICES_DATA_PATH = os.path.join(ALIBABACLOUD_ROOT, 'services')


def _is_subclass(object_, class_, sub=1):
    if isinstance(object_, class_):
        return
    mro = inspect.getmro(object_)
    if len(mro) > sub and mro[sub] is class_:
        return object_.__name__


def _get_client_classes(path):
    for name, obj in inspect.getmembers(path):
        if inspect.isclass(obj):
            if _is_subclass(obj, AlibabaCloudClient):
                return obj.__name__


def _format_api_version(api_version):
    return time.strftime("%Y-%m-%d", time.strptime(api_version, '%Y%m%d'))


def _list_available_client_services():
    # find py file ,get name ,split
    services = dict()
    for root, _, files in os.walk(CLIENTS_DATA_PATH):
        if root.endswith('clients'):
            if '__init__.py' in files:
                files.remove('__init__.py')
            for file in files:
                if file.endswith('.py'):
                    module_name = file.rstrip('.py')
                    service_name, api_version = module_name.rsplit('_', 1)
                    api_version = _format_api_version(api_version)
                    client_module = __import__(
                        '.'.join(['alibabacloud', 'clients', module_name]), globals(), locals(),
                        ['clients', module_name], 0)
                    client_name = _get_client_classes(client_module)
                    if service_name not in services:
                        services[service_name] = (client_name, [api_version])
                    elif api_version not in services[service_name][1]:
                        services[service_name][1].append(api_version)
    return services


def _get_resources_classes(path, sub):
    services = dict()
    services_file = path.__name__.split("\\")[-1].split(".")[-1]
    from alibabacloud.resources.base import ServiceResource
    for class_name, obj in inspect.getmembers(path):
        if inspect.isclass(obj):
            if _is_subclass(obj, ServiceResource, sub):
                try:
                    services[getattr(obj(""), "_service_name")] = obj, services_file
                except TypeError:
                    services[getattr(obj("", ""), "_service_name")] = obj, services_file
                except AttributeError:
                    services[services_file.lstrip("_")] = obj, services_file
    return services


def _read_dir_get_resources_info(generator_files, sub=1):
    services = dict()
    for file in generator_files:
        if file.endswith('.py'):
            module_name = file.rstrip('.py')
            services_module = __import__(
                '.'.join(['alibabacloud', 'services', module_name]), globals(), locals(),
                ['services', module_name], 0)
            service = _get_resources_classes(services_module, sub)
            services.update(service)
    return services


def _list_available_resource_services():
    services = dict()
    for root, _, files in os.walk(SERVICES_DATA_PATH):
        if root.endswith('services'):
            if '__init__.py' in files:
                files.remove('__init__.py')
            generator_files = [file for file in files if file.startswith("_")]
            services.update(_read_dir_get_resources_info(generator_files))
            modified_files = set(files) - set(generator_files)
            services.update(_read_dir_get_resources_info(modified_files, sub=2))
    return services
