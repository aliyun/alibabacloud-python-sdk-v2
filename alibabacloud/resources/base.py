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
import json
import jmespath
import alibabacloud.errors as errors
from aliyunsdkcore.acs_exception.exceptions import ClientException


_test_flag = False # FIXME when sdk-core has logging we won't need it


class _SearchableDict(dict):

    def search(self, expression):
        return jmespath.search(expression, self)


class ServiceResource(object):

    def __init__(self, service_name, client=None):
        self.service_name = service_name
        self._client = client

    def _do_request(self, request, params):
        for key, value in params.items():
            if hasattr(request, 'set_'+key):
                func = getattr(request, 'set_' + key)
                func(value)
            else:
                raise ClientException(errors.ERROR_INVALID_PARAMETER,
                                      "{0} has no parameter named {1}.".format(
                                          request.__class__.__name__,
                                          key,
                                      ))
        if _test_flag:
            import time
            print(time.time(), request.__class__.__name__, request.get_query_params())

        response = self._client.do_action_with_exception(request)

        if _test_flag:
            print(response.decode('utf-8'))

        return json.loads(response.decode('utf-8'), object_hook=_SearchableDict)

    @staticmethod
    def _check_server_response(obj, key):
        if key not in obj:
            raise ClientException(
                errors.ERROR_INVALID_SERVER_RESPONSE,
                "No '{0}' in server response.".format(key)
            )

    def _get_response(self, request, params, key=None, keys=None):
        response = self._do_request(request, params)
        if key:
            self._check_server_response(response, key)
            return response[key]
        if keys:
            obj = response
            for key in keys:
                self._check_server_response(obj, key)
                obj = obj[key]
            return obj

