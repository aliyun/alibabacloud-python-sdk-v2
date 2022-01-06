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
# -*- coding: utf-8 -*-


import json

from alibabacloud.exceptions import ServerException
from alibabacloud.handlers import RequestHandler
from alibabacloud.vendored.requests import codes
from alibabacloud.compat import ensure_string

SDK_UNKNOWN_SERVER_ERROR = 'SDK.UnknownServerError'


class ServerErrorHandler(RequestHandler):

    def handle_response(self, context):
        http_request = context.http_request
        response = context.http_response
        request_id = None
        # if isinstance(response, Response):
        if context.exception is None:
            try:
                body_obj = json.loads(response.text)
                request_id = body_obj.get('RequestId')
            except (ValueError, TypeError, AttributeError):
                # in case the response body is not a json string, return the raw
                # data instead
                pass
                # context.client.logger.warning(
                # 'Failed to parse response as json format. Response:%s', response.content)
            if response.status_code < codes.OK or response.status_code >= codes.MULTIPLE_CHOICES:

                server_error_code, server_error_message = self._parse_error_info_from_response_body(
                    context.client.logger, response.content)
                special_error_codes = {'IncompleteSignature', 'SignatureDoesNotMatch'}
                if response.status_code == codes.BAD_REQUEST and \
                        server_error_code in special_error_codes:
                    if http_request.signature == server_error_message.split(':', 1)[1]:
                        server_error_code = 'InvalidAccessKeySecret'
                        server_error_message = 'The AccessKeySecret is incorrect. ' \
                                               'Please check your AccessKeyId and AccessKeySecret.'
                context.exception = ServerException(server_error_code, server_error_message,
                                                    context.endpoint, context.client.product_code,
                                                    response.status_code, request_id,
                                                    context.client.api_version)

    @staticmethod
    def _parse_error_info_from_response_body(logger, response_body):
        error_code_to_return = SDK_UNKNOWN_SERVER_ERROR
        # TODO handle if response_body is too big
        error_message_to_return = "ServerResponseBody: " + str(response_body)
        try:
            body_obj = json.loads(ensure_string(response_body))
            if 'Code' in body_obj:
                error_code_to_return = body_obj['Code']
            if 'Message' in body_obj:
                error_message_to_return = body_obj['Message']
        except ValueError:
            # failed to parse body as json format
            logger.warning('Failed to parse response as json format. Response:%s',
                           str(response_body))
            pass

        return error_code_to_return, error_message_to_return
