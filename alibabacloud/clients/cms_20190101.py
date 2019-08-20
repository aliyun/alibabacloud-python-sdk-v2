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


class CmsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Cms'
        self.api_version = '2019-01-01'
        self.location_service_code = 'cms'
        self.location_endpoint_type = 'openAPI'

    def create_metric_rule_resources(self, resources=None, rule_id=None, overwrite=None):
        api_request = APIRequest('CreateMetricRuleResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Resources": resources, "RuleId": rule_id, "Overwrite": overwrite}
        return self._handle_request(api_request).result

    def delete_metric_rule_resources(self, resources=None, rule_id=None):
        api_request = APIRequest('DeleteMetricRuleResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Resources": resources, "RuleId": rule_id}
        return self._handle_request(api_request).result

    def delete_metric_rule_targets(self, list_of_target_ids=None, rule_id=None):
        api_request = APIRequest('DeleteMetricRuleTargets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TargetIds": list_of_target_ids, "RuleId": rule_id}
        repeat_info = {"TargetIds": ('TargetIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def put_metric_rule_targets(self, rule_id=None, list_of_targets=None):
        api_request = APIRequest('PutMetricRuleTargets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RuleId": rule_id, "Targets": list_of_targets}
        repeat_info = {"Targets": ('Targets', 'list', 'dict', [('Level', 'str', None, None),
                                                               ('Id', 'str', None, None),
                                                               ('Arn', 'str', None, None),
                                                               ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_metric_rule_targets(self, rule_id=None):
        api_request = APIRequest('DescribeMetricRuleTargets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RuleId": rule_id}
        return self._handle_request(api_request).result

    def modify_monitor_group_instances(self, list_of_instances=None, group_id=None):
        api_request = APIRequest('ModifyMonitorGroupInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Instances": list_of_instances, "GroupId": group_id}
        repeat_info = {"Instances": ('Instances',
                                     'list',
                                     'dict',
                                     [('InstanceId',
                                       'str',
                                       None,
                                       None),
                                      ('InstanceName',
                                       'str',
                                       None,
                                       None),
                                         ('RegionId',
                                          'str',
                                          None,
                                          None),
                                         ('Category',
                                          'str',
                                          None,
                                          None),
                                      ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_monitoring_agent_statuses(self, instance_ids=None):
        api_request = APIRequest('DescribeMonitoringAgentStatuses', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceIds": instance_ids}
        return self._handle_request(api_request).result

    def create_monitor_agent_process(self, instance_id=None, process_name=None, process_user=None):
        api_request = APIRequest('CreateMonitorAgentProcess', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "ProcessName": process_name,
            "ProcessUser": process_user}
        return self._handle_request(api_request).result

    def describe_alert_history_list(
            self,
            group_id=None,
            alert_status=None,
            namespace=None,
            page_size=None,
            end_time=None,
            rule_name=None,
            state=None,
            start_time=None,
            page=None,
            rule_id=None,
            metric_name=None,
            ascending=None):
        api_request = APIRequest('DescribeAlertHistoryList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GroupId": group_id,
            "AlertStatus": alert_status,
            "Namespace": namespace,
            "PageSize": page_size,
            "EndTime": end_time,
            "RuleName": rule_name,
            "State": state,
            "StartTime": start_time,
            "Page": page,
            "RuleId": rule_id,
            "MetricName": metric_name,
            "Ascending": ascending}
        return self._handle_request(api_request).result

    def describe_alerting_metric_rule_resources(self, group_id=None, rule_id=None):
        api_request = APIRequest('DescribeAlertingMetricRuleResources',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {"GroupId": group_id, "RuleId": rule_id}
        return self._handle_request(api_request).result

    def disable_active_metric_rule(self, product=None):
        api_request = APIRequest('DisableActiveMetricRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Product": product}
        return self._handle_request(api_request).result

    def describe_active_metric_rule_list(self, product=None):
        api_request = APIRequest('DescribeActiveMetricRuleList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Product": product}
        return self._handle_request(api_request).result

    def describe_products_of_active_metric_rule(self,):
        api_request = APIRequest('DescribeProductsOfActiveMetricRule', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def enable_active_metric_rule(self, product=None):
        api_request = APIRequest('EnableActiveMetricRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Product": product}
        return self._handle_request(api_request).result

    def describe_monitor_group_instance_attribute(
            self,
            total=None,
            instance_ids=None,
            group_id=None,
            page_size=None,
            category=None,
            keyword=None,
            page_number=None):
        api_request = APIRequest('DescribeMonitorGroupInstanceAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Total": total,
            "InstanceIds": instance_ids,
            "GroupId": group_id,
            "PageSize": page_size,
            "Category": category,
            "Keyword": keyword,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_monitor_group_notify_policy_list(
            self,
            policy_type=None,
            group_id=None,
            page_size=None,
            page_number=None):
        api_request = APIRequest('DescribeMonitorGroupNotifyPolicyList',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PolicyType": policy_type,
            "GroupId": group_id,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_monitor_group(self, group_id=None):
        api_request = APIRequest('DeleteMonitorGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"GroupId": group_id}
        return self._handle_request(api_request).result

    def create_monitor_group(
            self,
            contact_groups=None,
            options=None,
            type_=None,
            service_id=None,
            group_name=None,
            bind_url=None):
        api_request = APIRequest('CreateMonitorGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContactGroups": contact_groups,
            "Options": options,
            "Type": type_,
            "ServiceId": service_id,
            "GroupName": group_name,
            "BindUrl": bind_url}
        return self._handle_request(api_request).result

    def describe_monitor_groups(
            self,
            select_contact_groups=None,
            instance_id=None,
            page_size=None,
            keyword=None,
            group_name=None,
            page_number=None):
        api_request = APIRequest('DescribeMonitorGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SelectContactGroups": select_contact_groups,
            "InstanceId": instance_id,
            "PageSize": page_size,
            "Keyword": keyword,
            "GroupName": group_name,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_monitor_group_notify_policy(self, policy_type=None, group_id=None):
        api_request = APIRequest('DeleteMonitorGroupNotifyPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PolicyType": policy_type, "GroupId": group_id}
        return self._handle_request(api_request).result

    def describe_monitor_group_dynamic_rules(self, group_id=None):
        api_request = APIRequest('DescribeMonitorGroupDynamicRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"GroupId": group_id}
        return self._handle_request(api_request).result

    def create_monitor_group_instances(self, list_of_instances=None, group_id=None):
        api_request = APIRequest('CreateMonitorGroupInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Instances": list_of_instances, "GroupId": group_id}
        repeat_info = {"Instances": ('Instances',
                                     'list',
                                     'dict',
                                     [('InstanceId',
                                       'str',
                                       None,
                                       None),
                                      ('InstanceName',
                                       'str',
                                       None,
                                       None),
                                         ('RegionId',
                                          'str',
                                          None,
                                          None),
                                         ('Category',
                                          'str',
                                          None,
                                          None),
                                      ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_monitor_group_notify_policy(
            self,
            policy_type=None,
            group_id=None,
            end_time=None,
            start_time=None):
        api_request = APIRequest('CreateMonitorGroupNotifyPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PolicyType": policy_type,
            "GroupId": group_id,
            "EndTime": end_time,
            "StartTime": start_time}
        return self._handle_request(api_request).result

    def delete_monitor_group_instances(self, instance_id_list=None, group_id=None, category=None):
        api_request = APIRequest('DeleteMonitorGroupInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceIdList": instance_id_list,
            "GroupId": group_id,
            "Category": category}
        return self._handle_request(api_request).result

    def delete_monitor_group_dynamic_rule(self, group_id=None, category=None):
        api_request = APIRequest('DeleteMonitorGroupDynamicRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"GroupId": group_id, "Category": category}
        return self._handle_request(api_request).result

    def put_monitor_group_dynamic_rule(self, list_of_group_rules=None, group_id=None):
        api_request = APIRequest('PutMonitorGroupDynamicRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"GroupRules": list_of_group_rules, "GroupId": group_id}
        repeat_info = {"GroupRules": ('GroupRules', 'list', 'dict', [('FilterRelation', 'str', None, None),
                                                                     ('Filters', 'list', 'dict', [('Function', 'str', None, None),
                                                                                                  ('Name', 'str', None, None),
                                                                                                  ('Value', 'str', None, None),
                                                                                                  ],),('Category', 'str', None, None),
                                                                     ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_monitor_group_instances(
            self,
            instance_ids=None,
            group_id=None,
            page_size=None,
            category=None,
            keyword=None,
            page_number=None):
        api_request = APIRequest('DescribeMonitorGroupInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceIds": instance_ids,
            "GroupId": group_id,
            "PageSize": page_size,
            "Category": category,
            "Keyword": keyword,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_monitor_group_categories(self, group_id=None):
        api_request = APIRequest('DescribeMonitorGroupCategories', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"GroupId": group_id}
        return self._handle_request(api_request).result

    def modify_monitor_group(
            self,
            contact_groups=None,
            group_id=None,
            service_id=None,
            group_name=None,
            bind_urls=None):
        api_request = APIRequest('ModifyMonitorGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContactGroups": contact_groups,
            "GroupId": group_id,
            "ServiceId": service_id,
            "GroupName": group_name,
            "BindUrls": bind_urls}
        return self._handle_request(api_request).result

    def describe_metric_rule_list(
            self,
            enable_state=None,
            rule_ids=None,
            group_id=None,
            namespace=None,
            page_size=None,
            alert_state=None,
            rule_name=None,
            page=None,
            metric_name=None,
            dimensions=None):
        api_request = APIRequest('DescribeMetricRuleList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EnableState": enable_state,
            "RuleIds": rule_ids,
            "GroupId": group_id,
            "Namespace": namespace,
            "PageSize": page_size,
            "AlertState": alert_state,
            "RuleName": rule_name,
            "Page": page,
            "MetricName": metric_name,
            "Dimensions": dimensions}
        return self._handle_request(api_request).result

    def put_resource_metric_rule(
            self,
            webhook=None,
            escalations_warn_comparison_operator=None,
            rule_name=None,
            escalations_info_statistics=None,
            effective_interval=None,
            escalations_info_comparison_operator=None,
            no_effective_interval=None,
            email_subject=None,
            silence_time=None,
            metric_name=None,
            escalations_warn_times=None,
            period=None,
            escalations_warn_threshold=None,
            contact_groups=None,
            escalations_critical_statistics=None,
            resources=None,
            escalations_info_times=None,
            escalations_critical_times=None,
            escalations_warn_statistics=None,
            escalations_info_threshold=None,
            namespace=None,
            interval=None,
            rule_id=None,
            escalations_critical_comparison_operator=None,
            escalations_critical_threshold=None):
        api_request = APIRequest('PutResourceMetricRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Webhook": webhook,
            "Escalations.Warn.ComparisonOperator": escalations_warn_comparison_operator,
            "RuleName": rule_name,
            "Escalations.Info.Statistics": escalations_info_statistics,
            "EffectiveInterval": effective_interval,
            "Escalations.Info.ComparisonOperator": escalations_info_comparison_operator,
            "NoEffectiveInterval": no_effective_interval,
            "EmailSubject": email_subject,
            "SilenceTime": silence_time,
            "MetricName": metric_name,
            "Escalations.Warn.Times": escalations_warn_times,
            "Period": period,
            "Escalations.Warn.Threshold": escalations_warn_threshold,
            "ContactGroups": contact_groups,
            "Escalations.Critical.Statistics": escalations_critical_statistics,
            "Resources": resources,
            "Escalations.Info.Times": escalations_info_times,
            "Escalations.Critical.Times": escalations_critical_times,
            "Escalations.Warn.Statistics": escalations_warn_statistics,
            "Escalations.Info.Threshold": escalations_info_threshold,
            "Namespace": namespace,
            "Interval": interval,
            "RuleId": rule_id,
            "Escalations.Critical.ComparisonOperator": escalations_critical_comparison_operator,
            "Escalations.Critical.Threshold": escalations_critical_threshold}
        return self._handle_request(api_request).result

    def put_group_metric_rule(
            self,
            webhook=None,
            escalations_warn_comparison_operator=None,
            rule_name=None,
            escalations_info_statistics=None,
            effective_interval=None,
            escalations_info_comparison_operator=None,
            no_effective_interval=None,
            email_subject=None,
            silence_time=None,
            metric_name=None,
            escalations_warn_times=None,
            period=None,
            escalations_warn_threshold=None,
            escalations_critical_statistics=None,
            group_id=None,
            escalations_info_times=None,
            escalations_critical_times=None,
            escalations_warn_statistics=None,
            escalations_info_threshold=None,
            namespace=None,
            interval=None,
            rule_id=None,
            category=None,
            escalations_critical_comparison_operator=None,
            escalations_critical_threshold=None,
            dimensions=None):
        api_request = APIRequest('PutGroupMetricRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Webhook": webhook,
            "Escalations.Warn.ComparisonOperator": escalations_warn_comparison_operator,
            "RuleName": rule_name,
            "Escalations.Info.Statistics": escalations_info_statistics,
            "EffectiveInterval": effective_interval,
            "Escalations.Info.ComparisonOperator": escalations_info_comparison_operator,
            "NoEffectiveInterval": no_effective_interval,
            "EmailSubject": email_subject,
            "SilenceTime": silence_time,
            "MetricName": metric_name,
            "Escalations.Warn.Times": escalations_warn_times,
            "Period": period,
            "Escalations.Warn.Threshold": escalations_warn_threshold,
            "Escalations.Critical.Statistics": escalations_critical_statistics,
            "GroupId": group_id,
            "Escalations.Info.Times": escalations_info_times,
            "Escalations.Critical.Times": escalations_critical_times,
            "Escalations.Warn.Statistics": escalations_warn_statistics,
            "Escalations.Info.Threshold": escalations_info_threshold,
            "Namespace": namespace,
            "Interval": interval,
            "RuleId": rule_id,
            "Category": category,
            "Escalations.Critical.ComparisonOperator": escalations_critical_comparison_operator,
            "Escalations.Critical.Threshold": escalations_critical_threshold,
            "Dimensions": dimensions}
        return self._handle_request(api_request).result

    def enable_metric_rules(self, list_of_rule_id=None):
        api_request = APIRequest('EnableMetricRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RuleId": list_of_rule_id}
        repeat_info = {"RuleId": ('RuleId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_metric_rule_count(self, namespace=None, metric_name=None):
        api_request = APIRequest('DescribeMetricRuleCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Namespace": namespace, "MetricName": metric_name}
        return self._handle_request(api_request).result

    def create_group_metric_rules(self, group_id=None, list_of_group_metric_rules=None):
        api_request = APIRequest('CreateGroupMetricRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"GroupId": group_id, "GroupMetricRules": list_of_group_metric_rules}
        repeat_info = {"GroupMetricRules": ('GroupMetricRules', 'list', 'dict', [('Webhook', 'str', None, None),
                                                                                 ('Escalations.Warn.ComparisonOperator', 'str', None, None),
                                                                                 ('RuleName', 'str', None, None),
                                                                                 ('Escalations.Info.Statistics', 'str', None, None),
                                                                                 ('EffectiveInterval', 'str', None, None),
                                                                                 ('Escalations.Info.ComparisonOperator', 'str', None, None),
                                                                                 ('NoEffectiveInterval', 'str', None, None),
                                                                                 ('EmailSubject', 'str', None, None),
                                                                                 ('SilenceTime', 'str', None, None),
                                                                                 ('MetricName', 'str', None, None),
                                                                                 ('Escalations.Warn.Times', 'str', None, None),
                                                                                 ('Period', 'str', None, None),
                                                                                 ('Escalations.Warn.Threshold', 'str', None, None),
                                                                                 ('Escalations.Critical.Statistics', 'str', None, None),
                                                                                 ('Escalations.Info.Times', 'str', None, None),
                                                                                 ('Escalations.Critical.Times', 'str', None, None),
                                                                                 ('Escalations.Warn.Statistics', 'str', None, None),
                                                                                 ('Escalations.Info.Threshold', 'str', None, None),
                                                                                 ('Namespace', 'str', None, None),
                                                                                 ('Interval', 'str', None, None),
                                                                                 ('Category', 'str', None, None),
                                                                                 ('RuleId', 'str', None, None),
                                                                                 ('Escalations.Critical.ComparisonOperator', 'str', None, None),
                                                                                 ('Escalations.Critical.Threshold', 'str', None, None),
                                                                                 ('Dimensions', 'str', None, None),
                                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def disable_metric_rules(self, list_of_rule_id=None):
        api_request = APIRequest('DisableMetricRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RuleId": list_of_rule_id}
        repeat_info = {"RuleId": ('RuleId', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_metric_rules(self, list_of_id_=None):
        api_request = APIRequest('DeleteMetricRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": list_of_id_}
        repeat_info = {"Id": ('Id', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_metric_rule_template(
            self,
            name=None,
            rest_version=None,
            description=None,
            list_of_alert_templates=None,
            template_id=None):
        api_request = APIRequest('ModifyMetricRuleTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Name": name,
            "RestVersion": rest_version,
            "Description": description,
            "AlertTemplates": list_of_alert_templates,
            "TemplateId": template_id}
        repeat_info = {"AlertTemplates": ('AlertTemplates', 'list', 'dict', [('Period', 'str', None, None),
                                                                             ('Escalations.Warn.Threshold', 'str', None, None),
                                                                             ('Escalations.Warn.ComparisonOperator', 'str', None, None),
                                                                             ('Escalations.Critical.Statistics', 'str', None, None),
                                                                             ('Escalations.Info.Times', 'str', None, None),
                                                                             ('RuleName', 'str', None, None),
                                                                             ('Escalations.Info.Statistics', 'str', None, None),
                                                                             ('Escalations.Critical.Times', 'str', None, None),
                                                                             ('Escalations.Info.ComparisonOperator', 'str', None, None),
                                                                             ('Escalations.Warn.Statistics', 'str', None, None),
                                                                             ('Escalations.Info.Threshold', 'str', None, None),
                                                                             ('Namespace', 'str', None, None),
                                                                             ('Selector', 'str', None, None),
                                                                             ('MetricName', 'str', None, None),
                                                                             ('Category', 'str', None, None),
                                                                             ('Escalations.Critical.ComparisonOperator', 'str', None, None),
                                                                             ('Escalations.Warn.Times', 'str', None, None),
                                                                             ('Escalations.Critical.Threshold', 'str', None, None),
                                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def apply_metric_rule_template(
            self,
            enable_start_time=None,
            apply_mode=None,
            webhook=None,
            template_ids=None,
            enable_end_time=None,
            group_id=None,
            notify_level=None,
            silence_time=None):
        api_request = APIRequest('ApplyMetricRuleTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EnableStartTime": enable_start_time,
            "ApplyMode": apply_mode,
            "Webhook": webhook,
            "TemplateIds": template_ids,
            "EnableEndTime": enable_end_time,
            "GroupId": group_id,
            "NotifyLevel": notify_level,
            "SilenceTime": silence_time}
        return self._handle_request(api_request).result

    def describe_metric_rule_template_attribute(self, name=None, template_id=None):
        api_request = APIRequest('DescribeMetricRuleTemplateAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name, "TemplateId": template_id}
        return self._handle_request(api_request).result

    def create_metric_rule_template(
            self,
            name=None,
            description=None,
            list_of_alert_templates=None):
        api_request = APIRequest('CreateMetricRuleTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Name": name,
            "Description": description,
            "AlertTemplates": list_of_alert_templates}
        repeat_info = {"AlertTemplates": ('AlertTemplates', 'list', 'dict', [('Period', 'str', None, None),
                                                                             ('Escalations.Warn.Threshold', 'str', None, None),
                                                                             ('Escalations.Warn.ComparisonOperator', 'str', None, None),
                                                                             ('Escalations.Critical.Statistics', 'str', None, None),
                                                                             ('Escalations.Info.Times', 'str', None, None),
                                                                             ('RuleName', 'str', None, None),
                                                                             ('Escalations.Info.Statistics', 'str', None, None),
                                                                             ('Escalations.Critical.Times', 'str', None, None),
                                                                             ('Escalations.Info.ComparisonOperator', 'str', None, None),
                                                                             ('Escalations.Warn.Statistics', 'str', None, None),
                                                                             ('Escalations.Info.Threshold', 'str', None, None),
                                                                             ('Namespace', 'str', None, None),
                                                                             ('Selector', 'str', None, None),
                                                                             ('MetricName', 'str', None, None),
                                                                             ('Category', 'str', None, None),
                                                                             ('Escalations.Critical.ComparisonOperator', 'str', None, None),
                                                                             ('Escalations.Warn.Times', 'str', None, None),
                                                                             ('Escalations.Critical.Threshold', 'str', None, None),
                                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_metric_rule_template(self, template_id=None):
        api_request = APIRequest('DeleteMetricRuleTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TemplateId": template_id}
        return self._handle_request(api_request).result

    def describe_metric_rule_template_list(
            self,
            name=None,
            page_size=None,
            history=None,
            keyword=None,
            template_id=None,
            page_number=None):
        api_request = APIRequest('DescribeMetricRuleTemplateList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Name": name,
            "PageSize": page_size,
            "History": history,
            "Keyword": keyword,
            "TemplateId": template_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def put_custom_event(self, list_of_event_info=None):
        api_request = APIRequest('PutCustomEvent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"EventInfo": list_of_event_info}
        repeat_info = {"EventInfo": ('EventInfo', 'list', 'dict', [('GroupId', 'str', None, None),
                                                                   ('Time', 'str', None, None),
                                                                   ('EventName', 'str', None, None),
                                                                   ('Content', 'str', None, None),
                                                                   ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_custom_event_count(
            self,
            event_id=None,
            level=None,
            group_id=None,
            name=None,
            end_time=None,
            start_time=None,
            search_keywords=None):
        api_request = APIRequest('DescribeCustomEventCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EventId": event_id,
            "Level": level,
            "GroupId": group_id,
            "Name": name,
            "EndTime": end_time,
            "StartTime": start_time,
            "SearchKeywords": search_keywords}
        return self._handle_request(api_request).result

    def describe_custom_event_attribute(
            self,
            event_id=None,
            level=None,
            group_id=None,
            name=None,
            page_size=None,
            end_time=None,
            start_time=None,
            search_keywords=None,
            page_number=None):
        api_request = APIRequest('DescribeCustomEventAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EventId": event_id,
            "Level": level,
            "GroupId": group_id,
            "Name": name,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "SearchKeywords": search_keywords,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_custom_event_histogram(
            self,
            event_id=None,
            level=None,
            group_id=None,
            name=None,
            end_time=None,
            start_time=None,
            search_keywords=None):
        api_request = APIRequest('DescribeCustomEventHistogram', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EventId": event_id,
            "Level": level,
            "GroupId": group_id,
            "Name": name,
            "EndTime": end_time,
            "StartTime": start_time,
            "SearchKeywords": search_keywords}
        return self._handle_request(api_request).result

    def delete_custom_metric(self, group_id=None, metric_name=None, uuid=None, md5=None):
        api_request = APIRequest('DeleteCustomMetric', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GroupId": group_id,
            "MetricName": metric_name,
            "UUID": uuid,
            "Md5": md5}
        return self._handle_request(api_request).result

    def describe_custom_metric_list(
            self,
            group_id=None,
            page_size=None,
            metric_name=None,
            dimension=None,
            page_number=None,
            md5=None):
        api_request = APIRequest('DescribeCustomMetricList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GroupId": group_id,
            "PageSize": page_size,
            "MetricName": metric_name,
            "Dimension": dimension,
            "PageNumber": page_number,
            "Md5": md5}
        return self._handle_request(api_request).result

    def put_custom_metric(self, list_of_metric_list=None):
        api_request = APIRequest('PutCustomMetric', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"MetricList": list_of_metric_list}
        repeat_info = {"MetricList": ('MetricList',
                                      'list',
                                      'dict',
                                      [('Period',
                                        'str',
                                        None,
                                        None),
                                       ('GroupId',
                                        'str',
                                        None,
                                        None),
                                          ('Values',
                                           'str',
                                           None,
                                           None),
                                          ('Time',
                                           'str',
                                           None,
                                           None),
                                          ('MetricName',
                                           'str',
                                           None,
                                           None),
                                          ('Type',
                                           'str',
                                           None,
                                           None),
                                          ('Dimensions',
                                           'str',
                                           None,
                                           None),
                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_event_rule_attribute(self, rule_name=None):
        api_request = APIRequest('DescribeEventRuleAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RuleName": rule_name}
        return self._handle_request(api_request).result

    def delete_contact_group(self, contact_group_name=None):
        api_request = APIRequest('DeleteContactGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ContactGroupName": contact_group_name}
        return self._handle_request(api_request).result

    def describe_contact_list(self, contact_name=None, page_size=None, page_number=None):
        api_request = APIRequest('DescribeContactList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContactName": contact_name,
            "PageSize": page_size,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_contact_list_by_contact_group(self, contact_group_name=None):
        api_request = APIRequest('DescribeContactListByContactGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ContactGroupName": contact_group_name}
        return self._handle_request(api_request).result

    def delete_contact(self, contact_name=None):
        api_request = APIRequest('DeleteContact', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ContactName": contact_name}
        return self._handle_request(api_request).result

    def put_contact_group(self, describe=None, contact_group_name=None, list_of_contact_names=None):
        api_request = APIRequest('PutContactGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Describe": describe,
            "ContactGroupName": contact_group_name,
            "ContactNames": list_of_contact_names}
        repeat_info = {"ContactNames": ('ContactNames', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def put_contact(
            self,
            contact_name=None,
            channels_mail=None,
            channels_ali_im=None,
            channels_ding_web_hook=None,
            describe=None,
            channels_sms=None):
        api_request = APIRequest('PutContact', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContactName": contact_name,
            "Channels.Mail": channels_mail,
            "Channels.AliIM": channels_ali_im,
            "Channels.DingWebHook": channels_ding_web_hook,
            "Describe": describe,
            "Channels.SMS": channels_sms}
        return self._handle_request(api_request).result

    def describe_contact_group_list(self, page_size=None, page_number=None):
        api_request = APIRequest('DescribeContactGroupList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "PageNumber": page_number}
        return self._handle_request(api_request).result

    def put_event_rule_targets(
            self,
            list_of_webhook_parameters=None,
            list_of_contact_parameters=None,
            list_of_sls_parameters=None,
            list_of_fc_parameters=None,
            rule_name=None,
            list_of_mns_parameters=None):
        api_request = APIRequest('PutEventRuleTargets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "WebhookParameters": list_of_webhook_parameters,
            "ContactParameters": list_of_contact_parameters,
            "SlsParameters": list_of_sls_parameters,
            "FcParameters": list_of_fc_parameters,
            "RuleName": rule_name,
            "MnsParameters": list_of_mns_parameters}
        repeat_info = {"WebhookParameters": ('WebhookParameters', 'list', 'dict', [('Protocol', 'str', None, None),
                                                                                   ('Method', 'str', None, None),
                                                                                   ('Id', 'str', None, None),
                                                                                   ('Url', 'str', None, None),
                                                                                   ]),
                       "ContactParameters": ('ContactParameters', 'list', 'dict', [('Level', 'str', None, None),
                                                                                   ('Id', 'str', None, None),
                                                                                   ('ContactGroupName', 'str', None, None),
                                                                                   ]),
                       "SlsParameters": ('SlsParameters', 'list', 'dict', [('Project', 'str', None, None),
                                                                           ('Id', 'str', None, None),
                                                                           ('Region', 'str', None, None),
                                                                           ('LogStore', 'str', None, None),
                                                                           ]),
                       "FcParameters": ('FcParameters', 'list', 'dict', [('FunctionName', 'str', None, None),
                                                                         ('ServiceName', 'str', None, None),
                                                                         ('Id', 'str', None, None),
                                                                         ('Region', 'str', None, None),
                                                                         ]),
                       "MnsParameters": ('MnsParameters', 'list', 'dict', [('Id', 'str', None, None),
                                                                           ('Region', 'str', None, None),
                                                                           ('Queue', 'str', None, None),
                                                                           ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_event_rule_targets(self, list_of_ids=None, rule_name=None):
        api_request = APIRequest('DeleteEventRuleTargets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Ids": list_of_ids, "RuleName": rule_name}
        repeat_info = {"Ids": ('Ids', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def disable_event_rules(self, list_of_rule_names=None):
        api_request = APIRequest('DisableEventRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RuleNames": list_of_rule_names}
        repeat_info = {"RuleNames": ('RuleNames', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_event_rule_target_list(self, rule_name=None):
        api_request = APIRequest('DescribeEventRuleTargetList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RuleName": rule_name}
        return self._handle_request(api_request).result

    def delete_event_rules(self, list_of_rule_names=None):
        api_request = APIRequest('DeleteEventRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RuleNames": list_of_rule_names}
        repeat_info = {"RuleNames": ('RuleNames', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def enable_event_rules(self, list_of_rule_names=None):
        api_request = APIRequest('EnableEventRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"RuleNames": list_of_rule_names}
        repeat_info = {"RuleNames": ('RuleNames', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def put_event_rule(
            self,
            list_of_event_pattern=None,
            group_id=None,
            description=None,
            rule_name=None,
            event_type=None,
            state=None):
        api_request = APIRequest('PutEventRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EventPattern": list_of_event_pattern,
            "GroupId": group_id,
            "Description": description,
            "RuleName": rule_name,
            "EventType": event_type,
            "State": state}
        repeat_info = {"EventPattern": ('EventPattern',
                                        'list',
                                        'dict',
                                        [('LevelList',
                                          'list',
                                          'str',
                                          None),
                                         ('Product',
                                          'str',
                                          None,
                                          None),
                                            ('StatusList',
                                             'list',
                                             'str',
                                             None),
                                            ('NameList',
                                             'list',
                                             'str',
                                             None),
                                            ('EventTypeList',
                                             'list',
                                             'str',
                                             None),
                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_event_rule_list(
            self,
            group_id=None,
            page_size=None,
            name_prefix=None,
            page_number=None):
        api_request = APIRequest('DescribeEventRuleList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GroupId": group_id,
            "PageSize": page_size,
            "NamePrefix": name_prefix,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_system_event_attribute(
            self,
            product=None,
            level=None,
            group_id=None,
            name=None,
            page_size=None,
            end_time=None,
            event_type=None,
            start_time=None,
            search_keywords=None,
            page_number=None,
            status=None):
        api_request = APIRequest('DescribeSystemEventAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Product": product,
            "Level": level,
            "GroupId": group_id,
            "Name": name,
            "PageSize": page_size,
            "EndTime": end_time,
            "EventType": event_type,
            "StartTime": start_time,
            "SearchKeywords": search_keywords,
            "PageNumber": page_number,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_system_event_histogram(
            self,
            product=None,
            level=None,
            group_id=None,
            name=None,
            page_size=None,
            end_time=None,
            event_type=None,
            start_time=None,
            search_keywords=None,
            page_number=None,
            status=None):
        api_request = APIRequest('DescribeSystemEventHistogram', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Product": product,
            "Level": level,
            "GroupId": group_id,
            "Name": name,
            "PageSize": page_size,
            "EndTime": end_time,
            "EventType": event_type,
            "StartTime": start_time,
            "SearchKeywords": search_keywords,
            "PageNumber": page_number,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_system_event_count(
            self,
            product=None,
            level=None,
            group_id=None,
            name=None,
            end_time=None,
            event_type=None,
            start_time=None,
            search_keywords=None,
            status=None):
        api_request = APIRequest('DescribeSystemEventCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Product": product,
            "Level": level,
            "GroupId": group_id,
            "Name": name,
            "EndTime": end_time,
            "EventType": event_type,
            "StartTime": start_time,
            "SearchKeywords": search_keywords,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_system_event_meta_list(self,):
        api_request = APIRequest('DescribeSystemEventMetaList', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def describe_monitoring_agent_processes(self, instance_id=None):
        api_request = APIRequest('DescribeMonitoringAgentProcesses', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def uninstall_monitoring_agent(self, instance_id=None):
        api_request = APIRequest('UninstallMonitoringAgent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def describe_monitoring_agent_access_key(self,):
        api_request = APIRequest('DescribeMonitoringAgentAccessKey', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def install_monitoring_agent(self, list_of_instance_ids=None, force=None):
        api_request = APIRequest('InstallMonitoringAgent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceIds": list_of_instance_ids, "Force": force}
        repeat_info = {"InstanceIds": ('InstanceIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def send_dry_run_system_event(
            self,
            product=None,
            group_id=None,
            event_name=None,
            event_content=None):
        api_request = APIRequest('SendDryRunSystemEvent', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Product": product,
            "GroupId": group_id,
            "EventName": event_name,
            "EventContent": event_content}
        return self._handle_request(api_request).result

    def create_monitoring_agent_process(
            self,
            instance_id=None,
            process_name=None,
            process_user=None):
        api_request = APIRequest('CreateMonitoringAgentProcess', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "ProcessName": process_name,
            "ProcessUser": process_user}
        return self._handle_request(api_request).result

    def describe_monitoring_agent_config(self,):
        api_request = APIRequest('DescribeMonitoringAgentConfig', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def delete_monitoring_agent_process(self, instance_id=None, process_id=None, process_name=None):
        api_request = APIRequest('DeleteMonitoringAgentProcess', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "ProcessId": process_id,
            "ProcessName": process_name}
        return self._handle_request(api_request).result

    def describe_monitoring_agent_hosts(
            self,
            host_name=None,
            instance_ids=None,
            instance_region_id=None,
            page_size=None,
            key_word=None,
            serial_numbers=None,
            page_number=None):
        api_request = APIRequest('DescribeMonitoringAgentHosts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HostName": host_name,
            "InstanceIds": instance_ids,
            "InstanceRegionId": instance_region_id,
            "PageSize": page_size,
            "KeyWord": key_word,
            "SerialNumbers": serial_numbers,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_site_monitor_data(
            self,
            period=None,
            next_token=None,
            length=None,
            end_time=None,
            start_time=None,
            type_=None,
            metric_name=None,
            task_id=None):
        api_request = APIRequest('DescribeSiteMonitorData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "NextToken": next_token,
            "Length": length,
            "EndTime": end_time,
            "StartTime": start_time,
            "Type": type_,
            "MetricName": metric_name,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def modify_site_monitor(
            self,
            options_json=None,
            address=None,
            alert_ids=None,
            task_name=None,
            interval=None,
            task_id=None,
            isp_cities=None):
        api_request = APIRequest('ModifySiteMonitor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OptionsJson": options_json,
            "Address": address,
            "AlertIds": alert_ids,
            "TaskName": task_name,
            "Interval": interval,
            "TaskId": task_id,
            "IspCities": isp_cities}
        return self._handle_request(api_request).result

    def describe_site_monitor_isp_city_list(self, city=None, isp=None):
        api_request = APIRequest('DescribeSiteMonitorISPCityList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"City": city, "Isp": isp}
        return self._handle_request(api_request).result

    def describe_site_monitor_quota(self,):
        api_request = APIRequest('DescribeSiteMonitorQuota', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def describe_site_monitor_statistics(
            self,
            time_range=None,
            start_time=None,
            metric_name=None,
            task_id=None):
        api_request = APIRequest('DescribeSiteMonitorStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TimeRange": time_range,
            "StartTime": start_time,
            "MetricName": metric_name,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def enable_site_monitors(self, task_ids=None):
        api_request = APIRequest('EnableSiteMonitors', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TaskIds": task_ids}
        return self._handle_request(api_request).result

    def describe_site_monitor_attribute(self, include_alert=None, task_id=None):
        api_request = APIRequest('DescribeSiteMonitorAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"IncludeAlert": include_alert, "TaskId": task_id}
        return self._handle_request(api_request).result

    def describe_site_monitor_list(
            self,
            task_type=None,
            page_size=None,
            page=None,
            keyword=None,
            task_id=None):
        api_request = APIRequest('DescribeSiteMonitorList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TaskType": task_type,
            "PageSize": page_size,
            "Page": page,
            "Keyword": keyword,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def delete_site_monitors(self, is_delete_alarms=None, task_ids=None):
        api_request = APIRequest('DeleteSiteMonitors', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"IsDeleteAlarms": is_delete_alarms, "TaskIds": task_ids}
        return self._handle_request(api_request).result

    def disable_site_monitors(self, task_ids=None):
        api_request = APIRequest('DisableSiteMonitors', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"TaskIds": task_ids}
        return self._handle_request(api_request).result

    def create_site_monitor(
            self,
            options_json=None,
            address=None,
            task_type=None,
            alert_ids=None,
            task_name=None,
            interval=None,
            isp_cities=None):
        api_request = APIRequest('CreateSiteMonitor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "OptionsJson": options_json,
            "Address": address,
            "TaskType": task_type,
            "AlertIds": alert_ids,
            "TaskName": task_name,
            "Interval": interval,
            "IspCities": isp_cities}
        return self._handle_request(api_request).result

    def describe_project_meta(self, page_size=None, page_number=None, labels=None):
        api_request = APIRequest('DescribeProjectMeta', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "PageNumber": page_number, "Labels": labels}
        return self._handle_request(api_request).result

    def describe_metric_list(
            self,
            period=None,
            next_token=None,
            namespace=None,
            length=None,
            end_time=None,
            express=None,
            start_time=None,
            metric_name=None,
            dimensions=None):
        api_request = APIRequest('DescribeMetricList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "NextToken": next_token,
            "Namespace": namespace,
            "Length": length,
            "EndTime": end_time,
            "Express": express,
            "StartTime": start_time,
            "MetricName": metric_name,
            "Dimensions": dimensions}
        return self._handle_request(api_request).result

    def describe_metric_meta_list(
            self,
            namespace=None,
            page_size=None,
            metric_name=None,
            page_number=None,
            labels=None):
        api_request = APIRequest('DescribeMetricMetaList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Namespace": namespace,
            "PageSize": page_size,
            "MetricName": metric_name,
            "PageNumber": page_number,
            "Labels": labels}
        return self._handle_request(api_request).result

    def describe_metric_top(
            self,
            period=None,
            namespace=None,
            length=None,
            end_time=None,
            orderby=None,
            express=None,
            start_time=None,
            metric_name=None,
            dimensions=None,
            order_desc=None):
        api_request = APIRequest('DescribeMetricTop', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "Namespace": namespace,
            "Length": length,
            "EndTime": end_time,
            "Orderby": orderby,
            "Express": express,
            "StartTime": start_time,
            "MetricName": metric_name,
            "Dimensions": dimensions,
            "OrderDesc": order_desc}
        return self._handle_request(api_request).result

    def describe_metric_data(
            self,
            period=None,
            namespace=None,
            length=None,
            end_time=None,
            express=None,
            start_time=None,
            metric_name=None,
            dimensions=None):
        api_request = APIRequest('DescribeMetricData', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "Namespace": namespace,
            "Length": length,
            "EndTime": end_time,
            "Express": express,
            "StartTime": start_time,
            "MetricName": metric_name,
            "Dimensions": dimensions}
        return self._handle_request(api_request).result

    def describe_metric_last(
            self,
            period=None,
            next_token=None,
            namespace=None,
            length=None,
            end_time=None,
            express=None,
            start_time=None,
            metric_name=None,
            dimensions=None):
        api_request = APIRequest('DescribeMetricLast', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "NextToken": next_token,
            "Namespace": namespace,
            "Length": length,
            "EndTime": end_time,
            "Express": express,
            "StartTime": start_time,
            "MetricName": metric_name,
            "Dimensions": dimensions}
        return self._handle_request(api_request).result

    def enable_host_availability(self, list_of_id_=None):
        api_request = APIRequest('EnableHostAvailability', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": list_of_id_}
        repeat_info = {"Id": ('Id', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_host_availability(
            self,
            list_of_instance_list=None,
            task_option_http_method=None,
            list_of_alert_config_escalation_list=None,
            group_id=None,
            task_name=None,
            alert_config_silence_time=None,
            task_option_http_response_charset=None,
            alert_config_end_time=None,
            task_option_http_uri=None,
            task_option_http_negative=None,
            task_scope=None,
            alert_config_notify_type=None,
            alert_config_start_time=None,
            task_option_telnet_or_ping_host=None,
            task_option_http_response_match_content=None,
            id_=None,
            alert_config_web_hook=None):
        api_request = APIRequest('ModifyHostAvailability', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceList": list_of_instance_list,
            "TaskOption.HttpMethod": task_option_http_method,
            "AlertConfigEscalationList": list_of_alert_config_escalation_list,
            "GroupId": group_id,
            "TaskName": task_name,
            "AlertConfig.SilenceTime": alert_config_silence_time,
            "TaskOption.HttpResponseCharset": task_option_http_response_charset,
            "AlertConfig.EndTime": alert_config_end_time,
            "TaskOption.HttpURI": task_option_http_uri,
            "TaskOption.HttpNegative": task_option_http_negative,
            "TaskScope": task_scope,
            "AlertConfig.NotifyType": alert_config_notify_type,
            "AlertConfig.StartTime": alert_config_start_time,
            "TaskOption.TelnetOrPingHost": task_option_telnet_or_ping_host,
            "TaskOption.HttpResponseMatchContent": task_option_http_response_match_content,
            "Id": id_,
            "AlertConfig.WebHook": alert_config_web_hook}
        repeat_info = {"InstanceList": ('InstanceList',
                                        'list',
                                        'str',
                                        None),
                       "AlertConfigEscalationList": ('AlertConfigEscalationList',
                                                     'list',
                                                     'dict',
                                                     [('Times',
                                                       'str',
                                                       None,
                                                       None),
                                                      ('MetricName',
                                                       'str',
                                                       None,
                                                       None),
                                                         ('Value',
                                                          'str',
                                                          None,
                                                          None),
                                                         ('Operator',
                                                          'str',
                                                          None,
                                                          None),
                                                         ('Aggregate',
                                                          'str',
                                                          None,
                                                          None),
                                                      ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def disable_host_availability(self, list_of_id_=None):
        api_request = APIRequest('DisableHostAvailability', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": list_of_id_}
        repeat_info = {"Id": ('Id', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_unhealthy_host_availability(self, list_of_id_=None):
        api_request = APIRequest('DescribeUnhealthyHostAvailability', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": list_of_id_}
        repeat_info = {"Id": ('Id', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_host_availability(
            self,
            list_of_instance_list=None,
            task_type=None,
            task_option_http_method=None,
            list_of_alert_config_escalation_list=None,
            group_id=None,
            task_name=None,
            alert_config_silence_time=None,
            task_option_http_response_charset=None,
            alert_config_end_time=None,
            task_option_http_uri=None,
            task_option_http_negative=None,
            task_scope=None,
            alert_config_notify_type=None,
            alert_config_start_time=None,
            task_option_telnet_or_ping_host=None,
            task_option_http_response_match_content=None,
            alert_config_web_hook=None):
        api_request = APIRequest('CreateHostAvailability', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceList": list_of_instance_list,
            "TaskType": task_type,
            "TaskOption.HttpMethod": task_option_http_method,
            "AlertConfigEscalationList": list_of_alert_config_escalation_list,
            "GroupId": group_id,
            "TaskName": task_name,
            "AlertConfig.SilenceTime": alert_config_silence_time,
            "TaskOption.HttpResponseCharset": task_option_http_response_charset,
            "AlertConfig.EndTime": alert_config_end_time,
            "TaskOption.HttpURI": task_option_http_uri,
            "TaskOption.HttpNegative": task_option_http_negative,
            "TaskScope": task_scope,
            "AlertConfig.NotifyType": alert_config_notify_type,
            "AlertConfig.StartTime": alert_config_start_time,
            "TaskOption.TelnetOrPingHost": task_option_telnet_or_ping_host,
            "TaskOption.HttpResponseMatchContent": task_option_http_response_match_content,
            "AlertConfig.WebHook": alert_config_web_hook}
        repeat_info = {"InstanceList": ('InstanceList',
                                        'list',
                                        'str',
                                        None),
                       "AlertConfigEscalationList": ('AlertConfigEscalationList',
                                                     'list',
                                                     'dict',
                                                     [('Times',
                                                       'str',
                                                       None,
                                                       None),
                                                      ('MetricName',
                                                       'str',
                                                       None,
                                                       None),
                                                         ('Value',
                                                          'str',
                                                          None,
                                                          None),
                                                         ('Operator',
                                                          'str',
                                                          None,
                                                          None),
                                                         ('Aggregate',
                                                          'str',
                                                          None,
                                                          None),
                                                      ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_host_availability_list(
            self,
            group_id=None,
            page_size=None,
            task_name=None,
            id_=None,
            page_number=None):
        api_request = APIRequest('DescribeHostAvailabilityList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "GroupId": group_id,
            "PageSize": page_size,
            "TaskName": task_name,
            "Id": id_,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_host_availability(self, list_of_id_=None):
        api_request = APIRequest('DeleteHostAvailability', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Id": list_of_id_}
        repeat_info = {"Id": ('Id', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_monitoring_config(self,):
        api_request = APIRequest('DescribeMonitoringConfig', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def put_monitoring_config(self, enable_install_agent_new_ecs=None, auto_install=None):
        api_request = APIRequest('PutMonitoringConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EnableInstallAgentNewECS": enable_install_agent_new_ecs,
            "AutoInstall": auto_install}
        return self._handle_request(api_request).result
