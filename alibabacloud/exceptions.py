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

SDK_ENDPOINT_MANAGEMENT_DOC_HTML = "https://www.alibabacloud.com/help/doc-detail/92074.htm"


class AlibabaCloudException(Exception):
    fmt = 'An unspecified error occurred'

    def __init__(self, **kwargs):
        msg = self.fmt.format(**kwargs)
        Exception.__init__(self, msg)
        self.error_message = msg


class ClientException(AlibabaCloudException):
    """client exception"""
    fmt = '{msg}'


class HttpErrorException(AlibabaCloudException):
    fmt = '{http_error}'


class InvalidProductCode(AlibabaCloudException):
    fmt = "No endpoint for product '{product_code}'.\n" +\
          "Please check the product code, " + \
          "or set an endpoint for your request explicitly.\n" + \
          "See " + SDK_ENDPOINT_MANAGEMENT_DOC_HTML + "\n"


class InvalidRegionIDException(AlibabaCloudException):
    fmt = "No such region '{region_id}'. Please check your region ID."


class NoSuchEndpointException(AlibabaCloudException):
    fmt = "No endpoint in the region '{region_id}' for product '{product_code}'.\n" \
          "You can set an endpoint for your request explicitly.{more}\n" \
          "See " + SDK_ENDPOINT_MANAGEMENT_DOC_HTML + "\n"


class ParamTypeInvalidException(AlibabaCloudException):
    fmt = 'The type of param {param} must be {param_type}.'


class ServerException(Exception):

    def __init__(self, error_code, error_message, endpoint=None, service_name=None,
                 http_status=None, request_id=None, version=None):
        self.error_code = error_code
        self.error_message = error_message
        self.endpoint = endpoint
        # TODO service_name
        self.service_name = service_name
        self.http_status = http_status
        self.request_id = request_id
        self.version = version

    def __str__(self):
        return "HTTP Status: %s Product:%s Endpoint:%s Error:%s %s RequestID: %s Version:%s" % (
            str(self.http_status),
            self.service_name,
            self.endpoint,
            self.error_code,
            self.error_message,
            self.request_id,
            self.version
        )
