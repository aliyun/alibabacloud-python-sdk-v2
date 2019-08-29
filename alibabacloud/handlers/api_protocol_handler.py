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

import json
import platform

import jmespath

from alibabacloud.compat import urlencode
from alibabacloud.exceptions import ParamTypeInvalidException, ClientException
from alibabacloud.handlers import RequestHandler
from alibabacloud.utils import format_type
from alibabacloud.vendored.requests.structures import CaseInsensitiveDict
from alibabacloud.vendored.requests.structures import OrderedDict


def _user_agent_header():
    base = '%s (%s %s;%s)' \
           % ('AlibabaCloud',
              platform.system(),
              platform.release(),
              platform.machine()
              )
    return base


def _default_user_agent():
    default_agent = OrderedDict()
    default_agent['Python'] = platform.python_version()
    default_agent['Alibabacloud'] = __import__('alibabacloud').__version__
    default_agent['python-requests'] = __import__(
        'alibabacloud.vendored.requests.__version__', globals(), locals(),
        ['vendored', 'requests', '__version__'], 0).__version__

    return CaseInsensitiveDict(default_agent)


class _SearchableDict(dict):

    def search(self, expression):
        return jmespath.search(expression, self)


def _merge_user_agent(default_agent, extra_agent):
    if default_agent is None:
        return extra_agent

    if extra_agent is None:
        return default_agent
    user_agent = default_agent.copy()
    for key, value in extra_agent.items():
        if key not in default_agent:
            user_agent[key] = value
    return user_agent


def _modify_user_agent(client_user_agent):
    base = _user_agent_header()
    default_agent = _default_user_agent()
    # merge default UA and client_UA
    user_agent = _merge_user_agent(default_agent, None)
    for key, value in user_agent.items():
        base += ' %s/%s' % (key, value)
    if client_user_agent is not None:
        if not isinstance(client_user_agent, str):
            raise ParamTypeInvalidException(param='client_user_agent', param_type='str')
        return ' '.join([base, client_user_agent])
    return base


class APIProtocolHandler(RequestHandler):

    @staticmethod
    def _filter_params(params):
        # handle params
        new_params = {}

        def handle_params(params, prefix=''):
            if isinstance(params, list):
                for i in range(len(params)):
                    handle_params(params[i], prefix=prefix + '.' + str(i + 1))
            elif isinstance(params, dict):
                for item in params.keys():
                    handle_params(params.get(item), prefix=prefix + '.' + item)
            else:
                new_params[prefix.rstrip('.')] = params

        # TODO None and [] are filer
        if params is not None:
            if not isinstance(params, dict):
                raise ParamTypeInvalidException(params=params, param_type='dict')
            for key, value in params.items():
                if params[key] is not None:
                    handle_params(params=value, prefix=key)

            return new_params

    def handle_request(self, context):
        http_request = context.http_request
        api_request = context.api_request
        http_request.accept_format = 'JSON'

        # handle params to body_params or query_params
        parse_params = {
            "query": (api_request._query_params, "QueryParams"),
            "body": (api_request._body_params, "BodyParams"),
            "path": (api_request.path_params, "PathParams"),
            "header": (api_request._headers, "Headers")
        }
        # TODO default params is query_params
        if api_request.params:
            key = api_request._param_position
            if key in parse_params:
                params, position = parse_params[key]
                params.update(self._filter_params(api_request.params))
                context.client.logger.debug('Request received. Product:%s %s: %s',
                                            context.client.product_code, position, str(params))

        # handle api_request region_id, rpc and roa must
        if 'RegionId' not in api_request._query_params:
            api_request._query_params['RegionId'] = context.config.region_id

        # handle headers
        body_params = api_request._body_params
        # ROA GET POST PUT DEL
        # RPC GET POST

        if body_params:
            body = urlencode(body_params)
            api_request._content = body
            api_request._headers["Content-Type"] = format_type.APPLICATION_FORM

        elif api_request._content and "Content-Type" not in api_request._headers:
            api_request._headers["Content-Type"] = format_type.APPLICATION_OCTET_STREAM

        http_request.body = api_request._content

        user_agent = _modify_user_agent(context.config.user_agent)

        api_request._headers['User-Agent'] = user_agent
        api_request._headers['x-acs-region-id'] = str(context.config.region_id)
        api_request._headers['x-sdk-client'] = 'python/2.0.0'
        api_request._headers['Accept-Encoding'] = 'identity'

        # handle other attr
        http_request.method = api_request.method
        http_request.proxy = context.config.proxy  # {}
        http_request.scheme = api_request.scheme  # http|https
        if http_request.scheme == 'https':
            if context.config.enable_https:
                http_request.port = context.config.https_port
            else:
                raise ClientException(msg='Please make sure the config enable_https is True.')
        else:
            http_request.port = context.config.http_port

        http_request.verify = context.config.verify

    def handle_response(self, context):
        if not context.exception:
            try:
                context.result = json.loads(context.http_response.text, object_hook=_SearchableDict)
            except ValueError:
                # failed to parse body as json format
                raise ClientException(
                    msg='Failed to parse response as json format.Response:%s' % str(
                        context.http_response.text))
