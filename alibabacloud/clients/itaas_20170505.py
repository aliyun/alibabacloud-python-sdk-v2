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


class ITaaSClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'ITaaS'
        self.api_version = '2017-05-05'
        self.location_service_code = 'itaas'
        self.location_endpoint_type = 'openAPI'

    def update_room_name(
            self,
            clientappid=None,
            region_id=None,
            drname=None,
            sysfrom=None,
            operator=None,
            screencode=None):
        api_request = APIRequest('UpdateRoomName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Drname": drname,
            "Sysfrom": sysfrom,
            "Operator": operator,
            "Screencode": screencode}
        return self._handle_request(api_request).result

    def update_ip_segment(
            self,
            clientappid=None,
            region_id=None,
            ipsegment=None,
            memo=None,
            sysfrom=None,
            uuid=None,
            operator=None):
        api_request = APIRequest('UpdateIPSegment', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Ipsegment": ipsegment,
            "Memo": memo,
            "Sysfrom": sysfrom,
            "Uuid": uuid,
            "Operator": operator}
        return self._handle_request(api_request).result

    def update_enterprise_config(
            self,
            config_key=None,
            clientappid=None,
            region_id=None,
            config_value=None,
            memo=None,
            sysfrom=None,
            operator=None):
        api_request = APIRequest('UpdateEnterpriseConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ConfigKey": config_key,
            "Clientappid": clientappid,
            "RegionId": region_id,
            "ConfigValue": config_value,
            "Memo": memo,
            "Sysfrom": sysfrom,
            "Operator": operator}
        return self._handle_request(api_request).result

    def set_welcome_page_uri(
            self,
            clientappid=None,
            region_id=None,
            sysfrom=None,
            operator=None,
            welcomeuri=None):
        api_request = APIRequest('SetWelcomePageURI', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Sysfrom": sysfrom,
            "Operator": operator,
            "Welcomeuri": welcomeuri}
        return self._handle_request(api_request).result

    def remove_register_box(
            self,
            clientappid=None,
            region_id=None,
            drsessionid=None,
            sysfrom=None,
            operator=None):
        api_request = APIRequest('RemoveRegisterBox', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Drsessionid": drsessionid,
            "Sysfrom": sysfrom,
            "Operator": operator}
        return self._handle_request(api_request).result

    def remove_ip_segment(
            self,
            clientappid=None,
            region_id=None,
            sysfrom=None,
            uuid=None,
            operator=None):
        api_request = APIRequest('RemoveIPSegment', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Sysfrom": sysfrom,
            "Uuid": uuid,
            "Operator": operator}
        return self._handle_request(api_request).result

    def remove_box_code(
            self,
            clientappid=None,
            code=None,
            region_id=None,
            sysfrom=None,
            operator=None):
        api_request = APIRequest('RemoveBoxCode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "Code": code,
            "RegionId": region_id,
            "Sysfrom": sysfrom,
            "Operator": operator}
        return self._handle_request(api_request).result

    def get_welcome_page_uri(self, clientappid=None, region_id=None, sysfrom=None, operator=None):
        api_request = APIRequest('GetWelcomePageURI', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Sysfrom": sysfrom,
            "Operator": operator}
        return self._handle_request(api_request).result

    def get_register_history_list(
            self,
            clientappid=None,
            region_id=None,
            sysfrom=None,
            operator=None):
        api_request = APIRequest('GetRegisterHistoryList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Sysfrom": sysfrom,
            "Operator": operator}
        return self._handle_request(api_request).result

    def get_register_box_number(
            self,
            clientappid=None,
            region_id=None,
            sysfrom=None,
            operator=None):
        api_request = APIRequest('GetRegisterBoxNumber', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Sysfrom": sysfrom,
            "Operator": operator}
        return self._handle_request(api_request).result

    def get_register_box_list(self, clientappid=None, region_id=None, sysfrom=None, operator=None):
        api_request = APIRequest('GetRegisterBoxList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Sysfrom": sysfrom,
            "Operator": operator}
        return self._handle_request(api_request).result

    def get_ip_segments_list(self, clientappid=None, region_id=None, sysfrom=None, operator=None):
        api_request = APIRequest('GetIPSegmentsList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Sysfrom": sysfrom,
            "Operator": operator}
        return self._handle_request(api_request).result

    def get_enterprise_config(self, clientappid=None, region_id=None, sysfrom=None, operator=None):
        api_request = APIRequest('GetEnterpriseConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Sysfrom": sysfrom,
            "Operator": operator}
        return self._handle_request(api_request).result

    def get_box_code_list(self, clientappid=None, region_id=None, sysfrom=None, operator=None):
        api_request = APIRequest('GetBoxCodeList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Sysfrom": sysfrom,
            "Operator": operator}
        return self._handle_request(api_request).result

    def create_enterprise(
            self,
            clientappid=None,
            region_id=None,
            service_flag=None,
            sysfrom=None,
            box_number=None,
            operator=None):
        api_request = APIRequest('CreateEnterprise', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "ServiceFlag": service_flag,
            "Sysfrom": sysfrom,
            "BoxNumber": box_number,
            "Operator": operator}
        return self._handle_request(api_request).result

    def create_box_code(self, clientappid=None, region_id=None, sysfrom=None, operator=None):
        api_request = APIRequest('CreateBoxCode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Sysfrom": sysfrom,
            "Operator": operator}
        return self._handle_request(api_request).result

    def add_ip_segment(
            self,
            clientappid=None,
            region_id=None,
            ipsegment=None,
            memo=None,
            sysfrom=None,
            operator=None):
        api_request = APIRequest('AddIPSegment', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Clientappid": clientappid,
            "RegionId": region_id,
            "Ipsegment": ipsegment,
            "Memo": memo,
            "Sysfrom": sysfrom,
            "Operator": operator}
        return self._handle_request(api_request).result
