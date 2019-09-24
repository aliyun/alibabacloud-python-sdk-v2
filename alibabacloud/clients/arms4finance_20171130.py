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


class ARMS4FINANCEClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'ARMS4FINANCE'
        self.api_version = '2017-11-30'
        self.location_service_code = 'arms4finance'
        self.location_endpoint_type = 'openAPI'

    def where_in_dim_query(
            self,
            where_in_key=None,
            list_of_measures=None,
            interval_in_sec=None,
            date_str=None,
            is_drill_down=None,
            min_time=None,
            dataset_id=None,
            list_of_where_in_values=None,
            max_time=None,
            list_of_dimensions=None):
        api_request = APIRequest('WhereInDimQuery', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WhereInKey": where_in_key,
            "Measures": list_of_measures,
            "IntervalInSec": interval_in_sec,
            "DateStr": date_str,
            "IsDrillDown": is_drill_down,
            "MinTime": min_time,
            "DatasetId": dataset_id,
            "WhereInValues": list_of_where_in_values,
            "MaxTime": max_time,
            "Dimensions": list_of_dimensions}
        repeat_info = {"Measures": ('Measures', 'list', 'str', None),
                       "WhereInValues": ('WhereInValues', 'list', 'str', None),
                       "Dimensions": ('Dimensions', 'list', 'dict', [('Value', 'str', None, None),
                                                                     ('Key', 'str', None, None),
                                                                     ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def arms_query_data_set(
            self,
            list_of_measures=None,
            interval_in_sec=None,
            date_str=None,
            is_drill_down=None,
            min_time=None,
            dataset_id=None,
            max_time=None,
            list_of_dimensions=None):
        api_request = APIRequest('ARMSQueryDataSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Measures": list_of_measures,
            "IntervalInSec": interval_in_sec,
            "DateStr": date_str,
            "IsDrillDown": is_drill_down,
            "MinTime": min_time,
            "DatasetId": dataset_id,
            "MaxTime": max_time,
            "Dimensions": list_of_dimensions}
        repeat_info = {"Measures": ('Measures', 'list', 'str', None),
                       "Dimensions": ('Dimensions', 'list', 'dict', [('Value', 'str', None, None),
                                                                     ('Key', 'str', None, None),
                                                                     ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result
