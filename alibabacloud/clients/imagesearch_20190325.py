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


class ImageSearchClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'ImageSearch'
        self.api_version = '2019-03-25'
        self.location_service_code = 'imagesearch'
        self.location_endpoint_type = 'openAPI'

    def add_image(
            self,
            pic_content=None,
            str_attr=None,
            instance_name=None,
            int_attr=None,
            product_id=None,
            pic_name=None,
            custom_content=None,
            region=None,
            category_id=None,
            crop=None):
        api_request = APIRequest('AddImage', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/v2/image/add'
        api_request._params = {
            "PicContent": pic_content,
            "StrAttr": str_attr,
            "InstanceName": instance_name,
            "IntAttr": int_attr,
            "ProductId": product_id,
            "PicName": pic_name,
            "CustomContent": custom_content,
            "Region": region,
            "CategoryId": category_id,
            "Crop": crop}
        return self._handle_request(api_request).result

    def delete_image(self, instance_name=None, product_id=None, pic_name=None):
        api_request = APIRequest('DeleteImage', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/v2/image/delete'
        api_request._params = {
            "InstanceName": instance_name,
            "ProductId": product_id,
            "PicName": pic_name}
        return self._handle_request(api_request).result

    def search_image(
            self,
            filter_=None,
            pic_content=None,
            instance_name=None,
            product_id=None,
            num=None,
            pic_name=None,
            start=None,
            region=None,
            type_=None,
            category_id=None,
            crop=None):
        api_request = APIRequest('SearchImage', 'POST', 'http', 'ROA', 'body')
        api_request.uri_pattern = '/v2/image/search'
        api_request._params = {
            "Filter": filter_,
            "PicContent": pic_content,
            "InstanceName": instance_name,
            "ProductId": product_id,
            "Num": num,
            "PicName": pic_name,
            "Start": start,
            "Region": region,
            "Type": type_,
            "CategoryId": category_id,
            "Crop": crop}
        return self._handle_request(api_request).result
