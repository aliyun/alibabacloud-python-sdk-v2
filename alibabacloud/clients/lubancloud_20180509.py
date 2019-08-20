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


class LubancloudClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'lubancloud'
        self.api_version = '2018-05-09'
        self.location_service_code = 'luban'
        self.location_endpoint_type = 'openAPI'

    def submit_cutout_task(self, list_of_picture_url=None):
        api_request = APIRequest('SubmitCutoutTask', 'POST', 'http', 'RPC', 'query')
        api_request._params = {"PictureUrl": list_of_picture_url}
        repeat_info = {"PictureUrl": ('PictureUrl', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def query_cutout_task_result(self, task_id=None):
        api_request = APIRequest('QueryCutoutTaskResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TaskId": task_id}
        return self._handle_request(api_request).result

    def submit_generate_task(
            self,
            image_count=None,
            action_point=None,
            logo_image_path=None,
            type_=None,
            list_of_major_image_path=None,
            width=None,
            list_of_copy_write=None,
            list_of_property_id=None,
            height=None):
        api_request = APIRequest('SubmitGenerateTask', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageCount": image_count,
            "ActionPoint": action_point,
            "LogoImagePath": logo_image_path,
            "Type": type_,
            "MajorImagePath": list_of_major_image_path,
            "Width": width,
            "CopyWrite": list_of_copy_write,
            "PropertyId": list_of_property_id,
            "Height": height}
        repeat_info = {"MajorImagePath": ('MajorImagePath', 'list', 'str', None),
                       "CopyWrite": ('CopyWrite', 'list', 'str', None),
                       "PropertyId": ('PropertyId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def query_generate_task_result(self, task_id=None):
        api_request = APIRequest('QueryGenerateTaskResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TaskId": task_id}
        return self._handle_request(api_request).result

    def get_styles(self,):
        api_request = APIRequest('GetStyles', 'POST', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def buy_origin_pictures(self, list_of_picture_id=None):
        api_request = APIRequest('BuyOriginPictures', 'POST', 'http', 'RPC', 'query')
        api_request._params = {"PictureId": list_of_picture_id}
        repeat_info = {"PictureId": ('PictureId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result
