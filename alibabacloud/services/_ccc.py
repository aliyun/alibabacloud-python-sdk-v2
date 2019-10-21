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


class _CCCResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ccc', _client=_client)
        self.roles = _create_special_resource_collection(
            _CCCRoleResource, _client, _client.list_roles,
            'Roles.Role', 'RoleId', 
        )
    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _CCCInstanceResource(instance_id, _client=self._client)

    def create_ccc_post_order(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ccc_post_order(**_params)
        order_id = _new_get_key_in_response(response, 'OrderId')
        return _CCCPostOrderResource(order_id, _client=self._client)

class _CCCInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "ccc.instance", _client=_client)
        self.instance_id = instance_id
        

        self.contact_flows = _create_sub_resource_without_page_collection(
            _CCCContactFlowResource, _client, _client.list_contact_flows,
            'ContactFlows.ContactFlow', 'ContactFlowId', parent_identifier="InstanceId",parent_identifier_value=self.instance_id
        )
        self.phone_numbers = _create_sub_resource_without_page_collection(
            _CCCPhoneNumberResource, _client, _client.list_phone_numbers,
            'PhoneNumbers.PhoneNumber', 'PhoneNumberId', parent_identifier="InstanceId",parent_identifier_value=self.instance_id
        )
        self.skill_groups = _create_sub_resource_without_page_collection(
            _CCCSkillGroupResource, _client, _client.list_skill_groups,
            'SkillGroups.SkillGroup', 'SkillGroupId', parent_identifier="InstanceId",parent_identifier_value=self.instance_id
        )
    def add_bulk_phone_numbers(self, **params):
        _params = _transfer_params(params)
        return self._client.add_bulk_phone_numbers(instance_id=self.instance_id, **_params)

    def assign_users(self, **params):
        _params = _transfer_params(params)
        return self._client.assign_users(instance_id=self.instance_id, **_params)

    def call_online_privacy_number(self, **params):
        _params = _transfer_params(params)
        return self._client.call_online_privacy_number(instance_id=self.instance_id, **_params)

    def cancel_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.cancel_jobs(instance_id=self.instance_id, **_params)

    def commit_contact_flow_version_modification(self, **params):
        _params = _transfer_params(params)
        return self._client.commit_contact_flow_version_modification(instance_id=self.instance_id, **_params)

    def create_fault(self, **params):
        _params = _transfer_params(params)
        return self._client.create_fault(instance_id=self.instance_id, **_params)

    def create_media(self, **params):
        _params = _transfer_params(params)
        return self._client.create_media(instance_id=self.instance_id, **_params)

    def create_scenario_from_template(self, **params):
        _params = _transfer_params(params)
        return self._client.create_scenario_from_template(instance_id=self.instance_id, **_params)

    def create_voice_appraise(self, **params):
        _params = _transfer_params(params)
        return self._client.create_voice_appraise(instance_id=self.instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_instance(instance_id=self.instance_id, **_params)

    def delete_media(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_media(instance_id=self.instance_id, **_params)

    def dial_ex(self, **params):
        _params = _transfer_params(params)
        return self._client.dial_ex(instance_id=self.instance_id, **_params)

    def dialogue(self, **params):
        _params = _transfer_params(params)
        return self._client.dialogue(instance_id=self.instance_id, **_params)

    def download_all_type_recording(self, **params):
        _params = _transfer_params(params)
        return self._client.download_all_type_recording(instance_id=self.instance_id, **_params)

    def download_cab_recording(self, **params):
        _params = _transfer_params(params)
        return self._client.download_cab_recording(instance_id=self.instance_id, **_params)

    def download_recording(self, **params):
        _params = _transfer_params(params)
        return self._client.download_recording(instance_id=self.instance_id, **_params)

    def find_users(self, **params):
        _params = _transfer_params(params)
        return self._client.find_users(instance_id=self.instance_id, **_params)

    def generate_agent_statistic_report(self, **params):
        _params = _transfer_params(params)
        return self._client.generate_agent_statistic_report(instance_id=self.instance_id, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_instance(instance_id=self.instance_id, **_params)

    def get_agent_data(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_agent_data(instance_id=self.instance_id, **_params)
        return response

    def get_agent_state(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_agent_state(instance_id=self.instance_id, **_params)
        return response

    def get_config(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_config(instance_id=self.instance_id, **_params)
        return response

    def get_contact_identify_by_out_bound_task_id(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_contact_identify_by_out_bound_task_id(instance_id=self.instance_id, **_params)
        return response

    def get_conversation_detail_by_contact_id(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_conversation_detail_by_contact_id(instance_id=self.instance_id, **_params)
        return response

    def get_conversation_list(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_conversation_list(instance_id=self.instance_id, **_params)
        return response

    def get_instance_state(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_instance_state(instance_id=self.instance_id, **_params)
        return response

    def get_instance_summary_report(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_instance_summary_report(instance_id=self.instance_id, **_params)
        return response

    def get_instance_summary_report_by_interval(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_instance_summary_report_by_interval(instance_id=self.instance_id, **_params)
        return response

    def get_instance_summary_report_since_midnight(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_instance_summary_report_since_midnight(instance_id=self.instance_id, **_params)
        return response

    def get_job(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_job(instance_id=self.instance_id, **_params)
        return response

    def get_job_data_upload_params(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_job_data_upload_params(instance_id=self.instance_id, **_params)
        return response

    def get_job_file_upload_url(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_job_file_upload_url(instance_id=self.instance_id, **_params)
        return response

    def get_job_status_by_call_id(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_job_status_by_call_id(instance_id=self.instance_id, **_params)
        return response

    def get_number_region_info(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_number_region_info(instance_id=self.instance_id, **_params)
        return response

    def get_predictive_job(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_predictive_job(instance_id=self.instance_id, **_params)
        return response

    def get_record_oss_upload_param(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_record_oss_upload_param(instance_id=self.instance_id, **_params)
        return response

    def get_service_extensions(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_service_extensions(instance_id=self.instance_id, **_params)
        return response

    def get_sms_config(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_sms_config(instance_id=self.instance_id, **_params)
        return response

    def get_turn_credentials(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_turn_credentials(instance_id=self.instance_id, **_params)
        return response

    def get_turn_server_list(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_turn_server_list(instance_id=self.instance_id, **_params)
        return response

    def get_task_list(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_task_list(instance_id=self.instance_id, **_params)
        return response

    def launch_appraise(self, **params):
        _params = _transfer_params(params)
        return self._client.launch_appraise(instance_id=self.instance_id, **_params)

    def launch_short_message_appraise(self, **params):
        _params = _transfer_params(params)
        return self._client.launch_short_message_appraise(instance_id=self.instance_id, **_params)

    def list_agent_devices(self, **params):
        _params = _transfer_params(params)
        return self._client.list_agent_devices(instance_id=self.instance_id, **_params)

    def list_agent_events(self, **params):
        _params = _transfer_params(params)
        return self._client.list_agent_events(instance_id=self.instance_id, **_params)

    def list_agent_states(self, **params):
        _params = _transfer_params(params)
        return self._client.list_agent_states(instance_id=self.instance_id, **_params)

    def list_agent_summary_reports(self, **params):
        _params = _transfer_params(params)
        return self._client.list_agent_summary_reports(instance_id=self.instance_id, **_params)

    def list_agent_summary_reports_by_interval(self, **params):
        _params = _transfer_params(params)
        return self._client.list_agent_summary_reports_by_interval(instance_id=self.instance_id, **_params)

    def list_agent_summary_reports_since_midnight(self, **params):
        _params = _transfer_params(params)
        return self._client.list_agent_summary_reports_since_midnight(instance_id=self.instance_id, **_params)

    def list_call_detail_records(self, **params):
        _params = _transfer_params(params)
        return self._client.list_call_detail_records(instance_id=self.instance_id, **_params)

    def list_call_event_detail_by_contact_id(self, **params):
        _params = _transfer_params(params)
        return self._client.list_call_event_detail_by_contact_id(instance_id=self.instance_id, **_params)

    def list_config(self, **params):
        _params = _transfer_params(params)
        return self._client.list_config(instance_id=self.instance_id, **_params)

    def list_ivr_tracking_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.list_ivr_tracking_detail(instance_id=self.instance_id, **_params)

    def list_job_groups(self, **params):
        _params = _transfer_params(params)
        return self._client.list_job_groups(instance_id=self.instance_id, **_params)

    def list_job_status(self, **params):
        _params = _transfer_params(params)
        return self._client.list_job_status(instance_id=self.instance_id, **_params)

    def list_medias(self, **params):
        _params = _transfer_params(params)
        return self._client.list_medias(instance_id=self.instance_id, **_params)

    def list_predictive_job_groups(self, **params):
        _params = _transfer_params(params)
        return self._client.list_predictive_job_groups(instance_id=self.instance_id, **_params)

    def list_privacy_number_call_details(self, **params):
        _params = _transfer_params(params)
        return self._client.list_privacy_number_call_details(instance_id=self.instance_id, **_params)

    def list_privileges_of_user(self, **params):
        _params = _transfer_params(params)
        return self._client.list_privileges_of_user(instance_id=self.instance_id, **_params)

    def list_real_time_agent(self, **params):
        _params = _transfer_params(params)
        return self._client.list_real_time_agent(instance_id=self.instance_id, **_params)

    def list_recent_call_records(self, **params):
        _params = _transfer_params(params)
        return self._client.list_recent_call_records(instance_id=self.instance_id, **_params)

    def list_recording_of_dual_track(self, **params):
        _params = _transfer_params(params)
        return self._client.list_recording_of_dual_track(instance_id=self.instance_id, **_params)

    def list_recordings(self, **params):
        _params = _transfer_params(params)
        return self._client.list_recordings(instance_id=self.instance_id, **_params)

    def list_recordings_by_contact_id(self, **params):
        _params = _transfer_params(params)
        return self._client.list_recordings_by_contact_id(instance_id=self.instance_id, **_params)

    def list_scenarios(self, **params):
        _params = _transfer_params(params)
        return self._client.list_scenarios(instance_id=self.instance_id, **_params)

    def list_skill_group_states(self, **params):
        _params = _transfer_params(params)
        return self._client.list_skill_group_states(instance_id=self.instance_id, **_params)

    def list_skill_group_summary_reports(self, **params):
        _params = _transfer_params(params)
        return self._client.list_skill_group_summary_reports(instance_id=self.instance_id, **_params)

    def list_skill_group_summary_reports_by_interval(self, **params):
        _params = _transfer_params(params)
        return self._client.list_skill_group_summary_reports_by_interval(instance_id=self.instance_id, **_params)

    def list_skill_group_summary_reports_since_midnight(self, **params):
        _params = _transfer_params(params)
        return self._client.list_skill_group_summary_reports_since_midnight(instance_id=self.instance_id, **_params)

    def list_users(self, **params):
        _params = _transfer_params(params)
        return self._client.list_users(instance_id=self.instance_id, **_params)

    def list_voice_appraise(self, **params):
        _params = _transfer_params(params)
        return self._client.list_voice_appraise(instance_id=self.instance_id, **_params)

    def modify_cab(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_cab_instance(instance_id=self.instance_id, **_params)

    def modify_media(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_media(instance_id=self.instance_id, **_params)

    def modify_notification_config(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_notification_config(instance_id=self.instance_id, **_params)

    def modify_privacy_number_call_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_privacy_number_call_detail(instance_id=self.instance_id, **_params)

    def pick_local_number(self, **params):
        _params = _transfer_params(params)
        return self._client.pick_local_number(instance_id=self.instance_id, **_params)

    def pick_outbound_numbers(self, **params):
        _params = _transfer_params(params)
        return self._client.pick_outbound_numbers(instance_id=self.instance_id, **_params)

    def pre_create_media(self, **params):
        _params = _transfer_params(params)
        return self._client.pre_create_media(instance_id=self.instance_id, **_params)

    def pre_modify_media(self, **params):
        _params = _transfer_params(params)
        return self._client.pre_modify_media(instance_id=self.instance_id, **_params)

    def predictive_record_failure(self, **params):
        _params = _transfer_params(params)
        return self._client.predictive_record_failure(instance_id=self.instance_id, **_params)

    def predictive_record_success(self, **params):
        _params = _transfer_params(params)
        return self._client.predictive_record_success(instance_id=self.instance_id, **_params)

    def publish_contact_flow_version(self, **params):
        _params = _transfer_params(params)
        return self._client.publish_contact_flow_version(instance_id=self.instance_id, **_params)

    def query_redial_indicator(self, **params):
        _params = _transfer_params(params)
        return self._client.query_redial_indicator(instance_id=self.instance_id, **_params)

    def refresh_token(self, **params):
        _params = _transfer_params(params)
        return self._client.refresh_token(instance_id=self.instance_id, **_params)

    def request_login_info(self, **params):
        _params = _transfer_params(params)
        return self._client.request_login_info(instance_id=self.instance_id, **_params)

    def reset_user_status(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_user_status(instance_id=self.instance_id, **_params)

    def resume_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.resume_jobs(instance_id=self.instance_id, **_params)

    def save_stats(self, **params):
        _params = _transfer_params(params)
        return self._client.save_stats(instance_id=self.instance_id, **_params)

    def save_web_rtc_stats(self, **params):
        _params = _transfer_params(params)
        return self._client.save_web_rtc_stats(instance_id=self.instance_id, **_params)

    def send_predefined_short_message(self, **params):
        _params = _transfer_params(params)
        return self._client.send_predefined_short_message(instance_id=self.instance_id, **_params)

    def simple_dial(self, **params):
        _params = _transfer_params(params)
        return self._client.simple_dial(instance_id=self.instance_id, **_params)

    def start_back2_back_call(self, **params):
        _params = _transfer_params(params)
        return self._client.start_back2_back_call(instance_id=self.instance_id, **_params)

    def submit_cab_recording(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_cab_recording(instance_id=self.instance_id, **_params)

    def suspend_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.suspend_jobs(instance_id=self.instance_id, **_params)

    def two_parties_call(self, **params):
        _params = _transfer_params(params)
        return self._client.two_parties_call(instance_id=self.instance_id, **_params)

    def add_agent_device(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_agent_device(instance_id=self.instance_id,**_params)
        agent_device_id = _new_get_key_in_response(response, 'AgentDeviceId')
        return _CCCAgentDeviceResource(agent_device_id,self.instance_id, _client=self._client)

    def create_contact_flow(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_contact_flow(instance_id=self.instance_id,**_params)
        contact_flow_id = _new_get_key_in_response(response, 'ContactFlowId')
        return _CCCContactFlowResource(contact_flow_id,self.instance_id, _client=self._client)

    def create_job_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_job_group(instance_id=self.instance_id,**_params)
        job_group_id = _new_get_key_in_response(response, 'JobGroupId')
        return _CCCJobGroupResource(job_group_id,self.instance_id, _client=self._client)

    def add_phone_number(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_phone_number(instance_id=self.instance_id,**_params)
        phone_number_id = _new_get_key_in_response(response, 'PhoneNumberId')
        return _CCCPhoneNumberResource(phone_number_id,self.instance_id, _client=self._client)

    def create_scenario(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_scenario(instance_id=self.instance_id,**_params)
        scenario_id = _new_get_key_in_response(response, 'ScenarioId')
        return _CCCScenarioResource(scenario_id,self.instance_id, _client=self._client)

    def create_skill_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_skill_group(instance_id=self.instance_id,**_params)
        skill_group_id = _new_get_key_in_response(response, 'SkillGroupId')
        return _CCCSkillGroupResource(skill_group_id,self.instance_id, _client=self._client)

    def create_user(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_user(instance_id=self.instance_id,**_params)
        user_id = _new_get_key_in_response(response, 'UserId')
        return _CCCUserResource(user_id,self.instance_id, _client=self._client)

class _CCCAgentDeviceResource(ServiceResource):

    def __init__(self, agent_device_id,instance_id, _client=None):
        ServiceResource.__init__(self, "ccc.agent_device", _client=_client)
        self.agent_device_id = agent_device_id
        self.instance_id = instance_id

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_agent_device(agent_device_id=self.agent_device_id,instance_id=self.instance_id, **_params)

class _CCCContactFlowResource(ServiceResource):

    def __init__(self, contact_flow_id,instance_id, _client=None):
        ServiceResource.__init__(self, "ccc.contact_flow", _client=_client)
        self.contact_flow_id = contact_flow_id
        self.instance_id = instance_id
        self.applied_version = None
        self.contact_flow_description = None
        self.contact_flow_name = None
        self.phone_numbers = None
        self.type_ = None
        self.versions = None

    def get_route_point(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_route_point(contact_flow_id=self.contact_flow_id,instance_id=self.instance_id, **_params)
        return response

class _CCCJobGroupResource(ServiceResource):

    def __init__(self, job_group_id,instance_id, _client=None):
        ServiceResource.__init__(self, "ccc.job_group", _client=_client)
        self.job_group_id = job_group_id
        self.instance_id = instance_id

    def cancel_predictive_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.cancel_predictive_jobs(job_group_id=self.job_group_id,instance_id=self.instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_job_group(job_group_id=self.job_group_id,instance_id=self.instance_id, **_params)

    def download_original_statistics_report(self, **params):
        _params = _transfer_params(params)
        return self._client.download_original_statistics_report(job_group_id=self.job_group_id,instance_id=self.instance_id, **_params)

    def download_unreachable_contacts(self, **params):
        _params = _transfer_params(params)
        return self._client.download_unreachable_contacts(job_group_id=self.job_group_id,instance_id=self.instance_id, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_job_group(job_group_id=self.job_group_id,instance_id=self.instance_id, **_params)

    def get_job_list(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_job_list(job_group_id=self.job_group_id,instance_id=self.instance_id, **_params)
        return response

    def list_basic_statistics_report_sub_items(self, **params):
        _params = _transfer_params(params)
        return self._client.list_basic_statistics_report_sub_items(job_group_id=self.job_group_id,instance_id=self.instance_id, **_params)

    def list_jobs_by_group(self, **params):
        _params = _transfer_params(params)
        return self._client.list_jobs_by_group(job_group_id=self.job_group_id,instance_id=self.instance_id, **_params)

    def list_predictive_job_status(self, **params):
        _params = _transfer_params(params)
        return self._client.list_predictive_job_status(job_group_id=self.job_group_id,instance_id=self.instance_id, **_params)

    def list_unreachable_contacts(self, **params):
        _params = _transfer_params(params)
        return self._client.list_unreachable_contacts(job_group_id=self.job_group_id,instance_id=self.instance_id, **_params)

    def submit_batch_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_batch_jobs(job_group_id=self.job_group_id,instance_id=self.instance_id, **_params)

    def publish_predictive(self, **params):
        _params = _transfer_params(params)
        return self._client.publish_predictive_job_group(job_group_id=self.job_group_id,instance_id=self.instance_id, **_params)

class _CCCPhoneNumberResource(ServiceResource):

    def __init__(self, phone_number_id,instance_id, _client=None):
        ServiceResource.__init__(self, "ccc.phone_number", _client=_client)
        self.phone_number_id = phone_number_id
        self.instance_id = instance_id
        self.allow_outbound = None
        self.assignee = None
        self.city = None
        self.contact_flow = None
        self.number = None
        self.number_commodity_status = None
        self.phone_number_description = None
        self.privacy_number = None
        self.province = None
        self.remaining_time = None
        self.sip_telx = None
        self.skill_groups = None
        self.test_only = None
        self.trunks = None
        self.usage = None

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_phone_number(phone_number_id=self.phone_number_id,instance_id=self.instance_id, **_params)

    def remove(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_phone_number(phone_number_id=self.phone_number_id,instance_id=self.instance_id, **_params)

class _CCCScenarioResource(ServiceResource):

    def __init__(self, scenario_id,instance_id, _client=None):
        ServiceResource.__init__(self, "ccc.scenario", _client=_client)
        self.scenario_id = scenario_id
        self.instance_id = instance_id

    def assign_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.assign_jobs(scenario_id=self.scenario_id,instance_id=self.instance_id, **_params)

    def create_batch_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.create_batch_jobs(scenario_id=self.scenario_id,instance_id=self.instance_id, **_params)

    def create_survey(self, **params):
        _params = _transfer_params(params)
        return self._client.create_survey(scenario_id=self.scenario_id,instance_id=self.instance_id, **_params)

    def delete_survey(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_survey(scenario_id=self.scenario_id,instance_id=self.instance_id, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_scenario(scenario_id=self.scenario_id,instance_id=self.instance_id, **_params)

    def get_job_template_download_params(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_job_template_download_params(scenario_id=self.scenario_id,instance_id=self.instance_id, **_params)
        return response

    def get_survey(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_survey(scenario_id=self.scenario_id,instance_id=self.instance_id, **_params)
        return response

    def list_surveys(self, **params):
        _params = _transfer_params(params)
        return self._client.list_surveys(scenario_id=self.scenario_id,instance_id=self.instance_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_scenario(scenario_id=self.scenario_id,instance_id=self.instance_id, **_params)

    def modify_survey(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_survey(scenario_id=self.scenario_id,instance_id=self.instance_id, **_params)

    def publish_survey(self, **params):
        _params = _transfer_params(params)
        return self._client.publish_survey(scenario_id=self.scenario_id,instance_id=self.instance_id, **_params)

    def start_job(self, **params):
        _params = _transfer_params(params)
        return self._client.start_job(scenario_id=self.scenario_id,instance_id=self.instance_id, **_params)

class _CCCSkillGroupResource(ServiceResource):

    def __init__(self, skill_group_id,instance_id, _client=None):
        ServiceResource.__init__(self, "ccc.skill_group", _client=_client)
        self.skill_group_id = skill_group_id
        self.instance_id = instance_id
        self.acc_queue_name = None
        self.acc_skill_group_name = None
        self.outbound_phone_numbers = None
        self.routing_strategy = None
        self.skill_group_description = None
        self.skill_group_name = None
        self.user_count = None

    def pick_global_outbound_numbers(self, **params):
        _params = _transfer_params(params)
        return self._client.pick_global_outbound_numbers(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)

    def pick_outbound_numbers_by_tags(self, **params):
        _params = _transfer_params(params)
        return self._client.pick_outbound_numbers_by_tags(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)

    def add_number_to(self, **params):
        _params = _transfer_params(params)
        return self._client.add_number_to_skill_group(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)

    def create_predictive_job_group(self, **params):
        _params = _transfer_params(params)
        return self._client.create_predictive_job_group(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)

    def create_predictive_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.create_predictive_jobs(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_skill_group(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)

    def get_contact_info_by_outbound_task_id(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_contact_info_by_outbound_task_id(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)
        return response

    def get_jobs_progress(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_jobs_progress(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)
        return response

    def list_users_of(self, **params):
        _params = _transfer_params(params)
        return self._client.list_users_of_skill_group(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_skill_group(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)

    def modify_outbound_numbers(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_skill_group_outbound_numbers(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)

    def remove_number_from(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_number_from_skill_group(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)

    def remove_users_from(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_users_from_skill_group(skill_group_id=self.skill_group_id,instance_id=self.instance_id, **_params)

class _CCCUserResource(ServiceResource):

    def __init__(self, user_id,instance_id, _client=None):
        ServiceResource.__init__(self, "ccc.user", _client=_client)
        self.user_id = user_id
        self.instance_id = instance_id

    def remove(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_users(user_id=self.user_id,instance_id=self.instance_id, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_user(user_id=self.user_id,instance_id=self.instance_id, **_params)

    def list_outbound_phone_number_of(self, **params):
        _params = _transfer_params(params)
        return self._client.list_outbound_phone_number_of_user(user_id=self.user_id,instance_id=self.instance_id, **_params)

    def list_skill_groups_of(self, **params):
        _params = _transfer_params(params)
        return self._client.list_skill_groups_of_user(user_id=self.user_id,instance_id=self.instance_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_user(user_id=self.user_id,instance_id=self.instance_id, **_params)

    def modify_skill_group_of(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_skill_group_of_user(user_id=self.user_id,instance_id=self.instance_id, **_params)

class _CCCPostOrderResource(ServiceResource):

    def __init__(self, order_id, _client=None):
        ServiceResource.__init__(self, "ccc.post_order", _client=_client)
        self.order_id = order_id
        

class _CCCRoleResource(ServiceResource):

    def __init__(self, role_id, _client=None):
        ServiceResource.__init__(self, "ccc.role", _client=_client)
        self.role_id = role_id
        
        self.instance_id = None
        self.role_description = None
        self.role_name = None
