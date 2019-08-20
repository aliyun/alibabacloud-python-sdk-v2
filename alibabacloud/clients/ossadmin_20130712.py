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


class OssAdminClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'OssAdmin'
        self.api_version = '2013-07-12'
        self.location_service_code = 'ossadmin'
        self.location_endpoint_type = 'openAPI'

    def put_bucket_status(self, bucket=None, uid=None, owner_account=None, bid=None, status=None):
        api_request = APIRequest('PutBucketStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Bucket": bucket,
            "uid": uid,
            "OwnerAccount": owner_account,
            "bid": bid,
            "Status": status}
        return self._handle_request(api_request).result

    def put_bucket_policy(
            self,
            log_prefix=None,
            owner_account=None,
            error_file=None,
            index_file=None,
            disallow_empty_refer=None,
            uid=None,
            log_bucket=None,
            bucket_name=None,
            location=None,
            bid=None,
            enable_dual_cluster=None,
            white_refer_list=None,
            iam_policy=None):
        api_request = APIRequest('PutBucketPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LogPrefix": log_prefix,
            "OwnerAccount": owner_account,
            "ErrorFile": error_file,
            "IndexFile": index_file,
            "DisallowEmptyRefer": disallow_empty_refer,
            "uid": uid,
            "LogBucket": log_bucket,
            "BucketName": bucket_name,
            "Location": location,
            "bid": bid,
            "EnableDualCluster": enable_dual_cluster,
            "WhiteReferList": white_refer_list,
            "IamPolicy": iam_policy}
        return self._handle_request(api_request).result

    def put_bucket_limit(self, uid=None, owner_account=None, bid=None, bucket_limit=None):
        api_request = APIRequest('PutBucketLimit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "uid": uid,
            "OwnerAccount": owner_account,
            "bid": bid,
            "BucketLimit": bucket_limit}
        return self._handle_request(api_request).result

    def get_bucket_policy(self, uid=None, bucket_name=None, owner_account=None, bid=None):
        api_request = APIRequest('GetBucketPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "uid": uid,
            "BucketName": bucket_name,
            "OwnerAccount": owner_account,
            "bid": bid}
        return self._handle_request(api_request).result

    def create_oss_instance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            ali_uid=None,
            owner_id=None,
            region=None):
        api_request = APIRequest('CreateOssInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "aliUid": ali_uid,
            "OwnerId": owner_id,
            "region": region}
        return self._handle_request(api_request).result
