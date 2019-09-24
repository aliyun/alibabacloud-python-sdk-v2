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


class RtcClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'rtc'
        self.api_version = '2018-01-11'
        self.location_service_code = 'rtc'
        self.location_endpoint_type = 'openAPI'

    def describe_rtc_channel_list(
            self,
            sort_type=None,
            user_id=None,
            service_area=None,
            page_size=None,
            owner_id=None,
            page_no=None,
            app_id=None,
            channel_id=None,
            time_point=None):
        api_request = APIRequest('DescribeRtcChannelList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SortType": sort_type,
            "UserId": user_id,
            "ServiceArea": service_area,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNo": page_no,
            "AppId": app_id,
            "ChannelId": channel_id,
            "TimePoint": time_point}
        return self._handle_request(api_request).result

    def describe_rtc_channel_user_list(
            self,
            page_size=None,
            owner_id=None,
            page_no=None,
            app_id=None,
            channel_id=None,
            time_point=None):
        api_request = APIRequest('DescribeRtcChannelUserList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNo": page_no,
            "AppId": app_id,
            "ChannelId": channel_id,
            "TimePoint": time_point}
        return self._handle_request(api_request).result

    def describe_rtc_channel_metric(
            self,
            owner_id=None,
            app_id=None,
            channel_id=None,
            time_point=None):
        api_request = APIRequest('DescribeRtcChannelMetric', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OwnerId": owner_id,
            "AppId": app_id,
            "ChannelId": channel_id,
            "TimePoint": time_point}
        return self._handle_request(api_request).result

    def describe_channel_participants(
            self,
            page_num=None,
            page_size=None,
            order=None,
            owner_id=None,
            app_id=None,
            channel_id=None):
        api_request = APIRequest('DescribeChannelParticipants', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageNum": page_num,
            "PageSize": page_size,
            "Order": order,
            "OwnerId": owner_id,
            "AppId": app_id,
            "ChannelId": channel_id}
        return self._handle_request(api_request).result

    def describe_rtc_channel_cnt_data(
            self,
            start_time=None,
            service_area=None,
            end_time=None,
            owner_id=None,
            app_id=None,
            interval=None):
        api_request = APIRequest('DescribeRtcChannelCntData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "ServiceArea": service_area,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "AppId": app_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_rtc_duration_data(
            self,
            start_time=None,
            service_area=None,
            end_time=None,
            owner_id=None,
            app_id=None,
            interval=None):
        api_request = APIRequest('DescribeRtcDurationData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "ServiceArea": service_area,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "AppId": app_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_rtc_peak_channel_cnt_data(
            self,
            start_time=None,
            service_area=None,
            end_time=None,
            owner_id=None,
            app_id=None,
            interval=None):
        api_request = APIRequest('DescribeRtcPeakChannelCntData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "ServiceArea": service_area,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "AppId": app_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_rtc_peak_user_cnt_data(
            self,
            start_time=None,
            service_area=None,
            end_time=None,
            owner_id=None,
            app_id=None,
            interval=None):
        api_request = APIRequest('DescribeRtcPeakUserCntData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "ServiceArea": service_area,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "AppId": app_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_rtc_user_cnt_data(
            self,
            start_time=None,
            service_area=None,
            end_time=None,
            owner_id=None,
            app_id=None,
            interval=None):
        api_request = APIRequest('DescribeRtcUserCntData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "ServiceArea": service_area,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "AppId": app_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def stop_mpu_task(self, owner_id=None, app_id=None, task_id=None):
        api_request = APIRequest('StopMPUTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "AppId": app_id, "TaskId": task_id}
        return self._handle_request(api_request).result

    def start_mpu_task(
            self,
            list_of_user_panes=None,
            background_color=None,
            crop_mode=None,
            task_profile=None,
            list_of_layout_ids=None,
            task_id=None,
            stream_url=None,
            owner_id=None,
            app_id=None,
            media_encode=None,
            channel_id=None):
        api_request = APIRequest('StartMPUTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserPanes": list_of_user_panes,
            "BackgroundColor": background_color,
            "CropMode": crop_mode,
            "TaskProfile": task_profile,
            "LayoutIds": list_of_layout_ids,
            "TaskId": task_id,
            "StreamURL": stream_url,
            "OwnerId": owner_id,
            "AppId": app_id,
            "MediaEncode": media_encode,
            "ChannelId": channel_id}
        repeat_info = {"UserPanes": ('UserPanes', 'list', 'dict', [('PaneId', 'str', None, None),
                                                                   ('UserId', 'str', None, None),
                                                                   ('SourceType', 'str', None, None),
                                                                   ]),
                       "LayoutIds": ('LayoutIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_mpu_task_status(self, owner_id=None, app_id=None, task_id=None):
        api_request = APIRequest('GetMPUTaskStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "AppId": app_id, "TaskId": task_id}
        return self._handle_request(api_request).result

    def receive_notify(
            self,
            trace_id=None,
            content=None,
            event=None,
            owner_id=None,
            content_type=None,
            biz_id=None):
        api_request = APIRequest('ReceiveNotify', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TraceId": trace_id,
            "Content": content,
            "Event": event,
            "OwnerId": owner_id,
            "ContentType": content_type,
            "BizId": biz_id}
        return self._handle_request(api_request).result

    def update_task_param(
            self,
            list_of_mix_panes=None,
            task_id=None,
            owner_id=None,
            template_id=None,
            app_id=None,
            channel_id=None):
        api_request = APIRequest('UpdateTaskParam', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MixPanes": list_of_mix_panes,
            "TaskId": task_id,
            "OwnerId": owner_id,
            "TemplateId": template_id,
            "AppId": app_id,
            "ChannelId": channel_id}
        repeat_info = {"MixPanes": ('MixPanes', 'list', 'dict', [('PaneId', 'str', None, None),
                                                                 ('UserId', 'str', None, None),
                                                                 ('SourceType', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def stop_task(self, owner_id=None, app_id=None, channel_id=None, task_id=None):
        api_request = APIRequest('StopTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OwnerId": owner_id,
            "AppId": app_id,
            "ChannelId": channel_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def start_task(
            self,
            list_of_mix_panes=None,
            idempotent_id=None,
            owner_id=None,
            template_id=None,
            app_id=None,
            channel_id=None):
        api_request = APIRequest('StartTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MixPanes": list_of_mix_panes,
            "IdempotentId": idempotent_id,
            "OwnerId": owner_id,
            "TemplateId": template_id,
            "AppId": app_id,
            "ChannelId": channel_id}
        repeat_info = {"MixPanes": ('MixPanes', 'list', 'dict', [('PaneId', 'str', None, None),
                                                                 ('UserId', 'str', None, None),
                                                                 ('SourceType', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_template_info(self, owner_id=None, template_id=None, app_id=None):
        api_request = APIRequest('GetTemplateInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "TemplateId": template_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def get_task_status(self, owner_id=None, app_id=None, channel_id=None, task_id=None):
        api_request = APIRequest('GetTaskStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OwnerId": owner_id,
            "AppId": app_id,
            "ChannelId": channel_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def get_task_param(self, owner_id=None, app_id=None, task_id=None):
        api_request = APIRequest('GetTaskParam', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "AppId": app_id, "TaskId": task_id}
        return self._handle_request(api_request).result

    def get_all_template(self, owner_id=None, app_id=None):
        api_request = APIRequest('GetAllTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def delete_template(self, owner_id=None, template_id=None, app_id=None):
        api_request = APIRequest('DeleteTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "TemplateId": template_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def create_template(
            self,
            service_mode=None,
            list_of_live_config=None,
            media_config=None,
            max_mix_stream_count=None,
            list_of_record_config=None,
            owner_id=None,
            list_of_lay_out=None,
            app_id=None,
            call_back=None,
            mix_mode=None):
        api_request = APIRequest('CreateTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ServiceMode": service_mode,
            "LiveConfig": list_of_live_config,
            "MediaConfig": media_config,
            "MaxMixStreamCount": max_mix_stream_count,
            "RecordConfig": list_of_record_config,
            "OwnerId": owner_id,
            "LayOut": list_of_lay_out,
            "AppId": app_id,
            "CallBack": call_back,
            "MixMode": mix_mode}
        repeat_info = {"LiveConfig": ('LiveConfig',
                                      'list',
                                      'dict',
                                      [('DomainName',
                                        'str',
                                        None,
                                        None),
                                       ('AppName',
                                        'str',
                                        None,
                                        None),
                                       ]),
                       "RecordConfig": ('RecordConfig',
                                        'list',
                                        'dict',
                                        [('StorageType',
                                          'str',
                                          None,
                                          None),
                                         ('FileFormat',
                                            'str',
                                            None,
                                            None),
                                            ('OssEndPoint',
                                             'str',
                                             None,
                                             None),
                                            ('OssBucket',
                                             'str',
                                             None,
                                             None),
                                            ('VodTransCodeGroupId',
                                             'str',
                                             None,
                                             None),
                                         ]),
                       "LayOut": ('LayOut',
                                  'list',
                                  'dict',
                                  [('Color',
                                    'str',
                                    None,
                                    None),
                                   ('CutMode',
                                      'str',
                                      None,
                                      None),
                                      ('LayOutId',
                                       'str',
                                       None,
                                       None),
                                   ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_channel_token(
            self,
            session_id=None,
            uid=None,
            owner_id=None,
            nonce=None,
            app_id=None,
            channel_id=None):
        api_request = APIRequest('CreateChannelToken', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SessionId": session_id,
            "UId": uid,
            "OwnerId": owner_id,
            "Nonce": nonce,
            "AppId": app_id,
            "ChannelId": channel_id}
        return self._handle_request(api_request).result

    def remove_terminals(
            self,
            list_of_terminal_ids=None,
            owner_id=None,
            app_id=None,
            channel_id=None):
        api_request = APIRequest('RemoveTerminals', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TerminalIds": list_of_terminal_ids,
            "OwnerId": owner_id,
            "AppId": app_id,
            "ChannelId": channel_id}
        repeat_info = {"TerminalIds": ('TerminalIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def remove_participants(
            self,
            list_of_participant_ids=None,
            owner_id=None,
            conference_id=None,
            app_id=None):
        api_request = APIRequest('RemoveParticipants', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ParticipantIds": list_of_participant_ids,
            "OwnerId": owner_id,
            "ConferenceId": conference_id,
            "AppId": app_id}
        repeat_info = {"ParticipantIds": ('ParticipantIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_statis(
            self,
            sort_type=None,
            start_time=None,
            data_type=None,
            service_area=None,
            end_time=None,
            owner_id=None,
            app_id=None,
            interval=None):
        api_request = APIRequest('DescribeStatis', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SortType": sort_type,
            "StartTime": start_time,
            "DataType": data_type,
            "ServiceArea": service_area,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "AppId": app_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_record_list(
            self,
            sort_type=None,
            start_time=None,
            service_area=None,
            page_size=None,
            id_=None,
            end_time=None,
            owner_id=None,
            id_type=None,
            page_no=None,
            app_id=None):
        api_request = APIRequest('DescribeRecordList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SortType": sort_type,
            "StartTime": start_time,
            "ServiceArea": service_area,
            "PageSize": page_size,
            "Id": id_,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "IdType": id_type,
            "PageNo": page_no,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def describe_record_detail(
            self,
            start_time=None,
            end_time=None,
            owner_id=None,
            record_id=None,
            app_id=None,
            channel_id=None):
        api_request = APIRequest('DescribeRecordDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "RecordId": record_id,
            "AppId": app_id,
            "ChannelId": channel_id}
        return self._handle_request(api_request).result

    def describe_real_time_record_list(self, end_time=None, start_time=None, owner_id=None):
        api_request = APIRequest('DescribeRealTimeRecordList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"EndTime": end_time, "StartTime": start_time, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_real_time_record_detail(
            self,
            owner_id=None,
            record_id=None,
            app_id=None,
            channel_id=None):
        api_request = APIRequest('DescribeRealTimeRecordDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OwnerId": owner_id,
            "RecordId": record_id,
            "AppId": app_id,
            "ChannelId": channel_id}
        return self._handle_request(api_request).result

    def update_channel(self, owner_id=None, nonce=None, app_id=None, channel_id=None):
        api_request = APIRequest('UpdateChannel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OwnerId": owner_id,
            "Nonce": nonce,
            "AppId": app_id,
            "ChannelId": channel_id}
        return self._handle_request(api_request).result

    def delete_channel(self, owner_id=None, app_id=None, channel_id=None):
        api_request = APIRequest('DeleteChannel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "AppId": app_id, "ChannelId": channel_id}
        return self._handle_request(api_request).result

    def create_channel(self, owner_id=None, app_id=None, channel_id=None):
        api_request = APIRequest('CreateChannel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "AppId": app_id, "ChannelId": channel_id}
        return self._handle_request(api_request).result

    def unmute_audio_all(self, owner_id=None, participant_id=None, conference_id=None, app_id=None):
        api_request = APIRequest('UnmuteAudioAll', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OwnerId": owner_id,
            "ParticipantId": participant_id,
            "ConferenceId": conference_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def unmute_audio(
            self,
            list_of_participant_ids=None,
            owner_id=None,
            conference_id=None,
            app_id=None):
        api_request = APIRequest('UnmuteAudio', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ParticipantIds": list_of_participant_ids,
            "OwnerId": owner_id,
            "ConferenceId": conference_id,
            "AppId": app_id}
        repeat_info = {"ParticipantIds": ('ParticipantIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def mute_audio_all(self, owner_id=None, participant_id=None, conference_id=None, app_id=None):
        api_request = APIRequest('MuteAudioAll', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OwnerId": owner_id,
            "ParticipantId": participant_id,
            "ConferenceId": conference_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def mute_audio(
            self,
            list_of_participant_ids=None,
            owner_id=None,
            conference_id=None,
            app_id=None):
        api_request = APIRequest('MuteAudio', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ParticipantIds": list_of_participant_ids,
            "OwnerId": owner_id,
            "ConferenceId": conference_id,
            "AppId": app_id}
        repeat_info = {"ParticipantIds": ('ParticipantIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_conference(
            self,
            start_time=None,
            type_=None,
            conference_id=None,
            conference_name=None,
            owner_id=None,
            app_id=None,
            remind_notice=None):
        api_request = APIRequest('ModifyConference', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Type": type_,
            "ConferenceId": conference_id,
            "ConferenceName": conference_name,
            "OwnerId": owner_id,
            "AppId": app_id,
            "RemindNotice": remind_notice}
        return self._handle_request(api_request).result

    def modify_app(self, owner_id=None, app_name=None, app_id=None):
        api_request = APIRequest('ModifyApp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "AppName": app_name, "AppId": app_id}
        return self._handle_request(api_request).result

    def describe_conference_auth_info(self, owner_id=None, conference_id=None, app_id=None):
        api_request = APIRequest('DescribeConferenceAuthInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "ConferenceId": conference_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def describe_apps(
            self,
            page_num=None,
            page_size=None,
            order=None,
            owner_id=None,
            app_id=None,
            status=None):
        api_request = APIRequest('DescribeApps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageNum": page_num,
            "PageSize": page_size,
            "Order": order,
            "OwnerId": owner_id,
            "AppId": app_id,
            "Status": status}
        return self._handle_request(api_request).result

    def delete_conference(self, owner_id=None, conference_id=None, app_id=None):
        api_request = APIRequest('DeleteConference', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "ConferenceId": conference_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def create_conference(
            self,
            client_token=None,
            start_time=None,
            type_=None,
            conference_name=None,
            owner_id=None,
            app_id=None,
            remind_notice=None):
        api_request = APIRequest('CreateConference', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "StartTime": start_time,
            "Type": type_,
            "ConferenceName": conference_name,
            "OwnerId": owner_id,
            "AppId": app_id,
            "RemindNotice": remind_notice}
        return self._handle_request(api_request).result
