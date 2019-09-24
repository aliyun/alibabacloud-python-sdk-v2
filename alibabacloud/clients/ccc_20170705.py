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


class CCCClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'CCC'
        self.api_version = '2017-07-05'
        self.location_service_code = 'ccc'
        self.location_endpoint_type = 'openAPI'

    def get_turn_server_list(self, instance_id=None):
        api_request = APIRequest('GetTURNServerList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def predictive_record_failure(
            self,
            call_id=None,
            actual_time=None,
            calling_number=None,
            instance_id=None,
            disposition_code=None,
            called_number=None,
            task_id=None,
            cab_instance_id=None,
            cab_instance_owner_id=None):
        api_request = APIRequest('PredictiveRecordFailure', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallId": call_id,
            "ActualTime": actual_time,
            "CallingNumber": calling_number,
            "InstanceId": instance_id,
            "DispositionCode": disposition_code,
            "CalledNumber": called_number,
            "TaskId": task_id,
            "CabInstanceId": cab_instance_id,
            "CabInstanceOwnerId": cab_instance_owner_id}
        return self._handle_request(api_request).result

    def predictive_record_success(
            self,
            call_id=None,
            calling_number=None,
            instance_id=None,
            called_number=None,
            call_type=None,
            scenario_id=None,
            task_id=None,
            cab_instance_id=None,
            cab_instance_owner_id=None):
        api_request = APIRequest('PredictiveRecordSuccess', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallId": call_id,
            "CallingNumber": calling_number,
            "InstanceId": instance_id,
            "CalledNumber": called_number,
            "CallType": call_type,
            "ScenarioId": scenario_id,
            "TaskId": task_id,
            "CabInstanceId": cab_instance_id,
            "CabInstanceOwnerId": cab_instance_owner_id}
        return self._handle_request(api_request).result

    def download_all_type_recording(self, instance_id=None, contact_id=None, channel=None):
        api_request = APIRequest('DownloadAllTypeRecording', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "ContactId": contact_id,
            "Channel": channel}
        return self._handle_request(api_request).result

    def get_turn_credentials(self, instance_id=None, user_name=None):
        api_request = APIRequest('GetTURNCredentials', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "UserName": user_name}
        return self._handle_request(api_request).result

    def modify_cab_instance(
            self,
            max_concurrent_conversation=None,
            instance_id=None,
            instance_name=None,
            call_center_instance_id=None,
            instance_description=None):
        api_request = APIRequest('ModifyCabInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MaxConcurrentConversation": max_concurrent_conversation,
            "InstanceId": instance_id,
            "InstanceName": instance_name,
            "CallCenterInstanceId": call_center_instance_id,
            "InstanceDescription": instance_description}
        return self._handle_request(api_request).result

    def list_agent_devices(self, instance_id=None, ram_ids=None, start_time=None, stop_time=None):
        api_request = APIRequest('ListAgentDevices', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "RamIds": ram_ids,
            "StartTime": start_time,
            "StopTime": stop_time}
        return self._handle_request(api_request).result

    def add_agent_device(
            self,
            instance_id=None,
            client_ip=None,
            remark=None,
            client_port=None,
            browser_version=None):
        api_request = APIRequest('AddAgentDevice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "ClientIp": client_ip,
            "Remark": remark,
            "ClientPort": client_port,
            "BrowserVersion": browser_version}
        return self._handle_request(api_request).result

    def modify_agent_device(self, agent_device_id=None, instance_id=None, is_login=None):
        api_request = APIRequest('ModifyAgentDevice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AgentDeviceId": agent_device_id,
            "InstanceId": instance_id,
            "IsLogin": is_login}
        return self._handle_request(api_request).result

    def create_fault(
            self,
            speaker_list=None,
            agent_id=None,
            agent_oss_file_name=None,
            description=None,
            end_time=None,
            operating_system_version=None,
            start_time=None,
            microphone_list=None,
            speaker_equipment=None,
            service_port=None,
            client_port=None,
            service_ip=None,
            instance_id=None,
            custom_file_path=None,
            client_ip=None,
            agent_file_path=None,
            connect_id=None,
            custom_oss_file_name=None,
            microphone_equipment=None,
            browser_version=None):
        api_request = APIRequest('CreateFault', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SpeakerList": speaker_list,
            "AgentId": agent_id,
            "AgentOssFileName": agent_oss_file_name,
            "Description": description,
            "EndTime": end_time,
            "OperatingSystemVersion": operating_system_version,
            "StartTime": start_time,
            "MicrophoneList": microphone_list,
            "SpeakerEquipment": speaker_equipment,
            "ServicePort": service_port,
            "ClientPort": client_port,
            "ServiceIp": service_ip,
            "InstanceId": instance_id,
            "CustomFilePath": custom_file_path,
            "ClientIp": client_ip,
            "AgentFilePath": agent_file_path,
            "ConnectId": connect_id,
            "CustomOssFileName": custom_oss_file_name,
            "MicrophoneEquipment": microphone_equipment,
            "BrowserVersion": browser_version}
        return self._handle_request(api_request).result

    def get_record_oss_upload_param(self, instance_id=None, file_name=None):
        api_request = APIRequest('GetRecordOssUploadParam', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "FileName": file_name}
        return self._handle_request(api_request).result

    def pick_global_outbound_numbers(
            self,
            is_virtual=None,
            instance_id=None,
            list_of_skill_group_id=None,
            count=None,
            callee_number=None):
        api_request = APIRequest('PickGlobalOutboundNumbers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IsVirtual": is_virtual,
            "InstanceId": instance_id,
            "SkillGroupId": list_of_skill_group_id,
            "Count": count,
            "CalleeNumber": callee_number}
        repeat_info = {"SkillGroupId": ('SkillGroupId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def submit_cab_recording(
            self,
            instance_id=None,
            instance_owner_id=None,
            merged_recording=None,
            task_id=None,
            resource_recording=None):
        api_request = APIRequest('SubmitCabRecording', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "InstanceOwnerId": instance_owner_id,
            "MergedRecording": merged_recording,
            "TaskId": task_id,
            "ResourceRecording": resource_recording}
        return self._handle_request(api_request).result

    def download_cab_recording(self, instance_id=None, task_id=None):
        api_request = APIRequest('DownloadCabRecording', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "TaskId": task_id}
        return self._handle_request(api_request).result

    def list_instances_of_user(self,):
        api_request = APIRequest('ListInstancesOfUser', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def save_web_rtc_stats(
            self,
            call_id=None,
            uid=None,
            record_time=None,
            instance_id=None,
            stats=None,
            call_start_time=None,
            tenant_id=None,
            callee_number=None,
            caller_number=None):
        api_request = APIRequest('SaveWebRTCStats', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallId": call_id,
            "Uid": uid,
            "RecordTime": record_time,
            "InstanceId": instance_id,
            "Stats": stats,
            "CallStartTime": call_start_time,
            "TenantId": tenant_id,
            "CalleeNumber": callee_number,
            "CallerNumber": caller_number}
        return self._handle_request(api_request).result

    def save_stats(
            self,
            call_id=None,
            uid=None,
            record_time=None,
            instance_id=None,
            stats=None,
            call_start_time=None,
            tenant_id=None,
            callee_number=None,
            caller_number=None):
        api_request = APIRequest('SaveStats', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallId": call_id,
            "Uid": uid,
            "RecordTime": record_time,
            "InstanceId": instance_id,
            "Stats": stats,
            "CallStartTime": call_start_time,
            "TenantId": tenant_id,
            "CalleeNumber": callee_number,
            "CallerNumber": caller_number}
        return self._handle_request(api_request).result

    def publish_predictive_job_group(
            self,
            instance_id=None,
            skill_group_id=None,
            job_group_id=None):
        api_request = APIRequest('PublishPredictiveJobGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SkillGroupId": skill_group_id,
            "JobGroupId": job_group_id}
        return self._handle_request(api_request).result

    def get_contact_info_by_outbound_task_id(
            self,
            instance_id=None,
            outbound_task_id=None,
            skill_group_id=None):
        api_request = APIRequest('GetContactInfoByOutboundTaskId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "OutboundTaskId": outbound_task_id,
            "SkillGroupId": skill_group_id}
        return self._handle_request(api_request).result

    def get_job_file_upload_url(self, instance_id=None, file_name=None):
        api_request = APIRequest('GetJobFileUploadUrl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "FileName": file_name}
        return self._handle_request(api_request).result

    def get_jobs_progress(self, instance_id=None, skill_group_id=None, job_group_id=None):
        api_request = APIRequest('GetJobsProgress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SkillGroupId": skill_group_id,
            "JobGroupId": job_group_id}
        return self._handle_request(api_request).result

    def list_predictive_job_groups(
            self,
            instance_id=None,
            criteria=None,
            skill_group_id=None,
            name=None,
            page_size=None,
            end_time=None,
            start_time=None,
            page_number=None):
        api_request = APIRequest('ListPredictiveJobGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Criteria": criteria,
            "SkillGroupId": skill_group_id,
            "Name": name,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def create_predictive_job_group(
            self,
            instance_id=None,
            is_draft=None,
            skill_group_id=None,
            strategy_json=None,
            name=None,
            description=None,
            timing_schedule=None,
            list_of_jobs_json=None,
            job_file_path=None):
        api_request = APIRequest('CreatePredictiveJobGroup', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "IsDraft": is_draft,
            "SkillGroupId": skill_group_id,
            "StrategyJson": strategy_json,
            "Name": name,
            "Description": description,
            "TimingSchedule": timing_schedule,
            "JobsJson": list_of_jobs_json,
            "JobFilePath": job_file_path}
        repeat_info = {"JobsJson": ('JobsJson', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_skill_group_outbound_numbers(
            self,
            instance_id=None,
            list_of_outbound_phone_number_id=None,
            skill_group_id=None,
            operation_type=None):
        api_request = APIRequest('ModifySkillGroupOutboundNumbers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "OutboundPhoneNumberId": list_of_outbound_phone_number_id,
            "SkillGroupId": skill_group_id,
            "OperationType": operation_type}
        repeat_info = {"OutboundPhoneNumberId": ('OutboundPhoneNumberId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_call_event_detail_by_contact_id(self, instance_id=None, contact_id=None):
        api_request = APIRequest('ListCallEventDetailByContactId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "ContactId": contact_id}
        return self._handle_request(api_request).result

    def dial_ex(
            self,
            rout_point=None,
            caller=None,
            instance_id=None,
            provider=None,
            callee=None,
            answer_mode=None):
        api_request = APIRequest('DialEx', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RoutPoint": rout_point,
            "Caller": caller,
            "InstanceId": instance_id,
            "Provider": provider,
            "Callee": callee,
            "AnswerMode": answer_mode}
        return self._handle_request(api_request).result

    def list_voice_appraise(self, instance_id=None):
        api_request = APIRequest('ListVoiceAppraise', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def create_voice_appraise(
            self,
            instance_id=None,
            contact_flow_version_id=None,
            is_appraise=None,
            content=None):
        api_request = APIRequest('CreateVoiceAppraise', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "ContactFlowVersionId": contact_flow_version_id,
            "IsAppraise": is_appraise,
            "Content": content}
        return self._handle_request(api_request).result

    def add_bulk_phone_numbers(
            self,
            contact_flow_id=None,
            instance_id=None,
            usage=None,
            list_of_skill_group_id=None,
            list_of_phone_number=None):
        api_request = APIRequest('AddBulkPhoneNumbers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContactFlowId": contact_flow_id,
            "InstanceId": instance_id,
            "Usage": usage,
            "SkillGroupId": list_of_skill_group_id,
            "PhoneNumber": list_of_phone_number}
        repeat_info = {"SkillGroupId": ('SkillGroupId', 'list', 'str', None),
                       "PhoneNumber": ('PhoneNumber', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_agent_events(
            self,
            instance_id=None,
            start_time=None,
            stop_time=None,
            list_of_event=None,
            list_of_ram_id=None):
        api_request = APIRequest('ListAgentEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "StartTime": start_time,
            "StopTime": stop_time,
            "Event": list_of_event,
            "RamId": list_of_ram_id}
        repeat_info = {"Event": ('Event', 'list', 'str', None),
                       "RamId": ('RamId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def pick_outbound_numbers_by_tags(
            self,
            list_of_prioritized_caller_area=None,
            instance_id=None,
            list_of_service_tag=None,
            list_of_skill_group_id=None,
            count=None,
            callee_number=None):
        api_request = APIRequest('PickOutboundNumbersByTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PrioritizedCallerArea": list_of_prioritized_caller_area,
            "InstanceId": instance_id,
            "ServiceTag": list_of_service_tag,
            "SkillGroupId": list_of_skill_group_id,
            "Count": count,
            "CalleeNumber": callee_number}
        repeat_info = {"PrioritizedCallerArea": ('PrioritizedCallerArea', 'list', 'str', None),
                       "ServiceTag": ('ServiceTag', 'list', 'str', None),
                       "SkillGroupId": ('SkillGroupId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_cab_instance(
            self,
            max_concurrent_conversation=None,
            instance_name=None,
            call_center_instance_id=None,
            instance_description=None):
        api_request = APIRequest('CreateCabInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MaxConcurrentConversation": max_concurrent_conversation,
            "InstanceName": instance_name,
            "CallCenterInstanceId": call_center_instance_id,
            "InstanceDescription": instance_description}
        return self._handle_request(api_request).result

    def list_recording_of_dual_track(
            self,
            calling_number=None,
            agent_id=None,
            instance_id=None,
            called_number=None,
            page_size=None,
            start_time=None,
            stop_time=None,
            connect_id=None,
            page_number=None):
        api_request = APIRequest('ListRecordingOfDualTrack', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallingNumber": calling_number,
            "AgentId": agent_id,
            "InstanceId": instance_id,
            "CalledNumber": called_number,
            "PageSize": page_size,
            "StartTime": start_time,
            "StopTime": stop_time,
            "ConnectId": connect_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def pick_outbound_numbers(
            self,
            instance_id=None,
            count=None,
            list_of_candidate_number=None,
            callee_number=None):
        api_request = APIRequest('PickOutboundNumbers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Count": count,
            "CandidateNumber": list_of_candidate_number,
            "CalleeNumber": callee_number}
        repeat_info = {"CandidateNumber": ('CandidateNumber', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def query_redial_indicator(self, instance_id=None, contact_id=None, mock_response=None):
        api_request = APIRequest('QueryRedialIndicator', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "ContactId": contact_id,
            "MockResponse": mock_response}
        return self._handle_request(api_request).result

    def get_agent_state(self, agent_id=None, instance_id=None, dn=None):
        api_request = APIRequest('GetAgentState', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AgentId": agent_id, "InstanceId": instance_id, "Dn": dn}
        return self._handle_request(api_request).result

    def add_number_to_skill_group(self, number=None, instance_id=None, skill_group_id=None):
        api_request = APIRequest('AddNumberToSkillGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Number": number,
            "InstanceId": instance_id,
            "SkillGroupId": skill_group_id}
        return self._handle_request(api_request).result

    def remove_number_from_skill_group(self, number=None, instance_id=None, skill_group_id=None):
        api_request = APIRequest('RemoveNumberFromSkillGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Number": number,
            "InstanceId": instance_id,
            "SkillGroupId": skill_group_id}
        return self._handle_request(api_request).result

    def list_ivr_tracking_detail(
            self,
            calling_number=None,
            instance_id=None,
            contact_id=None,
            called_number=None,
            page_size=None,
            start_time=None,
            stop_time=None,
            page_number=None):
        api_request = APIRequest('ListIvrTrackingDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallingNumber": calling_number,
            "InstanceId": instance_id,
            "ContactId": contact_id,
            "CalledNumber": called_number,
            "PageSize": page_size,
            "StartTime": start_time,
            "StopTime": stop_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def remove_users_from_skill_group(
            self,
            instance_id=None,
            skill_group_id=None,
            list_of_user_id=None):
        api_request = APIRequest('RemoveUsersFromSkillGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SkillGroupId": skill_group_id,
            "UserId": list_of_user_id}
        repeat_info = {"UserId": ('UserId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_call_measure_summary_reports(self, interval_type=None):
        api_request = APIRequest('ListCallMeasureSummaryReports', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"IntervalType": interval_type}
        return self._handle_request(api_request).result

    def get_call_measure_summary_report(
            self,
            interval_type=None,
            month=None,
            year=None,
            page_size=None,
            day=None,
            page_number=None):
        api_request = APIRequest('GetCallMeasureSummaryReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IntervalType": interval_type,
            "Month": month,
            "Year": year,
            "PageSize": page_size,
            "Day": day,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def call_online_privacy_number(self, tel_a=None, tel_b=None, instance_id=None):
        api_request = APIRequest('CallOnlinePrivacyNumber', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TelA": tel_a, "TelB": tel_b, "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def modify_privacy_number_call_detail(self, call_id=None, instance_id=None, contact_id=None):
        api_request = APIRequest('ModifyPrivacyNumberCallDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallId": call_id,
            "InstanceId": instance_id,
            "ContactId": contact_id}
        return self._handle_request(api_request).result

    def list_privacy_number_call_details(
            self,
            agent_id=None,
            instance_id=None,
            contact_id=None,
            agent_name=None,
            page_size=None,
            end_time=None,
            start_time=None,
            page_number=None):
        api_request = APIRequest('ListPrivacyNumberCallDetails', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AgentId": agent_id,
            "InstanceId": instance_id,
            "ContactId": contact_id,
            "AgentName": agent_name,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def create_media(
            self,
            instance_id=None,
            file_name=None,
            name=None,
            description=None,
            oss_file_path=None,
            upload_result=None,
            type_=None,
            content=None,
            oss_file_name=None):
        api_request = APIRequest('CreateMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "FileName": file_name,
            "Name": name,
            "Description": description,
            "OssFilePath": oss_file_path,
            "UploadResult": upload_result,
            "Type": type_,
            "Content": content,
            "OssFileName": oss_file_name}
        return self._handle_request(api_request).result

    def modify_media(
            self,
            instance_id=None,
            file_name=None,
            name=None,
            description=None,
            oss_file_path=None,
            upload_result=None,
            type_=None,
            content=None,
            oss_file_name=None):
        api_request = APIRequest('ModifyMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "FileName": file_name,
            "Name": name,
            "Description": description,
            "OssFilePath": oss_file_path,
            "UploadResult": upload_result,
            "Type": type_,
            "Content": content,
            "OssFileName": oss_file_name}
        return self._handle_request(api_request).result

    def delete_media(self, instance_id=None, name=None):
        api_request = APIRequest('DeleteMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Name": name}
        return self._handle_request(api_request).result

    def pre_modify_media(
            self,
            instance_id=None,
            file_name=None,
            name=None,
            description=None,
            type_=None,
            content=None):
        api_request = APIRequest('PreModifyMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "FileName": file_name,
            "Name": name,
            "Description": description,
            "Type": type_,
            "Content": content}
        return self._handle_request(api_request).result

    def list_medias(self, instance_id=None, page_size=None, name_prefix=None, page_number=None):
        api_request = APIRequest('ListMedias', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "NamePrefix": name_prefix,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def pre_create_media(
            self,
            instance_id=None,
            file_name=None,
            name=None,
            description=None,
            type_=None,
            content=None):
        api_request = APIRequest('PreCreateMedia', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "FileName": file_name,
            "Name": name,
            "Description": description,
            "Type": type_,
            "Content": content}
        return self._handle_request(api_request).result

    def create_ccc_post_order(self, owner_id=None):
        api_request = APIRequest('CreateCCCPostOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id}
        return self._handle_request(api_request).result

    def simple_dial(self, caller=None, instance_id=None, contract_flow_id=None, callee=None):
        api_request = APIRequest('SimpleDial', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Caller": caller,
            "InstanceId": instance_id,
            "ContractFlowId": contract_flow_id,
            "Callee": callee}
        return self._handle_request(api_request).result

    def list_outbound_phone_number_of_user(self, instance_id=None, user_id=None):
        api_request = APIRequest('ListOutboundPhoneNumberOfUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "UserId": user_id}
        return self._handle_request(api_request).result

    def list_skill_group_summary_reports_since_midnight(
            self,
            instance_id=None,
            skill_groups=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest(
            'ListSkillGroupSummaryReportsSinceMidnight',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SkillGroups": skill_groups,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_skill_group_summary_reports_by_interval(
            self,
            instance_id=None,
            skill_group_ids=None,
            page_size=None,
            end_time=None,
            interval=None,
            start_time=None,
            page_number=None):
        api_request = APIRequest('ListSkillGroupSummaryReportsByInterval',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SkillGroupIds": skill_group_ids,
            "PageSize": page_size,
            "EndTime": end_time,
            "Interval": interval,
            "StartTime": start_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_instance_summary_report(
            self,
            instance_id=None,
            page_size=None,
            end_time=None,
            start_time=None,
            page_number=None):
        api_request = APIRequest('GetInstanceSummaryReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_instance_summary_report_by_interval(
            self,
            instance_id=None,
            page_size=None,
            end_time=None,
            interval=None,
            start_time=None,
            page_number=None):
        api_request = APIRequest('GetInstanceSummaryReportByInterval',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "Interval": interval,
            "StartTime": start_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_instance_summary_report_since_midnight(
            self, instance_id=None, page_size=None, page_number=None):
        api_request = APIRequest('GetInstanceSummaryReportSinceMidnight',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_skill_group_states(
            self,
            instance_id=None,
            skill_group_ids=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('ListSkillGroupStates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SkillGroupIds": skill_group_ids,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def create_instance(
            self,
            list_of_phone_numbers=None,
            list_of_user_object=None,
            name=None,
            domain_name=None,
            phone_number=None,
            description=None,
            storage_max_days=None,
            storage_max_size=None,
            directory_id=None,
            list_of_admin_ram_id=None):
        api_request = APIRequest('CreateInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PhoneNumbers": list_of_phone_numbers,
            "UserObject": list_of_user_object,
            "Name": name,
            "DomainName": domain_name,
            "PhoneNumber": phone_number,
            "Description": description,
            "StorageMaxDays": storage_max_days,
            "StorageMaxSize": storage_max_size,
            "DirectoryId": directory_id,
            "AdminRamId": list_of_admin_ram_id}
        repeat_info = {"PhoneNumbers": ('PhoneNumbers', 'list', 'str', None),
                       "UserObject": ('UserObject', 'list', 'str', None),
                       "AdminRamId": ('AdminRamId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_instance(self, instance_id=None):
        api_request = APIRequest('DeleteInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def get_instance(self, instance_id=None):
        api_request = APIRequest('GetInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def create_contact_flow(
            self,
            canvas=None,
            instance_id=None,
            name=None,
            description=None,
            type_=None,
            content=None):
        api_request = APIRequest('CreateContactFlow', 'POST', 'http', 'RPC', 'body')
        api_request._params = {
            "Canvas": canvas,
            "InstanceId": instance_id,
            "Name": name,
            "Description": description,
            "Type": type_,
            "Content": content}
        return self._handle_request(api_request).result

    def commit_contact_flow_version_modification(
            self,
            canvas=None,
            instance_id=None,
            contact_flow_version_id=None,
            content=None):
        api_request = APIRequest('CommitContactFlowVersionModification',
                                 'POST', 'http', 'RPC', 'body')
        api_request._params = {
            "Canvas": canvas,
            "InstanceId": instance_id,
            "ContactFlowVersionId": contact_flow_version_id,
            "Content": content}
        return self._handle_request(api_request).result

    def publish_contact_flow_version(
            self,
            instance_id=None,
            contact_flow_version_id=None,
            use_tian_gong=None):
        api_request = APIRequest('PublishContactFlowVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "ContactFlowVersionId": contact_flow_version_id,
            "UseTianGong": use_tian_gong}
        return self._handle_request(api_request).result

    def get_instance_state(self, instance_id=None):
        api_request = APIRequest('GetInstanceState', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def modify_skill_group_of_user(
            self,
            list_of_skill_level=None,
            instance_id=None,
            list_of_role_id=None,
            list_of_skill_group_id=None,
            user_id=None):
        api_request = APIRequest('ModifySkillGroupOfUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SkillLevel": list_of_skill_level,
            "InstanceId": instance_id,
            "RoleId": list_of_role_id,
            "SkillGroupId": list_of_skill_group_id,
            "UserId": user_id}
        repeat_info = {"SkillLevel": ('SkillLevel', 'list', 'str', None),
                       "RoleId": ('RoleId', 'list', 'str', None),
                       "SkillGroupId": ('SkillGroupId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_notification_config(
            self,
            list_of_subscriptions=None,
            instance_id=None,
            access_point=None,
            topic=None,
            producer_id=None):
        api_request = APIRequest('ModifyNotificationConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Subscriptions": list_of_subscriptions,
            "InstanceId": instance_id,
            "AccessPoint": access_point,
            "Topic": topic,
            "ProducerId": producer_id}
        repeat_info = {"Subscriptions": ('Subscriptions', 'list', 'dict', [('DisplayName', 'str', None, None),
                                                                           ('Name', 'str', None, None),
                                                                           ('Selected', 'str', None, None),
                                                                           ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def find_users(self, instance_id=None, criteria=None, page_size=None, page_number=None):
        api_request = APIRequest('FindUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Criteria": criteria,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_agent_summary_reports_since_midnight(
            self,
            agent_ids=None,
            instance_id=None,
            skill_group_id=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('ListAgentSummaryReportsSinceMidnight',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AgentIds": agent_ids,
            "InstanceId": instance_id,
            "SkillGroupId": skill_group_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_skill_group_summary_reports(
            self,
            instance_id=None,
            skill_group_ids=None,
            page_size=None,
            end_time=None,
            start_time=None,
            page_number=None):
        api_request = APIRequest('ListSkillGroupSummaryReports', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SkillGroupIds": skill_group_ids,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_agent_summary_reports_by_interval(
            self,
            agent_ids=None,
            instance_id=None,
            skill_group_id=None,
            page_size=None,
            end_time=None,
            interval=None,
            start_time=None,
            page_number=None):
        api_request = APIRequest('ListAgentSummaryReportsByInterval', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AgentIds": agent_ids,
            "InstanceId": instance_id,
            "SkillGroupId": skill_group_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "Interval": interval,
            "StartTime": start_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_agent_summary_reports(
            self,
            agent_ids=None,
            instance_id=None,
            skill_group_id=None,
            page_size=None,
            end_time=None,
            start_time=None,
            page_number=None):
        api_request = APIRequest('ListAgentSummaryReports', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AgentIds": agent_ids,
            "InstanceId": instance_id,
            "SkillGroupId": skill_group_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_predictive_job(self, job_id=None, instance_id=None):
        api_request = APIRequest('GetPredictiveJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JobId": job_id, "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def get_contact_identify_by_out_bound_task_id(self, instance_id=None, outbound_task_id=None):
        api_request = APIRequest('GetContactIdentifyByOutBoundTaskId',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "OutboundTaskId": outbound_task_id}
        return self._handle_request(api_request).result

    def list_agent_states(
            self,
            agent_ids=None,
            instance_id=None,
            skill_group_id=None,
            page_size=None,
            state=None,
            page_number=None):
        api_request = APIRequest('ListAgentStates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AgentIds": agent_ids,
            "InstanceId": instance_id,
            "SkillGroupId": skill_group_id,
            "PageSize": page_size,
            "State": state,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_sms_config(self, instance_id=None, list_of_scenario=None):
        api_request = APIRequest('GetSmsConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Scenario": list_of_scenario}
        repeat_info = {"Scenario": ('Scenario', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_recent_call_records(
            self,
            instance_id=None,
            criteria=None,
            page_size=None,
            start_time=None,
            stop_time=None,
            page_number=None):
        api_request = APIRequest('ListRecentCallRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Criteria": criteria,
            "PageSize": page_size,
            "StartTime": start_time,
            "StopTime": stop_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def send_predefined_short_message(
            self,
            instance_id=None,
            phone_numbers=None,
            config_id=None,
            template_param=None):
        api_request = APIRequest('SendPredefinedShortMessage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PhoneNumbers": phone_numbers,
            "ConfigId": config_id,
            "TemplateParam": template_param}
        return self._handle_request(api_request).result

    def launch_short_message_appraise(
            self,
            acid=None,
            instance_id=None,
            contact_type=None,
            phone_numbers=None,
            skill_group_id=None):
        api_request = APIRequest('LaunchShortMessageAppraise', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Acid": acid,
            "InstanceId": instance_id,
            "ContactType": contact_type,
            "PhoneNumbers": phone_numbers,
            "SkillGroupId": skill_group_id}
        return self._handle_request(api_request).result

    def get_conversation_detail_by_contact_id(
            self,
            instance_id=None,
            contact_id=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('GetConversationDetailByContactId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "ContactId": contact_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_job_group(self, instance_id=None, job_group_id=None):
        api_request = APIRequest('DeleteJobGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "JobGroupId": job_group_id}
        return self._handle_request(api_request).result

    def modify_scenario(
            self,
            variables=None,
            instance_id=None,
            name=None,
            description=None,
            scenario_id=None):
        api_request = APIRequest('ModifyScenario', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Variables": variables,
            "InstanceId": instance_id,
            "Name": name,
            "Description": description,
            "ScenarioId": scenario_id}
        return self._handle_request(api_request).result

    def cancel_predictive_jobs(
            self,
            all_=None,
            list_of_job_id=None,
            instance_id=None,
            job_group_id=None):
        api_request = APIRequest('CancelPredictiveJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "All": all_,
            "JobId": list_of_job_id,
            "InstanceId": instance_id,
            "JobGroupId": job_group_id}
        repeat_info = {"JobId": ('JobId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_predictive_jobs(
            self,
            instance_id=None,
            skill_group_id=None,
            strategy_json=None,
            list_of_jobs_json=None):
        api_request = APIRequest('CreatePredictiveJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SkillGroupId": skill_group_id,
            "StrategyJson": strategy_json,
            "JobsJson": list_of_jobs_json}
        repeat_info = {"JobsJson": ('JobsJson', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_predictive_job_status(
            self,
            contact_name=None,
            instance_id=None,
            time_alignment=None,
            job_group_id=None,
            phone_number=None,
            page_size=None,
            end_time=None,
            start_time=None,
            page_number=None):
        api_request = APIRequest('ListPredictiveJobStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContactName": contact_name,
            "InstanceId": instance_id,
            "TimeAlignment": time_alignment,
            "JobGroupId": job_group_id,
            "PhoneNumber": phone_number,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def create_survey(
            self,
            instance_id=None,
            role=None,
            round=None,
            flow_json=None,
            name=None,
            global_questions=None,
            description=None,
            corpora=None,
            speech_optimization_param=None,
            scenario_id=None):
        api_request = APIRequest('CreateSurvey', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Role": role,
            "Round": round,
            "FlowJson": flow_json,
            "Name": name,
            "GlobalQuestions": global_questions,
            "Description": description,
            "Corpora": corpora,
            "SpeechOptimizationParam": speech_optimization_param,
            "ScenarioId": scenario_id}
        return self._handle_request(api_request).result

    def delete_survey(self, survey_id=None, instance_id=None, scenario_id=None):
        api_request = APIRequest('DeleteSurvey', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SurveyId": survey_id,
            "InstanceId": instance_id,
            "ScenarioId": scenario_id}
        return self._handle_request(api_request).result

    def get_survey(self, survey_id=None, instance_id=None, scenario_id=None):
        api_request = APIRequest('GetSurvey', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SurveyId": survey_id,
            "InstanceId": instance_id,
            "ScenarioId": scenario_id}
        return self._handle_request(api_request).result

    def list_surveys(self, instance_id=None, scenario_id=None):
        api_request = APIRequest('ListSurveys', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "ScenarioId": scenario_id}
        return self._handle_request(api_request).result

    def modify_survey(
            self,
            survey_id=None,
            instance_id=None,
            role=None,
            round=None,
            flow_json=None,
            name=None,
            global_questions=None,
            description=None,
            corpora=None,
            speech_optimization_param=None,
            scenario_id=None,
            flow_id=None):
        api_request = APIRequest('ModifySurvey', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SurveyId": survey_id,
            "InstanceId": instance_id,
            "Role": role,
            "Round": round,
            "FlowJson": flow_json,
            "Name": name,
            "GlobalQuestions": global_questions,
            "Description": description,
            "Corpora": corpora,
            "SpeechOptimizationParam": speech_optimization_param,
            "ScenarioId": scenario_id,
            "FlowId": flow_id}
        return self._handle_request(api_request).result

    def publish_survey(self, survey_id=None, instance_id=None, scenario_id=None):
        api_request = APIRequest('PublishSurvey', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SurveyId": survey_id,
            "InstanceId": instance_id,
            "ScenarioId": scenario_id}
        return self._handle_request(api_request).result

    def get_scenario(self, instance_id=None, scenario_id=None):
        api_request = APIRequest('GetScenario', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "ScenarioId": scenario_id}
        return self._handle_request(api_request).result

    def get_job_template_download_params(self, instance_id=None, scenario_id=None):
        api_request = APIRequest('GetJobTemplateDownloadParams', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "ScenarioId": scenario_id}
        return self._handle_request(api_request).result

    def download_unreachable_contacts(self, instance_id=None, job_group_id=None):
        api_request = APIRequest('DownloadUnreachableContacts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "JobGroupId": job_group_id}
        return self._handle_request(api_request).result

    def list_unreachable_contacts(
            self,
            instance_id=None,
            job_group_id=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('ListUnreachableContacts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "JobGroupId": job_group_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_basic_statistics_report_sub_items(
            self,
            instance_id=None,
            job_group_id=None,
            page_size=None,
            title=None,
            page_number=None):
        api_request = APIRequest('ListBasicStatisticsReportSubItems', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "JobGroupId": job_group_id,
            "PageSize": page_size,
            "Title": title,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def download_original_statistics_report(self, instance_id=None, job_group_id=None):
        api_request = APIRequest('DownloadOriginalStatisticsReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "JobGroupId": job_group_id}
        return self._handle_request(api_request).result

    def list_privileges_of_user(self, instance_id=None, user_id=None):
        api_request = APIRequest('ListPrivilegesOfUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "UserId": user_id}
        return self._handle_request(api_request).result

    def generate_agent_statistic_report(
            self,
            agent_id=None,
            instance_id=None,
            end_date=None,
            page_size=None,
            start_date=None,
            page_number=None):
        api_request = APIRequest('GenerateAgentStatisticReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AgentId": agent_id,
            "InstanceId": instance_id,
            "EndDate": end_date,
            "PageSize": page_size,
            "StartDate": start_date,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def start_back2_back_call(
            self,
            caller=None,
            instance_id=None,
            call_center_number=None,
            callee=None,
            workflow_id=None):
        api_request = APIRequest('StartBack2BackCall', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Caller": caller,
            "InstanceId": instance_id,
            "CallCenterNumber": call_center_number,
            "Callee": callee,
            "WorkflowId": workflow_id}
        return self._handle_request(api_request).result

    def two_parties_call(
            self,
            caller=None,
            instance_id=None,
            callee_customer=None,
            callee_agent=None):
        api_request = APIRequest('TwoPartiesCall', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Caller": caller,
            "InstanceId": instance_id,
            "CalleeCustomer": callee_customer,
            "CalleeAgent": callee_agent}
        return self._handle_request(api_request).result

    def get_agent_data(
            self,
            instance_id=None,
            start_day=None,
            end_day=None,
            page_size=None,
            user_id=None,
            page_number=None):
        api_request = APIRequest('GetAgentData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "StartDay": start_day,
            "EndDay": end_day,
            "PageSize": page_size,
            "UserId": user_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_job_group(self, instance_id=None, job_group_id=None):
        api_request = APIRequest('GetJobGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "JobGroupId": job_group_id}
        return self._handle_request(api_request).result

    def assign_jobs(
            self,
            list_of_calling_number=None,
            instance_id=None,
            group_id=None,
            strategy_json=None,
            scenario_id=None,
            list_of_jobs_json=None):
        api_request = APIRequest('AssignJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallingNumber": list_of_calling_number,
            "InstanceId": instance_id,
            "GroupId": group_id,
            "StrategyJson": strategy_json,
            "ScenarioId": scenario_id,
            "JobsJson": list_of_jobs_json}
        repeat_info = {"CallingNumber": ('CallingNumber', 'list', 'str', None),
                       "JobsJson": ('JobsJson', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def cancel_jobs(
            self,
            all_=None,
            list_of_job_id=None,
            instance_id=None,
            list_of_job_reference_id=None,
            group_id=None,
            scenario_id=None):
        api_request = APIRequest('CancelJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "All": all_,
            "JobId": list_of_job_id,
            "InstanceId": instance_id,
            "JobReferenceId": list_of_job_reference_id,
            "GroupId": group_id,
            "ScenarioId": scenario_id}
        repeat_info = {"JobId": ('JobId', 'list', 'str', None),
                       "JobReferenceId": ('JobReferenceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_batch_jobs(
            self,
            list_of_calling_number=None,
            instance_id=None,
            submitted=None,
            strategy_json=None,
            name=None,
            description=None,
            scenario_id=None,
            job_file_path=None):
        api_request = APIRequest('CreateBatchJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallingNumber": list_of_calling_number,
            "InstanceId": instance_id,
            "Submitted": submitted,
            "StrategyJson": strategy_json,
            "Name": name,
            "Description": description,
            "ScenarioId": scenario_id,
            "JobFilePath": job_file_path}
        repeat_info = {"CallingNumber": ('CallingNumber', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_jobs_by_group(
            self,
            instance_id=None,
            job_failure_reason=None,
            job_status=None,
            job_group_id=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('ListJobsByGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "JobFailureReason": job_failure_reason,
            "JobStatus": job_status,
            "JobGroupId": job_group_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def resume_jobs(
            self,
            all_=None,
            list_of_job_id=None,
            instance_id=None,
            list_of_job_reference_id=None,
            group_id=None,
            scenario_id=None):
        api_request = APIRequest('ResumeJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "All": all_,
            "JobId": list_of_job_id,
            "InstanceId": instance_id,
            "JobReferenceId": list_of_job_reference_id,
            "GroupId": group_id,
            "ScenarioId": scenario_id}
        repeat_info = {"JobId": ('JobId', 'list', 'str', None),
                       "JobReferenceId": ('JobReferenceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def submit_batch_jobs(self, instance_id=None, job_group_id=None):
        api_request = APIRequest('SubmitBatchJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "JobGroupId": job_group_id}
        return self._handle_request(api_request).result

    def suspend_jobs(
            self,
            all_=None,
            list_of_job_id=None,
            instance_id=None,
            list_of_job_reference_id=None,
            group_id=None,
            scenario_id=None):
        api_request = APIRequest('SuspendJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "All": all_,
            "JobId": list_of_job_id,
            "InstanceId": instance_id,
            "JobReferenceId": list_of_job_reference_id,
            "GroupId": group_id,
            "ScenarioId": scenario_id}
        repeat_info = {"JobId": ('JobId', 'list', 'str', None),
                       "JobReferenceId": ('JobReferenceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_scenario_from_template(
            self,
            variables=None,
            instance_id=None,
            name=None,
            description=None,
            template_id=None):
        api_request = APIRequest('CreateScenarioFromTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Variables": variables,
            "InstanceId": instance_id,
            "Name": name,
            "Description": description,
            "TemplateId": template_id}
        return self._handle_request(api_request).result

    def list_scenario_templates(self,):
        api_request = APIRequest('ListScenarioTemplates', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def get_job_data_upload_params(self, instance_id=None, file_name=None):
        api_request = APIRequest('GetJobDataUploadParams', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "FileName": file_name}
        return self._handle_request(api_request).result

    def launch_appraise(self, acid=None, instance_id=None):
        api_request = APIRequest('LaunchAppraise', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Acid": acid, "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def get_conversation_list(self, instance_id=None, task_id=None):
        api_request = APIRequest('GetConversationList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "TaskId": task_id}
        return self._handle_request(api_request).result

    def get_job_list(
            self,
            instance_id=None,
            job_group_id=None,
            page_size=None,
            page_number=None,
            status=None,
            query_all=None):
        api_request = APIRequest('GetJobList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "JobGroupId": job_group_id,
            "PageSize": page_size,
            "PageNumber": page_number,
            "Status": status,
            "QueryAll": query_all}
        return self._handle_request(api_request).result

    def get_task_list(self, job_id=None, instance_id=None):
        api_request = APIRequest('GetTaskList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JobId": job_id, "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def list_config(self, instance_id=None, list_of_config_item=None):
        api_request = APIRequest('ListConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "ConfigItem": list_of_config_item}
        repeat_info = {"ConfigItem": ('ConfigItem', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_real_time_agent(self, instance_id=None):
        api_request = APIRequest('ListRealTimeAgent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def get_job(self, job_id=None, instance_id=None):
        api_request = APIRequest('GetJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JobId": job_id, "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def list_scenarios(self, instance_id=None):
        api_request = APIRequest('ListScenarios', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def create_scenario(
            self,
            instance_id=None,
            list_of_surveys_json=None,
            strategy_json=None,
            name=None,
            description=None,
            type_=None):
        api_request = APIRequest('CreateScenario', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SurveysJson": list_of_surveys_json,
            "StrategyJson": strategy_json,
            "Name": name,
            "Description": description,
            "Type": type_}
        repeat_info = {"SurveysJson": ('SurveysJson', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_number_region_info(self, number=None, instance_id=None):
        api_request = APIRequest('GetNumberRegionInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Number": number, "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def pick_local_number(
            self,
            instance_id=None,
            list_of_candidate_number=None,
            callee_number=None):
        api_request = APIRequest('PickLocalNumber', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "CandidateNumber": list_of_candidate_number,
            "CalleeNumber": callee_number}
        repeat_info = {"CandidateNumber": ('CandidateNumber', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def dialogue(
            self,
            call_id=None,
            calling_number=None,
            instance_id=None,
            called_number=None,
            instance_owner_id=None,
            action_key=None,
            action_params=None,
            call_type=None,
            scenario_id=None,
            task_id=None,
            utterance=None):
        api_request = APIRequest('Dialogue', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallId": call_id,
            "CallingNumber": calling_number,
            "InstanceId": instance_id,
            "CalledNumber": called_number,
            "InstanceOwnerId": instance_owner_id,
            "ActionKey": action_key,
            "ActionParams": action_params,
            "CallType": call_type,
            "ScenarioId": scenario_id,
            "TaskId": task_id,
            "Utterance": utterance}
        return self._handle_request(api_request).result

    def create_job_group(
            self,
            list_of_calling_number=None,
            instance_id=None,
            strategy_json=None,
            name=None,
            description=None,
            scenario_id=None):
        api_request = APIRequest('CreateJobGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallingNumber": list_of_calling_number,
            "InstanceId": instance_id,
            "StrategyJson": strategy_json,
            "Name": name,
            "Description": description,
            "ScenarioId": scenario_id}
        repeat_info = {"CallingNumber": ('CallingNumber', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_job_groups(
            self,
            instance_id=None,
            page_size=None,
            end_time=None,
            start_time=None,
            page_number=None):
        api_request = APIRequest('ListJobGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_job_status_by_call_id(self, call_id=None, instance_id=None):
        api_request = APIRequest('GetJobStatusByCallId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CallId": call_id, "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def list_job_status(
            self,
            contact_name=None,
            instance_id=None,
            time_alignment=None,
            group_id=None,
            phone_number=None,
            page_size=None,
            end_time=None,
            start_time=None,
            scenario_id=None,
            page_number=None):
        api_request = APIRequest('ListJobStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContactName": contact_name,
            "InstanceId": instance_id,
            "TimeAlignment": time_alignment,
            "GroupId": group_id,
            "PhoneNumber": phone_number,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "ScenarioId": scenario_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def start_job(
            self,
            job_json=None,
            list_of_calling_number=None,
            instance_id=None,
            group_id=None,
            self_hosted_call_center=None,
            scenario_id=None):
        api_request = APIRequest('StartJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobJson": job_json,
            "CallingNumber": list_of_calling_number,
            "InstanceId": instance_id,
            "GroupId": group_id,
            "SelfHostedCallCenter": self_hosted_call_center,
            "ScenarioId": scenario_id}
        repeat_info = {"CallingNumber": ('CallingNumber', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_recordings_by_contact_id(self, instance_id=None, contact_id=None):
        api_request = APIRequest('ListRecordingsByContactId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "ContactId": contact_id}
        return self._handle_request(api_request).result

    def list_call_detail_records(
            self,
            contact_type=None,
            contact_id=None,
            criteria=None,
            phone_number=None,
            order_by=None,
            start_time=None,
            stop_time=None,
            page_number=None,
            instance_id=None,
            contact_disposition=None,
            page_size=None,
            with_recording=None):
        api_request = APIRequest('ListCallDetailRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContactType": contact_type,
            "ContactId": contact_id,
            "Criteria": criteria,
            "PhoneNumber": phone_number,
            "OrderBy": order_by,
            "StartTime": start_time,
            "StopTime": stop_time,
            "PageNumber": page_number,
            "InstanceId": instance_id,
            "ContactDisposition": contact_disposition,
            "PageSize": page_size,
            "WithRecording": with_recording}
        return self._handle_request(api_request).result

    def list_recordings(
            self,
            agent_id=None,
            instance_id=None,
            criteria=None,
            phone_number=None,
            page_size=None,
            stop_time=None,
            start_time=None,
            page_number=None):
        api_request = APIRequest('ListRecordings', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AgentId": agent_id,
            "InstanceId": instance_id,
            "Criteria": criteria,
            "PhoneNumber": phone_number,
            "PageSize": page_size,
            "StopTime": stop_time,
            "StartTime": start_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def download_recording(self, instance_id=None, file_name=None, channel=None):
        api_request = APIRequest('DownloadRecording', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "FileName": file_name, "Channel": channel}
        return self._handle_request(api_request).result

    def request_login_info(self, instance_id=None):
        api_request = APIRequest('RequestLoginInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def remove_users(self, instance_id=None, list_of_user_id=None):
        api_request = APIRequest('RemoveUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "UserId": list_of_user_id}
        repeat_info = {"UserId": ('UserId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def remove_phone_number(self, instance_id=None, phone_number_id=None):
        api_request = APIRequest('RemovePhoneNumber', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "PhoneNumberId": phone_number_id}
        return self._handle_request(api_request).result

    def add_phone_number(
            self,
            contact_flow_id=None,
            instance_id=None,
            usage=None,
            phone_number=None):
        api_request = APIRequest('AddPhoneNumber', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContactFlowId": contact_flow_id,
            "InstanceId": instance_id,
            "Usage": usage,
            "PhoneNumber": phone_number}
        return self._handle_request(api_request).result

    def assign_users(
            self,
            list_of_user_ram_id=None,
            list_of_skill_level=None,
            instance_id=None,
            list_of_role_id=None,
            list_of_skill_group_id=None):
        api_request = APIRequest('AssignUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserRamId": list_of_user_ram_id,
            "SkillLevel": list_of_skill_level,
            "InstanceId": instance_id,
            "RoleId": list_of_role_id,
            "SkillGroupId": list_of_skill_group_id}
        repeat_info = {"UserRamId": ('UserRamId', 'list', 'str', None),
                       "SkillLevel": ('SkillLevel', 'list', 'str', None),
                       "RoleId": ('RoleId', 'list', 'str', None),
                       "SkillGroupId": ('SkillGroupId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_skill_group(
            self,
            list_of_skill_level=None,
            instance_id=None,
            allow_private_outbound_number=None,
            list_of_outbound_phone_number_id=None,
            name=None,
            description=None,
            routing_strategy=None,
            list_of_user_id=None):
        api_request = APIRequest('CreateSkillGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SkillLevel": list_of_skill_level,
            "InstanceId": instance_id,
            "AllowPrivateOutboundNumber": allow_private_outbound_number,
            "OutboundPhoneNumberId": list_of_outbound_phone_number_id,
            "Name": name,
            "Description": description,
            "RoutingStrategy": routing_strategy,
            "UserId": list_of_user_id}
        repeat_info = {"SkillLevel": ('SkillLevel', 'list', 'str', None),
                       "OutboundPhoneNumberId": ('OutboundPhoneNumberId', 'list', 'str', None),
                       "UserId": ('UserId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_user(
            self,
            private_outbound_number_id=None,
            list_of_skill_level=None,
            instance_id=None,
            login_name=None,
            phone=None,
            list_of_role_id=None,
            display_name=None,
            list_of_skill_group_id=None,
            email=None):
        api_request = APIRequest('CreateUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PrivateOutboundNumberId": private_outbound_number_id,
            "SkillLevel": list_of_skill_level,
            "InstanceId": instance_id,
            "LoginName": login_name,
            "Phone": phone,
            "RoleId": list_of_role_id,
            "DisplayName": display_name,
            "SkillGroupId": list_of_skill_group_id,
            "Email": email}
        repeat_info = {"SkillLevel": ('SkillLevel', 'list', 'str', None),
                       "RoleId": ('RoleId', 'list', 'str', None),
                       "SkillGroupId": ('SkillGroupId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_skill_group(self, instance_id=None, skill_group_id=None):
        api_request = APIRequest('DeleteSkillGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "SkillGroupId": skill_group_id}
        return self._handle_request(api_request).result

    def get_config(self, instance_id=None, name=None, object_type=None, object_id=None):
        api_request = APIRequest('GetConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Name": name,
            "ObjectType": object_type,
            "ObjectId": object_id}
        return self._handle_request(api_request).result

    def get_service_extensions(self, service_type=None, instance_id=None):
        api_request = APIRequest('GetServiceExtensions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ServiceType": service_type, "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def get_user(self, instance_id=None, user_id=None):
        api_request = APIRequest('GetUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "UserId": user_id}
        return self._handle_request(api_request).result

    def list_contact_flows(self, instance_id=None):
        api_request = APIRequest('ListContactFlows', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def list_phone_numbers(self, outbound_only=None, instance_id=None):
        api_request = APIRequest('ListPhoneNumbers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OutboundOnly": outbound_only, "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def list_roles(self, instance_id=None):
        api_request = APIRequest('ListRoles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def list_skill_groups(self, instance_id=None):
        api_request = APIRequest('ListSkillGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def list_skill_groups_of_user(self, instance_id=None, user_id=None):
        api_request = APIRequest('ListSkillGroupsOfUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "UserId": user_id}
        return self._handle_request(api_request).result

    def list_users(self, instance_id=None, page_size=None, page_number=None):
        api_request = APIRequest('ListUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_users_of_skill_group(
            self,
            instance_id=None,
            skill_group_id=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('ListUsersOfSkillGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SkillGroupId": skill_group_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_phone_number(
            self,
            contact_flow_id=None,
            instance_id=None,
            phone_number_id=None,
            usage=None,
            list_of_skill_group_id=None):
        api_request = APIRequest('ModifyPhoneNumber', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContactFlowId": contact_flow_id,
            "InstanceId": instance_id,
            "PhoneNumberId": phone_number_id,
            "Usage": usage,
            "SkillGroupId": list_of_skill_group_id}
        repeat_info = {"SkillGroupId": ('SkillGroupId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_skill_group(
            self,
            list_of_skill_level=None,
            instance_id=None,
            allow_private_outbound_number=None,
            list_of_outbound_phone_number_id=None,
            skill_group_id=None,
            name=None,
            description=None,
            routing_strategy=None,
            list_of_user_id=None):
        api_request = APIRequest('ModifySkillGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SkillLevel": list_of_skill_level,
            "InstanceId": instance_id,
            "AllowPrivateOutboundNumber": allow_private_outbound_number,
            "OutboundPhoneNumberId": list_of_outbound_phone_number_id,
            "SkillGroupId": skill_group_id,
            "Name": name,
            "Description": description,
            "RoutingStrategy": routing_strategy,
            "UserId": list_of_user_id}
        repeat_info = {"SkillLevel": ('SkillLevel', 'list', 'str', None),
                       "OutboundPhoneNumberId": ('OutboundPhoneNumberId', 'list', 'str', None),
                       "UserId": ('UserId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_user(
            self,
            private_outbound_number_id=None,
            list_of_skill_level=None,
            instance_id=None,
            phone=None,
            list_of_role_id=None,
            display_name=None,
            list_of_skill_group_id=None,
            user_id=None,
            email=None):
        api_request = APIRequest('ModifyUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PrivateOutboundNumberId": private_outbound_number_id,
            "SkillLevel": list_of_skill_level,
            "InstanceId": instance_id,
            "Phone": phone,
            "RoleId": list_of_role_id,
            "DisplayName": display_name,
            "SkillGroupId": list_of_skill_group_id,
            "UserId": user_id,
            "Email": email}
        repeat_info = {"SkillLevel": ('SkillLevel', 'list', 'str', None),
                       "RoleId": ('RoleId', 'list', 'str', None),
                       "SkillGroupId": ('SkillGroupId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def refresh_token(self, instance_id=None):
        api_request = APIRequest('RefreshToken', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result
