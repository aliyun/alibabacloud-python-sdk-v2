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


class _LIVEResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'live', _client=_client)
        self.boards = _create_special_resource_collection(
            _LIVEBoardResource, _client, _client.describe_boards,
            'Boards.Event', 'BoardId', 
        )
        self.casters = _create_special_resource_collection(
            _LIVECasterResource, _client, _client.describe_casters,
            'CasterList.Caster', 'CasterId', 
        )
        self.records = _create_special_resource_collection(
            _LIVERecordResource, _client, _client.describe_records,
            'Records.Record', 'RecordId', 
        )
    def create_board(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_board(**_params)
        board_id = _new_get_key_in_response(response, 'BoardId')
        return _LIVEBoardResource(board_id, _client=self._client)

    def join_board(self, **params):
        _params = _transfer_params(params)
        response = self._client.join_board(**_params)
        board_id = _new_get_key_in_response(response, 'BoardId')
        return _LIVEBoardResource(board_id, _client=self._client)

    def copy_caster(self, **params):
        _params = _transfer_params(params)
        response = self._client.copy_caster(**_params)
        caster_id = _new_get_key_in_response(response, 'CasterId')
        return _LIVECasterResource(caster_id, _client=self._client)

    def create_caster(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_caster(**_params)
        caster_id = _new_get_key_in_response(response, 'CasterId')
        return _LIVECasterResource(caster_id, _client=self._client)

    def delete_caster(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_caster(**_params)
        caster_id = _new_get_key_in_response(response, 'CasterId')
        return _LIVECasterResource(caster_id, _client=self._client)

    def add_caster_episode_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_caster_episode_group(**_params)
        program_id = _new_get_key_in_response(response, 'ProgramId')
        return _LIVECasterEpisodeGroupResource(program_id, _client=self._client)

    def add_live_domain(self, **params):
        _params = _transfer_params(params)
        self._client.add_live_domain(**_params)
        live_domain_name = _params.get("live_domain_name")
        return _LIVELiveDomainResource(live_domain_name, _client=self._client)

    def create_room(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_room(**_params)
        room_id = _new_get_key_in_response(response, 'RoomId')
        return _LIVERoomResource(room_id, _client=self._client)

class _LIVEBoardResource(ServiceResource):

    def __init__(self, board_id, _client=None):
        ServiceResource.__init__(self, "live.board", _client=_client)
        self.board_id = board_id
        
        self.state = None
        self.topic = None
        self.user_id = None

    def apply_board_token(self, **params):
        _params = _transfer_params(params)
        return self._client.apply_board_token(board_id=self.board_id, **_params)

    def complete(self, **params):
        _params = _transfer_params(params)
        return self._client.complete_board(board_id=self.board_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_board(board_id=self.board_id, **_params)

    def describe_board_events(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_board_events(board_id=self.board_id, **_params)

    def describe_board_snapshot(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_board_snapshot(board_id=self.board_id, **_params)

    def start_board_record(self, **params):
        _params = _transfer_params(params)
        return self._client.start_board_record(board_id=self.board_id, **_params)

class _LIVECasterResource(ServiceResource):

    def __init__(self, caster_id, _client=None):
        ServiceResource.__init__(self, "live.caster", _client=_client)
        self.caster_id = caster_id
        
        self.caster_name = None
        self.caster_template = None
        self.channel_enable = None
        self.charge_type = None
        self.create_time = None
        self.expire_time = None
        self.norm_type = None
        self.purchase_time = None
        self.start_time = None
        self.status = None

        self.caster_components = _create_sub_resource_without_page_collection(
            _LIVECasterComponentResource, _client, _client.describe_caster_components,
            'Components.Component', 'ComponentId', parent_identifier="CasterId",parent_identifier_value=self.caster_id
        )
        self.caster_layouts = _create_sub_resource_without_page_collection(
            _LIVECasterLayoutResource, _client, _client.describe_caster_layouts,
            'Layouts.Layout', 'LayoutId', parent_identifier="CasterId",parent_identifier_value=self.caster_id
        )
    def add_caster_program(self, **params):
        _params = _transfer_params(params)
        return self._client.add_caster_program(caster_id=self.caster_id, **_params)

    def add_caster_video_resource(self, **params):
        _params = _transfer_params(params)
        return self._client.add_caster_video_resource(caster_id=self.caster_id, **_params)

    def copy_caster_scene_config(self, **params):
        _params = _transfer_params(params)
        return self._client.copy_caster_scene_config(caster_id=self.caster_id, **_params)

    def delete_caster_program(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_caster_program(caster_id=self.caster_id, **_params)

    def delete_caster_video_resource(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_caster_video_resource(caster_id=self.caster_id, **_params)

    def describe_caster_channels(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_caster_channels(caster_id=self.caster_id, **_params)

    def describe_caster_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_caster_config(caster_id=self.caster_id, **_params)

    def describe_caster_program(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_caster_program(caster_id=self.caster_id, **_params)

    def describe_caster_rtc_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_caster_rtc_info(caster_id=self.caster_id, **_params)

    def describe_caster_scene_audio(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_caster_scene_audio(caster_id=self.caster_id, **_params)

    def describe_caster_scenes(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_caster_scenes(caster_id=self.caster_id, **_params)

    def describe_caster_stream_url(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_caster_stream_url(caster_id=self.caster_id, **_params)

    def describe_caster_video_resources(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_caster_video_resources(caster_id=self.caster_id, **_params)

    def modify_program(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_caster_program(caster_id=self.caster_id, **_params)

    def modify_video_resource(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_caster_video_resource(caster_id=self.caster_id, **_params)

    def set_caster_config(self, **params):
        _params = _transfer_params(params)
        return self._client.set_caster_config(caster_id=self.caster_id, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        return self._client.start_caster(caster_id=self.caster_id, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_caster(caster_id=self.caster_id, **_params)

    def delete_caster_scene_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_caster_scene_config(caster_id=self.caster_id, **_params)

    def effect_caster_urgent(self, **params):
        _params = _transfer_params(params)
        return self._client.effect_caster_urgent(caster_id=self.caster_id, **_params)

    def effect_caster_video_resource(self, **params):
        _params = _transfer_params(params)
        return self._client.effect_caster_video_resource(caster_id=self.caster_id, **_params)

    def set_caster_channel(self, **params):
        _params = _transfer_params(params)
        return self._client.set_caster_channel(caster_id=self.caster_id, **_params)

    def set_caster_scene_config(self, **params):
        _params = _transfer_params(params)
        return self._client.set_caster_scene_config(caster_id=self.caster_id, **_params)

    def start_caster_scene(self, **params):
        _params = _transfer_params(params)
        return self._client.start_caster_scene(caster_id=self.caster_id, **_params)

    def stop_caster_scene(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_caster_scene(caster_id=self.caster_id, **_params)

    def update_caster_scene_audio(self, **params):
        _params = _transfer_params(params)
        return self._client.update_caster_scene_audio(caster_id=self.caster_id, **_params)

    def add_caster_component(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_caster_component(caster_id=self.caster_id,**_params)
        component_id = _new_get_key_in_response(response, 'ComponentId')
        return _LIVECasterComponentResource(component_id,self.caster_id, _client=self._client)

    def add_caster_episode(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_caster_episode(caster_id=self.caster_id,**_params)
        episode_id = _new_get_key_in_response(response, 'EpisodeId')
        return _LIVECasterEpisodeResource(episode_id,self.caster_id, _client=self._client)

    def add_caster_layout(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_caster_layout(caster_id=self.caster_id,**_params)
        layout_id = _new_get_key_in_response(response, 'LayoutId')
        return _LIVECasterLayoutResource(layout_id,self.caster_id, _client=self._client)

class _LIVECasterComponentResource(ServiceResource):

    def __init__(self, component_id,caster_id, _client=None):
        ServiceResource.__init__(self, "live.caster_component", _client=_client)
        self.component_id = component_id
        self.caster_id = caster_id
        self.caption_layer_content = None
        self.component_layer = None
        self.component_name = None
        self.component_type = None
        self.effect = None
        self.image_layer_content = None
        self.location_id = None
        self.text_layer_content = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_caster_component(component_id=self.component_id,caster_id=self.caster_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_caster_component(component_id=self.component_id,caster_id=self.caster_id, **_params)

class _LIVECasterEpisodeResource(ServiceResource):

    def __init__(self, episode_id,caster_id, _client=None):
        ServiceResource.__init__(self, "live.caster_episode", _client=_client)
        self.episode_id = episode_id
        self.caster_id = caster_id

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_caster_episode(episode_id=self.episode_id,caster_id=self.caster_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_caster_episode(episode_id=self.episode_id,caster_id=self.caster_id, **_params)

class _LIVECasterLayoutResource(ServiceResource):

    def __init__(self, layout_id,caster_id, _client=None):
        ServiceResource.__init__(self, "live.caster_layout", _client=_client)
        self.layout_id = layout_id
        self.caster_id = caster_id
        self.audio_layers = None
        self.blend_list = None
        self.mix_list = None
        self.video_layers = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_caster_layout(layout_id=self.layout_id,caster_id=self.caster_id, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_caster_layout(layout_id=self.layout_id,caster_id=self.caster_id, **_params)

    def update_caster_scene_config(self, **params):
        _params = _transfer_params(params)
        return self._client.update_caster_scene_config(layout_id=self.layout_id,caster_id=self.caster_id, **_params)

class _LIVECasterEpisodeGroupResource(ServiceResource):

    def __init__(self, program_id, _client=None):
        ServiceResource.__init__(self, "live.caster_episode_group", _client=_client)
        self.program_id = program_id
        

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_caster_episode_group(program_id=self.program_id, **_params)

class _LIVELiveDomainResource(ServiceResource):

    def __init__(self, live_domain_name, _client=None):
        ServiceResource.__init__(self, "live.live_domain", _client=_client)
        self.live_domain_name = live_domain_name
        

    def batch_delete_live_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_delete_live_domain_configs(live_domain_name=self.live_domain_name, **_params)

    def batch_set_live_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_set_live_domain_configs(live_domain_name=self.live_domain_name, **_params)

    def add_live_app_record_config(self, **params):
        _params = _transfer_params(params)
        return self._client.add_live_app_record_config(live_domain_name=self.live_domain_name, **_params)

    def add_live_app_snapshot_config(self, **params):
        _params = _transfer_params(params)
        return self._client.add_live_app_snapshot_config(live_domain_name=self.live_domain_name, **_params)

    def add_live_detect_notify_config(self, **params):
        _params = _transfer_params(params)
        return self._client.add_live_detect_notify_config(live_domain_name=self.live_domain_name, **_params)

    def add_live_pull_stream_info_config(self, **params):
        _params = _transfer_params(params)
        return self._client.add_live_pull_stream_info_config(live_domain_name=self.live_domain_name, **_params)

    def add_live_record_notify_config(self, **params):
        _params = _transfer_params(params)
        return self._client.add_live_record_notify_config(live_domain_name=self.live_domain_name, **_params)

    def add_live_record_vod_config(self, **params):
        _params = _transfer_params(params)
        return self._client.add_live_record_vod_config(live_domain_name=self.live_domain_name, **_params)

    def add_live_snapshot_detect_porn_config(self, **params):
        _params = _transfer_params(params)
        return self._client.add_live_snapshot_detect_porn_config(live_domain_name=self.live_domain_name, **_params)

    def add_trancode_sei(self, **params):
        _params = _transfer_params(params)
        return self._client.add_trancode_sei(live_domain_name=self.live_domain_name, **_params)

    def create_live_real_time_log_dery(self, **params):
        _params = _transfer_params(params)
        return self._client.create_live_real_time_log_delivery(live_domain_name=self.live_domain_name, **_params)

    def create_live_stream_record_index_files(self, **params):
        _params = _transfer_params(params)
        return self._client.create_live_stream_record_index_files(live_domain_name=self.live_domain_name, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_live_domain(live_domain_name=self.live_domain_name, **_params)

    def delete_live_app_record_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_live_app_record_config(live_domain_name=self.live_domain_name, **_params)

    def delete_live_app_snapshot_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_live_app_snapshot_config(live_domain_name=self.live_domain_name, **_params)

    def delete_live_detect_notify_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_live_detect_notify_config(live_domain_name=self.live_domain_name, **_params)

    def delete_live_lazy_pull_stream_info_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_live_lazy_pull_stream_info_config(live_domain_name=self.live_domain_name, **_params)

    def delete_live_pull_stream_info_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_live_pull_stream_info_config(live_domain_name=self.live_domain_name, **_params)

    def delete_live_realtime_log_dery(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_live_realtime_log_delivery(live_domain_name=self.live_domain_name, **_params)

    def delete_live_record_notify_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_live_record_notify_config(live_domain_name=self.live_domain_name, **_params)

    def delete_live_record_vod_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_live_record_vod_config(live_domain_name=self.live_domain_name, **_params)

    def delete_live_snapshot_detect_porn_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_live_snapshot_detect_porn_config(live_domain_name=self.live_domain_name, **_params)

    def delete_live_streams_notify_url_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_live_streams_notify_url_config(live_domain_name=self.live_domain_name, **_params)

    def describe_live_detect_notify_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_detect_notify_config(live_domain_name=self.live_domain_name, **_params)

    def describe_live_domain_bps_data_by_time_stamp(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_domain_bps_data_by_time_stamp(live_domain_name=self.live_domain_name, **_params)

    def describe_live_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_domain_configs(live_domain_name=self.live_domain_name, **_params)

    def describe_live_domain_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_domain_detail(live_domain_name=self.live_domain_name, **_params)

    def describe_live_domain_frame_rate_and_bit_rate_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_domain_frame_rate_and_bit_rate_data(live_domain_name=self.live_domain_name, **_params)

    def describe_live_domain_mapping(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_domain_mapping(live_domain_name=self.live_domain_name, **_params)

    def describe_live_domain_online_user_num(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_domain_online_user_num(live_domain_name=self.live_domain_name, **_params)

    def describe_live_domain_real_time_bps_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_domain_real_time_bps_data(live_domain_name=self.live_domain_name, **_params)

    def describe_live_domain_real_time_http_code_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_domain_real_time_http_code_data(live_domain_name=self.live_domain_name, **_params)

    def describe_live_domain_realtime_log_dery(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_domain_realtime_log_delivery(live_domain_name=self.live_domain_name, **_params)

    def describe_live_lazy_pull_stream_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_lazy_pull_stream_config(live_domain_name=self.live_domain_name, **_params)

    def describe_live_pull_stream_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_pull_stream_config(live_domain_name=self.live_domain_name, **_params)

    def describe_live_record_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_record_config(live_domain_name=self.live_domain_name, **_params)

    def describe_live_record_notify_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_record_notify_config(live_domain_name=self.live_domain_name, **_params)

    def describe_live_record_vod_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_record_vod_configs(live_domain_name=self.live_domain_name, **_params)

    def describe_live_snapshot_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_snapshot_config(live_domain_name=self.live_domain_name, **_params)

    def describe_live_snapshot_detect_porn_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_snapshot_detect_porn_config(live_domain_name=self.live_domain_name, **_params)

    def describe_live_stream_bit_rate_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_stream_bit_rate_data(live_domain_name=self.live_domain_name, **_params)

    def describe_live_stream_count(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_stream_count(live_domain_name=self.live_domain_name, **_params)

    def describe_live_stream_delay_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_stream_delay_config(live_domain_name=self.live_domain_name, **_params)

    def describe_live_stream_history_user_num(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_stream_history_user_num(live_domain_name=self.live_domain_name, **_params)

    def describe_live_stream_online_user_num(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_stream_online_user_num(live_domain_name=self.live_domain_name, **_params)

    def describe_live_stream_optimized_feature_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_stream_optimized_feature_config(live_domain_name=self.live_domain_name, **_params)

    def describe_live_stream_record_content(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_stream_record_content(live_domain_name=self.live_domain_name, **_params)

    def describe_live_stream_record_index_file(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_stream_record_index_file(live_domain_name=self.live_domain_name, **_params)

    def describe_live_stream_record_index_files(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_stream_record_index_files(live_domain_name=self.live_domain_name, **_params)

    def describe_live_stream_snapshot_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_stream_snapshot_info(live_domain_name=self.live_domain_name, **_params)

    def describe_live_stream_transcode_stream_num(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_stream_transcode_stream_num(live_domain_name=self.live_domain_name, **_params)

    def describe_live_streams_block_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_streams_block_list(live_domain_name=self.live_domain_name, **_params)

    def describe_live_streams_control_history(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_streams_control_history(live_domain_name=self.live_domain_name, **_params)

    def describe_live_streams_frame_rate_and_bit_rate_data(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_streams_frame_rate_and_bit_rate_data(live_domain_name=self.live_domain_name, **_params)

    def describe_live_streams_notify_url_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_streams_notify_url_config(live_domain_name=self.live_domain_name, **_params)

    def describe_live_streams_online_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_streams_online_list(live_domain_name=self.live_domain_name, **_params)

    def describe_live_streams_publish_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_live_streams_publish_list(live_domain_name=self.live_domain_name, **_params)

    def disable_live_realtime_log_dery(self, **params):
        _params = _transfer_params(params)
        return self._client.disable_live_realtime_log_delivery(live_domain_name=self.live_domain_name, **_params)

    def enable_live_realtime_log_dery(self, **params):
        _params = _transfer_params(params)
        return self._client.enable_live_realtime_log_delivery(live_domain_name=self.live_domain_name, **_params)

    def forbid_live_stream(self, **params):
        _params = _transfer_params(params)
        return self._client.forbid_live_stream(live_domain_name=self.live_domain_name, **_params)

    def modify_live_realtime_log_dery(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_live_realtime_log_delivery(live_domain_name=self.live_domain_name, **_params)

    def modify_schdm_by_property(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_live_domain_schdm_by_property(live_domain_name=self.live_domain_name, **_params)

    def real_time_record_command(self, **params):
        _params = _transfer_params(params)
        return self._client.real_time_record_command(live_domain_name=self.live_domain_name, **_params)

    def real_time_snapshot_command(self, **params):
        _params = _transfer_params(params)
        return self._client.real_time_snapshot_command(live_domain_name=self.live_domain_name, **_params)

    def resume_live_stream(self, **params):
        _params = _transfer_params(params)
        return self._client.resume_live_stream(live_domain_name=self.live_domain_name, **_params)

    def set_live_domain_certificate(self, **params):
        _params = _transfer_params(params)
        return self._client.set_live_domain_certificate(live_domain_name=self.live_domain_name, **_params)

    def set_live_lazy_pull_stream_info_config(self, **params):
        _params = _transfer_params(params)
        return self._client.set_live_lazy_pull_stream_info_config(live_domain_name=self.live_domain_name, **_params)

    def set_live_stream_delay_config(self, **params):
        _params = _transfer_params(params)
        return self._client.set_live_stream_delay_config(live_domain_name=self.live_domain_name, **_params)

    def set_live_stream_optimized_feature_config(self, **params):
        _params = _transfer_params(params)
        return self._client.set_live_stream_optimized_feature_config(live_domain_name=self.live_domain_name, **_params)

    def set_live_streams_notify_url_config(self, **params):
        _params = _transfer_params(params)
        return self._client.set_live_streams_notify_url_config(live_domain_name=self.live_domain_name, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        return self._client.start_live_domain(live_domain_name=self.live_domain_name, **_params)

    def start_live_index(self, **params):
        _params = _transfer_params(params)
        return self._client.start_live_index(live_domain_name=self.live_domain_name, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_live_domain(live_domain_name=self.live_domain_name, **_params)

    def stop_live_index(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_live_index(live_domain_name=self.live_domain_name, **_params)

    def update_live_app_snapshot_config(self, **params):
        _params = _transfer_params(params)
        return self._client.update_live_app_snapshot_config(live_domain_name=self.live_domain_name, **_params)

    def update_live_detect_notify_config(self, **params):
        _params = _transfer_params(params)
        return self._client.update_live_detect_notify_config(live_domain_name=self.live_domain_name, **_params)

    def update_live_record_notify_config(self, **params):
        _params = _transfer_params(params)
        return self._client.update_live_record_notify_config(live_domain_name=self.live_domain_name, **_params)

    def update_live_snapshot_detect_porn_config(self, **params):
        _params = _transfer_params(params)
        return self._client.update_live_snapshot_detect_porn_config(live_domain_name=self.live_domain_name, **_params)

    def update_live_top_level_domain(self, **params):
        _params = _transfer_params(params)
        return self._client.update_live_top_level_domain(live_domain_name=self.live_domain_name, **_params)

class _LIVERecordResource(ServiceResource):

    def __init__(self, record_id, _client=None):
        ServiceResource.__init__(self, "live.record", _client=_client)
        self.record_id = record_id
        
        self.app_id = None
        self.board_id = None
        self.end_time = None
        self.oss_bucket = None
        self.oss_endpoint = None
        self.oss_path = None
        self.record_start_time = None
        self.start_time = None
        self.state = None

    def complete_board(self, **params):
        _params = _transfer_params(params)
        return self._client.complete_board_record(record_id=self.record_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_record(record_id=self.record_id, **_params)

class _LIVERoomResource(ServiceResource):

    def __init__(self, room_id, _client=None):
        ServiceResource.__init__(self, "live.room", _client=_client)
        self.room_id = room_id
        

    def allow_push_stream(self, **params):
        _params = _transfer_params(params)
        return self._client.allow_push_stream(room_id=self.room_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_room(room_id=self.room_id, **_params)

    def describe_room_kickout_user_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_room_kickout_user_list(room_id=self.room_id, **_params)

    def describe_room_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_room_status(room_id=self.room_id, **_params)

    def forbid_push_stream(self, **params):
        _params = _transfer_params(params)
        return self._client.forbid_push_stream(room_id=self.room_id, **_params)

    def send_room_notification(self, **params):
        _params = _transfer_params(params)
        return self._client.send_room_notification(room_id=self.room_id, **_params)

    def send_room_user_notification(self, **params):
        _params = _transfer_params(params)
        return self._client.send_room_user_notification(room_id=self.room_id, **_params)
