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


class Cusanalytic_sc_onlineClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'cusanalytic_sc_online'
        self.api_version = '2019-05-24'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def get_image_url(self, object_keys=None, origin_urls=None, store_id=None):
        api_request = APIRequest('GetImageUrl', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "ObjectKeys": object_keys,
            "OriginUrls": origin_urls,
            "StoreId": store_id}
        return self._handle_request(api_request).result

    def get_action_cursor(self, store_id=None):
        api_request = APIRequest('GetActionCursor', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"StoreId": store_id}
        return self._handle_request(api_request).result

    def describe_action_data(
            self,
            ts_end=None,
            page_no=None,
            ts_start=None,
            store_id=None,
            page_limit=None):
        api_request = APIRequest('DescribeActionData', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "TsEnd": ts_end,
            "PageNo": page_no,
            "TsStart": ts_start,
            "StoreId": store_id,
            "PageLimit": page_limit}
        return self._handle_request(api_request).result

    def describe_locations(self, store_id=None):
        api_request = APIRequest('DescribeLocations', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"StoreId": store_id}
        return self._handle_request(api_request).result

    def search_person_by_img(self, img_url=None, store_id=None):
        api_request = APIRequest('SearchPersonByImg', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"ImgUrl": img_url, "StoreId": store_id}
        return self._handle_request(api_request).result

    def get_locations(self, store_id=None):
        api_request = APIRequest('GetLocations', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"StoreId": store_id}
        return self._handle_request(api_request).result

    def list_visitors(
            self,
            pk_id=None,
            gender=None,
            uk_id=None,
            page_size=None,
            location_ids=None,
            end_time=None,
            enter_count=None,
            page_index=None,
            start_time=None,
            age_start=None,
            age_end=None,
            store_ids=None):
        api_request = APIRequest('ListVisitors', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "PkId": pk_id,
            "Gender": gender,
            "UkId": uk_id,
            "PageSize": page_size,
            "LocationIds": location_ids,
            "EndTime": end_time,
            "EnterCount": enter_count,
            "PageIndex": page_index,
            "StartTime": start_time,
            "AgeStart": age_start,
            "AgeEnd": age_end,
            "StoreIds": store_ids}
        return self._handle_request(api_request).result

    def get_analyze_commodity_data(
            self,
            start_user_count=None,
            end_date=None,
            end_user_count=None,
            page_size=None,
            min_support_count=None,
            page_index=None,
            store_id=None,
            start_date=None,
            stay_period=None):
        api_request = APIRequest('GetAnalyzeCommodityData', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "StartUserCount": start_user_count,
            "EndDate": end_date,
            "EndUserCount": end_user_count,
            "PageSize": page_size,
            "MinSupportCount": min_support_count,
            "PageIndex": page_index,
            "StoreId": store_id,
            "StartDate": start_date,
            "StayPeriod": stay_period}
        return self._handle_request(api_request).result

    def get_heat_map_data(self, emap_name=None, store_id=None):
        api_request = APIRequest('GetHeatMapData', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"EMapName": emap_name, "StoreId": store_id}
        return self._handle_request(api_request).result

    def get_emap(self, location_id=None, store_id=None):
        api_request = APIRequest('GetEMap', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"LocationId": location_id, "StoreId": store_id}
        return self._handle_request(api_request).result

    def get_analyze_place_data(
            self,
            end_uv_count=None,
            parent_amount=None,
            end_date=None,
            location_id=None,
            parent_location_ids=None,
            start_date=None,
            start_uv_count=None,
            store_id=None):
        api_request = APIRequest('GetAnalyzePlaceData', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "EndUVCount": end_uv_count,
            "ParentAmount": parent_amount,
            "EndDate": end_date,
            "LocationId": location_id,
            "ParentLocationIds": parent_location_ids,
            "StartDate": start_date,
            "StartUVCount": start_uv_count,
            "StoreId": store_id}
        return self._handle_request(api_request).result

    def get_portrayal(self, date=None, location_ids=None, store_ids=None):
        api_request = APIRequest('GetPortrayal', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"Date": date, "LocationIds": location_ids, "StoreIds": store_ids}
        return self._handle_request(api_request).result

    def get_overview_data(self, date=None, store_ids=None):
        api_request = APIRequest('GetOverviewData', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"Date": date, "StoreIds": store_ids}
        return self._handle_request(api_request).result

    def get_support_store(self,):
        api_request = APIRequest('GetSupportStore', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result
