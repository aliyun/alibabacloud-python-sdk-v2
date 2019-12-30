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

from alibabacloud.exceptions import ClientException
from alibabacloud.utils.utils import _assert_is_list_but_not_string
from alibabacloud.utils.utils import _transfer_params, _new_get_key_in_response
from alibabacloud.vendored.six import iteritems


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

    next = __next__  # For Python 2.x compatibility

    def _clone(self):
        return ResourceCollection(
            self._page_handler,
            self._resource_creator,
            limit=self._limit,
            page_size=self._page_size,
            filter_params=copy.deepcopy(self._filter_params),
        )

    def pages(self, **kwargs):

        count = 0
        page_num = 1

        while True:

            # prepare parameters
            params = copy.deepcopy(self._filter_params)
            if params is None:
                params = {}
            if kwargs:
                params.update(kwargs)
            params['PageNumber'] = page_num
            if self._page_size:
                params['PageSize'] = self._page_size
            _params = _transfer_params(params)
            total_count, page_size, page_num, items = self._page_handler(_params)
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

    def all(self, **kwargs):
        if kwargs:
            return self.filter(**kwargs)
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
            raise ClientException(msg="count must be a positive integer.")

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


class NoPageResourceCollection(ResourceCollection):

    def pages(self, **kwargs):
        # prepare parameters
        params = copy.deepcopy(self._filter_params)
        if params is None:
            params = {}
        if kwargs:
            params.update(kwargs)
        _params = _transfer_params(params)
        items = self._page_handler(_params)

        resources = []
        for item in items:
            resource = self._resource_creator(item)
            resources.append(resource)
        return resources

    def __iter__(self):
        for item in self.pages():
            yield item

    def _clone(self):
        return NoPageResourceCollection(
            self._page_handler,
            self._resource_creator,
            limit=self._limit,
            page_size=self._page_size,
            filter_params=copy.deepcopy(self._filter_params),
        )

    def all(self, **kwargs):
        if kwargs:
            return self.filter(**kwargs)
        return self


class SubResourceCollection(ResourceCollection):
    pass


def _param_expand_to_json(params, rules, singular=True):
    for key, value in iteritems(rules):
        # key is like: instance_id or instance_ids
        # value is like: InstanceIds
        if key in params:
            if singular:
                to_add = [params[key]]
            else:
                to_add = params[key]
                _assert_is_list_but_not_string(to_add, key)
            del params[key]

            if value in params:
                raise ClientException(msg=
                                      "Param {0} is already set.".format(value))
            params[value] = json.dumps(to_add)


def _handle_param_aliases(params, aliases):
    for key, value in iteritems(aliases):
        if key in params:
            if value in params:
                raise ClientException(msg=
                                      "Param {0} is already set.".format(value))
            params[value] = params[key]
            del params[key]


def _create_resource_collection(resource_class, client, request_class,
                                key_to_resource_items,
                                key_to_resource_id,
                                key_to_total_count="TotalCount",
                                key_to_page_size="PageSize",
                                key_to_page_number="PageNumber",
                                singular_param_to_json=None,
                                plural_param_to_json=None,
                                param_aliases=None):

    def page_handler(params):
        if singular_param_to_json:
            _param_expand_to_json(params, singular_param_to_json)
        if plural_param_to_json:
            _param_expand_to_json(params, plural_param_to_json, singular=False)
        if param_aliases:
            _handle_param_aliases(params, param_aliases)

        _params = _transfer_params(params)
        response = request_class(**_params)
        return (
            _new_get_key_in_response(response, key_to_total_count),
            _new_get_key_in_response(response, key_to_page_size),
            _new_get_key_in_response(response, key_to_page_number),
            _new_get_key_in_response(response, key_to_resource_items),
        )

    def resource_creator(resource_data_item):
        resource_id = _new_get_key_in_response(resource_data_item, key_to_resource_id)
        del resource_data_item[key_to_resource_id]
        resource = resource_class(resource_id, _client=client)
        resource._assign_attributes(resource_data_item)
        return resource

    def resource_creator2(resource_data_item):
        resource = resource_class(None, _client=client)
        resource._assign_attributes(resource_data_item)
        return resource

    if key_to_resource_id is None:
        return ResourceCollection(page_handler, resource_creator2)
    else:
        return ResourceCollection(page_handler, resource_creator)


def _create_default_resource_collection(resource_class, client, request_class,
                                        key_to_resource_items,
                                        plural_param_to_json=None,
                                        param_aliases=None):
    return _create_resource_collection(resource_class, client, request_class,
                                       key_to_resource_items, None,
                                       plural_param_to_json=plural_param_to_json,
                                       param_aliases=param_aliases)


