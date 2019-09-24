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

import json
import time

from alibabacloud.exceptions import ClientException
from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, _create_special_resource_collection
from alibabacloud.resources.collection import _create_default_resource_collection
from alibabacloud.resources.collection import _create_sub_resource_with_page_collection
from alibabacloud.resources.collection import _create_sub_resource_without_page_collection
from alibabacloud.utils.utils import _assert_is_not_none, _new_get_key_in_response, _transfer_params


class _CDNResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'cdn', _client=_client)
        self.fc_triggers = _create_special_resource_collection(
            _CDNFCTriggerResource, _client, _client.list_fc_trigger,
            'FCTriggers.FCTrigger', 'FCTriggerName',
        )

    def add_cdn_domain(self, **params):
        _params = _transfer_params(params)
        self._client.add_cdn_domain(**_params)
        cdn_domain_name = _params.get("cdn_domain_name")
        return _CDNCdnDomainResource(cdn_domain_name, _client=self._client)

    def add_fc_trigger(self, **params):
        _params = _transfer_params(params)
        self._client.add_fc_trigger(**_params)
        fc_trigger_name = _params.get("fc_trigger_name")
        return _CDNFCTriggerResource(fc_trigger_name, _client=self._client)

    def create_user_usage_data_export_task(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_user_usage_data_export_task(**_params)
        task_id = _new_get_key_in_response(response, 'TaskId')
        return _CDNUserUsageDataExportTaskResource(task_id, _client=self._client)


class _CDNCdnDomainResource(ServiceResource):

    def __init__(self, cdn_domain_name, _client=None):
        ServiceResource.__init__(self, "cdn.cdn_domain", _client=_client)
        self.cdn_domain_name = cdn_domain_name

    def batch_add(self, **params):
        _params = _transfer_params(params)
        self._client.batch_add_cdn_domain(cdn_domain_name=self.cdn_domain_name, **_params)

    def batch_delete_cdn_domain_config(self, **params):
        _params = _transfer_params(params)
        self._client.batch_delete_cdn_domain_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def batch_set_cdn_domain_config(self, **params):
        _params = _transfer_params(params)
        self._client.batch_set_cdn_domain_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def batch_set_cdn_domain_server_certificate(self, **params):
        _params = _transfer_params(params)
        self._client.batch_set_cdn_domain_server_certificate(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def batch_update(self, **params):
        _params = _transfer_params(params)
        self._client.batch_update_cdn_domain(cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_range_data_by_locate_and_isp_service(self, **params):
        _params = _transfer_params(params)
        self._client.describe_range_data_by_locate_and_isp_service(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_cdn_domain(cdn_domain_name=self.cdn_domain_name, **_params)

    def delete_specific_config(self, **params):
        _params = _transfer_params(params)
        self._client.delete_specific_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def delete_specific_staging_config(self, **params):
        _params = _transfer_params(params)
        self._client.delete_specific_staging_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_cdn_domain_configs(self, **params):
        _params = _transfer_params(params)
        self._client.describe_cdn_domain_configs(cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_cdn_domain_detail(self, **params):
        _params = _transfer_params(params)
        self._client.describe_cdn_domain_detail(cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_cdn_domain_logs(self, **params):
        _params = _transfer_params(params)
        self._client.describe_cdn_domain_logs(cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_bps_data_by_time_stamp(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_bps_data_by_time_stamp(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_certificate_info(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_certificate_info(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_cname(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_cname(cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_custom_log_config(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_custom_log_config(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_file_size_proportion_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_file_size_proportion_data(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_path_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_path_data(cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_pv_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_pv_data(cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_real_time_bps_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_real_time_bps_data(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_real_time_byte_hit_rate_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_real_time_byte_hit_rate_data(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_real_time_http_code_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_real_time_http_code_data(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_real_time_qps_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_real_time_qps_data(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_real_time_req_hit_rate_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_real_time_req_hit_rate_data(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_real_time_src_bps_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_real_time_src_bps_data(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_real_time_src_traffic_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_real_time_src_traffic_data(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_top_refer_visit(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_top_refer_visit(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_top_url_visit(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_top_url_visit(cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_domain_uv_data(self, **params):
        _params = _transfer_params(params)
        self._client.describe_domain_uv_data(cdn_domain_name=self.cdn_domain_name, **_params)

    def describe_l2_vips_by_domain(self, **params):
        _params = _transfer_params(params)
        self._client.describe_l2_vips_by_domain(cdn_domain_name=self.cdn_domain_name, **_params)

    def modify(self, **params):
        _params = _transfer_params(params)
        self._client.modify_cdn_domain(cdn_domain_name=self.cdn_domain_name, **_params)

    def modify_domain_custom_log_config(self, **params):
        _params = _transfer_params(params)
        self._client.modify_domain_custom_log_config(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def modify_file_cache_expired_config(self, **params):
        _params = _transfer_params(params)
        self._client.modify_file_cache_expired_config(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def modify_http_header_config(self, **params):
        _params = _transfer_params(params)
        self._client.modify_http_header_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def modify_schdm_by_property(self, **params):
        _params = _transfer_params(params)
        self._client.modify_cdn_domain_schdm_by_property(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def set_cc_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_cc_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_domain_green_manager_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_domain_green_manager_config(
            cdn_domain_name=self.cdn_domain_name, **_params)

    def set_domain_server_certificate(self, **params):
        _params = _transfer_params(params)
        self._client.set_domain_server_certificate(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_error_page_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_error_page_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_file_cache_expired_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_file_cache_expired_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_force_redirect_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_force_redirect_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_forward_scheme_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_forward_scheme_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_http_error_page_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_http_error_page_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_http_header_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_http_header_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_https_option_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_https_option_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_ignore_query_string_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_ignore_query_string_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_ip_allow_list_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_ip_allow_list_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_ip_black_list_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_ip_black_list_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_l2_oss_key_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_l2_oss_key_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_optimize_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_optimize_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_page_compress_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_page_compress_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_range_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_range_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_referer_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_referer_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_remove_query_string_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_remove_query_string_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_req_auth_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_req_auth_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_req_header_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_req_header_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_source_host_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_source_host_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_video_seek_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_video_seek_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_waf_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_waf_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def set_waiting_room_config(self, **params):
        _params = _transfer_params(params)
        self._client.set_waiting_room_config(cdn_domain_name=self.cdn_domain_name, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        self._client.start_cdn_domain(cdn_domain_name=self.cdn_domain_name, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        self._client.stop_cdn_domain(cdn_domain_name=self.cdn_domain_name, **_params)


class _CDNFCTriggerResource(ServiceResource):

    def __init__(self, fc_trigger_name, _client=None):
        ServiceResource.__init__(self, "cdn.fc_trigger", _client=_client)
        self.fc_trigger_name = fc_trigger_name

        self.event_meta_name = None
        self.event_meta_version = None
        self.notes = None
        self.role_arn = None
        self.source_arn = None
        self.trigger_arn = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_fc_trigger(fc_trigger_name=self.fc_trigger_name, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        self._client.describe_fc_trigger(fc_trigger_name=self.fc_trigger_name, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        self._client.update_fc_trigger(fc_trigger_name=self.fc_trigger_name, **_params)


class _CDNUserUsageDataExportTaskResource(ServiceResource):

    def __init__(self, task_id, _client=None):
        ServiceResource.__init__(self, "cdn.user_usage_data_export_task", _client=_client)
        self.task_id = task_id

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_user_usage_data_export_task(task_id=self.task_id, **_params)

    def delete_usage_detail_data_export_task(self, **params):
        _params = _transfer_params(params)
        self._client.delete_usage_detail_data_export_task(task_id=self.task_id, **_params)
