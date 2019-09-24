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

from alibabacloud.client import AlibabaCloudClient
from alibabacloud.request import APIRequest
from alibabacloud.utils.parameter_validation import verify_params


class StsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Sts'
        self.api_version = '2015-04-01'
        self.location_service_code = 'sts'
        self.location_endpoint_type = 'openAPI'

    def assume_role_with_saml(
            self,
            role_arn=None,
            saml_provider_arn=None,
            saml_assertion=None,
            duration_seconds=None,
            policy=None):
        api_request = APIRequest('AssumeRoleWithSAML', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "RoleArn": role_arn,
            "SAMLProviderArn": saml_provider_arn,
            "SAMLAssertion": saml_assertion,
            "DurationSeconds": duration_seconds,
            "Policy": policy}
        return self._handle_request(api_request).result

    def get_caller_identity(self,):
        api_request = APIRequest('GetCallerIdentity', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def assume_role(
            self,
            role_arn=None,
            role_session_name=None,
            duration_seconds=None,
            policy=None):
        api_request = APIRequest('AssumeRole', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "RoleArn": role_arn,
            "RoleSessionName": role_session_name,
            "DurationSeconds": duration_seconds,
            "Policy": policy}
        return self._handle_request(api_request).result
