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
import copy
from aliyunsdkcore.acs_exception.exceptions import ClientException
from alibabacloud.errors import ERROR_INVALID_PARAMETER


class ResourceCollection:

    def __init__(self, get_resource_page_handler, resource_creator,
                 limit=None, page_size=None, filter_params=None):
        self._page_handler = get_resource_page_handler
        self._resource_creator = resource_creator
        self._limit = limit
        self._page_size = page_size
        self._filter_params = filter_params
        self._iterator = iter(self)

    def __iter__(self):
        for page in self.pages():
            for item in page:
                yield item

    def __next__(self):
        return next(self._iterator)

    def _clone(self):
        return ResourceCollection(
            self._page_handler,
            self._resource_creator,
            limit=self._limit,
            page_size=self._page_size,
            filter_params=copy.deepcopy(self._filter_params),
        )

    def pages(self):

        count = 0
        page_num = 1

        while True:

            # prepare parameters
            params = copy.deepcopy(self._filter_params)
            if params is None:
                params = {}
            params['PageNumber'] = page_num
            if self._page_size:
                params['PageSize'] = self._page_size

            total_count, page_size, page_num, items = self._page_handler(params)
            if self._limit is not None:
                limit = min(total_count, self._limit)
            else:
                limit = total_count

            resources = []
            for item in items:
                resource = self._resource_creator(item)
                resources.append(resource)
                count += 1
                if count >= limit:
                    break
            yield resources
            if count >= limit:
                break
            page_num += 1

    def all(self):
        return self

    def filter(self, **params):
        clone = self._clone()
        if clone._filter_params is None:
            clone._filter_params = copy.deepcopy(params)
        else:
            clone._filter_params.update(params)
        return clone

    def _check_count(self, count):
        if not isinstance(count, int) or count <= 0:
            raise ClientException(ERROR_INVALID_PARAMETER, "count must be a positive integer.")

    def limit(self, count):
        self._check_count(count)
        clone = self._clone()
        clone._limit = count
        return clone

    def page_size(self, count):
        self._check_count(count)
        clone = self._clone()
        clone._page_size = count
        return clone
