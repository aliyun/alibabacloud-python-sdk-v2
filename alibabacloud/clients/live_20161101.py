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


class LiveClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'live'
        self.api_version = '2016-11-01'
        self.location_service_code = 'live'
        self.location_endpoint_type = 'openAPI'

    def describe_live_domain_bps_data_by_time_stamp(
            self,
            location_names=None,
            isp_names=None,
            domain_name=None,
            owner_id=None,
            time_point=None):
        api_request = APIRequest('DescribeLiveDomainBpsDataByTimeStamp',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNames": location_names,
            "IspNames": isp_names,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "TimePoint": time_point}
        return self._handle_request(api_request).result

    def describe_live_stream_transcode_stream_num(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeLiveStreamTranscodeStreamNum',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_live_top_level_domain(
            self,
            top_level_domain=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('UpdateLiveTopLevelDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_live_domain_schdm_by_property(self, property_=None, domain_name=None, owner_id=None):
        api_request = APIRequest('ModifyLiveDomainSchdmByProperty', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Property": property_,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_live_stream_optimized_feature_config(
            self,
            config_status=None,
            config_name=None,
            domain_name=None,
            config_value=None,
            owner_id=None):
        api_request = APIRequest('SetLiveStreamOptimizedFeatureConfig',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ConfigStatus": config_status,
            "ConfigName": config_name,
            "DomainName": domain_name,
            "ConfigValue": config_value,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_stream_optimized_feature_config(
            self, config_name=None, domain_name=None, owner_id=None):
        api_request = APIRequest(
            'DescribeLiveStreamOptimizedFeatureConfig',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ConfigName": config_name,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_live_stream_delay_config(
            self,
            flv_level=None,
            hls_level=None,
            rtmp_delay=None,
            domain_name=None,
            owner_id=None,
            flv_delay=None,
            rtmp_level=None,
            hls_delay=None):
        api_request = APIRequest('SetLiveStreamDelayConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FlvLevel": flv_level,
            "HlsLevel": hls_level,
            "RtmpDelay": rtmp_delay,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "FlvDelay": flv_delay,
            "RtmpLevel": rtmp_level,
            "HlsDelay": hls_delay}
        return self._handle_request(api_request).result

    def describe_live_stream_delay_config(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeLiveStreamDelayConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_domain_online_user_num(
            self, query_time=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeLiveDomainOnlineUserNum', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "QueryTime": query_time,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_domain_frame_rate_and_bit_rate_data(
            self, query_time=None, domain_name=None, owner_id=None):
        api_request = APIRequest(
            'DescribeLiveDomainFrameRateAndBitRateData',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "QueryTime": query_time,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_board_callback(
            self,
            auth_key=None,
            callback_enable=None,
            callback_events=None,
            owner_id=None,
            callback_uri=None,
            app_id=None,
            auth_switch=None):
        api_request = APIRequest('SetBoardCallback', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AuthKey": auth_key,
            "CallbackEnable": callback_enable,
            "CallbackEvents": callback_events,
            "OwnerId": owner_id,
            "CallbackUri": callback_uri,
            "AppId": app_id,
            "AuthSwitch": auth_switch}
        return self._handle_request(api_request).result

    def describe_records(
            self,
            record_state=None,
            page_num=None,
            page_size=None,
            owner_id=None,
            app_id=None):
        api_request = APIRequest('DescribeRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RecordState": record_state,
            "PageNum": page_num,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def describe_record(self, owner_id=None, record_id=None, app_id=None):
        api_request = APIRequest('DescribeRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "RecordId": record_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def complete_board_record(self, end_time=None, owner_id=None, record_id=None, app_id=None):
        api_request = APIRequest('CompleteBoardRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndTime": end_time,
            "OwnerId": owner_id,
            "RecordId": record_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def start_board_record(self, start_time=None, board_id=None, owner_id=None, app_id=None):
        api_request = APIRequest('StartBoardRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "BoardId": board_id,
            "OwnerId": owner_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def apply_record_token(self, owner_id=None, app_id=None):
        api_request = APIRequest('ApplyRecordToken', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def update_board_callback(
            self,
            auth_key=None,
            callback_enable=None,
            callback_events=None,
            owner_id=None,
            callback_uri=None,
            app_id=None,
            auth_switch=None):
        api_request = APIRequest('UpdateBoardCallback', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AuthKey": auth_key,
            "CallbackEnable": callback_enable,
            "CallbackEvents": callback_events,
            "OwnerId": owner_id,
            "CallbackUri": callback_uri,
            "AppId": app_id,
            "AuthSwitch": auth_switch}
        return self._handle_request(api_request).result

    def describe_live_domain_mapping(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeLiveDomainMapping', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_live_index(
            self,
            app_name=None,
            domain_name=None,
            owner_id=None,
            stream_name=None,
            task_id=None):
        api_request = APIRequest('StopLiveIndex', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "StreamName": stream_name,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def start_live_index(
            self,
            oss_bucket=None,
            token_id=None,
            domain_name=None,
            oss_endpoint=None,
            input_url=None,
            owner_id=None,
            app_name=None,
            interval=None,
            oss_ram_role=None,
            stream_name=None,
            oss_user_id=None):
        api_request = APIRequest('StartLiveIndex', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OssBucket": oss_bucket,
            "TokenId": token_id,
            "DomainName": domain_name,
            "OssEndpoint": oss_endpoint,
            "InputUrl": input_url,
            "OwnerId": owner_id,
            "AppName": app_name,
            "Interval": interval,
            "OssRamRole": oss_ram_role,
            "StreamName": stream_name,
            "OssUserId": oss_user_id}
        return self._handle_request(api_request).result

    def real_time_snapshot_command(
            self,
            mode=None,
            app_name=None,
            domain_name=None,
            interval=None,
            owner_id=None,
            command=None,
            stream_name=None):
        api_request = APIRequest('RealTimeSnapshotCommand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Mode": mode,
            "AppName": app_name,
            "DomainName": domain_name,
            "Interval": interval,
            "OwnerId": owner_id,
            "Command": command,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_live_top_domains_by_flow(
            self,
            start_time=None,
            limit=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveTopDomainsByFlow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Limit": limit,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_domain_real_time_bps_data(
            self,
            location_name_en=None,
            isp_name_en=None,
            start_time=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveDomainRealTimeBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "IspNameEn": isp_name_en,
            "StartTime": start_time,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_domain_real_time_http_code_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveDomainRealTimeHttpCodeData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_domain_real_time_traffic_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveDomainRealTimeTrafficData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_live_lazy_pull_stream_info_config(
            self, domain_name=None, owner_id=None, app_name=None):
        api_request = APIRequest('DeleteLiveLazyPullStreamInfoConfig',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id, "AppName": app_name}
        return self._handle_request(api_request).result

    def describe_live_lazy_pull_stream_config(
            self,
            app_name=None,
            liveapi_request_from=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveLazyPullStreamConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "LiveapiRequestFrom": liveapi_request_from,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_live_lazy_pull_stream_info_config(
            self,
            pull_args=None,
            app_name=None,
            liveapi_request_from=None,
            pull_auth_key=None,
            pull_auth_type=None,
            domain_name=None,
            pull_domain_name=None,
            owner_id=None,
            pull_app_name=None,
            pull_protocol=None):
        api_request = APIRequest('SetLiveLazyPullStreamInfoConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PullArgs": pull_args,
            "AppName": app_name,
            "LiveapiRequestFrom": liveapi_request_from,
            "PullAuthKey": pull_auth_key,
            "PullAuthType": pull_auth_type,
            "DomainName": domain_name,
            "PullDomainName": pull_domain_name,
            "OwnerId": owner_id,
            "PullAppName": pull_app_name,
            "PullProtocol": pull_protocol}
        return self._handle_request(api_request).result

    def update_caster_scene_audio(
            self,
            list_of_audio_layer=None,
            caster_id=None,
            scene_id=None,
            list_of_mix_list=None,
            owner_id=None,
            follow_enable=None):
        api_request = APIRequest('UpdateCasterSceneAudio', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AudioLayer": list_of_audio_layer,
            "CasterId": caster_id,
            "SceneId": scene_id,
            "MixList": list_of_mix_list,
            "OwnerId": owner_id,
            "FollowEnable": follow_enable}
        repeat_info = {"AudioLayer": ('AudioLayer',
                                      'list',
                                      'dict',
                                      [('FixedDelayDuration',
                                        'str',
                                        None,
                                        None),
                                       ('VolumeRate',
                                        'str',
                                        None,
                                        None),
                                          ('ValidChannel',
                                           'str',
                                           None,
                                           None),
                                       ]),
                       "MixList": ('MixList',
                                   'list',
                                   'str',
                                   None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def set_caster_channel(
            self,
            resource_id=None,
            play_status=None,
            caster_id=None,
            owner_id=None,
            seek_offset=None,
            channel_id=None):
        api_request = APIRequest('SetCasterChannel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceId": resource_id,
            "PlayStatus": play_status,
            "CasterId": caster_id,
            "OwnerId": owner_id,
            "SeekOffset": seek_offset,
            "ChannelId": channel_id}
        return self._handle_request(api_request).result

    def describe_caster_scene_audio(self, caster_id=None, scene_id=None, owner_id=None):
        api_request = APIRequest('DescribeCasterSceneAudio', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "SceneId": scene_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_caster_channels(self, caster_id=None, owner_id=None):
        api_request = APIRequest('DescribeCasterChannels', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_board(self, owner_id=None, app_id=None, board_data=None):
        api_request = APIRequest('UpdateBoard', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "AppId": app_id, "BoardData": board_data}
        return self._handle_request(api_request).result

    def join_board(self, board_id=None, app_uid=None, owner_id=None, app_id=None):
        api_request = APIRequest('JoinBoard', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BoardId": board_id,
            "AppUid": app_uid,
            "OwnerId": owner_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def describe_board_snapshot(self, owner_id=None, app_id=None, board_id=None):
        api_request = APIRequest('DescribeBoardSnapshot', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "AppId": app_id, "BoardId": board_id}
        return self._handle_request(api_request).result

    def describe_boards(self, page_num=None, page_size=None, owner_id=None, app_id=None):
        api_request = APIRequest('DescribeBoards', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageNum": page_num,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def describe_board_events(
            self,
            start_time=None,
            board_id=None,
            end_time=None,
            owner_id=None,
            app_id=None):
        api_request = APIRequest('DescribeBoardEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "BoardId": board_id,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def delete_board(self, owner_id=None, app_id=None, board_id=None):
        api_request = APIRequest('DeleteBoard', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "AppId": app_id, "BoardId": board_id}
        return self._handle_request(api_request).result

    def create_board(self, app_uid=None, owner_id=None, app_id=None):
        api_request = APIRequest('CreateBoard', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AppUid": app_uid, "OwnerId": owner_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def complete_board(self, owner_id=None, app_id=None, board_id=None):
        api_request = APIRequest('CompleteBoard', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "AppId": app_id, "BoardId": board_id}
        return self._handle_request(api_request).result

    def apply_board_token(self, board_id=None, app_uid=None, owner_id=None, app_id=None):
        api_request = APIRequest('ApplyBoardToken', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BoardId": board_id,
            "AppUid": app_uid,
            "OwnerId": owner_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def describe_live_stream_count(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeLiveStreamCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_certificate_detail(self, security_token=None, cert_name=None, owner_id=None):
        api_request = APIRequest('DescribeLiveCertificateDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "CertName": cert_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_hls_live_stream_real_time_bps_data(
            self, domain_name=None, time=None, owner_id=None):
        api_request = APIRequest('DescribeHlsLiveStreamRealTimeBpsData',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "Time": time, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_live_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('StopLiveDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_live_domain(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('StartLiveDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_live_domain_certificate(
            self,
            force_set=None,
            security_token=None,
            cert_type=None,
            ssl_pub=None,
            cert_name=None,
            ssl_protocol=None,
            domain_name=None,
            owner_id=None,
            ssl_pri=None):
        api_request = APIRequest('SetLiveDomainCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ForceSet": force_set,
            "SecurityToken": security_token,
            "CertType": cert_type,
            "SSLPub": ssl_pub,
            "CertName": cert_name,
            "SSLProtocol": ssl_protocol,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "SSLPri": ssl_pri}
        return self._handle_request(api_request).result

    def batch_set_live_domain_configs(
            self,
            functions=None,
            security_token=None,
            domain_names=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('BatchSetLiveDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Functions": functions,
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_certificate_list(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeLiveCertificateList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_live_domain(
            self,
            security_token=None,
            owner_account=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteLiveDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_domain_configs(
            self,
            function_names=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FunctionNames": function_names,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_live_domain(
            self,
            top_level_domain=None,
            security_token=None,
            owner_account=None,
            scope=None,
            domain_name=None,
            owner_id=None,
            region=None,
            check_url=None,
            live_domain_type=None):
        api_request = APIRequest('AddLiveDomain', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopLevelDomain": top_level_domain,
            "SecurityToken": security_token,
            "OwnerAccount": owner_account,
            "Scope": scope,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "Region": region,
            "CheckUrl": check_url,
            "LiveDomainType": live_domain_type}
        return self._handle_request(api_request).result

    def describe_live_domain_detail(self, security_token=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeLiveDomainDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_delete_live_domain_configs(
            self,
            function_names=None,
            security_token=None,
            domain_names=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('BatchDeleteLiveDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FunctionNames": function_names,
            "SecurityToken": security_token,
            "DomainNames": domain_names,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_room_status(self, owner_id=None, room_id=None, app_id=None):
        api_request = APIRequest('DescribeRoomStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "RoomId": room_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def describe_room_list(
            self,
            start_time=None,
            anchor_id=None,
            page_num=None,
            room_status=None,
            page_size=None,
            order=None,
            end_time=None,
            owner_id=None,
            room_id=None,
            app_id=None):
        api_request = APIRequest('DescribeRoomList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "AnchorId": anchor_id,
            "PageNum": page_num,
            "RoomStatus": room_status,
            "PageSize": page_size,
            "Order": order,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "RoomId": room_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def describe_room_kickout_user_list(
            self,
            page_num=None,
            page_size=None,
            order=None,
            owner_id=None,
            room_id=None,
            app_id=None):
        api_request = APIRequest('DescribeRoomKickoutUserList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageNum": page_num,
            "PageSize": page_size,
            "Order": order,
            "OwnerId": owner_id,
            "RoomId": room_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def send_room_user_notification(
            self,
            data=None,
            to_app_uid=None,
            app_uid=None,
            owner_id=None,
            priority=None,
            room_id=None,
            app_id=None):
        api_request = APIRequest('SendRoomUserNotification', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Data": data,
            "ToAppUid": to_app_uid,
            "AppUid": app_uid,
            "OwnerId": owner_id,
            "Priority": priority,
            "RoomId": room_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def describe_forbid_push_stream_room_list(
            self,
            page_num=None,
            page_size=None,
            order=None,
            owner_id=None,
            app_id=None):
        api_request = APIRequest('DescribeForbidPushStreamRoomList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageNum": page_num,
            "PageSize": page_size,
            "Order": order,
            "OwnerId": owner_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def send_room_notification(
            self,
            data=None,
            app_uid=None,
            owner_id=None,
            priority=None,
            room_id=None,
            app_id=None):
        api_request = APIRequest('SendRoomNotification', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Data": data,
            "AppUid": app_uid,
            "OwnerId": owner_id,
            "Priority": priority,
            "RoomId": room_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def forbid_push_stream(
            self,
            user_data=None,
            end_time=None,
            owner_id=None,
            room_id=None,
            app_id=None):
        api_request = APIRequest('ForbidPushStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "UserData": user_data,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "RoomId": room_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def delete_room(self, owner_id=None, room_id=None, app_id=None):
        api_request = APIRequest('DeleteRoom', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "RoomId": room_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def create_room(
            self,
            template_ids=None,
            anchor_id=None,
            use_app_transcode=None,
            owner_id=None,
            room_id=None,
            app_id=None):
        api_request = APIRequest('CreateRoom', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TemplateIds": template_ids,
            "AnchorId": anchor_id,
            "UseAppTranscode": use_app_transcode,
            "OwnerId": owner_id,
            "RoomId": room_id,
            "AppId": app_id}
        return self._handle_request(api_request).result

    def allow_push_stream(self, owner_id=None, room_id=None, app_id=None):
        api_request = APIRequest('AllowPushStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "RoomId": room_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def describe_live_user_domains(
            self,
            security_token=None,
            page_size=None,
            domain_name=None,
            region_name=None,
            owner_id=None,
            page_number=None,
            domain_status=None,
            live_domain_type=None,
            domain_search_type=None):
        api_request = APIRequest('DescribeLiveUserDomains', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "PageSize": page_size,
            "DomainName": domain_name,
            "RegionName": region_name,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "DomainStatus": domain_status,
            "LiveDomainType": live_domain_type,
            "DomainSearchType": domain_search_type}
        return self._handle_request(api_request).result

    def describe_caster_rtc_info(self, caster_id=None, owner_id=None):
        api_request = APIRequest('DescribeCasterRtcInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_up_bps_peak_data(
            self,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            domain_switch=None):
        api_request = APIRequest('DescribeUpBpsPeakData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "DomainSwitch": domain_switch}
        return self._handle_request(api_request).result

    def describe_up_bps_peak_of_line(
            self,
            line=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            domain_switch=None):
        api_request = APIRequest('DescribeUpBpsPeakOfLine', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Line": line,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "DomainSwitch": domain_switch}
        return self._handle_request(api_request).result

    def describe_up_peak_publish_stream_data(
            self,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            domain_switch=None):
        api_request = APIRequest('DescribeUpPeakPublishStreamData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "DomainSwitch": domain_switch}
        return self._handle_request(api_request).result

    def delete_live_domain_mapping(
            self,
            pull_domain=None,
            security_token=None,
            push_domain=None,
            owner_id=None):
        api_request = APIRequest('DeleteLiveDomainMapping', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PullDomain": pull_domain,
            "SecurityToken": security_token,
            "PushDomain": push_domain,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_live_domain_mapping(
            self,
            pull_domain=None,
            security_token=None,
            push_domain=None,
            owner_id=None):
        api_request = APIRequest('AddLiveDomainMapping', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PullDomain": pull_domain,
            "SecurityToken": security_token,
            "PushDomain": push_domain,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_caster_episode_group_content(self, client_token=None, owner_id=None, content=None):
        api_request = APIRequest('AddCasterEpisodeGroupContent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClientToken": client_token, "OwnerId": owner_id, "Content": content}
        return self._handle_request(api_request).result

    def modify_caster_program(self, caster_id=None, list_of_episode=None, owner_id=None):
        api_request = APIRequest('ModifyCasterProgram', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CasterId": caster_id,
            "Episode": list_of_episode,
            "OwnerId": owner_id}
        repeat_info = {"Episode": ('Episode', 'list', 'dict', [('ResourceId', 'str', None, None),
                                                               ('ComponentId', 'list', 'str', None),
                                                               ('SwitchType', 'str', None, None),
                                                               ('EpisodeType', 'str', None, None),
                                                               ('EpisodeName', 'str', None, None),
                                                               ('EndTime', 'str', None, None),
                                                               ('StartTime', 'str', None, None),
                                                               ('EpisodeId', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_caster_episode(
            self,
            resource_id=None,
            list_of_component_id=None,
            switch_type=None,
            caster_id=None,
            episode_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            episode_id=None):
        api_request = APIRequest('ModifyCasterEpisode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceId": resource_id,
            "ComponentId": list_of_component_id,
            "SwitchType": switch_type,
            "CasterId": caster_id,
            "EpisodeName": episode_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "EpisodeId": episode_id}
        repeat_info = {"ComponentId": ('ComponentId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_caster_program(
            self,
            caster_id=None,
            episode_type=None,
            page_size=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            episode_id=None,
            page_num=None,
            status=None):
        api_request = APIRequest('DescribeCasterProgram', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CasterId": caster_id,
            "EpisodeType": episode_type,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "EpisodeId": episode_id,
            "PageNum": page_num,
            "Status": status}
        return self._handle_request(api_request).result

    def delete_caster_program(self, caster_id=None, owner_id=None):
        api_request = APIRequest('DeleteCasterProgram', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_caster_episode_group(self, owner_id=None, program_id=None):
        api_request = APIRequest('DeleteCasterEpisodeGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "ProgramId": program_id}
        return self._handle_request(api_request).result

    def delete_caster_episode(self, caster_id=None, owner_id=None, episode_id=None):
        api_request = APIRequest('DeleteCasterEpisode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "OwnerId": owner_id, "EpisodeId": episode_id}
        return self._handle_request(api_request).result

    def add_caster_program(self, caster_id=None, list_of_episode=None, owner_id=None):
        api_request = APIRequest('AddCasterProgram', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CasterId": caster_id,
            "Episode": list_of_episode,
            "OwnerId": owner_id}
        repeat_info = {"Episode": ('Episode', 'list', 'dict', [('ResourceId', 'str', None, None),
                                                               ('ComponentId', 'list', 'str', None),
                                                               ('SwitchType', 'str', None, None),
                                                               ('EpisodeType', 'str', None, None),
                                                               ('EpisodeName', 'str', None, None),
                                                               ('EndTime', 'str', None, None),
                                                               ('StartTime', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def add_caster_episode_group(
            self,
            side_output_url=None,
            list_of_item=None,
            client_token=None,
            domain_name=None,
            start_time=None,
            repeat_num=None,
            callback_url=None,
            owner_id=None):
        api_request = APIRequest('AddCasterEpisodeGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SideOutputUrl": side_output_url,
            "Item": list_of_item,
            "ClientToken": client_token,
            "DomainName": domain_name,
            "StartTime": start_time,
            "RepeatNum": repeat_num,
            "CallbackUrl": callback_url,
            "OwnerId": owner_id}
        repeat_info = {"Item": ('Item', 'list', 'dict', [('VodUrl', 'str', None, None),
                                                         ('ItemName', 'str', None, None),
                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def add_caster_episode(
            self,
            resource_id=None,
            list_of_component_id=None,
            switch_type=None,
            caster_id=None,
            episode_type=None,
            episode_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('AddCasterEpisode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceId": resource_id,
            "ComponentId": list_of_component_id,
            "SwitchType": switch_type,
            "CasterId": caster_id,
            "EpisodeType": episode_type,
            "EpisodeName": episode_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        repeat_info = {"ComponentId": ('ComponentId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_live_domain_transcode_data(
            self,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveDomainTranscodeData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_domain_snapshot_data(
            self,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveDomainSnapshotData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_domain_record_data(
            self,
            record_type=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveDomainRecordData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RecordType": record_type,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def real_time_record_command(
            self,
            app_name=None,
            domain_name=None,
            owner_id=None,
            command=None,
            stream_name=None):
        api_request = APIRequest('RealTimeRecordCommand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "Command": command,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_live_domain_traffic_data(
            self,
            domain_name=None,
            end_time=None,
            interval=None,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveDomainTrafficData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainName": domain_name,
            "EndTime": end_time,
            "Interval": interval,
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_domain_bps_data(
            self,
            domain_name=None,
            end_time=None,
            interval=None,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveDomainBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DomainName": domain_name,
            "EndTime": end_time,
            "Interval": interval,
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_trancode_sei(
            self,
            delay=None,
            app_name=None,
            repeat=None,
            domain_name=None,
            pattern=None,
            text=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('AddTrancodeSEI', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Delay": delay,
            "AppName": app_name,
            "Repeat": repeat,
            "DomainName": domain_name,
            "Pattern": pattern,
            "Text": text,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def delete_caster_scene_config(self, caster_id=None, scene_id=None, owner_id=None, type_=None):
        api_request = APIRequest('DeleteCasterSceneConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CasterId": caster_id,
            "SceneId": scene_id,
            "OwnerId": owner_id,
            "Type": type_}
        return self._handle_request(api_request).result

    def add_custom_live_stream_transcode(
            self,
            app=None,
            template=None,
            audio_channel_num=None,
            profile=None,
            fps=None,
            gop=None,
            owner_id=None,
            audio_codec=None,
            audio_rate=None,
            template_type=None,
            audio_bitrate=None,
            domain=None,
            width=None,
            video_bitrate=None,
            audio_profile=None,
            height=None):
        api_request = APIRequest('AddCustomLiveStreamTranscode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "App": app,
            "Template": template,
            "AudioChannelNum": audio_channel_num,
            "Profile": profile,
            "FPS": fps,
            "Gop": gop,
            "OwnerId": owner_id,
            "AudioCodec": audio_codec,
            "AudioRate": audio_rate,
            "TemplateType": template_type,
            "AudioBitrate": audio_bitrate,
            "Domain": domain,
            "Width": width,
            "VideoBitrate": video_bitrate,
            "AudioProfile": audio_profile,
            "Height": height}
        return self._handle_request(api_request).result

    def describe_live_record_vod_configs(
            self,
            page_num=None,
            app_name=None,
            page_size=None,
            stream_name=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveRecordVodConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageNum": page_num,
            "AppName": app_name,
            "PageSize": page_size,
            "StreamName": stream_name,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_live_record_vod_config(
            self,
            app_name=None,
            stream_name=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteLiveRecordVodConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "StreamName": stream_name,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_live_record_vod_config(
            self,
            auto_compose=None,
            compose_vod_transcode_group_id=None,
            storage_location=None,
            app_name=None,
            stream_name=None,
            vod_transcode_group_id=None,
            domain_name=None,
            cycle_duration=None,
            owner_id=None):
        api_request = APIRequest('AddLiveRecordVodConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AutoCompose": auto_compose,
            "ComposeVodTranscodeGroupId": compose_vod_transcode_group_id,
            "StorageLocation": storage_location,
            "AppName": app_name,
            "StreamName": stream_name,
            "VodTranscodeGroupId": vod_transcode_group_id,
            "DomainName": domain_name,
            "CycleDuration": cycle_duration,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_caster_component(
            self,
            component_id=None,
            component_type=None,
            image_layer_content=None,
            caster_id=None,
            effect=None,
            component_layer=None,
            caption_layer_content=None,
            component_name=None,
            owner_id=None,
            text_layer_content=None):
        api_request = APIRequest('ModifyCasterComponent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ComponentId": component_id,
            "ComponentType": component_type,
            "ImageLayerContent": image_layer_content,
            "CasterId": caster_id,
            "Effect": effect,
            "ComponentLayer": component_layer,
            "CaptionLayerContent": caption_layer_content,
            "ComponentName": component_name,
            "OwnerId": owner_id,
            "TextLayerContent": text_layer_content}
        return self._handle_request(api_request).result

    def describe_caster_components(self, component_id=None, caster_id=None, owner_id=None):
        api_request = APIRequest('DescribeCasterComponents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ComponentId": component_id,
            "CasterId": caster_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_caster_component(self, component_id=None, caster_id=None, owner_id=None):
        api_request = APIRequest('DeleteCasterComponent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ComponentId": component_id,
            "CasterId": caster_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_caster_component(
            self,
            component_type=None,
            location_id=None,
            image_layer_content=None,
            caster_id=None,
            effect=None,
            component_layer=None,
            caption_layer_content=None,
            component_name=None,
            owner_id=None,
            text_layer_content=None):
        api_request = APIRequest('AddCasterComponent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ComponentType": component_type,
            "LocationId": location_id,
            "ImageLayerContent": image_layer_content,
            "CasterId": caster_id,
            "Effect": effect,
            "ComponentLayer": component_layer,
            "CaptionLayerContent": caption_layer_content,
            "ComponentName": component_name,
            "OwnerId": owner_id,
            "TextLayerContent": text_layer_content}
        return self._handle_request(api_request).result

    def stop_caster(self, caster_id=None, owner_id=None):
        api_request = APIRequest('StopCaster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_caster(self, caster_id=None, owner_id=None):
        api_request = APIRequest('StartCaster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_stream_history_user_num(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DescribeLiveStreamHistoryUserNum', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def update_caster_scene_config(
            self,
            list_of_component_id=None,
            caster_id=None,
            scene_id=None,
            owner_id=None,
            layout_id=None):
        api_request = APIRequest('UpdateCasterSceneConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ComponentId": list_of_component_id,
            "CasterId": caster_id,
            "SceneId": scene_id,
            "OwnerId": owner_id,
            "LayoutId": layout_id}
        repeat_info = {"ComponentId": ('ComponentId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def stop_caster_scene(self, caster_id=None, scene_id=None, owner_id=None):
        api_request = APIRequest('StopCasterScene', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "SceneId": scene_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_caster_scene(self, caster_id=None, scene_id=None, owner_id=None):
        api_request = APIRequest('StartCasterScene', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "SceneId": scene_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_caster_scene_config(
            self,
            list_of_component_id=None,
            caster_id=None,
            scene_id=None,
            owner_id=None,
            layout_id=None):
        api_request = APIRequest('SetCasterSceneConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ComponentId": list_of_component_id,
            "CasterId": caster_id,
            "SceneId": scene_id,
            "OwnerId": owner_id,
            "LayoutId": layout_id}
        repeat_info = {"ComponentId": ('ComponentId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def set_caster_config(
            self,
            side_output_url=None,
            caster_id=None,
            channel_enable=None,
            domain_name=None,
            program_effect=None,
            program_name=None,
            owner_id=None,
            record_config=None,
            urgent_material_id=None,
            transcode_config=None,
            delay=None,
            caster_name=None,
            callback_url=None):
        api_request = APIRequest('SetCasterConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SideOutputUrl": side_output_url,
            "CasterId": caster_id,
            "ChannelEnable": channel_enable,
            "DomainName": domain_name,
            "ProgramEffect": program_effect,
            "ProgramName": program_name,
            "OwnerId": owner_id,
            "RecordConfig": record_config,
            "UrgentMaterialId": urgent_material_id,
            "TranscodeConfig": transcode_config,
            "Delay": delay,
            "CasterName": caster_name,
            "CallbackUrl": callback_url}
        return self._handle_request(api_request).result

    def modify_caster_video_resource(
            self,
            resource_id=None,
            vod_url=None,
            caster_id=None,
            end_offset=None,
            owner_id=None,
            material_id=None,
            begin_offset=None,
            live_stream_url=None,
            pts_callback_interval=None,
            resource_name=None,
            repeat_num=None):
        api_request = APIRequest('ModifyCasterVideoResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceId": resource_id,
            "VodUrl": vod_url,
            "CasterId": caster_id,
            "EndOffset": end_offset,
            "OwnerId": owner_id,
            "MaterialId": material_id,
            "BeginOffset": begin_offset,
            "LiveStreamUrl": live_stream_url,
            "PtsCallbackInterval": pts_callback_interval,
            "ResourceName": resource_name,
            "RepeatNum": repeat_num}
        return self._handle_request(api_request).result

    def modify_caster_layout(
            self,
            list_of_blend_list=None,
            list_of_audio_layer=None,
            list_of_video_layer=None,
            caster_id=None,
            list_of_mix_list=None,
            owner_id=None,
            layout_id=None):
        api_request = APIRequest('ModifyCasterLayout', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BlendList": list_of_blend_list,
            "AudioLayer": list_of_audio_layer,
            "VideoLayer": list_of_video_layer,
            "CasterId": caster_id,
            "MixList": list_of_mix_list,
            "OwnerId": owner_id,
            "LayoutId": layout_id}
        repeat_info = {"BlendList": ('BlendList', 'list', 'str', None),
                       "AudioLayer": ('AudioLayer', 'list', 'dict', [('FixedDelayDuration', 'str', None, None),
                                                                     ('VolumeRate', 'str', None, None),
                                                                     ('ValidChannel', 'str', None, None),
                                                                     ]),
                       "VideoLayer": ('VideoLayer', 'list', 'dict', [('FillMode', 'str', None, None),
                                                                     ('WidthNormalized', 'str', None, None),
                                                                     ('FixedDelayDuration', 'str', None, None),
                                                                     ('PositionRefer', 'str', None, None),
                                                                     ('PositionNormalized', 'list', 'str', None),
                                                                     ('HeightNormalized', 'str', None, None),
                                                                     ]),
                       "MixList": ('MixList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def effect_caster_video_resource(
            self,
            resource_id=None,
            caster_id=None,
            scene_id=None,
            owner_id=None):
        api_request = APIRequest('EffectCasterVideoResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceId": resource_id,
            "CasterId": caster_id,
            "SceneId": scene_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def effect_caster_urgent(self, caster_id=None, scene_id=None, owner_id=None):
        api_request = APIRequest('EffectCasterUrgent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "SceneId": scene_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_caster_video_resources(self, caster_id=None, owner_id=None):
        api_request = APIRequest('DescribeCasterVideoResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_caster_stream_url(self, caster_id=None, owner_id=None):
        api_request = APIRequest('DescribeCasterStreamUrl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_caster_scenes(self, caster_id=None, scene_id=None, owner_id=None):
        api_request = APIRequest('DescribeCasterScenes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "SceneId": scene_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_casters(
            self,
            caster_name=None,
            caster_id=None,
            page_size=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_num=None,
            status=None):
        api_request = APIRequest('DescribeCasters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CasterName": caster_name,
            "CasterId": caster_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_caster_layouts(self, caster_id=None, owner_id=None, layout_id=None):
        api_request = APIRequest('DescribeCasterLayouts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "OwnerId": owner_id, "LayoutId": layout_id}
        return self._handle_request(api_request).result

    def describe_caster_config(self, caster_id=None, owner_id=None):
        api_request = APIRequest('DescribeCasterConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_caster_video_resource(self, resource_id=None, caster_id=None, owner_id=None):
        api_request = APIRequest('DeleteCasterVideoResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceId": resource_id,
            "CasterId": caster_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_caster_layout(self, caster_id=None, owner_id=None, layout_id=None):
        api_request = APIRequest('DeleteCasterLayout', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CasterId": caster_id, "OwnerId": owner_id, "LayoutId": layout_id}
        return self._handle_request(api_request).result

    def delete_caster(self, security_token=None, caster_id=None, owner_id=None):
        api_request = APIRequest('DeleteCaster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "CasterId": caster_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_caster(
            self,
            caster_template=None,
            expire_time=None,
            norm_type=None,
            caster_name=None,
            client_token=None,
            charge_type=None,
            owner_id=None,
            purchase_time=None):
        api_request = APIRequest('CreateCaster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CasterTemplate": caster_template,
            "ExpireTime": expire_time,
            "NormType": norm_type,
            "CasterName": caster_name,
            "ClientToken": client_token,
            "ChargeType": charge_type,
            "OwnerId": owner_id,
            "PurchaseTime": purchase_time}
        return self._handle_request(api_request).result

    def copy_caster_scene_config(
            self,
            from_scene_id=None,
            caster_id=None,
            owner_id=None,
            to_scene_id=None):
        api_request = APIRequest('CopyCasterSceneConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FromSceneId": from_scene_id,
            "CasterId": caster_id,
            "OwnerId": owner_id,
            "ToSceneId": to_scene_id}
        return self._handle_request(api_request).result

    def copy_caster(self, src_caster_id=None, caster_name=None, client_token=None, owner_id=None):
        api_request = APIRequest('CopyCaster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcCasterId": src_caster_id,
            "CasterName": caster_name,
            "ClientToken": client_token,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_caster_video_resource(
            self,
            vod_url=None,
            caster_id=None,
            end_offset=None,
            owner_id=None,
            material_id=None,
            begin_offset=None,
            live_stream_url=None,
            location_id=None,
            pts_callback_interval=None,
            resource_name=None,
            repeat_num=None):
        api_request = APIRequest('AddCasterVideoResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VodUrl": vod_url,
            "CasterId": caster_id,
            "EndOffset": end_offset,
            "OwnerId": owner_id,
            "MaterialId": material_id,
            "BeginOffset": begin_offset,
            "LiveStreamUrl": live_stream_url,
            "LocationId": location_id,
            "PtsCallbackInterval": pts_callback_interval,
            "ResourceName": resource_name,
            "RepeatNum": repeat_num}
        return self._handle_request(api_request).result

    def add_caster_layout(
            self,
            list_of_blend_list=None,
            list_of_audio_layer=None,
            list_of_video_layer=None,
            caster_id=None,
            list_of_mix_list=None,
            owner_id=None):
        api_request = APIRequest('AddCasterLayout', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BlendList": list_of_blend_list,
            "AudioLayer": list_of_audio_layer,
            "VideoLayer": list_of_video_layer,
            "CasterId": caster_id,
            "MixList": list_of_mix_list,
            "OwnerId": owner_id}
        repeat_info = {"BlendList": ('BlendList', 'list', 'str', None),
                       "AudioLayer": ('AudioLayer', 'list', 'dict', [('FixedDelayDuration', 'str', None, None),
                                                                     ('VolumeRate', 'str', None, None),
                                                                     ('ValidChannel', 'str', None, None),
                                                                     ]),
                       "VideoLayer": ('VideoLayer', 'list', 'dict', [('FillMode', 'str', None, None),
                                                                     ('WidthNormalized', 'str', None, None),
                                                                     ('FixedDelayDuration', 'str', None, None),
                                                                     ('PositionRefer', 'str', None, None),
                                                                     ('PositionNormalized', 'list', 'str', None),
                                                                     ('HeightNormalized', 'str', None, None),
                                                                     ]),
                       "MixList": ('MixList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_live_pull_stream_config(
            self,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeLivePullStreamConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_live_pull_stream_info_config(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DeleteLivePullStreamInfoConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def add_live_pull_stream_info_config(
            self,
            source_url=None,
            app_name=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('AddLivePullStreamInfoConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceUrl": source_url,
            "AppName": app_name,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_live_stream_bit_rate_data(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DescribeLiveStreamBitRateData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def add_live_detect_notify_config(
            self,
            security_token=None,
            domain_name=None,
            notify_url=None,
            owner_id=None):
        api_request = APIRequest('AddLiveDetectNotifyConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "NotifyUrl": notify_url,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_live_snapshot_detect_porn_config(
            self,
            oss_bucket=None,
            app_name=None,
            security_token=None,
            domain_name=None,
            oss_endpoint=None,
            interval=None,
            owner_id=None,
            oss_object=None,
            list_of_scene=None):
        api_request = APIRequest('AddLiveSnapshotDetectPornConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OssBucket": oss_bucket,
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OssEndpoint": oss_endpoint,
            "Interval": interval,
            "OwnerId": owner_id,
            "OssObject": oss_object,
            "Scene": list_of_scene}
        repeat_info = {"Scene": ('Scene', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_live_detect_notify_config(
            self,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteLiveDetectNotifyConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_detect_notify_config(
            self,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveDetectNotifyConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_live_snapshot_detect_porn_config(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteLiveSnapshotDetectPornConfig',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_snapshot_detect_porn_config(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            page_size=None,
            owner_id=None,
            page_num=None,
            order=None):
        api_request = APIRequest('DescribeLiveSnapshotDetectPornConfig',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "Order": order}
        return self._handle_request(api_request).result

    def update_live_detect_notify_config(
            self,
            security_token=None,
            domain_name=None,
            notify_url=None,
            owner_id=None):
        api_request = APIRequest('UpdateLiveDetectNotifyConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "NotifyUrl": notify_url,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_live_snapshot_detect_porn_config(
            self,
            oss_bucket=None,
            app_name=None,
            security_token=None,
            domain_name=None,
            oss_endpoint=None,
            interval=None,
            owner_id=None,
            oss_object=None,
            list_of_scene=None):
        api_request = APIRequest('UpdateLiveSnapshotDetectPornConfig',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OssBucket": oss_bucket,
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OssEndpoint": oss_endpoint,
            "Interval": interval,
            "OwnerId": owner_id,
            "OssObject": oss_object,
            "Scene": list_of_scene}
        repeat_info = {"Scene": ('Scene', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def add_live_record_notify_config(
            self,
            on_demand_url=None,
            security_token=None,
            domain_name=None,
            notify_url=None,
            owner_id=None,
            need_status_notify=None):
        api_request = APIRequest('AddLiveRecordNotifyConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OnDemandUrl": on_demand_url,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "NotifyUrl": notify_url,
            "OwnerId": owner_id,
            "NeedStatusNotify": need_status_notify}
        return self._handle_request(api_request).result

    def delete_live_streams_notify_url_config(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DeleteLiveStreamsNotifyUrlConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_live_record_notify_config(
            self,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteLiveRecordNotifyConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_record_notify_config(
            self,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveRecordNotifyConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_streams_notify_url_config(self, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeLiveStreamsNotifyUrlConfig',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_live_record_notify_config(
            self,
            on_demand_url=None,
            security_token=None,
            domain_name=None,
            notify_url=None,
            owner_id=None,
            need_status_notify=None):
        api_request = APIRequest('UpdateLiveRecordNotifyConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OnDemandUrl": on_demand_url,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "NotifyUrl": notify_url,
            "OwnerId": owner_id,
            "NeedStatusNotify": need_status_notify}
        return self._handle_request(api_request).result

    def describe_live_streams_block_list(
            self,
            security_token=None,
            domain_name=None,
            page_size=None,
            owner_id=None,
            page_num=None):
        api_request = APIRequest('DescribeLiveStreamsBlockList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNum": page_num}
        return self._handle_request(api_request).result

    def describe_live_stream_online_user_num(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DescribeLiveStreamOnlineUserNum', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_live_streams_publish_list(
            self,
            start_time=None,
            page_number=None,
            app_name=None,
            page_size=None,
            stream_name=None,
            query_type=None,
            stream_type=None,
            domain_name=None,
            end_time=None,
            order_by=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveStreamsPublishList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "PageNumber": page_number,
            "AppName": app_name,
            "PageSize": page_size,
            "StreamName": stream_name,
            "QueryType": query_type,
            "StreamType": stream_type,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OrderBy": order_by,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_streams_online_list(
            self,
            stream_type=None,
            domain_name=None,
            end_time=None,
            order_by=None,
            start_time=None,
            owner_id=None,
            page_num=None,
            app_name=None,
            page_size=None,
            stream_name=None,
            query_type=None):
        api_request = APIRequest('DescribeLiveStreamsOnlineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StreamType": stream_type,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OrderBy": order_by,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "AppName": app_name,
            "PageSize": page_size,
            "StreamName": stream_name,
            "QueryType": query_type}
        return self._handle_request(api_request).result

    def describe_live_streams_control_history(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeLiveStreamsControlHistory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_live_stream_transcode(
            self,
            app=None,
            template=None,
            security_token=None,
            domain=None,
            owner_id=None):
        api_request = APIRequest('AddLiveStreamTranscode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "App": app,
            "Template": template,
            "SecurityToken": security_token,
            "Domain": domain,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_live_stream_transcode(
            self,
            app=None,
            template=None,
            security_token=None,
            domain=None,
            owner_id=None):
        api_request = APIRequest('DeleteLiveStreamTranscode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "App": app,
            "Template": template,
            "SecurityToken": security_token,
            "Domain": domain,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_live_streams_frame_rate_and_bit_rate_data(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest(
            'DescribeLiveStreamsFrameRateAndBitRateData',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def forbid_live_stream(
            self,
            resume_time=None,
            app_name=None,
            live_stream_type=None,
            domain_name=None,
            owner_id=None,
            oneshot=None,
            stream_name=None,
            control_stream_action=None):
        api_request = APIRequest('ForbidLiveStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResumeTime": resume_time,
            "AppName": app_name,
            "LiveStreamType": live_stream_type,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "Oneshot": oneshot,
            "StreamName": stream_name,
            "ControlStreamAction": control_stream_action}
        return self._handle_request(api_request).result

    def describe_live_stream_transcode_info(self, owner_id=None, domain_transcode_name=None):
        api_request = APIRequest('DescribeLiveStreamTranscodeInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"OwnerId": owner_id, "DomainTranscodeName": domain_transcode_name}
        return self._handle_request(api_request).result

    def set_live_streams_notify_url_config(
            self,
            auth_key=None,
            domain_name=None,
            notify_url=None,
            owner_id=None,
            auth_type=None):
        api_request = APIRequest('SetLiveStreamsNotifyUrlConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AuthKey": auth_key,
            "DomainName": domain_name,
            "NotifyUrl": notify_url,
            "OwnerId": owner_id,
            "AuthType": auth_type}
        return self._handle_request(api_request).result

    def resume_live_stream(
            self,
            app_name=None,
            security_token=None,
            live_stream_type=None,
            domain_name=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('ResumeLiveStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "LiveStreamType": live_stream_type,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def add_live_app_snapshot_config(
            self,
            time_interval=None,
            oss_bucket=None,
            app_name=None,
            security_token=None,
            domain_name=None,
            oss_endpoint=None,
            sequence_oss_object=None,
            overwrite_oss_object=None,
            owner_id=None):
        api_request = APIRequest('AddLiveAppSnapshotConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TimeInterval": time_interval,
            "OssBucket": oss_bucket,
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OssEndpoint": oss_endpoint,
            "SequenceOssObject": sequence_oss_object,
            "OverwriteOssObject": overwrite_oss_object,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_live_app_record_config(
            self,
            oss_bucket=None,
            app_name=None,
            security_token=None,
            list_of_record_format=None,
            domain_name=None,
            oss_endpoint=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            on_demand=None,
            stream_name=None):
        api_request = APIRequest('AddLiveAppRecordConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OssBucket": oss_bucket,
            "AppName": app_name,
            "SecurityToken": security_token,
            "RecordFormat": list_of_record_format,
            "DomainName": domain_name,
            "OssEndpoint": oss_endpoint,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "OnDemand": on_demand,
            "StreamName": stream_name}
        repeat_info = {"RecordFormat": ('RecordFormat',
                                        'list',
                                        'dict',
                                        [('SliceOssObjectPrefix',
                                          'str',
                                          None,
                                          None),
                                         ('Format',
                                          'str',
                                          None,
                                          None),
                                            ('OssObjectPrefix',
                                             'str',
                                             None,
                                             None),
                                            ('CycleDuration',
                                             'str',
                                             None,
                                             None),
                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_live_record_config(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            page_size=None,
            owner_id=None,
            page_num=None,
            stream_name=None,
            order=None):
        api_request = APIRequest('DescribeLiveRecordConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "StreamName": stream_name,
            "Order": order}
        return self._handle_request(api_request).result

    def delete_live_app_snapshot_config(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DeleteLiveAppSnapshotConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_live_app_record_config(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DeleteLiveAppRecordConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def create_live_stream_record_index_files(
            self,
            oss_bucket=None,
            app_name=None,
            security_token=None,
            domain_name=None,
            oss_endpoint=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None,
            oss_object=None):
        api_request = APIRequest('CreateLiveStreamRecordIndexFiles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OssBucket": oss_bucket,
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OssEndpoint": oss_endpoint,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name,
            "OssObject": oss_object}
        return self._handle_request(api_request).result

    def describe_live_stream_snapshot_info(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            limit=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None,
            order=None):
        api_request = APIRequest('DescribeLiveStreamSnapshotInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "Limit": limit,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name,
            "Order": order}
        return self._handle_request(api_request).result

    def describe_live_stream_record_index_files(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            page_size=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_num=None,
            stream_name=None,
            order=None):
        api_request = APIRequest('DescribeLiveStreamRecordIndexFiles',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "StreamName": stream_name,
            "Order": order}
        return self._handle_request(api_request).result

    def describe_live_stream_record_index_file(
            self,
            record_id=None,
            app_name=None,
            security_token=None,
            domain_name=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DescribeLiveStreamRecordIndexFile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RecordId": record_id,
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_live_stream_record_content(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            stream_name=None):
        api_request = APIRequest('DescribeLiveStreamRecordContent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "StreamName": stream_name}
        return self._handle_request(api_request).result

    def describe_live_snapshot_config(
            self,
            app_name=None,
            security_token=None,
            domain_name=None,
            page_size=None,
            owner_id=None,
            page_num=None,
            order=None):
        api_request = APIRequest('DescribeLiveSnapshotConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNum": page_num,
            "Order": order}
        return self._handle_request(api_request).result

    def update_live_app_snapshot_config(
            self,
            time_interval=None,
            oss_bucket=None,
            app_name=None,
            security_token=None,
            domain_name=None,
            oss_endpoint=None,
            sequence_oss_object=None,
            overwrite_oss_object=None,
            owner_id=None):
        api_request = APIRequest('UpdateLiveAppSnapshotConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TimeInterval": time_interval,
            "OssBucket": oss_bucket,
            "AppName": app_name,
            "SecurityToken": security_token,
            "DomainName": domain_name,
            "OssEndpoint": oss_endpoint,
            "SequenceOssObject": sequence_oss_object,
            "OverwriteOssObject": overwrite_oss_object,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result
