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

import os.path
import yaml
import jmespath
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
import alibabacloud
import alibabacloud.errors
from alibabacloud.resources.paginator import Paginator


class Session(object):

    def __init__(self, access_key_id=None, access_key_secret=None, region_id=None):
        self._access_key_id = access_key_id
        self._access_key_secret = access_key_secret
        self._region_id = region_id
        self._client = AcsClient(access_key_id, access_key_secret, region_id)
        self._loaded = set()
        self._services = {}
        self._resources = {}
        self._paginators = {}
        self._api_decorations = {}
        self._request_handlers = {}

    def _load(self, service_name):
        if service_name in self._loaded:
            return

        basedir = os.path.dirname(alibabacloud.__file__)
        yaml_file = os.path.join(basedir, "data", "services", service_name + ".yml")
        if not os.path.isfile(yaml_file):
            print(yaml_file)
            raise ClientException(alibabacloud.errors.ERROR_INVALID_PARAMETER,
                                  "Service '{0}' is not supported.".format(service_name))
        with open(yaml_file) as fp:
            service_data = yaml.load(fp)

        product = service_data['using_product']
        api_version = service_data['api_version']

        def request_handler(api, params):
            self._do_request(service_name, product, api_version, api, params)
        self._request_handlers[service_name] = request_handler
        self._api_decorations[service_name] = service_data['api_decorations']

        for reg in service_data['registrations']:

            if reg['type'] == 'paginator':
                self._load_paginator(service_name, reg)
            elif reg['type'] == 'resource':
                self._load_resource(reg)

    def _load_paginator(self, service_name, config):
        api = config['name'].split('.')[1]

        paginator = Paginator(self._request_handlers[service_name],
                              api,
                              config['items_path'],
                              config['total_count_path'],
                              config['page_size_path'],
                              config['page_num_path'])
        self._paginators[config['name']] = paginator

    def _load_resource(self, config):
        pass

    def _do_request(self, service_name, product, api_version, api, params):
        pass

    def get_service(self, service_name):
        self._load(service_name)
        return self._services[service_name]

    def get_resource(self, resource_name, resource_id):
        service_name = resource_name.split('.')[0]
        self._load(service_name)
        if resource_name not in self._resources:
            raise ClientException(
                alibabacloud.errors.ERROR_CODE_SERVICE_NOT_SUPPORTED,
                "Resource '{0}' is not currently supported.".format(resource_name))

        resource_class = self._resources[resource_name]
        return resource_class(resource_name, resource_id)