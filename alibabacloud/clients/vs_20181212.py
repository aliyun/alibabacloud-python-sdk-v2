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


class VsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'vs'
        self.api_version = '2018-12-12'
        self.location_service_code = 'vs'
        self.location_endpoint_type = 'openAPI'

    def describe_device_channels(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('DescribeDeviceChannels', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def sync_catalogs(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('SyncCatalogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def unlock_device(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('UnlockDevice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vod_stream_url(self, show_log=None, tx_id=None, owner_id=None, url=None):
        api_request = APIRequest('DescribeVodStreamURL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ShowLog": show_log, "TxId": tx_id, "OwnerId": owner_id, "Url": url}
        return self._handle_request(api_request).result

    def batch_unbind_templates(
            self,
            template_type=None,
            instance_type=None,
            show_log=None,
            owner_id=None,
            template_id=None,
            instance_id=None):
        api_request = APIRequest('BatchUnbindTemplates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TemplateType": template_type,
            "InstanceType": instance_type,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "TemplateId": template_id,
            "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def batch_bind_templates(
            self,
            replace=None,
            instance_type=None,
            show_log=None,
            apply_all=None,
            owner_id=None,
            template_id=None,
            instance_id=None):
        api_request = APIRequest('BatchBindTemplates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Replace": replace,
            "InstanceType": instance_type,
            "ShowLog": show_log,
            "ApplyAll": apply_all,
            "OwnerId": owner_id,
            "TemplateId": template_id,
            "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def batch_stop_streams(self, start_time=None, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('BatchStopStreams', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Id": id_,
            "ShowLog": show_log,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_start_streams(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('BatchStartStreams', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_stream_url(
            self,
            auth_key=None,
            auth=None,
            type_=None,
            id_=None,
            show_log=None,
            out_protocol=None,
            owner_id=None,
            expire=None,
            location=None):
        api_request = APIRequest('DescribeStreamURL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AuthKey": auth_key,
            "Auth": auth,
            "Type": type_,
            "Id": id_,
            "ShowLog": show_log,
            "OutProtocol": out_protocol,
            "OwnerId": owner_id,
            "Expire": expire,
            "Location": location}
        return self._handle_request(api_request).result

    def batch_delete_devices(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('BatchDeleteDevices', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_stop_devices(self, start_time=None, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('BatchStopDevices', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Id": id_,
            "ShowLog": show_log,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_start_devices(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('BatchStartDevices', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vs_domain_certificate_info(self, show_log=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeVsDomainCertificateInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ShowLog": show_log, "DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vs_user_resource_package(self, security_token=None, owner_id=None, show_log=None):
        api_request = APIRequest('DescribeVsUserResourcePackage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityToken": security_token,
            "OwnerId": owner_id,
            "ShowLog": show_log}
        return self._handle_request(api_request).result

    def describe_vs_certificate_list(self, show_log=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeVsCertificateList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ShowLog": show_log, "DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vs_certificate_detail(self, show_log=None, cert_name=None, owner_id=None):
        api_request = APIRequest('DescribeVsCertificateDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ShowLog": show_log, "CertName": cert_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_vs_domain_certificate(
            self,
            ssl_protocol=None,
            cert_type=None,
            show_log=None,
            ssl_pri=None,
            force_set=None,
            cert_name=None,
            domain_name=None,
            owner_id=None,
            ssl_pub=None,
            region=None):
        api_request = APIRequest('SetVsDomainCertificate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SSLProtocol": ssl_protocol,
            "CertType": cert_type,
            "ShowLog": show_log,
            "SSLPri": ssl_pri,
            "ForceSet": force_set,
            "CertName": cert_name,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "SSLPub": ssl_pub,
            "Region": region}
        return self._handle_request(api_request).result

    def describe_vs_domain_detail(self, show_log=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeVsDomainDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ShowLog": show_log, "DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vs_domain_traffic_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            show_log=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeVsDomainTrafficData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "ShowLog": show_log,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_vs_domain_bps_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            show_log=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeVsDomainBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "ShowLog": show_log,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_vs_domain_req_traffic_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            show_log=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeVsDomainReqTrafficData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "ShowLog": show_log,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_vs_domain_req_bps_data(
            self,
            location_name_en=None,
            start_time=None,
            isp_name_en=None,
            show_log=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            interval=None):
        api_request = APIRequest('DescribeVsDomainReqBpsData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "LocationNameEn": location_name_en,
            "StartTime": start_time,
            "IspNameEn": isp_name_en,
            "ShowLog": show_log,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "Interval": interval}
        return self._handle_request(api_request).result

    def describe_vs_domain_record_data(
            self,
            start_time=None,
            show_log=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeVsDomainRecordData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "ShowLog": show_log,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vs_domain_snapshot_data(
            self,
            start_time=None,
            show_log=None,
            domain_name=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeVsDomainSnapshotData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "ShowLog": show_log,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_device(self, start_time=None, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('StopDevice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Id": id_,
            "ShowLog": show_log,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_device(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('StartDevice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_device(
            self,
            gb_id=None,
            description=None,
            type_=None,
            auto_start=None,
            parent_id=None,
            password=None,
            vendor=None,
            id_=None,
            show_log=None,
            group_id=None,
            ip=None,
            owner_id=None,
            url=None,
            port=None,
            name=None,
            username=None):
        api_request = APIRequest('ModifyDevice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GbId": gb_id,
            "Description": description,
            "Type": type_,
            "AutoStart": auto_start,
            "ParentId": parent_id,
            "Password": password,
            "Vendor": vendor,
            "Id": id_,
            "ShowLog": show_log,
            "GroupId": group_id,
            "Ip": ip,
            "OwnerId": owner_id,
            "Url": url,
            "Port": port,
            "Name": name,
            "Username": username}
        return self._handle_request(api_request).result

    def create_device(
            self,
            gb_id=None,
            description=None,
            type_=None,
            auto_start=None,
            parent_id=None,
            password=None,
            vendor=None,
            show_log=None,
            group_id=None,
            ip=None,
            owner_id=None,
            url=None,
            port=None,
            name=None,
            username=None):
        api_request = APIRequest('CreateDevice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GbId": gb_id,
            "Description": description,
            "Type": type_,
            "AutoStart": auto_start,
            "ParentId": parent_id,
            "Password": password,
            "Vendor": vendor,
            "ShowLog": show_log,
            "GroupId": group_id,
            "Ip": ip,
            "OwnerId": owner_id,
            "Url": url,
            "Port": port,
            "Name": name,
            "Username": username}
        return self._handle_request(api_request).result

    def describe_device(self, include_stats=None, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('DescribeDevice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IncludeStats": include_stats,
            "Id": id_,
            "ShowLog": show_log,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_device(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('DeleteDevice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_devices(
            self,
            sort_direction=None,
            type_=None,
            page_num=None,
            parent_id=None,
            include_stats=None,
            vendor=None,
            page_size=None,
            id_=None,
            show_log=None,
            group_id=None,
            owner_id=None,
            name=None,
            sort_by=None,
            status=None):
        api_request = APIRequest('DescribeDevices', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SortDirection": sort_direction,
            "Type": type_,
            "PageNum": page_num,
            "ParentId": parent_id,
            "IncludeStats": include_stats,
            "Vendor": vendor,
            "PageSize": page_size,
            "Id": id_,
            "ShowLog": show_log,
            "GroupId": group_id,
            "OwnerId": owner_id,
            "Name": name,
            "SortBy": sort_by,
            "Status": status}
        return self._handle_request(api_request).result

    def create_template(
            self,
            hls_ts=None,
            oss_endpoint=None,
            description=None,
            oss_file_prefix=None,
            jpg_overwrite=None,
            start_time=None,
            type_=None,
            retention=None,
            show_log=None,
            hls_m3u8=None,
            oss_bucket=None,
            end_time=None,
            owner_id=None,
            jpg_sequence=None,
            mp4=None,
            flv=None,
            name=None,
            callback=None,
            interval=None,
            file_format=None,
            region=None):
        api_request = APIRequest('CreateTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HlsTs": hls_ts,
            "OssEndpoint": oss_endpoint,
            "Description": description,
            "OssFilePrefix": oss_file_prefix,
            "JpgOverwrite": jpg_overwrite,
            "StartTime": start_time,
            "Type": type_,
            "Retention": retention,
            "ShowLog": show_log,
            "HlsM3u8": hls_m3u8,
            "OssBucket": oss_bucket,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "JpgSequence": jpg_sequence,
            "Mp4": mp4,
            "Flv": flv,
            "Name": name,
            "Callback": callback,
            "Interval": interval,
            "FileFormat": file_format,
            "Region": region}
        return self._handle_request(api_request).result

    def delete_template(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('DeleteTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_unbind_template(
            self,
            template_type=None,
            instance_type=None,
            show_log=None,
            owner_id=None,
            template_id=None,
            instance_id=None):
        api_request = APIRequest('BatchUnbindTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TemplateType": template_type,
            "InstanceType": instance_type,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "TemplateId": template_id,
            "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def unbind_template(
            self,
            template_type=None,
            instance_type=None,
            show_log=None,
            owner_id=None,
            template_id=None,
            instance_id=None):
        api_request = APIRequest('UnbindTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TemplateType": template_type,
            "InstanceType": instance_type,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "TemplateId": template_id,
            "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def batch_bind_template(
            self,
            replace=None,
            instance_type=None,
            show_log=None,
            apply_all=None,
            owner_id=None,
            template_id=None,
            instance_id=None):
        api_request = APIRequest('BatchBindTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Replace": replace,
            "InstanceType": instance_type,
            "ShowLog": show_log,
            "ApplyAll": apply_all,
            "OwnerId": owner_id,
            "TemplateId": template_id,
            "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def modify_template(
            self,
            hls_ts=None,
            oss_endpoint=None,
            description=None,
            oss_file_prefix=None,
            jpg_overwrite=None,
            start_time=None,
            id_=None,
            retention=None,
            show_log=None,
            hls_m3u8=None,
            oss_bucket=None,
            end_time=None,
            owner_id=None,
            jpg_sequence=None,
            mp4=None,
            flv=None,
            name=None,
            callback=None,
            interval=None,
            file_format=None,
            region=None):
        api_request = APIRequest('ModifyTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HlsTs": hls_ts,
            "OssEndpoint": oss_endpoint,
            "Description": description,
            "OssFilePrefix": oss_file_prefix,
            "JpgOverwrite": jpg_overwrite,
            "StartTime": start_time,
            "Id": id_,
            "Retention": retention,
            "ShowLog": show_log,
            "HlsM3u8": hls_m3u8,
            "OssBucket": oss_bucket,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "JpgSequence": jpg_sequence,
            "Mp4": mp4,
            "Flv": flv,
            "Name": name,
            "Callback": callback,
            "Interval": interval,
            "FileFormat": file_format,
            "Region": region}
        return self._handle_request(api_request).result

    def describe_template(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('DescribeTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_templates(
            self,
            sort_direction=None,
            type_=None,
            page_num=None,
            page_size=None,
            id_=None,
            show_log=None,
            owner_id=None,
            instance_id=None,
            sort_by=None):
        api_request = APIRequest('DescribeTemplates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SortDirection": sort_direction,
            "Type": type_,
            "PageNum": page_num,
            "PageSize": page_size,
            "Id": id_,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "InstanceId": instance_id,
            "SortBy": sort_by}
        return self._handle_request(api_request).result

    def bind_template(
            self,
            replace=None,
            instance_type=None,
            show_log=None,
            apply_all=None,
            owner_id=None,
            template_id=None,
            instance_id=None):
        api_request = APIRequest('BindTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Replace": replace,
            "InstanceType": instance_type,
            "ShowLog": show_log,
            "ApplyAll": apply_all,
            "OwnerId": owner_id,
            "TemplateId": template_id,
            "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def forbid_vs_stream(
            self,
            app_name=None,
            stream_name=None,
            show_log=None,
            control_stream_action=None,
            resume_time=None,
            live_stream_type=None,
            domain_name=None,
            owner_id=None,
            oneshot=None):
        api_request = APIRequest('ForbidVsStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "StreamName": stream_name,
            "ShowLog": show_log,
            "ControlStreamAction": control_stream_action,
            "ResumeTime": resume_time,
            "LiveStreamType": live_stream_type,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "Oneshot": oneshot}
        return self._handle_request(api_request).result

    def batch_forbid_vs_stream(
            self,
            channel=None,
            show_log=None,
            control_stream_action=None,
            resume_time=None,
            live_stream_type=None,
            domain_name=None,
            owner_id=None,
            oneshot=None):
        api_request = APIRequest('BatchForbidVsStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Channel": channel,
            "ShowLog": show_log,
            "ControlStreamAction": control_stream_action,
            "ResumeTime": resume_time,
            "LiveStreamType": live_stream_type,
            "DomainName": domain_name,
            "OwnerId": owner_id,
            "Oneshot": oneshot}
        return self._handle_request(api_request).result

    def describe_stream(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('DescribeStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_resume_vs_stream(
            self,
            channel=None,
            show_log=None,
            control_stream_action=None,
            live_stream_type=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('BatchResumeVsStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Channel": channel,
            "ShowLog": show_log,
            "ControlStreamAction": control_stream_action,
            "LiveStreamType": live_stream_type,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def set_vs_streams_notify_url_config(
            self,
            auth_key=None,
            auth_type=None,
            notify_url=None,
            show_log=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('SetVsStreamsNotifyUrlConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AuthKey": auth_key,
            "AuthType": auth_type,
            "NotifyUrl": notify_url,
            "ShowLog": show_log,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def resume_vs_stream(
            self,
            app_name=None,
            stream_name=None,
            show_log=None,
            control_stream_action=None,
            live_stream_type=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('ResumeVsStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppName": app_name,
            "StreamName": stream_name,
            "ShowLog": show_log,
            "ControlStreamAction": control_stream_action,
            "LiveStreamType": live_stream_type,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def start_stream(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('StartStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vs_streams_notify_url_config(self, show_log=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DescribeVsStreamsNotifyUrlConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ShowLog": show_log, "DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vs_streams_publish_list(
            self,
            start_time=None,
            page_number=None,
            app_name=None,
            page_size=None,
            stream_name=None,
            query_type=None,
            show_log=None,
            stream_type=None,
            domain_name=None,
            end_time=None,
            order_by=None,
            owner_id=None):
        api_request = APIRequest('DescribeVsStreamsPublishList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "PageNumber": page_number,
            "AppName": app_name,
            "PageSize": page_size,
            "StreamName": stream_name,
            "QueryType": query_type,
            "ShowLog": show_log,
            "StreamType": stream_type,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OrderBy": order_by,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_vs_up_peak_publish_stream_data(
            self,
            start_time=None,
            show_log=None,
            domain_name=None,
            end_time=None,
            owner_id=None,
            domain_switch=None):
        api_request = APIRequest('DescribeVsUpPeakPublishStreamData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "ShowLog": show_log,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "DomainSwitch": domain_switch}
        return self._handle_request(api_request).result

    def describe_streams(
            self,
            sort_direction=None,
            page_num=None,
            parent_id=None,
            page_size=None,
            id_=None,
            show_log=None,
            app=None,
            group_id=None,
            owner_id=None,
            device_id=None,
            domain=None,
            name=None,
            sort_by=None):
        api_request = APIRequest('DescribeStreams', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SortDirection": sort_direction,
            "PageNum": page_num,
            "ParentId": parent_id,
            "PageSize": page_size,
            "Id": id_,
            "ShowLog": show_log,
            "App": app,
            "GroupId": group_id,
            "OwnerId": owner_id,
            "DeviceId": device_id,
            "Domain": domain,
            "Name": name,
            "SortBy": sort_by}
        return self._handle_request(api_request).result

    def describe_vs_streams_online_list(
            self,
            start_time=None,
            page_num=None,
            app_name=None,
            page_size=None,
            stream_name=None,
            query_type=None,
            show_log=None,
            stream_type=None,
            domain_name=None,
            end_time=None,
            order_by=None,
            owner_id=None):
        api_request = APIRequest('DescribeVsStreamsOnlineList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "PageNum": page_num,
            "AppName": app_name,
            "PageSize": page_size,
            "StreamName": stream_name,
            "QueryType": query_type,
            "ShowLog": show_log,
            "StreamType": stream_type,
            "DomainName": domain_name,
            "EndTime": end_time,
            "OrderBy": order_by,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_vs_streams_notify_url_config(self, show_log=None, domain_name=None, owner_id=None):
        api_request = APIRequest('DeleteVsStreamsNotifyUrlConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ShowLog": show_log, "DomainName": domain_name, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def stop_stream(self, start_time=None, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('StopStream', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StartTime": start_time,
            "Id": id_,
            "ShowLog": show_log,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_group(self, include_stats=None, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('DescribeGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "IncludeStats": include_stats,
            "Id": id_,
            "ShowLog": show_log,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_group(
            self,
            description=None,
            enabled=None,
            push_domain=None,
            id_=None,
            show_log=None,
            play_domain=None,
            out_protocol=None,
            owner_id=None,
            in_protocol=None,
            name=None,
            region=None):
        api_request = APIRequest('ModifyGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Description": description,
            "Enabled": enabled,
            "PushDomain": push_domain,
            "Id": id_,
            "ShowLog": show_log,
            "PlayDomain": play_domain,
            "OutProtocol": out_protocol,
            "OwnerId": owner_id,
            "InProtocol": in_protocol,
            "Name": name,
            "Region": region}
        return self._handle_request(api_request).result

    def create_group(
            self,
            description=None,
            push_domain=None,
            show_log=None,
            app=None,
            play_domain=None,
            out_protocol=None,
            owner_id=None,
            in_protocol=None,
            name=None,
            region=None):
        api_request = APIRequest('CreateGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Description": description,
            "PushDomain": push_domain,
            "ShowLog": show_log,
            "App": app,
            "PlayDomain": play_domain,
            "OutProtocol": out_protocol,
            "OwnerId": owner_id,
            "InProtocol": in_protocol,
            "Name": name,
            "Region": region}
        return self._handle_request(api_request).result

    def delete_group(self, id_=None, show_log=None, owner_id=None):
        api_request = APIRequest('DeleteGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": id_, "ShowLog": show_log, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_records(
            self,
            sort_direction=None,
            start_time=None,
            type_=None,
            page_num=None,
            page_size=None,
            show_log=None,
            stream_id=None,
            end_time=None,
            owner_id=None,
            sort_by=None):
        api_request = APIRequest('DescribeRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SortDirection": sort_direction,
            "StartTime": start_time,
            "Type": type_,
            "PageNum": page_num,
            "PageSize": page_size,
            "ShowLog": show_log,
            "StreamId": stream_id,
            "EndTime": end_time,
            "OwnerId": owner_id,
            "SortBy": sort_by}
        return self._handle_request(api_request).result

    def describe_groups(
            self,
            sort_direction=None,
            page_num=None,
            include_stats=None,
            page_size=None,
            id_=None,
            show_log=None,
            owner_id=None,
            in_protocol=None,
            name=None,
            sort_by=None,
            region=None,
            status=None):
        api_request = APIRequest('DescribeGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SortDirection": sort_direction,
            "PageNum": page_num,
            "IncludeStats": include_stats,
            "PageSize": page_size,
            "Id": id_,
            "ShowLog": show_log,
            "OwnerId": owner_id,
            "InProtocol": in_protocol,
            "Name": name,
            "SortBy": sort_by,
            "Region": region,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_vs_domain_configs(
            self,
            function_names=None,
            show_log=None,
            domain_name=None,
            owner_id=None):
        api_request = APIRequest('DescribeVsDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FunctionNames": function_names,
            "ShowLog": show_log,
            "DomainName": domain_name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_set_vs_domain_configs(
            self,
            functions=None,
            domain_names=None,
            show_log=None,
            owner_id=None):
        api_request = APIRequest('BatchSetVsDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Functions": functions,
            "DomainNames": domain_names,
            "ShowLog": show_log,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def batch_delete_vs_domain_configs(
            self,
            function_names=None,
            domain_names=None,
            show_log=None,
            owner_id=None):
        api_request = APIRequest('BatchDeleteVsDomainConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FunctionNames": function_names,
            "DomainNames": domain_names,
            "ShowLog": show_log,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result
