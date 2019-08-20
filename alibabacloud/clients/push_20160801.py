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


class PushClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Push'
        self.api_version = '2016-08-01'
        self.location_service_code = None
        self.location_endpoint_type = 'openAPI'

    def query_devices_by_alias(self, alias=None, app_key=None):
        api_request = APIRequest('QueryDevicesByAlias', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Alias": alias, "AppKey": app_key}
        return self._handle_request(api_request).result

    def query_devices_by_account(self, app_key=None, account=None):
        api_request = APIRequest('QueryDevicesByAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AppKey": app_key, "Account": account}
        return self._handle_request(api_request).result

    def unbind_phone(self, app_key=None, device_id=None):
        api_request = APIRequest('UnbindPhone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AppKey": app_key, "DeviceId": device_id}
        return self._handle_request(api_request).result

    def bind_phone(self, phone_number=None, app_key=None, device_id=None):
        api_request = APIRequest('BindPhone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PhoneNumber": phone_number,
            "AppKey": app_key,
            "DeviceId": device_id}
        return self._handle_request(api_request).result

    def remove_tag(self, tag_name=None, app_key=None):
        api_request = APIRequest('RemoveTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TagName": tag_name, "AppKey": app_key}
        return self._handle_request(api_request).result

    def check_devices(self, device_ids=None, app_key=None):
        api_request = APIRequest('CheckDevices', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DeviceIds": device_ids, "AppKey": app_key}
        return self._handle_request(api_request).result

    def query_push_list(
            self,
            page_size=None,
            end_time=None,
            app_key=None,
            start_time=None,
            page=None,
            push_type=None):
        api_request = APIRequest('QueryPushList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "EndTime": end_time,
            "AppKey": app_key,
            "StartTime": start_time,
            "Page": page,
            "PushType": push_type}
        return self._handle_request(api_request).result

    def check_device(self, app_key=None, device_id=None):
        api_request = APIRequest('CheckDevice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AppKey": app_key, "DeviceId": device_id}
        return self._handle_request(api_request).result

    def unbind_tag(self, tag_name=None, client_key=None, app_key=None, key_type=None):
        api_request = APIRequest('UnbindTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TagName": tag_name,
            "ClientKey": client_key,
            "AppKey": app_key,
            "KeyType": key_type}
        return self._handle_request(api_request).result

    def unbind_alias(self, alias_name=None, app_key=None, device_id=None, unbind_all=None):
        api_request = APIRequest('UnbindAlias', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AliasName": alias_name,
            "AppKey": app_key,
            "DeviceId": device_id,
            "UnbindAll": unbind_all}
        return self._handle_request(api_request).result

    def query_unique_device_stat(
            self,
            granularity=None,
            end_time=None,
            app_key=None,
            start_time=None):
        api_request = APIRequest('QueryUniqueDeviceStat', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Granularity": granularity,
            "EndTime": end_time,
            "AppKey": app_key,
            "StartTime": start_time}
        return self._handle_request(api_request).result

    def query_tags(self, client_key=None, app_key=None, key_type=None):
        api_request = APIRequest('QueryTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClientKey": client_key, "AppKey": app_key, "KeyType": key_type}
        return self._handle_request(api_request).result

    def query_push_stat_by_msg(self, message_id=None, app_key=None):
        api_request = APIRequest('QueryPushStatByMsg', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MessageId": message_id, "AppKey": app_key}
        return self._handle_request(api_request).result

    def query_push_stat_by_app(
            self,
            granularity=None,
            end_time=None,
            app_key=None,
            start_time=None):
        api_request = APIRequest('QueryPushStatByApp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Granularity": granularity,
            "EndTime": end_time,
            "AppKey": app_key,
            "StartTime": start_time}
        return self._handle_request(api_request).result

    def query_device_stat(
            self,
            end_time=None,
            app_key=None,
            start_time=None,
            device_type=None,
            query_type=None):
        api_request = APIRequest('QueryDeviceStat', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndTime": end_time,
            "AppKey": app_key,
            "StartTime": start_time,
            "DeviceType": device_type,
            "QueryType": query_type}
        return self._handle_request(api_request).result

    def query_device_info(self, app_key=None, device_id=None):
        api_request = APIRequest('QueryDeviceInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AppKey": app_key, "DeviceId": device_id}
        return self._handle_request(api_request).result

    def query_aliases(self, app_key=None, device_id=None):
        api_request = APIRequest('QueryAliases', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AppKey": app_key, "DeviceId": device_id}
        return self._handle_request(api_request).result

    def push_notice_toi_os(
            self,
            ext_parameters=None,
            apns_env=None,
            app_key=None,
            target_value=None,
            title=None,
            body=None,
            job_key=None,
            target=None):
        api_request = APIRequest('PushNoticeToiOS', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ExtParameters": ext_parameters,
            "ApnsEnv": apns_env,
            "AppKey": app_key,
            "TargetValue": target_value,
            "Title": title,
            "Body": body,
            "JobKey": job_key,
            "Target": target}
        return self._handle_request(api_request).result

    def push_notice_to_android(
            self,
            ext_parameters=None,
            app_key=None,
            target_value=None,
            title=None,
            body=None,
            job_key=None,
            target=None):
        api_request = APIRequest('PushNoticeToAndroid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ExtParameters": ext_parameters,
            "AppKey": app_key,
            "TargetValue": target_value,
            "Title": title,
            "Body": body,
            "JobKey": job_key,
            "Target": target}
        return self._handle_request(api_request).result

    def push_message_toi_os(
            self,
            app_key=None,
            target_value=None,
            title=None,
            body=None,
            job_key=None,
            target=None):
        api_request = APIRequest('PushMessageToiOS', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppKey": app_key,
            "TargetValue": target_value,
            "Title": title,
            "Body": body,
            "JobKey": job_key,
            "Target": target}
        return self._handle_request(api_request).result

    def push_message_to_android(
            self,
            app_key=None,
            target_value=None,
            title=None,
            body=None,
            job_key=None,
            target=None):
        api_request = APIRequest('PushMessageToAndroid', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AppKey": app_key,
            "TargetValue": target_value,
            "Title": title,
            "Body": body,
            "JobKey": job_key,
            "Target": target}
        return self._handle_request(api_request).result

    def push(
            self,
            android_notification_bar_type=None,
            sms_send_policy=None,
            android_ext_parameters=None,
            ios_badge=None,
            ios_badge_auto_increment=None,
            android_open_type=None,
            title=None,
            body=None,
            device_type=None,
            push_time=None,
            sms_delay_secs=None,
            send_speed=None,
            android_popup_activity=None,
            ios_remind_body=None,
            ios_ext_parameters=None,
            android_notify_type=None,
            android_popup_title=None,
            ios_music=None,
            ios_apns_env=None,
            ios_mutable_content=None,
            android_notification_bar_priority=None,
            expire_time=None,
            sms_template_name=None,
            android_popup_body=None,
            ios_notification_category=None,
            store_offline=None,
            ios_silent_notification=None,
            sms_params=None,
            job_key=None,
            target=None,
            android_open_url=None,
            android_notification_channel=None,
            android_remind=None,
            android_activity=None,
            android_xiao_mi_notify_body=None,
            ios_subtitle=None,
            sms_sign_name=None,
            ios_remind=None,
            app_key=None,
            target_value=None,
            android_music=None,
            android_xiao_mi_activity=None,
            android_xiao_mi_notify_title=None,
            push_type=None):
        api_request = APIRequest('Push', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AndroidNotificationBarType": android_notification_bar_type,
            "SmsSendPolicy": sms_send_policy,
            "AndroidExtParameters": android_ext_parameters,
            "iOSBadge": ios_badge,
            "iOSBadgeAutoIncrement": ios_badge_auto_increment,
            "AndroidOpenType": android_open_type,
            "Title": title,
            "Body": body,
            "DeviceType": device_type,
            "PushTime": push_time,
            "SmsDelaySecs": sms_delay_secs,
            "SendSpeed": send_speed,
            "AndroidPopupActivity": android_popup_activity,
            "iOSRemindBody": ios_remind_body,
            "iOSExtParameters": ios_ext_parameters,
            "AndroidNotifyType": android_notify_type,
            "AndroidPopupTitle": android_popup_title,
            "iOSMusic": ios_music,
            "iOSApnsEnv": ios_apns_env,
            "iOSMutableContent": ios_mutable_content,
            "AndroidNotificationBarPriority": android_notification_bar_priority,
            "ExpireTime": expire_time,
            "SmsTemplateName": sms_template_name,
            "AndroidPopupBody": android_popup_body,
            "iOSNotificationCategory": ios_notification_category,
            "StoreOffline": store_offline,
            "iOSSilentNotification": ios_silent_notification,
            "SmsParams": sms_params,
            "JobKey": job_key,
            "Target": target,
            "AndroidOpenUrl": android_open_url,
            "AndroidNotificationChannel": android_notification_channel,
            "AndroidRemind": android_remind,
            "AndroidActivity": android_activity,
            "AndroidXiaoMiNotifyBody": android_xiao_mi_notify_body,
            "iOSSubtitle": ios_subtitle,
            "SmsSignName": sms_sign_name,
            "iOSRemind": ios_remind,
            "AppKey": app_key,
            "TargetValue": target_value,
            "AndroidMusic": android_music,
            "AndroidXiaoMiActivity": android_xiao_mi_activity,
            "AndroidXiaoMiNotifyTitle": android_xiao_mi_notify_title,
            "PushType": push_type}
        return self._handle_request(api_request).result

    def list_tags(self, app_key=None):
        api_request = APIRequest('ListTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AppKey": app_key}
        return self._handle_request(api_request).result

    def list_summary_apps(self,):
        api_request = APIRequest('ListSummaryApps', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def list_push_records(
            self,
            page_size=None,
            end_time=None,
            app_key=None,
            start_time=None,
            page=None,
            push_type=None):
        api_request = APIRequest('ListPushRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "EndTime": end_time,
            "AppKey": app_key,
            "StartTime": start_time,
            "Page": page,
            "PushType": push_type}
        return self._handle_request(api_request).result

    def bind_tag(self, tag_name=None, client_key=None, app_key=None, key_type=None):
        api_request = APIRequest('BindTag', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TagName": tag_name,
            "ClientKey": client_key,
            "AppKey": app_key,
            "KeyType": key_type}
        return self._handle_request(api_request).result

    def bind_alias(self, alias_name=None, app_key=None, device_id=None):
        api_request = APIRequest('BindAlias', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AliasName": alias_name, "AppKey": app_key, "DeviceId": device_id}
        return self._handle_request(api_request).result

    def cancel_push(self, message_id=None, app_key=None):
        api_request = APIRequest('CancelPush', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MessageId": message_id, "AppKey": app_key}
        return self._handle_request(api_request).result
