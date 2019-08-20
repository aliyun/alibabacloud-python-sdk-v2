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


class GpdbClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'gpdb'
        self.api_version = '2016-05-03'
        self.location_service_code = 'gpdb'
        self.location_endpoint_type = 'openAPI'

    def upgrade_db_version(
            self,
            switch_time_mode=None,
            major_version=None,
            region_id=None,
            minor_version=None,
            db_instance_id=None,
            switch_time=None,
            owner_id=None):
        api_request = APIRequest('UpgradeDBVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SwitchTimeMode": switch_time_mode,
            "MajorVersion": major_version,
            "RegionId": region_id,
            "MinorVersion": minor_version,
            "DBInstanceId": db_instance_id,
            "SwitchTime": switch_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def upgrade_db_instance(
            self,
            db_instance_group_count=None,
            region_id=None,
            db_instance_id=None,
            owner_id=None,
            pay_type=None,
            db_instance_class=None):
        api_request = APIRequest('UpgradeDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DBInstanceGroupCount": db_instance_group_count,
            "RegionId": region_id,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "PayType": pay_type,
            "DBInstanceClass": db_instance_class}
        return self._handle_request(api_request).result

    def untag_resources(
            self,
            all_=None,
            resource_owner_id=None,
            list_of_resource_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            list_of_tag_key=None,
            resource_type=None):
        api_request = APIRequest('UntagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "All": all_,
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": list_of_resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "TagKey": list_of_tag_key,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "TagKey": ('TagKey', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def tag_resources(
            self,
            resource_owner_id=None,
            list_of_resource_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            list_of_tag=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('TagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": list_of_resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_tag_resources(
            self,
            resource_owner_id=None,
            list_of_resource_id=None,
            resource_owner_account=None,
            region_id=None,
            next_token=None,
            owner_account=None,
            list_of_tag=None,
            owner_id=None,
            resource_type=None):
        api_request = APIRequest('ListTagResources', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceId": list_of_resource_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NextToken": next_token,
            "OwnerAccount": owner_account,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "ResourceType": resource_type}
        repeat_info = {"ResourceId": ('ResourceId', 'list', 'str', None),
                       "Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_rds_vswitchs(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            vpc_id=None,
            zone_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeRdsVSwitchs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "VpcId": vpc_id,
            "ZoneId": zone_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_rds_vpcs(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            zone_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeRdsVpcs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ZoneId": zone_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_bu_db_instance_relation(self, business_unit=None, db_instance_id=None, owner_id=None):
        api_request = APIRequest('AddBuDBInstanceRelation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BusinessUnit": business_unit,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_sql_log_records(
            self,
            database=None,
            form=None,
            page_size=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            user=None,
            query_keywords=None,
            page_number=None):
        api_request = APIRequest('DescribeSQLLogRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Database": database,
            "Form": form,
            "PageSize": page_size,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "User": user,
            "QueryKeywords": query_keywords,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_sql_collector_policy(self, sql_collector_status=None, db_instance_id=None):
        api_request = APIRequest('ModifySQLCollectorPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SQLCollectorStatus": sql_collector_status,
            "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def describe_sql_log_files(
            self,
            file_name=None,
            page_size=None,
            db_instance_id=None,
            page_number=None):
        api_request = APIRequest('DescribeSQLLogFiles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "FileName": file_name,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_sql_collector_policy(self, db_instance_id=None):
        api_request = APIRequest('DescribeSQLCollectorPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def describe_slow_log_records(
            self,
            sql_id=None,
            db_name=None,
            page_size=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            page_number=None):
        api_request = APIRequest('DescribeSlowLogRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SQLId": sql_id,
            "DBName": db_name,
            "PageSize": page_size,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def switch_db_instance_net_type(
            self,
            connection_string_prefix=None,
            port=None,
            db_instance_id=None):
        api_request = APIRequest('SwitchDBInstanceNetType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ConnectionStringPrefix": connection_string_prefix,
            "Port": port,
            "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def restart_db_instance(self, client_token=None, db_instance_id=None):
        api_request = APIRequest('RestartDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClientToken": client_token, "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def reset_account_password(self, account_password=None, account_name=None, db_instance_id=None):
        api_request = APIRequest('ResetAccountPassword', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccountPassword": account_password,
            "AccountName": account_name,
            "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def release_instance_public_connection(
            self,
            db_instance_id=None,
            current_connection_string=None):
        api_request = APIRequest('ReleaseInstancePublicConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DBInstanceId": db_instance_id,
                               "CurrentConnectionString": current_connection_string}
        return self._handle_request(api_request).result

    def modify_security_ips(
            self,
            security_ip_list=None,
            db_instance_ip_array_name=None,
            db_instance_ip_array_attribute=None,
            db_instance_id=None):
        api_request = APIRequest('ModifySecurityIps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SecurityIPList": security_ip_list,
            "DBInstanceIPArrayName": db_instance_ip_array_name,
            "DBInstanceIPArrayAttribute": db_instance_ip_array_attribute,
            "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def modify_db_instance_network_type(
            self,
            vswitch_id=None,
            private_ip_address=None,
            vpc_id=None,
            db_instance_id=None,
            instance_network_type=None):
        api_request = APIRequest('ModifyDBInstanceNetworkType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "VPCId": vpc_id,
            "DBInstanceId": db_instance_id,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def modify_db_instance_maintain_time(self, end_time=None, db_instance_id=None, start_time=None):
        api_request = APIRequest('ModifyDBInstanceMaintainTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time}
        return self._handle_request(api_request).result

    def modify_db_instance_description(self, db_instance_id=None, db_instance_description=None):
        api_request = APIRequest('ModifyDBInstanceDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DBInstanceId": db_instance_id,
                               "DBInstanceDescription": db_instance_description}
        return self._handle_request(api_request).result

    def modify_db_instance_connection_string(
            self,
            connection_string_prefix=None,
            port=None,
            db_instance_id=None,
            current_connection_string=None):
        api_request = APIRequest('ModifyDBInstanceConnectionString', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ConnectionStringPrefix": connection_string_prefix,
            "Port": port,
            "DBInstanceId": db_instance_id,
            "CurrentConnectionString": current_connection_string}
        return self._handle_request(api_request).result

    def modify_db_instance_connection_mode(self, connection_mode=None, db_instance_id=None):
        api_request = APIRequest('ModifyDBInstanceConnectionMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ConnectionMode": connection_mode, "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def modify_account_description(
            self,
            account_name=None,
            db_instance_id=None,
            account_description=None):
        api_request = APIRequest('ModifyAccountDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccountName": account_name,
            "DBInstanceId": db_instance_id,
            "AccountDescription": account_description}
        return self._handle_request(api_request).result

    def describe_resource_usage(self, db_instance_id=None):
        api_request = APIRequest('DescribeResourceUsage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def describe_regions(self,):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def describe_db_instances(
            self,
            db_instance_ids=None,
            region_id=None,
            page_size=None,
            db_instance_description=None,
            list_of_tag=None,
            owner_id=None,
            instance_network_type=None,
            page_number=None):
        api_request = APIRequest('DescribeDBInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DBInstanceIds": db_instance_ids,
            "RegionId": region_id,
            "PageSize": page_size,
            "DBInstanceDescription": db_instance_description,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "InstanceNetworkType": instance_network_type,
            "PageNumber": page_number}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_db_instance_performance(
            self,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            key=None):
        api_request = APIRequest('DescribeDBInstancePerformance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "Key": key}
        return self._handle_request(api_request).result

    def describe_db_instance_net_info(self, db_instance_id=None):
        api_request = APIRequest('DescribeDBInstanceNetInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def describe_db_instance_ip_array_list(self, db_instance_id=None):
        api_request = APIRequest('DescribeDBInstanceIPArrayList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def describe_db_instance_attribute(self, db_instance_id=None, owner_id=None):
        api_request = APIRequest('DescribeDBInstanceAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DBInstanceId": db_instance_id, "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_accounts(self, account_name=None, db_instance_id=None):
        api_request = APIRequest('DescribeAccounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"AccountName": account_name, "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def delete_db_instance(self, client_token=None, db_instance_id=None, owner_id=None):
        api_request = APIRequest('DeleteDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ClientToken": client_token,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_database(self, db_name=None, db_instance_id=None):
        api_request = APIRequest('DeleteDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DBName": db_name, "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def create_db_instance(
            self,
            db_instance_group_count=None,
            period=None,
            client_token=None,
            engine_version=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            security_ip_list=None,
            vswitch_id=None,
            private_ip_address=None,
            region_id=None,
            engine=None,
            vpc_id=None,
            zone_id=None,
            db_instance_description=None,
            pay_type=None,
            instance_network_type=None):
        api_request = APIRequest('CreateDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DBInstanceGroupCount": db_instance_group_count,
            "Period": period,
            "ClientToken": client_token,
            "EngineVersion": engine_version,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "SecurityIPList": security_ip_list,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "RegionId": region_id,
            "Engine": engine,
            "VPCId": vpc_id,
            "ZoneId": zone_id,
            "DBInstanceDescription": db_instance_description,
            "PayType": pay_type,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def create_account(
            self,
            account_password=None,
            account_name=None,
            database_name=None,
            db_instance_id=None,
            owner_id=None,
            account_description=None):
        api_request = APIRequest('CreateAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AccountPassword": account_password,
            "AccountName": account_name,
            "DatabaseName": database_name,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "AccountDescription": account_description}
        return self._handle_request(api_request).result

    def allocate_instance_public_connection(
            self,
            resource_owner_id=None,
            connection_string_prefix=None,
            resource_owner_account=None,
            port=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('AllocateInstancePublicConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ConnectionStringPrefix": connection_string_prefix,
            "ResourceOwnerAccount": resource_owner_account,
            "Port": port,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result
