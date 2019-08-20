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


class QualitycheckClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Qualitycheck'
        self.api_version = '2019-01-15'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def get_user_config(self, resource_owner_id=None):
        api_request = APIRequest('GetUserConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id}
        return self._handle_request(api_request).result

    def update_user_config(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UpdateUserConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def delete_user(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DeleteUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def delete_task_assign_rule(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DeleteTaskAssignRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def create_user(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('CreateUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def create_task_assign_rule(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('CreateTaskAssignRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def assign_reviewer(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('AssignReviewer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def handle_complaint(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('HandleComplaint', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def submit_complaint(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('SubmitComplaint', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def update_task_assign_rule(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UpdateTaskAssignRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def update_user(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UpdateUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def list_users(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ListUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def list_roles(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ListRoles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def list_task_assign_rules(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ListTaskAssignRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def create_skill_group_config(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('CreateSkillGroupConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def create_warning_config(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('CreateWarningConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def delete_precision_task(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DeletePrecisionTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def delete_skill_group_config(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DeleteSkillGroupConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def delete_warning_config(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DeleteWarningConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_skill_group_config(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetSkillGroupConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def list_skill_group_config(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ListSkillGroupConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def list_warning_config(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ListWarningConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def update_skill_group_config(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UpdateSkillGroupConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def update_warning_config(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UpdateWarningConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_next_result_to_verify(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetNextResultToVerify', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_precision_task(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetPrecisionTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def list_precision_task(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ListPrecisionTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def submit_precision_task(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('SubmitPrecisionTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def verify_file(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('VerifyFile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def verify_sentence(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('VerifySentence', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def list_asr_vocab(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ListAsrVocab', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_user_info(self, resource_owner_id=None):
        api_request = APIRequest('GetUserInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id}
        return self._handle_request(api_request).result

    def restart_asr_task(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('RestartAsrTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def open_service(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('OpenService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_result_to_review(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetResultToReview', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def create_rule(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('CreateRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_next_result_to_review(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetNextResultToReview', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def close_service(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('CloseService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def save_review_result(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('SaveReviewResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def upload_audio_data(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UploadAudioData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def upload_audio_data4_pre(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UploadAudioData4Pre', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def generate_customization_model_id(self, resource_owner_id=None):
        api_request = APIRequest('GenerateCustomizationModelId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id}
        return self._handle_request(api_request).result

    def add_thesaurus_for_api(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('AddThesaurusForApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def remove_and_get_task_rules(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('RemoveAndGetTaskRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def submit_review_info(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('SubmitReviewInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_audio_data_status(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetAudioDataStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def review_single_result_by_id(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ReviewSingleResultById', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def upload_data_sync(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UploadDataSync', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def save_config_data_set(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('SaveConfigDataSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def update_sub_score_for_api(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UpdateSubScoreForApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def config_data_set(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ConfigDataSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def upload_rule(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UploadRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def insert_score_for_api(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('InsertScoreForApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def insert_sub_score_for_api(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('InsertSubScoreForApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def submit_model_test_task(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('SubmitModelTestTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def del_rule_category(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DelRuleCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_acc_asr_result(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetAccAsrResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def test_rule(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('TestRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def exchange_audio(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ExchangeAudio', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_poc_test_report(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetPocTestReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_rule_detail(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetRuleDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def update_asr_vocab(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UpdateAsrVocab', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def update_rule_for_ant(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UpdateRuleForAnt', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_oss_header(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetOssHeader', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_recognize_result(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetRecognizeResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_business_category_list(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetBusinessCategoryList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def invalid_rule(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('InvalidRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def delete_sub_score_for_api(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DeleteSubScoreForApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def update_on_purchase_success(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UpdateOnPurchaseSuccess', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_thesaurus_by_synonym_for_api(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetThesaurusBySynonymForApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def create_asr_vocab(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('CreateAsrVocab', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def list_data_set_task(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ListDataSetTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def submit_audio_label(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('SubmitAudioLabel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def del_thesaurus_for_api(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DelThesaurusForApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def delete_asr_vocab(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DeleteAsrVocab', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_audio_url(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetAudioUrl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def add_rule_category(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('AddRuleCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_rule_dimension(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetRuleDimension', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def add_upload_data_set(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('AddUploadDataSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_result_count(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetResultCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_customization_config_list(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetCustomizationConfigList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def edit_thesaurus_for_api(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('EditThesaurusForApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def execute_asr_transform(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ExecuteAsrTransform', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_score_info(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetScoreInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def upload_data(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UploadData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def add_business_category(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('AddBusinessCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_asr_vocab(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetAsrVocab', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def do_logical_delete_resource(
            self,
            country=None,
            resource_owner_id=None,
            hid=None,
            success=None,
            interrupt=None,
            gmt_wakeup=None,
            pk=None,
            bid=None,
            message=None,
            task_extra_data=None,
            task_identifier=None):
        api_request = APIRequest('DoLogicalDeleteResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "ResourceOwnerId": resource_owner_id,
            "Hid": hid,
            "Success": success,
            "Interrupt": interrupt,
            "GmtWakeup": gmt_wakeup,
            "Pk": pk,
            "Bid": bid,
            "Message": message,
            "TaskExtraData": task_extra_data,
            "TaskIdentifier": task_identifier}
        return self._handle_request(api_request).result

    def upload_audio_data_with_rules(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UploadAudioDataWithRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_review_info(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetReviewInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_result(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def submit_quality_check_task(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('SubmitQualityCheckTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_rule_category(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetRuleCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_rule(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_data_set_list(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetDataSetList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def upload_rule_for_ant(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UploadRuleForAnt', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_user_group(self, resource_owner_id=None):
        api_request = APIRequest('GetUserGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id}
        return self._handle_request(api_request).result

    def submit_customization_config(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('SubmitCustomizationConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_task_file_result_list(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetTaskFileResultList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def do_physical_delete_resource(
            self,
            country=None,
            resource_owner_id=None,
            hid=None,
            success=None,
            interrupt=None,
            gmt_wakeup=None,
            pk=None,
            bid=None,
            task_extra_data=None,
            task_identifier=None):
        api_request = APIRequest('DoPhysicalDeleteResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "ResourceOwnerId": resource_owner_id,
            "Hid": hid,
            "Success": success,
            "Interrupt": interrupt,
            "GmtWakeup": gmt_wakeup,
            "Pk": pk,
            "Bid": bid,
            "TaskExtraData": task_extra_data,
            "TaskIdentifier": task_identifier}
        return self._handle_request(api_request).result

    def delete_data_set(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DeleteDataSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def update_score_for_api(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UpdateScoreForApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def upload_data_with_rules(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UploadDataWithRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def delete_customization_config(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DeleteCustomizationConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def validate_role_set(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('ValidateRoleSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def do_check_resource(
            self,
            country=None,
            resource_owner_id=None,
            hid=None,
            level=None,
            message=None,
            success=None,
            interrupt=None,
            gmt_wakeup=None,
            pk=None,
            bid=None,
            prompt=None,
            task_extra_data=None,
            task_identifier=None):
        api_request = APIRequest('DoCheckResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Country": country,
            "ResourceOwnerId": resource_owner_id,
            "Hid": hid,
            "Level": level,
            "Message": message,
            "Success": success,
            "Interrupt": interrupt,
            "GmtWakeup": gmt_wakeup,
            "Pk": pk,
            "Bid": bid,
            "Prompt": prompt,
            "TaskExtraData": task_extra_data,
            "TaskIdentifier": task_identifier}
        return self._handle_request(api_request).result

    def register_notice(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('RegisterNotice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def delete_business_category(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DeleteBusinessCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_data_set_oss_header(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetDataSetOssHeader', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_task_rule_list(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetTaskRuleList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_audio_content_info(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetAudioContentInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def upload_audio_data_with_rules4_pre(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UploadAudioDataWithRules4Pre', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_file_dimension(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetFileDimension', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def get_result_review_list(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('GetResultReviewList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def update_rule(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('UpdateRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def delete_score_for_api(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('DeleteScoreForApi', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result

    def test_network(self, resource_owner_id=None, json_str=None):
        api_request = APIRequest('TestNetwork', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ResourceOwnerId": resource_owner_id, "JsonStr": json_str}
        return self._handle_request(api_request).result
