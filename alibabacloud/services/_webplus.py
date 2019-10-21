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
import time

from alibabacloud.exceptions import ClientException
from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, _create_special_resource_collection
from alibabacloud.resources.collection import _create_default_resource_collection
from alibabacloud.resources.collection import _create_sub_resource_with_page_collection
from alibabacloud.resources.collection import _create_sub_resource_without_page_collection
from alibabacloud.utils.utils import _assert_is_not_none, _new_get_key_in_response, _transfer_params


class _WEBPLUSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'webplus', _client=_client)
        self.app_envs = _create_resource_collection(
            _WEBPLUSAppEnvResource, _client, _client.describe_app_envs,
            'AppEnvs.AppEnv', 'EnvId', 
        )
        self.applications = _create_resource_collection(
            _WEBPLUSApplicationResource, _client, _client.describe_applications,
            'Applications.Application', 'AppId', 
        )
        self.categories = _create_special_resource_collection(
            _WEBPLUSCategoryResource, _client, _client.describe_categories,
            'Categories.Category', 'CategoryName', 
        )
        self.changes = _create_resource_collection(
            _WEBPLUSChangeResource, _client, _client.describe_changes,
            'Changes.Change', 'ChangeId', 
        )
        self.config_templates = _create_resource_collection(
            _WEBPLUSConfigTemplateResource, _client, _client.describe_config_templates,
            'ConfigTemplates.ConfigTemplate', 'TemplateId', 
        )
        self.events = _create_resource_collection(
            _WEBPLUSEventResource, _client, _client.describe_events,
            'Events.Event', 'EventId', 
        )
        self.pkg_versions = _create_resource_collection(
            _WEBPLUSPkgVersionResource, _client, _client.describe_pkg_versions,
            'PkgVersions.PkgVersion', 'PkgVersionId', 
        )
        self.stacks = _create_resource_collection(
            _WEBPLUSStackResource, _client, _client.describe_stacks,
            'Stacks.Stack', 'StackId', 
        )
    def create_app_env(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_app_env(**_params)
        env_id = _new_get_key_in_response(response, 'EnvId')
        return _WEBPLUSAppEnvResource(env_id, _client=self._client)

    def create_application(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_application(**_params)
        app_id = _new_get_key_in_response(response, 'AppId')
        return _WEBPLUSApplicationResource(app_id, _client=self._client)

    def create_config_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_config_template(**_params)
        template_id = _new_get_key_in_response(response, 'TemplateId')
        return _WEBPLUSConfigTemplateResource(template_id, _client=self._client)

    def create_pkg_version(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_pkg_version(**_params)
        pkg_version_id = _new_get_key_in_response(response, 'PkgVersionId')
        return _WEBPLUSPkgVersionResource(pkg_version_id, _client=self._client)

    def create_storage(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_storage(**_params)
        bucket_name = _new_get_key_in_response(response, 'BucketName')
        return _WEBPLUSStorageResource(bucket_name, _client=self._client)

class _WEBPLUSAppEnvResource(ServiceResource):

    def __init__(self, env_id, _client=None):
        ServiceResource.__init__(self, "webplus.app_env", _client=_client)
        self.env_id = env_id
        
        self.aborting_change = None
        self.app_id = None
        self.app_name = None
        self.applying_change = None
        self.category_name = None
        self.change_banner = None
        self.create_time = None
        self.create_username = None
        self.data_root = None
        self.env_description = None
        self.env_name = None
        self.env_status = None
        self.env_type = None
        self.last_env_status = None
        self.latest_change_id = None
        self.log_base = None
        self.pkg_version_id = None
        self.pkg_version_label = None
        self.pkg_version_storage_key = None
        self.stack_id = None
        self.stack_name = None
        self.storage_base = None
        self.total_instances = None
        self.update_time = None
        self.update_username = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_app_env(env_id=self.env_id, **_params)

    def describe_app_env_instance_health(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_app_env_instance_health(env_id=self.env_id, **_params)

    def describe_app_env_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_app_env_status(env_id=self.env_id, **_params)

    def describe_env_resource(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_env_resource(env_id=self.env_id, **_params)

class _WEBPLUSApplicationResource(ServiceResource):

    def __init__(self, app_id, _client=None):
        ServiceResource.__init__(self, "webplus.application", _client=_client)
        self.app_id = app_id
        
        self.app_description = None
        self.app_name = None
        self.category_name = None
        self.create_time = None
        self.create_username = None
        self.running_envs = None
        self.terminated_envs = None
        self.total_envs = None
        self.update_time = None
        self.update_username = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_application(app_id=self.app_id, **_params)

class _WEBPLUSCategoryResource(ServiceResource):

    def __init__(self, category_name, _client=None):
        ServiceResource.__init__(self, "webplus.category", _client=_client)
        self.category_name = category_name
        
        self.category_description = None
        self.category_id = None
        self.category_logo = None
        self.create_time = None
        self.demo_projects = None
        self.update_time = None

class _WEBPLUSChangeResource(ServiceResource):

    def __init__(self, change_id, _client=None):
        ServiceResource.__init__(self, "webplus.change", _client=_client)
        self.change_id = change_id
        
        self.action_name = None
        self.change_aborted = None
        self.change_description = None
        self.change_finished = None
        self.change_message = None
        self.change_name = None
        self.change_paused = None
        self.change_succeed = None
        self.change_timedout = None
        self.create_time = None
        self.create_username = None
        self.env_id = None
        self.finish_time = None
        self.update_time = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_change(change_id=self.change_id, **_params)

class _WEBPLUSConfigTemplateResource(ServiceResource):

    def __init__(self, template_id, _client=None):
        ServiceResource.__init__(self, "webplus.config_template", _client=_client)
        self.template_id = template_id
        
        self.app_id = None
        self.app_name = None
        self.create_time = None
        self.pkg_version_id = None
        self.pkg_version_label = None
        self.stack_id = None
        self.stack_name = None
        self.template_description = None
        self.template_name = None
        self.update_time = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_config_template(template_id=self.template_id, **_params)

class _WEBPLUSEventResource(ServiceResource):

    def __init__(self, event_id, _client=None):
        ServiceResource.__init__(self, "webplus.event", _client=_client)
        self.event_id = event_id
        
        self.app_id = None
        self.env_id = None
        self.envent_name = None
        self.event_level = None
        self.event_message = None
        self.event_timestamp = None
        self.msg_code = None
        self.msg_params = None
        self.object_attrs = None
        self.object_id = None
        self.object_name = None
        self.object_type = None
        self.primary_user_id = None
        self.primary_user_name = None
        self.second_user_id = None
        self.second_user_name = None
        self.trace_id = None

class _WEBPLUSPkgVersionResource(ServiceResource):

    def __init__(self, pkg_version_id, _client=None):
        ServiceResource.__init__(self, "webplus.pkg_version", _client=_client)
        self.pkg_version_id = pkg_version_id
        
        self.app_id = None
        self.app_name = None
        self.create_time = None
        self.create_username = None
        self.package_source = None
        self.pkg_version_description = None
        self.pkg_version_label = None
        self.update_time = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_pkg_version(pkg_version_id=self.pkg_version_id, **_params)

class _WEBPLUSStackResource(ServiceResource):

    def __init__(self, stack_id, _client=None):
        ServiceResource.__init__(self, "webplus.stack", _client=_client)
        self.stack_id = stack_id
        
        self.category_name = None
        self.create_time = None
        self.latest_stack = None
        self.recommended_stack = None
        self.stack_name = None
        self.update_time = None
        self.version_code = None

class _WEBPLUSStorageResource(ServiceResource):

    def __init__(self, bucket_name, _client=None):
        ServiceResource.__init__(self, "webplus.storage", _client=_client)
        self.bucket_name = bucket_name
        
