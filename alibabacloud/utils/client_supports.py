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

CLIENTS_DATA_PATH = os.path.join('alibabacloud', 'clients')


def _is_subclass_of_alibabacloudclient(object):
    if object.__name__ == 'AlibabaCloudClient':
        return
    from alibabacloud.client import AlibabaCloudClient
    return issubclass(object, AlibabaCloudClient)


def _get_client_classes(path):
    for name, obj in inspect.getmembers(path):
        if inspect.isclass(obj):
            if _is_subclass_of_alibabacloudclient(obj):
                return obj.__name__


def _format_api_version(api_version):
    return time.strftime("%Y-%m-%d", time.strptime(api_version, '%Y%m%d'))


def _list_available_client_services():
    # find py file ,get name ,split
    services = dict()
    for path in os.walk(CLIENTS_DATA_PATH):
        if path[0].endswith('clients'):
            files = path[2]
            if '__init__.py' in files:
                files.remove('__init__.py')
            for file in files:
                if file.endswith('.py'):
                    module_name = file.rstrip('.py')
                    service_name, api_version = module_name.split('_')
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
