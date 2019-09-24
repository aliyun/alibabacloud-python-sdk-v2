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


class ImmClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'imm'
        self.api_version = '2017-09-06'
        self.location_service_code = 'imm'
        self.location_endpoint_type = 'openAPI'

    def get_media_meta(self, media_uri=None, project=None):
        api_request = APIRequest('GetMediaMeta', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MediaUri": media_uri, "Project": project}
        return self._handle_request(api_request).result

    def list_project_ap_is(self, project=None):
        api_request = APIRequest('ListProjectAPIs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project}
        return self._handle_request(api_request).result

    def create_video_compress_task(
            self,
            video_uri=None,
            notify_topic_name=None,
            target_list=None,
            notify_endpoint=None,
            project=None):
        api_request = APIRequest('CreateVideoCompressTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VideoUri": video_uri,
            "NotifyTopicName": notify_topic_name,
            "TargetList": target_list,
            "NotifyEndpoint": notify_endpoint,
            "Project": project}
        return self._handle_request(api_request).result

    def detect_image_bodies(self, image_uri=None, project=None):
        api_request = APIRequest('DetectImageBodies', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ImageUri": image_uri, "Project": project}
        return self._handle_request(api_request).result

    def create_merge_face_groups_job(
            self,
            group_id_from=None,
            group_id_to=None,
            notify_topic_name=None,
            notify_endpoint=None,
            project=None,
            set_id=None):
        api_request = APIRequest('CreateMergeFaceGroupsJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GroupIdFrom": group_id_from,
            "GroupIdTo": group_id_to,
            "NotifyTopicName": notify_topic_name,
            "NotifyEndpoint": notify_endpoint,
            "Project": project,
            "SetId": set_id}
        return self._handle_request(api_request).result

    def detect_image_logos(self, image_uri=None, project=None):
        api_request = APIRequest('DetectImageLogos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ImageUri": image_uri, "Project": project}
        return self._handle_request(api_request).result

    def update_face_group(
            self,
            group_id=None,
            project=None,
            set_id=None,
            group_name=None,
            group_cover_face_id=None):
        api_request = APIRequest('UpdateFaceGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GroupId": group_id,
            "Project": project,
            "SetId": set_id,
            "GroupName": group_name,
            "GroupCoverFaceId": group_cover_face_id}
        return self._handle_request(api_request).result

    def create_cad_conversion_task(
            self,
            src_type=None,
            base_col=None,
            notify_topic_name=None,
            unit_width=None,
            zoom_level=None,
            base_row=None,
            model_id=None,
            project=None,
            zoom_factor=None,
            tgt_type=None,
            unit_height=None,
            notify_endpoint=None,
            src_uri=None,
            thumbnails=None,
            tgt_uri=None):
        api_request = APIRequest('CreateCADConversionTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcType": src_type,
            "BaseCol": base_col,
            "NotifyTopicName": notify_topic_name,
            "UnitWidth": unit_width,
            "ZoomLevel": zoom_level,
            "BaseRow": base_row,
            "ModelId": model_id,
            "Project": project,
            "ZoomFactor": zoom_factor,
            "TgtType": tgt_type,
            "UnitHeight": unit_height,
            "NotifyEndpoint": notify_endpoint,
            "SrcUri": src_uri,
            "Thumbnails": thumbnails,
            "TgtUri": tgt_uri}
        return self._handle_request(api_request).result

    def find_similar_faces(
            self,
            image_uri=None,
            min_similarity=None,
            response_format=None,
            limit=None,
            project=None,
            set_id=None,
            face_id=None):
        api_request = APIRequest('FindSimilarFaces', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageUri": image_uri,
            "MinSimilarity": min_similarity,
            "ResponseFormat": response_format,
            "Limit": limit,
            "Project": project,
            "SetId": set_id,
            "FaceId": face_id}
        return self._handle_request(api_request).result

    def find_images(
            self,
            gender=None,
            project=None,
            external_id=None,
            faces_modify_time_range=None,
            image_size_range=None,
            remarks_bprefix=None,
            location_boundary=None,
            image_time_range=None,
            ocr_contents_match=None,
            limit=None,
            remarks_dprefix=None,
            tags_modify_time_range=None,
            source_type=None,
            age_range=None,
            order=None,
            remarks_aprefix=None,
            group_id=None,
            order_by=None,
            tag_names=None,
            source_uri_prefix=None,
            emotion=None,
            marker=None,
            remarks_cprefix=None,
            create_time_range=None,
            set_id=None,
            modify_time_range=None):
        api_request = APIRequest('FindImages', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Gender": gender,
            "Project": project,
            "ExternalId": external_id,
            "FacesModifyTimeRange": faces_modify_time_range,
            "ImageSizeRange": image_size_range,
            "RemarksBPrefix": remarks_bprefix,
            "LocationBoundary": location_boundary,
            "ImageTimeRange": image_time_range,
            "OCRContentsMatch": ocr_contents_match,
            "Limit": limit,
            "RemarksDPrefix": remarks_dprefix,
            "TagsModifyTimeRange": tags_modify_time_range,
            "SourceType": source_type,
            "AgeRange": age_range,
            "Order": order,
            "RemarksAPrefix": remarks_aprefix,
            "GroupId": group_id,
            "OrderBy": order_by,
            "TagNames": tag_names,
            "SourceUriPrefix": source_uri_prefix,
            "Emotion": emotion,
            "Marker": marker,
            "RemarksCPrefix": remarks_cprefix,
            "CreateTimeRange": create_time_range,
            "SetId": set_id,
            "ModifyTimeRange": modify_time_range}
        return self._handle_request(api_request).result

    def find_images_by_tag_names(
            self,
            marker=None,
            limit=None,
            project=None,
            set_id=None,
            tag_names=None):
        api_request = APIRequest('FindImagesByTagNames', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Marker": marker,
            "Limit": limit,
            "Project": project,
            "SetId": set_id,
            "TagNames": tag_names}
        return self._handle_request(api_request).result

    def create_set(self, set_name=None, project=None, set_id=None):
        api_request = APIRequest('CreateSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SetName": set_name, "Project": project, "SetId": set_id}
        return self._handle_request(api_request).result

    def get_set(self, project=None, set_id=None):
        api_request = APIRequest('GetSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "SetId": set_id}
        return self._handle_request(api_request).result

    def index_image(
            self,
            remarks_b=None,
            project=None,
            remarks_a=None,
            external_id=None,
            image_uri=None,
            source_uri=None,
            source_position=None,
            remarks_d=None,
            remarks_c=None,
            set_id=None,
            source_type=None,
            real_uid=None):
        api_request = APIRequest('IndexImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RemarksB": remarks_b,
            "Project": project,
            "RemarksA": remarks_a,
            "ExternalId": external_id,
            "ImageUri": image_uri,
            "SourceUri": source_uri,
            "SourcePosition": source_position,
            "RemarksD": remarks_d,
            "RemarksC": remarks_c,
            "SetId": set_id,
            "SourceType": source_type,
            "RealUid": real_uid}
        return self._handle_request(api_request).result

    def update_set(self, set_name=None, project=None, set_id=None):
        api_request = APIRequest('UpdateSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SetName": set_name, "Project": project, "SetId": set_id}
        return self._handle_request(api_request).result

    def list_sets(self, marker=None, project=None):
        api_request = APIRequest('ListSets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Marker": marker, "Project": project}
        return self._handle_request(api_request).result

    def get_image(self, image_uri=None, project=None, set_id=None):
        api_request = APIRequest('GetImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ImageUri": image_uri, "Project": project, "SetId": set_id}
        return self._handle_request(api_request).result

    def delete_set(self, project=None, set_id=None):
        api_request = APIRequest('DeleteSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "SetId": set_id}
        return self._handle_request(api_request).result

    def list_video_frames(self, video_uri=None, marker=None, project=None, set_id=None):
        api_request = APIRequest('ListVideoFrames', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VideoUri": video_uri,
            "Marker": marker,
            "Project": project,
            "SetId": set_id}
        return self._handle_request(api_request).result

    def list_video_audios(self, video_uri=None, marker=None, project=None, set_id=None):
        api_request = APIRequest('ListVideoAudios', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VideoUri": video_uri,
            "Marker": marker,
            "Project": project,
            "SetId": set_id}
        return self._handle_request(api_request).result

    def detect_image_tags(self, image_uri=None, project=None, real_uid=None):
        api_request = APIRequest('DetectImageTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ImageUri": image_uri, "Project": project, "RealUid": real_uid}
        return self._handle_request(api_request).result

    def detect_image_faces(self, image_uri=None, project=None, real_uid=None):
        api_request = APIRequest('DetectImageFaces', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ImageUri": image_uri, "Project": project, "RealUid": real_uid}
        return self._handle_request(api_request).result

    def delete_image(self, image_uri=None, project=None, set_id=None):
        api_request = APIRequest('DeleteImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ImageUri": image_uri, "Project": project, "SetId": set_id}
        return self._handle_request(api_request).result

    def compare_image_faces(
            self,
            image_uri_b=None,
            image_uri_a=None,
            project=None,
            set_id=None,
            face_id_a=None,
            face_id_b=None):
        api_request = APIRequest('CompareImageFaces', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageUriB": image_uri_b,
            "ImageUriA": image_uri_a,
            "Project": project,
            "SetId": set_id,
            "FaceIdA": face_id_a,
            "FaceIdB": face_id_b}
        return self._handle_request(api_request).result

    def delete_video(self, video_uri=None, project=None, set_id=None, resources=None):
        api_request = APIRequest('DeleteVideo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VideoUri": video_uri,
            "Project": project,
            "SetId": set_id,
            "Resources": resources}
        return self._handle_request(api_request).result

    def list_images(
            self,
            marker=None,
            limit=None,
            project=None,
            set_id=None,
            create_time_start=None):
        api_request = APIRequest('ListImages', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Marker": marker,
            "Limit": limit,
            "Project": project,
            "SetId": set_id,
            "CreateTimeStart": create_time_start}
        return self._handle_request(api_request).result

    def update_image(
            self,
            remarks_b=None,
            project=None,
            remarks_a=None,
            external_id=None,
            image_uri=None,
            source_uri=None,
            source_position=None,
            remarks_d=None,
            remarks_c=None,
            set_id=None,
            source_type=None):
        api_request = APIRequest('UpdateImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RemarksB": remarks_b,
            "Project": project,
            "RemarksA": remarks_a,
            "ExternalId": external_id,
            "ImageUri": image_uri,
            "SourceUri": source_uri,
            "SourcePosition": source_position,
            "RemarksD": remarks_d,
            "RemarksC": remarks_c,
            "SetId": set_id,
            "SourceType": source_type}
        return self._handle_request(api_request).result

    def list_videos(self, marker=None, project=None, set_id=None, create_time_start=None):
        api_request = APIRequest('ListVideos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Marker": marker,
            "Project": project,
            "SetId": set_id,
            "CreateTimeStart": create_time_start}
        return self._handle_request(api_request).result

    def detect_image_texts(self, image_uri=None, project=None):
        api_request = APIRequest('DetectImageTexts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ImageUri": image_uri, "Project": project}
        return self._handle_request(api_request).result

    def detect_image_celebrity(self, image_uri=None, library=None, project=None, real_uid=None):
        api_request = APIRequest('DetectImageCelebrity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageUri": image_uri,
            "Library": library,
            "Project": project,
            "RealUid": real_uid}
        return self._handle_request(api_request).result

    def index_video(
            self,
            grab_type=None,
            remarks_b=None,
            project=None,
            remarks_a=None,
            end_time=None,
            external_id=None,
            start_time=None,
            video_uri=None,
            save_type=None,
            remarks_d=None,
            remarks_c=None,
            set_id=None,
            interval=None,
            tgt_uri=None):
        api_request = APIRequest('IndexVideo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GrabType": grab_type,
            "RemarksB": remarks_b,
            "Project": project,
            "RemarksA": remarks_a,
            "EndTime": end_time,
            "ExternalId": external_id,
            "StartTime": start_time,
            "VideoUri": video_uri,
            "SaveType": save_type,
            "RemarksD": remarks_d,
            "RemarksC": remarks_c,
            "SetId": set_id,
            "Interval": interval,
            "TgtUri": tgt_uri}
        return self._handle_request(api_request).result

    def get_video(self, video_uri=None, project=None, set_id=None):
        api_request = APIRequest('GetVideo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"VideoUri": video_uri, "Project": project, "SetId": set_id}
        return self._handle_request(api_request).result

    def list_set_tags(self, project=None, set_id=None):
        api_request = APIRequest('ListSetTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "SetId": set_id}
        return self._handle_request(api_request).result

    def create_video_analyse_task(
            self,
            notify_topic_name=None,
            grab_type=None,
            project=None,
            end_time=None,
            start_time=None,
            video_uri=None,
            save_type=None,
            notify_endpoint=None,
            interval=None,
            tgt_uri=None):
        api_request = APIRequest('CreateVideoAnalyseTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NotifyTopicName": notify_topic_name,
            "GrabType": grab_type,
            "Project": project,
            "EndTime": end_time,
            "StartTime": start_time,
            "VideoUri": video_uri,
            "SaveType": save_type,
            "NotifyEndpoint": notify_endpoint,
            "Interval": interval,
            "TgtUri": tgt_uri}
        return self._handle_request(api_request).result

    def get_video_task(self, task_type=None, project=None, task_id=None):
        api_request = APIRequest('GetVideoTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TaskType": task_type, "Project": project, "TaskId": task_id}
        return self._handle_request(api_request).result

    def delete_video_task(self, task_type=None, project=None, task_id=None):
        api_request = APIRequest('DeleteVideoTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TaskType": task_type, "Project": project, "TaskId": task_id}
        return self._handle_request(api_request).result

    def list_video_tasks(self, max_keys=None, task_type=None, marker=None, project=None):
        api_request = APIRequest('ListVideoTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MaxKeys": max_keys,
            "TaskType": task_type,
            "Marker": marker,
            "Project": project}
        return self._handle_request(api_request).result

    def get_image_job(self, job_id=None, project=None, job_type=None):
        api_request = APIRequest('GetImageJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JobId": job_id, "Project": project, "JobType": job_type}
        return self._handle_request(api_request).result

    def delete_image_job(self, job_id=None, project=None, job_type=None):
        api_request = APIRequest('DeleteImageJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JobId": job_id, "Project": project, "JobType": job_type}
        return self._handle_request(api_request).result

    def list_image_jobs(self, max_keys=None, marker=None, project=None, job_type=None):
        api_request = APIRequest('ListImageJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MaxKeys": max_keys,
            "Marker": marker,
            "Project": project,
            "JobType": job_type}
        return self._handle_request(api_request).result

    def create_group_faces_job(
            self,
            notify_topic_name=None,
            notify_endpoint=None,
            project=None,
            set_id=None):
        api_request = APIRequest('CreateGroupFacesJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NotifyTopicName": notify_topic_name,
            "NotifyEndpoint": notify_endpoint,
            "Project": project,
            "SetId": set_id}
        return self._handle_request(api_request).result

    def create_doc_index_task(
            self,
            custom_key1=None,
            set=None,
            custom_key5=None,
            custom_key4=None,
            custom_key3=None,
            custom_key2=None,
            project=None,
            custom_key6=None,
            content_type=None,
            name=None,
            src_uri=None,
            unique_id=None):
        api_request = APIRequest('CreateDocIndexTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CustomKey1": custom_key1,
            "Set": set,
            "CustomKey5": custom_key5,
            "CustomKey4": custom_key4,
            "CustomKey3": custom_key3,
            "CustomKey2": custom_key2,
            "Project": project,
            "CustomKey6": custom_key6,
            "ContentType": content_type,
            "Name": name,
            "SrcUri": src_uri,
            "UniqueId": unique_id}
        return self._handle_request(api_request).result

    def get_doc_index_task(self, project=None, task_id=None):
        api_request = APIRequest('GetDocIndexTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "TaskId": task_id}
        return self._handle_request(api_request).result

    def update_doc_index_meta(
            self,
            custom_key1=None,
            set=None,
            custom_key5=None,
            custom_key4=None,
            custom_key3=None,
            custom_key2=None,
            project=None,
            custom_key6=None,
            name=None,
            unique_id=None):
        api_request = APIRequest('UpdateDocIndexMeta', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CustomKey1": custom_key1,
            "Set": set,
            "CustomKey5": custom_key5,
            "CustomKey4": custom_key4,
            "CustomKey3": custom_key3,
            "CustomKey2": custom_key2,
            "Project": project,
            "CustomKey6": custom_key6,
            "Name": name,
            "UniqueId": unique_id}
        return self._handle_request(api_request).result

    def get_doc_index(self, set=None, project=None, unique_id=None):
        api_request = APIRequest('GetDocIndex', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Set": set, "Project": project, "UniqueId": unique_id}
        return self._handle_request(api_request).result

    def delete_doc_index(self, set=None, project=None, unique_id=None):
        api_request = APIRequest('DeleteDocIndex', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Set": set, "Project": project, "UniqueId": unique_id}
        return self._handle_request(api_request).result

    def search_doc_index(
            self,
            modified_time_end=None,
            custom_key1=None,
            set=None,
            size_limit_end=None,
            custom_key5=None,
            offset=None,
            custom_key4=None,
            custom_key3=None,
            custom_key2=None,
            project=None,
            modified_time_start=None,
            page_num_limit_start=None,
            custom_key6=None,
            content=None,
            page_num_limit_end=None,
            content_type=None,
            size_limit_start=None,
            name=None,
            limit=None):
        api_request = APIRequest('SearchDocIndex', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ModifiedTimeEnd": modified_time_end,
            "CustomKey1": custom_key1,
            "Set": set,
            "SizeLimitEnd": size_limit_end,
            "CustomKey5": custom_key5,
            "Offset": offset,
            "CustomKey4": custom_key4,
            "CustomKey3": custom_key3,
            "CustomKey2": custom_key2,
            "Project": project,
            "ModifiedTimeStart": modified_time_start,
            "PageNumLimitStart": page_num_limit_start,
            "CustomKey6": custom_key6,
            "Content": content,
            "PageNumLimitEnd": page_num_limit_end,
            "ContentType": content_type,
            "SizeLimitStart": size_limit_start,
            "Name": name,
            "Limit": limit}
        return self._handle_request(api_request).result

    def detect_logo(self, src_uris=None, project=None):
        api_request = APIRequest('DetectLogo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SrcUris": src_uris, "Project": project}
        return self._handle_request(api_request).result

    def detect_clothes(self, src_uris=None, project=None):
        api_request = APIRequest('DetectClothes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SrcUris": src_uris, "Project": project}
        return self._handle_request(api_request).result

    def update_project(self, new_service_role=None, project=None, new_cu=None):
        api_request = APIRequest('UpdateProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NewServiceRole": new_service_role,
            "Project": project,
            "NewCU": new_cu}
        return self._handle_request(api_request).result

    def detect_qr_codes(self, src_uris=None, project=None):
        api_request = APIRequest('DetectQRCodes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SrcUris": src_uris, "Project": project}
        return self._handle_request(api_request).result

    def compare_face(self, src_uri_b=None, src_uri_a=None, project=None):
        api_request = APIRequest('CompareFace', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SrcUriB": src_uri_b, "SrcUriA": src_uri_a, "Project": project}
        return self._handle_request(api_request).result

    def regist_face(
            self,
            choose_biggest_face=None,
            is_quality_limit=None,
            project=None,
            src_uri=None,
            register_check_level=None,
            group_name=None,
            user=None):
        api_request = APIRequest('RegistFace', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ChooseBiggestFace": choose_biggest_face,
            "IsQualityLimit": is_quality_limit,
            "Project": project,
            "SrcUri": src_uri,
            "RegisterCheckLevel": register_check_level,
            "GroupName": group_name,
            "User": user}
        return self._handle_request(api_request).result

    def search_face(
            self,
            result_num=None,
            project=None,
            search_threshold_level=None,
            src_uri=None,
            is_threshold=None,
            group_name=None):
        api_request = APIRequest('SearchFace', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResultNum": result_num,
            "Project": project,
            "SearchThresholdLevel": search_threshold_level,
            "SrcUri": src_uri,
            "IsThreshold": is_threshold,
            "GroupName": group_name}
        return self._handle_request(api_request).result

    def list_face_search_group_users(
            self,
            max_keys=None,
            marker=None,
            project=None,
            group_name=None):
        api_request = APIRequest('ListFaceSearchGroupUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MaxKeys": max_keys,
            "Marker": marker,
            "Project": project,
            "GroupName": group_name}
        return self._handle_request(api_request).result

    def list_face_search_groups(self, max_keys=None, marker=None, project=None):
        api_request = APIRequest('ListFaceSearchGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MaxKeys": max_keys, "Marker": marker, "Project": project}
        return self._handle_request(api_request).result

    def list_face_search_group_images(
            self,
            max_keys=None,
            marker=None,
            project=None,
            group_name=None,
            user=None):
        api_request = APIRequest('ListFaceSearchGroupImages', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MaxKeys": max_keys,
            "Marker": marker,
            "Project": project,
            "GroupName": group_name,
            "User": user}
        return self._handle_request(api_request).result

    def delete_face_search_image_by_id(
            self,
            image_id=None,
            project=None,
            src_uri=None,
            group_name=None,
            user=None):
        api_request = APIRequest('DeleteFaceSearchImageById', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageId": image_id,
            "Project": project,
            "SrcUri": src_uri,
            "GroupName": group_name,
            "User": user}
        return self._handle_request(api_request).result

    def delete_face_search_user(self, project=None, group_name=None, user=None):
        api_request = APIRequest('DeleteFaceSearchUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "GroupName": group_name, "User": user}
        return self._handle_request(api_request).result

    def delete_face_search_group(self, project=None, group_name=None):
        api_request = APIRequest('DeleteFaceSearchGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "GroupName": group_name}
        return self._handle_request(api_request).result

    def get_face_search_group(self, project=None, group_name=None):
        api_request = APIRequest('GetFaceSearchGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "GroupName": group_name}
        return self._handle_request(api_request).result

    def get_face_search_user(self, project=None, group_name=None, user=None):
        api_request = APIRequest('GetFaceSearchUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "GroupName": group_name, "User": user}
        return self._handle_request(api_request).result

    def get_face_search_image(
            self,
            image_id=None,
            project=None,
            src_uri=None,
            group_name=None,
            user=None):
        api_request = APIRequest('GetFaceSearchImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageId": image_id,
            "Project": project,
            "SrcUri": src_uri,
            "GroupName": group_name,
            "User": user}
        return self._handle_request(api_request).result

    def delete_tag_by_url(self, project=None, set_id=None, src_uri=None):
        api_request = APIRequest('DeleteTagByUrl', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "SetId": set_id, "SrcUri": src_uri}
        return self._handle_request(api_request).result

    def delete_tag_by_name(self, tag_name=None, project=None, set_id=None, src_uri=None):
        api_request = APIRequest('DeleteTagByName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TagName": tag_name,
            "Project": project,
            "SetId": set_id,
            "SrcUri": src_uri}
        return self._handle_request(api_request).result

    def list_tag_names(self, marker=None, project=None, set_id=None):
        api_request = APIRequest('ListTagNames', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Marker": marker, "Project": project, "SetId": set_id}
        return self._handle_request(api_request).result

    def list_office_conversion_task(self, max_keys=None, marker=None, project=None):
        api_request = APIRequest('ListOfficeConversionTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MaxKeys": max_keys, "Marker": marker, "Project": project}
        return self._handle_request(api_request).result

    def list_tag_photos(self, tag_name=None, max_keys=None, marker=None, project=None, set_id=None):
        api_request = APIRequest('ListTagPhotos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TagName": tag_name,
            "MaxKeys": max_keys,
            "Marker": marker,
            "Project": project,
            "SetId": set_id}
        return self._handle_request(api_request).result

    def get_office_conversion_task(self, project=None, task_id=None):
        api_request = APIRequest('GetOfficeConversionTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "TaskId": task_id}
        return self._handle_request(api_request).result

    def delete_office_conversion_task(self, project=None, task_id=None):
        api_request = APIRequest('DeleteOfficeConversionTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "TaskId": task_id}
        return self._handle_request(api_request).result

    def create_office_conversion_task(
            self,
            src_type=None,
            project=None,
            idempotent_token=None,
            pdf_vector=None,
            password=None,
            start_page=None,
            notify_endpoint=None,
            fit_to_pages_wide=None,
            tgt_file_prefix=None,
            notify_topic_name=None,
            model_id=None,
            display_dpi=None,
            max_sheet_row=None,
            max_sheet_count=None,
            end_page=None,
            tgt_file_suffix=None,
            sheet_one_page=None,
            max_sheet_col=None,
            tgt_type=None,
            hidecomments=None,
            fit_to_pages_tall=None,
            src_uri=None,
            tgt_file_pages=None,
            tgt_uri=None):
        api_request = APIRequest('CreateOfficeConversionTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcType": src_type,
            "Project": project,
            "IdempotentToken": idempotent_token,
            "PdfVector": pdf_vector,
            "Password": password,
            "StartPage": start_page,
            "NotifyEndpoint": notify_endpoint,
            "FitToPagesWide": fit_to_pages_wide,
            "TgtFilePrefix": tgt_file_prefix,
            "NotifyTopicName": notify_topic_name,
            "ModelId": model_id,
            "DisplayDpi": display_dpi,
            "MaxSheetRow": max_sheet_row,
            "MaxSheetCount": max_sheet_count,
            "EndPage": end_page,
            "TgtFileSuffix": tgt_file_suffix,
            "SheetOnePage": sheet_one_page,
            "MaxSheetCol": max_sheet_col,
            "TgtType": tgt_type,
            "Hidecomments": hidecomments,
            "FitToPagesTall": fit_to_pages_tall,
            "SrcUri": src_uri,
            "TgtFilePages": tgt_file_pages,
            "TgtUri": tgt_uri}
        return self._handle_request(api_request).result

    def describe_regions(self,):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def convert_office_format(
            self,
            src_type=None,
            model_id=None,
            project=None,
            max_sheet_row=None,
            max_sheet_count=None,
            end_page=None,
            tgt_file_suffix=None,
            pdf_vector=None,
            sheet_one_page=None,
            password=None,
            start_page=None,
            max_sheet_col=None,
            tgt_type=None,
            fit_to_pages_wide=None,
            hidecomments=None,
            tgt_file_prefix=None,
            fit_to_pages_tall=None,
            src_uri=None,
            tgt_file_pages=None,
            tgt_uri=None):
        api_request = APIRequest('ConvertOfficeFormat', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcType": src_type,
            "ModelId": model_id,
            "Project": project,
            "MaxSheetRow": max_sheet_row,
            "MaxSheetCount": max_sheet_count,
            "EndPage": end_page,
            "TgtFileSuffix": tgt_file_suffix,
            "PdfVector": pdf_vector,
            "SheetOnePage": sheet_one_page,
            "Password": password,
            "StartPage": start_page,
            "MaxSheetCol": max_sheet_col,
            "TgtType": tgt_type,
            "FitToPagesWide": fit_to_pages_wide,
            "Hidecomments": hidecomments,
            "TgtFilePrefix": tgt_file_prefix,
            "FitToPagesTall": fit_to_pages_tall,
            "SrcUri": src_uri,
            "TgtFilePages": tgt_file_pages,
            "TgtUri": tgt_uri}
        return self._handle_request(api_request).result

    def photo_process(
            self,
            notify_topic_name=None,
            notify_endpoint=None,
            project=None,
            external_id=None,
            src_uri=None,
            style=None,
            tgt_uri=None):
        api_request = APIRequest('PhotoProcess', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NotifyTopicName": notify_topic_name,
            "NotifyEndpoint": notify_endpoint,
            "Project": project,
            "ExternalID": external_id,
            "SrcUri": src_uri,
            "Style": style,
            "TgtUri": tgt_uri}
        return self._handle_request(api_request).result

    def delete_photo_process_task(self, project=None, task_id=None):
        api_request = APIRequest('DeletePhotoProcessTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "TaskId": task_id}
        return self._handle_request(api_request).result

    def get_photo_process_task(self, project=None, task_id=None):
        api_request = APIRequest('GetPhotoProcessTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "TaskId": task_id}
        return self._handle_request(api_request).result

    def list_photo_process_tasks(self, max_keys=None, marker=None, project=None):
        api_request = APIRequest('ListPhotoProcessTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MaxKeys": max_keys, "Marker": marker, "Project": project}
        return self._handle_request(api_request).result

    def delete_project(self, project=None):
        api_request = APIRequest('DeleteProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project}
        return self._handle_request(api_request).result

    def get_tag_set(self, project=None, set_id=None):
        api_request = APIRequest('GetTagSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project, "SetId": set_id}
        return self._handle_request(api_request).result

    def delete_tag_set(self, lazy_mode=None, project=None, set_id=None, check_empty=None):
        api_request = APIRequest('DeleteTagSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LazyMode": lazy_mode,
            "Project": project,
            "SetId": set_id,
            "CheckEmpty": check_empty}
        return self._handle_request(api_request).result

    def list_tag_sets(self, max_keys=None, marker=None, project=None):
        api_request = APIRequest('ListTagSets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MaxKeys": max_keys, "Marker": marker, "Project": project}
        return self._handle_request(api_request).result

    def create_tag_set(self, project=None):
        api_request = APIRequest('CreateTagSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project}
        return self._handle_request(api_request).result

    def index_tag(self, src_uris=None, model_id=None, project=None, set_id=None, force=None):
        api_request = APIRequest('IndexTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SrcUris": src_uris,
            "ModelId": model_id,
            "Project": project,
            "SetId": set_id,
            "Force": force}
        return self._handle_request(api_request).result

    def create_face_set(self, project=None):
        api_request = APIRequest('CreateFaceSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project}
        return self._handle_request(api_request).result

    def list_face_groups(
            self,
            marker=None,
            limit=None,
            project=None,
            set_id=None,
            order_by=None,
            order=None):
        api_request = APIRequest('ListFaceGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Marker": marker,
            "Limit": limit,
            "Project": project,
            "SetId": set_id,
            "OrderBy": order_by,
            "Order": order}
        return self._handle_request(api_request).result

    def delete_face_job(self, job_id=None, project=None, clear_index_data=None):
        api_request = APIRequest('DeleteFaceJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "Project": project,
            "ClearIndexData": clear_index_data}
        return self._handle_request(api_request).result

    def create_tag_job(
            self,
            notify_topic_name=None,
            notify_endpoint=None,
            project=None,
            external_id=None,
            src_uri=None):
        api_request = APIRequest('CreateTagJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NotifyTopicName": notify_topic_name,
            "NotifyEndpoint": notify_endpoint,
            "Project": project,
            "ExternalID": external_id,
            "SrcUri": src_uri}
        return self._handle_request(api_request).result

    def delete_tag_job(self, job_id=None, project=None, clear_index_data=None):
        api_request = APIRequest('DeleteTagJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "JobId": job_id,
            "Project": project,
            "ClearIndexData": clear_index_data}
        return self._handle_request(api_request).result

    def list_tag_jobs(self, condition=None, max_keys=None, marker=None, project=None):
        api_request = APIRequest('ListTagJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Condition": condition,
            "MaxKeys": max_keys,
            "Marker": marker,
            "Project": project}
        return self._handle_request(api_request).result

    def get_tag_job(self, job_id=None, project=None):
        api_request = APIRequest('GetTagJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JobId": job_id, "Project": project}
        return self._handle_request(api_request).result

    def detect_tag(self, src_uris=None, model_id=None, project=None):
        api_request = APIRequest('DetectTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SrcUris": src_uris, "ModelId": model_id, "Project": project}
        return self._handle_request(api_request).result

    def put_project(self, cu=None, service_role=None, project=None, billing_type=None, type_=None):
        api_request = APIRequest('PutProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "CU": cu,
            "ServiceRole": service_role,
            "Project": project,
            "BillingType": billing_type,
            "Type": type_}
        return self._handle_request(api_request).result

    def get_project(self, project=None):
        api_request = APIRequest('GetProject', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Project": project}
        return self._handle_request(api_request).result

    def list_projects(self, max_keys=None, marker=None):
        api_request = APIRequest('ListProjects', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MaxKeys": max_keys, "Marker": marker}
        return self._handle_request(api_request).result

    def delete_porn_batch_detect_job(self, job_id=None, project=None):
        api_request = APIRequest('DeletePornBatchDetectJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JobId": job_id, "Project": project}
        return self._handle_request(api_request).result

    def create_porn_batch_detect_job(
            self,
            notify_topic_name=None,
            notify_endpoint=None,
            project=None,
            external_id=None,
            src_uri=None,
            tgt_uri=None):
        api_request = APIRequest('CreatePornBatchDetectJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "NotifyTopicName": notify_topic_name,
            "NotifyEndpoint": notify_endpoint,
            "Project": project,
            "ExternalID": external_id,
            "SrcUri": src_uri,
            "TgtUri": tgt_uri}
        return self._handle_request(api_request).result

    def get_porn_batch_detect_job(self, job_id=None, project=None):
        api_request = APIRequest('GetPornBatchDetectJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JobId": job_id, "Project": project}
        return self._handle_request(api_request).result

    def list_porn_batch_detect_jobs(self, max_keys=None, marker=None, project=None):
        api_request = APIRequest('ListPornBatchDetectJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MaxKeys": max_keys, "Marker": marker, "Project": project}
        return self._handle_request(api_request).result
