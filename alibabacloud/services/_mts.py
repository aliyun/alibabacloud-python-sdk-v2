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

from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, \
    _create_special_resource_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _MTSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'mts', _client=_client)
        self.jobs = _create_special_resource_collection(
            _MTSJobResource, _client, _client.list_job,
            'JobList.Job', 'JobId',
        )
        self.medias = _create_special_resource_collection(
            _MTSMediaResource, _client, _client.search_media,
            'MediaList.Media', 'MediaId',
        )
        self.medias = _create_special_resource_collection(
            _MTSMediaResource, _client, _client.search_media,
            'MediaList.Media', 'MediaId',
        )
        self.media_workflows = _create_resource_collection(
            _MTSMediaWorkflowResource, _client, _client.search_media_workflow,
            'MediaWorkflowList.MediaWorkflow', 'MediaWorkflowId',
        )

    def add_category(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_category(**_params)
        cate_id = _new_get_key_in_response(response, 'CateId')
        return _MTSCategoryResource(cate_id, _client=self._client)

    def cancel_job(self, **params):
        _params = _transfer_params(params)
        response = self._client.cancel_job(**_params)
        job_id = _new_get_key_in_response(response, 'JobId')
        return _MTSJobResource(job_id, _client=self._client)

    def add_media(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_media(**_params)
        media_id = _new_get_key_in_response(response, 'MediaId')
        return _MTSMediaResource(media_id, _client=self._client)

    def activate_media_workflow(self, **params):
        _params = _transfer_params(params)
        response = self._client.activate_media_workflow(**_params)
        media_workflow_id = _new_get_key_in_response(response, 'MediaWorkflowId')
        return _MTSMediaWorkflowResource(media_workflow_id, _client=self._client)

    def add_media_workflow(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_media_workflow(**_params)
        media_workflow_id = _new_get_key_in_response(response, 'MediaWorkflowId')
        return _MTSMediaWorkflowResource(media_workflow_id, _client=self._client)

    def deactivate_media_workflow(self, **params):
        _params = _transfer_params(params)
        response = self._client.deactivate_media_workflow(**_params)
        media_workflow_id = _new_get_key_in_response(response, 'MediaWorkflowId')
        return _MTSMediaWorkflowResource(media_workflow_id, _client=self._client)

    def delete_media_workflow(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_media_workflow(**_params)
        media_workflow_id = _new_get_key_in_response(response, 'MediaWorkflowId')
        return _MTSMediaWorkflowResource(media_workflow_id, _client=self._client)

    def update_media_workflow(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_media_workflow(**_params)
        media_workflow_id = _new_get_key_in_response(response, 'MediaWorkflowId')
        return _MTSMediaWorkflowResource(media_workflow_id, _client=self._client)

    def delete_pipeline(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_pipeline(**_params)
        pipeline_id = _new_get_key_in_response(response, 'PipelineId')
        return _MTSPipelineResource(pipeline_id, _client=self._client)

    def create_session(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_session(**_params)
        session_id = _new_get_key_in_response(response, 'SessionId')
        return _MTSSessionResource(session_id, _client=self._client)

    def delete_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_template(**_params)
        template_id = _new_get_key_in_response(response, 'TemplateId')
        return _MTSTemplateResource(template_id, _client=self._client)

    def delete_water_mark_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_water_mark_template(**_params)
        water_mark_template_id = _new_get_key_in_response(response, 'WaterMarkTemplateId')
        return _MTSWaterMarkTemplateResource(water_mark_template_id, _client=self._client)


class _MTSCategoryResource(ServiceResource):

    def __init__(self, cate_id, _client=None):
        ServiceResource.__init__(self, "mts.category", _client=_client)
        self.cate_id = cate_id

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_category(cate_id=self.cate_id, **_params)

    def update_category_name(self, **params):
        _params = _transfer_params(params)
        return self._client.update_category_name(cate_id=self.cate_id, **_params)


class _MTSJobResource(ServiceResource):

    def __init__(self, job_id, _client=None):
        ServiceResource.__init__(self, "mts.job", _client=_client)
        self.job_id = job_id

        self.code = None
        self.creation_time = None
        self.finish_time = None
        self.input = None
        self.mns_message_result = None
        self.message = None
        self.output = None
        self.percent = None
        self.pipeline_id = None
        self.state = None

    def delete_mcu(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_mcu_job(job_id=self.job_id, **_params)

    def query_media_censor_job_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.query_media_censor_job_detail(job_id=self.job_id, **_params)

    def register_media_detail_scenario(self, **params):
        _params = _transfer_params(params)
        return self._client.register_media_detail_scenario(job_id=self.job_id, **_params)

    def report_annotation_job_result(self, **params):
        _params = _transfer_params(params)
        return self._client.report_annotation_job_result(job_id=self.job_id, **_params)

    def report_censor_job_result(self, **params):
        _params = _transfer_params(params)
        return self._client.report_censor_job_result(job_id=self.job_id, **_params)

    def report_cover_job_result(self, **params):
        _params = _transfer_params(params)
        return self._client.report_cover_job_result(job_id=self.job_id, **_params)

    def report_facerecog_job_result(self, **params):
        _params = _transfer_params(params)
        return self._client.report_facerecog_job_result(job_id=self.job_id, **_params)

    def report_fp_shot_job_result(self, **params):
        _params = _transfer_params(params)
        return self._client.report_fp_shot_job_result(job_id=self.job_id, **_params)

    def report_media_detail_job_result(self, **params):
        _params = _transfer_params(params)
        return self._client.report_media_detail_job_result(job_id=self.job_id, **_params)

    def report_porn_job_result(self, **params):
        _params = _transfer_params(params)
        return self._client.report_porn_job_result(job_id=self.job_id, **_params)

    def report_tag_job_result(self, **params):
        _params = _transfer_params(params)
        return self._client.report_tag_job_result(job_id=self.job_id, **_params)

    def report_terrorism_job_result(self, **params):
        _params = _transfer_params(params)
        return self._client.report_terrorism_job_result(job_id=self.job_id, **_params)

    def report_video_split_job_result(self, **params):
        _params = _transfer_params(params)
        return self._client.report_video_split_job_result(job_id=self.job_id, **_params)


class _MTSMediaResource(ServiceResource):

    def __init__(self, media_id, _client=None):
        ServiceResource.__init__(self, "mts.media", _client=_client)
        self.media_id = media_id

        self.bitrate = None
        self.cate_id = None
        self.censor_state = None
        self.cover_url = None
        self.creation_time = None
        self.description = None
        self.duration = None
        self.file = None
        self.format = None
        self.fps = None
        self.height = None
        self.publish_state = None
        self.run_id_list = None
        self.size = None
        self.tags = None
        self.title = None
        self.width = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_media(media_id=self.media_id, **_params)

    def add_media_tag(self, **params):
        _params = _transfer_params(params)
        return self._client.add_media_tag(media_id=self.media_id, **_params)

    def delete_media_tag(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_media_tag(media_id=self.media_id, **_params)

    def get_license(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_license(media_id=self.media_id, **_params)
        return response

    def play_info(self, **params):
        _params = _transfer_params(params)
        return self._client.play_info(media_id=self.media_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_media(media_id=self.media_id, **_params)

    def update_media_category(self, **params):
        _params = _transfer_params(params)
        return self._client.update_media_category(media_id=self.media_id, **_params)

    def update_media_cover(self, **params):
        _params = _transfer_params(params)
        return self._client.update_media_cover(media_id=self.media_id, **_params)

    def update_media_publish_state(self, **params):
        _params = _transfer_params(params)
        return self._client.update_media_publish_state(media_id=self.media_id, **_params)


class _MTSMediaWorkflowResource(ServiceResource):

    def __init__(self, media_workflow_id, _client=None):
        ServiceResource.__init__(self, "mts.media_workflow", _client=_client)
        self.media_workflow_id = media_workflow_id

        self.creation_time = None
        self.name = None
        self.state = None
        self.topology = None
        self.trigger_mode = None

    def update_media_workflow_trigger_mode(self, **params):
        _params = _transfer_params(params)
        return self._client.update_media_workflow_trigger_mode(
            media_workflow_id=self.media_workflow_id, **_params)


class _MTSPipelineResource(ServiceResource):

    def __init__(self, pipeline_id, _client=None):
        ServiceResource.__init__(self, "mts.pipeline", _client=_client)
        self.pipeline_id = pipeline_id

    def query_asr_pipeline_list(self, **params):
        _params = _transfer_params(params)
        return self._client.query_asr_pipeline_list(pipeline_id=self.pipeline_id, **_params)

    def query_censor_pipeline_list(self, **params):
        _params = _transfer_params(params)
        return self._client.query_censor_pipeline_list(pipeline_id=self.pipeline_id, **_params)

    def query_cover_pipeline_list(self, **params):
        _params = _transfer_params(params)
        return self._client.query_cover_pipeline_list(pipeline_id=self.pipeline_id, **_params)

    def query_pipeline_list(self, **params):
        _params = _transfer_params(params)
        return self._client.query_pipeline_list(pipeline_id=self.pipeline_id, **_params)

    def query_porn_pipeline_list(self, **params):
        _params = _transfer_params(params)
        return self._client.query_porn_pipeline_list(pipeline_id=self.pipeline_id, **_params)

    def query_terrorism_pipeline_list(self, **params):
        _params = _transfer_params(params)
        return self._client.query_terrorism_pipeline_list(pipeline_id=self.pipeline_id, **_params)

    def submit_analysis_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_analysis_job(pipeline_id=self.pipeline_id, **_params)

    def submit_annotation_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_annotation_job(pipeline_id=self.pipeline_id, **_params)

    def submit_asr_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_asr_job(pipeline_id=self.pipeline_id, **_params)

    def submit_complex_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_complex_job(pipeline_id=self.pipeline_id, **_params)

    def submit_cover_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_cover_job(pipeline_id=self.pipeline_id, **_params)

    def submit_editing_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_editing_jobs(pipeline_id=self.pipeline_id, **_params)

    def submit_facerecog_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_facerecog_job(pipeline_id=self.pipeline_id, **_params)

    def submit_fp_compare_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_fp_compare_job(pipeline_id=self.pipeline_id, **_params)

    def submit_fp_shot_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_fp_shot_job(pipeline_id=self.pipeline_id, **_params)

    def submit_image_search_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_image_search_job(pipeline_id=self.pipeline_id, **_params)

    def submit_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_jobs(pipeline_id=self.pipeline_id, **_params)

    def submit_mc_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_mc_job(pipeline_id=self.pipeline_id, **_params)

    def submit_mcu_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_mcu_job(pipeline_id=self.pipeline_id, **_params)

    def submit_media_censor_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_media_censor_job(pipeline_id=self.pipeline_id, **_params)

    def submit_media_detail_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_media_detail_job(pipeline_id=self.pipeline_id, **_params)

    def submit_media_fp_delete_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_media_fp_delete_job(pipeline_id=self.pipeline_id, **_params)

    def submit_porn_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_porn_job(pipeline_id=self.pipeline_id, **_params)

    def submit_subtitle_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_subtitle_job(pipeline_id=self.pipeline_id, **_params)

    def submit_tag_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_tag_job(pipeline_id=self.pipeline_id, **_params)

    def submit_terrorism_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_terrorism_job(pipeline_id=self.pipeline_id, **_params)

    def submit_video_gif_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_video_gif_job(pipeline_id=self.pipeline_id, **_params)

    def submit_video_pose_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_video_pose_job(pipeline_id=self.pipeline_id, **_params)

    def submit_video_split_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_video_split_job(pipeline_id=self.pipeline_id, **_params)

    def submit_video_summary_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_video_summary_job(pipeline_id=self.pipeline_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_pipeline(pipeline_id=self.pipeline_id, **_params)

    def update_asr(self, **params):
        _params = _transfer_params(params)
        return self._client.update_asr_pipeline(pipeline_id=self.pipeline_id, **_params)

    def update_censor(self, **params):
        _params = _transfer_params(params)
        return self._client.update_censor_pipeline(pipeline_id=self.pipeline_id, **_params)

    def update_cover(self, **params):
        _params = _transfer_params(params)
        return self._client.update_cover_pipeline(pipeline_id=self.pipeline_id, **_params)

    def update_porn(self, **params):
        _params = _transfer_params(params)
        return self._client.update_porn_pipeline(pipeline_id=self.pipeline_id, **_params)

    def update_terrorism(self, **params):
        _params = _transfer_params(params)
        return self._client.update_terrorism_pipeline(pipeline_id=self.pipeline_id, **_params)


class _MTSSessionResource(ServiceResource):

    def __init__(self, session_id, _client=None):
        ServiceResource.__init__(self, "mts.session", _client=_client)
        self.session_id = session_id


class _MTSTemplateResource(ServiceResource):

    def __init__(self, template_id, _client=None):
        ServiceResource.__init__(self, "mts.template", _client=_client)
        self.template_id = template_id

    def query_template_list(self, **params):
        _params = _transfer_params(params)
        return self._client.query_template_list(template_id=self.template_id, **_params)

    def delete_mc(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_mc_template(template_id=self.template_id, **_params)

    def delete_mcu(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_mcu_template(template_id=self.template_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_template(template_id=self.template_id, **_params)

    def update_mc(self, **params):
        _params = _transfer_params(params)
        return self._client.update_mc_template(template_id=self.template_id, **_params)

    def update_mcu(self, **params):
        _params = _transfer_params(params)
        return self._client.update_mcu_template(template_id=self.template_id, **_params)


class _MTSWaterMarkTemplateResource(ServiceResource):

    def __init__(self, water_mark_template_id, _client=None):
        ServiceResource.__init__(self, "mts.water_mark_template", _client=_client)
        self.water_mark_template_id = water_mark_template_id

    def query_water_mark_template_list(self, **params):
        _params = _transfer_params(params)
        return self._client.query_water_mark_template_list(
            water_mark_template_id=self.water_mark_template_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_water_mark_template(
            water_mark_template_id=self.water_mark_template_id, **_params)
