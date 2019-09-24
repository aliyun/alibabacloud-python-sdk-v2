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


class CloudPhotoClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'CloudPhoto'
        self.api_version = '2017-07-11'
        self.location_service_code = 'cloudphoto'
        self.location_endpoint_type = 'openAPI'

    def fetch_photos(
            self,
            size=None,
            library_id=None,
            order_by=None,
            store_name=None,
            state=None,
            page=None,
            order=None):
        api_request = APIRequest('FetchPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Size": size,
            "LibraryId": library_id,
            "OrderBy": order_by,
            "StoreName": store_name,
            "State": state,
            "Page": page,
            "Order": order}
        return self._handle_request(api_request).result

    def fetch_moment_photos(
            self,
            size=None,
            library_id=None,
            order_by=None,
            store_name=None,
            page=None,
            moment_id=None,
            order=None):
        api_request = APIRequest('FetchMomentPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Size": size,
            "LibraryId": library_id,
            "OrderBy": order_by,
            "StoreName": store_name,
            "Page": page,
            "MomentId": moment_id,
            "Order": order}
        return self._handle_request(api_request).result

    def fetch_libraries(self, size=None, need_quota=None, store_name=None, page=None):
        api_request = APIRequest('FetchLibraries', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Size": size,
            "NeedQuota": need_quota,
            "StoreName": store_name,
            "Page": page}
        return self._handle_request(api_request).result

    def fetch_album_tag_photos(
            self,
            size=None,
            tag_id=None,
            library_id=None,
            album_id=None,
            store_name=None,
            page=None):
        api_request = APIRequest('FetchAlbumTagPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Size": size,
            "TagId": tag_id,
            "LibraryId": library_id,
            "AlbumId": album_id,
            "StoreName": store_name,
            "Page": page}
        return self._handle_request(api_request).result

    def get_albums_by_names(self, library_id=None, list_of_name=None, store_name=None):
        api_request = APIRequest('GetAlbumsByNames', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "Name": list_of_name,
            "StoreName": store_name}
        repeat_info = {"Name": ('Name', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_event(self, event_id=None, library_id=None, store_name=None):
        api_request = APIRequest('GetEvent', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "EventId": event_id,
            "LibraryId": library_id,
            "StoreName": store_name}
        return self._handle_request(api_request).result

    def edit_event(
            self,
            event_id=None,
            banner_photo_id=None,
            watermark_photo_id=None,
            identity=None,
            splash_photo_id=None,
            library_id=None,
            weixin_title=None,
            store_name=None,
            remark=None,
            title=None,
            end_at=None,
            start_at=None):
        api_request = APIRequest('EditEvent', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "EventId": event_id,
            "BannerPhotoId": banner_photo_id,
            "WatermarkPhotoId": watermark_photo_id,
            "Identity": identity,
            "SplashPhotoId": splash_photo_id,
            "LibraryId": library_id,
            "WeixinTitle": weixin_title,
            "StoreName": store_name,
            "Remark": remark,
            "Title": title,
            "EndAt": end_at,
            "StartAt": start_at}
        return self._handle_request(api_request).result

    def list_events(self, cursor=None, size=None, store_name=None, state=None, direction=None):
        api_request = APIRequest('ListEvents', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Cursor": cursor,
            "Size": size,
            "StoreName": store_name,
            "State": state,
            "Direction": direction}
        return self._handle_request(api_request).result

    def delete_event(self, event_id=None, library_id=None, store_name=None):
        api_request = APIRequest('DeleteEvent', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "EventId": event_id,
            "LibraryId": library_id,
            "StoreName": store_name}
        return self._handle_request(api_request).result

    def create_event(
            self,
            banner_photo_id=None,
            watermark_photo_id=None,
            identity=None,
            splash_photo_id=None,
            library_id=None,
            weixin_title=None,
            store_name=None,
            remark=None,
            title=None,
            end_at=None,
            start_at=None):
        api_request = APIRequest('CreateEvent', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "BannerPhotoId": banner_photo_id,
            "WatermarkPhotoId": watermark_photo_id,
            "Identity": identity,
            "SplashPhotoId": splash_photo_id,
            "LibraryId": library_id,
            "WeixinTitle": weixin_title,
            "StoreName": store_name,
            "Remark": remark,
            "Title": title,
            "EndAt": end_at,
            "StartAt": start_at}
        return self._handle_request(api_request).result

    def register_photo(
            self,
            library_id=None,
            latitude=None,
            photo_title=None,
            store_name=None,
            is_video=None,
            remark=None,
            size=None,
            taken_at=None,
            width=None,
            location=None,
            longitude=None,
            height=None,
            md5=None):
        api_request = APIRequest('RegisterPhoto', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "Latitude": latitude,
            "PhotoTitle": photo_title,
            "StoreName": store_name,
            "IsVideo": is_video,
            "Remark": remark,
            "Size": size,
            "TakenAt": taken_at,
            "Width": width,
            "Location": location,
            "Longitude": longitude,
            "Height": height,
            "Md5": md5}
        return self._handle_request(api_request).result

    def get_similar_photos(self, library_id=None, photo_id=None, store_name=None):
        api_request = APIRequest('GetSimilarPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": photo_id,
            "StoreName": store_name}
        return self._handle_request(api_request).result

    def tag_photo(
            self,
            library_id=None,
            list_of_confidence=None,
            store_name=None,
            photo_id=None,
            list_of_tag_key=None):
        api_request = APIRequest('TagPhoto', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "Confidence": list_of_confidence,
            "StoreName": store_name,
            "PhotoId": photo_id,
            "TagKey": list_of_tag_key}
        repeat_info = {"Confidence": ('Confidence', 'list', 'str', None),
                       "TagKey": ('TagKey', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def register_tag(self, store_name=None, text=None, tag_key=None, lang=None):
        api_request = APIRequest('RegisterTag', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "StoreName": store_name,
            "Text": text,
            "TagKey": tag_key,
            "Lang": lang}
        return self._handle_request(api_request).result

    def list_registered_tags(self, store_name=None, list_of_lang=None):
        api_request = APIRequest('ListRegisteredTags', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"StoreName": store_name, "Lang": list_of_lang}
        repeat_info = {"Lang": ('Lang', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_library(self, library_id=None, store_name=None):
        api_request = APIRequest('GetLibrary', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"LibraryId": library_id, "StoreName": store_name}
        return self._handle_request(api_request).result

    def edit_photo_store(
            self,
            auto_clean_enabled=None,
            default_trash_quota=None,
            store_name=None,
            remark=None,
            default_quota=None,
            auto_clean_days=None):
        api_request = APIRequest('EditPhotoStore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "AutoCleanEnabled": auto_clean_enabled,
            "DefaultTrashQuota": default_trash_quota,
            "StoreName": store_name,
            "Remark": remark,
            "DefaultQuota": default_quota,
            "AutoCleanDays": auto_clean_days}
        return self._handle_request(api_request).result

    def toggle_features(
            self,
            list_of_disabled_features=None,
            store_name=None,
            list_of_enabled_features=None):
        api_request = APIRequest('ToggleFeatures', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "DisabledFeatures": list_of_disabled_features,
            "StoreName": store_name,
            "EnabledFeatures": list_of_enabled_features}
        repeat_info = {"DisabledFeatures": ('DisabledFeatures', 'list', 'str', None),
                       "EnabledFeatures": ('EnabledFeatures', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_time_lines(
            self,
            cursor=None,
            photo_size=None,
            time_line_count=None,
            library_id=None,
            store_name=None,
            time_line_unit=None,
            filter_by=None,
            direction=None,
            order=None):
        api_request = APIRequest('ListTimeLines', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Cursor": cursor,
            "PhotoSize": photo_size,
            "TimeLineCount": time_line_count,
            "LibraryId": library_id,
            "StoreName": store_name,
            "TimeLineUnit": time_line_unit,
            "FilterBy": filter_by,
            "Direction": direction,
            "Order": order}
        return self._handle_request(api_request).result

    def list_photo_faces(self, library_id=None, photo_id=None, store_name=None):
        api_request = APIRequest('ListPhotoFaces', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": photo_id,
            "StoreName": store_name}
        return self._handle_request(api_request).result

    def list_time_line_photos(
            self,
            size=None,
            library_id=None,
            end_time=None,
            store_name=None,
            page=None,
            start_time=None,
            filter_by=None,
            direction=None,
            order=None):
        api_request = APIRequest('ListTimeLinePhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Size": size,
            "LibraryId": library_id,
            "EndTime": end_time,
            "StoreName": store_name,
            "Page": page,
            "StartTime": start_time,
            "FilterBy": filter_by,
            "Direction": direction,
            "Order": order}
        return self._handle_request(api_request).result

    def like_photo(self, library_id=None, photo_id=None, store_name=None):
        api_request = APIRequest('LikePhoto', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": photo_id,
            "StoreName": store_name}
        return self._handle_request(api_request).result

    def get_public_access_urls(
            self,
            domain_type=None,
            library_id=None,
            list_of_photo_id=None,
            store_name=None,
            zoom_type=None):
        api_request = APIRequest('GetPublicAccessUrls', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "DomainType": domain_type,
            "LibraryId": library_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name,
            "ZoomType": zoom_type}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_private_access_urls(
            self,
            library_id=None,
            list_of_photo_id=None,
            store_name=None,
            zoom_type=None):
        api_request = APIRequest('GetPrivateAccessUrls', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name,
            "ZoomType": zoom_type}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_photos_by_md5s(self, library_id=None, store_name=None, state=None, list_of_md5=None):
        api_request = APIRequest('GetPhotosByMd5s', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "StoreName": store_name,
            "State": state,
            "Md5": list_of_md5}
        repeat_info = {"Md5": ('Md5', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_framed_photo_urls(
            self,
            frame_id=None,
            library_id=None,
            list_of_photo_id=None,
            store_name=None):
        api_request = APIRequest('GetFramedPhotoUrls', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "FrameId": frame_id,
            "LibraryId": library_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def edit_photos(
            self,
            taken_at=None,
            library_id=None,
            share_expire_time=None,
            list_of_photo_id=None,
            store_name=None,
            remark=None,
            title=None):
        api_request = APIRequest('EditPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "TakenAt": taken_at,
            "LibraryId": library_id,
            "ShareExpireTime": share_expire_time,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name,
            "Remark": remark,
            "Title": title}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def activate_photos(self, library_id=None, list_of_photo_id=None, store_name=None):
        api_request = APIRequest('ActivatePhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_thumbnails(
            self,
            library_id=None,
            list_of_photo_id=None,
            store_name=None,
            zoom_type=None):
        api_request = APIRequest('GetThumbnails', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name,
            "ZoomType": zoom_type}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_download_urls(self, library_id=None, list_of_photo_id=None, store_name=None):
        api_request = APIRequest('GetDownloadUrls', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_photos(self, library_id=None, list_of_photo_id=None, store_name=None):
        api_request = APIRequest('GetPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def set_face_cover(self, library_id=None, photo_id=None, store_name=None, face_id=None):
        api_request = APIRequest('SetFaceCover', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": photo_id,
            "StoreName": store_name,
            "FaceId": face_id}
        return self._handle_request(api_request).result

    def set_quota(self, total_quota=None, library_id=None, store_name=None):
        api_request = APIRequest('SetQuota', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "TotalQuota": total_quota,
            "LibraryId": library_id,
            "StoreName": store_name}
        return self._handle_request(api_request).result

    def set_me(self, library_id=None, store_name=None, face_id=None):
        api_request = APIRequest('SetMe', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"LibraryId": library_id, "StoreName": store_name, "FaceId": face_id}
        return self._handle_request(api_request).result

    def set_album_cover(self, library_id=None, album_id=None, photo_id=None, store_name=None):
        api_request = APIRequest('SetAlbumCover', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "AlbumId": album_id,
            "PhotoId": photo_id,
            "StoreName": store_name}
        return self._handle_request(api_request).result

    def search_photos(self, size=None, library_id=None, store_name=None, page=None, keyword=None):
        api_request = APIRequest('SearchPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Size": size,
            "LibraryId": library_id,
            "StoreName": store_name,
            "Page": page,
            "Keyword": keyword}
        return self._handle_request(api_request).result

    def rename_face(self, library_id=None, store_name=None, face_id=None, face_name=None):
        api_request = APIRequest('RenameFace', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "StoreName": store_name,
            "FaceId": face_id,
            "FaceName": face_name}
        return self._handle_request(api_request).result

    def rename_album(self, album_name=None, library_id=None, album_id=None, store_name=None):
        api_request = APIRequest('RenameAlbum', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "AlbumName": album_name,
            "LibraryId": library_id,
            "AlbumId": album_id,
            "StoreName": store_name}
        return self._handle_request(api_request).result

    def remove_face_photos(
            self,
            library_id=None,
            list_of_photo_id=None,
            store_name=None,
            face_id=None):
        api_request = APIRequest('RemoveFacePhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name,
            "FaceId": face_id}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def remove_album_photos(
            self,
            library_id=None,
            album_id=None,
            list_of_photo_id=None,
            store_name=None):
        api_request = APIRequest('RemoveAlbumPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "AlbumId": album_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def reactivate_photos(self, library_id=None, list_of_photo_id=None, store_name=None):
        api_request = APIRequest('ReactivatePhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def move_face_photos(
            self,
            library_id=None,
            target_face_id=None,
            list_of_photo_id=None,
            store_name=None,
            source_face_id=None):
        api_request = APIRequest('MoveFacePhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "TargetFaceId": target_face_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name,
            "SourceFaceId": source_face_id}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def move_album_photos(
            self,
            source_album_id=None,
            target_album_id=None,
            library_id=None,
            list_of_photo_id=None,
            store_name=None):
        api_request = APIRequest('MoveAlbumPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "SourceAlbumId": source_album_id,
            "TargetAlbumId": target_album_id,
            "LibraryId": library_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def merge_faces(
            self,
            library_id=None,
            target_face_id=None,
            store_name=None,
            list_of_face_id=None):
        api_request = APIRequest('MergeFaces', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "TargetFaceId": target_face_id,
            "StoreName": store_name,
            "FaceId": list_of_face_id}
        repeat_info = {"FaceId": ('FaceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_tags(self, library_id=None, store_name=None, lang=None):
        api_request = APIRequest('ListTags', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"LibraryId": library_id, "StoreName": store_name, "Lang": lang}
        return self._handle_request(api_request).result

    def list_tag_photos(
            self,
            cursor=None,
            size=None,
            tag_id=None,
            library_id=None,
            store_name=None,
            state=None,
            direction=None):
        api_request = APIRequest('ListTagPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Cursor": cursor,
            "Size": size,
            "TagId": tag_id,
            "LibraryId": library_id,
            "StoreName": store_name,
            "State": state,
            "Direction": direction}
        return self._handle_request(api_request).result

    def list_photo_tags(self, library_id=None, photo_id=None, store_name=None, lang=None):
        api_request = APIRequest('ListPhotoTags', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": photo_id,
            "StoreName": store_name,
            "Lang": lang}
        return self._handle_request(api_request).result

    def list_photo_stores(self,):
        api_request = APIRequest('ListPhotoStores', 'GET', 'https', 'RPC', '')

        return self._handle_request(api_request).result

    def list_photos(
            self,
            cursor=None,
            size=None,
            library_id=None,
            store_name=None,
            state=None,
            direction=None):
        api_request = APIRequest('ListPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Cursor": cursor,
            "Size": size,
            "LibraryId": library_id,
            "StoreName": store_name,
            "State": state,
            "Direction": direction}
        return self._handle_request(api_request).result

    def list_moments(
            self,
            cursor=None,
            size=None,
            library_id=None,
            store_name=None,
            state=None,
            direction=None):
        api_request = APIRequest('ListMoments', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Cursor": cursor,
            "Size": size,
            "LibraryId": library_id,
            "StoreName": store_name,
            "State": state,
            "Direction": direction}
        return self._handle_request(api_request).result

    def list_moment_photos(
            self,
            cursor=None,
            size=None,
            library_id=None,
            store_name=None,
            state=None,
            moment_id=None,
            direction=None):
        api_request = APIRequest('ListMomentPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Cursor": cursor,
            "Size": size,
            "LibraryId": library_id,
            "StoreName": store_name,
            "State": state,
            "MomentId": moment_id,
            "Direction": direction}
        return self._handle_request(api_request).result

    def list_faces(
            self,
            cursor=None,
            has_face_name=None,
            size=None,
            library_id=None,
            store_name=None,
            state=None,
            direction=None):
        api_request = APIRequest('ListFaces', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Cursor": cursor,
            "HasFaceName": has_face_name,
            "Size": size,
            "LibraryId": library_id,
            "StoreName": store_name,
            "State": state,
            "Direction": direction}
        return self._handle_request(api_request).result

    def list_face_photos(
            self,
            cursor=None,
            size=None,
            library_id=None,
            store_name=None,
            face_id=None,
            state=None,
            direction=None):
        api_request = APIRequest('ListFacePhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Cursor": cursor,
            "Size": size,
            "LibraryId": library_id,
            "StoreName": store_name,
            "FaceId": face_id,
            "State": state,
            "Direction": direction}
        return self._handle_request(api_request).result

    def list_albums(
            self,
            cursor=None,
            size=None,
            library_id=None,
            store_name=None,
            state=None,
            direction=None):
        api_request = APIRequest('ListAlbums', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Cursor": cursor,
            "Size": size,
            "LibraryId": library_id,
            "StoreName": store_name,
            "State": state,
            "Direction": direction}
        return self._handle_request(api_request).result

    def list_album_photos(
            self,
            cursor=None,
            size=None,
            library_id=None,
            album_id=None,
            store_name=None,
            state=None,
            direction=None):
        api_request = APIRequest('ListAlbumPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Cursor": cursor,
            "Size": size,
            "LibraryId": library_id,
            "AlbumId": album_id,
            "StoreName": store_name,
            "State": state,
            "Direction": direction}
        return self._handle_request(api_request).result

    def inactivate_photos(
            self,
            library_id=None,
            list_of_photo_id=None,
            store_name=None,
            inactive_time=None):
        api_request = APIRequest('InactivatePhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name,
            "InactiveTime": inactive_time}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_video_cover(self, library_id=None, photo_id=None, store_name=None, zoom_type=None):
        api_request = APIRequest('GetVideoCover', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": photo_id,
            "StoreName": store_name,
            "ZoomType": zoom_type}
        return self._handle_request(api_request).result

    def get_thumbnail(self, library_id=None, photo_id=None, store_name=None, zoom_type=None):
        api_request = APIRequest('GetThumbnail', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": photo_id,
            "StoreName": store_name,
            "ZoomType": zoom_type}
        return self._handle_request(api_request).result

    def get_quota(self, library_id=None, store_name=None):
        api_request = APIRequest('GetQuota', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"LibraryId": library_id, "StoreName": store_name}
        return self._handle_request(api_request).result

    def get_photo_store(self, store_name=None):
        api_request = APIRequest('GetPhotoStore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"StoreName": store_name}
        return self._handle_request(api_request).result

    def get_download_url(self, library_id=None, photo_id=None, store_name=None):
        api_request = APIRequest('GetDownloadUrl', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "PhotoId": photo_id,
            "StoreName": store_name}
        return self._handle_request(api_request).result

    def delete_photo_store(self, store_name=None):
        api_request = APIRequest('DeletePhotoStore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"StoreName": store_name}
        return self._handle_request(api_request).result

    def delete_photos(self, library_id=None, store_name=None, list_of_photo_id=None):
        api_request = APIRequest('DeletePhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "StoreName": store_name,
            "PhotoId": list_of_photo_id}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_faces(self, library_id=None, store_name=None, list_of_face_id=None):
        api_request = APIRequest('DeleteFaces', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "StoreName": store_name,
            "FaceId": list_of_face_id}
        repeat_info = {"FaceId": ('FaceId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_albums(self, library_id=None, list_of_album_id=None, store_name=None):
        api_request = APIRequest('DeleteAlbums', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "AlbumId": list_of_album_id,
            "StoreName": store_name}
        repeat_info = {"AlbumId": ('AlbumId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_transaction(
            self,
            ext=None,
            size=None,
            library_id=None,
            store_name=None,
            force=None,
            md5=None):
        api_request = APIRequest('CreateTransaction', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "Ext": ext,
            "Size": size,
            "LibraryId": library_id,
            "StoreName": store_name,
            "Force": force,
            "Md5": md5}
        return self._handle_request(api_request).result

    def create_photo_store(
            self,
            bucket_name=None,
            store_name=None,
            remark=None,
            default_quota=None):
        api_request = APIRequest('CreatePhotoStore', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "BucketName": bucket_name,
            "StoreName": store_name,
            "Remark": remark,
            "DefaultQuota": default_quota}
        return self._handle_request(api_request).result

    def create_photo(
            self,
            taken_at=None,
            photo_title=None,
            library_id=None,
            share_expire_time=None,
            store_name=None,
            upload_type=None,
            remark=None,
            session_id=None,
            staging=None,
            file_id=None):
        api_request = APIRequest('CreatePhoto', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "TakenAt": taken_at,
            "PhotoTitle": photo_title,
            "LibraryId": library_id,
            "ShareExpireTime": share_expire_time,
            "StoreName": store_name,
            "UploadType": upload_type,
            "Remark": remark,
            "SessionId": session_id,
            "Staging": staging,
            "FileId": file_id}
        return self._handle_request(api_request).result

    def create_album(self, album_name=None, library_id=None, store_name=None, remark=None):
        api_request = APIRequest('CreateAlbum', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "AlbumName": album_name,
            "LibraryId": library_id,
            "StoreName": store_name,
            "Remark": remark}
        return self._handle_request(api_request).result

    def add_album_photos(
            self,
            library_id=None,
            album_id=None,
            list_of_photo_id=None,
            store_name=None):
        api_request = APIRequest('AddAlbumPhotos', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "LibraryId": library_id,
            "AlbumId": album_id,
            "PhotoId": list_of_photo_id,
            "StoreName": store_name}
        repeat_info = {"PhotoId": ('PhotoId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result
