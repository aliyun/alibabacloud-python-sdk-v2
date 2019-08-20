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


class MtsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Mts'
        self.api_version = '2014-06-18'
        self.location_service_code = 'mts'
        self.location_endpoint_type = 'openAPI'

    def describe_mts_user_resource_package(self, security_token=None, owner_id=None):
        api_request = APIRequest('DescribeMtsUserResourcePackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_beautify_jobs(
            self,
            beautify_config=None,
            user_data=None,
            async_=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitBeautifyJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BeautifyConfig": beautify_config,
            "UserData": user_data,
            "Async": async_,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def query_media_censor_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            next_page_token=None,
            owner_account=None,
            start_of_job_created_time_range=None,
            maximum_page_size=None,
            owner_id=None,
            pipeline_id=None,
            job_id=None,
            state=None,
            end_of_job_created_time_range=None):
        api_request = APIRequest('QueryMediaCensorJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "NextPageToken": next_page_token,
            "OwnerAccount": owner_account,
            "StartOfJobCreatedTimeRange": start_of_job_created_time_range,
            "MaximumPageSize": maximum_page_size,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id,
            "JobId": job_id,
            "State": state,
            "EndOfJobCreatedTimeRange": end_of_job_created_time_range}
        return self._handle_request(api_request).result

    def submit_fp_compare_job(
            self,
            matched_frame_storage=None,
            user_data=None,
            resource_owner_id=None,
            query_media=None,
            fp_db_id=None,
            resource_owner_account=None,
            master_media=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitFpCompareJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MatchedFrameStorage": matched_frame_storage,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "QueryMedia": query_media,
            "FpDBId": fp_db_id,
            "ResourceOwnerAccount": resource_owner_account,
            "MasterMedia": master_media,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def query_fp_compare_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryFpCompareJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_mc_job(
            self,
            user_data=None,
            resource_owner_id=None,
            images=None,
            texts=None,
            resource_owner_account=None,
            owner_account=None,
            video=None,
            owner_id=None,
            censor_config=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitMCJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "Images": images,
            "Texts": texts,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Video": video,
            "OwnerId": owner_id,
            "CensorConfig": censor_config,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def query_mc_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            next_page_token=None,
            start_of_job_created_time_range=None,
            owner_account=None,
            maximum_page_size=None,
            owner_id=None,
            pipeline_id=None,
            job_ids=None,
            state=None,
            end_of_job_created_time_range=None):
        api_request = APIRequest('QueryMCJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "NextPageToken": next_page_token,
            "StartOfJobCreatedTimeRange": start_of_job_created_time_range,
            "OwnerAccount": owner_account,
            "MaximumPageSize": maximum_page_size,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id,
            "JobIds": job_ids,
            "State": state,
            "EndOfJobCreatedTimeRange": end_of_job_created_time_range}
        return self._handle_request(api_request).result

    def update_mc_template(
            self,
            politics=None,
            resource_owner_id=None,
            contraband=None,
            ad=None,
            abuse=None,
            resource_owner_account=None,
            qrcode=None,
            owner_account=None,
            owner_id=None,
            template_id=None,
            porn=None,
            terrorism=None,
            name=None,
            logo=None,
            spam=None,
            live=None):
        api_request = APIRequest('UpdateMCTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Politics": politics,
            "ResourceOwnerId": resource_owner_id,
            "Contraband": contraband,
            "Ad": ad,
            "Abuse": abuse,
            "ResourceOwnerAccount": resource_owner_account,
            "Qrcode": qrcode,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TemplateId": template_id,
            "Porn": porn,
            "Terrorism": terrorism,
            "Name": name,
            "Logo": logo,
            "spam": spam,
            "Live": live}
        return self._handle_request(api_request).result

    def query_mc_template_list(
            self,
            resource_owner_id=None,
            template_ids=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryMCTemplateList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TemplateIds": template_ids,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_mc_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            template_id=None):
        api_request = APIRequest('DeleteMCTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def add_mc_template(
            self,
            politics=None,
            resource_owner_id=None,
            contraband=None,
            ad=None,
            abuse=None,
            resource_owner_account=None,
            qrcode=None,
            owner_account=None,
            owner_id=None,
            porn=None,
            terrorism=None,
            name=None,
            logo=None,
            spam=None,
            live=None):
        api_request = APIRequest('AddMCTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Politics": politics,
            "ResourceOwnerId": resource_owner_id,
            "Contraband": contraband,
            "Ad": ad,
            "Abuse": abuse,
            "ResourceOwnerAccount": resource_owner_account,
            "Qrcode": qrcode,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Porn": porn,
            "Terrorism": terrorism,
            "Name": name,
            "Logo": logo,
            "spam": spam,
            "Live": live}
        return self._handle_request(api_request).result

    def create_mcu_template(
            self,
            template=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CreateMcuTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Template": template,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_mcu_job(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            job_ids=None,
            owner_id=None):
        api_request = APIRequest('DeleteMcuJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "JobIds": job_ids,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_mcu_job(
            self,
            template=None,
            input=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            template_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitMcuJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Template": template,
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TemplateId": template_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def update_mcu_template(
            self,
            template=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            template_id=None):
        api_request = APIRequest('UpdateMcuTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Template": template,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def query_mcu_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            template_id=None):
        api_request = APIRequest('QueryMcuTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def query_mcu_job(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            job_ids=None,
            owner_id=None):
        api_request = APIRequest('QueryMcuJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "JobIds": job_ids,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_mcu_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            template_id=None):
        api_request = APIRequest('DeleteMcuTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def query_media_fp_delete_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryMediaFpDeleteJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_media_fp_delete_job(
            self,
            user_data=None,
            resource_owner_id=None,
            fp_db_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None,
            primary_key=None):
        api_request = APIRequest('SubmitMediaFpDeleteJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "FpDBId": fp_db_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id,
            "PrimaryKey": primary_key}
        return self._handle_request(api_request).result

    def query_image_search_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryImageSearchJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_image_search_job(
            self,
            input_image=None,
            user_data=None,
            resource_owner_id=None,
            fp_db_id=None,
            resource_owner_account=None,
            input_video=None,
            owner_account=None,
            owner_id=None,
            config=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitImageSearchJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InputImage": input_image,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "FpDBId": fp_db_id,
            "ResourceOwnerAccount": resource_owner_account,
            "InputVideo": input_video,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Config": config,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def query_fp_import_result(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            end_time=None,
            page_index=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('QueryFpImportResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "EndTime": end_time,
            "PageIndex": page_index,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_video_pose_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryVideoPoseJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_video_pose_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            output_config=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitVideoPoseJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "OutputConfig": output_config,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def query_media_censor_job_detail(
            self,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            next_page_token=None,
            owner_account=None,
            maximum_page_size=None,
            owner_id=None):
        api_request = APIRequest('QueryMediaCensorJobDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "NextPageToken": next_page_token,
            "OwnerAccount": owner_account,
            "MaximumPageSize": maximum_page_size,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_media_censor_job(
            self,
            resource_owner_id=None,
            cover_images=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            owner_id=None,
            title=None,
            pipeline_id=None,
            video_censor_config=None,
            input=None,
            user_data=None,
            barrages=None):
        api_request = APIRequest('SubmitMediaCensorJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "CoverImages": cover_images,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "Title": title,
            "PipelineId": pipeline_id,
            "VideoCensorConfig": video_censor_config,
            "Input": input,
            "UserData": user_data,
            "Barrages": barrages}
        return self._handle_request(api_request).result

    def query_complex_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryComplexJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_complex_job(
            self,
            resource_owner_id=None,
            transcode_output=None,
            resource_owner_account=None,
            inputs=None,
            owner_account=None,
            output_location=None,
            owner_id=None,
            pipeline_id=None,
            output_bucket=None,
            user_data=None,
            complex_configs=None):
        api_request = APIRequest('SubmitComplexJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TranscodeOutput": transcode_output,
            "ResourceOwnerAccount": resource_owner_account,
            "Inputs": inputs,
            "OwnerAccount": owner_account,
            "OutputLocation": output_location,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id,
            "OutputBucket": output_bucket,
            "UserData": user_data,
            "ComplexConfigs": complex_configs}
        return self._handle_request(api_request).result

    def query_subtitle_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QuerySubtitleJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_subtitle_job(
            self,
            user_data=None,
            resource_owner_id=None,
            output_config=None,
            input_config=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitSubtitleJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "OutputConfig": output_config,
            "InputConfig": input_config,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def physical_delete_resource(
            self,
            country=None,
            hid=None,
            success=None,
            interrupt=None,
            gmt_wakeup=None,
            pk=None,
            invoker=None,
            bid=None,
            message=None,
            task_extra_data=None,
            task_identifier=None):
        api_request = APIRequest('PhysicalDeleteResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "Hid": hid,
            "Success": success,
            "Interrupt": interrupt,
            "GmtWakeup": gmt_wakeup,
            "Pk": pk,
            "Invoker": invoker,
            "Bid": bid,
            "Message": message,
            "TaskExtraData": task_extra_data,
            "TaskIdentifier": task_identifier}
        return self._handle_request(api_request).result

    def logical_delete_resource(
            self,
            country=None,
            hid=None,
            success=None,
            interrupt=None,
            gmt_wakeup=None,
            pk=None,
            invoker=None,
            bid=None,
            message=None,
            task_extra_data=None,
            task_identifier=None):
        api_request = APIRequest('LogicalDeleteResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "Hid": hid,
            "Success": success,
            "Interrupt": interrupt,
            "GmtWakeup": gmt_wakeup,
            "Pk": pk,
            "Invoker": invoker,
            "Bid": bid,
            "Message": message,
            "TaskExtraData": task_extra_data,
            "TaskIdentifier": task_identifier}
        return self._handle_request(api_request).result

    def check_resource(
            self,
            country=None,
            hid=None,
            level=None,
            invoker=None,
            message=None,
            url=None,
            success=None,
            interrupt=None,
            gmt_wakeup=None,
            pk=None,
            bid=None,
            prompt=None,
            task_extra_data=None,
            task_identifier=None):
        api_request = APIRequest('CheckResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "Hid": hid,
            "Level": level,
            "Invoker": invoker,
            "Message": message,
            "Url": url,
            "Success": success,
            "Interrupt": interrupt,
            "GmtWakeup": gmt_wakeup,
            "Pk": pk,
            "Bid": bid,
            "Prompt": prompt,
            "TaskExtraData": task_extra_data,
            "TaskIdentifier": task_identifier}
        return self._handle_request(api_request).result

    def submit_image_quality_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitImageQualityJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def submit_video_gif_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            video_gif_config=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitVideoGifJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "VideoGifConfig": video_gif_config,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def query_video_gif_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryVideoGifJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_media_workflow_trigger_mode(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            media_workflow_id=None,
            owner_id=None,
            trigger_mode=None):
        api_request = APIRequest('UpdateMediaWorkflowTriggerMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "MediaWorkflowId": media_workflow_id,
            "OwnerId": owner_id,
            "TriggerMode": trigger_mode}
        return self._handle_request(api_request).result

    def create_session(
            self,
            resource_owner_id=None,
            session_time=None,
            resource_owner_account=None,
            owner_account=None,
            end_user_id=None,
            owner_id=None,
            media_id=None):
        api_request = APIRequest('CreateSession', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SessionTime": session_time,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndUserId": end_user_id,
            "OwnerId": owner_id,
            "MediaId": media_id}
        return self._handle_request(api_request).result

    def get_license(
            self,
            resource_owner_id=None,
            data=None,
            resource_owner_account=None,
            owner_account=None,
            header=None,
            owner_id=None,
            media_id=None,
            type_=None,
            license_url=None):
        api_request = APIRequest('GetLicense', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Data": data,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Header": header,
            "OwnerId": owner_id,
            "MediaId": media_id,
            "Type": type_,
            "LicenseUrl": license_url}
        return self._handle_request(api_request).result

    def get_package(
            self,
            resource_owner_id=None,
            data=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('GetPackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Data": data,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_fp_shot_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            next_page_token=None,
            start_of_job_created_time_range=None,
            owner_account=None,
            maximum_page_size=None,
            owner_id=None,
            pipeline_id=None,
            primary_key_list=None,
            job_ids=None,
            state=None,
            end_of_job_created_time_range=None):
        api_request = APIRequest('QueryFpShotJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "NextPageToken": next_page_token,
            "StartOfJobCreatedTimeRange": start_of_job_created_time_range,
            "OwnerAccount": owner_account,
            "MaximumPageSize": maximum_page_size,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id,
            "PrimaryKeyList": primary_key_list,
            "JobIds": job_ids,
            "State": state,
            "EndOfJobCreatedTimeRange": end_of_job_created_time_range}
        return self._handle_request(api_request).result

    def report_fp_shot_job_result(
            self,
            result=None,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            details=None,
            owner_id=None):
        api_request = APIRequest('ReportFpShotJobResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Result": result,
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Details": details,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_fp_shot_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            fp_shot_config=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitFpShotJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "FpShotConfig": fp_shot_config,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def register_media_detail_person(
            self,
            resource_owner_id=None,
            images=None,
            resource_owner_account=None,
            owner_account=None,
            person_lib=None,
            owner_id=None,
            category=None,
            person_name=None):
        api_request = APIRequest('RegisterMediaDetailPerson', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Images": images,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PersonLib": person_lib,
            "OwnerId": owner_id,
            "Category": category,
            "PersonName": person_name}
        return self._handle_request(api_request).result

    def report_video_split_job_result(
            self,
            result=None,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            details=None,
            owner_id=None):
        api_request = APIRequest('ReportVideoSplitJobResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Result": result,
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Details": details,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_video_split_job(
            self,
            input=None,
            video_split_config=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitVideoSplitJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "VideoSplitConfig": video_split_config,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def query_video_split_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryVideoSplitJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def register_media_detail_scenario(
            self,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            scenario=None,
            owner_account=None,
            description=None,
            owner_id=None):
        api_request = APIRequest('RegisterMediaDetailScenario', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Scenario": scenario,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_media_detail_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryMediaDetailJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_media_detail_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            media_detail_config=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitMediaDetailJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "MediaDetailConfig": media_detail_config,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def report_media_detail_job_result(
            self,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            tag=None,
            owner_id=None,
            results=None):
        api_request = APIRequest('ReportMediaDetailJobResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Tag": tag,
            "OwnerId": owner_id,
            "Results": results}
        return self._handle_request(api_request).result

    def submit_facerecog_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            facerecog_config=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitFacerecogJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FacerecogConfig": facerecog_config,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def submit_annotation_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            annotation_config=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitAnnotationJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AnnotationConfig": annotation_config,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def report_facerecog_job_result(
            self,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            facerecog=None,
            owner_account=None,
            details=None,
            owner_id=None):
        api_request = APIRequest('ReportFacerecogJobResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Facerecog": facerecog,
            "OwnerAccount": owner_account,
            "Details": details,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def report_annotation_job_result(
            self,
            annotation=None,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            details=None,
            owner_id=None):
        api_request = APIRequest('ReportAnnotationJobResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Annotation": annotation,
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Details": details,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_facerecog_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            facerecog_job_ids=None,
            owner_id=None):
        api_request = APIRequest('QueryFacerecogJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "FacerecogJobIds": facerecog_job_ids,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_annotation_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            annotation_job_ids=None):
        api_request = APIRequest('QueryAnnotationJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AnnotationJobIds": annotation_job_ids}
        return self._handle_request(api_request).result

    def update_terrorism_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            state=None,
            notify_config=None,
            owner_id=None,
            priority=None,
            pipeline_id=None):
        api_request = APIRequest('UpdateTerrorismPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "State": state,
            "NotifyConfig": notify_config,
            "OwnerId": owner_id,
            "Priority": priority,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def update_censor_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            state=None,
            notify_config=None,
            owner_id=None,
            priority=None,
            pipeline_id=None):
        api_request = APIRequest('UpdateCensorPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "State": state,
            "NotifyConfig": notify_config,
            "OwnerId": owner_id,
            "Priority": priority,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def submit_terrorism_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None,
            terrorism_config=None):
        api_request = APIRequest('SubmitTerrorismJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id,
            "TerrorismConfig": terrorism_config}
        return self._handle_request(api_request).result

    def report_terrorism_job_result(
            self,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            label=None,
            detail=None,
            owner_id=None):
        api_request = APIRequest('ReportTerrorismJobResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Label": label,
            "Detail": detail,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def report_censor_job_result(
            self,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            label=None,
            detail=None,
            owner_id=None):
        api_request = APIRequest('ReportCensorJobResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Label": label,
            "Detail": detail,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_terrorism_pipeline_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            pipeline_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryTerrorismPipelineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PipelineIds": pipeline_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_censor_pipeline_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            pipeline_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryCensorPipelineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PipelineIds": pipeline_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_terrorism_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryTerrorismJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_censor_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryCensorJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def list_terrorism_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            state=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('ListTerrorismPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "State": state,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_censor_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            state=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('ListCensorPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "State": state,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def add_terrorism_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            notify_config=None,
            owner_id=None,
            priority=None):
        api_request = APIRequest('AddTerrorismPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "NotifyConfig": notify_config,
            "OwnerId": owner_id,
            "Priority": priority}
        return self._handle_request(api_request).result

    def add_censor_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            notify_config=None,
            owner_id=None,
            priority=None):
        api_request = APIRequest('AddCensorPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "NotifyConfig": notify_config,
            "OwnerId": owner_id,
            "Priority": priority}
        return self._handle_request(api_request).result

    def report_tag_job_result(
            self,
            result=None,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            tag=None,
            owner_id=None):
        api_request = APIRequest('ReportTagJobResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Result": result,
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Tag": tag,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_tag_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            tag_job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryTagJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "TagJobIds": tag_job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_tag_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            tag_config=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitTagJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "TagConfig": tag_config,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def submit_video_summary_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            video_summary_config=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitVideoSummaryJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "VideoSummaryConfig": video_summary_config,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def query_video_summary_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryVideoSummaryJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_editing_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryEditingJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def submit_editing_jobs(
            self,
            output_bucket=None,
            resource_owner_id=None,
            editing_job_outputs=None,
            resource_owner_account=None,
            owner_account=None,
            output_location=None,
            owner_id=None,
            editing_inputs=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitEditingJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OutputBucket": output_bucket,
            "ResourceOwnerId": resource_owner_id,
            "EditingJobOutputs": editing_job_outputs,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OutputLocation": output_location,
            "OwnerId": owner_id,
            "EditingInputs": editing_inputs,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def update_cover_pipeline(
            self,
            resource_owner_id=None,
            role=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            state=None,
            notify_config=None,
            owner_id=None,
            priority=None,
            pipeline_id=None):
        api_request = APIRequest('UpdateCoverPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Role": role,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "State": state,
            "NotifyConfig": notify_config,
            "OwnerId": owner_id,
            "Priority": priority,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def submit_cover_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            cover_config=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitCoverJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "CoverConfig": cover_config,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def report_cover_job_result(
            self,
            result=None,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ReportCoverJobResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Result": result,
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_cover_pipeline_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            pipeline_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryCoverPipelineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PipelineIds": pipeline_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_cover_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            next_page_token=None,
            start_of_job_created_time_range=None,
            owner_account=None,
            maximum_page_size=None,
            owner_id=None,
            cover_job_ids=None,
            pipeline_id=None,
            state=None,
            end_of_job_created_time_range=None):
        api_request = APIRequest('QueryCoverJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "NextPageToken": next_page_token,
            "StartOfJobCreatedTimeRange": start_of_job_created_time_range,
            "OwnerAccount": owner_account,
            "MaximumPageSize": maximum_page_size,
            "OwnerId": owner_id,
            "CoverJobIds": cover_job_ids,
            "PipelineId": pipeline_id,
            "State": state,
            "EndOfJobCreatedTimeRange": end_of_job_created_time_range}
        return self._handle_request(api_request).result

    def list_cover_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            state=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('ListCoverPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "State": state,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def add_cover_pipeline(
            self,
            resource_owner_id=None,
            role=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            notify_config=None,
            owner_id=None,
            priority=None):
        api_request = APIRequest('AddCoverPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Role": role,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "NotifyConfig": notify_config,
            "OwnerId": owner_id,
            "Priority": priority}
        return self._handle_request(api_request).result

    def update_asr_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            state=None,
            notify_config=None,
            owner_id=None,
            priority=None,
            pipeline_id=None):
        api_request = APIRequest('UpdateAsrPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "State": state,
            "NotifyConfig": notify_config,
            "OwnerId": owner_id,
            "Priority": priority,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def submit_asr_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            asr_config=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitAsrJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AsrConfig": asr_config,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def query_asr_pipeline_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            pipeline_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryAsrPipelineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PipelineIds": pipeline_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_asr_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryAsrJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def list_asr_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            state=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('ListAsrPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "State": state,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def add_asr_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            notify_config=None,
            owner_id=None,
            priority=None):
        api_request = APIRequest('AddAsrPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "NotifyConfig": notify_config,
            "OwnerId": owner_id,
            "Priority": priority}
        return self._handle_request(api_request).result

    def update_porn_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            state=None,
            notify_config=None,
            owner_id=None,
            priority=None,
            pipeline_id=None):
        api_request = APIRequest('UpdatePornPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "State": state,
            "NotifyConfig": notify_config,
            "OwnerId": owner_id,
            "Priority": priority,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def submit_porn_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            porn_config=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitPornJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PornConfig": porn_config,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def report_porn_job_result(
            self,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            label=None,
            detail=None,
            owner_id=None):
        api_request = APIRequest('ReportPornJobResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Label": label,
            "Detail": detail,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_porn_pipeline_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            pipeline_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryPornPipelineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PipelineIds": pipeline_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_porn_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryPornJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def list_porn_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            state=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('ListPornPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "State": state,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def add_porn_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            notify_config=None,
            owner_id=None,
            priority=None):
        api_request = APIRequest('AddPornPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "NotifyConfig": notify_config,
            "OwnerId": owner_id,
            "Priority": priority}
        return self._handle_request(api_request).result

    def unbind_output_bucket(
            self,
            bucket=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('UnbindOutputBucket', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Bucket": bucket,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def unbind_input_bucket(
            self,
            bucket=None,
            resource_owner_id=None,
            resource_owner_account=None,
            role_arn=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('UnbindInputBucket', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Bucket": bucket,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RoleArn": role_arn,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def list_media(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            next_page_token=None,
            owner_account=None,
            maximum_page_size=None,
            from_=None,
            to=None,
            owner_id=None):
        api_request = APIRequest('ListMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "NextPageToken": next_page_token,
            "OwnerAccount": owner_account,
            "MaximumPageSize": maximum_page_size,
            "From": from_,
            "To": to,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def refresh_cdn_domain_configs_cache(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            domains=None,
            owner_id=None):
        api_request = APIRequest('RefreshCdnDomainConfigsCache', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Domains": domains,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_auth_config(
            self,
            key1=None,
            key2=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('SetAuthConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Key1": key1,
            "Key2": key2,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_auth_config(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryAuthConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def play_info(
            self,
            play_domain=None,
            resource_owner_id=None,
            formats=None,
            resource_owner_account=None,
            owner_account=None,
            hls_uri_token=None,
            terminal=None,
            owner_id=None,
            media_id=None,
            rand=None,
            auth_timeout=None,
            auth_info=None):
        api_request = APIRequest('PlayInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PlayDomain": play_domain,
            "ResourceOwnerId": resource_owner_id,
            "Formats": formats,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "HlsUriToken": hls_uri_token,
            "Terminal": terminal,
            "OwnerId": owner_id,
            "MediaId": media_id,
            "Rand": rand,
            "AuthTimeout": auth_timeout,
            "AuthInfo": auth_info}
        return self._handle_request(api_request).result

    def decrypt_key(
            self,
            rand=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            ciphertext_blob=None):
        api_request = APIRequest('DecryptKey', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Rand": rand,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "CiphertextBlob": ciphertext_blob}
        return self._handle_request(api_request).result

    def update_media_publish_state(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            publish=None,
            owner_account=None,
            owner_id=None,
            media_id=None):
        api_request = APIRequest('UpdateMediaPublishState', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Publish": publish,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "MediaId": media_id}
        return self._handle_request(api_request).result

    def update_media_cover(
            self,
            cover_url=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            media_id=None):
        api_request = APIRequest('UpdateMediaCover', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CoverURL": cover_url,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "MediaId": media_id}
        return self._handle_request(api_request).result

    def update_media_category(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cate_id=None,
            owner_account=None,
            owner_id=None,
            media_id=None):
        api_request = APIRequest('UpdateMediaCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CateId": cate_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "MediaId": media_id}
        return self._handle_request(api_request).result

    def update_media(
            self,
            cover_url=None,
            resource_owner_id=None,
            resource_owner_account=None,
            cate_id=None,
            owner_account=None,
            description=None,
            owner_id=None,
            media_id=None,
            title=None,
            tags=None):
        api_request = APIRequest('UpdateMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CoverURL": cover_url,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CateId": cate_id,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "MediaId": media_id,
            "Title": title,
            "Tags": tags}
        return self._handle_request(api_request).result

    def update_category_name(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cate_id=None,
            owner_account=None,
            owner_id=None,
            cate_name=None):
        api_request = APIRequest('UpdateCategoryName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CateId": cate_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "CateName": cate_name}
        return self._handle_request(api_request).result

    def query_media_list_by_url(
            self,
            resource_owner_id=None,
            include_summary_list=None,
            resource_owner_account=None,
            include_snapshot_list=None,
            file_ur_ls=None,
            owner_account=None,
            owner_id=None,
            include_play_list=None,
            include_media_info=None):
        api_request = APIRequest('QueryMediaListByURL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "IncludeSummaryList": include_summary_list,
            "ResourceOwnerAccount": resource_owner_account,
            "IncludeSnapshotList": include_snapshot_list,
            "FileURLs": file_ur_ls,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "IncludePlayList": include_play_list,
            "IncludeMediaInfo": include_media_info}
        return self._handle_request(api_request).result

    def list_all_media_bucket(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            next_page_token=None,
            owner_account=None,
            maximum_page_size=None,
            owner_id=None):
        api_request = APIRequest('ListAllMediaBucket', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "NextPageToken": next_page_token,
            "OwnerAccount": owner_account,
            "MaximumPageSize": maximum_page_size,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def list_all_category(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ListAllCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_media_tag(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            tag=None,
            owner_id=None,
            media_id=None):
        api_request = APIRequest('DeleteMediaTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Tag": tag,
            "OwnerId": owner_id,
            "MediaId": media_id}
        return self._handle_request(api_request).result

    def delete_category(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            cate_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CateId": cate_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def category_tree(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CategoryTree', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def bind_output_bucket(
            self,
            bucket=None,
            resource_owner_id=None,
            resource_owner_account=None,
            role_arn=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('BindOutputBucket', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Bucket": bucket,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RoleArn": role_arn,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def bind_input_bucket(
            self,
            bucket=None,
            resource_owner_id=None,
            resource_owner_account=None,
            role_arn=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('BindInputBucket', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Bucket": bucket,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RoleArn": role_arn,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_media_tag(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            tag=None,
            owner_id=None,
            media_id=None):
        api_request = APIRequest('AddMediaTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Tag": tag,
            "OwnerId": owner_id,
            "MediaId": media_id}
        return self._handle_request(api_request).result

    def add_media(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            override_params=None,
            owner_id=None,
            title=None,
            input_unbind=None,
            tags=None,
            cover_url=None,
            cate_id=None,
            file_url=None,
            media_workflow_id=None,
            media_workflow_user_data=None):
        api_request = APIRequest('AddMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "OverrideParams": override_params,
            "OwnerId": owner_id,
            "Title": title,
            "InputUnbind": input_unbind,
            "Tags": tags,
            "CoverURL": cover_url,
            "CateId": cate_id,
            "FileURL": file_url,
            "MediaWorkflowId": media_workflow_id,
            "MediaWorkflowUserData": media_workflow_user_data}
        return self._handle_request(api_request).result

    def add_category(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            parent_id=None,
            cate_name=None):
        api_request = APIRequest('AddCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ParentId": parent_id,
            "CateName": cate_name}
        return self._handle_request(api_request).result

    def list_job(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            next_page_token=None,
            start_of_job_created_time_range=None,
            owner_account=None,
            maximum_page_size=None,
            state=None,
            owner_id=None,
            end_of_job_created_time_range=None,
            pipeline_id=None):
        api_request = APIRequest('ListJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "NextPageToken": next_page_token,
            "StartOfJobCreatedTimeRange": start_of_job_created_time_range,
            "OwnerAccount": owner_account,
            "MaximumPageSize": maximum_page_size,
            "State": state,
            "OwnerId": owner_id,
            "EndOfJobCreatedTimeRange": end_of_job_created_time_range,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def update_media_workflow(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            topology=None,
            owner_account=None,
            media_workflow_id=None,
            owner_id=None):
        api_request = APIRequest('UpdateMediaWorkflow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Topology": topology,
            "OwnerAccount": owner_account,
            "MediaWorkflowId": media_workflow_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def search_media_workflow(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            state_list=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('SearchMediaWorkflow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "StateList": state_list,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def search_media(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            owner_id=None,
            title=None,
            page_number=None,
            cate_id=None,
            page_size=None,
            from_=None,
            sort_by=None,
            to=None,
            tag=None,
            key_word=None):
        api_request = APIRequest('SearchMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "Title": title,
            "PageNumber": page_number,
            "CateId": cate_id,
            "PageSize": page_size,
            "From": from_,
            "SortBy": sort_by,
            "To": to,
            "Tag": tag,
            "KeyWord": key_word}
        return self._handle_request(api_request).result

    def query_media_workflow_list(
            self,
            media_workflow_ids=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryMediaWorkflowList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MediaWorkflowIds": media_workflow_ids,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_media_workflow_execution_list(
            self,
            run_ids=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryMediaWorkflowExecutionList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RunIds": run_ids,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_media_list(
            self,
            resource_owner_id=None,
            include_summary_list=None,
            resource_owner_account=None,
            include_snapshot_list=None,
            owner_account=None,
            media_ids=None,
            owner_id=None,
            include_play_list=None,
            include_media_info=None):
        api_request = APIRequest('QueryMediaList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "IncludeSummaryList": include_summary_list,
            "ResourceOwnerAccount": resource_owner_account,
            "IncludeSnapshotList": include_snapshot_list,
            "OwnerAccount": owner_account,
            "MediaIds": media_ids,
            "OwnerId": owner_id,
            "IncludePlayList": include_play_list,
            "IncludeMediaInfo": include_media_info}
        return self._handle_request(api_request).result

    def list_media_workflow_executions(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            input_file_url=None,
            next_page_token=None,
            owner_account=None,
            maximum_page_size=None,
            media_workflow_id=None,
            owner_id=None,
            media_workflow_name=None):
        api_request = APIRequest('ListMediaWorkflowExecutions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "InputFileURL": input_file_url,
            "NextPageToken": next_page_token,
            "OwnerAccount": owner_account,
            "MaximumPageSize": maximum_page_size,
            "MediaWorkflowId": media_workflow_id,
            "OwnerId": owner_id,
            "MediaWorkflowName": media_workflow_name}
        return self._handle_request(api_request).result

    def delete_media_workflow(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            media_workflow_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteMediaWorkflow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "MediaWorkflowId": media_workflow_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_media(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            media_ids=None,
            owner_id=None):
        api_request = APIRequest('DeleteMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "MediaIds": media_ids,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def deactivate_media_workflow(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            media_workflow_id=None,
            owner_id=None):
        api_request = APIRequest('DeactivateMediaWorkflow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "MediaWorkflowId": media_workflow_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_media_workflow(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            topology=None,
            owner_account=None,
            name=None,
            owner_id=None,
            trigger_mode=None):
        api_request = APIRequest('AddMediaWorkflow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Topology": topology,
            "OwnerAccount": owner_account,
            "Name": name,
            "OwnerId": owner_id,
            "TriggerMode": trigger_mode}
        return self._handle_request(api_request).result

    def activate_media_workflow(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            media_workflow_id=None,
            owner_id=None):
        api_request = APIRequest('ActivateMediaWorkflow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "MediaWorkflowId": media_workflow_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_template(
            self,
            container=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            trans_config=None,
            mux_config=None,
            video=None,
            audio=None,
            owner_id=None):
        api_request = APIRequest('AddTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Container": container,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "TransConfig": trans_config,
            "MuxConfig": mux_config,
            "Video": video,
            "Audio": audio,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_pipeline(
            self,
            resource_owner_id=None,
            role=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            notify_config=None,
            owner_id=None,
            speed_level=None,
            speed=None):
        api_request = APIRequest('AddPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Role": role,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "NotifyConfig": notify_config,
            "OwnerId": owner_id,
            "SpeedLevel": speed_level,
            "Speed": speed}
        return self._handle_request(api_request).result

    def query_analysis_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            analysis_job_ids=None):
        api_request = APIRequest('QueryAnalysisJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AnalysisJobIds": analysis_job_ids}
        return self._handle_request(api_request).result

    def player_auth(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('PlayerAuth', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_water_mark_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            water_mark_template_id=None):
        api_request = APIRequest('DeleteWaterMarkTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "WaterMarkTemplateId": water_mark_template_id}
        return self._handle_request(api_request).result

    def delete_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            template_id=None):
        api_request = APIRequest('DeleteTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def delete_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('DeletePipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def cancel_job(
            self,
            job_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CancelJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_water_mark_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            owner_id=None,
            config=None):
        api_request = APIRequest('AddWaterMarkTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "OwnerId": owner_id,
            "Config": config}
        return self._handle_request(api_request).result

    def query_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            job_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "JobIds": job_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_template_list(
            self,
            resource_owner_id=None,
            template_ids=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryTemplateList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TemplateIds": template_ids,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_snapshot_job_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            next_page_token=None,
            snapshot_job_ids=None,
            start_of_job_created_time_range=None,
            owner_account=None,
            maximum_page_size=None,
            owner_id=None,
            pipeline_id=None,
            state=None,
            end_of_job_created_time_range=None):
        api_request = APIRequest('QuerySnapshotJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "NextPageToken": next_page_token,
            "SnapshotJobIds": snapshot_job_ids,
            "StartOfJobCreatedTimeRange": start_of_job_created_time_range,
            "OwnerAccount": owner_account,
            "MaximumPageSize": maximum_page_size,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id,
            "State": state,
            "EndOfJobCreatedTimeRange": end_of_job_created_time_range}
        return self._handle_request(api_request).result

    def query_pipeline_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            pipeline_ids=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryPipelineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PipelineIds": pipeline_ids,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_media_info_job_list(
            self,
            resource_owner_id=None,
            media_info_job_ids=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryMediaInfoJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "MediaInfoJobIds": media_info_job_ids,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def search_pipeline(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            state=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('SearchPipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "State": state,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def query_water_mark_template_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            water_mark_template_ids=None):
        api_request = APIRequest('QueryWaterMarkTemplateList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "WaterMarkTemplateIds": water_mark_template_ids}
        return self._handle_request(api_request).result

    def submit_analysis_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            analysis_config=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            priority=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitAnalysisJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "AnalysisConfig": analysis_config,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Priority": priority,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def search_water_mark_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            state=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('SearchWaterMarkTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "State": state,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def search_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            state=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('SearchTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "State": state,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def update_water_mark_template(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            owner_id=None,
            water_mark_template_id=None,
            config=None):
        api_request = APIRequest('UpdateWaterMarkTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "OwnerId": owner_id,
            "WaterMarkTemplateId": water_mark_template_id,
            "Config": config}
        return self._handle_request(api_request).result

    def update_template(
            self,
            container=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            mux_config=None,
            video=None,
            owner_id=None,
            template_id=None,
            name=None,
            trans_config=None,
            audio=None):
        api_request = APIRequest('UpdateTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Container": container,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "MuxConfig": mux_config,
            "Video": video,
            "OwnerId": owner_id,
            "TemplateId": template_id,
            "Name": name,
            "TransConfig": trans_config,
            "Audio": audio}
        return self._handle_request(api_request).result

    def update_pipeline(
            self,
            resource_owner_id=None,
            role=None,
            resource_owner_account=None,
            owner_account=None,
            name=None,
            state=None,
            notify_config=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('UpdatePipeline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Role": role,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Name": name,
            "State": state,
            "NotifyConfig": notify_config,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def submit_snapshot_job(
            self,
            input=None,
            user_data=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            snapshot_config=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitSnapshotJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "SnapshotConfig": snapshot_config,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def submit_media_info_job(
            self,
            input=None,
            user_data=None,
            async_=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitMediaInfoJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Input": input,
            "UserData": user_data,
            "Async": async_,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def submit_jobs(
            self,
            outputs=None,
            input=None,
            output_bucket=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            output_location=None,
            owner_id=None,
            pipeline_id=None):
        api_request = APIRequest('SubmitJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Outputs": outputs,
            "Input": input,
            "OutputBucket": output_bucket,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OutputLocation": output_location,
            "OwnerId": owner_id,
            "PipelineId": pipeline_id}
        return self._handle_request(api_request).result
