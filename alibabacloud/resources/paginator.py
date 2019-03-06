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
import json
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.vendored.six import iteritems
from alibabacloud.errors import ERROR_INVALID_PARAMETER
from alibabacloud.utils import _assert_is_list_but_not_string
from alibabacloud.utils import _do_request
from alibabacloud.utils import _get_key_in_response


class Paginator:

    def __init__(self, request_handler, api,
                 items_path, total_count_path, page_size_path, page_num_path,
                 limit=None, page_size=None, filter_params=None):
        self._request_handler = request_handler
        self._api = api
        self._items_path = items_path
        self._total_count_path = total_count_path
        self._page_size_path = page_size_path
        self._page_num_path = page_num_path
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

    next = __next__  # For Python 2.x compatibility

    def _clone(self):
        return Paginator(
            self._request_handler,
            self._api,
            self._items_path,
            self._total_count_path,
            self._page_size_path,
            self._page_num_path,
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

            response = self._request_handler(self._api, params)

            total_count = _get_key_in_response(response, self._total_count_path)
            page_size = _get_key_in_response(response, self._page_size_path)
            page_num = _get_key_in_response(response, self._page_num_path)
            items = _get_key_in_response(response, self._items_path)

            if self._limit is not None:
                limit = min(total_count, self._limit)
            else:
                limit = total_count

            ret = []
            for item in items:
                ret.append(item)
                count += 1
                if count >= limit:
                    break
            yield ret
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
