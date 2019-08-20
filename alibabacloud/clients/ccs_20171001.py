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


class CcsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Ccs'
        self.api_version = '2017-10-01'
        self.location_service_code = 'ccs'
        self.location_endpoint_type = 'openAPI'

    def query_ticket(
            self,
            stage=None,
            page_size=None,
            creator_id=None,
            end_time=None,
            start_time=None,
            page_num=None,
            type_=None,
            ccs_instance_id=None):
        api_request = APIRequest('QueryTicket', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Stage": stage,
            "PageSize": page_size,
            "CreatorId": creator_id,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNum": page_num,
            "Type": type_,
            "CcsInstanceId": ccs_instance_id}
        return self._handle_request(api_request).result

    def proceed_ticket(
            self,
            memo=None,
            id_=None,
            ccs_instance_id=None,
            operation=None,
            operator_id=None):
        api_request = APIRequest('ProceedTicket', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Memo": memo,
            "Id": id_,
            "CcsInstanceId": ccs_instance_id,
            "Operation": operation,
            "OperatorId": operator_id}
        return self._handle_request(api_request).result

    def create_ticket(
            self,
            creator_id=None,
            description=None,
            type_=None,
            ccs_instance_id=None,
            custom_fields=None):
        api_request = APIRequest('CreateTicket', 'POST', 'http', 'RPC', 'query')
        api_request._params = {
            "CreatorId": creator_id,
            "Description": description,
            "Type": type_,
            "CcsInstanceId": ccs_instance_id,
            "CustomFields": custom_fields}
        return self._handle_request(api_request).result

    def query_hotline_record(
            self,
            agent_id=None,
            max_talk_duration=None,
            group_id=None,
            end_time=None,
            start_time=None,
            page_num=None,
            satisfaction=None,
            min_talk_duratoin=None,
            category_ids=None,
            visitor_province=None,
            page_size=None,
            call_type=None,
            ccs_instance_id=None,
            visitor_phone=None,
            visitor_id=None,
            status=None):
        api_request = APIRequest('QueryHotlineRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AgentId": agent_id,
            "MaxTalkDuration": max_talk_duration,
            "GroupId": group_id,
            "EndTime": end_time,
            "StartTime": start_time,
            "PageNum": page_num,
            "Satisfaction": satisfaction,
            "MinTalkDuratoin": min_talk_duratoin,
            "CategoryIds": category_ids,
            "VisitorProvince": visitor_province,
            "PageSize": page_size,
            "CallType": call_type,
            "CcsInstanceId": ccs_instance_id,
            "VisitorPhone": visitor_phone,
            "VisitorId": visitor_id,
            "Status": status}
        return self._handle_request(api_request).result

    def get_hotline_record(self, id_=None, ccs_instance_id=None):
        api_request = APIRequest('GetHotlineRecord', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "CcsInstanceId": ccs_instance_id}
        return self._handle_request(api_request).result
