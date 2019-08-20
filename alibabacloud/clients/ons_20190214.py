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


class OnsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Ons'
        self.api_version = '2019-02-14'
        self.location_service_code = 'ons'
        self.location_endpoint_type = 'openAPI'

    def ons_group_sub_detail(self, instance_id=None, group_id=None):
        api_request = APIRequest('OnsGroupSubDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id}
        return self._handle_request(api_request).result

    def ons_topic_sub_detail(self, instance_id=None, topic=None):
        api_request = APIRequest('OnsTopicSubDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Topic": topic}
        return self._handle_request(api_request).result

    def ons_dlq_message_get_by_id(self, instance_id=None, group_id=None, msg_id=None):
        api_request = APIRequest('OnsDLQMessageGetById', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id, "MsgId": msg_id}
        return self._handle_request(api_request).result

    def ons_dlq_message_page_query_by_group_id(
            self,
            instance_id=None,
            group_id=None,
            page_size=None,
            end_time=None,
            begin_time=None,
            current_page=None,
            task_id=None):
        api_request = APIRequest('OnsDLQMessagePageQueryByGroupId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "GroupId": group_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "BeginTime": begin_time,
            "CurrentPage": current_page,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def ons_dlq_message_resend_by_id(self, instance_id=None, group_id=None, msg_id=None):
        api_request = APIRequest('OnsDLQMessageResendById', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id, "MsgId": msg_id}
        return self._handle_request(api_request).result

    def ons_consumer_accumulate(self, instance_id=None, group_id=None, detail=None):
        api_request = APIRequest('OnsConsumerAccumulate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id, "Detail": detail}
        return self._handle_request(api_request).result

    def ons_consumer_get_connection(self, instance_id=None, group_id=None):
        api_request = APIRequest('OnsConsumerGetConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id}
        return self._handle_request(api_request).result

    def ons_consumer_status(self, instance_id=None, need_jstack=None, group_id=None, detail=None):
        api_request = APIRequest('OnsConsumerStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "NeedJstack": need_jstack,
            "GroupId": group_id,
            "Detail": detail}
        return self._handle_request(api_request).result

    def ons_group_consumer_update(self, read_enable=None, instance_id=None, group_id=None):
        api_request = APIRequest('OnsGroupConsumerUpdate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ReadEnable": read_enable,
            "InstanceId": instance_id,
            "GroupId": group_id}
        return self._handle_request(api_request).result

    def ons_group_delete(self, instance_id=None, group_id=None):
        api_request = APIRequest('OnsGroupDelete', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id}
        return self._handle_request(api_request).result

    def ons_consumer_reset_offset(
            self,
            instance_id=None,
            group_id=None,
            topic=None,
            reset_timestamp=None,
            type_=None):
        api_request = APIRequest('OnsConsumerResetOffset', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "GroupId": group_id,
            "Topic": topic,
            "ResetTimestamp": reset_timestamp,
            "Type": type_}
        return self._handle_request(api_request).result

    def ons_consumer_time_span(self, instance_id=None, group_id=None, topic=None):
        api_request = APIRequest('OnsConsumerTimeSpan', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id, "Topic": topic}
        return self._handle_request(api_request).result

    def ons_group_create(self, instance_id=None, group_id=None, remark=None):
        api_request = APIRequest('OnsGroupCreate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id, "Remark": remark}
        return self._handle_request(api_request).result

    def ons_instance_base_info(self, instance_id=None):
        api_request = APIRequest('OnsInstanceBaseInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def ons_group_list(self, instance_id=None, group_id=None):
        api_request = APIRequest('OnsGroupList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id}
        return self._handle_request(api_request).result

    def ons_instance_create(self, instance_name=None, remark=None):
        api_request = APIRequest('OnsInstanceCreate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceName": instance_name, "Remark": remark}
        return self._handle_request(api_request).result

    def ons_instance_delete(self, instance_id=None):
        api_request = APIRequest('OnsInstanceDelete', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def ons_instance_in_service_list(self,):
        api_request = APIRequest('OnsInstanceInServiceList', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def ons_instance_update(self, instance_name=None, instance_id=None, remark=None):
        api_request = APIRequest('OnsInstanceUpdate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceName": instance_name,
            "InstanceId": instance_id,
            "Remark": remark}
        return self._handle_request(api_request).result

    def ons_message_get_by_key(self, instance_id=None, topic=None, key=None):
        api_request = APIRequest('OnsMessageGetByKey', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Topic": topic, "Key": key}
        return self._handle_request(api_request).result

    def ons_message_get_by_msg_id(self, instance_id=None, msg_id=None, topic=None):
        api_request = APIRequest('OnsMessageGetByMsgId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "MsgId": msg_id, "Topic": topic}
        return self._handle_request(api_request).result

    def ons_message_page_query_by_topic(
            self,
            instance_id=None,
            page_size=None,
            topic=None,
            end_time=None,
            begin_time=None,
            current_page=None,
            task_id=None):
        api_request = APIRequest('OnsMessagePageQueryByTopic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "Topic": topic,
            "EndTime": end_time,
            "BeginTime": begin_time,
            "CurrentPage": current_page,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def ons_message_trace(self, instance_id=None, topic=None, msg_id=None):
        api_request = APIRequest('OnsMessageTrace', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Topic": topic, "MsgId": msg_id}
        return self._handle_request(api_request).result

    def ons_message_push(
            self,
            client_id=None,
            instance_id=None,
            group_id=None,
            msg_id=None,
            topic=None):
        api_request = APIRequest('OnsMessagePush', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientId": client_id,
            "InstanceId": instance_id,
            "GroupId": group_id,
            "MsgId": msg_id,
            "Topic": topic}
        return self._handle_request(api_request).result

    def ons_message_send(self, instance_id=None, topic=None, tag=None, message=None, key=None):
        api_request = APIRequest('OnsMessageSend', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Topic": topic,
            "Tag": tag,
            "Message": message,
            "Key": key}
        return self._handle_request(api_request).result

    def ons_mqtt_group_id_create(self, instance_id=None, group_id=None, topic=None):
        api_request = APIRequest('OnsMqttGroupIdCreate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id, "Topic": topic}
        return self._handle_request(api_request).result

    def ons_mqtt_group_id_delete(self, instance_id=None, group_id=None):
        api_request = APIRequest('OnsMqttGroupIdDelete', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id}
        return self._handle_request(api_request).result

    def ons_mqtt_group_id_list(self, instance_id=None):
        api_request = APIRequest('OnsMqttGroupIdList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def ons_mqtt_query_client_by_client_id(self, client_id=None, instance_id=None):
        api_request = APIRequest('OnsMqttQueryClientByClientId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClientId": client_id, "InstanceId": instance_id}
        return self._handle_request(api_request).result

    def ons_mqtt_query_client_by_group_id(self, instance_id=None, group_id=None):
        api_request = APIRequest('OnsMqttQueryClientByGroupId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id}
        return self._handle_request(api_request).result

    def ons_mqtt_query_client_by_topic(self, instance_id=None, parent_topic=None, sub_topic=None):
        api_request = APIRequest('OnsMqttQueryClientByTopic', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "ParentTopic": parent_topic,
            "SubTopic": sub_topic}
        return self._handle_request(api_request).result

    def ons_mqtt_query_history_online(
            self,
            instance_id=None,
            group_id=None,
            end_time=None,
            begin_time=None):
        api_request = APIRequest('OnsMqttQueryHistoryOnline', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "GroupId": group_id,
            "EndTime": end_time,
            "BeginTime": begin_time}
        return self._handle_request(api_request).result

    def ons_mqtt_query_msg_trans_trend(
            self,
            instance_id=None,
            qos=None,
            trans_type=None,
            end_time=None,
            begin_time=None,
            tps_type=None,
            parent_topic=None,
            msg_type=None,
            sub_topic=None):
        api_request = APIRequest('OnsMqttQueryMsgTransTrend', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Qos": qos,
            "TransType": trans_type,
            "EndTime": end_time,
            "BeginTime": begin_time,
            "TpsType": tps_type,
            "ParentTopic": parent_topic,
            "MsgType": msg_type,
            "SubTopic": sub_topic}
        return self._handle_request(api_request).result

    def ons_region_list(self,):
        api_request = APIRequest('OnsRegionList', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def ons_topic_create(self, instance_id=None, message_type=None, topic=None, remark=None):
        api_request = APIRequest('OnsTopicCreate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "MessageType": message_type,
            "Topic": topic,
            "Remark": remark}
        return self._handle_request(api_request).result

    def ons_topic_delete(self, instance_id=None, topic=None):
        api_request = APIRequest('OnsTopicDelete', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Topic": topic}
        return self._handle_request(api_request).result

    def ons_topic_list(self, instance_id=None, topic=None):
        api_request = APIRequest('OnsTopicList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Topic": topic}
        return self._handle_request(api_request).result

    def ons_topic_status(self, instance_id=None, topic=None):
        api_request = APIRequest('OnsTopicStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Topic": topic}
        return self._handle_request(api_request).result

    def ons_topic_update(self, instance_id=None, perm=None, topic=None):
        api_request = APIRequest('OnsTopicUpdate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Perm": perm, "Topic": topic}
        return self._handle_request(api_request).result

    def ons_trace_get_result(self, query_id=None):
        api_request = APIRequest('OnsTraceGetResult', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"QueryId": query_id}
        return self._handle_request(api_request).result

    def ons_trace_query_by_msg_id(
            self,
            instance_id=None,
            topic=None,
            msg_id=None,
            end_time=None,
            begin_time=None):
        api_request = APIRequest('OnsTraceQueryByMsgId', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Topic": topic,
            "MsgId": msg_id,
            "EndTime": end_time,
            "BeginTime": begin_time}
        return self._handle_request(api_request).result

    def ons_trace_query_by_msg_key(
            self,
            instance_id=None,
            topic=None,
            end_time=None,
            begin_time=None,
            msg_key=None):
        api_request = APIRequest('OnsTraceQueryByMsgKey', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "Topic": topic,
            "EndTime": end_time,
            "BeginTime": begin_time,
            "MsgKey": msg_key}
        return self._handle_request(api_request).result

    def ons_trend_group_output_tps(
            self,
            period=None,
            instance_id=None,
            group_id=None,
            topic=None,
            end_time=None,
            begin_time=None,
            type_=None):
        api_request = APIRequest('OnsTrendGroupOutputTps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "InstanceId": instance_id,
            "GroupId": group_id,
            "Topic": topic,
            "EndTime": end_time,
            "BeginTime": begin_time,
            "Type": type_}
        return self._handle_request(api_request).result

    def ons_trend_topic_input_tps(
            self,
            period=None,
            instance_id=None,
            topic=None,
            end_time=None,
            begin_time=None,
            type_=None):
        api_request = APIRequest('OnsTrendTopicInputTps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "InstanceId": instance_id,
            "Topic": topic,
            "EndTime": end_time,
            "BeginTime": begin_time,
            "Type": type_}
        return self._handle_request(api_request).result

    def ons_warn_create(
            self,
            instance_id=None,
            block_time=None,
            level=None,
            group_id=None,
            delay_time=None,
            topic=None,
            threshold=None,
            alert_time=None,
            contacts=None):
        api_request = APIRequest('OnsWarnCreate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "BlockTime": block_time,
            "Level": level,
            "GroupId": group_id,
            "DelayTime": delay_time,
            "Topic": topic,
            "Threshold": threshold,
            "AlertTime": alert_time,
            "Contacts": contacts}
        return self._handle_request(api_request).result

    def ons_warn_delete(self, instance_id=None, group_id=None, topic=None):
        api_request = APIRequest('OnsWarnDelete', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "GroupId": group_id, "Topic": topic}
        return self._handle_request(api_request).result
