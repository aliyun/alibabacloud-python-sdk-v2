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
import re
import jmespath
import json
import alibabacloud.errors as errors
from aliyunsdkcore.acs_exception.exceptions import ClientException

_test_flag = False  # FIXME when sdk-core has logging we won't need it


class _SearchableDict(dict):

    def search(self, expression):
        return jmespath.search(expression, self)


def _do_request(client, request, params):
    for key, value in params.items():
        if hasattr(request, 'set_' + key):
            func = getattr(request, 'set_' + key)
            func(value)
        elif key == "RegionId":
            request.add_query_param(key, value)
        else:
            raise ClientException(errors.ERROR_INVALID_PARAMETER,
                                  "{0} has no parameter named {1}.".format(
                                      request.__class__.__name__,
                                      key,
                                  ))
    if _test_flag:
        import time
        print(time.time(), request.__class__.__name__, request.get_query_params())

    response = client.do_action_with_exception(request)

    if _test_flag:
        print(response.decode('utf-8'))

    return json.loads(response.decode('utf-8'), object_hook=_SearchableDict)


def _get_key_in_response(response, key):
    result = jmespath.search(key, response)
    if result is None:
        raise ClientException(
            errors.ERROR_INVALID_SERVER_RESPONSE,
            "No '{0}' in server response.".format(key)
        )
    return result


def _get_response(client, request, params, key):
    response = _do_request(client, request, params)
    return _get_key_in_response(response, key)


def _convert_name_from_camel_case_to_snake_case(name):
    # covert name from camel case to snake case
    # e.g: InstanceName -> instance_name
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def _assert_is_list_but_not_string(item, name):
    if not isinstance(item, str) and (isinstance(item, list) or isinstance(item, tuple)):
        pass
    else:
        message = "{0} should be a list or a tuple, {1} found.".format(name,
                                                                       item.__class__.__name__)
        raise ClientException(errors.ERROR_INVALID_PARAMETER, message)


def _assert_is_not_none(item, name):
    if item is None:
        raise ClientException(errors.ERROR_INVALID_PARAMETER,
                              "{0} should not be None".format(name))
