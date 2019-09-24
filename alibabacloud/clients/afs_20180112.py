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


class AfsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'afs'
        self.api_version = '2018-01-12'
        self.location_service_code = 'afs'
        self.location_endpoint_type = 'openAPI'

    def update_config_name(self, source_ip=None, config_name=None, ref_ext_id=None, lang=None):
        api_request = APIRequest('UpdateConfigName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ConfigName": config_name,
            "RefExtId": ref_ext_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_captcha_order(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeCaptchaOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_order_info(self, source_ip=None):
        api_request = APIRequest('DescribeOrderInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def set_early_warning(
            self,
            time_end=None,
            warn_open=None,
            source_ip=None,
            channel=None,
            title=None,
            time_open=None,
            time_begin=None,
            frequency=None):
        api_request = APIRequest('SetEarlyWarning', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TimeEnd": time_end,
            "WarnOpen": warn_open,
            "SourceIp": source_ip,
            "Channel": channel,
            "Title": title,
            "TimeOpen": time_open,
            "TimeBegin": time_begin,
            "Frequency": frequency}
        return self._handle_request(api_request).result

    def describe_person_machine_list(self, source_ip=None):
        api_request = APIRequest('DescribePersonMachineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_early_warning(self, source_ip=None):
        api_request = APIRequest('DescribeEarlyWarning', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_config_name(self, source_ip=None):
        api_request = APIRequest('DescribeConfigName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip}
        return self._handle_request(api_request).result

    def describe_captcha_risk(self, source_ip=None, config_name=None, ref_ext_id=None, time=None):
        api_request = APIRequest('DescribeCaptchaRisk', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ConfigName": config_name,
            "RefExtId": ref_ext_id,
            "Time": time}
        return self._handle_request(api_request).result

    def describe_captcha_min(
            self,
            source_ip=None,
            config_name=None,
            ref_ext_id=None,
            time=None,
            type_=None):
        api_request = APIRequest('DescribeCaptchaMin', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ConfigName": config_name,
            "RefExtId": ref_ext_id,
            "Time": time,
            "Type": type_}
        return self._handle_request(api_request).result

    def describe_captcha_ip_city(
            self,
            source_ip=None,
            config_name=None,
            ref_ext_id=None,
            time=None,
            type_=None):
        api_request = APIRequest('DescribeCaptchaIpCity', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ConfigName": config_name,
            "RefExtId": ref_ext_id,
            "Time": time,
            "Type": type_}
        return self._handle_request(api_request).result

    def describe_captcha_day(
            self,
            source_ip=None,
            config_name=None,
            ref_ext_id=None,
            time=None,
            type_=None):
        api_request = APIRequest('DescribeCaptchaDay', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ConfigName": config_name,
            "RefExtId": ref_ext_id,
            "Time": time,
            "Type": type_}
        return self._handle_request(api_request).result

    def create_configuration(
            self,
            source_ip=None,
            configuration_name=None,
            max_pv=None,
            configuration_method=None,
            apply_type=None,
            scene=None):
        api_request = APIRequest('CreateConfiguration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ConfigurationName": configuration_name,
            "MaxPV": max_pv,
            "ConfigurationMethod": configuration_method,
            "ApplyType": apply_type,
            "Scene": scene}
        return self._handle_request(api_request).result

    def configuration_style(
            self,
            source_ip=None,
            configuration_method=None,
            ref_ext_id=None,
            apply_type=None,
            scene=None):
        api_request = APIRequest('ConfigurationStyle', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "ConfigurationMethod": configuration_method,
            "RefExtId": ref_ext_id,
            "ApplyType": apply_type,
            "Scene": scene}
        return self._handle_request(api_request).result

    def authenticate_sig(
            self,
            sig=None,
            remote_ip=None,
            source_ip=None,
            app_key=None,
            session_id=None,
            token=None,
            scene=None):
        api_request = APIRequest('AuthenticateSig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Sig": sig,
            "RemoteIp": remote_ip,
            "SourceIp": source_ip,
            "AppKey": app_key,
            "SessionId": session_id,
            "Token": token,
            "Scene": scene}
        return self._handle_request(api_request).result

    def analyze_nvc(self, source_ip=None, data=None, score_json_str=None):
        api_request = APIRequest('AnalyzeNvc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Data": data, "ScoreJsonStr": score_json_str}
        return self._handle_request(api_request).result