def _create_special_resource_collection(resource_class, client, request_class,
                                        key_to_resource_items,
                                        key_to_resource_id,
                                        singular_param_to_json=None,
                                        plural_param_to_json=None,
                                        param_aliases=None):
    def page_handler(params):
        if singular_param_to_json:
            _param_expand_to_json(params, singular_param_to_json)
        if plural_param_to_json:
            _param_expand_to_json(params, plural_param_to_json, singular=False)
        if param_aliases:
            _handle_param_aliases(params, param_aliases)

        _params = _transfer_params(params)
        response = request_class(**_params)

        return _new_get_key_in_response(response, key_to_resource_items)

    def resource_creator(resource_data_item):
        resource_id = _new_get_key_in_response(resource_data_item, key_to_resource_id)
        del resource_data_item[key_to_resource_id]
        resource = resource_class(resource_id, _client=client)
        resource._assign_attributes(resource_data_item)
        return resource

    def resource_creator2(resource_data_item):
        resource = resource_class(None, _client=client)
        resource._assign_attributes(resource_data_item)
        return resource

    if key_to_resource_id is None:
        return NoPageResourceCollection(page_handler, resource_creator2)
    else:
        return NoPageResourceCollection(page_handler, resource_creator)


def _create_sub_resource_without_page_collection(resource_class, client, request_class,
                                                 key_to_resource_items,
                                                 key_to_resource_id,
                                                 singular_param_to_json=None,
                                                 plural_param_to_json=None,
                                                 param_aliases=None,
                                                 parent_identifier=None,
                                                 parent_identifier_value=None):
    def page_handler(params):
        if singular_param_to_json:
            _param_expand_to_json(params, singular_param_to_json)
        if plural_param_to_json:
            _param_expand_to_json(params, plural_param_to_json, singular=False)
        if param_aliases:
            _handle_param_aliases(params, param_aliases)
        if parent_identifier:
            params.update({parent_identifier: parent_identifier_value})

        _params = _transfer_params(params)
        response = request_class(**_params)

        return _new_get_key_in_response(response, key_to_resource_items)

    def resource_creator(resource_data_item):
        resource_id = _new_get_key_in_response(resource_data_item, key_to_resource_id)
        del resource_data_item[key_to_resource_id]
        resource = resource_class(resource_id, parent_identifier_value, _client=client)
        resource._assign_attributes(resource_data_item)
        return resource

    def resource_creator2(resource_data_item):
        resource = resource_class(None, _client=client)
        resource._assign_attributes(resource_data_item)
        return resource

    if key_to_resource_id is None:
        return NoPageResourceCollection(page_handler, resource_creator2)
    else:
        return NoPageResourceCollection(page_handler, resource_creator)


def _create_sub_resource_with_page_collection(resource_class, client, request_class,
                                              key_to_resource_items,
                                              key_to_resource_id,
                                              key_to_total_count="TotalCount",
                                              key_to_page_size="PageSize",
                                              key_to_page_number="PageNumber",
                                              singular_param_to_json=None,
                                              plural_param_to_json=None,
                                              param_aliases=None,
                                              parent_identifier=None,
                                              parent_identifier_value=None):
    def page_handler(params):
        if singular_param_to_json:
            _param_expand_to_json(params, singular_param_to_json)
        if plural_param_to_json:
            _param_expand_to_json(params, plural_param_to_json, singular=False)
        if param_aliases:
            _handle_param_aliases(params, param_aliases)

        if parent_identifier:
            params.update({parent_identifier: parent_identifier_value})

        _params = _transfer_params(params)
        response = request_class(**_params)

        # return _new_get_key_in_response(response, key_to_resource_items)
        return (
            _new_get_key_in_response(response, key_to_total_count),
            _new_get_key_in_response(response, key_to_page_size),
            _new_get_key_in_response(response, key_to_page_number),
            _new_get_key_in_response(response, key_to_resource_items),
        )

    def resource_creator(resource_data_item):
        resource_id = _new_get_key_in_response(resource_data_item, key_to_resource_id)
        del resource_data_item[key_to_resource_id]
        resource = resource_class(resource_id, parent_identifier_value, _client=client)
        resource._assign_attributes(resource_data_item)
        return resource

    def resource_creator2(resource_data_item):
        resource = resource_class(None, _client=client)
        resource._assign_attributes(resource_data_item)
        return resource

    if key_to_resource_id is None:
        return ResourceCollection(page_handler, resource_creator2)
    else:
        return ResourceCollection(page_handler, resource_creator)
