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


class YundundsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Yundun-ds'
        self.api_version = '2019-01-03'
        self.location_service_code = 'sddp'
        self.location_endpoint_type = 'openAPI'

    def validate_connector(
            self,
            password=None,
            source_ip=None,
            connector=None,
            lang=None,
            resource_type=None,
            service_region_id=None,
            parent_id=None,
            user_name=None):
        api_request = APIRequest('ValidateConnector', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Password": password,
            "SourceIp": source_ip,
            "Connector": connector,
            "Lang": lang,
            "ResourceType": resource_type,
            "ServiceRegionId": service_region_id,
            "ParentId": parent_id,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def modify_rule_status(
            self,
            source_ip=None,
            feature_type=None,
            id_=None,
            lang=None,
            status=None):
        api_request = APIRequest('ModifyRuleStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "Id": id_,
            "Lang": lang,
            "Status": status}
        return self._handle_request(api_request).result

    def modify_rule(
            self,
            source_ip=None,
            feature_type=None,
            name=None,
            id_=None,
            risk_level_id=None,
            lang=None,
            custom_type=None,
            category=None,
            content=None):
        api_request = APIRequest('ModifyRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "Name": name,
            "Id": id_,
            "RiskLevelId": risk_level_id,
            "Lang": lang,
            "CustomType": custom_type,
            "Category": category,
            "Content": content}
        return self._handle_request(api_request).result

    def modify_event_type_status(self, sub_type_ids=None, source_ip=None, lang=None):
        api_request = APIRequest('ModifyEventTypeStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SubTypeIds": sub_type_ids, "SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def modify_event_status(
            self,
            source_ip=None,
            backed=None,
            feature_type=None,
            deal_reason=None,
            id_=None,
            lang=None,
            status=None):
        api_request = APIRequest('ModifyEventStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Backed": backed,
            "FeatureType": feature_type,
            "DealReason": deal_reason,
            "Id": id_,
            "Lang": lang,
            "Status": status}
        return self._handle_request(api_request).result

    def modify_default_level(
            self,
            source_ip=None,
            feature_type=None,
            default_id=None,
            lang=None,
            sensitive_ids=None):
        api_request = APIRequest('ModifyDefaultLevel', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "DefaultId": default_id,
            "Lang": lang,
            "SensitiveIds": sensitive_ids}
        return self._handle_request(api_request).result

    def describe_user_status(self, source_ip=None, lang=None):
        api_request = APIRequest('DescribeUserStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_transfer_event_counts(self, source_ip=None, feature_type=None, lang=None):
        api_request = APIRequest('DescribeTransferEventCounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "FeatureType": feature_type, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_total_count(self, source_ip=None, feature_type=None, lang=None):
        api_request = APIRequest('DescribeTotalCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "FeatureType": feature_type, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_tables(
            self,
            product_id=None,
            feature_type=None,
            package_id=None,
            current_page=None,
            query_name=None,
            risk_level_id=None,
            instance_id=None,
            source_ip=None,
            name=None,
            page_size=None,
            lang=None,
            rule_id=None,
            query_type=None):
        api_request = APIRequest('DescribeTables', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductId": product_id,
            "FeatureType": feature_type,
            "PackageId": package_id,
            "CurrentPage": current_page,
            "QueryName": query_name,
            "RiskLevelId": risk_level_id,
            "InstanceId": instance_id,
            "SourceIp": source_ip,
            "Name": name,
            "PageSize": page_size,
            "Lang": lang,
            "RuleId": rule_id,
            "QueryType": query_type}
        return self._handle_request(api_request).result

    def describe_rule_total_count(self, source_ip=None, feature_type=None, lang=None):
        api_request = APIRequest('DescribeRuleTotalCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "FeatureType": feature_type, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_rules(
            self,
            source_ip=None,
            page_size=None,
            name=None,
            current_page=None,
            risk_level_id=None,
            lang=None,
            custom_type=None,
            category=None):
        api_request = APIRequest('DescribeRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "PageSize": page_size,
            "Name": name,
            "CurrentPage": current_page,
            "RiskLevelId": risk_level_id,
            "Lang": lang,
            "CustomType": custom_type,
            "Category": category}
        return self._handle_request(api_request).result

    def describe_privileges(
            self,
            account_id=None,
            use_account_id=None,
            data_type_ids=None,
            source_ip=None,
            feature_type=None,
            page_size=None,
            current_page=None,
            lang=None,
            key=None):
        api_request = APIRequest('DescribePrivileges', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccountId": account_id,
            "UseAccountId": use_account_id,
            "DataTypeIds": data_type_ids,
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang,
            "Key": key}
        return self._handle_request(api_request).result

    def describe_packages(
            self,
            instance_id=None,
            source_ip=None,
            product_id=None,
            feature_type=None,
            name=None,
            page_size=None,
            current_page=None,
            query_name=None,
            risk_level_id=None,
            lang=None,
            rule_id=None,
            query_type=None):
        api_request = APIRequest('DescribePackages', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SourceIp": source_ip,
            "ProductId": product_id,
            "FeatureType": feature_type,
            "Name": name,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "QueryName": query_name,
            "RiskLevelId": risk_level_id,
            "Lang": lang,
            "RuleId": rule_id,
            "QueryType": query_type}
        return self._handle_request(api_request).result

    def describe_oss_objects(
            self,
            instance_id=None,
            source_ip=None,
            feature_type=None,
            name=None,
            page_size=None,
            current_page=None,
            query_name=None,
            risk_level_id=None,
            lang=None,
            rule_id=None):
        api_request = APIRequest('DescribeOssObjects', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "Name": name,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "QueryName": query_name,
            "RiskLevelId": risk_level_id,
            "Lang": lang,
            "RuleId": rule_id}
        return self._handle_request(api_request).result

    def describe_oss_object_detail(self, source_ip=None, feature_type=None, id_=None, lang=None):
        api_request = APIRequest('DescribeOssObjectDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "Id": id_,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_instances(
            self,
            product_code=None,
            source_ip=None,
            product_id=None,
            feature_type=None,
            name=None,
            page_size=None,
            current_page=None,
            query_name=None,
            risk_level_id=None,
            lang=None,
            rule_id=None,
            query_type=None):
        api_request = APIRequest('DescribeInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "SourceIp": source_ip,
            "ProductId": product_id,
            "FeatureType": feature_type,
            "Name": name,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "QueryName": query_name,
            "RiskLevelId": risk_level_id,
            "Lang": lang,
            "RuleId": rule_id,
            "QueryType": query_type}
        return self._handle_request(api_request).result

    def describe_flow_total_count(
            self,
            product_code=None,
            source_ip=None,
            feature_type=None,
            depart_id=None,
            lang=None):
        api_request = APIRequest('DescribeFlowTotalCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "DepartId": depart_id,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_event_types(self, source_ip=None, parent_type_id=None, lang=None):
        api_request = APIRequest('DescribeEventTypes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "ParentTypeId": parent_type_id, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_event_total_count(
            self,
            type_code=None,
            source_ip=None,
            feature_type=None,
            count_type=None,
            lang=None):
        api_request = APIRequest('DescribeEventTotalCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TypeCode": type_code,
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "CountType": count_type,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_events(
            self,
            feature_type=None,
            end_time=None,
            current_page=None,
            start_time=None,
            user_id=None,
            type_code=None,
            sub_type_code=None,
            source_ip=None,
            page_size=None,
            depart_id=None,
            lang=None,
            deal_user_id=None,
            status=None):
        api_request = APIRequest('DescribeEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FeatureType": feature_type,
            "EndTime": end_time,
            "CurrentPage": current_page,
            "StartTime": start_time,
            "UserId": user_id,
            "TypeCode": type_code,
            "SubTypeCode": sub_type_code,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "DepartId": depart_id,
            "Lang": lang,
            "DealUserId": deal_user_id,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_event_detail(self, source_ip=None, feature_type=None, id_=None, lang=None):
        api_request = APIRequest('DescribeEventDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "Id": id_,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_event_counts(
            self,
            type_code=None,
            source_ip=None,
            feature_type=None,
            count_type=None,
            days=None,
            lang=None):
        api_request = APIRequest('DescribeEventCounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TypeCode": type_code,
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "CountType": count_type,
            "Days": days,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_depart_total_count(self, source_ip=None, feature_type=None, lang=None):
        api_request = APIRequest('DescribeDepartTotalCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "FeatureType": feature_type, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_departs(
            self,
            source_ip=None,
            feature_type=None,
            account_type=None,
            page_size=None,
            current_page=None,
            lang=None,
            key=None):
        api_request = APIRequest('DescribeDeparts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "AccountType": account_type,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang,
            "Key": key}
        return self._handle_request(api_request).result

    def describe_depart_counts(
            self,
            type_code=None,
            depart_name=None,
            source_ip=None,
            feature_type=None,
            page_size=None,
            current_page=None,
            lang=None):
        api_request = APIRequest('DescribeDepartCounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TypeCode": type_code,
            "DepartName": depart_name,
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_data_total_count(
            self,
            product_code=None,
            instance_id=None,
            source_ip=None,
            feature_type=None,
            count_type=None,
            lang=None):
        api_request = APIRequest('DescribeDataTotalCount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "InstanceId": instance_id,
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "CountType": count_type,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_data_hub_topics(
            self,
            source_ip=None,
            feature_type=None,
            page_size=None,
            depart_id=None,
            current_page=None,
            lang=None,
            project_id=None,
            key=None):
        api_request = APIRequest('DescribeDataHubTopics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "PageSize": page_size,
            "DepartId": depart_id,
            "CurrentPage": current_page,
            "Lang": lang,
            "ProjectId": project_id,
            "Key": key}
        return self._handle_request(api_request).result

    def describe_data_hub_subscriptions(
            self,
            topic_id=None,
            source_ip=None,
            feature_type=None,
            page_size=None,
            depart_id=None,
            current_page=None,
            lang=None,
            project_id=None,
            key=None):
        api_request = APIRequest('DescribeDataHubSubscriptions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopicId": topic_id,
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "PageSize": page_size,
            "DepartId": depart_id,
            "CurrentPage": current_page,
            "Lang": lang,
            "ProjectId": project_id,
            "Key": key}
        return self._handle_request(api_request).result

    def describe_data_hub_projects(
            self,
            source_ip=None,
            feature_type=None,
            page_size=None,
            depart_id=None,
            current_page=None,
            lang=None,
            key=None,
            query_type=None):
        api_request = APIRequest('DescribeDataHubProjects', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "PageSize": page_size,
            "DepartId": depart_id,
            "CurrentPage": current_page,
            "Lang": lang,
            "Key": key,
            "QueryType": query_type}
        return self._handle_request(api_request).result

    def describe_data_hub_connectors(
            self,
            topic_id=None,
            source_ip=None,
            feature_type=None,
            page_size=None,
            depart_id=None,
            current_page=None,
            lang=None,
            project_id=None,
            key=None):
        api_request = APIRequest('DescribeDataHubConnectors', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TopicId": topic_id,
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "PageSize": page_size,
            "DepartId": depart_id,
            "CurrentPage": current_page,
            "Lang": lang,
            "ProjectId": project_id,
            "Key": key}
        return self._handle_request(api_request).result

    def describe_data_counts(self, source_ip=None, feature_type=None, lang=None):
        api_request = APIRequest('DescribeDataCounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "FeatureType": feature_type, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_data_assets(
            self,
            range_id=None,
            source_ip=None,
            feature_type=None,
            risk_levels=None,
            name=None,
            page_size=None,
            current_page=None,
            lang=None,
            rule_id=None):
        api_request = APIRequest('DescribeDataAssets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RangeId": range_id,
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "RiskLevels": risk_levels,
            "Name": name,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang,
            "RuleId": rule_id}
        return self._handle_request(api_request).result

    def describe_configs(self, source_ip=None, feature_type=None, lang=None):
        api_request = APIRequest('DescribeConfigs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "FeatureType": feature_type, "Lang": lang}
        return self._handle_request(api_request).result

    def describe_conditions(
            self,
            product_code=None,
            source_ip=None,
            feature_type=None,
            search_type=None,
            lang=None,
            query_type=None):
        api_request = APIRequest('DescribeConditions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "SearchType": search_type,
            "Lang": lang,
            "QueryType": query_type}
        return self._handle_request(api_request).result

    def describe_columns(
            self,
            source_ip=None,
            feature_type=None,
            risk_levels=None,
            name=None,
            page_size=None,
            table_id=None,
            current_page=None,
            query_name=None,
            lang=None,
            rule_id=None):
        api_request = APIRequest('DescribeColumns', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "RiskLevels": risk_levels,
            "Name": name,
            "PageSize": page_size,
            "TableId": table_id,
            "CurrentPage": current_page,
            "QueryName": query_name,
            "Lang": lang,
            "RuleId": rule_id}
        return self._handle_request(api_request).result

    def describe_auth_accounts(
            self,
            source_ip=None,
            feature_type=None,
            page_size=None,
            current_page=None,
            lang=None):
        api_request = APIRequest('DescribeAuthAccounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "PageSize": page_size,
            "CurrentPage": current_page,
            "Lang": lang}
        return self._handle_request(api_request).result

    def describe_accounts(
            self,
            product_code=None,
            login_name=None,
            feature_type=None,
            column_id=None,
            package_id=None,
            current_page=None,
            instance_id=None,
            source_ip=None,
            page_size=None,
            depart_id=None,
            operation_id=None,
            table_id=None,
            lang=None,
            key=None,
            query_type=None):
        api_request = APIRequest('DescribeAccounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ProductCode": product_code,
            "LoginName": login_name,
            "FeatureType": feature_type,
            "ColumnId": column_id,
            "PackageId": package_id,
            "CurrentPage": current_page,
            "InstanceId": instance_id,
            "SourceIp": source_ip,
            "PageSize": page_size,
            "DepartId": depart_id,
            "OperationId": operation_id,
            "TableId": table_id,
            "Lang": lang,
            "Key": key,
            "QueryType": query_type}
        return self._handle_request(api_request).result

    def describe_account_detail(
            self,
            source_ip=None,
            lang=None,
            user_id=None,
            account_type_id=None):
        api_request = APIRequest('DescribeAccountDetail', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "Lang": lang,
            "UserId": user_id,
            "AccountTypeId": account_type_id}
        return self._handle_request(api_request).result

    def delete_rule(self, source_ip=None, feature_type=None, id_=None, lang=None):
        api_request = APIRequest('DeleteRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "Id": id_,
            "Lang": lang}
        return self._handle_request(api_request).result

    def delete_data_limit(self, source_ip=None, feature_type=None, id_=None, lang=None):
        api_request = APIRequest('DeleteDataLimit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "Id": id_,
            "Lang": lang}
        return self._handle_request(api_request).result

    def create_user_auth(
            self,
            account_id=None,
            source_ip=None,
            access_key=None,
            access_key_secret=None,
            lang=None):
        api_request = APIRequest('CreateUserAuth', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccountId": account_id,
            "SourceIp": source_ip,
            "AccessKey": access_key,
            "AccessKeySecret": access_key_secret,
            "Lang": lang}
        return self._handle_request(api_request).result

    def create_rule(
            self,
            source_ip=None,
            feature_type=None,
            name=None,
            risk_level_id=None,
            lang=None,
            custom_type=None,
            category=None,
            content=None):
        api_request = APIRequest('CreateRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "Name": name,
            "RiskLevelId": risk_level_id,
            "Lang": lang,
            "CustomType": custom_type,
            "Category": category,
            "Content": content}
        return self._handle_request(api_request).result

    def create_config(
            self,
            code=None,
            source_ip=None,
            feature_type=None,
            description=None,
            config_list=None,
            lang=None,
            value=None):
        api_request = APIRequest('CreateConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Code": code,
            "SourceIp": source_ip,
            "FeatureType": feature_type,
            "Description": description,
            "ConfigList": config_list,
            "Lang": lang,
            "Value": value}
        return self._handle_request(api_request).result

    def describe_data_limit_set(self, source_ip=None, lang=None, resource_type=None):
        api_request = APIRequest('DescribeDataLimitSet', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"SourceIp": source_ip, "Lang": lang, "ResourceType": resource_type}
        return self._handle_request(api_request).result

    def create_data_limit(
            self,
            password=None,
            source_ip=None,
            connector=None,
            data_limit_list=None,
            lang=None,
            resource_type=None,
            service_region_id=None,
            parent_id=None,
            user_name=None):
        api_request = APIRequest('CreateDataLimit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Password": password,
            "SourceIp": source_ip,
            "Connector": connector,
            "DataLimitList": data_limit_list,
            "Lang": lang,
            "ResourceType": resource_type,
            "ServiceRegionId": service_region_id,
            "ParentId": parent_id,
            "UserName": user_name}
        return self._handle_request(api_request).result
