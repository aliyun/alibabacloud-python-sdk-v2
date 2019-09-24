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


class IvisionClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'ivision'
        self.api_version = '2019-03-08'
        self.location_service_code = 'ivision'
        self.location_endpoint_type = 'openAPI'

    def register_face(
            self,
            content=None,
            data_type=None,
            show_log=None,
            group_id=None,
            owner_id=None):
        api_request = APIRequest('RegisterFace', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Content": content,
            "DataType": data_type,
            "ShowLog": show_log,
            "GroupId": group_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_face_groups(
            self,
            next_page_token=None,
            page_size=None,
            show_log=None,
            current_page=None,
            owner_id=None):
        api_request = APIRequest('DescribeFaceGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NextPageToken": next_page_token,
            "PageSize": page_size,
            "ShowLog": show_log,
            "CurrentPage": current_page,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_face_group(self, show_log=None, group_id=None, owner_id=None):
        api_request = APIRequest('DeleteFaceGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ShowLog": show_log, "GroupId": group_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_face_group(self, show_log=None, owner_id=None, name=None):
        api_request = APIRequest('CreateFaceGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ShowLog": show_log, "OwnerId": owner_id, "Name": name}
        return self._handle_request(api_request).result

    def search_face(
            self,
            content=None,
            data_type=None,
            probability_threshold=None,
            show_log=None,
            group_id=None,
            count=None,
            owner_id=None):
        api_request = APIRequest('SearchFace', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Content": content,
            "DataType": data_type,
            "ProbabilityThreshold": probability_threshold,
            "ShowLog": show_log,
            "GroupId": group_id,
            "Count": count,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def unregister_face(self, show_log=None, group_id=None, owner_id=None, face_token=None):
        api_request = APIRequest('UnregisterFace', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ShowLog": show_log,
            "GroupId": group_id,
            "OwnerId": owner_id,
            "FaceToken": face_token}
        return self._handle_request(api_request).result

    def image_predict(self, data_url=None, show_log=None, model_id=None, owner_id=None):
        api_request = APIRequest('ImagePredict', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataUrl": data_url,
            "ShowLog": show_log,
            "ModelId": model_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_tags(
            self,
            next_page_token=None,
            page_size=None,
            project_id=None,
            show_log=None,
            tag_ids=None,
            current_page=None,
            owner_id=None,
            iteration_id=None):
        api_request = APIRequest('DescribeTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NextPageToken": next_page_token,
            "PageSize": page_size,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "TagIds": tag_ids,
            "CurrentPage": current_page,
            "OwnerId": owner_id,
            "IterationId": iteration_id}
        return self._handle_request(api_request).result

    def modify_tag_attribute(
            self,
            description=None,
            project_id=None,
            show_log=None,
            tag_id=None,
            owner_id=None,
            name=None):
        api_request = APIRequest('ModifyTagAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Description": description,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "TagId": tag_id,
            "OwnerId": owner_id,
            "Name": name}
        return self._handle_request(api_request).result

    def create_tag(
            self,
            description=None,
            project_id=None,
            show_log=None,
            owner_id=None,
            name=None):
        api_request = APIRequest('CreateTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Description": description,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "Name": name}
        return self._handle_request(api_request).result

    def delete_tag(self, project_id=None, show_log=None, tag_id=None, owner_id=None):
        api_request = APIRequest('DeleteTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProjectId": project_id,
            "ShowLog": show_log,
            "TagId": tag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_iteration(self, project_id=None, show_log=None, owner_id=None, iteration_id=None):
        api_request = APIRequest('DeleteIteration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProjectId": project_id,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "IterationId": iteration_id}
        return self._handle_request(api_request).result

    def describe_iterations(
            self,
            threshold=None,
            project_id=None,
            show_log=None,
            iteration_ids=None,
            owner_id=None,
            status=None):
        api_request = APIRequest('DescribeIterations', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Threshold": threshold,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "IterationIds": iteration_ids,
            "OwnerId": owner_id,
            "Status": status}
        return self._handle_request(api_request).result

    def train_project(self, project_id=None, show_log=None, owner_id=None):
        api_request = APIRequest('TrainProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ProjectId": project_id, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_train_result(
            self,
            threshold=None,
            project_id=None,
            show_log=None,
            owner_id=None,
            iteration_id=None):
        api_request = APIRequest('DescribeTrainResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Threshold": threshold,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "IterationId": iteration_id}
        return self._handle_request(api_request).result

    def delete_train_datas(self, data_ids=None, project_id=None, show_log=None, owner_id=None):
        api_request = APIRequest('DeleteTrainDatas', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataIds": data_ids,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_train_data_tag(
            self,
            project_id=None,
            show_log=None,
            tag_items=None,
            owner_id=None,
            data_id=None):
        api_request = APIRequest('CreateTrainDataTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProjectId": project_id,
            "ShowLog": show_log,
            "TagItems": tag_items,
            "OwnerId": owner_id,
            "DataId": data_id}
        return self._handle_request(api_request).result

    def describe_train_datas_by_ids(
            self,
            data_ids=None,
            project_id=None,
            show_log=None,
            owner_id=None,
            iteration_id=None):
        api_request = APIRequest('DescribeTrainDatasByIds', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataIds": data_ids,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "IterationId": iteration_id}
        return self._handle_request(api_request).result

    def create_train_datas_tag(
            self,
            data_ids=None,
            project_id=None,
            show_log=None,
            tag_id=None,
            owner_id=None):
        api_request = APIRequest('CreateTrainDatasTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataIds": data_ids,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "TagId": tag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_train_datas_from_prediction(
            self,
            data_ids=None,
            project_id=None,
            show_log=None,
            tag_id=None,
            owner_id=None,
            iteration_id=None):
        api_request = APIRequest('CreateTrainDatasFromPrediction', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataIds": data_ids,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "TagId": tag_id,
            "OwnerId": owner_id,
            "IterationId": iteration_id}
        return self._handle_request(api_request).result

    def create_train_datas_from_urls(
            self,
            urls=None,
            project_id=None,
            show_log=None,
            tag_id=None,
            owner_id=None):
        api_request = APIRequest('CreateTrainDatasFromUrls', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Urls": urls,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "TagId": tag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_train_data_region_tag(
            self,
            project_id=None,
            show_log=None,
            tag_items=None,
            owner_id=None,
            data_id=None):
        api_request = APIRequest('CreateTrainDataRegionTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProjectId": project_id,
            "ShowLog": show_log,
            "TagItems": tag_items,
            "OwnerId": owner_id,
            "DataId": data_id}
        return self._handle_request(api_request).result

    def delete_train_datas_tag(
            self,
            data_ids=None,
            project_id=None,
            show_log=None,
            tag_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteTrainDatasTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataIds": data_ids,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "TagId": tag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_train_data_tag_attribute(
            self,
            project_id=None,
            show_log=None,
            tag_items=None,
            owner_id=None,
            data_id=None):
        api_request = APIRequest('ModifyTrainDataTagAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProjectId": project_id,
            "ShowLog": show_log,
            "TagItems": tag_items,
            "OwnerId": owner_id,
            "DataId": data_id}
        return self._handle_request(api_request).result

    def describe_train_datas(
            self,
            next_page_token=None,
            tag_status=None,
            page_size=None,
            project_id=None,
            show_log=None,
            tag_id=None,
            current_page=None,
            owner_id=None,
            iteration_id=None):
        api_request = APIRequest('DescribeTrainDatas', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NextPageToken": next_page_token,
            "TagStatus": tag_status,
            "PageSize": page_size,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "TagId": tag_id,
            "CurrentPage": current_page,
            "OwnerId": owner_id,
            "IterationId": iteration_id}
        return self._handle_request(api_request).result

    def modify_train_data_region_tag_attribute(
            self,
            project_id=None,
            show_log=None,
            tag_items=None,
            owner_id=None,
            data_id=None):
        api_request = APIRequest('ModifyTrainDataRegionTagAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProjectId": project_id,
            "ShowLog": show_log,
            "TagItems": tag_items,
            "OwnerId": owner_id,
            "DataId": data_id}
        return self._handle_request(api_request).result

    def predict_image(
            self,
            project_id=None,
            show_log=None,
            owner_id=None,
            iteration_id=None,
            data_urls=None):
        api_request = APIRequest('PredictImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProjectId": project_id,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "IterationId": iteration_id,
            "DataUrls": data_urls}
        return self._handle_request(api_request).result

    def create_upload_token(self, project_id=None, show_log=None, owner_id=None, file_name=None):
        api_request = APIRequest('CreateUploadToken', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProjectId": project_id,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "FileName": file_name}
        return self._handle_request(api_request).result

    def describe_projects(
            self,
            next_page_token=None,
            page_size=None,
            show_log=None,
            current_page=None,
            project_ids=None,
            owner_id=None):
        api_request = APIRequest('DescribeProjects', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NextPageToken": next_page_token,
            "PageSize": page_size,
            "ShowLog": show_log,
            "CurrentPage": current_page,
            "ProjectIds": project_ids,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_project(self, project_id=None, show_log=None, owner_id=None):
        api_request = APIRequest('DeleteProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ProjectId": project_id, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_project(
            self,
            description=None,
            show_log=None,
            model_id=None,
            owner_id=None,
            pro_type=None,
            name=None):
        api_request = APIRequest('CreateProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Description": description,
            "ShowLog": show_log,
            "ModelId": model_id,
            "OwnerId": owner_id,
            "ProType": pro_type,
            "Name": name}
        return self._handle_request(api_request).result

    def modify_project_attribute(
            self,
            description=None,
            project_id=None,
            show_log=None,
            owner_id=None,
            name=None):
        api_request = APIRequest('ModifyProjectAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Description": description,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "Name": name}
        return self._handle_request(api_request).result

    def delete_predict_datas(
            self,
            data_ids=None,
            project_id=None,
            show_log=None,
            owner_id=None,
            iteration_id=None):
        api_request = APIRequest('DeletePredictDatas', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DataIds": data_ids,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "IterationId": iteration_id}
        return self._handle_request(api_request).result

    def describe_predict_datas(
            self,
            next_page_token=None,
            data_ids=None,
            page_size=None,
            probability_threshold=None,
            overlap_threshold=None,
            project_id=None,
            show_log=None,
            model_id=None,
            tag_id=None,
            current_page=None,
            owner_id=None,
            iteration_id=None):
        api_request = APIRequest('DescribePredictDatas', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NextPageToken": next_page_token,
            "DataIds": data_ids,
            "PageSize": page_size,
            "ProbabilityThreshold": probability_threshold,
            "OverlapThreshold": overlap_threshold,
            "ProjectId": project_id,
            "ShowLog": show_log,
            "ModelId": model_id,
            "TagId": tag_id,
            "CurrentPage": current_page,
            "OwnerId": owner_id,
            "IterationId": iteration_id}
        return self._handle_request(api_request).result

    def create_stream_predict(
            self,
            auto_start=None,
            notify=None,
            output=None,
            user_data=None,
            show_log=None,
            stream_type=None,
            face_group_id=None,
            stream_id=None,
            detect_intervals=None,
            owner_id=None,
            probability_thresholds=None,
            model_ids=None):
        api_request = APIRequest('CreateStreamPredict', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AutoStart": auto_start,
            "Notify": notify,
            "Output": output,
            "UserData": user_data,
            "ShowLog": show_log,
            "StreamType": stream_type,
            "FaceGroupId": face_group_id,
            "StreamId": stream_id,
            "DetectIntervals": detect_intervals,
            "OwnerId": owner_id,
            "ProbabilityThresholds": probability_thresholds,
            "ModelIds": model_ids}
        return self._handle_request(api_request).result

    def delete_stream_predict(self, predict_id=None, show_log=None, owner_id=None):
        api_request = APIRequest('DeleteStreamPredict', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PredictId": predict_id, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_stream_predict(self, predict_id=None, show_log=None, owner_id=None):
        api_request = APIRequest('StopStreamPredict', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PredictId": predict_id, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_stream_predict_result(
            self,
            next_page_token=None,
            start_time=None,
            predict_id=None,
            page_size=None,
            probability_threshold=None,
            show_log=None,
            model_id=None,
            end_time=None,
            current_page=None,
            owner_id=None):
        api_request = APIRequest('DescribeStreamPredictResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NextPageToken": next_page_token,
            "StartTime": start_time,
            "PredictId": predict_id,
            "PageSize": page_size,
            "ProbabilityThreshold": probability_threshold,
            "ShowLog": show_log,
            "ModelId": model_id,
            "EndTime": end_time,
            "CurrentPage": current_page,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_stream_predicts(
            self,
            next_page_token=None,
            predict_ids=None,
            page_size=None,
            show_log=None,
            current_page=None,
            owner_id=None):
        api_request = APIRequest('DescribeStreamPredicts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NextPageToken": next_page_token,
            "PredictIds": predict_ids,
            "PageSize": page_size,
            "ShowLog": show_log,
            "CurrentPage": current_page,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_stream_predict(self, predict_id=None, show_log=None, owner_id=None):
        api_request = APIRequest('StartStreamPredict', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PredictId": predict_id, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result
