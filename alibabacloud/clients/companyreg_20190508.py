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


class CompanyregClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'companyreg'
        self.api_version = '2019-05-08'
        self.location_service_code = 'companyreg'
        self.location_endpoint_type = 'openAPI'

    def submit_communication_note(
            self,
            note=None,
            biz_code=None,
            biz_id=None,
            type_=None,
            action_request_id=None,
            operator_type=None):
        api_request = APIRequest('SubmitCommunicationNote', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Note": note,
            "BizCode": biz_code,
            "BizId": biz_id,
            "Type": type_,
            "ActionRequestId": action_request_id,
            "OperatorType": operator_type}
        return self._handle_request(api_request).result

    def process_company_reg_order(
            self,
            action_type=None,
            biz_code=None,
            biz_id=None,
            action_request_id=None,
            operator_type=None,
            action_info=None):
        api_request = APIRequest('ProcessCompanyRegOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ActionType": action_type,
            "BizCode": biz_code,
            "BizId": biz_id,
            "ActionRequestId": action_request_id,
            "OperatorType": operator_type,
            "ActionInfo": action_info}
        return self._handle_request(api_request).result

    def send_vcode(self, biz_code=None, mobile=None):
        api_request = APIRequest('SendVcode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BizCode": biz_code, "Mobile": mobile}
        return self._handle_request(api_request).result

    def submit_consultation(self, data=None, biz_code=None, consult_request_id=None, vcode=None):
        api_request = APIRequest('SubmitConsultation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Data": data,
            "BizCode": biz_code,
            "ConsultRequestId": consult_request_id,
            "Vcode": vcode}
        return self._handle_request(api_request).result

    def list_company_reg_orders(
            self,
            biz_code=None,
            biz_status=None,
            company_name=None,
            page_size=None,
            aliyun_order_id=None,
            page_num=None):
        api_request = APIRequest('ListCompanyRegOrders', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BizCode": biz_code,
            "BizStatus": biz_status,
            "CompanyName": company_name,
            "PageSize": page_size,
            "AliyunOrderId": aliyun_order_id,
            "PageNum": page_num}
        return self._handle_request(api_request).result

    def get_company_reg_order(
            self,
            action_types=None,
            biz_code=None,
            biz_id=None,
            max_operation_size=None):
        api_request = APIRequest('GetCompanyRegOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ActionTypes": action_types,
            "BizCode": biz_code,
            "BizId": biz_id,
            "MaxOperationSize": max_operation_size}
        return self._handle_request(api_request).result

    def list_company_reg_consultations(
            self,
            end_gmt_create=None,
            biz_code=None,
            city=None,
            page_size=None,
            biz_id=None,
            start_gmt_create=None,
            page_num=None):
        api_request = APIRequest('ListCompanyRegConsultations', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndGmtCreate": end_gmt_create,
            "BizCode": biz_code,
            "City": city,
            "PageSize": page_size,
            "BizId": biz_id,
            "StartGmtCreate": start_gmt_create,
            "PageNum": page_num}
        return self._handle_request(api_request).result
