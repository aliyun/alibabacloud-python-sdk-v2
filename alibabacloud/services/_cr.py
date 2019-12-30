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

from alibabacloud.resources.base import ServiceResource
from alibabacloud.utils.utils import _transfer_params


class _CRResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'cr', _client=_client)


class _CRBuildResource(ServiceResource):

    def __init__(self, build_id, _client=None):
        ServiceResource.__init__(self, "cr.build", _client=_client)
        self.build_id = build_id

    def cancel_repo(self, **params):
        _params = _transfer_params(params)
        return self._client.cancel_repo_build(build_id=self.build_id, **_params)

    def get_repo_logs(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_repo_build_logs(build_id=self.build_id, **_params)
        return response

    def get_repo_status(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_repo_build_status(build_id=self.build_id, **_params)
        return response


class _CRCollectionResource(ServiceResource):

    def __init__(self, collection_id, _client=None):
        ServiceResource.__init__(self, "cr.collection", _client=_client)
        self.collection_id = collection_id

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_collection(collection_id=self.collection_id, **_params)


class _CRBuildRuleResource(ServiceResource):

    def __init__(self, build_rule_id, _client=None):
        ServiceResource.__init__(self, "cr.build_rule", _client=_client)
        self.build_rule_id = build_rule_id

    def delete_repo(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_repo_build_rule(build_rule_id=self.build_rule_id, **_params)

    def update_repo(self, **params):
        _params = _transfer_params(params)
        return self._client.update_repo_build_rule(build_rule_id=self.build_rule_id, **_params)


class _CRWebhookResource(ServiceResource):

    def __init__(self, webhook_id, _client=None):
        ServiceResource.__init__(self, "cr.webhook", _client=_client)
        self.webhook_id = webhook_id

    def delete_repo(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_repo_webhook(webhook_id=self.webhook_id, **_params)

    def get_repo_log_list(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_repo_webhook_log_list(webhook_id=self.webhook_id, **_params)
        return response

    def update_repo(self, **params):
        _params = _transfer_params(params)
        return self._client.update_repo_webhook(webhook_id=self.webhook_id, **_params)


class _CRSourceAccountResource(ServiceResource):

    def __init__(self, source_account_id, _client=None):
        ServiceResource.__init__(self, "cr.source_account", _client=_client)
        self.source_account_id = source_account_id

    def delete_user(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_user_source_account(source_account_id=self.source_account_id,
                                                       **_params)


class _CRRepoResource(ServiceResource):

    def __init__(self, repo_ids, _client=None):
        ServiceResource.__init__(self, "cr.repo", _client=_client)
        self.repo_ids = repo_ids

    def get_batch(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_repo_batch(repo_ids=self.repo_ids, **_params)
        return response


class _CRSyncTaskResource(ServiceResource):

    def __init__(self, sync_task_id, _client=None):
        ServiceResource.__init__(self, "cr.sync_task", _client=_client)
        self.sync_task_id = sync_task_id

    def get_repo(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_repo_sync_task(sync_task_id=self.sync_task_id, **_params)
        return response
