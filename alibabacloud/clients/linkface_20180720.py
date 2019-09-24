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


class LinkFaceClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'LinkFace'
        self.api_version = '2018-07-20'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def delete_device_group(self, iot_id=None, group_id=None, device_name=None, product_key=None):
        api_request = APIRequest('DeleteDeviceGroup', 'POST', 'https', 'RPC', 'body')
        api_request._params = {
            "IotId": iot_id,
            "GroupId": group_id,
            "DeviceName": device_name,
            "ProductKey": product_key}
        return self._handle_request(api_request).result

    def delete_device_all_group(self, iot_id=None, device_name=None, product_key=None):
        api_request = APIRequest('DeleteDeviceAllGroup', 'POST', 'https', 'RPC', 'body')
        api_request._params = {
            "IotId": iot_id,
            "DeviceName": device_name,
            "ProductKey": product_key}
        return self._handle_request(api_request).result

    def search_face(self, image=None, group_id=None):
        api_request = APIRequest('SearchFace', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"Image": image, "GroupId": group_id}
        return self._handle_request(api_request).result

    def query_licenses(self, license_type=None, page_size=None, current_page=None):
        api_request = APIRequest('QueryLicenses', 'POST', 'https', 'RPC', 'body')
        api_request._params = {
            "LicenseType": license_type,
            "PageSize": page_size,
            "CurrentPage": current_page}
        return self._handle_request(api_request).result

    def query_authentication(
            self,
            license_type=None,
            iot_id=None,
            page_size=None,
            current_page=None,
            device_name=None,
            product_key=None):
        api_request = APIRequest('QueryAuthentication', 'POST', 'https', 'RPC', 'body')
        api_request._params = {
            "LicenseType": license_type,
            "IotId": iot_id,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "DeviceName": device_name,
            "ProductKey": product_key}
        return self._handle_request(api_request).result

    def query_add_user_info(self, iot_id=None, group_id=None, device_name=None, product_key=None):
        api_request = APIRequest('QueryAddUserInfo', 'POST', 'https', 'RPC', 'body')
        api_request._params = {
            "IotId": iot_id,
            "GroupId": group_id,
            "DeviceName": device_name,
            "ProductKey": product_key}
        return self._handle_request(api_request).result

    def unlink_face(self, group_id=None, user_id=None):
        api_request = APIRequest('UnlinkFace', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"GroupId": group_id, "UserId": user_id}
        return self._handle_request(api_request).result

    def query_all_groups(self, page_size=None, current_page=None):
        api_request = APIRequest('QueryAllGroups', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"PageSize": page_size, "CurrentPage": current_page}
        return self._handle_request(api_request).result

    def sync_face_pictures(self, iot_id=None, group_id=None, device_name=None, product_key=None):
        api_request = APIRequest('SyncFacePictures', 'POST', 'https', 'RPC', 'body')
        api_request._params = {
            "IotId": iot_id,
            "GroupId": group_id,
            "DeviceName": device_name,
            "ProductKey": product_key}
        return self._handle_request(api_request).result

    def query_sync_pic_schedule(
            self,
            iot_id=None,
            group_id=None,
            device_name=None,
            product_key=None):
        api_request = APIRequest('QuerySyncPicSchedule', 'POST', 'https', 'RPC', 'body')
        api_request._params = {
            "IotId": iot_id,
            "GroupId": group_id,
            "DeviceName": device_name,
            "ProductKey": product_key}
        return self._handle_request(api_request).result

    def query_group_users(self, group_id=None, page_size=None, current_page=None):
        api_request = APIRequest('QueryGroupUsers', 'POST', 'https', 'RPC', 'body')
        api_request._params = {
            "GroupId": group_id,
            "PageSize": page_size,
            "CurrentPage": current_page}
        return self._handle_request(api_request).result

    def query_face(self, user_id=None):
        api_request = APIRequest('QueryFace', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"UserId": user_id}
        return self._handle_request(api_request).result

    def update_face(self, image=None, user_id=None, user_info=None):
        api_request = APIRequest('UpdateFace', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"Image": image, "UserId": user_id, "UserInfo": user_info}
        return self._handle_request(api_request).result

    def delete_face(self, group_id=None, user_id=None):
        api_request = APIRequest('DeleteFace', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"GroupId": group_id, "UserId": user_id}
        return self._handle_request(api_request).result

    def register_face(self, image=None, group_id=None, user_id=None, user_info=None):
        api_request = APIRequest('RegisterFace', 'POST', 'https', 'RPC', 'body')
        api_request._params = {
            "Image": image,
            "GroupId": group_id,
            "UserId": user_id,
            "UserInfo": user_info}
        return self._handle_request(api_request).result

    def link_face(self, group_id=None, user_id=None):
        api_request = APIRequest('LinkFace', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"GroupId": group_id, "UserId": user_id}
        return self._handle_request(api_request).result

    def delete_group(self, group_id=None):
        api_request = APIRequest('DeleteGroup', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"GroupId": group_id}
        return self._handle_request(api_request).result

    def create_group(self, group_id=None):
        api_request = APIRequest('CreateGroup', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"GroupId": group_id}
        return self._handle_request(api_request).result
