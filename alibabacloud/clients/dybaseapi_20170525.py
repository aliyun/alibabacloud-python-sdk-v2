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


class DybaseapiClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Dybaseapi'
        self.api_version = '2017-05-25'
        self.location_service_code = 'dybaseapi'
        self.location_endpoint_type = 'openAPI'

    def query_token_for_mns_queue(
            self,
            queue_name=None,
            resource_owner_id=None,
            resource_owner_account=None,
            message_type=None,
            owner_id=None):
        api_request = APIRequest('QueryTokenForMnsQueue', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "QueueName": queue_name,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "MessageType": message_type,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result
