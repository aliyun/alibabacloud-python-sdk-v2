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


class WebPlusClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'WebPlus'
        self.api_version = '2019-03-20'
        self.location_service_code = 'webx'
        self.location_endpoint_type = 'openAPI'

    def dry_run_rebuild_app_env(self, env_id=None):
        api_request = APIRequest('DryRunRebuildAppEnv', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/dryRunRebuild'
        api_request._params = {"EnvId": env_id}
        return self._handle_request(api_request).result

    def dry_run_create_app_env(
            self,
            option_settings=None,
            stack_id=None,
            profile_name=None,
            source_env_id=None,
            template_id=None):
        api_request = APIRequest('DryRunCreateAppEnv', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/dryRunCreate'
        api_request._params = {
            "OptionSettings": option_settings,
            "StackId": stack_id,
            "ProfileName": profile_name,
            "SourceEnvId": source_env_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def dry_run_terminate_app_env(self, env_id=None):
        api_request = APIRequest('DryRunTerminateAppEnv', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/dryRunTerminate'
        api_request._params = {"EnvId": env_id}
        return self._handle_request(api_request).result

    def delete_change(self, change_id=None):
        api_request = APIRequest('DeleteChange', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/change'
        api_request._params = {"ChangeId": change_id}
        return self._handle_request(api_request).result

    def abort_change(self, change_id=None):
        api_request = APIRequest('AbortChange', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/change/abort'
        api_request._params = {"ChangeId": change_id}
        return self._handle_request(api_request).result

    def create_app_env(
            self,
            option_settings=None,
            dry_run=None,
            env_name=None,
            stack_id=None,
            app_id=None,
            profile_name=None,
            env_description=None,
            pkg_version_id=None,
            source_env_id=None,
            template_id=None):
        api_request = APIRequest('CreateAppEnv', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/appEnv'
        api_request._params = {
            "OptionSettings": option_settings,
            "DryRun": dry_run,
            "EnvName": env_name,
            "StackId": stack_id,
            "AppId": app_id,
            "ProfileName": profile_name,
            "EnvDescription": env_description,
            "PkgVersionId": pkg_version_id,
            "SourceEnvId": source_env_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def create_application(self, app_description=None, app_name=None, category_name=None):
        api_request = APIRequest('CreateApplication', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/application'
        api_request._params = {
            "AppDescription": app_description,
            "AppName": app_name,
            "CategoryName": category_name}
        return self._handle_request(api_request).result

    def create_config_template(
            self,
            option_settings=None,
            source_template_id=None,
            app_id=None,
            stack_id=None,
            profile_name=None,
            template_name=None,
            source_env_id=None,
            pkg_version_id=None,
            template_description=None):
        api_request = APIRequest('CreateConfigTemplate', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/configTemplate'
        api_request._params = {
            "OptionSettings": option_settings,
            "SourceTemplateId": source_template_id,
            "AppId": app_id,
            "StackId": stack_id,
            "ProfileName": profile_name,
            "TemplateName": template_name,
            "SourceEnvId": source_env_id,
            "PkgVersionId": pkg_version_id,
            "TemplateDescription": template_description}
        return self._handle_request(api_request).result

    def create_pkg_version(
            self,
            package_source=None,
            pkg_version_label=None,
            pkg_version_description=None,
            app_id=None):
        api_request = APIRequest('CreatePkgVersion', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/pkgVersion'
        api_request._params = {
            "PackageSource": package_source,
            "PkgVersionLabel": pkg_version_label,
            "PkgVersionDescription": pkg_version_description,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def create_storage(self,):
        api_request = APIRequest('CreateStorage', 'POST', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v1/wam/storage'

        return self._handle_request(api_request).result

    def delete_app_env(self, env_id=None):
        api_request = APIRequest('DeleteAppEnv', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/appEnv'
        api_request._params = {"EnvId": env_id}
        return self._handle_request(api_request).result

    def delete_application(self, app_id=None):
        api_request = APIRequest('DeleteApplication', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/application'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def delete_config_template(self, template_id=None):
        api_request = APIRequest('DeleteConfigTemplate', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/configTemplate'
        api_request._params = {"TemplateId": template_id}
        return self._handle_request(api_request).result

    def delete_pkg_version(self, pkg_version_id=None):
        api_request = APIRequest('DeletePkgVersion', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/pkgVersion'
        api_request._params = {"PkgVersionId": pkg_version_id}
        return self._handle_request(api_request).result

    def describe_app_env_instance_health(self, env_id=None):
        api_request = APIRequest('DescribeAppEnvInstanceHealth', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/instanceHealth'
        api_request._params = {"EnvId": env_id}
        return self._handle_request(api_request).result

    def describe_app_envs(
            self,
            recent_updated=None,
            env_name=None,
            app_id=None,
            page_size=None,
            include_terminated=None,
            env_id=None,
            stack_search=None,
            page_number=None,
            env_search=None):
        api_request = APIRequest('DescribeAppEnvs', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/appEnv'
        api_request._params = {
            "RecentUpdated": recent_updated,
            "EnvName": env_name,
            "AppId": app_id,
            "PageSize": page_size,
            "IncludeTerminated": include_terminated,
            "EnvId": env_id,
            "StackSearch": stack_search,
            "PageNumber": page_number,
            "EnvSearch": env_search}
        return self._handle_request(api_request).result

    def describe_app_env_status(self, env_id=None):
        api_request = APIRequest('DescribeAppEnvStatus', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/status'
        api_request._params = {"EnvId": env_id}
        return self._handle_request(api_request).result

    def describe_applications(
            self,
            app_name=None,
            app_id=None,
            page_size=None,
            category_search=None,
            stack_search=None,
            page_number=None,
            app_search=None,
            env_search=None):
        api_request = APIRequest('DescribeApplications', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/application'
        api_request._params = {
            "AppName": app_name,
            "AppId": app_id,
            "PageSize": page_size,
            "CategorySearch": category_search,
            "StackSearch": stack_search,
            "PageNumber": page_number,
            "AppSearch": app_search,
            "EnvSearch": env_search}
        return self._handle_request(api_request).result

    def describe_categories(self,):
        api_request = APIRequest('DescribeCategories', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v1/wam/category'

        return self._handle_request(api_request).result

    def describe_change(self, env_id=None, change_id=None):
        api_request = APIRequest('DescribeChange', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/changeInfo'
        api_request._params = {"EnvId": env_id, "ChangeId": change_id}
        return self._handle_request(api_request).result

    def describe_changes(self, page_size=None, env_id=None, action_name=None, page_number=None):
        api_request = APIRequest('DescribeChanges', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/change'
        api_request._params = {
            "PageSize": page_size,
            "EnvId": env_id,
            "ActionName": action_name,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_config_index(self, stack_id=None, profile_name=None, env_id=None):
        api_request = APIRequest('DescribeConfigIndex', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/config/configIndex'
        api_request._params = {"StackId": stack_id, "ProfileName": profile_name, "EnvId": env_id}
        return self._handle_request(api_request).result

    def describe_config_options(self, stack_id=None, profile_name=None, env_id=None):
        api_request = APIRequest('DescribeConfigOptions', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/config/configOption'
        api_request._params = {"StackId": stack_id, "ProfileName": profile_name, "EnvId": env_id}
        return self._handle_request(api_request).result

    def describe_config_settings(
            self,
            option_name=None,
            env_id=None,
            template_id=None,
            path_name=None):
        api_request = APIRequest('DescribeConfigSettings', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/config/configSetting'
        api_request._params = {
            "OptionName": option_name,
            "EnvId": env_id,
            "TemplateId": template_id,
            "PathName": path_name}
        return self._handle_request(api_request).result

    def describe_config_templates(
            self,
            template_search=None,
            app_id=None,
            page_size=None,
            template_name=None,
            page_number=None):
        api_request = APIRequest('DescribeConfigTemplates', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/configTemplate'
        api_request._params = {
            "TemplateSearch": template_search,
            "AppId": app_id,
            "PageSize": page_size,
            "TemplateName": template_name,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_env_resource(self, env_id=None):
        api_request = APIRequest('DescribeEnvResource', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/envResource'
        api_request._params = {"EnvId": env_id}
        return self._handle_request(api_request).result

    def describe_events(
            self,
            last_change_events=None,
            reverse_by_timestamp=None,
            page_size=None,
            end_time=None,
            env_id=None,
            start_time=None,
            change_id=None,
            page_number=None):
        api_request = APIRequest('DescribeEvents', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/event'
        api_request._params = {
            "LastChangeEvents": last_change_events,
            "ReverseByTimestamp": reverse_by_timestamp,
            "PageSize": page_size,
            "EndTime": end_time,
            "EnvId": env_id,
            "StartTime": start_time,
            "ChangeId": change_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_gather_log_result(self, change_id=None):
        api_request = APIRequest('DescribeGatherLogResult', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/gatherLog'
        api_request._params = {"ChangeId": change_id}
        return self._handle_request(api_request).result

    def describe_gather_stats_result(self, change_id=None):
        api_request = APIRequest('DescribeGatherStatsResult', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/gatherStats'
        api_request._params = {"ChangeId": change_id}
        return self._handle_request(api_request).result

    def describe_instance_health(self, instance_id=None):
        api_request = APIRequest('DescribeInstanceHealth', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/instance/health'
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def describe_pkg_versions(
            self,
            pkg_version_label=None,
            app_id=None,
            page_size=None,
            pkg_version_search=None,
            page_number=None):
        api_request = APIRequest('DescribePkgVersions', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/pkgVersion'
        api_request._params = {
            "PkgVersionLabel": pkg_version_label,
            "AppId": app_id,
            "PageSize": page_size,
            "PkgVersionSearch": pkg_version_search,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_stacks(
            self,
            page_size=None,
            category_name=None,
            recommended_only=None,
            page_number=None):
        api_request = APIRequest('DescribeStacks', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v1/wam/stack'
        api_request._params = {
            "PageSize": page_size,
            "CategoryName": category_name,
            "RecommendedOnly": recommended_only,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_storage(self,):
        api_request = APIRequest('DescribeStorage', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v1/wam/storage'

        return self._handle_request(api_request).result

    def gather_app_env_log(self, log_path=None, target_instances=None, env_id=None):
        api_request = APIRequest('GatherAppEnvLog', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/gatherLog'
        api_request._params = {
            "LogPath": log_path,
            "TargetInstances": target_instances,
            "EnvId": env_id}
        return self._handle_request(api_request).result

    def gather_app_env_stats(self, target_instances=None, env_id=None):
        api_request = APIRequest('GatherAppEnvStats', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/gatherStats'
        api_request._params = {"TargetInstances": target_instances, "EnvId": env_id}
        return self._handle_request(api_request).result

    def pause_change(self, change_id=None):
        api_request = APIRequest('PauseChange', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/change/pause'
        api_request._params = {"ChangeId": change_id}
        return self._handle_request(api_request).result

    def rebuild_app_env(self, dry_run=None, env_id=None):
        api_request = APIRequest('RebuildAppEnv', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/rebuild'
        api_request._params = {"DryRun": dry_run, "EnvId": env_id}
        return self._handle_request(api_request).result

    def restart_app_env(self, env_id=None):
        api_request = APIRequest('RestartAppEnv', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/restart'
        api_request._params = {"EnvId": env_id}
        return self._handle_request(api_request).result

    def resume_change(self, change_id=None):
        api_request = APIRequest('ResumeChange', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/change/resume'
        api_request._params = {"ChangeId": change_id}
        return self._handle_request(api_request).result

    def start_app_env(self, env_id=None):
        api_request = APIRequest('StartAppEnv', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/start'
        api_request._params = {"EnvId": env_id}
        return self._handle_request(api_request).result

    def stop_app_env(self, env_id=None):
        api_request = APIRequest('StopAppEnv', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/stop'
        api_request._params = {"EnvId": env_id}
        return self._handle_request(api_request).result

    def terminate_app_env(self, dry_run=None, env_id=None):
        api_request = APIRequest('TerminateAppEnv', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/appEnv/terminate'
        api_request._params = {"DryRun": dry_run, "EnvId": env_id}
        return self._handle_request(api_request).result

    def update_app_env(
            self,
            option_settings=None,
            dry_run=None,
            stack_id=None,
            env_description=None,
            env_id=None,
            pkg_version_id=None):
        api_request = APIRequest('UpdateAppEnv', 'PUT', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/appEnv'
        api_request._params = {
            "OptionSettings": option_settings,
            "DryRun": dry_run,
            "StackId": stack_id,
            "EnvDescription": env_description,
            "EnvId": env_id,
            "PkgVersionId": pkg_version_id}
        return self._handle_request(api_request).result

    def update_application(self, app_description=None, app_id=None):
        api_request = APIRequest('UpdateApplication', 'PUT', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/application'
        api_request._params = {"AppDescription": app_description, "AppId": app_id}
        return self._handle_request(api_request).result

    def update_config_template(
            self,
            option_settings=None,
            template_id=None,
            template_description=None):
        api_request = APIRequest('UpdateConfigTemplate', 'PUT', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/configTemplate'
        api_request._params = {
            "OptionSettings": option_settings,
            "TemplateId": template_id,
            "TemplateDescription": template_description}
        return self._handle_request(api_request).result

    def validate_config_setting(
            self,
            option_settings=None,
            stack_id=None,
            env_id=None,
            template_id=None):
        api_request = APIRequest('ValidateConfigSetting', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/pop/v1/wam/config/configSetting/validate'
        api_request._params = {
            "OptionSettings": option_settings,
            "StackId": stack_id,
            "EnvId": env_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result
