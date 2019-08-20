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


class GreenClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Green'
        self.api_version = '2018-05-09'
        self.location_service_code = 'green'
        self.location_endpoint_type = 'openAPI'

    def detect_face(self, client_info=None):
        api_request = APIRequest('DetectFace', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/face/detect'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def list_similarity_images(self, client_info=None):
        api_request = APIRequest('ListSimilarityImages', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/similarity/image/list'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def list_similarity_libraries(self, client_info=None):
        api_request = APIRequest('ListSimilarityLibraries', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/similarity/library/list'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def add_similarity_library(self, client_info=None):
        api_request = APIRequest('AddSimilarityLibrary', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/similarity/library/add'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def delete_similarity_library(self, client_info=None):
        api_request = APIRequest('DeleteSimilarityLibrary', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/similarity/library/delete'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def get_similarity_library(self, client_info=None):
        api_request = APIRequest('GetSimilarityLibrary', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/similarity/library/get'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def get_similarity_image(self, client_info=None):
        api_request = APIRequest('GetSimilarityImage', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/similarity/image/get'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def add_video_dna(self, client_info=None):
        api_request = APIRequest('AddVideoDna', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/video/dna/add'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def add_video_dna_group(self, client_info=None):
        api_request = APIRequest('AddVideoDnaGroup', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/video/dna/group/add'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def delete_video_dna(self, client_info=None):
        api_request = APIRequest('DeleteVideoDna', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/video/dna/delete'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def delete_video_dna_group(self, client_info=None):
        api_request = APIRequest('DeleteVideoDnaGroup', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/video/dna/group/delete'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def get_add_video_dna_results(self, client_info=None):
        api_request = APIRequest('GetAddVideoDnaResults', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/video/dna/add/results'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def voice_cancel_scan(self, client_info=None):
        api_request = APIRequest('VoiceCancelScan', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/voice/cancelscan'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def upload_credentials(self, region_id=None, client_info=None):
        api_request = APIRequest('UploadCredentials', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/credentials/uploadcredentials'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def voice_identity_check(self, region_id=None, client_info=None):
        api_request = APIRequest('VoiceIdentityCheck', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/voice/auth/check'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def voice_identity_register(self, region_id=None, client_info=None):
        api_request = APIRequest('VoiceIdentityRegister', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/voice/auth/register'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def voice_identity_start_check(self, region_id=None, client_info=None):
        api_request = APIRequest('VoiceIdentityStartCheck', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/voice/auth/start/check'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def voice_identity_unregister(self, region_id=None, client_info=None):
        api_request = APIRequest('VoiceIdentityUnregister', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/voice/auth/unregister'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def voice_identity_start_register(self, region_id=None, client_info=None):
        api_request = APIRequest('VoiceIdentityStartRegister', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/voice/auth/start/register'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def video_sync_scan(self, client_info=None):
        api_request = APIRequest('VideoSyncScan', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/video/syncscan'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def video_async_scan_results(self, client_info=None):
        api_request = APIRequest('VideoAsyncScanResults', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/video/results'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def voice_async_scan_results(self, client_info=None):
        api_request = APIRequest('VoiceAsyncScanResults', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/voice/results'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def get_faces(self, region_id=None, client_info=None):
        api_request = APIRequest('GetFaces', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/sface/faces'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def add_groups(self, region_id=None, client_info=None):
        api_request = APIRequest('AddGroups', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/sface/person/groups/add'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def get_groups(self, region_id=None, client_info=None):
        api_request = APIRequest('GetGroups', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/sface/groups'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def get_persons(self, region_id=None, client_info=None):
        api_request = APIRequest('GetPersons', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/sface/group/persons'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def delete_similarity_image(self, client_info=None):
        api_request = APIRequest('DeleteSimilarityImage', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/similarity/image/delete'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def text_feedback(self, client_info=None):
        api_request = APIRequest('TextFeedback', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/text/feedback'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def add_faces(self, region_id=None, client_info=None):
        api_request = APIRequest('AddFaces', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/sface/face/add'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def set_person(self, region_id=None, client_info=None):
        api_request = APIRequest('SetPerson', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/sface/person/update'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def delete_person(self, region_id=None, client_info=None):
        api_request = APIRequest('DeletePerson', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/sface/person/delete'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def delete_faces(self, region_id=None, client_info=None):
        api_request = APIRequest('DeleteFaces', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/sface/face/delete'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def voice_async_scan(self, client_info=None):
        api_request = APIRequest('VoiceAsyncScan', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/voice/asyncscan'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def image_async_scan(self, client_info=None):
        api_request = APIRequest('ImageAsyncScan', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/image/asyncscan'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def image_sync_scan(self, client_info=None):
        api_request = APIRequest('ImageSyncScan', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/image/scan'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def get_person(self, region_id=None, client_info=None):
        api_request = APIRequest('GetPerson', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/sface/person'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def add_person(self, region_id=None, client_info=None):
        api_request = APIRequest('AddPerson', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/sface/person/add'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def video_feedback(self, client_info=None):
        api_request = APIRequest('VideoFeedback', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/video/feedback'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def file_async_scan_results(self, client_info=None):
        api_request = APIRequest('FileAsyncScanResults', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/file/results'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def add_similarity_image(self, client_info=None):
        api_request = APIRequest('AddSimilarityImage', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/similarity/image/add'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def image_scan_feedback(self, client_info=None):
        api_request = APIRequest('ImageScanFeedback', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/image/feedback'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def search_person(self, region_id=None, client_info=None):
        api_request = APIRequest('SearchPerson', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/sface/search'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result

    def image_async_scan_results(self, client_info=None):
        api_request = APIRequest('ImageAsyncScanResults', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/image/results'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def video_async_scan(self, client_info=None):
        api_request = APIRequest('VideoAsyncScan', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/video/asyncscan'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def text_scan(self, client_info=None):
        api_request = APIRequest('TextScan', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/text/scan'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def file_async_scan(self, client_info=None):
        api_request = APIRequest('FileAsyncScan', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/file/asyncscan'
        api_request._params = {"ClientInfo": client_info}
        return self._handle_request(api_request).result

    def delete_groups(self, region_id=None, client_info=None):
        api_request = APIRequest('DeleteGroups', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/green/sface/person/groups/delete'
        api_request._params = {"RegionId": region_id, "ClientInfo": client_info}
        return self._handle_request(api_request).result
