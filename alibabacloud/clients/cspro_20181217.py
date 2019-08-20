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


class CsproClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'cspro'
        self.api_version = '2018-12-17'
        self.location_service_code = 'cspro'
        self.location_endpoint_type = 'openAPI'

    def auth_sec_check_sample_pic_upload(self,):
        api_request = APIRequest('AuthSecCheckSamplePicUpload', 'POST', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def add_sec_check_sample(self, lib_id=None, list_of_contents=None, type_=None):
        api_request = APIRequest('AddSecCheckSample', 'POST', 'http', 'RPC', 'body')
        api_request._params = {"LibId": lib_id, "Contents": list_of_contents, "Type": type_}
        repeat_info = {"Contents": ('Contents', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def add_omni_sec_check_config(
            self,
            list_of_check_detail_dto_list=None,
            name=None,
            extras=None,
            check_target=None,
            conf_type=None):
        api_request = APIRequest('AddOmniSecCheckConfig', 'POST', 'http', 'RPC', 'body')
        api_request._params = {
            "CheckDetailDTOList": list_of_check_detail_dto_list,
            "Name": name,
            "Extras": extras,
            "CheckTarget": check_target,
            "ConfType": conf_type}
        repeat_info = {"CheckDetailDTOList": ('CheckDetailDTOList',
                                              'list',
                                              'dict',
                                              [('CheckType',
                                                'str',
                                                None,
                                                None),
                                               ('CheckIntervalUnit',
                                                'str',
                                                None,
                                                None),
                                                  ('CheckExtras',
                                                   'str',
                                                   None,
                                                   None),
                                                  ('CheckIntervalVal',
                                                   'str',
                                                   None,
                                                   None),
                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def update_omni_sec_check_config(
            self,
            conf_id=None,
            valid=None,
            list_of_check_detail_dto_list=None,
            name=None,
            extras=None):
        api_request = APIRequest('UpdateOmniSecCheckConfig', 'POST', 'http', 'RPC', 'body')
        api_request._params = {
            "ConfId": conf_id,
            "Valid": valid,
            "CheckDetailDTOList": list_of_check_detail_dto_list,
            "Name": name,
            "Extras": extras}
        repeat_info = {"CheckDetailDTOList": ('CheckDetailDTOList',
                                              'list',
                                              'dict',
                                              [('CheckIntervalUnit',
                                                'str',
                                                None,
                                                None),
                                               ('CheckExtras',
                                                'str',
                                                None,
                                                None),
                                                  ('CheckIntervalVal',
                                                   'str',
                                                   None,
                                                   None),
                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def del_omni_sec_check_config(self, conf_id=None):
        api_request = APIRequest('DelOmniSecCheckConfig', 'POST', 'http', 'RPC', 'body')
        api_request._params = {"ConfId": conf_id}
        return self._handle_request(api_request).result

    def query_sec_check_latest_summary(
            self,
            check_type=None,
            page_size=None,
            current_page=None,
            conf_type=None):
        api_request = APIRequest('QuerySecCheckLatestSummary', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "CheckType": check_type,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "ConfType": conf_type}
        return self._handle_request(api_request).result

    def query_sec_check_result(
            self,
            check_type=None,
            end_date=None,
            page_size=None,
            current_page=None,
            start_date=None,
            check_target=None,
            conf_type=None):
        api_request = APIRequest('QuerySecCheckResult', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "CheckType": check_type,
            "EndDate": end_date,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "StartDate": start_date,
            "CheckTarget": check_target,
            "ConfType": conf_type}
        return self._handle_request(api_request).result

    def get_sec_check_result_detail(self, risk_type=None, risk_source=None, result_id=None):
        api_request = APIRequest('GetSecCheckResultDetail', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "RiskType": risk_type,
            "RiskSource": risk_source,
            "ResultId": result_id}
        return self._handle_request(api_request).result

    def get_snapshot_info(self, snapshot_info=None):
        api_request = APIRequest('GetSnapshotInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SnapshotInfo": snapshot_info}
        return self._handle_request(api_request).result

    def add_sec_check_sample_lib(self, name=None, type_=None, result_type=None, scene=None):
        api_request = APIRequest('AddSecCheckSampleLib', 'POST', 'http', 'RPC', 'body')
        api_request._params = {
            "Name": name,
            "Type": type_,
            "ResultType": result_type,
            "Scene": scene}
        return self._handle_request(api_request).result

    def del_sec_check_sample_lib(self, lib_id=None, type_=None):
        api_request = APIRequest('DelSecCheckSampleLib', 'POST', 'http', 'RPC', 'body')
        api_request._params = {"LibId": lib_id, "Type": type_}
        return self._handle_request(api_request).result

    def query_sec_check_samples(self, lib_id=None, type_=None):
        api_request = APIRequest('QuerySecCheckSamples', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"LibId": lib_id, "Type": type_}
        return self._handle_request(api_request).result

    def del_sec_check_sample(self, lib_id=None, list_of_sample_ids=None, type_=None):
        api_request = APIRequest('DelSecCheckSample', 'POST', 'http', 'RPC', 'body')
        api_request._params = {"LibId": lib_id, "SampleIds": list_of_sample_ids, "Type": type_}
        repeat_info = {"SampleIds": ('SampleIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result
