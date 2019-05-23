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


class CSBClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None):
        AlibabaCloudClient.__init__(self, client_config, credentials_provider)
        self.product_code = 'CSB'
        self.product_version = '2017-11-18'
        self.location_service_code = 'csb'
        self.location_endpoint_type = 'openAPI'

    def find_service_statistical_data(
        self,
        csb_id=None,
        end_time=None,
        service_name=None,
        start_time=None,
    ):
        api_request = APIRequest(
            'FindServiceStatisticalData',
            'GET',
            'https',
            'RPC',
            'query')
        api_request._params = {
            "CsbId": csb_id,
            "EndTime": end_time,
            "ServiceName": service_name,
            "StartTime": start_time,
        }
        return self._handle_request(api_request).result

    def get_instance(self, csb_id=None,):
        api_request = APIRequest('GetInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CsbId": csb_id, }
        return self._handle_request(api_request).result

    def delete_cas_service(
        self,
        leaf_only=None,
        cas_csb_name=None,
        src_user_id=None,
        cas_service_id=None,
    ):
        api_request = APIRequest(
            'DeleteCasService',
            'POST',
            'https',
            'RPC',
            'query')
        api_request._params = {
            "LeafOnly": leaf_only,
            "CasCsbName": cas_csb_name,
            "SrcUserId": src_user_id,
            "CasServiceId": cas_service_id,
        }
        return self._handle_request(api_request).result

    def find_instance_list(
        self,
        search_txt=None,
        csb_id=None,
        page_num=None,
        status=None,
    ):
        api_request = APIRequest(
            'FindInstanceList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SearchTxt": search_txt,
            "CsbId": csb_id,
            "PageNum": page_num,
            "Status": status,
        }
        return self._handle_request(api_request).result

    def publish_cas_service(self, cas_csb_name=None, data=None,):
        api_request = APIRequest(
            'PublishCasService',
            'POST',
            'https',
            'RPC',
            'query')
        api_request._params = {"CasCsbName": cas_csb_name, "Data": data, }
        return self._handle_request(api_request).result

    def commit_successed_services(self, csb_name=None, services=None,):
        api_request = APIRequest(
            'CommitSuccessedServices',
            'POST',
            'https',
            'RPC',
            'query')
        api_request._params = {"CsbName": csb_name, "Services": services, }
        return self._handle_request(api_request).result

    def delete_union_cas_service(
        self,
        leaf_only=None,
        cas_csb_name=None,
        src_user_id=None,
        cas_service_id=None,
    ):
        api_request = APIRequest(
            'DeleteUnionCasService',
            'POST',
            'https',
            'RPC',
            'query')
        api_request._params = {
            "LeafOnly": leaf_only,
            "CasCsbName": cas_csb_name,
            "SrcUserId": src_user_id,
            "CasServiceId": cas_service_id,
        }
        return self._handle_request(api_request).result

    def publish_union_cas_service(self, cas_csb_name=None, data=None,):
        api_request = APIRequest(
            'PublishUnionCasService',
            'POST',
            'https',
            'RPC',
            'query')
        api_request._params = {"CasCsbName": cas_csb_name, "Data": data, }
        return self._handle_request(api_request).result

    def update_service_qps(self, qps=None, service_id=None,):
        api_request = APIRequest(
            'UpdateServiceQPS',
            'POST',
            'https',
            'RPC',
            'query')
        api_request._params = {"Qps": qps, "ServiceId": service_id, }
        return self._handle_request(api_request).result

    def delete_service_list(self, data=None, csb_id=None,):
        api_request = APIRequest(
            'DeleteServiceList',
            'POST',
            'https',
            'RPC',
            'body')
        api_request._params = {"Data": data, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def update_order_list(self, data=None,):
        api_request = APIRequest(
            'UpdateOrderList',
            'POST',
            'https',
            'RPC',
            'body')
        api_request._params = {"Data": data, }
        return self._handle_request(api_request).result

    def update_service_list_status(self, data=None, csb_id=None,):
        api_request = APIRequest(
            'UpdateServiceListStatus',
            'POST',
            'https',
            'RPC',
            'body')
        api_request._params = {"Data": data, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def update_project_list_status(self, data=None, csb_id=None,):
        api_request = APIRequest(
            'UpdateProjectListStatus',
            'POST',
            'https',
            'RPC',
            'body')
        api_request._params = {"Data": data, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def approve_order_list(self, data=None,):
        api_request = APIRequest(
            'ApproveOrderList',
            'POST',
            'https',
            'RPC',
            'body')
        api_request._params = {"Data": data, }
        return self._handle_request(api_request).result

    def delete_project(self, csb_id=None, project_id=None,):
        api_request = APIRequest(
            'DeleteProject', 'POST', 'https', 'RPC', 'query')
        api_request._params = {"CsbId": csb_id, "ProjectId": project_id, }
        return self._handle_request(api_request).result

    def delete_service(self, service_name=None, service_id=None,):
        api_request = APIRequest(
            'DeleteService', 'POST', 'https', 'RPC', 'query')
        api_request._params = {
            "ServiceName": service_name,
            "ServiceId": service_id,
        }
        return self._handle_request(api_request).result

    def delete_order_list(self, data=None,):
        api_request = APIRequest(
            'DeleteOrderList',
            'POST',
            'https',
            'RPC',
            'body')
        api_request._params = {"Data": data, }
        return self._handle_request(api_request).result

    def delete_project_list(self, data=None, csb_id=None,):
        api_request = APIRequest(
            'DeleteProjectList',
            'POST',
            'https',
            'RPC',
            'body')
        api_request._params = {"Data": data, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def create_credentials(self, data=None, csb_id=None,):
        api_request = APIRequest(
            'CreateCredentials',
            'POST',
            'https',
            'RPC',
            'body')
        api_request._params = {"Data": data, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def create_service(self, data=None, csb_id=None,):
        api_request = APIRequest(
            'CreateService', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"Data": data, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def update_service(self, data=None, csb_id=None,):
        api_request = APIRequest(
            'UpdateService', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"Data": data, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def update_order(self, data=None, csb_id=None,):
        api_request = APIRequest('UpdateOrder', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"Data": data, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def create_order(self, data=None, csb_id=None,):
        api_request = APIRequest('CreateOrder', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"Data": data, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def update_project(self, data=None, csb_id=None,):
        api_request = APIRequest(
            'UpdateProject', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"Data": data, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def create_project(self, data=None, csb_id=None,):
        api_request = APIRequest(
            'CreateProject', 'POST', 'https', 'RPC', 'body')
        api_request._params = {"Data": data, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def delete_credentials_list(
        self,
        data=None,
        ignore_dauth=None,
        force=None,
    ):
        api_request = APIRequest(
            'DeleteCredentialsList',
            'POST',
            'https',
            'RPC',
            'body')
        api_request._params = {
            "Data": data,
            "IgnoreDauth": ignore_dauth,
            "Force": force,
        }
        return self._handle_request(api_request).result

    def find_projects_name_list(self, operation_flag=None, csb_id=None,):
        api_request = APIRequest(
            'FindProjectsNameList',
            'GET',
            'https',
            'RPC',
            'query')
        api_request._params = {
            "OperationFlag": operation_flag, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def get_project(self, project_name=None, csb_id=None,):
        api_request = APIRequest('GetProject', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"ProjectName": project_name, "CsbId": csb_id, }
        return self._handle_request(api_request).result

    def get_service(self, csb_id=None, service_id=None,):
        api_request = APIRequest('GetService', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"CsbId": csb_id, "ServiceId": service_id, }
        return self._handle_request(api_request).result

    def check_service_exist(self, csb_id=None, service_name=None,):
        api_request = APIRequest(
            'CheckServiceExist',
            'POST',
            'https',
            'RPC',
            'query')
        api_request._params = {"CsbId": csb_id, "ServiceName": service_name, }
        return self._handle_request(api_request).result

    def get_order(self, order_id=None, service_name=None,):
        api_request = APIRequest('GetOrder', 'GET', 'https', 'RPC', 'query')
        api_request._params = {
            "OrderId": order_id,
            "ServiceName": service_name,
        }
        return self._handle_request(api_request).result

    def find_project_list(
        self,
        project_name=None,
        csb_id=None,
        page_num=None,
    ):
        api_request = APIRequest(
            'FindProjectList',
            'GET',
            'https',
            'RPC',
            'query')
        api_request._params = {
            "ProjectName": project_name,
            "CsbId": csb_id,
            "PageNum": page_num,
        }
        return self._handle_request(api_request).result

    def find_approval_order_list(
        self,
        project_name=None,
        csb_id=None,
        alias=None,
        service_name=None,
        service_id=None,
        page_num=None,
        only_pending=None,
    ):
        api_request = APIRequest(
            'FindApprovalOrderList',
            'GET',
            'https',
            'RPC',
            'query')
        api_request._params = {
            "ProjectName": project_name,
            "CsbId": csb_id,
            "Alias": alias,
            "ServiceName": service_name,
            "ServiceId": service_id,
            "PageNum": page_num,
            "OnlyPending": only_pending,
        }
        return self._handle_request(api_request).result

    def find_approve_service_list(
        self,
        project_name=None,
        approve_level=None,
        show_del_service=None,
        csb_id=None,
        alias=None,
        service_name=None,
    ):
        api_request = APIRequest(
            'FindApproveServiceList',
            'GET',
            'https',
            'RPC',
            'query')
        api_request._params = {
            "ProjectName": project_name,
            "ApproveLevel": approve_level,
            "ShowDelService": show_del_service,
            "CsbId": csb_id,
            "Alias": alias,
            "ServiceName": service_name,
        }
        return self._handle_request(api_request).result

    def find_credentials_list(
        self,
        csb_id=None,
        page_num=None,
        group_name=None,
    ):
        api_request = APIRequest(
            'FindCredentialsList',
            'GET',
            'https',
            'RPC',
            'query')
        api_request._params = {
            "CsbId": csb_id,
            "PageNum": page_num,
            "GroupName": group_name,
        }
        return self._handle_request(api_request).result

    def renew_credentials(self, credential_id=None,):
        api_request = APIRequest(
            'RenewCredentials',
            'POST',
            'https',
            'RPC',
            'query')
        api_request._params = {"CredentialId": credential_id, }
        return self._handle_request(api_request).result

    def replace_credential(self, credential_id=None,):
        api_request = APIRequest(
            'ReplaceCredential',
            'POST',
            'https',
            'RPC',
            'query')
        api_request._params = {"CredentialId": credential_id, }
        return self._handle_request(api_request).result

    def find_orderable_list(
        self,
        project_name=None,
        csb_id=None,
        alias=None,
        service_name=None,
        page_num=None,
    ):
        api_request = APIRequest(
            'FindOrderableList',
            'GET',
            'https',
            'RPC',
            'query')
        api_request._params = {
            "ProjectName": project_name,
            "CsbId": csb_id,
            "Alias": alias,
            "ServiceName": service_name,
            "PageNum": page_num,
        }
        return self._handle_request(api_request).result

    def find_ordered_list(
        self,
        project_name=None,
        show_del_order=None,
        csb_id=None,
        alias=None,
        service_name=None,
        page_num=None,
        service_id=None,
        status=None,
    ):
        api_request = APIRequest(
            'FindOrderedList',
            'GET',
            'https',
            'RPC',
            'query')
        api_request._params = {
            "ProjectName": project_name,
            "ShowDelOrder": show_del_order,
            "CsbId": csb_id,
            "Alias": alias,
            "ServiceName": service_name,
            "PageNum": page_num,
            "ServiceId": service_id,
            "Status": status,
        }
        return self._handle_request(api_request).result

    def find_service_list(
        self,
        project_name=None,
        show_del_service=None,
        cas_show_type=None,
        csb_id=None,
        alias=None,
        service_name=None,
        page_num=None,
    ):
        api_request = APIRequest(
            'FindServiceList',
            'GET',
            'https',
            'RPC',
            'query')
        api_request._params = {
            "ProjectName": project_name,
            "ShowDelService": show_del_service,
            "CasShowType": cas_show_type,
            "CsbId": csb_id,
            "Alias": alias,
            "ServiceName": service_name,
            "PageNum": page_num,
        }
        return self._handle_request(api_request).result
