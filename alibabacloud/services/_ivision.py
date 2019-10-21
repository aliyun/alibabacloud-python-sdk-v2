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


class _IVISIONResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ivision', _client=_client)
        self.predict_datases = _create_special_resource_collection(
            _IVISIONPredictDatasResource, _client, _client.describe_predict_datas,
            'PredictDatas.PredictData', 'DataId', 
        )
        self.predict_models = _create_special_resource_collection(
            _IVISIONPredictModelResource, _client, _client.describe_predict_models,
            'Models.Model', 'ModelId', 
        )
        self.predict_templates = _create_special_resource_collection(
            _IVISIONPredictTemplateResource, _client, _client.describe_predict_templates,
            'Templates.Template', 'TemplateId', 
        )
        self.projects = _create_special_resource_collection(
            _IVISIONProjectResource, _client, _client.describe_projects,
            'Projects.Project', 'ProjectId', 
        )
        self.stream_predicts = _create_special_resource_collection(
            _IVISIONStreamPredictResource, _client, _client.describe_stream_predicts,
            'StreamPredicts.StreamPredict', 'PredictId', 
        )
    def create_predict_model(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_predict_model(**_params)
        model_id = _new_get_key_in_response(response, 'ModelId')
        return _IVISIONPredictModelResource(model_id, _client=self._client)

    def delete_predict_model(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_predict_model(**_params)
        model_id = _new_get_key_in_response(response, 'ModelId')
        return _IVISIONPredictModelResource(model_id, _client=self._client)

    def create_predict_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_predict_template(**_params)
        template_id = _new_get_key_in_response(response, 'TemplateId')
        return _IVISIONPredictTemplateResource(template_id, _client=self._client)

    def delete_predict_template(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_predict_template(**_params)
        template_id = _new_get_key_in_response(response, 'TemplateId')
        return _IVISIONPredictTemplateResource(template_id, _client=self._client)

    def create_project(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_project(**_params)
        project_id = _new_get_key_in_response(response, 'ProjectId')
        return _IVISIONProjectResource(project_id, _client=self._client)

    def delete_project(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_project(**_params)
        project_id = _new_get_key_in_response(response, 'ProjectId')
        return _IVISIONProjectResource(project_id, _client=self._client)

    def create_stream_predict(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_stream_predict(**_params)
        predict_id = _new_get_key_in_response(response, 'PredictId')
        return _IVISIONStreamPredictResource(predict_id, _client=self._client)

    def delete_stream_predict(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_stream_predict(**_params)
        predict_id = _new_get_key_in_response(response, 'PredictId')
        return _IVISIONStreamPredictResource(predict_id, _client=self._client)

    def start_stream_predict(self, **params):
        _params = _transfer_params(params)
        response = self._client.start_stream_predict(**_params)
        predict_id = _new_get_key_in_response(response, 'PredictId')
        return _IVISIONStreamPredictResource(predict_id, _client=self._client)

    def stop_stream_predict(self, **params):
        _params = _transfer_params(params)
        response = self._client.stop_stream_predict(**_params)
        predict_id = _new_get_key_in_response(response, 'PredictId')
        return _IVISIONStreamPredictResource(predict_id, _client=self._client)

class _IVISIONPredictDatasResource(ServiceResource):

    def __init__(self, data_id, _client=None):
        ServiceResource.__init__(self, "ivision.predict_datas", _client=_client)
        self.data_id = data_id
        
        self.creation_time = None
        self.data_name = None
        self.data_url = None
        self.error_code = None
        self.error_message = None
        self.iteration_id = None
        self.prediction_results = None
        self.project_id = None
        self.status = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_predict_datas(data_id=self.data_id, **_params)

class _IVISIONPredictModelResource(ServiceResource):

    def __init__(self, model_id, _client=None):
        ServiceResource.__init__(self, "ivision.predict_model", _client=_client)
        self.model_id = model_id
        
        self.creation_time = None
        self.deploy_status = None
        self.description = None
        self.iteration_id = None
        self.iteration_version = None
        self.map_ = None
        self.name = None
        self.precision = None
        self.project_id = None
        self.project_name = None
        self.recall = None
        self.regions = None
        self.source = None
        self.type_ = None

    def image_predict(self, **params):
        _params = _transfer_params(params)
        return self._client.image_predict(model_id=self.model_id, **_params)

class _IVISIONPredictTemplateResource(ServiceResource):

    def __init__(self, template_id, _client=None):
        ServiceResource.__init__(self, "ivision.predict_template", _client=_client)
        self.template_id = template_id
        
        self.creation_time = None
        self.description = None
        self.interval = None
        self.model_ids = None
        self.name = None
        self.output = None

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_predict_template_attribute(template_id=self.template_id, **_params)

class _IVISIONProjectResource(ServiceResource):

    def __init__(self, project_id, _client=None):
        ServiceResource.__init__(self, "ivision.project", _client=_client)
        self.project_id = project_id
        
        self.creation_time = None
        self.description = None
        self.iter_count = None
        self.name = None
        self.pro_type = None
        self.status = None

        self.iterations = _create_sub_resource_without_page_collection(
            _IVISIONIterationResource, _client, _client.describe_iterations,
            'Iterations.Iteration', 'IterationId', parent_identifier="ProjectId",parent_identifier_value=self.project_id
        )
        self.tags = _create_sub_resource_without_page_collection(
            _IVISIONTagResource, _client, _client.describe_tags,
            'Tags.Tag', 'TagId', parent_identifier="ProjectId",parent_identifier_value=self.project_id
        )
    def create_train_data_tag(self, **params):
        _params = _transfer_params(params)
        return self._client.create_train_data_tag(project_id=self.project_id, **_params)

    def create_train_datas_from_urls(self, **params):
        _params = _transfer_params(params)
        return self._client.create_train_datas_from_urls(project_id=self.project_id, **_params)

    def delete_train_datas(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_train_datas(project_id=self.project_id, **_params)

    def delete_train_datas_tag(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_train_datas_tag(project_id=self.project_id, **_params)

    def describe_train_datas(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_train_datas(project_id=self.project_id, **_params)

    def describe_train_datas_by_ids(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_train_datas_by_ids(project_id=self.project_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_project_attribute(project_id=self.project_id, **_params)

    def modify_train_data_region_tag_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_train_data_region_tag_attribute(project_id=self.project_id, **_params)

    def modify_train_data_tag_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_train_data_tag_attribute(project_id=self.project_id, **_params)

    def train(self, **params):
        _params = _transfer_params(params)
        return self._client.train_project(project_id=self.project_id, **_params)

    def delete_iteration(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_iteration(project_id=self.project_id,**_params)
        iteration_id = _new_get_key_in_response(response, 'IterationId')
        return _IVISIONIterationResource(iteration_id,self.project_id, _client=self._client)

    def create_tag(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_tag(project_id=self.project_id,**_params)
        tag_id = _new_get_key_in_response(response, 'TagId')
        return _IVISIONTagResource(tag_id,self.project_id, _client=self._client)

    def delete_tag(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_tag(project_id=self.project_id,**_params)
        tag_id = _new_get_key_in_response(response, 'TagId')
        return _IVISIONTagResource(tag_id,self.project_id, _client=self._client)

class _IVISIONIterationResource(ServiceResource):

    def __init__(self, iteration_id,project_id, _client=None):
        ServiceResource.__init__(self, "ivision.iteration", _client=_client)
        self.iteration_id = iteration_id
        self.project_id = project_id
        self.creation_time = None
        self.finish_time = None
        self.iteration_name = None
        self.map_ = None
        self.model_id = None
        self.precision = None
        self.recall = None
        self.status = None

    def create_quick_deploy(self, **params):
        _params = _transfer_params(params)
        return self._client.create_quick_deploy(iteration_id=self.iteration_id,project_id=self.project_id, **_params)

    def create_train_datas_from_prediction(self, **params):
        _params = _transfer_params(params)
        return self._client.create_train_datas_from_prediction(iteration_id=self.iteration_id,project_id=self.project_id, **_params)

    def describe_train_result(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_train_result(iteration_id=self.iteration_id,project_id=self.project_id, **_params)

    def quick_test(self, **params):
        _params = _transfer_params(params)
        return self._client.quick_test(iteration_id=self.iteration_id,project_id=self.project_id, **_params)

class _IVISIONTagResource(ServiceResource):

    def __init__(self, tag_id,project_id, _client=None):
        ServiceResource.__init__(self, "ivision.tag", _client=_client)
        self.tag_id = tag_id
        self.project_id = project_id
        self.count = None
        self.creation_time = None
        self.description = None
        self.tag_name = None

    def create_train_datas(self, **params):
        _params = _transfer_params(params)
        return self._client.create_train_datas_tag(tag_id=self.tag_id,project_id=self.project_id, **_params)

    def modify_attribute(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_tag_attribute(tag_id=self.tag_id,project_id=self.project_id, **_params)

class _IVISIONStreamPredictResource(ServiceResource):

    def __init__(self, predict_id, _client=None):
        ServiceResource.__init__(self, "ivision.stream_predict", _client=_client)
        self.predict_id = predict_id
        
        self.creation_time = None
        self.detect_intervals = None
        self.model_ids = None
        self.notify = None
        self.output = None
        self.probability_thresholds = None
        self.status = None
        self.stream_id = None
        self.stream_type = None
        self.user_data = None

    def describe_stream_predict_result(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_stream_predict_result(predict_id=self.predict_id, **_params)
