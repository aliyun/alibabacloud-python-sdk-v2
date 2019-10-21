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


class _IMMResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'imm', _client=_client)
        self.porn_batch_detect_jobs = _create_special_resource_collection(
            _IMMPornBatchDetectJobResource, _client, _client.list_porn_batch_detect_jobs,
            'Jobs.Jobs', 'JobId', 
        )
    def create_cad_conversion_task(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_cad_conversion_task(**_params)
        task_id = _new_get_key_in_response(response, 'TaskId')
        return _IMMCADConversionTaskResource(task_id, _client=self._client)

    def create_porn_batch_detect_job(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_porn_batch_detect_job(**_params)
        job_id = _new_get_key_in_response(response, 'JobId')
        return _IMMPornBatchDetectJobResource(job_id, _client=self._client)

    def get_porn_batch_detect_job(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_porn_batch_detect_job(**_params)
        job_id = _new_get_key_in_response(response, 'JobId')
        return _IMMPornBatchDetectJobResource(job_id, _client=self._client)

class _IMMCADConversionTaskResource(ServiceResource):

    def __init__(self, task_id, _client=None):
        ServiceResource.__init__(self, "imm.cad_conversion_task", _client=_client)
        self.task_id = task_id
        

    def delete_office_conversion_task(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_office_conversion_task(task_id=self.task_id, **_params)

    def delete_photo_process_task(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_photo_process_task(task_id=self.task_id, **_params)

    def delete_video_task(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_video_task(task_id=self.task_id, **_params)

    def get_doc_index_task(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_doc_index_task(task_id=self.task_id, **_params)
        return response

    def get_office_conversion_task(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_office_conversion_task(task_id=self.task_id, **_params)
        return response

    def get_photo_process_task(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_photo_process_task(task_id=self.task_id, **_params)
        return response

    def get_video_task(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_video_task(task_id=self.task_id, **_params)
        return response

class _IMMPornBatchDetectJobResource(ServiceResource):

    def __init__(self, job_id, _client=None):
        ServiceResource.__init__(self, "imm.porn_batch_detect_job", _client=_client)
        self.job_id = job_id
        
        self.create_time = None
        self.external_id = None
        self.finish_time = None
        self.notify_endpoint = None
        self.notify_topic_name = None
        self.percent = None
        self.src_uri = None
        self.status = None
        self.tgt_uri = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_porn_batch_detect_job(job_id=self.job_id, **_params)

    def delete_face_job(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_face_job(job_id=self.job_id, **_params)

    def delete_image_job(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_image_job(job_id=self.job_id, **_params)

    def delete_tag_job(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_tag_job(job_id=self.job_id, **_params)

    def get_image_job(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_image_job(job_id=self.job_id, **_params)
        return response

    def get_tag_job(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_tag_job(job_id=self.job_id, **_params)
        return response
