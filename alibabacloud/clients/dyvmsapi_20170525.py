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


class DyvmsapiClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Dyvmsapi'
        self.api_version = '2017-05-25'
        self.location_service_code = 'dyvmsapi'
        self.location_endpoint_type = 'openAPI'

    def cancel_robot_task(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            task_id=None):
        api_request = APIRequest('CancelRobotTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def upload_robot_task_called_file(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            called_number=None,
            tts_param_head=None,
            tts_param=None,
            id_=None,
            owner_id=None):
        api_request = APIRequest('UploadRobotTaskCalledFile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CalledNumber": called_number,
            "TtsParamHead": tts_param_head,
            "TtsParam": tts_param,
            "Id": id_,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_robot_task(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            task_id=None):
        api_request = APIRequest('DeleteRobotTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def stop_robot_task(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            task_id=None):
        api_request = APIRequest('StopRobotTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def query_robot_task_call_detail(
            self,
            resource_owner_id=None,
            query_date=None,
            resource_owner_account=None,
            callee=None,
            owner_id=None,
            task_id=None):
        api_request = APIRequest('QueryRobotTaskCallDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "QueryDate": query_date,
            "ResourceOwnerAccount": resource_owner_account,
            "Callee": callee,
            "OwnerId": owner_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def query_robotv2_all_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryRobotv2AllList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_robot_task_detail(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            id_=None,
            owner_id=None):
        api_request = APIRequest('QueryRobotTaskDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Id": id_,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def query_robot_task_call_list(
            self,
            resource_owner_id=None,
            called=None,
            resource_owner_account=None,
            dialog_count_from=None,
            duration_to=None,
            hangup_direction=None,
            dialog_count_to=None,
            owner_id=None,
            duration_from=None,
            page_no=None,
            page_size=None,
            call_result=None,
            task_id=None):
        api_request = APIRequest('QueryRobotTaskCallList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Called": called,
            "ResourceOwnerAccount": resource_owner_account,
            "DialogCountFrom": dialog_count_from,
            "DurationTo": duration_to,
            "HangupDirection": hangup_direction,
            "DialogCountTo": dialog_count_to,
            "OwnerId": owner_id,
            "DurationFrom": duration_from,
            "PageNo": page_no,
            "PageSize": page_size,
            "CallResult": call_result,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def start_robot_task(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            schedule_time=None,
            owner_id=None,
            task_id=None):
        api_request = APIRequest('StartRobotTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ScheduleTime": schedule_time,
            "OwnerId": owner_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def query_robot_task_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            page_no=None,
            page_size=None,
            task_name=None,
            time=None,
            owner_id=None,
            status=None):
        api_request = APIRequest('QueryRobotTaskList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PageNo": page_no,
            "PageSize": page_size,
            "TaskName": task_name,
            "Time": time,
            "OwnerId": owner_id,
            "Status": status}
        return self._handle_request(api_request).result

    def create_robot_task(
            self,
            resource_owner_id=None,
            recall_state_codes=None,
            resource_owner_account=None,
            task_name=None,
            retry_type=None,
            owner_id=None,
            dialog_id=None,
            recall_times=None,
            caller=None,
            number_status_ident=None,
            corp_name=None,
            recall_interval=None,
            is_self_line=None):
        api_request = APIRequest('CreateRobotTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RecallStateCodes": recall_state_codes,
            "ResourceOwnerAccount": resource_owner_account,
            "TaskName": task_name,
            "RetryType": retry_type,
            "OwnerId": owner_id,
            "DialogId": dialog_id,
            "RecallTimes": recall_times,
            "Caller": caller,
            "NumberStatusIdent": number_status_ident,
            "CorpName": corp_name,
            "RecallInterval": recall_interval,
            "IsSelfLine": is_self_line}
        return self._handle_request(api_request).result

    def cancel_order_robot_task(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            task_id=None):
        api_request = APIRequest('CancelOrderRobotTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def smart_call_operate(
            self,
            call_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            param=None,
            owner_id=None,
            command=None):
        api_request = APIRequest('SmartCallOperate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallId": call_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Param": param,
            "OwnerId": owner_id,
            "Command": command}
        return self._handle_request(api_request).result

    def query_robot_info_list(
            self,
            resource_owner_id=None,
            audit_status=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('QueryRobotInfoList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AuditStatus": audit_status,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_robot_smart_call(
            self,
            resource_owner_id=None,
            early_media_asr=None,
            resource_owner_account=None,
            tts_param_head=None,
            task_name=None,
            tts_param=None,
            owner_id=None,
            dialog_id=None,
            called_number=None,
            schedule_time=None,
            called_show_number=None,
            corp_name=None,
            schedule_call=None,
            is_self_line=None):
        api_request = APIRequest('BatchRobotSmartCall', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "EarlyMediaAsr": early_media_asr,
            "ResourceOwnerAccount": resource_owner_account,
            "TtsParamHead": tts_param_head,
            "TaskName": task_name,
            "TtsParam": tts_param,
            "OwnerId": owner_id,
            "DialogId": dialog_id,
            "CalledNumber": called_number,
            "ScheduleTime": schedule_time,
            "CalledShowNumber": called_show_number,
            "CorpName": corp_name,
            "ScheduleCall": schedule_call,
            "IsSelfLine": is_self_line}
        return self._handle_request(api_request).result

    def query_call_detail_by_task_id(
            self,
            resource_owner_id=None,
            query_date=None,
            resource_owner_account=None,
            callee=None,
            owner_id=None,
            task_id=None):
        api_request = APIRequest('QueryCallDetailByTaskId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "QueryDate": query_date,
            "ResourceOwnerAccount": resource_owner_account,
            "Callee": callee,
            "OwnerId": owner_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def get_rtc_token(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            user_id=None,
            device_id=None,
            is_custom_account=None):
        api_request = APIRequest('GetRtcToken', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "UserId": user_id,
            "DeviceId": device_id,
            "IsCustomAccount": is_custom_account}
        return self._handle_request(api_request).result

    def add_rtc_account(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            device_id=None):
        api_request = APIRequest('AddRtcAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "DeviceId": device_id}
        return self._handle_request(api_request).result

    def voip_add_account(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None,
            device_id=None):
        api_request = APIRequest('VoipAddAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "DeviceId": device_id}
        return self._handle_request(api_request).result

    def voip_get_token(
            self,
            resource_owner_id=None,
            voip_id=None,
            resource_owner_account=None,
            owner_id=None,
            device_id=None,
            is_custom_account=None):
        api_request = APIRequest('VoipGetToken', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "VoipId": voip_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id,
            "DeviceId": device_id,
            "IsCustomAccount": is_custom_account}
        return self._handle_request(api_request).result

    def smart_call(
            self,
            resource_owner_id=None,
            voice_code_param=None,
            early_media_asr=None,
            speed=None,
            asr_base_id=None,
            session_timeout=None,
            dynamic_id=None,
            called_number=None,
            tts_speed=None,
            voice_code=None,
            called_show_number=None,
            action_code_time_break=None,
            tts_conf=None,
            action_code_break=None,
            resource_owner_account=None,
            record_flag=None,
            owner_id=None,
            tts_volume=None,
            volume=None,
            mute_time=None,
            out_id=None,
            asr_model_id=None,
            pause_time=None,
            tts_style=None):
        api_request = APIRequest('SmartCall', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "VoiceCodeParam": voice_code_param,
            "EarlyMediaAsr": early_media_asr,
            "Speed": speed,
            "AsrBaseId": asr_base_id,
            "SessionTimeout": session_timeout,
            "DynamicId": dynamic_id,
            "CalledNumber": called_number,
            "TtsSpeed": tts_speed,
            "VoiceCode": voice_code,
            "CalledShowNumber": called_show_number,
            "ActionCodeTimeBreak": action_code_time_break,
            "TtsConf": tts_conf,
            "ActionCodeBreak": action_code_break,
            "ResourceOwnerAccount": resource_owner_account,
            "RecordFlag": record_flag,
            "OwnerId": owner_id,
            "TtsVolume": tts_volume,
            "Volume": volume,
            "MuteTime": mute_time,
            "OutId": out_id,
            "AsrModelId": asr_model_id,
            "PauseTime": pause_time,
            "TtsStyle": tts_style}
        return self._handle_request(api_request).result

    def query_call_detail_by_call_id(
            self,
            call_id=None,
            resource_owner_id=None,
            query_date=None,
            resource_owner_account=None,
            prod_id=None,
            owner_id=None):
        api_request = APIRequest('QueryCallDetailByCallId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallId": call_id,
            "ResourceOwnerId": resource_owner_id,
            "QueryDate": query_date,
            "ResourceOwnerAccount": resource_owner_account,
            "ProdId": prod_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def cancel_call(
            self,
            call_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('CancelCall', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CallId": call_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def click_to_dial(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            record_flag=None,
            owner_id=None,
            caller_show_number=None,
            session_timeout=None,
            called_number=None,
            called_show_number=None,
            out_id=None,
            asr_flag=None,
            asr_model_id=None,
            caller_number=None):
        api_request = APIRequest('ClickToDial', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RecordFlag": record_flag,
            "OwnerId": owner_id,
            "CallerShowNumber": caller_show_number,
            "SessionTimeout": session_timeout,
            "CalledNumber": called_number,
            "CalledShowNumber": called_show_number,
            "OutId": out_id,
            "AsrFlag": asr_flag,
            "AsrModelId": asr_model_id,
            "CallerNumber": caller_number}
        return self._handle_request(api_request).result

    def ivr_call(
            self,
            bye_code=None,
            list_of_menu_key_map=None,
            resource_owner_id=None,
            resource_owner_account=None,
            start_tts_params=None,
            play_times=None,
            owner_id=None,
            timeout=None,
            start_code=None,
            called_number=None,
            called_show_number=None,
            out_id=None,
            bye_tts_params=None):
        api_request = APIRequest('IvrCall', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ByeCode": bye_code,
            "MenuKeyMap": list_of_menu_key_map,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "StartTtsParams": start_tts_params,
            "PlayTimes": play_times,
            "OwnerId": owner_id,
            "Timeout": timeout,
            "StartCode": start_code,
            "CalledNumber": called_number,
            "CalledShowNumber": called_show_number,
            "OutId": out_id,
            "ByeTtsParams": bye_tts_params}
        repeat_info = {"MenuKeyMap": ('MenuKeyMap', 'list', 'dict', [('Code', 'str', None, None),
                                                                     ('TtsParams', 'str', None, None),
                                                                     ('Key', 'str', None, None),
                                                                     ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def single_call_by_voice(
            self,
            volume=None,
            resource_owner_id=None,
            resource_owner_account=None,
            called_number=None,
            voice_code=None,
            called_show_number=None,
            play_times=None,
            out_id=None,
            owner_id=None,
            speed=None):
        api_request = APIRequest('SingleCallByVoice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Volume": volume,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "CalledNumber": called_number,
            "VoiceCode": voice_code,
            "CalledShowNumber": called_show_number,
            "PlayTimes": play_times,
            "OutId": out_id,
            "OwnerId": owner_id,
            "Speed": speed}
        return self._handle_request(api_request).result

    def single_call_by_tts(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            tts_code=None,
            play_times=None,
            tts_param=None,
            owner_id=None,
            speed=None,
            volume=None,
            called_number=None,
            called_show_number=None,
            out_id=None):
        api_request = APIRequest('SingleCallByTts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "TtsCode": tts_code,
            "PlayTimes": play_times,
            "TtsParam": tts_param,
            "OwnerId": owner_id,
            "Speed": speed,
            "Volume": volume,
            "CalledNumber": called_number,
            "CalledShowNumber": called_show_number,
            "OutId": out_id}
        return self._handle_request(api_request).result
