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


class crClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None):
        AlibabaCloudClient.__init__(self, client_config, credentials_provider)
        self.product_code = 'cr'
        self.product_version = '2016-06-07'
        self.location_service_code = 'cr'
        self.location_endpoint_type = 'openAPI'

    def delete_user_source_account(self, source_account_id=None,):
        api_request = APIRequest(
            'DeleteUserSourceAccount',
            'DELETE',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/users/sourceAccount/[SourceAccountId]'
        api_request._params = {"SourceAccountId": source_account_id, }
        return self._handle_request(api_request).result

    def get_repo_sync_task_list(
        self,
        repo_namespace=None,
        repo_name=None,
        page_size=None,
        page=None,
    ):
        api_request = APIRequest(
            'GetRepoSyncTaskList',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/syncTasks'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "PageSize": page_size,
            "Page": page,
        }
        return self._handle_request(api_request).result

    def delete_image(self, repo_namespace=None, repo_name=None, tag=None,):
        api_request = APIRequest(
            'DeleteImage', 'DELETE', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/tags/[Tag]'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "Tag": tag,
        }
        return self._handle_request(api_request).result

    def get_authorization_token(self,):
        api_request = APIRequest(
            'GetAuthorizationToken', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/tokens'

        return self._handle_request(api_request).result

    def update_repo_source_repo(self, repo_namespace=None, repo_name=None,):
        api_request = APIRequest(
            'UpdateRepoSourceRepo',
            'POST',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/sourceRepo'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def update_user_info(self,):
        api_request = APIRequest('UpdateUserInfo', 'POST', 'http', 'ROA', '')
        api_request.uri_pattern = '/users'

        return self._handle_request(api_request).result

    def update_repo_webhook(
        self,
        repo_namespace=None,
        webhook_id=None,
        repo_name=None,
    ):
        api_request = APIRequest(
            'UpdateRepoWebhook',
            'POST',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/webhooks/[WebhookId]'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "WebhookId": webhook_id,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def update_repo_build_rule(
        self,
        repo_namespace=None,
        repo_name=None,
        build_rule_id=None,
    ):
        api_request = APIRequest(
            'UpdateRepoBuildRule',
            'POST',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/rules/[BuildRuleId]'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "BuildRuleId": build_rule_id,
        }
        return self._handle_request(api_request).result

    def update_repo_authorization(
        self,
        repo_namespace=None,
        repo_name=None,
        authorize_id=None,
    ):
        api_request = APIRequest(
            'UpdateRepoAuthorization',
            'POST',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/authorizations/[AuthorizeId]'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "AuthorizeId": authorize_id,
        }
        return self._handle_request(api_request).result

    def update_repo(self, repo_namespace=None, repo_name=None,):
        api_request = APIRequest('UpdateRepo', 'POST', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def update_namespace_authorization(
            self, authorize_id=None, namespace=None,):
        api_request = APIRequest(
            'UpdateNamespaceAuthorization',
            'POST',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/namespace/[Namespace]/authorizations/[AuthorizeId]'
        api_request._params = {
            "AuthorizeId": authorize_id,
            "Namespace": namespace,
        }
        return self._handle_request(api_request).result

    def update_namespace(self, namespace=None,):
        api_request = APIRequest(
            'UpdateNamespace', 'POST', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/namespace/[Namespace]'
        api_request._params = {"Namespace": namespace, }
        return self._handle_request(api_request).result

    def start_repo_build_by_rule(
        self,
        repo_namespace=None,
        repo_name=None,
        build_rule_id=None,
    ):
        api_request = APIRequest(
            'StartRepoBuildByRule',
            'PUT',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/rules/[BuildRuleId]/build'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "BuildRuleId": build_rule_id,
        }
        return self._handle_request(api_request).result

    def start_image_scan(self, repo_namespace=None, repo_name=None, tag=None,):
        api_request = APIRequest(
            'StartImageScan', 'PUT', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/tags/[Tag]/scan'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "Tag": tag,
        }
        return self._handle_request(api_request).result

    def search_repo(
        self,
        origin=None,
        page_size=None,
        page=None,
        keyword=None,
    ):
        api_request = APIRequest('SearchRepo', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/search'
        api_request._params = {
            "Origin": origin,
            "PageSize": page_size,
            "Page": page,
            "Keyword": keyword,
        }
        return self._handle_request(api_request).result

    def get_user_source_repo_ref_list(
        self,
        source_account_id=None,
        source_repo_name=None,
        source_repo_namespace=None,
    ):
        api_request = APIRequest(
            'GetUserSourceRepoRefList',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/users/sourceAccount/[SourceAccountId]/repos/[SourceRepoNamespace]/[SourceRepoName]/refs'
        api_request._params = {
            "SourceAccountId": source_account_id,
            "SourceRepoName": source_repo_name,
            "SourceRepoNamespace": source_repo_namespace,
        }
        return self._handle_request(api_request).result

    def get_user_source_repo_list(self, source_account_id=None,):
        api_request = APIRequest(
            'GetUserSourceRepoList',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/users/sourceAccount/[SourceAccountId]/repos'
        api_request._params = {"SourceAccountId": source_account_id, }
        return self._handle_request(api_request).result

    def get_user_source_account(self, source_origin_type=None,):
        api_request = APIRequest(
            'GetUserSourceAccount',
            'GET',
            'http',
            'ROA',
            'query')
        api_request.uri_pattern = '/users/sourceAccount'
        api_request._params = {"SourceOriginType": source_origin_type, }
        return self._handle_request(api_request).result

    def get_sub_user_list(self,):
        api_request = APIRequest('GetSubUserList', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/users/subAccount'

        return self._handle_request(api_request).result

    def get_repo_webhook_log_list(
        self,
        repo_namespace=None,
        webhook_id=None,
        repo_name=None,
    ):
        api_request = APIRequest(
            'GetRepoWebhookLogList',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/webhooks/[WebhookId]/logs'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "WebhookId": webhook_id,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def get_repo_source_repo(self, repo_namespace=None, repo_name=None,):
        api_request = APIRequest(
            'GetRepoSourceRepo', 'GET', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/sourceRepo'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def get_repo_build_rule_list(self, repo_namespace=None, repo_name=None,):
        api_request = APIRequest(
            'GetRepoBuildRuleList',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/rules'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def get_repo_build_list(
        self,
        repo_namespace=None,
        repo_name=None,
        page_size=None,
        page=None,
    ):
        api_request = APIRequest(
            'GetRepoBuildList', 'GET', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/build'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "PageSize": page_size,
            "Page": page,
        }
        return self._handle_request(api_request).result

    def get_namespace(self, namespace=None,):
        api_request = APIRequest('GetNamespace', 'GET', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/namespace/[Namespace]'
        api_request._params = {"Namespace": namespace, }
        return self._handle_request(api_request).result

    def get_mirror_list(self,):
        api_request = APIRequest('GetMirrorList', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/mirrors'

        return self._handle_request(api_request).result

    def get_image_scan(self, repo_namespace=None, repo_name=None, tag=None,):
        api_request = APIRequest('GetImageScan', 'GET', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/tags/[Tag]/scan'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "Tag": tag,
        }
        return self._handle_request(api_request).result

    def get_image_layer(self, repo_namespace=None, repo_name=None, tag=None,):
        api_request = APIRequest('GetImageLayer', 'GET', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/tags/[Tag]/layers'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "Tag": tag,
        }
        return self._handle_request(api_request).result

    def delete_repo_build_rule(
        self,
        repo_namespace=None,
        repo_name=None,
        build_rule_id=None,
    ):
        api_request = APIRequest(
            'DeleteRepoBuildRule',
            'DELETE',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/rules/[BuildRuleId]'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "BuildRuleId": build_rule_id,
        }
        return self._handle_request(api_request).result

    def delete_namespace(self, namespace=None,):
        api_request = APIRequest(
            'DeleteNamespace',
            'DELETE',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/namespace/[Namespace]'
        api_request._params = {"Namespace": namespace, }
        return self._handle_request(api_request).result

    def create_user_source_account(self,):
        api_request = APIRequest(
            'CreateUserSourceAccount', 'PUT', 'http', 'ROA', '')
        api_request.uri_pattern = '/users/sourceAccount'

        return self._handle_request(api_request).result

    def create_user_info(self,):
        api_request = APIRequest('CreateUserInfo', 'PUT', 'http', 'ROA', '')
        api_request.uri_pattern = '/users'

        return self._handle_request(api_request).result

    def create_repo_build_rule(self, repo_namespace=None, repo_name=None,):
        api_request = APIRequest(
            'CreateRepoBuildRule',
            'PUT',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/rules'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def cancel_repo_build(
        self,
        repo_namespace=None,
        repo_name=None,
        build_id=None,
    ):
        api_request = APIRequest(
            'CancelRepoBuild', 'POST', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/build/[BuildId]/cancel'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "BuildId": build_id,
        }
        return self._handle_request(api_request).result

    def get_repo_batch(self, repo_ids=None,):
        api_request = APIRequest('GetRepoBatch', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/batchsearch'
        api_request._params = {"RepoIds": repo_ids, }
        return self._handle_request(api_request).result

    def get_image_manifest(
        self,
        repo_namespace=None,
        repo_name=None,
        tag=None,
        schema_version=None,
    ):
        api_request = APIRequest(
            'GetImageManifest', 'GET', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/tags/[Tag]/manifest'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "Tag": tag,
            "SchemaVersion": schema_version,
        }
        return self._handle_request(api_request).result

    def get_collection(self, page_size=None, page=None,):
        api_request = APIRequest(
            'GetCollection', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/collections'
        api_request._params = {"PageSize": page_size, "Page": page, }
        return self._handle_request(api_request).result

    def delete_collection(self, collection_id=None,):
        api_request = APIRequest(
            'DeleteCollection',
            'DELETE',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/collections/[CollectionId]'
        api_request._params = {"CollectionId": collection_id, }
        return self._handle_request(api_request).result

    def create_collection(self,):
        api_request = APIRequest('CreateCollection', 'PUT', 'http', 'ROA', '')
        api_request.uri_pattern = '/collections'

        return self._handle_request(api_request).result

    def get_search(
        self,
        origin=None,
        page_size=None,
        page=None,
        keyword=None,
    ):
        api_request = APIRequest('GetSearch', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/search-delete'
        api_request._params = {
            "Origin": origin,
            "PageSize": page_size,
            "Page": page,
            "Keyword": keyword,
        }
        return self._handle_request(api_request).result

    def create_namespace(self,):
        api_request = APIRequest('CreateNamespace', 'PUT', 'http', 'ROA', '')
        api_request.uri_pattern = '/namespace'

        return self._handle_request(api_request).result

    def get_repo_webhook(self, repo_namespace=None, repo_name=None,):
        api_request = APIRequest(
            'GetRepoWebhook', 'GET', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/webhooks'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def delete_repo_webhook(
        self,
        repo_namespace=None,
        webhook_id=None,
        repo_name=None,
    ):
        api_request = APIRequest(
            'DeleteRepoWebhook',
            'DELETE',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/webhooks/[WebhookId]'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "WebhookId": webhook_id,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def get_repo(self, repo_namespace=None, repo_name=None,):
        api_request = APIRequest('GetRepo', 'GET', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def get_namespace_list(self, authorize=None, status=None,):
        api_request = APIRequest(
            'GetNamespaceList', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/namespace'
        api_request._params = {"Authorize": authorize, "Status": status, }
        return self._handle_request(api_request).result

    def get_repo_list_by_namespace(
        self,
        repo_namespace=None,
        page_size=None,
        page=None,
        status=None,
    ):
        api_request = APIRequest(
            'GetRepoListByNamespace',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "PageSize": page_size,
            "Page": page,
            "Status": status,
        }
        return self._handle_request(api_request).result

    def get_repo_sync_task(
        self,
        repo_namespace=None,
        repo_name=None,
        sync_task_id=None,
    ):
        api_request = APIRequest(
            'GetRepoSyncTask', 'GET', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/syncTasks/[SyncTaskId]'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "SyncTaskId": sync_task_id,
        }
        return self._handle_request(api_request).result

    def get_region(self, domain=None,):
        api_request = APIRequest('GetRegion', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/regions'
        api_request._params = {"Domain": domain, }
        return self._handle_request(api_request).result

    def create_repo_sync_task(self, repo_namespace=None, repo_name=None,):
        api_request = APIRequest(
            'CreateRepoSyncTask',
            'PUT',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/syncTasks'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def get_repo_authorization_list(
        self,
        repo_namespace=None,
        repo_name=None,
        authorize=None,
    ):
        api_request = APIRequest(
            'GetRepoAuthorizationList',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/authorizations'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "Authorize": authorize,
        }
        return self._handle_request(api_request).result

    def get_region_list(self,):
        api_request = APIRequest('GetRegionList', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/regions'

        return self._handle_request(api_request).result

    def get_namespace_authorization_list(
            self, namespace=None, authorize=None,):
        api_request = APIRequest(
            'GetNamespaceAuthorizationList',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/namespace/[Namespace]/authorizations'
        api_request._params = {
            "Namespace": namespace,
            "Authorize": authorize,
        }
        return self._handle_request(api_request).result

    def delete_repo_authorization(
        self,
        repo_namespace=None,
        repo_name=None,
        authorize_id=None,
    ):
        api_request = APIRequest(
            'DeleteRepoAuthorization',
            'DELETE',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/authorizations/[AuthorizeId]'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "AuthorizeId": authorize_id,
        }
        return self._handle_request(api_request).result

    def delete_repo(self, repo_namespace=None, repo_name=None,):
        api_request = APIRequest('DeleteRepo', 'DELETE', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def delete_namespace_authorization(
            self, authorize_id=None, namespace=None,):
        api_request = APIRequest(
            'DeleteNamespaceAuthorization',
            'DELETE',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/namespace/[Namespace]/authorizations/[AuthorizeId]'
        api_request._params = {
            "AuthorizeId": authorize_id,
            "Namespace": namespace,
        }
        return self._handle_request(api_request).result

    def create_repo_webhook(self, repo_namespace=None, repo_name=None,):
        api_request = APIRequest(
            'CreateRepoWebhook', 'PUT', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/webhooks'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def create_repo_authorization(self, repo_namespace=None, repo_name=None,):
        api_request = APIRequest(
            'CreateRepoAuthorization',
            'PUT',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/authorizations'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def create_namespace_authorization(self, namespace=None,):
        api_request = APIRequest(
            'CreateNamespaceAuthorization',
            'PUT',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/namespace/[Namespace]/authorizations'
        api_request._params = {"Namespace": namespace, }
        return self._handle_request(api_request).result

    def start_repo_build(self, repo_namespace=None, repo_name=None,):
        api_request = APIRequest(
            'StartRepoBuild', 'PUT', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/build'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
        }
        return self._handle_request(api_request).result

    def get_user_info(self,):
        api_request = APIRequest('GetUserInfo', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/users'

        return self._handle_request(api_request).result

    def get_repo_tags(
        self,
        repo_namespace=None,
        repo_name=None,
        page_size=None,
        page=None,
    ):
        api_request = APIRequest('GetRepoTags', 'GET', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/tags'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "PageSize": page_size,
            "Page": page,
        }
        return self._handle_request(api_request).result

    def get_repo_list(self, page_size=None, page=None, status=None,):
        api_request = APIRequest('GetRepoList', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/repos'
        api_request._params = {
            "PageSize": page_size,
            "Page": page,
            "Status": status,
        }
        return self._handle_request(api_request).result

    def get_repo_build_status(
        self,
        repo_namespace=None,
        repo_name=None,
        build_id=None,
    ):
        api_request = APIRequest(
            'GetRepoBuildStatus',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/build/[BuildId]/status'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "BuildId": build_id,
        }
        return self._handle_request(api_request).result

    def get_repo_build_logs(
        self,
        repo_namespace=None,
        repo_name=None,
        build_id=None,
    ):
        api_request = APIRequest(
            'GetRepoBuildLogs', 'GET', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/repos/[RepoNamespace]/[RepoName]/build/[BuildId]/logs'
        api_request._params = {
            "RepoNamespace": repo_namespace,
            "RepoName": repo_name,
            "BuildId": build_id,
        }
        return self._handle_request(api_request).result

    def create_repo(self,):
        api_request = APIRequest('CreateRepo', 'PUT', 'http', 'ROA', '')
        api_request.uri_pattern = '/repos'

        return self._handle_request(api_request).result
