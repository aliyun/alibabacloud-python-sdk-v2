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


class VodClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'vod'
        self.api_version = '2017-03-21'
        self.location_service_code = 'vod'
        self.location_endpoint_type = 'openAPI'

    def modify_vod_domain_schdm_by_property(self, property_=None, domain_name=None, owner_id=None):
        api_request = APIRequest('ModifyVodDomainSchdmByProperty', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Property": property_,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_ai_video_tag_result(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            media_id=None):
        api_request = APIRequest('GetAIVideoTagResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "MediaId": media_id}
        return self._handle_request(api_request).result

    def get_upload_details(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            resource_real_owner_id=None,
            media_ids=None,
            owner_id=None,
            media_type=None):
        api_request = APIRequest('GetUploadDetails', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ResourceRealOwnerId": resource_real_owner_id,
            "MediaIds": media_ids,
            "OwnerId": owner_id,
            "MediaType": media_type}
        return self._handle_request(api_request).result

    def describe_vod_storage_data(
            self,
            start_time=None,
            storage=None,
            storage_type=None,
            end_time=None,
            owner_id=None,
            region=None):
        api_request = APIRequest('DescribeVodStorageData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Storage": storage,
            "StorageType": storage_type,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Region": region}
        return self._handle_request(api_request).result

    def describe_vod_ai_data(
            self,
            start_time=None,
            ai_type=None,
            end_time=None,
            owner_id=None,
            region=None):
        api_request = APIRequest('DescribeVodAIData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "AIType": ai_type,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Region": region}
        return self._handle_request(api_request).result

    def describe_vod_transcode_data(
            self,
            start_time=None,
            storage=None,
            end_time=None,
            specification=None,
            owner_id=None,
            region=None):
        api_request = APIRequest('DescribeVodTranscodeData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Storage": storage,
            "EndTime": end_time,
            "Specification": specification,
            "OwnerId": owner_id,
            "Region": region}
        return self._handle_request(api_request).result

    def delete_multipart_upload(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            resource_real_owner_id=None,
            owner_id=None,
            media_id=None,
            media_type=None):
        api_request = APIRequest('DeleteMultipartUpload', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id,
            "MediaId": media_id,
            "MediaType": media_type}
        return self._handle_request(api_request).result

    def get_attached_media_info(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            output_type=None,
            media_ids=None,
            resource_real_owner_id=None,
            owner_id=None,
            auth_timeout=None):
        api_request = APIRequest('GetAttachedMediaInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OutputType": output_type,
            "MediaIds": media_ids,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id,
            "AuthTimeout": auth_timeout}
        return self._handle_request(api_request).result

    def delete_attached_media(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            media_ids=None,
            owner_id=None):
        api_request = APIRequest('DeleteAttachedMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "MediaIds": media_ids,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_attached_media_infos(
            self,
            resource_owner_id=None,
            update_content=None,
            resource_owner_account=None,
            resource_real_owner_id=None,
            owner_id=None):
        api_request = APIRequest('UpdateAttachedMediaInfos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UpdateContent": update_content,
            "ResourceOwnerAccount": resource_owner_account,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def attach_app_policy_to_identity(
            self,
            identity_name=None,
            resource_owner_id=None,
            identity_type=None,
            resource_owner_account=None,
            app_id=None,
            policy_names=None,
            resource_real_owner_id=None,
            owner_id=None):
        api_request = APIRequest('AttachAppPolicyToIdentity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IdentityName": identity_name,
            "ResourceOwnerId": resource_owner_id,
            "IdentityType": identity_type,
            "ResourceOwnerAccount": resource_owner_account,
            "AppId": app_id,
            "PolicyNames": policy_names,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def detach_app_policy_from_identity(
            self,
            identity_name=None,
            resource_owner_id=None,
            identity_type=None,
            resource_owner_account=None,
            app_id=None,
            policy_names=None,
            owner_id=None):
        api_request = APIRequest('DetachAppPolicyFromIdentity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IdentityName": identity_name,
            "ResourceOwnerId": resource_owner_id,
            "IdentityType": identity_type,
            "ResourceOwnerAccount": resource_owner_account,
            "AppId": app_id,
            "PolicyNames": policy_names,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def list_app_policies_for_identity(
            self,
            identity_name=None,
            resource_owner_id=None,
            identity_type=None,
            resource_owner_account=None,
            app_id=None,
            owner_id=None):
        api_request = APIRequest('ListAppPoliciesForIdentity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IdentityName": identity_name,
            "ResourceOwnerId": resource_owner_id,
            "IdentityType": identity_type,
            "ResourceOwnerAccount": resource_owner_account,
            "AppId": app_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_app_info(
            self,
            resource_owner_id=None,
            app_name=None,
            resource_owner_account=None,
            description=None,
            resource_real_owner_id=None,
            owner_id=None):
        api_request = APIRequest('CreateAppInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AppName": app_name,
            "ResourceOwnerAccount": resource_owner_account,
            "Description": description,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_app_infos(
            self,
            resource_owner_id=None,
            app_ids=None,
            resource_owner_account=None,
            resource_real_owner_id=None,
            owner_id=None):
        api_request = APIRequest('GetAppInfos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AppIds": app_ids,
            "ResourceOwnerAccount": resource_owner_account,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_app_info(
            self,
            resource_owner_id=None,
            app_name=None,
            resource_owner_account=None,
            app_id=None,
            description=None,
            resource_real_owner_id=None,
            owner_id=None,
            status=None):
        api_request = APIRequest('UpdateAppInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AppName": app_name,
            "ResourceOwnerAccount": resource_owner_account,
            "AppId": app_id,
            "Description": description,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id,
            "Status": status}
        return self._handle_request(api_request).result

    def delete_app_info(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            app_id=None,
            resource_real_owner_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteAppInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "AppId": app_id,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def list_app_info(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            page_no=None,
            page_size=None,
            resource_real_owner_id=None,
            owner_id=None,
            status=None):
        api_request = APIRequest('ListAppInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PageNo": page_no,
            "PageSize": page_size,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id,
            "Status": status}
        return self._handle_request(api_request).result

    def move_app_resource(
            self,
            target_app_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            resource_real_owner_id=None,
            owner_id=None,
            resource_type=None,
            resource_ids=None):
        api_request = APIRequest('MoveAppResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TargetAppId": target_app_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id,
            "ResourceType": resource_type,
            "ResourceIds": resource_ids}
        return self._handle_request(api_request).result

    def delete_message_callback(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            app_id=None,
            resource_real_owner_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteMessageCallback', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AppId": app_id,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_transcode_summary(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            video_ids=None):
        api_request = APIRequest('GetTranscodeSummary', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "VideoIds": video_ids}
        return self._handle_request(api_request).result

    def list_transcode_task(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            page_no=None,
            page_size=None,
            end_time=None,
            video_id=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('ListTranscodeTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PageNo": page_no,
            "PageSize": page_size,
            "EndTime": end_time,
            "VideoId": video_id,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_transcode_task(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            transcode_task_id=None,
            owner_id=None):
        api_request = APIRequest('GetTranscodeTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "TranscodeTaskId": transcode_task_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_url_upload_infos(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            upload_ur_ls=None,
            owner_id=None):
        api_request = APIRequest('GetURLUploadInfos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "UploadURLs": upload_ur_ls,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_transcode_template_group(
            self,
            transcode_template_list=None,
            resource_owner_id=None,
            resource_owner_account=None,
            name=None,
            owner_id=None,
            locked=None,
            transcode_template_group_id=None):
        api_request = APIRequest('UpdateTranscodeTemplateGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TranscodeTemplateList": transcode_template_list,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Name": name,
            "OwnerId": owner_id,
            "Locked": locked,
            "TranscodeTemplateGroupId": transcode_template_group_id}
        return self._handle_request(api_request).result

    def add_transcode_template_group(
            self,
            transcode_template_list=None,
            resource_owner_id=None,
            resource_owner_account=None,
            app_id=None,
            name=None,
            owner_id=None,
            transcode_template_group_id=None):
        api_request = APIRequest('AddTranscodeTemplateGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TranscodeTemplateList": transcode_template_list,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "AppId": app_id,
            "Name": name,
            "OwnerId": owner_id,
            "TranscodeTemplateGroupId": transcode_template_group_id}
        return self._handle_request(api_request).result

    def delete_transcode_template_group(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            transcode_template_ids=None,
            owner_id=None,
            transcode_template_group_id=None,
            force_del_group=None):
        api_request = APIRequest('DeleteTranscodeTemplateGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "TranscodeTemplateIds": transcode_template_ids,
            "OwnerId": owner_id,
            "TranscodeTemplateGroupId": transcode_template_group_id,
            "ForceDelGroup": force_del_group}
        return self._handle_request(api_request).result

    def get_transcode_template_group(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            transcode_template_group_id=None):
        api_request = APIRequest('GetTranscodeTemplateGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "TranscodeTemplateGroupId": transcode_template_group_id}
        return self._handle_request(api_request).result

    def set_default_transcode_template_group(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            transcode_template_group_id=None):
        api_request = APIRequest('SetDefaultTranscodeTemplateGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "TranscodeTemplateGroupId": transcode_template_group_id}
        return self._handle_request(api_request).result

    def list_transcode_template_group(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            page_no=None,
            app_id=None,
            page_size=None,
            owner_id=None):
        api_request = APIRequest('ListTranscodeTemplateGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PageNo": page_no,
            "AppId": app_id,
            "PageSize": page_size,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_ai_media_audit_job(
            self,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('GetAIMediaAuditJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_ai_media_audit_job(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            media_id=None,
            template_id=None):
        api_request = APIRequest('SubmitAIMediaAuditJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "MediaId": media_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def get_media_audit_result(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            resource_real_owner_id=None,
            owner_id=None,
            media_id=None):
        api_request = APIRequest('GetMediaAuditResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id,
            "MediaId": media_id}
        return self._handle_request(api_request).result

    def get_media_audit_result_detail(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            page_no=None,
            owner_id=None,
            media_id=None):
        api_request = APIRequest('GetMediaAuditResultDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PageNo": page_no,
            "OwnerId": owner_id,
            "MediaId": media_id}
        return self._handle_request(api_request).result

    def get_media_audit_result_timeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            media_id=None):
        api_request = APIRequest('GetMediaAuditResultTimeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "MediaId": media_id}
        return self._handle_request(api_request).result

    def add_ai_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            template_config=None,
            template_type=None,
            template_name=None,
            owner_id=None):
        api_request = APIRequest('AddAITemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "TemplateConfig": template_config,
            "TemplateType": template_type,
            "TemplateName": template_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_ai_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            template_id=None):
        api_request = APIRequest('DeleteAITemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def update_ai_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            template_config=None,
            template_name=None,
            owner_id=None,
            template_id=None):
        api_request = APIRequest('UpdateAITemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "TemplateConfig": template_config,
            "TemplateName": template_name,
            "OwnerId": owner_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def get_ai_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            template_id=None):
        api_request = APIRequest('GetAITemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def list_ai_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            template_type=None,
            owner_id=None):
        api_request = APIRequest('ListAITemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "TemplateType": template_type,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_default_ai_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            template_type=None,
            owner_id=None):
        api_request = APIRequest('GetDefaultAITemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "TemplateType": template_type,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_default_ai_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            template_id=None):
        api_request = APIRequest('SetDefaultAITemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def describe_vod_domain_log(
            self,
            start_time=None,
            page_number=None,
            page_size=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeVodDomainLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "PageNumber": page_number,
            "PageSize": page_size,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vod_domain_certificate_info(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeVodDomainCertificateInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vod_domain_traffic_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeVodDomainTrafficData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_vod_domain_bps_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeVodDomainBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_vod_domain_usage_data(
            self,
            start_time=None,
            type_=None,
            area=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            field=None):
        api_request = APIRequest('DescribeVodDomainUsageData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Type": type_,
            "Area": area,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Field": field}
        return self._handle_request(api_request).result

    def describe_vod_certificate_list(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeVodCertificateList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_stop_vod_domain(self, security_token=None, domain_names=None, owner_id=None):
        api_request = APIRequest('BatchStopVodDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_vod_domain(
            self,
            security_token=None,
            owner_account=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteVodDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_vod_domain_certificate(
            self,
            security_token=None,
            ssl_pub=None,
            cert_name=None,
            ssl_protocol=None,
            domain_name=None,
            owner_id=None,
            region=None,
            ssl_pri=None):
        api_request = APIRequest('SetVodDomainCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "SSLPub": ssl_pub,
            "CertName": cert_name,
            "SSLProtocol": ssl_protocol,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "Region": region,
            "SSLPri": ssl_pri}
        return self._handle_request(api_request).result

    def delete_vod_specific_config(
            self,
            security_token=None,
            config_id=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteVodSpecificConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ConfigId": config_id,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_set_vod_domain_configs(
            self,
            functions=None,
            security_token=None,
            domain_names=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('BatchSetVodDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Functions": functions,
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_vod_domain(
            self,
            sources=None,
            security_token=None,
            owner_account=None,
            scope=None,
            domain_name=None,
            owner_id=None,
            check_url=None):
        api_request = APIRequest('AddVodDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Sources": sources,
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "Scope": scope,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "CheckUrl": check_url}
        return self._handle_request(api_request).result

    def describe_vod_refresh_quota(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeVodRefreshQuota', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vod_refresh_tasks(
            self,
            object_path=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            resource_group_id=None,
            security_token=None,
            page_size=None,
            object_type=None,
            task_id=None,
            status=None):
        api_request = APIRequest('DescribeVodRefreshTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ObjectPath": object_path,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "ResourceGroupId": resource_group_id,
            "SecurityToken": security_token,
            "PageSize": page_size,
            "ObjectType": object_type,
            "TaskId": task_id,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_vod_domain_configs(
            self,
            function_names=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeVodDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FunctionNames": function_names,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vod_user_domains(
            self,
            func_filter=None,
            check_domain_show=None,
            security_token=None,
            cdn_type=None,
            page_size=None,
            domain_name=None,
            owner_id=None,
            func_id=None,
            page_number=None,
            domain_status=None,
            domain_search_type=None):
        api_request = APIRequest('DescribeVodUserDomains', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FuncFilter": func_filter,
            "CheckDomainShow": check_domain_show,
            "SecurityToken": security_token,
            "CdnType": cdn_type,
            "PageSize": page_size,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "FuncId": func_id,
            "PageNumber": page_number,
            "DomainStatus": domain_status,
            "DomainSearchType": domain_search_type}
        return self._handle_request(api_request).result

    def update_vod_domain(
            self,
            top_level_domain=None,
            sources=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('UpdateVodDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "Sources": sources,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def refresh_vod_object_caches(
            self,
            security_token=None,
            object_path=None,
            owner_id=None,
            object_type=None):
        api_request = APIRequest('RefreshVodObjectCaches', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ObjectPath": object_path,
            "OwnerId": owner_id,
            "ObjectType": object_type}
        return self._handle_request(api_request).result

    def preload_vod_object_caches(self, security_token=None, object_path=None, owner_id=None):
        api_request = APIRequest('PreloadVodObjectCaches', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "ObjectPath": object_path,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_start_vod_domain(self, security_token=None, domain_names=None, owner_id=None):
        api_request = APIRequest('BatchStartVodDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vod_domain_detail(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeVodDomainDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_vod_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            vod_template_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteVodTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "VodTemplateId": vod_template_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_vod_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            vod_template_id=None,
            owner_id=None):
        api_request = APIRequest('GetVodTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "VodTemplateId": vod_template_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def list_vod_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            template_type=None,
            app_id=None,
            owner_id=None):
        api_request = APIRequest('ListVodTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "TemplateType": template_type,
            "AppId": app_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_vod_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            template_config=None,
            name=None,
            vod_template_id=None,
            owner_id=None):
        api_request = APIRequest('UpdateVodTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "TemplateConfig": template_config,
            "Name": name,
            "VodTemplateId": vod_template_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_vod_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            template_config=None,
            template_type=None,
            app_id=None,
            name=None,
            owner_id=None,
            sub_template_type=None):
        api_request = APIRequest('AddVodTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "TemplateConfig": template_config,
            "TemplateType": template_type,
            "AppId": app_id,
            "Name": name,
            "OwnerId": owner_id,
            "SubTemplateType": sub_template_type}
        return self._handle_request(api_request).result

    def create_upload_attached_media(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cate_ids=None,
            icon=None,
            description=None,
            file_size=None,
            owner_id=None,
            title=None,
            business_type=None,
            tags=None,
            storage_location=None,
            user_data=None,
            media_ext=None,
            file_name=None,
            cate_id=None,
            app_id=None):
        api_request = APIRequest('CreateUploadAttachedMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CateIds": cate_ids,
            "Icon": icon,
            "Description": description,
            "FileSize": file_size,
            "OwnerId": owner_id,
            "Title": title,
            "BusinessType": business_type,
            "Tags": tags,
            "StorageLocation": storage_location,
            "UserData": user_data,
            "MediaExt": media_ext,
            "FileName": file_name,
            "CateId": cate_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def register_media(
            self,
            user_data=None,
            resource_owner_id=None,
            template_group_id=None,
            resource_owner_account=None,
            owner_id=None,
            register_metadatas=None,
            workflow_id=None):
        api_request = APIRequest('RegisterMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "TemplateGroupId": template_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "RegisterMetadatas": register_metadatas,
            "WorkflowId": workflow_id}
        return self._handle_request(api_request).result

    def delete_watermark(
            self,
            watermark_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteWatermark', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WatermarkId": watermark_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_watermark(
            self,
            watermark_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('GetWatermark', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WatermarkId": watermark_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_default_watermark(
            self,
            watermark_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('SetDefaultWatermark', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WatermarkId": watermark_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def list_watermark(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            page_no=None,
            app_id=None,
            page_size=None,
            owner_id=None):
        api_request = APIRequest('ListWatermark', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PageNo": page_no,
            "AppId": app_id,
            "PageSize": page_size,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_watermark(
            self,
            watermark_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            name=None,
            owner_id=None,
            watermark_config=None):
        api_request = APIRequest('UpdateWatermark', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WatermarkId": watermark_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Name": name,
            "OwnerId": owner_id,
            "WatermarkConfig": watermark_config}
        return self._handle_request(api_request).result

    def add_watermark(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            app_id=None,
            name=None,
            file_url=None,
            owner_id=None,
            type_=None,
            watermark_config=None):
        api_request = APIRequest('AddWatermark', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "AppId": app_id,
            "Name": name,
            "FileUrl": file_url,
            "OwnerId": owner_id,
            "Type": type_,
            "WatermarkConfig": watermark_config}
        return self._handle_request(api_request).result

    def get_media_dna_result(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            media_id=None):
        api_request = APIRequest('GetMediaDNAResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "MediaId": media_id}
        return self._handle_request(api_request).result

    def delete_mezzanines(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            force=None,
            owner_id=None,
            video_ids=None):
        api_request = APIRequest('DeleteMezzanines', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Force": force,
            "OwnerId": owner_id,
            "VideoIds": video_ids}
        return self._handle_request(api_request).result

    def update_image_infos(
            self,
            resource_owner_id=None,
            update_content=None,
            resource_owner_account=None,
            resource_real_owner_id=None,
            owner_id=None):
        api_request = APIRequest('UpdateImageInfos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UpdateContent": update_content,
            "ResourceOwnerAccount": resource_owner_account,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_image(
            self,
            resource_owner_id=None,
            image_type=None,
            resource_owner_account=None,
            image_ur_ls=None,
            video_id=None,
            owner_id=None,
            delete_image_type=None,
            image_ids=None):
        api_request = APIRequest('DeleteImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImageType": image_type,
            "ResourceOwnerAccount": resource_owner_account,
            "ImageURLs": image_ur_ls,
            "VideoId": video_id,
            "OwnerId": owner_id,
            "DeleteImageType": delete_image_type,
            "ImageIds": image_ids}
        return self._handle_request(api_request).result

    def list_audit_security_ip(self, security_group_name=None):
        api_request = APIRequest('ListAuditSecurityIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityGroupName": security_group_name}
        return self._handle_request(api_request).result

    def set_audit_security_ip(self, operate_mode=None, security_group_name=None, ips=None):
        api_request = APIRequest('SetAuditSecurityIp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OperateMode": operate_mode,
            "SecurityGroupName": security_group_name,
            "Ips": ips}
        return self._handle_request(api_request).result

    def upload_media_by_url(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            message_callback=None,
            owner_id=None,
            priority=None,
            storage_location=None,
            user_data=None,
            template_group_id=None,
            upload_metadatas=None,
            upload_ur_ls=None,
            app_id=None,
            workflow_id=None):
        api_request = APIRequest('UploadMediaByURL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "MessageCallback": message_callback,
            "OwnerId": owner_id,
            "Priority": priority,
            "StorageLocation": storage_location,
            "UserData": user_data,
            "TemplateGroupId": template_group_id,
            "UploadMetadatas": upload_metadatas,
            "UploadURLs": upload_ur_ls,
            "AppId": app_id,
            "WorkflowId": workflow_id}
        return self._handle_request(api_request).result

    def update_video_infos(
            self,
            resource_owner_id=None,
            update_content=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('UpdateVideoInfos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "UpdateContent": update_content,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def search_media(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            match=None,
            session_id=None,
            owner_id=None,
            scroll_token=None,
            page_no=None,
            search_type=None,
            page_size=None,
            sort_by=None,
            result_types=None,
            fields=None):
        api_request = APIRequest('SearchMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Match": match,
            "SessionId": session_id,
            "OwnerId": owner_id,
            "ScrollToken": scroll_token,
            "PageNo": page_no,
            "SearchType": search_type,
            "PageSize": page_size,
            "SortBy": sort_by,
            "ResultTypes": result_types,
            "Fields": fields}
        return self._handle_request(api_request).result

    def get_video_infos(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            addition_type=None,
            owner_id=None,
            video_ids=None):
        api_request = APIRequest('GetVideoInfos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "AdditionType": addition_type,
            "OwnerId": owner_id,
            "VideoIds": video_ids}
        return self._handle_request(api_request).result

    def submit_preprocess_jobs(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            video_id=None,
            owner_id=None,
            preprocess_type=None):
        api_request = APIRequest('SubmitPreprocessJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "VideoId": video_id,
            "OwnerId": owner_id,
            "PreprocessType": preprocess_type}
        return self._handle_request(api_request).result

    def describe_play_video_statis(
            self,
            start_time=None,
            end_time=None,
            video_id=None,
            owner_id=None):
        api_request = APIRequest('DescribePlayVideoStatis', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "EndTime": end_time,
            "VideoId": video_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_play_user_total(self, start_time=None, end_time=None, owner_id=None):
        api_request = APIRequest('DescribePlayUserTotal', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"StartTime": start_time, "EndTime": end_time, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_play_user_avg(self, start_time=None, end_time=None, owner_id=None):
        api_request = APIRequest('DescribePlayUserAvg', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"StartTime": start_time, "EndTime": end_time, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_play_top_videos(self, page_size=None, owner_id=None, biz_date=None, page_no=None):
        api_request = APIRequest('DescribePlayTopVideos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "OwnerId": owner_id,
            "BizDate": biz_date,
            "PageNo": page_no}
        return self._handle_request(api_request).result

    def list_snapshots(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            snapshot_type=None,
            page_no=None,
            page_size=None,
            video_id=None,
            owner_id=None,
            auth_timeout=None):
        api_request = APIRequest('ListSnapshots', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "SnapshotType": snapshot_type,
            "PageNo": page_no,
            "PageSize": page_size,
            "VideoId": video_id,
            "OwnerId": owner_id,
            "AuthTimeout": auth_timeout}
        return self._handle_request(api_request).result

    def submit_transcode_jobs(
            self,
            user_data=None,
            resource_owner_id=None,
            template_group_id=None,
            resource_owner_account=None,
            video_id=None,
            override_params=None,
            owner_id=None,
            priority=None,
            encrypt_config=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitTranscodeJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "TemplateGroupId": template_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "VideoId": video_id,
            "OverrideParams": override_params,
            "OwnerId": owner_id,
            "Priority": priority,
            "EncryptConfig": encrypt_config,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def list_live_record_video(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            app_name=None,
            page_no=None,
            page_size=None,
            sort_by=None,
            stream_name=None,
            query_type=None):
        api_request = APIRequest('ListLiveRecordVideo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "AppName": app_name,
            "PageNo": page_no,
            "PageSize": page_size,
            "SortBy": sort_by,
            "StreamName": stream_name,
            "QueryType": query_type}
        return self._handle_request(api_request).result

    def create_audit(self, audit_content=None):
        api_request = APIRequest('CreateAudit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AuditContent": audit_content}
        return self._handle_request(api_request).result

    def get_audit_history(self, page_no=None, page_size=None, video_id=None, sort_by=None):
        api_request = APIRequest('GetAuditHistory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageNo": page_no,
            "PageSize": page_size,
            "VideoId": video_id,
            "SortBy": sort_by}
        return self._handle_request(api_request).result

    def list_ai_job(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            job_ids=None,
            owner_id=None):
        api_request = APIRequest('ListAIJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "JobIds": job_ids,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_ai_job(
            self,
            user_data=None,
            input=None,
            resource_owner_id=None,
            types=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            media_id=None,
            config=None):
        api_request = APIRequest('SubmitAIJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserData": user_data,
            "Input": input,
            "ResourceOwnerId": resource_owner_id,
            "Types": types,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "MediaId": media_id,
            "Config": config}
        return self._handle_request(api_request).result

    def get_image_info(
            self,
            resource_owner_id=None,
            image_id=None,
            resource_owner_account=None,
            output_type=None,
            owner_id=None,
            auth_timeout=None):
        api_request = APIRequest('GetImageInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImageId": image_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OutputType": output_type,
            "OwnerId": owner_id,
            "AuthTimeout": auth_timeout}
        return self._handle_request(api_request).result

    def delete_stream(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            video_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "VideoId": video_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_snapshot_job(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            count=None,
            video_id=None,
            owner_id=None,
            user_data=None,
            specified_offset_time=None,
            width=None,
            interval=None,
            sprite_snapshot_config=None,
            snapshot_template_id=None,
            height=None):
        api_request = APIRequest('SubmitSnapshotJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Count": count,
            "VideoId": video_id,
            "OwnerId": owner_id,
            "UserData": user_data,
            "SpecifiedOffsetTime": specified_offset_time,
            "Width": width,
            "Interval": interval,
            "SpriteSnapshotConfig": sprite_snapshot_config,
            "SnapshotTemplateId": snapshot_template_id,
            "Height": height}
        return self._handle_request(api_request).result

    def update_editing_project(
            self,
            cover_url=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            timeline=None,
            description=None,
            owner_id=None,
            title=None,
            project_id=None):
        api_request = APIRequest('UpdateEditingProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CoverURL": cover_url,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Timeline": timeline,
            "Description": description,
            "OwnerId": owner_id,
            "Title": title,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def set_editing_project_materials(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            material_ids=None,
            owner_id=None,
            project_id=None):
        api_request = APIRequest('SetEditingProjectMaterials', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "MaterialIds": material_ids,
            "OwnerId": owner_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def search_editing_project(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            title=None,
            page_no=None,
            page_size=None,
            sort_by=None,
            status=None):
        api_request = APIRequest('SearchEditingProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "Title": title,
            "PageNo": page_no,
            "PageSize": page_size,
            "SortBy": sort_by,
            "Status": status}
        return self._handle_request(api_request).result

    def produce_editing_project_video(
            self,
            resource_owner_id=None,
            media_metadata=None,
            resource_owner_account=None,
            description=None,
            owner_id=None,
            title=None,
            cover_url=None,
            user_data=None,
            timeline=None,
            produce_config=None,
            project_id=None):
        api_request = APIRequest('ProduceEditingProjectVideo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "MediaMetadata": media_metadata,
            "ResourceOwnerAccount": resource_owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "Title": title,
            "CoverURL": cover_url,
            "UserData": user_data,
            "Timeline": timeline,
            "ProduceConfig": produce_config,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def get_editing_project_materials(
            self,
            resource_owner_id=None,
            material_type=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            type_=None,
            project_id=None):
        api_request = APIRequest('GetEditingProjectMaterials', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "MaterialType": material_type,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Type": type_,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def get_editing_project(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            project_id=None):
        api_request = APIRequest('GetEditingProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ProjectId": project_id}
        return self._handle_request(api_request).result

    def delete_editing_project(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            project_ids=None,
            owner_id=None):
        api_request = APIRequest('DeleteEditingProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ProjectIds": project_ids,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_editing_project(
            self,
            cover_url=None,
            division=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            timeline=None,
            owner_id=None,
            title=None):
        api_request = APIRequest('AddEditingProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CoverURL": cover_url,
            "Division": division,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "Timeline": timeline,
            "OwnerId": owner_id,
            "Title": title}
        return self._handle_request(api_request).result

    def get_mezzanine_info(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            video_id=None,
            preview_segment=None,
            output_type=None,
            addition_type=None,
            owner_id=None,
            auth_timeout=None):
        api_request = APIRequest('GetMezzanineInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "VideoId": video_id,
            "PreviewSegment": preview_segment,
            "OutputType": output_type,
            "AdditionType": addition_type,
            "OwnerId": owner_id,
            "AuthTimeout": auth_timeout}
        return self._handle_request(api_request).result

    def update_category(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cate_id=None,
            owner_id=None,
            cate_name=None):
        api_request = APIRequest('UpdateCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CateId": cate_id,
            "OwnerId": owner_id,
            "CateName": cate_name}
        return self._handle_request(api_request).result

    def get_categories(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cate_id=None,
            page_no=None,
            page_size=None,
            sort_by=None,
            owner_id=None,
            type_=None):
        api_request = APIRequest('GetCategories', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CateId": cate_id,
            "PageNo": page_no,
            "PageSize": page_size,
            "SortBy": sort_by,
            "OwnerId": owner_id,
            "Type": type_}
        return self._handle_request(api_request).result

    def delete_category(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cate_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CateId": cate_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_category(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            type_=None,
            parent_id=None,
            cate_name=None):
        api_request = APIRequest('AddCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "Type": type_,
            "ParentId": parent_id,
            "CateName": cate_name}
        return self._handle_request(api_request).result

    def get_play_info(
            self,
            resource_owner_id=None,
            stream_type=None,
            formats=None,
            resource_owner_account=None,
            channel=None,
            video_id=None,
            player_version=None,
            owner_id=None,
            result_type=None,
            rand=None,
            re_auth_info=None,
            play_config=None,
            output_type=None,
            definition=None,
            auth_timeout=None,
            auth_info=None):
        api_request = APIRequest('GetPlayInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "StreamType": stream_type,
            "Formats": formats,
            "ResourceOwnerAccount": resource_owner_account,
            "Channel": channel,
            "VideoId": video_id,
            "PlayerVersion": player_version,
            "OwnerId": owner_id,
            "ResultType": result_type,
            "Rand": rand,
            "ReAuthInfo": re_auth_info,
            "PlayConfig": play_config,
            "OutputType": output_type,
            "Definition": definition,
            "AuthTimeout": auth_timeout,
            "AuthInfo": auth_info}
        return self._handle_request(api_request).result

    def create_upload_image(
            self,
            resource_owner_id=None,
            image_type=None,
            resource_owner_account=None,
            image_ext=None,
            description=None,
            owner_id=None,
            title=None,
            tags=None,
            storage_location=None,
            user_data=None,
            original_file_name=None,
            cate_id=None,
            app_id=None):
        api_request = APIRequest('CreateUploadImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImageType": image_type,
            "ResourceOwnerAccount": resource_owner_account,
            "ImageExt": image_ext,
            "Description": description,
            "OwnerId": owner_id,
            "Title": title,
            "Tags": tags,
            "StorageLocation": storage_location,
            "UserData": user_data,
            "OriginalFileName": original_file_name,
            "CateId": cate_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def set_message_callback(
            self,
            auth_key=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            event_type_list=None,
            mns_queue_name=None,
            resource_real_owner_id=None,
            owner_id=None,
            callback_type=None,
            callback_switch=None,
            mns_endpoint=None,
            app_id=None,
            auth_switch=None,
            callback_url=None):
        api_request = APIRequest('SetMessageCallback', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AuthKey": auth_key,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EventTypeList": event_type_list,
            "MnsQueueName": mns_queue_name,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id,
            "CallbackType": callback_type,
            "CallbackSwitch": callback_switch,
            "MnsEndpoint": mns_endpoint,
            "AppId": app_id,
            "AuthSwitch": auth_switch,
            "CallbackURL": callback_url}
        return self._handle_request(api_request).result

    def get_message_callback(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            app_id=None,
            resource_real_owner_id=None,
            owner_id=None):
        api_request = APIRequest('GetMessageCallback', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AppId": app_id,
            "ResourceRealOwnerId": resource_real_owner_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_video_info(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            description=None,
            video_id=None,
            owner_id=None,
            title=None,
            tags=None,
            cover_url=None,
            download_switch=None,
            cate_id=None,
            custom_media_info=None,
            status=None):
        api_request = APIRequest('UpdateVideoInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Description": description,
            "VideoId": video_id,
            "OwnerId": owner_id,
            "Title": title,
            "Tags": tags,
            "CoverURL": cover_url,
            "DownloadSwitch": download_switch,
            "CateId": cate_id,
            "CustomMediaInfo": custom_media_info,
            "Status": status}
        return self._handle_request(api_request).result

    def get_video_play_auth(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            re_auth_info=None,
            play_config=None,
            auth_info_timeout=None,
            video_id=None,
            owner_id=None):
        api_request = APIRequest('GetVideoPlayAuth', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ReAuthInfo": re_auth_info,
            "PlayConfig": play_config,
            "AuthInfoTimeout": auth_info_timeout,
            "VideoId": video_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_video_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cate_id=None,
            page_no=None,
            page_size=None,
            end_time=None,
            sort_by=None,
            start_time=None,
            owner_id=None,
            status=None,
            storage_location=None):
        api_request = APIRequest('GetVideoList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CateId": cate_id,
            "PageNo": page_no,
            "PageSize": page_size,
            "EndTime": end_time,
            "SortBy": sort_by,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "Status": status,
            "StorageLocation": storage_location}
        return self._handle_request(api_request).result

    def get_video_info(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            video_id=None,
            addition_type=None,
            result_types=None,
            owner_id=None):
        api_request = APIRequest('GetVideoInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "VideoId": video_id,
            "AdditionType": addition_type,
            "ResultTypes": result_types,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_video(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            video_ids=None):
        api_request = APIRequest('DeleteVideo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "VideoIds": video_ids}
        return self._handle_request(api_request).result

    def refresh_upload_video(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            video_id=None,
            owner_id=None):
        api_request = APIRequest('RefreshUploadVideo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "VideoId": video_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_upload_video(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            transcode_mode=None,
            ip=None,
            description=None,
            file_size=None,
            owner_id=None,
            title=None,
            tags=None,
            storage_location=None,
            cover_url=None,
            user_data=None,
            file_name=None,
            template_group_id=None,
            cate_id=None,
            app_id=None,
            workflow_id=None,
            custom_media_info=None):
        api_request = APIRequest('CreateUploadVideo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "TranscodeMode": transcode_mode,
            "IP": ip,
            "Description": description,
            "FileSize": file_size,
            "OwnerId": owner_id,
            "Title": title,
            "Tags": tags,
            "StorageLocation": storage_location,
            "CoverURL": cover_url,
            "UserData": user_data,
            "FileName": file_name,
            "TemplateGroupId": template_group_id,
            "CateId": cate_id,
            "AppId": app_id,
            "WorkflowId": workflow_id,
            "CustomMediaInfo": custom_media_info}
        return self._handle_request(api_request).result
