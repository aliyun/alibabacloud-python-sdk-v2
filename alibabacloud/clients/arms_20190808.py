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


class ARMSClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'ARMS'
        self.api_version = '2019-08-08'
        self.location_service_code = 'arms'
        self.location_endpoint_type = 'openAPI'

    def create_retcode_app(self, region_id=None, retcode_app_name=None, retcode_app_type=None):
        api_request = APIRequest('CreateRetcodeApp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "RetcodeAppName": retcode_app_name,
            "RetcodeAppType": retcode_app_type}
        return self._handle_request(api_request).result

    def delete_retcode_app(self, region_id=None, app_id=None):
        api_request = APIRequest('DeleteRetcodeApp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def query_dataset(
            self,
            date_str=None,
            min_time=None,
            reduce_tail=None,
            max_time=None,
            list_of_optional_dims=None,
            list_of_measures=None,
            interval_in_sec=None,
            is_drill_down=None,
            hungry_mode=None,
            order_by_key=None,
            limit=None,
            dataset_id=None,
            list_of_required_dims=None,
            list_of_dimensions=None):
        api_request = APIRequest('QueryDataset', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DateStr": date_str,
            "MinTime": min_time,
            "ReduceTail": reduce_tail,
            "MaxTime": max_time,
            "OptionalDims": list_of_optional_dims,
            "Measures": list_of_measures,
            "IntervalInSec": interval_in_sec,
            "IsDrillDown": is_drill_down,
            "HungryMode": hungry_mode,
            "OrderByKey": order_by_key,
            "Limit": limit,
            "DatasetId": dataset_id,
            "RequiredDims": list_of_required_dims,
            "Dimensions": list_of_dimensions}
        repeat_info = {"OptionalDims": ('OptionalDims', 'list', 'dict', [('Type', 'str', None, None),
                                                                         ('Value', 'str', None, None),
                                                                         ('Key', 'str', None, None),
                                                                         ]),
                       "Measures": ('Measures', 'list', 'str', None),
                       "RequiredDims": ('RequiredDims', 'list', 'dict', [('Type', 'str', None, None),
                                                                         ('Value', 'str', None, None),
                                                                         ('Key', 'str', None, None),
                                                                         ]),
                       "Dimensions": ('Dimensions', 'list', 'dict', [('Type', 'str', None, None),
                                                                     ('Value', 'str', None, None),
                                                                     ('Key', 'str', None, None),
                                                                     ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def query_metric(
            self,
            list_of_measures=None,
            interval_in_sec=None,
            metric=None,
            limit=None,
            end_time=None,
            order_by=None,
            start_time=None,
            list_of_filters=None,
            list_of_dimensions=None,
            order=None):
        api_request = APIRequest('QueryMetric', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Measures": list_of_measures,
            "IntervalInSec": interval_in_sec,
            "Metric": metric,
            "Limit": limit,
            "EndTime": end_time,
            "OrderBy": order_by,
            "StartTime": start_time,
            "Filters": list_of_filters,
            "Dimensions": list_of_dimensions,
            "Order": order}
        repeat_info = {"Measures": ('Measures', 'list', 'str', None),
                       "Filters": ('Filters', 'list', 'dict', [('Value', 'str', None, None),
                                                               ('Key', 'str', None, None),
                                                               ]),
                       "Dimensions": ('Dimensions', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_alert_contact(
            self,
            contact_name=None,
            region_id=None,
            phone_num=None,
            ding_robot_webhook_url=None,
            email=None,
            system_noc=None):
        api_request = APIRequest('CreateAlertContact', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContactName": contact_name,
            "RegionId": region_id,
            "PhoneNum": phone_num,
            "DingRobotWebhookUrl": ding_robot_webhook_url,
            "Email": email,
            "SystemNoc": system_noc}
        return self._handle_request(api_request).result

    def create_alert_contact_group(self, region_id=None, contact_group_name=None, contact_ids=None):
        api_request = APIRequest('CreateAlertContactGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "ContactGroupName": contact_group_name,
            "ContactIds": contact_ids}
        return self._handle_request(api_request).result

    def search_alert_contact(
            self,
            contact_name=None,
            phone=None,
            region_id=None,
            page_size=None,
            current_page=None,
            email=None):
        api_request = APIRequest('SearchAlertContact', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContactName": contact_name,
            "Phone": phone,
            "RegionId": region_id,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Email": email}
        return self._handle_request(api_request).result

    def search_alert_contact_group(self, region_id=None, contact_group_name=None):
        api_request = APIRequest('SearchAlertContactGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "ContactGroupName": contact_group_name}
        return self._handle_request(api_request).result

    def import_app_alert_rules(
            self,
            is_auto_start=None,
            region_id=None,
            contact_group_ids=None,
            pids=None,
            template_alert_id=None):
        api_request = APIRequest('ImportAppAlertRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IsAutoStart": is_auto_start,
            "RegionId": region_id,
            "ContactGroupIds": contact_group_ids,
            "Pids": pids,
            "TemplateAlertId": template_alert_id}
        return self._handle_request(api_request).result

    def search_retcode_app_by_page(
            self,
            region_id=None,
            retcode_app_name=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('SearchRetcodeAppByPage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "RetcodeAppName": retcode_app_name,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def search_trace_app_by_name(self, region_id=None, trace_app_name=None):
        api_request = APIRequest('SearchTraceAppByName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id, "TraceAppName": trace_app_name}
        return self._handle_request(api_request).result

    def search_trace_app_by_page(
            self,
            region_id=None,
            trace_app_name=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('SearchTraceAppByPage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "TraceAppName": trace_app_name,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_retcode_apps(self, security_token=None, region_id=None):
        api_request = APIRequest('ListRetcodeApps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SecurityToken": security_token, "RegionId": region_id}
        return self._handle_request(api_request).result

    def list_trace_apps(self, region_id=None):
        api_request = APIRequest('ListTraceApps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RegionId": region_id}
        return self._handle_request(api_request).result
