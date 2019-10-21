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


class _VODResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'vod', _client=_client)
        self.ai_templates = _create_special_resource_collection(
            _VODAITemplateResource, _client, _client.list_ai_template,
            'TemplateInfoList.TemplateInfoList', 'TemplateId', 
        )
        self.app_infos = _create_special_resource_collection(
            _VODAppInfoResource, _client, _client.list_app_info,
            'AppInfoList.AppInfo', 'AppId', 
        )
        self.transcode_tasks = _create_special_resource_collection(
            _VODTranscodeTaskResource, _client, _client.list_transcode_task,
            'TranscodeTaskList.TranscodeTask', 'TranscodeTaskId', 
        )
        self.transcode_template_groups = _create_special_resource_collection(
            _VODTranscodeTemplateGroupResource, _client, _client.list_transcode_template_group,
            'TranscodeTemplateGroupList.TranscodeTemplateGroup', 'TranscodeTemplateGroupId', 
        )
        self.vod_templates = _create_special_resource_collection(
            _VODVodTemplateResource, _client, _client.list_vod_template,
            'VodTemplateInfoList.VodTemplateInfo', 'VodTemplateId', 
        )
        self.watermarks = _create_special_resource_collection(
            _VODWatermarkResource, _client, _client.list_watermark,
            'WatermarkInfos.WatermarkInfo', 'WatermarkId', 
        )
    def add_ai_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_ai_template(**_params)
        template_id = _new_get_key_in_response(response, 'TemplateId')
        return _VODAITemplateResource(template_id, _client=self._client)

    def delete_ai_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_ai_template(**_params)
        template_id = _new_get_key_in_response(response, 'TemplateId')
        return _VODAITemplateResource(template_id, _client=self._client)

    def update_ai_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_ai_template(**_params)
        template_id = _new_get_key_in_response(response, 'TemplateId')
        return _VODAITemplateResource(template_id, _client=self._client)

    def create_app_info(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_app_info(**_params)
        app_id = _new_get_key_in_response(response, 'AppId')
        return _VODAppInfoResource(app_id, _client=self._client)

    def add_category(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_category(**_params)
        cate_id = _new_get_key_in_response(response, 'CateId')
        return _VODCategoryResource(cate_id, _client=self._client)

    def add_editing_project(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_editing_project(**_params)
        project_id = _new_get_key_in_response(response, 'ProjectId')
        return _VODEditingProjectResource(project_id, _client=self._client)

    def get_editing_project(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_editing_project(**_params)
        project_id = _new_get_key_in_response(response, 'ProjectId')
        return _VODEditingProjectResource(project_id, _client=self._client)

    def search_editing_project(self, **params):
        _params = _transfer_params(params)
        response = self._client.search_editing_project(**_params)
        project_ids = _new_get_key_in_response(response, 'None')
        editing_projects = []
        for project_id in project_ids:
            editing_project = _VODEditingProjectResource(project_id, _client=self._client)
            editing_projects.append(editing_project)
        return editing_projects

    def add_transcode_template_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_transcode_template_group(**_params)
        transcode_template_group_id = _new_get_key_in_response(response, 'TranscodeTemplateGroupId')
        return _VODTranscodeTemplateGroupResource(transcode_template_group_id, _client=self._client)

    def update_transcode_template_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_transcode_template_group(**_params)
        transcode_template_group_id = _new_get_key_in_response(response, 'TranscodeTemplateGroupId')
        return _VODTranscodeTemplateGroupResource(transcode_template_group_id, _client=self._client)

    def create_upload_attached_media(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_upload_attached_media(**_params)
        media_id = _new_get_key_in_response(response, 'MediaId')
        return _VODUploadAttachedMediaResource(media_id, _client=self._client)

    def add_vod_domain(self, **params):
        _params = _transfer_params(params)
        self._client.add_vod_domain(**_params)
        vod_domain_name = _params.get("vod_domain_name")
        return _VODVodDomainResource(vod_domain_name, _client=self._client)

    def add_vod_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_vod_template(**_params)
        vod_template_id = _new_get_key_in_response(response, 'VodTemplateId')
        return _VODVodTemplateResource(vod_template_id, _client=self._client)

    def delete_vod_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_vod_template(**_params)
        vod_template_id = _new_get_key_in_response(response, 'VodTemplateId')
        return _VODVodTemplateResource(vod_template_id, _client=self._client)

    def get_vod_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_vod_template(**_params)
        vod_template_id = _new_get_key_in_response(response, 'VodTemplateId')
        return _VODVodTemplateResource(vod_template_id, _client=self._client)

    def update_vod_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_vod_template(**_params)
        vod_template_id = _new_get_key_in_response(response, 'VodTemplateId')
        return _VODVodTemplateResource(vod_template_id, _client=self._client)

    def add_watermark(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_watermark(**_params)
        watermark_id = _new_get_key_in_response(response, 'WatermarkId')
        return _VODWatermarkResource(watermark_id, _client=self._client)

    def update_watermark(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_watermark(**_params)
        watermark_id = _new_get_key_in_response(response, 'WatermarkId')
        return _VODWatermarkResource(watermark_id, _client=self._client)

class _VODAITemplateResource(ServiceResource):

    def __init__(self, template_id, _client=None):
        ServiceResource.__init__(self, "vod.ai_template", _client=_client)
        self.template_id = template_id
        
        self.creation_time = None
        self.is_default = None
        self.modify_time = None
        self.source = None
        self.template_config = None
        self.template_name = None
        self.template_type = None

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_ai_template(template_id=self.template_id, **_params)

    def set_default(self, **params):
        _params = _transfer_params(params)
        return self._client.set_default_ai_template(template_id=self.template_id, **_params)

class _VODAppInfoResource(ServiceResource):

    def __init__(self, app_id, _client=None):
        ServiceResource.__init__(self, "vod.app_info", _client=_client)
        self.app_id = app_id
        
        self.app_name = None
        self.creation_time = None
        self.description = None
        self.modification_time = None
        self.status = None
        self.type_ = None

class _VODCategoryResource(ServiceResource):

    def __init__(self, cate_id, _client=None):
        ServiceResource.__init__(self, "vod.category", _client=_client)
        self.cate_id = cate_id
        

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_category(cate_id=self.cate_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_category(cate_id=self.cate_id, **_params)

class _VODEditingProjectResource(ServiceResource):

    def __init__(self, project_id, _client=None):
        ServiceResource.__init__(self, "vod.editing_project", _client=_client)
        self.project_id = project_id
        

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_editing_project(project_id=self.project_id, **_params)

    def get_editing_project_materials(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_editing_project_materials(project_id=self.project_id, **_params)
        return response

    def set_editing_project_materials(self, **params):
        _params = _transfer_params(params)
        return self._client.set_editing_project_materials(project_id=self.project_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_editing_project(project_id=self.project_id, **_params)

class _VODTranscodeTaskResource(ServiceResource):

    def __init__(self, transcode_task_id, _client=None):
        ServiceResource.__init__(self, "vod.transcode_task", _client=_client)
        self.transcode_task_id = transcode_task_id
        
        self.complete_time = None
        self.creation_time = None
        self.task_status = None
        self.transcode_template_group_id = None
        self.trigger = None
        self.video_id = None

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_transcode_task(transcode_task_id=self.transcode_task_id, **_params)

class _VODTranscodeTemplateGroupResource(ServiceResource):

    def __init__(self, transcode_template_group_id, _client=None):
        ServiceResource.__init__(self, "vod.transcode_template_group", _client=_client)
        self.transcode_template_group_id = transcode_template_group_id
        
        self.app_id = None
        self.creation_time = None
        self.is_default = None
        self.locked = None
        self.modify_time = None
        self.name = None
        self.transcode_mode = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_transcode_template_group(transcode_template_group_id=self.transcode_template_group_id, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_transcode_template_group(transcode_template_group_id=self.transcode_template_group_id, **_params)

    def set_default(self, **params):
        _params = _transfer_params(params)
        return self._client.set_default_transcode_template_group(transcode_template_group_id=self.transcode_template_group_id, **_params)

class _VODUploadAttachedMediaResource(ServiceResource):

    def __init__(self, media_id, _client=None):
        ServiceResource.__init__(self, "vod.upload_attached_media", _client=_client)
        self.media_id = media_id
        

    def delete_multipart_upload(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_multipart_upload(media_id=self.media_id, **_params)

    def get_ai_video_tag_result(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_ai_video_tag_result(media_id=self.media_id, **_params)
        return response

    def get_media_audit_result(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_media_audit_result(media_id=self.media_id, **_params)
        return response

    def get_media_audit_result_detail(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_media_audit_result_detail(media_id=self.media_id, **_params)
        return response

    def get_media_audit_result_timeline(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_media_audit_result_timeline(media_id=self.media_id, **_params)
        return response

    def get_media_dna_result(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_media_dna_result(media_id=self.media_id, **_params)
        return response

    def submit_ai_media_audit_job(self, **params):
        _params = _transfer_params(params)
        return self._client.submit_ai_media_audit_job(media_id=self.media_id, **_params)

class _VODVodDomainResource(ServiceResource):

    def __init__(self, vod_domain_name, _client=None):
        ServiceResource.__init__(self, "vod.vod_domain", _client=_client)
        self.vod_domain_name = vod_domain_name
        

    def batch_set_vod_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_set_vod_domain_configs(vod_domain_name=self.vod_domain_name, **_params)

    def batch_start(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_start_vod_domain(vod_domain_name=self.vod_domain_name, **_params)

    def batch_stop(self, **params):
        _params = _transfer_params(params)
        return self._client.batch_stop_vod_domain(vod_domain_name=self.vod_domain_name, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_vod_domain(vod_domain_name=self.vod_domain_name, **_params)

    def delete_vod_specific_config(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_vod_specific_config(vod_domain_name=self.vod_domain_name, **_params)

    def describe_vod_domain_certificate_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_vod_domain_certificate_info(vod_domain_name=self.vod_domain_name, **_params)

    def describe_vod_domain_configs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_vod_domain_configs(vod_domain_name=self.vod_domain_name, **_params)

    def describe_vod_domain_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_vod_domain_detail(vod_domain_name=self.vod_domain_name, **_params)

    def describe_vod_domain_log(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_vod_domain_log(vod_domain_name=self.vod_domain_name, **_params)

    def modify_schdm_by_property(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_vod_domain_schdm_by_property(vod_domain_name=self.vod_domain_name, **_params)

    def set_vod_domain_certificate(self, **params):
        _params = _transfer_params(params)
        return self._client.set_vod_domain_certificate(vod_domain_name=self.vod_domain_name, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_vod_domain(vod_domain_name=self.vod_domain_name, **_params)

class _VODVodTemplateResource(ServiceResource):

    def __init__(self, vod_template_id, _client=None):
        ServiceResource.__init__(self, "vod.vod_template", _client=_client)
        self.vod_template_id = vod_template_id
        
        self.app_id = None
        self.creation_time = None
        self.is_default = None
        self.modify_time = None
        self.name = None
        self.source = None
        self.sub_template_type = None
        self.template_config = None
        self.template_type = None

class _VODWatermarkResource(ServiceResource):

    def __init__(self, watermark_id, _client=None):
        ServiceResource.__init__(self, "vod.watermark", _client=_client)
        self.watermark_id = watermark_id
        
        self.app_id = None
        self.creation_time = None
        self.file_url = None
        self.is_default = None
        self.name = None
        self.type_ = None
        self.watermark_config = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_watermark(watermark_id=self.watermark_id, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_watermark(watermark_id=self.watermark_id, **_params)

    def set_default(self, **params):
        _params = _transfer_params(params)
        return self._client.set_default_watermark(watermark_id=self.watermark_id, **_params)
