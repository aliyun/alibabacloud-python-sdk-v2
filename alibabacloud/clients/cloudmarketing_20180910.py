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


class CloudmarketingClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'cloudmarketing'
        self.api_version = '2018-09-10'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def fetch_crowd_define(self, crowd_id=None):
        api_request = APIRequest('FetchCrowdDefine', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CrowdId": crowd_id}
        return self._handle_request(api_request).result

    def delete_crowd(self, crowd_id=None):
        api_request = APIRequest('DeleteCrowd', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CrowdId": crowd_id}
        return self._handle_request(api_request).result

    def delete_file(self, file_id=None):
        api_request = APIRequest('DeleteFile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"FileId": file_id}
        return self._handle_request(api_request).result

    def process_after_upload_file(self, src_file_name=None, oss_path=None):
        api_request = APIRequest('ProcessAfterUploadFile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SrcFileName": src_file_name, "OssPath": oss_path}
        return self._handle_request(api_request).result

    def auth2_brand(self, account_id=None, brand_id=None, list_of_channel_brand_reqs=None):
        api_request = APIRequest('Auth2Brand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccountId": account_id,
            "BrandId": brand_id,
            "ChannelBrandReqs": list_of_channel_brand_reqs}
        repeat_info = {
            "ChannelBrandReqs": (
                'ChannelBrandReqs', 'list', 'dict', [
                    ('ChannelType', 'str', None, None), ('OuterBrandId', 'list', 'str', None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_auth_brand(self, list_of_account_ids=None):
        api_request = APIRequest('DescribeAuthBrand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AccountIds": list_of_account_ids}
        repeat_info = {"AccountIds": ('AccountIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def update_crowd(self, request_json_data=None):
        api_request = APIRequest('UpdateCrowd', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"RequestJsonData": request_json_data}
        return self._handle_request(api_request).result

    def fetch_tag(self, tag_id=None):
        api_request = APIRequest('FetchTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TagId": tag_id}
        return self._handle_request(api_request).result

    def request_upload_file(self,):
        api_request = APIRequest('RequestUploadFile', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def define_tag(
            self,
            option_type=None,
            tag_name=None,
            column_index=None,
            tag_desc=None,
            valid_time=None,
            list_of_option_defines=None,
            category_id=None,
            file_id=None):
        api_request = APIRequest('DefineTag', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "OptionType": option_type,
            "TagName": tag_name,
            "ColumnIndex": column_index,
            "TagDesc": tag_desc,
            "ValidTime": valid_time,
            "OptionDefines": list_of_option_defines,
            "CategoryId": category_id,
            "FileId": file_id}
        repeat_info = {"OptionDefines": ('OptionDefines', 'list', 'dict', [('Name', 'str', None, None),
                                                                           ('Define', 'str', None, None),
                                                                           ('Value', 'str', None, None),
                                                                           ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def redefine_tag(
            self,
            option_type=None,
            tag_name=None,
            column_index=None,
            tag_id=None,
            tag_desc=None,
            valid_time=None,
            list_of_option_defines=None,
            category_id=None,
            file_id=None):
        api_request = APIRequest('RedefineTag', 'GET', 'http', 'RPC', 'body')
        api_request._params = {
            "OptionType": option_type,
            "TagName": tag_name,
            "ColumnIndex": column_index,
            "TagId": tag_id,
            "TagDesc": tag_desc,
            "ValidTime": valid_time,
            "OptionDefines": list_of_option_defines,
            "CategoryId": category_id,
            "FileId": file_id}
        repeat_info = {"OptionDefines": ('OptionDefines', 'list', 'dict', [('Name', 'str', None, None),
                                                                           ('Define', 'str', None, None),
                                                                           ('Value', 'str', None, None),
                                                                           ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_brand(self, name=None, desc=None):
        api_request = APIRequest('CreateBrand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name, "Desc": desc}
        return self._handle_request(api_request).result

    def update_brand(self, name=None, id_=None, desc=None):
        api_request = APIRequest('UpdateBrand', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"Name": name, "Id": id_, "Desc": desc}
        return self._handle_request(api_request).result

    def describe_brand(self, page_no=None, name=None, page_size=None):
        api_request = APIRequest('DescribeBrand', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"PageNo": page_no, "Name": name, "PageSize": page_size}
        return self._handle_request(api_request).result

    def create_category(self, parent_category_id=None, name=None):
        api_request = APIRequest('CreateCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ParentCategoryId": parent_category_id, "Name": name}
        return self._handle_request(api_request).result

    def describe_category(self, category_id=None, recursive=None):
        api_request = APIRequest('DescribeCategory', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CategoryId": category_id, "Recursive": recursive}
        return self._handle_request(api_request).result

    def describe_channel_brand(self,):
        api_request = APIRequest('DescribeChannelBrand', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def define_crowd(self, request_json_data=None):
        api_request = APIRequest('DefineCrowd', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"RequestJsonData": request_json_data}
        return self._handle_request(api_request).result

    def describe_auth_channel_brand(self,):
        api_request = APIRequest('DescribeAuthChannelBrand', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def fetch_file_schema(self, file_id=None):
        api_request = APIRequest('FetchFileSchema', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"FileId": file_id}
        return self._handle_request(api_request).result

    def define_file_schema(self, list_of_file_columns=None, file_id=None):
        api_request = APIRequest('DefineFileSchema', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"FileColumns": list_of_file_columns, "FileId": file_id}
        repeat_info = {"FileColumns": ('FileColumns',
                                       'list',
                                       'dict',
                                       [('Head',
                                         'str',
                                         None,
                                         None),
                                        ('DataType',
                                         'str',
                                         None,
                                         None),
                                           ('Name',
                                            'str',
                                            None,
                                            None),
                                           ('Index',
                                            'str',
                                            None,
                                            None),
                                           ('ColumnType',
                                            'str',
                                            None,
                                            None),
                                        ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_file(
            self,
            file_name=None,
            list_of_data_schema_status_list=None,
            page_no=None,
            page_size=None,
            file_id=None):
        api_request = APIRequest('DescribeFile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FileName": file_name,
            "DataSchemaStatusList": list_of_data_schema_status_list,
            "PageNo": page_no,
            "PageSize": page_size,
            "FileId": file_id}
        repeat_info = {"DataSchemaStatusList": ('DataSchemaStatusList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def cal_crowd_scale(self, request_json_data=None):
        api_request = APIRequest('CalCrowdScale', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"RequestJsonData": request_json_data}
        return self._handle_request(api_request).result

    def describe_crowd(
            self,
            sync_status=None,
            page_no=None,
            cal_status=None,
            page_size=None,
            keyword=None):
        api_request = APIRequest('DescribeCrowd', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SyncStatus": sync_status,
            "PageNo": page_no,
            "CalStatus": cal_status,
            "PageSize": page_size,
            "Keyword": keyword}
        return self._handle_request(api_request).result

    def fetch_crowd(self, crowd_id=None):
        api_request = APIRequest('FetchCrowd', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CrowdId": crowd_id}
        return self._handle_request(api_request).result

    def analysis_crowd(self, list_of_tag_ids=None, crowd_id=None):
        api_request = APIRequest('AnalysisCrowd', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TagIds": list_of_tag_ids, "CrowdId": crowd_id}
        repeat_info = {"TagIds": ('TagIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_tag(
            self,
            list_of_status_list=None,
            page_no=None,
            page_size=None,
            include_child=None,
            only_favorite=None,
            keyword=None,
            category_id=None):
        api_request = APIRequest('DescribeTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StatusList": list_of_status_list,
            "PageNo": page_no,
            "PageSize": page_size,
            "IncludeChild": include_child,
            "OnlyFavorite": only_favorite,
            "Keyword": keyword,
            "CategoryId": category_id}
        repeat_info = {"StatusList": ('StatusList', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def favorite_tag(self, tag_id=None, list_of_tag_ids=None, favorite=None):
        api_request = APIRequest('FavoriteTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TagId": tag_id, "TagIds": list_of_tag_ids, "Favorite": favorite}
        repeat_info = {"TagIds": ('TagIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def update_category(self, request_json_data=None):
        api_request = APIRequest('UpdateCategory', 'GET', 'http', 'RPC', 'body')
        api_request._params = {"RequestJsonData": request_json_data}
        return self._handle_request(api_request).result

    def fetch_file_schema_data(self, file_id=None):
        api_request = APIRequest('FetchFileSchemaData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"FileId": file_id}
        return self._handle_request(api_request).result

    def download_ud_report(self, crowd_id=None):
        api_request = APIRequest('DownloadUDReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CrowdId": crowd_id}
        return self._handle_request(api_request).result

    def download_crowd(self, crowd_id=None):
        api_request = APIRequest('DownloadCrowd', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"CrowdId": crowd_id}
        return self._handle_request(api_request).result

    def sync_crowd(
            self,
            outer_account_no=None,
            list_of_channel_brands=None,
            channel_type=None,
            crowd_id=None):
        api_request = APIRequest('SyncCrowd', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OuterAccountNo": outer_account_no,
            "ChannelBrands": list_of_channel_brands,
            "ChannelType": channel_type,
            "CrowdId": crowd_id}
        repeat_info = {
            "ChannelBrands": (
                'ChannelBrands', 'list', 'dict', [
                    ('OuterBrandId', 'str', None, None), ('OuterBrandName', 'str', None, None), ]), }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result
