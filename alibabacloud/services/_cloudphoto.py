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
from alibabacloud.utils.utils import _transfer_params


class _CLOUDPHOTOResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'cloudphoto', _client=_client)

    def create_photo_store(self, **params):
        _params = _transfer_params(params)
        self._client.create_photo_store(**_params)
        photo_store_name = _params.get("photo_store_name")
        return _CLOUDPHOTOPhotoStoreResource(photo_store_name, _client=self._client)


class _CLOUDPHOTOPhotoStoreResource(ServiceResource):

    def __init__(self, photo_store_name, _client=None):
        ServiceResource.__init__(self, "cloudphoto.photo_store", _client=_client)
        self.photo_store_name = photo_store_name

    def activate_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.activate_photos(photo_store_name=self.photo_store_name, **_params)

    def add_album_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.add_album_photos(photo_store_name=self.photo_store_name, **_params)

    def create_album(self, **params):
        _params = _transfer_params(params)
        return self._client.create_album(photo_store_name=self.photo_store_name, **_params)

    def create_event(self, **params):
        _params = _transfer_params(params)
        return self._client.create_event(photo_store_name=self.photo_store_name, **_params)

    def create_photo(self, **params):
        _params = _transfer_params(params)
        return self._client.create_photo(photo_store_name=self.photo_store_name, **_params)

    def create_transaction(self, **params):
        _params = _transfer_params(params)
        return self._client.create_transaction(photo_store_name=self.photo_store_name, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_photo_store(photo_store_name=self.photo_store_name, **_params)

    def delete_albums(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_albums(photo_store_name=self.photo_store_name, **_params)

    def delete_event(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_event(photo_store_name=self.photo_store_name, **_params)

    def delete_faces(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_faces(photo_store_name=self.photo_store_name, **_params)

    def delete_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_photos(photo_store_name=self.photo_store_name, **_params)

    def edit(self, **params):
        _params = _transfer_params(params)
        return self._client.edit_photo_store(photo_store_name=self.photo_store_name, **_params)

    def edit_event(self, **params):
        _params = _transfer_params(params)
        return self._client.edit_event(photo_store_name=self.photo_store_name, **_params)

    def edit_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.edit_photos(photo_store_name=self.photo_store_name, **_params)

    def fetch_album_tag_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.fetch_album_tag_photos(photo_store_name=self.photo_store_name,
                                                   **_params)

    def fetch_libraries(self, **params):
        _params = _transfer_params(params)
        return self._client.fetch_libraries(photo_store_name=self.photo_store_name, **_params)

    def fetch_moment_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.fetch_moment_photos(photo_store_name=self.photo_store_name, **_params)

    def fetch_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.fetch_photos(photo_store_name=self.photo_store_name, **_params)

    def get(self, **params):
        _params = _transfer_params(params)
        return self._client.get_photo_store(photo_store_name=self.photo_store_name, **_params)

    def get_albums_by_names(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_albums_by_names(photo_store_name=self.photo_store_name,
                                                    **_params)
        return response

    def get_download_urls(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_download_urls(photo_store_name=self.photo_store_name, **_params)
        return response

    def get_event(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_event(photo_store_name=self.photo_store_name, **_params)
        return response

    def get_framed_photo_urls(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_framed_photo_urls(photo_store_name=self.photo_store_name,
                                                      **_params)
        return response

    def get_library(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_library(photo_store_name=self.photo_store_name, **_params)
        return response

    def get_photos(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_photos(photo_store_name=self.photo_store_name, **_params)
        return response

    def get_photos_by_md5s(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_photos_by_md5s(photo_store_name=self.photo_store_name,
                                                   **_params)
        return response

    def get_private_access_urls(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_private_access_urls(photo_store_name=self.photo_store_name,
                                                        **_params)
        return response

    def get_public_access_urls(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_public_access_urls(photo_store_name=self.photo_store_name,
                                                       **_params)
        return response

    def get_quota(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_quota(photo_store_name=self.photo_store_name, **_params)
        return response

    def get_similar_photos(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_similar_photos(photo_store_name=self.photo_store_name,
                                                   **_params)
        return response

    def get_thumbnails(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_thumbnails(photo_store_name=self.photo_store_name, **_params)
        return response

    def inactivate_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.inactivate_photos(photo_store_name=self.photo_store_name, **_params)

    def like_photo(self, **params):
        _params = _transfer_params(params)
        return self._client.like_photo(photo_store_name=self.photo_store_name, **_params)

    def list_album_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.list_album_photos(photo_store_name=self.photo_store_name, **_params)

    def list_albums(self, **params):
        _params = _transfer_params(params)
        return self._client.list_albums(photo_store_name=self.photo_store_name, **_params)

    def list_events(self, **params):
        _params = _transfer_params(params)
        return self._client.list_events(photo_store_name=self.photo_store_name, **_params)

    def list_face_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.list_face_photos(photo_store_name=self.photo_store_name, **_params)

    def list_faces(self, **params):
        _params = _transfer_params(params)
        return self._client.list_faces(photo_store_name=self.photo_store_name, **_params)

    def list_moment_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.list_moment_photos(photo_store_name=self.photo_store_name, **_params)

    def list_moments(self, **params):
        _params = _transfer_params(params)
        return self._client.list_moments(photo_store_name=self.photo_store_name, **_params)

    def list_photo_faces(self, **params):
        _params = _transfer_params(params)
        return self._client.list_photo_faces(photo_store_name=self.photo_store_name, **_params)

    def list_photo_tags(self, **params):
        _params = _transfer_params(params)
        return self._client.list_photo_tags(photo_store_name=self.photo_store_name, **_params)

    def list_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.list_photos(photo_store_name=self.photo_store_name, **_params)

    def list_registered_tags(self, **params):
        _params = _transfer_params(params)
        return self._client.list_registered_tags(photo_store_name=self.photo_store_name, **_params)

    def list_tag_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.list_tag_photos(photo_store_name=self.photo_store_name, **_params)

    def list_tags(self, **params):
        _params = _transfer_params(params)
        return self._client.list_tags(photo_store_name=self.photo_store_name, **_params)

    def list_time_line_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.list_time_line_photos(photo_store_name=self.photo_store_name, **_params)

    def list_time_lines(self, **params):
        _params = _transfer_params(params)
        return self._client.list_time_lines(photo_store_name=self.photo_store_name, **_params)

    def merge_faces(self, **params):
        _params = _transfer_params(params)
        return self._client.merge_faces(photo_store_name=self.photo_store_name, **_params)

    def move_album_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.move_album_photos(photo_store_name=self.photo_store_name, **_params)

    def move_face_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.move_face_photos(photo_store_name=self.photo_store_name, **_params)

    def reactivate_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.reactivate_photos(photo_store_name=self.photo_store_name, **_params)

    def register_photo(self, **params):
        _params = _transfer_params(params)
        return self._client.register_photo(photo_store_name=self.photo_store_name, **_params)

    def register_tag(self, **params):
        _params = _transfer_params(params)
        return self._client.register_tag(photo_store_name=self.photo_store_name, **_params)

    def remove_album_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_album_photos(photo_store_name=self.photo_store_name, **_params)

    def remove_face_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.remove_face_photos(photo_store_name=self.photo_store_name, **_params)

    def rename_album(self, **params):
        _params = _transfer_params(params)
        return self._client.rename_album(photo_store_name=self.photo_store_name, **_params)

    def rename_face(self, **params):
        _params = _transfer_params(params)
        return self._client.rename_face(photo_store_name=self.photo_store_name, **_params)

    def search_photos(self, **params):
        _params = _transfer_params(params)
        return self._client.search_photos(photo_store_name=self.photo_store_name, **_params)

    def set_album_cover(self, **params):
        _params = _transfer_params(params)
        return self._client.set_album_cover(photo_store_name=self.photo_store_name, **_params)

    def set_me(self, **params):
        _params = _transfer_params(params)
        return self._client.set_me(photo_store_name=self.photo_store_name, **_params)

    def set_quota(self, **params):
        _params = _transfer_params(params)
        return self._client.set_quota(photo_store_name=self.photo_store_name, **_params)

    def tag_photo(self, **params):
        _params = _transfer_params(params)
        return self._client.tag_photo(photo_store_name=self.photo_store_name, **_params)

    def toggle_features(self, **params):
        _params = _transfer_params(params)
        return self._client.toggle_features(photo_store_name=self.photo_store_name, **_params)

    def get_download_url(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_download_url(photo_store_name=self.photo_store_name, **_params)
        return response

    def get_thumbnail(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_thumbnail(photo_store_name=self.photo_store_name, **_params)
        return response

    def get_video_cover(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_video_cover(photo_store_name=self.photo_store_name, **_params)
        return response

    def set_face_cover(self, **params):
        _params = _transfer_params(params)
        return self._client.set_face_cover(photo_store_name=self.photo_store_name, **_params)
