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
import time

from mock import patch

from alibabacloud.clients.ecs_20140526 import EcsClient
from alibabacloud.exceptions import ServerException, HttpErrorException, \
    ParamTypeInvalidException
from alibabacloud.handlers.api_protocol_handler import APIProtocolHandler
from alibabacloud.handlers.credentials_handler import CredentialsHandler
from alibabacloud.handlers.endpoint_handler import EndpointHandler
from alibabacloud.handlers.http_handler import HttpHandler
from alibabacloud.handlers.retry_handler import RetryHandler
from alibabacloud.handlers.server_error_handler import ServerErrorHandler
from alibabacloud.handlers.signer_handler import SignerHandler
from alibabacloud.handlers.timeout_config_reader import TimeoutConfigReader
from alibabacloud.request import APIRequest
from base import SDKTestBase

DEFAULT_HANDLERS = [
    RetryHandler(),
    APIProtocolHandler(),
    CredentialsHandler(),
    SignerHandler(),
    TimeoutConfigReader(),
    EndpointHandler(),
    HttpHandler(),
    ServerErrorHandler(),
]


class AlibabaCloudRetryTest(SDKTestBase):

    def test_no_retry(self):
        config = self.client_config
        config.enable_retry = False
        config.endpoint = 'somewhere.you.never'
        client = EcsClient(config, self.init_credentials_provider())
        with patch.object(client, "_handle_request",
                          wraps=client._handle_request) as monkey:
            try:
                context = client.describe_instances()
                assert False
            except HttpErrorException as e:
                self.assertTrue(e.error_message.startswith(
                    "HTTPConnectionPool(host='somewhere.you.never', port=80): "
                    "Max retries exceeded with url: /"))

        self.assertEqual(1, monkey.call_count)

    def test_default_retry_times(self):
        config = self.client_config
        config.endpoint = "somewhere.you.will.never.get"
        client = EcsClient(config, self.init_credentials_provider())
        with patch.object(client.handlers[-1], "handle_request",
                          wraps=client.handlers[-1].handle_request) as monkey:
            try:
                context = client.describe_instances()
                assert False
            except HttpErrorException as e:
                self.assertTrue(e.error_message.startswith(
                    "HTTPConnectionPool(host='somewhere.you.will.never.get', port=80):"
                    " Max retries exceeded with url:"))
        self.assertEqual(4, monkey.call_count)

    def test_no_retry_on_parameter_invalid(self):
        config = self.client_config
        client = EcsClient(config, self.init_credentials_provider())
        with patch.object(client.handlers[-1], "handle_request",
                          wraps=client.handlers[-1].handle_request) as monkey:
            try:
                context = client.run_instances()
                assert False
            except ServerException as e:
                self.assertEqual(e.http_status, 400)
                self.assertEqual(e.service_name, 'Ecs')
                self.assertEqual(e.error_code, 'MissingParameter')
                self.assertTrue(e.error_message.startswith("The input parameter ImageId that is"))
                self.assertEqual(e.endpoint, 'ecs-cn-hangzhou.aliyuncs.com')
        self.assertEqual(1, monkey.call_count)

    def test_retry_with_client_token(self):
        config = self.client_config
        client = EcsClient(config, self.init_credentials_provider())
        client.max_retry_times = 3
        client.handlers = DEFAULT_HANDLERS
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC')
        api_request._params = {
            'ImageId': "coreos_1745_7_0_64_30G_alibase_20180705.vhd",
            'InstanceType': "ecs.n2.small",
        }

        globals()['_test_client_token'] = None
        globals()['_test_retry_times'] = 0

        def _handle_request(context):
            global _test_client_token
            global _test_retry_times
            context.retry_flag = False
            request = context.api_request
            if _test_retry_times > 0:
                assert _test_client_token == request._params.get("ClientToken")
            _test_retry_times += 1
            _test_client_token = request._params.get("ClientToken")
            context.exception = HttpErrorException(http_error="some error")
            from alibabacloud.request import HTTPResponse
            context.http_response = HTTPResponse('', None, {}, None)

        def no_sleep(delay):
            pass

        with patch.object(time, "sleep", no_sleep):
            with patch.object(client.handlers[6], "handle_request",
                              wraps=_handle_request) as monkey:
                try:
                    ret = client._handle_request(api_request)
                    assert False
                except HttpErrorException as e:
                    self.assertEqual("some error", e.error_message)
            self.assertEqual(4, monkey.call_count)

    def test_retry_with_client_token_set(self):
        config = self.client_config
        config.max_retry_times = 3

        client = EcsClient(config, self.init_credentials_provider())
        client.handlers = DEFAULT_HANDLERS
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC')
        api_request._params = {
            'ImageId': "coreos_1745_7_0_64_30G_alibase_20180705.vhd",
            'InstanceType': "ecs.n2.small",
            'ClientToken': "ABCDEFGHIJKLMN",
        }

        globals()['_test_retry_times'] = 0

        def _handle_request(context):
            global _test_retry_times
            context.retry_flag = False
            request = context.api_request
            assert "ABCDEFGHIJKLMN" == request._params.get("ClientToken")
            _test_retry_times += 0
            context.exception = HttpErrorException(http_error="some error")
            from alibabacloud.request import HTTPResponse
            context.http_response = HTTPResponse('', None, {}, None)

        def no_sleep(delay):
            pass

        with patch.object(time, "sleep", no_sleep):
            with patch.object(client.handlers[6], "handle_request",
                              wraps=_handle_request) as monkey:
                try:
                    ret = client._handle_request(api_request)
                    assert False
                except HttpErrorException as e:
                    self.assertEqual("some error", e.error_message)
            self.assertEqual(4, monkey.call_count)

    def test_invalid_max_retry_times(self):
        config = self.client_config
        config.max_retry_times = -1
        try:
            client = EcsClient(config, self.init_credentials_provider())
            assert False
        except ParamTypeInvalidException as e:
            self.assertEqual("The type of param max_retry_times must be positive integer.",
                             e.error_message)

    def test_set_max_retry_times(self):
        config = self.client_config
        config.max_retry_times = 8
        config.endpoint = "somewhere.you.will.never.get"
        client = EcsClient(config, self.init_credentials_provider())
        with patch.object(client.handlers[-1], "handle_request",
                          wraps=client.handlers[-1].handle_request) as monkey:
            try:
                context = client.describe_instances()
                assert False
            except HttpErrorException as e:
                self.assertTrue(e.error_message.startswith(
                    "HTTPConnectionPool(host='somewhere.you.will.never.get',"
                    " port=80): Max retries exceeded with url:"))
        self.assertEqual(9, monkey.call_count)

    def test_retry_conditions(self):
        import alibabacloud.retry.retry_policy as retry_policy
        from alibabacloud.retry.retry_condition import RetryCondition
        from alibabacloud.retry.retry_policy_context import RetryPolicyContext

        config = self.client_config
        client = EcsClient(config, self.init_credentials_provider())

        default_retry_policy = retry_policy.get_default_retry_policy()

        def HE():
            return HttpErrorException(http_error="some error")

        def SE(code):
            return ServerException(code, "some error")

        def _get_retryable(*conditions):
            context = RetryPolicyContext(*conditions)
            return default_retry_policy.should_retry(context)

        def _assert_not_retryable(*conditions):
            retryable = _get_retryable(*conditions)
            self.assertTrue(retryable & RetryCondition.NO_RETRY)

        def _assert_retryable(*conditions):
            retryable = _get_retryable(*conditions)
            self.assertFalse(retryable & RetryCondition.NO_RETRY)

        def _assert_retryable_with_client_token(request):
            conditions = [request, SE("InternalError"), 0, 500, 'ecs', '2014-05-26']
            retryable = _get_retryable(*conditions)
            self.assertTrue(retryable &
                            RetryCondition.SHOULD_RETRY_WITH_THROTTLING_BACKOFF)

        def _assert_not_retryable_with_client_token(request):
            conditions = [request, SE("InternalError"), 0, 500, 'ecs', '2014-05-26']
            retryable = _get_retryable(*conditions)
            self.assertFalse(retryable & RetryCondition.SHOULD_RETRY_WITH_THROTTLING_BACKOFF)

        # retryable
        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC')
        timeout_exception = HE()
        invalid_param_excpetion = SE("MissingParameter")
        unknown_error = SE("SDK_UNKNOWN_SERVER_ERROR")
        internal_error = SE("InternalError")
        product_code = client.product_code.lower()
        api_version = client.api_version
        _assert_retryable(api_request, timeout_exception, 0, 500, product_code,
                          api_version)
        _assert_retryable(api_request, timeout_exception, 2, 500, product_code,
                          api_version)
        _assert_retryable(api_request, unknown_error, 0, 500, product_code, api_version)
        _assert_retryable(api_request, unknown_error, 0, 502, product_code, api_version)
        _assert_retryable(api_request, unknown_error, 0, 503, product_code, api_version)
        _assert_retryable(api_request, unknown_error, 0, 504, product_code, api_version)
        _assert_retryable(api_request, internal_error, 0, 500, product_code, api_version)
        _assert_retryable(api_request, SE("Throttling"), 0, 400, product_code,
                          api_version)
        _assert_retryable(api_request, SE("ServiceUnavailable"), 0, 503, product_code,
                          api_version)
        _assert_not_retryable(api_request, invalid_param_excpetion, 0, 400, product_code,
                              api_version)
        _assert_not_retryable(api_request, timeout_exception, 3, 500, product_code,
                              api_version)
        _assert_not_retryable(api_request, SE("InvalidAccessKeyId.NotFound"), 0, 404,
                              product_code, api_version)

        request1 = APIRequest('DescribeInstanceHistoryEvents', 'GET', 'http', 'RPC')

        _assert_retryable(request1, SE("ServiceUnavailable"), 0, 503,
                          product_code, api_version)

        request2 = APIRequest('DescribeDisks', 'GET', 'http', 'RPC')

        _assert_retryable(request2, SE("ServiceUnavailable"), 0, 503,
                          product_code, api_version)
        # no_retry
        no_retry_request = APIRequest('AttachDisk', 'GET', 'http', 'RPC')

        _assert_not_retryable(no_retry_request, timeout_exception, 0, 500, product_code,
                              api_version)
        _assert_not_retryable(no_retry_request, unknown_error, 0, 504, product_code,
                              api_version)
        _assert_not_retryable(no_retry_request, invalid_param_excpetion, 0, 400, product_code,
                              api_version)
        request1 = APIRequest('CreateInstance', 'GET', 'http', 'RPC')

        _assert_retryable_with_client_token(request1)

        request1 = APIRequest('RunInstances', 'GET', 'http', 'RPC')
        _assert_retryable_with_client_token(request1)

        request1 = APIRequest('AttachDisk', 'GET', 'http', 'RPC')

        _assert_not_retryable_with_client_token(request1)

        request1 = APIRequest('DescribeInstances', 'GET', 'http', 'RPC')
        _assert_not_retryable_with_client_token(request1)

    def test_normal_backoff(self):
        config = self.client_config
        config.max_retry_times = 10
        config.endpoint = "somewhere.you.will.never.get"
        client = EcsClient(config, self.init_credentials_provider())
        request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC')

        globals()['_test_compute_delay'] = []

        def record_sleep(delay):
            global _test_compute_delay
            _test_compute_delay.append(delay)

        with patch.object(time, "sleep", wraps=record_sleep) as monkey:
            try:
                client._handle_request(request)
                assert False
            except HttpErrorException as e:
                self.assertTrue(e.error_message.startswith(
                    "HTTPConnectionPool(host='somewhere.you.will.never.get', port=80)"))
        # self.assertEqual(10, monkey.call_count)
        self.assertEqual([0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4, 12.8, 20.0, 20.0],
                         _test_compute_delay)

    def test_throttled_backoff(self):
        def _handle_response(context):
            context.exception = ServerException("Throttling", "some error")

        config = self.client_config
        config.max_retry_times = 10
        config.endpoint = "somewhere.you.will.never.get"
        client = EcsClient(config, self.init_credentials_provider())
        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC')
        globals()["_test_compute_delay"] = []

        def record_sleep(delay):
            global _test_compute_delay
            _test_compute_delay.append(delay)

        from alibabacloud.handlers.api_protocol_handler import APIProtocolHandler
        from alibabacloud.handlers.credentials_handler import CredentialsHandler
        from alibabacloud.handlers.signer_handler import SignerHandler
        from alibabacloud.handlers.timeout_config_reader import TimeoutConfigReader
        from alibabacloud.handlers.endpoint_handler import EndpointHandler
        from alibabacloud.handlers.retry_handler import RetryHandler
        from alibabacloud.handlers.server_error_handler import ServerErrorHandler
        from alibabacloud.handlers.http_handler import HttpHandler
        DEFAULT_HANDLERS = [
            RetryHandler(),
            APIProtocolHandler(),
            CredentialsHandler(),
            SignerHandler(),
            TimeoutConfigReader(),
            EndpointHandler(),
            ServerErrorHandler(),
            HttpHandler(),
        ]

        client.handlers = DEFAULT_HANDLERS
        client.config = config

        with patch.object(time, "sleep", wraps=record_sleep) as monkey:
            with patch.object(ServerErrorHandler, "handle_response", wraps=_handle_response):
                try:
                    client._handle_request(api_request)
                    assert False
                except ServerException as e:
                    self.assertEqual("Throttling", e.error_code)
        self.assertEqual(10, monkey.call_count)
        self.assertEqual(10, len(_test_compute_delay))
