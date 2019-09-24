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


class RdsClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Rds'
        self.api_version = '2014-08-15'
        self.location_service_code = 'rds'
        self.location_endpoint_type = 'openAPI'

    def modify_action_event_policy(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            enable_event_log=None,
            owner_id=None):
        api_request = APIRequest('ModifyActionEventPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "EnableEventLog": enable_event_log,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_action_event_policy(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeActionEventPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_events(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            page_size=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeEvents', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def pre_check_create_order(
            self,
            connection_mode=None,
            resource_owner_id=None,
            db_instance_storage=None,
            node_type=None,
            system_db_charset=None,
            client_token=None,
            country_code=None,
            zone_id_slave1=None,
            zone_id_slave2=None,
            engine_version=None,
            currency_code=None,
            resource_group_id=None,
            region_id=None,
            engine=None,
            db_instance_id=None,
            db_instance_description=None,
            db_instance_storage_type=None,
            business_info=None,
            db_instance_net_type=None,
            agent_id=None,
            restore_time=None,
            quantity=None,
            auto_pay=None,
            resource_owner_account=None,
            resource=None,
            backup_id=None,
            owner_account=None,
            commodity_code=None,
            encryption_key=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            security_ip_list=None,
            vswitch_id=None,
            private_ip_address=None,
            instance_used_type=None,
            auto_renew=None,
            promotion_code=None,
            role_arn=None,
            vpc_id=None,
            zone_id=None,
            time_type=None,
            category=None,
            pay_type=None,
            instance_network_type=None):
        api_request = APIRequest('PreCheckCreateOrder', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ConnectionMode": connection_mode,
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "NodeType": node_type,
            "SystemDBCharset": system_db_charset,
            "ClientToken": client_token,
            "CountryCode": country_code,
            "ZoneIdSlave1": zone_id_slave1,
            "ZoneIdSlave2": zone_id_slave2,
            "EngineVersion": engine_version,
            "CurrencyCode": currency_code,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "Engine": engine,
            "DBInstanceId": db_instance_id,
            "DBInstanceDescription": db_instance_description,
            "DBInstanceStorageType": db_instance_storage_type,
            "BusinessInfo": business_info,
            "DBInstanceNetType": db_instance_net_type,
            "AgentId": agent_id,
            "RestoreTime": restore_time,
            "Quantity": quantity,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "Resource": resource,
            "BackupId": backup_id,
            "OwnerAccount": owner_account,
            "CommodityCode": commodity_code,
            "EncryptionKey": encryption_key,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "SecurityIPList": security_ip_list,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "InstanceUsedType": instance_used_type,
            "AutoRenew": auto_renew,
            "PromotionCode": promotion_code,
            "RoleARN": role_arn,
            "VPCId": vpc_id,
            "ZoneId": zone_id,
            "TimeType": time_type,
            "Category": category,
            "PayType": pay_type,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def pre_check_create_order_for_rebuild(
            self,
            resource_owner_id=None,
            client_token=None,
            resource_group_id=None,
            region_id=None,
            db_instance_id=None,
            db_instance_description=None,
            business_info=None,
            agent_id=None,
            auto_pay=None,
            resource_owner_account=None,
            resource=None,
            owner_account=None,
            commodity_code=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            vswitch_id=None,
            rebuild_instance_flag=None,
            auto_renew=None,
            promotion_code=None,
            vpc_id=None,
            zone_id=None,
            time_type=None,
            pay_type=None,
            instance_network_type=None):
        api_request = APIRequest('PreCheckCreateOrderForRebuild', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "DBInstanceId": db_instance_id,
            "DBInstanceDescription": db_instance_description,
            "BusinessInfo": business_info,
            "AgentId": agent_id,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "Resource": resource,
            "OwnerAccount": owner_account,
            "CommodityCode": commodity_code,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "VSwitchId": vswitch_id,
            "RebuildInstanceFlag": rebuild_instance_flag,
            "AutoRenew": auto_renew,
            "PromotionCode": promotion_code,
            "VPCId": vpc_id,
            "ZoneId": zone_id,
            "TimeType": time_type,
            "PayType": pay_type,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def pre_check_create_order_for_modify(
            self,
            resource_owner_id=None,
            db_instance_storage=None,
            node_type=None,
            client_token=None,
            engine_version=None,
            region_id=None,
            effective_time=None,
            db_instance_id=None,
            switch_time=None,
            db_instance_storage_type=None,
            business_info=None,
            auto_pay=None,
            resource_owner_account=None,
            resource=None,
            commodity_code=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            vswitch_id=None,
            promotion_code=None,
            vpc_id=None,
            zone_id=None,
            time_type=None,
            pay_type=None,
            instance_network_type=None):
        api_request = APIRequest('PreCheckCreateOrderForModify', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "NodeType": node_type,
            "ClientToken": client_token,
            "EngineVersion": engine_version,
            "RegionId": region_id,
            "EffectiveTime": effective_time,
            "DBInstanceId": db_instance_id,
            "SwitchTime": switch_time,
            "DBInstanceStorageType": db_instance_storage_type,
            "BusinessInfo": business_info,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "Resource": resource,
            "CommodityCode": commodity_code,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "VSwitchId": vswitch_id,
            "PromotionCode": promotion_code,
            "VpcId": vpc_id,
            "ZoneId": zone_id,
            "TimeType": time_type,
            "PayType": pay_type,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def pre_check_create_order_for_degrade(
            self,
            resource_owner_id=None,
            db_instance_storage=None,
            auto_pay=None,
            resource_owner_account=None,
            client_token=None,
            resource=None,
            commodity_code=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            region_id=None,
            effective_time=None,
            promotion_code=None,
            zone_id=None,
            db_instance_id=None,
            time_type=None,
            pay_type=None,
            business_info=None):
        api_request = APIRequest('PreCheckCreateOrderForDegrade', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Resource": resource,
            "CommodityCode": commodity_code,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "RegionId": region_id,
            "EffectiveTime": effective_time,
            "PromotionCode": promotion_code,
            "ZoneId": zone_id,
            "DBInstanceId": db_instance_id,
            "TimeType": time_type,
            "PayType": pay_type,
            "BusinessInfo": business_info}
        return self._handle_request(api_request).result

    def pre_check_create_order_for_defer(
            self,
            resource_owner_id=None,
            db_instance_storage=None,
            auto_pay=None,
            resource_owner_account=None,
            client_token=None,
            resource=None,
            commodity_code=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            renew_change=None,
            region_id=None,
            db_instance_id=None,
            time_type=None,
            db_instance_storage_type=None,
            pay_type=None,
            business_info=None):
        api_request = APIRequest('PreCheckCreateOrderForDefer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Resource": resource,
            "CommodityCode": commodity_code,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "RenewChange": renew_change,
            "RegionId": region_id,
            "DBInstanceId": db_instance_id,
            "TimeType": time_type,
            "DBInstanceStorageType": db_instance_storage_type,
            "PayType": pay_type,
            "BusinessInfo": business_info}
        return self._handle_request(api_request).result

    def pre_check_create_order_for_clone(
            self,
            resource_owner_id=None,
            db_instance_storage=None,
            node_type=None,
            client_token=None,
            country_code=None,
            currency_code=None,
            resource_group_id=None,
            table_meta=None,
            db_instance_id=None,
            db_instance_description=None,
            db_instance_storage_type=None,
            business_info=None,
            agent_id=None,
            restore_time=None,
            quantity=None,
            auto_pay=None,
            resource_owner_account=None,
            resource=None,
            backup_id=None,
            owner_account=None,
            restore_table=None,
            commodity_code=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            db_names=None,
            vswitch_id=None,
            private_ip_address=None,
            instance_used_type=None,
            auto_renew=None,
            promotion_code=None,
            vpc_id=None,
            zone_id=None,
            clone_instance_default_value=None,
            time_type=None,
            pay_type=None,
            instance_network_type=None):
        api_request = APIRequest('PreCheckCreateOrderForClone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "NodeType": node_type,
            "ClientToken": client_token,
            "CountryCode": country_code,
            "CurrencyCode": currency_code,
            "ResourceGroupId": resource_group_id,
            "TableMeta": table_meta,
            "DBInstanceId": db_instance_id,
            "DBInstanceDescription": db_instance_description,
            "DBInstanceStorageType": db_instance_storage_type,
            "BusinessInfo": business_info,
            "AgentId": agent_id,
            "RestoreTime": restore_time,
            "Quantity": quantity,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "Resource": resource,
            "BackupId": backup_id,
            "OwnerAccount": owner_account,
            "RestoreTable": restore_table,
            "CommodityCode": commodity_code,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "DBNames": db_names,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "InstanceUsedType": instance_used_type,
            "AutoRenew": auto_renew,
            "PromotionCode": promotion_code,
            "VPCId": vpc_id,
            "ZoneId": zone_id,
            "CloneInstanceDefaultValue": clone_instance_default_value,
            "TimeType": time_type,
            "PayType": pay_type,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def pre_check_create_order_for_temp_upgrade(
            self,
            resource_owner_id=None,
            db_instance_storage=None,
            node_type=None,
            auto_pay=None,
            resource_owner_account=None,
            client_token=None,
            resource=None,
            commodity_code=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            region_id=None,
            effective_time=None,
            db_instance_id=None,
            db_instance_storage_type=None,
            business_info=None):
        api_request = APIRequest('PreCheckCreateOrderForTempUpgrade', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "NodeType": node_type,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Resource": resource,
            "CommodityCode": commodity_code,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "RegionId": region_id,
            "EffectiveTime": effective_time,
            "DBInstanceId": db_instance_id,
            "DBInstanceStorageType": db_instance_storage_type,
            "BusinessInfo": business_info}
        return self._handle_request(api_request).result

    def pre_check_db_instance_operation(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_instance_id=None,
            owner_id=None,
            operation=None):
        api_request = APIRequest('PreCheckDBInstanceOperation', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "Operation": operation}
        return self._handle_request(api_request).result

    def describe_dtc_security_ip_hosts_for_sql_server(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDTCSecurityIpHostsForSQLServer',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_dtc_security_ip_hosts_for_sql_server(
            self,
            resource_owner_id=None,
            white_list_group_name=None,
            security_token=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            db_instance_id=None,
            security_ip_hosts=None,
            owner_id=None):
        api_request = APIRequest('ModifyDTCSecurityIpHostsForSQLServer',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "WhiteListGroupName": white_list_group_name,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "SecurityIpHosts": security_ip_hosts,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_instance_ip_hostname(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceIpHostname', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_instance_auto_upgrade_minor_version(
            self,
            auto_upgrade_minor_version=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest(
            'ModifyDBInstanceAutoUpgradeMinorVersion',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "AutoUpgradeMinorVersion": auto_upgrade_minor_version,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_available_cross_region(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeAvailableCrossRegion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def check_create_ddr_db_instance(
            self,
            resource_owner_id=None,
            restore_time=None,
            db_instance_storage=None,
            source_db_instance_name=None,
            bak_set_name=None,
            resource_owner_account=None,
            host_type=None,
            backup_set_id=None,
            engine_version=None,
            owner_id=None,
            user_bak_set_url=None,
            db_instance_class=None,
            restore_type=None,
            region_id=None,
            engine=None,
            source_region=None,
            backup_set_region=None,
            backup_set_type=None):
        api_request = APIRequest('CheckCreateDdrDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RestoreTime": restore_time,
            "DBInstanceStorage": db_instance_storage,
            "SourceDBInstanceName": source_db_instance_name,
            "BakSetName": bak_set_name,
            "ResourceOwnerAccount": resource_owner_account,
            "HostType": host_type,
            "BackupSetId": backup_set_id,
            "EngineVersion": engine_version,
            "OwnerId": owner_id,
            "UserBakSetURL": user_bak_set_url,
            "DBInstanceClass": db_instance_class,
            "RestoreType": restore_type,
            "RegionId": region_id,
            "Engine": engine,
            "SourceRegion": source_region,
            "BackupSetRegion": backup_set_region,
            "BackupSetType": backup_set_type}
        return self._handle_request(api_request).result

    def describe_available_recovery_time(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            cross_backup_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeAvailableRecoveryTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "CrossBackupId": cross_backup_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cross_region_log_backup_files(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            page_size=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            owner_id=None,
            cross_backup_region=None,
            page_number=None):
        api_request = APIRequest('DescribeCrossRegionLogBackupFiles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "PageSize": page_size,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "CrossBackupRegion": cross_backup_region,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_instance_cross_backup_policy(
            self,
            resource_owner_id=None,
            retent_type=None,
            resource_owner_account=None,
            cross_backup_type=None,
            log_backup_enabled=None,
            backup_enabled=None,
            rel_service=None,
            owner_id=None,
            cross_backup_region=None,
            storage_type=None,
            endpoint=None,
            region_id=None,
            storage_owner=None,
            db_instance_id=None,
            retention=None):
        api_request = APIRequest('ModifyInstanceCrossBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RetentType": retent_type,
            "ResourceOwnerAccount": resource_owner_account,
            "CrossBackupType": cross_backup_type,
            "LogBackupEnabled": log_backup_enabled,
            "BackupEnabled": backup_enabled,
            "RelService": rel_service,
            "OwnerId": owner_id,
            "CrossBackupRegion": cross_backup_region,
            "StorageType": storage_type,
            "Endpoint": endpoint,
            "RegionId": region_id,
            "StorageOwner": storage_owner,
            "DBInstanceId": db_instance_id,
            "Retention": retention}
        return self._handle_request(api_request).result

    def create_ddr_instance(
            self,
            connection_mode=None,
            resource_owner_id=None,
            db_instance_storage=None,
            system_db_charset=None,
            source_db_instance_name=None,
            client_token=None,
            host_type=None,
            engine_version=None,
            user_bak_set_url=None,
            resource_group_id=None,
            region_id=None,
            engine=None,
            db_instance_description=None,
            db_instance_storage_type=None,
            backup_set_region=None,
            db_instance_net_type=None,
            backup_set_type=None,
            period=None,
            restore_time=None,
            bak_set_name=None,
            resource_owner_account=None,
            owner_account=None,
            backup_set_id=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            security_ip_list=None,
            vswitch_id=None,
            private_ip_address=None,
            restore_type=None,
            vpc_id=None,
            tunnel_id=None,
            zone_id=None,
            pay_type=None,
            source_region=None,
            instance_network_type=None):
        api_request = APIRequest('CreateDdrInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ConnectionMode": connection_mode,
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "SystemDBCharset": system_db_charset,
            "SourceDBInstanceName": source_db_instance_name,
            "ClientToken": client_token,
            "HostType": host_type,
            "EngineVersion": engine_version,
            "UserBakSetURL": user_bak_set_url,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "Engine": engine,
            "DBInstanceDescription": db_instance_description,
            "DBInstanceStorageType": db_instance_storage_type,
            "BackupSetRegion": backup_set_region,
            "DBInstanceNetType": db_instance_net_type,
            "BackupSetType": backup_set_type,
            "Period": period,
            "RestoreTime": restore_time,
            "BakSetName": bak_set_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "BackupSetId": backup_set_id,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "SecurityIPList": security_ip_list,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "RestoreType": restore_type,
            "VPCId": vpc_id,
            "TunnelId": tunnel_id,
            "ZoneId": zone_id,
            "PayType": pay_type,
            "SourceRegion": source_region,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def describe_cross_region_backup_db_instance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            page_size=None,
            db_instance_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeCrossRegionBackupDBInstance',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_instance_cross_backup_policy(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceCrossBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cross_region_backups(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            cross_backup_region=None,
            page_number=None,
            region_id=None,
            page_size=None,
            db_instance_id=None,
            cross_backup_id=None):
        api_request = APIRequest('DescribeCrossRegionBackups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "CrossBackupRegion": cross_backup_region,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "CrossBackupId": cross_backup_id}
        return self._handle_request(api_request).result

    def evaluate_support_byok_show(
            self,
            resource_owner_id=None,
            node_type=None,
            resource_owner_account=None,
            owner_account=None,
            engine_version=None,
            owner_id=None,
            security_token=None,
            region_id=None,
            engine=None,
            target_region_id=None,
            db_instance_storage_type=None):
        api_request = APIRequest('EvaluateSupportByokShow', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "NodeType": node_type,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EngineVersion": engine_version,
            "OwnerId": owner_id,
            "SecurityToken": security_token,
            "RegionId": region_id,
            "Engine": engine,
            "TargetRegionId": target_region_id,
            "DbInstanceStorageType": db_instance_storage_type}
        return self._handle_request(api_request).result

    def describe_instance_vpc_migrate_info(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            vpc_id=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeInstanceVpcMigrateInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "VpcId": vpc_id,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_read_db_instance_delay(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            read_instance_id=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeReadDBInstanceDelay', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReadInstanceId": read_instance_id,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def allocate_instance_vpc_network_type(
            self,
            target_vpc_id=None,
            resource_owner_id=None,
            target_zone_id=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            target_region_id=None,
            target_vswitch_id=None,
            owner_id=None):
        api_request = APIRequest('AllocateInstanceVpcNetworkType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TargetVpcId": target_vpc_id,
            "ResourceOwnerId": resource_owner_id,
            "TargetZoneId": target_zone_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "TargetRegionId": target_region_id,
            "TargetVSwitchId": target_vswitch_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def restore_table(
            self,
            resource_owner_id=None,
            restore_time=None,
            resource_owner_account=None,
            client_token=None,
            backup_id=None,
            owner_account=None,
            table_meta=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('RestoreTable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RestoreTime": restore_time,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "BackupId": backup_id,
            "OwnerAccount": owner_account,
            "TableMeta": table_meta,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def migrate_to_other_region(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            target_vswitch_id=None,
            owner_id=None,
            target_vpc_id=None,
            target_zone_id=None,
            effective_time=None,
            db_instance_id=None,
            target_region_id=None,
            switch_time=None):
        api_request = APIRequest('MigrateToOtherRegion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "TargetVSwitchId": target_vswitch_id,
            "OwnerId": owner_id,
            "TargetVpcId": target_vpc_id,
            "TargetZoneId": target_zone_id,
            "EffectiveTime": effective_time,
            "DBInstanceId": db_instance_id,
            "TargetRegionId": target_region_id,
            "SwitchTime": switch_time}
        return self._handle_request(api_request).result

    def describe_meta_list(
            self,
            resource_owner_id=None,
            restore_time=None,
            resource_owner_account=None,
            client_token=None,
            pattern=None,
            backup_set_id=None,
            owner_id=None,
            get_db_name=None,
            restore_type=None,
            page_size=None,
            db_instance_id=None,
            page_index=None):
        api_request = APIRequest('DescribeMetaList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RestoreTime": restore_time,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Pattern": pattern,
            "BackupSetID": backup_set_id,
            "OwnerId": owner_id,
            "GetDbName": get_db_name,
            "RestoreType": restore_type,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "PageIndex": page_index}
        return self._handle_request(api_request).result

    def describe_proxy_function_support(
            self,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeProxyFunctionSupport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_available_instance_class(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            engine_version=None,
            owner_id=None,
            region_id=None,
            engine=None,
            zone_id=None,
            db_instance_id=None,
            instance_charge_type=None,
            order_type=None):
        api_request = APIRequest('DescribeAvailableInstanceClass', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EngineVersion": engine_version,
            "OwnerId": owner_id,
            "RegionId": region_id,
            "Engine": engine,
            "ZoneId": zone_id,
            "DBInstanceId": db_instance_id,
            "InstanceChargeType": instance_charge_type,
            "OrderType": order_type}
        return self._handle_request(api_request).result

    def request_service_of_cloud_db_expert(
            self,
            service_request_param=None,
            db_instance_id=None,
            service_request_type=None):
        api_request = APIRequest('RequestServiceOfCloudDBExpert', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ServiceRequestParam": service_request_param,
            "DBInstanceId": db_instance_id,
            "ServiceRequestType": service_request_type}
        return self._handle_request(api_request).result

    def describe_cloud_db_expert_service(
            self,
            service_request_param=None,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            service_request_type=None):
        api_request = APIRequest('DescribeCloudDbExpertService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ServiceRequestParam": service_request_param,
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "ServiceRequestType": service_request_type}
        return self._handle_request(api_request).result

    def describe_templates_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            min_avg_consume=None,
            owner_account=None,
            max_records_per_page=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            max_avg_consume=None,
            sort_key=None,
            min_avg_scan_rows=None,
            sq_type=None,
            security_token=None,
            sort_method=None,
            page_numbers=None,
            paging_id=None,
            db_instance_id=None,
            max_avg_scan_rows=None):
        api_request = APIRequest('DescribeTemplatesList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "MinAvgConsume": min_avg_consume,
            "OwnerAccount": owner_account,
            "MaxRecordsPerPage": max_records_per_page,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "MaxAvgConsume": max_avg_consume,
            "SortKey": sort_key,
            "MinAvgScanRows": min_avg_scan_rows,
            "SqType": sq_type,
            "SecurityToken": security_token,
            "SortMethod": sort_method,
            "PageNumbers": page_numbers,
            "PagingId": paging_id,
            "DBInstanceId": db_instance_id,
            "MaxAvgScanRows": max_avg_scan_rows}
        return self._handle_request(api_request).result

    def modify_my_sqldb_instance_delay(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            sql_delay=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyMySQLDBInstanceDelay', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "SqlDelay": sql_delay,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def check_instance_exist(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('CheckInstanceExist', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_log_backup_files(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeLogBackupFiles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def migrate_security_ip_mode(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('MigrateSecurityIPMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def switch_db_instance_vpc(
            self,
            vswitch_id=None,
            private_ip_address=None,
            resource_owner_id=None,
            resource_owner_account=None,
            vpc_id=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('SwitchDBInstanceVpc', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "VPCId": vpc_id,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_collation_time_zones(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeCollationTimeZones', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_collation_time_zone(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            timezone=None,
            db_instance_id=None,
            collation=None,
            owner_id=None):
        api_request = APIRequest('ModifyCollationTimeZone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Timezone": timezone,
            "DBInstanceId": db_instance_id,
            "Collation": collation,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_backup_database(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            backup_id=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeBackupDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "BackupId": backup_id,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def copy_database_between_instances(
            self,
            resource_owner_id=None,
            restore_time=None,
            resource_owner_account=None,
            client_token=None,
            backup_id=None,
            owner_account=None,
            owner_id=None,
            sync_user_privilege=None,
            db_names=None,
            resource_group_id=None,
            target_db_instance_id=None,
            db_instance_id=None,
            pay_type=None):
        api_request = APIRequest('CopyDatabaseBetweenInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RestoreTime": restore_time,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "BackupId": backup_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "SyncUserPrivilege": sync_user_privilege,
            "DbNames": db_names,
            "ResourceGroupId": resource_group_id,
            "TargetDBInstanceId": target_db_instance_id,
            "DBInstanceId": db_instance_id,
            "PayType": pay_type}
        return self._handle_request(api_request).result

    def recovery_db_instance(
            self,
            resource_owner_id=None,
            restore_time=None,
            period=None,
            db_instance_storage=None,
            resource_owner_account=None,
            client_token=None,
            backup_id=None,
            owner_account=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            db_names=None,
            vswitch_id=None,
            private_ip_address=None,
            resource_group_id=None,
            target_db_instance_id=None,
            vpc_id=None,
            db_instance_description=None,
            db_instance_id=None,
            pay_type=None,
            instance_network_type=None):
        api_request = APIRequest('RecoveryDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RestoreTime": restore_time,
            "Period": period,
            "DBInstanceStorage": db_instance_storage,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "BackupId": backup_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "DbNames": db_names,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "ResourceGroupId": resource_group_id,
            "TargetDBInstanceId": target_db_instance_id,
            "VPCId": vpc_id,
            "DBInstanceDescription": db_instance_description,
            "DBInstanceId": db_instance_id,
            "PayType": pay_type,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def describe_available_resource(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            engine_version=None,
            owner_id=None,
            db_instance_class=None,
            region_id=None,
            engine=None,
            zone_id=None,
            db_instance_id=None,
            instance_charge_type=None,
            order_type=None):
        api_request = APIRequest('DescribeAvailableResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EngineVersion": engine_version,
            "OwnerId": owner_id,
            "DBInstanceClass": db_instance_class,
            "RegionId": region_id,
            "Engine": engine,
            "ZoneId": zone_id,
            "DBInstanceId": db_instance_id,
            "InstanceChargeType": instance_charge_type,
            "OrderType": order_type}
        return self._handle_request(api_request).result

    def modify_readonly_instance_delay_replication_time(
            self,
            resource_owner_id=None,
            read_sql_replication_time=None,
            resource_owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest(
            'ModifyReadonlyInstanceDelayReplicationTime',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ReadSQLReplicationTime": read_sql_replication_time,
            "ResourceOwnerAccount": resource_owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_instance_proxy_configuration(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceProxyConfiguration',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_online_database_task(
            self,
            resource_owner_id=None,
            migrate_task_id=None,
            db_name=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            check_db_mode=None,
            owner_id=None):
        api_request = APIRequest('CreateOnlineDatabaseTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "MigrateTaskId": migrate_task_id,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "CheckDBMode": check_db_mode,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def upgrade_db_instance_kernel_version(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            upgrade_time=None,
            db_instance_id=None,
            switch_time=None,
            owner_id=None):
        api_request = APIRequest('UpgradeDBInstanceKernelVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "UpgradeTime": upgrade_time,
            "DBInstanceId": db_instance_id,
            "SwitchTime": switch_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_instance_proxy_configuration(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            proxy_configuration_key=None,
            proxy_configuration_value=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBInstanceProxyConfiguration',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ProxyConfigurationKey": proxy_configuration_key,
            "ProxyConfigurationValue": proxy_configuration_value,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_security_group_configuration(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeSecurityGroupConfiguration',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_security_group_configuration(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            security_group_id=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifySecurityGroupConfiguration', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "SecurityGroupId": security_group_id,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_oss_downloads_for_sql_server(
            self,
            resource_owner_id=None,
            migrate_task_id=None,
            resource_owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeOssDownloadsForSQLServer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "MigrateTaskId": migrate_task_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_migrate_tasks_for_sql_server(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            page_size=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeMigrateTasksForSQLServer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PageSize": page_size,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def create_migrate_task_for_sql_server(
            self,
            resource_owner_id=None,
            task_type=None,
            db_name=None,
            resource_owner_account=None,
            is_online_db=None,
            db_instance_id=None,
            owner_id=None,
            oss_urls=None):
        api_request = APIRequest('CreateMigrateTaskForSQLServer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "TaskType": task_type,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "IsOnlineDB": is_online_db,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "OSSUrls": oss_urls}
        return self._handle_request(api_request).result

    def create_migrate_task(
            self,
            resource_owner_id=None,
            migrate_task_id=None,
            resource_owner_account=None,
            is_online_db=None,
            owner_id=None,
            oss_object_positions=None,
            oss_urls=None,
            db_name=None,
            db_instance_id=None,
            backup_mode=None,
            check_db_mode=None):
        api_request = APIRequest('CreateMigrateTask', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "MigrateTaskId": migrate_task_id,
            "ResourceOwnerAccount": resource_owner_account,
            "IsOnlineDB": is_online_db,
            "OwnerId": owner_id,
            "OssObjectPositions": oss_object_positions,
            "OSSUrls": oss_urls,
            "DBName": db_name,
            "DBInstanceId": db_instance_id,
            "BackupMode": backup_mode,
            "CheckDBMode": check_db_mode}
        return self._handle_request(api_request).result

    def describe_oss_downloads(
            self,
            resource_owner_id=None,
            migrate_task_id=None,
            resource_owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeOssDownloads', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "MigrateTaskId": migrate_task_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_migrate_tasks(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            page_size=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeMigrateTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "PageSize": page_size,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def copy_database(self, resource_owner_id=None, resource_owner_account=None, owner_id=None):
        api_request = APIRequest('CopyDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def reset_account(
            self,
            resource_owner_id=None,
            account_password=None,
            account_name=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ResetAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountPassword": account_password,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_instances_as_csv(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstancesAsCsv', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_instance_network_expire_time(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            connection_string=None,
            classic_expired_days=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBInstanceNetworkExpireTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ConnectionString": connection_string,
            "ClassicExpiredDays": classic_expired_days,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_resource_group(
            self,
            resource_group_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyResourceGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_replica_description(
            self,
            replica_description=None,
            resource_owner_id=None,
            security_token=None,
            resource_owner_account=None,
            owner_account=None,
            replica_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyReplicaDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ReplicaDescription": replica_description,
            "ResourceOwnerId": resource_owner_id,
            "SecurityToken": security_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ReplicaId": replica_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_db_instance_replica(
            self,
            connection_mode=None,
            domain_mode=None,
            replica_description=None,
            resource_owner_id=None,
            db_instance_storage=None,
            system_db_charset=None,
            client_token=None,
            engine_version=None,
            region_id=None,
            engine=None,
            db_instance_description=None,
            db_instance_net_type=None,
            period=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            security_ip_list=None,
            vswitch_id=None,
            private_ip_address=None,
            source_db_instance_id=None,
            replica_mode=None,
            vpc_id=None,
            zone_id=None,
            pay_type=None,
            instance_network_type=None):
        api_request = APIRequest('CreateDBInstanceReplica', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ConnectionMode": connection_mode,
            "DomainMode": domain_mode,
            "ReplicaDescription": replica_description,
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "SystemDBCharset": system_db_charset,
            "ClientToken": client_token,
            "EngineVersion": engine_version,
            "RegionId": region_id,
            "Engine": engine,
            "DBInstanceDescription": db_instance_description,
            "DBInstanceNetType": db_instance_net_type,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "SecurityIPList": security_ip_list,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "SourceDBInstanceId": source_db_instance_id,
            "ReplicaMode": replica_mode,
            "VPCId": vpc_id,
            "ZoneId": zone_id,
            "PayType": pay_type,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def describe_renewal_price(
            self,
            resource_owner_id=None,
            quantity=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            commodity_code=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            region_id=None,
            promotion_code=None,
            db_instance_id=None,
            time_type=None,
            pay_type=None,
            business_info=None,
            order_type=None):
        api_request = APIRequest('DescribeRenewalPrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Quantity": quantity,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "CommodityCode": commodity_code,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "RegionId": region_id,
            "PromotionCode": promotion_code,
            "DBInstanceId": db_instance_id,
            "TimeType": time_type,
            "PayType": pay_type,
            "BusinessInfo": business_info,
            "OrderType": order_type}
        return self._handle_request(api_request).result

    def describe_price(
            self,
            resource_owner_id=None,
            db_instance_storage=None,
            quantity=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            commodity_code=None,
            engine_version=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            instance_used_type=None,
            region_id=None,
            engine=None,
            zone_id=None,
            time_type=None,
            pay_type=None,
            order_type=None):
        api_request = APIRequest('DescribePrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "Quantity": quantity,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "CommodityCode": commodity_code,
            "EngineVersion": engine_version,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "InstanceUsedType": instance_used_type,
            "RegionId": region_id,
            "Engine": engine,
            "ZoneId": zone_id,
            "TimeType": time_type,
            "PayType": pay_type,
            "OrderType": order_type}
        return self._handle_request(api_request).result

    def renew_instance(
            self,
            resource_owner_id=None,
            period=None,
            auto_pay=None,
            resource_owner_account=None,
            client_token=None,
            db_instance_id=None,
            owner_id=None,
            business_info=None):
        api_request = APIRequest('RenewInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "BusinessInfo": business_info}
        return self._handle_request(api_request).result

    def describe_task_info(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            task_id=None):
        api_request = APIRequest('DescribeTaskInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "TaskId": task_id}
        return self._handle_request(api_request).result

    def check_recovery_conditions(
            self,
            resource_owner_id=None,
            restore_time=None,
            resource_owner_account=None,
            backup_file=None,
            backup_id=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('CheckRecoveryConditions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RestoreTime": restore_time,
            "ResourceOwnerAccount": resource_owner_account,
            "BackupFile": backup_file,
            "BackupId": backup_id,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_instance_auto_renewal_attribute(
            self,
            duration=None,
            resource_owner_id=None,
            auto_renew=None,
            resource_owner_account=None,
            region_id=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyInstanceAutoRenewalAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "ResourceOwnerId": resource_owner_id,
            "AutoRenew": auto_renew,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_instance_auto_renewal_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            db_instance_id=None,
            owner_id=None,
            page_number=None,
            proxy_id=None):
        api_request = APIRequest('DescribeInstanceAutoRenewalAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "proxyId": proxy_id}
        return self._handle_request(api_request).result

    def release_read_write_splitting_connection(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ReleaseReadWriteSplittingConnection',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_read_write_splitting_connection(
            self,
            resource_owner_id=None,
            connection_string_prefix=None,
            resource_owner_account=None,
            port=None,
            distribution_type=None,
            owner_account=None,
            weight=None,
            db_instance_id=None,
            owner_id=None,
            max_delay_time=None):
        api_request = APIRequest('ModifyReadWriteSplittingConnection',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ConnectionStringPrefix": connection_string_prefix,
            "ResourceOwnerAccount": resource_owner_account,
            "Port": port,
            "DistributionType": distribution_type,
            "OwnerAccount": owner_account,
            "Weight": weight,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "MaxDelayTime": max_delay_time}
        return self._handle_request(api_request).result

    def calculate_db_instance_weight(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('CalculateDBInstanceWeight', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def allocate_read_write_splitting_connection(
            self,
            resource_owner_id=None,
            connection_string_prefix=None,
            resource_owner_account=None,
            owner_account=None,
            weight=None,
            owner_id=None,
            port=None,
            distribution_type=None,
            net_type=None,
            db_instance_id=None,
            max_delay_time=None):
        api_request = APIRequest('AllocateReadWriteSplittingConnection',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ConnectionStringPrefix": connection_string_prefix,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Weight": weight,
            "OwnerId": owner_id,
            "Port": port,
            "DistributionType": distribution_type,
            "NetType": net_type,
            "DBInstanceId": db_instance_id,
            "MaxDelayTime": max_delay_time}
        return self._handle_request(api_request).result

    def modify_db_instance_pay_type(
            self,
            resource_owner_id=None,
            period=None,
            agent_id=None,
            auto_pay=None,
            resource_owner_account=None,
            client_token=None,
            resource=None,
            owner_account=None,
            owner_id=None,
            used_time=None,
            db_instance_id=None,
            pay_type=None,
            business_info=None):
        api_request = APIRequest('ModifyDBInstancePayType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "AgentId": agent_id,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Resource": resource,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceId": db_instance_id,
            "PayType": pay_type,
            "BusinessInfo": business_info}
        return self._handle_request(api_request).result

    def check_resource(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            specify_count=None,
            engine_version=None,
            owner_id=None,
            db_instance_class=None,
            engine=None,
            region_id=None,
            zone_id=None,
            db_instance_use_type=None,
            db_instance_id=None):
        api_request = APIRequest('CheckResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SpecifyCount": specify_count,
            "EngineVersion": engine_version,
            "OwnerId": owner_id,
            "DBInstanceClass": db_instance_class,
            "Engine": engine,
            "RegionId": region_id,
            "ZoneId": zone_id,
            "DBInstanceUseType": db_instance_use_type,
            "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def describe_character_set_name(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            engine=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeCharacterSetName', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Engine": engine,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_backup(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            backup_id=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "BackupId": backup_id,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_diagnostic_report_list(self, db_instance_id=None):
        api_request = APIRequest('DescribeDiagnosticReportList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def create_diagnostic_report(self, end_time=None, db_instance_id=None, start_time=None):
        api_request = APIRequest('CreateDiagnosticReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time}
        return self._handle_request(api_request).result

    def clone_db_instance(
            self,
            resource_owner_id=None,
            db_instance_storage=None,
            client_token=None,
            zone_id_slave1=None,
            zone_id_slave2=None,
            resource_group_id=None,
            region_id=None,
            table_meta=None,
            db_instance_description=None,
            db_instance_id=None,
            db_instance_storage_type=None,
            restore_time=None,
            period=None,
            resource_owner_account=None,
            backup_id=None,
            owner_account=None,
            restore_table=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            db_names=None,
            vswitch_id=None,
            private_ip_address=None,
            vpc_id=None,
            zone_id=None,
            category=None,
            pay_type=None,
            instance_network_type=None):
        api_request = APIRequest('CloneDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "ClientToken": client_token,
            "ZoneIdSlave1": zone_id_slave1,
            "ZoneIdSlave2": zone_id_slave2,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "TableMeta": table_meta,
            "DBInstanceDescription": db_instance_description,
            "DBInstanceId": db_instance_id,
            "DBInstanceStorageType": db_instance_storage_type,
            "RestoreTime": restore_time,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "BackupId": backup_id,
            "OwnerAccount": owner_account,
            "RestoreTable": restore_table,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "DbNames": db_names,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "VPCId": vpc_id,
            "ZoneId": zone_id,
            "Category": category,
            "PayType": pay_type,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def describe_tags(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            proxy_id=None,
            tags=None):
        api_request = APIRequest('DescribeTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "proxyId": proxy_id,
            "Tags": tags}
        return self._handle_request(api_request).result

    def describe_db_instance_by_tags(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            db_instance_id=None,
            owner_id=None,
            page_number=None,
            proxy_id=None):
        api_request = APIRequest('DescribeDBInstanceByTags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "proxyId": proxy_id}
        return self._handle_request(api_request).result

    def revoke_operator_permission(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('RevokeOperatorPermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_instance_tde(
            self,
            resource_owner_id=None,
            db_name=None,
            resource_owner_account=None,
            role_arn=None,
            owner_account=None,
            db_instance_id=None,
            encryption_key=None,
            owner_id=None,
            tde_status=None):
        api_request = APIRequest('ModifyDBInstanceTDE', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RoleArn": role_arn,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "EncryptionKey": encryption_key,
            "OwnerId": owner_id,
            "TDEStatus": tde_status}
        return self._handle_request(api_request).result

    def modify_db_instance_ssl(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            connection_string=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBInstanceSSL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ConnectionString": connection_string,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def grant_operator_permission(
            self,
            privileges=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            expired_time=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('GrantOperatorPermission', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Privileges": privileges,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ExpiredTime": expired_time,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_instance_tde(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceTDE', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_instance_ssl(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceSSL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_sql_log_files(
            self,
            resource_owner_id=None,
            file_name=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            db_instance_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeSQLLogFiles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "FileName": file_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_db_instance_monitor(
            self,
            resource_owner_id=None,
            period=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBInstanceMonitor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def switch_db_instance_ha(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            effective_time=None,
            owner_account=None,
            db_instance_id=None,
            force=None,
            owner_id=None,
            node_id=None,
            operation=None):
        api_request = APIRequest('SwitchDBInstanceHA', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "EffectiveTime": effective_time,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "Force": force,
            "OwnerId": owner_id,
            "NodeId": node_id,
            "Operation": operation}
        return self._handle_request(api_request).result

    def describe_db_instance_monitor(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceMonitor', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_sql_collector_policy(
            self,
            resource_owner_id=None,
            storage_period=None,
            resource_owner_account=None,
            client_token=None,
            sql_collector_status=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifySQLCollectorPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "StoragePeriod": storage_period,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "SQLCollectorStatus": sql_collector_status,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_instance_ha_config(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            sync_mode=None,
            db_instance_id=None,
            owner_id=None,
            ha_mode=None):
        api_request = APIRequest('ModifyDBInstanceHAConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "SyncMode": sync_mode,
            "DbInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "HAMode": ha_mode}
        return self._handle_request(api_request).result

    def describe_db_instance_ha_config(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceHAConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_sql_reports(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeSQLReports', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_db_instance_ip_array_list(
            self,
            resource_owner_id=None,
            whitelist_network_type=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceIPArrayList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "WhitelistNetworkType": whitelist_network_type,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_sql_log_report_list(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeSQLLogReportList', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def reset_account_for_pg(
            self,
            resource_owner_id=None,
            account_password=None,
            account_name=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ResetAccountForPG', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountPassword": account_password,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def allocate_instance_private_connection(
            self,
            resource_owner_id=None,
            connection_string_prefix=None,
            resource_owner_account=None,
            port=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('AllocateInstancePrivateConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ConnectionStringPrefix": connection_string_prefix,
            "ResourceOwnerAccount": resource_owner_account,
            "Port": port,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def upgrade_db_instance_engine_version(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            effective_time=None,
            owner_account=None,
            db_instance_id=None,
            engine_version=None,
            owner_id=None):
        api_request = APIRequest('UpgradeDBInstanceEngineVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "EffectiveTime": effective_time,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "EngineVersion": engine_version,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def revoke_account_privilege(
            self,
            resource_owner_id=None,
            account_name=None,
            db_name=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('RevokeAccountPrivilege', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def restore_db_instance(
            self,
            resource_owner_id=None,
            restore_time=None,
            resource_owner_account=None,
            client_token=None,
            backup_id=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('RestoreDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RestoreTime": restore_time,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "BackupId": backup_id,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def restart_db_instance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('RestartDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def reset_account_password(
            self,
            resource_owner_id=None,
            account_password=None,
            account_name=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ResetAccountPassword', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountPassword": account_password,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def remove_tags_from_resource(
            self,
            tag4value=None,
            resource_owner_id=None,
            tag2key=None,
            tag5key=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            tag3key=None,
            owner_id=None,
            tag5value=None,
            tags=None,
            tag1key=None,
            tag1value=None,
            region_id=None,
            tag2value=None,
            tag4key=None,
            db_instance_id=None,
            tag3value=None,
            proxy_id=None):
        api_request = APIRequest('RemoveTagsFromResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Tag.4.value": tag4value,
            "ResourceOwnerId": resource_owner_id,
            "Tag.2.key": tag2key,
            "Tag.5.key": tag5key,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Tag.3.key": tag3key,
            "OwnerId": owner_id,
            "Tag.5.value": tag5value,
            "Tags": tags,
            "Tag.1.key": tag1key,
            "Tag.1.value": tag1value,
            "RegionId": region_id,
            "Tag.2.value": tag2value,
            "Tag.4.key": tag4key,
            "DBInstanceId": db_instance_id,
            "Tag.3.value": tag3value,
            "proxyId": proxy_id}
        return self._handle_request(api_request).result

    def purge_db_instance_log(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('PurgeDBInstanceLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_security_ips(
            self,
            db_instance_ip_array_name=None,
            resource_owner_id=None,
            modify_mode=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            security_ips=None,
            security_group_id=None,
            owner_id=None,
            whitelist_network_type=None,
            db_instance_ip_array_attribute=None,
            security_ip_type=None,
            db_instance_id=None):
        api_request = APIRequest('ModifySecurityIps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DBInstanceIPArrayName": db_instance_ip_array_name,
            "ResourceOwnerId": resource_owner_id,
            "ModifyMode": modify_mode,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "SecurityIps": security_ips,
            "SecurityGroupId": security_group_id,
            "OwnerId": owner_id,
            "WhitelistNetworkType": whitelist_network_type,
            "DBInstanceIPArrayAttribute": db_instance_ip_array_attribute,
            "SecurityIPType": security_ip_type,
            "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def modify_parameter(
            self,
            resource_owner_id=None,
            parameter_group_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            forcerestart=None,
            owner_id=None,
            parameters=None):
        api_request = APIRequest('ModifyParameter', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ParameterGroupId": parameter_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "Forcerestart": forcerestart,
            "OwnerId": owner_id,
            "Parameters": parameters}
        return self._handle_request(api_request).result

    def modify_db_instance_spec(
            self,
            resource_owner_id=None,
            db_instance_storage=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            engine_version=None,
            owner_id=None,
            db_instance_class=None,
            effective_time=None,
            db_instance_id=None,
            pay_type=None):
        api_request = APIRequest('ModifyDBInstanceSpec', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "EngineVersion": engine_version,
            "OwnerId": owner_id,
            "DBInstanceClass": db_instance_class,
            "EffectiveTime": effective_time,
            "DBInstanceId": db_instance_id,
            "PayType": pay_type}
        return self._handle_request(api_request).result

    def modify_db_instance_maintain_time(
            self,
            maintain_time=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBInstanceMaintainTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MaintainTime": maintain_time,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_instance_description(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            db_instance_description=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBInstanceDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "DBInstanceDescription": db_instance_description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_db_description(
            self,
            resource_owner_id=None,
            db_name=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            db_description=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "DBDescription": db_description,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_backup_policy(
            self,
            preferred_backup_period=None,
            resource_owner_id=None,
            resource_owner_account=None,
            local_log_retention_hours=None,
            owner_account=None,
            log_backup_frequency=None,
            compress_type=None,
            backup_log=None,
            local_log_retention_space=None,
            owner_id=None,
            duplication=None,
            preferred_backup_time=None,
            backup_retention_period=None,
            duplication_content=None,
            high_space_usage_protection=None,
            db_instance_id=None,
            duplication_location=None,
            log_backup_retention_period=None,
            enable_backup_log=None,
            backup_policy_mode=None):
        api_request = APIRequest('ModifyBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PreferredBackupPeriod": preferred_backup_period,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "LocalLogRetentionHours": local_log_retention_hours,
            "OwnerAccount": owner_account,
            "LogBackupFrequency": log_backup_frequency,
            "CompressType": compress_type,
            "BackupLog": backup_log,
            "LocalLogRetentionSpace": local_log_retention_space,
            "OwnerId": owner_id,
            "Duplication": duplication,
            "PreferredBackupTime": preferred_backup_time,
            "BackupRetentionPeriod": backup_retention_period,
            "DuplicationContent": duplication_content,
            "HighSpaceUsageProtection": high_space_usage_protection,
            "DBInstanceId": db_instance_id,
            "DuplicationLocation": duplication_location,
            "LogBackupRetentionPeriod": log_backup_retention_period,
            "EnableBackupLog": enable_backup_log,
            "BackupPolicyMode": backup_policy_mode}
        return self._handle_request(api_request).result

    def modify_account_description(
            self,
            resource_owner_id=None,
            account_name=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            account_description=None):
        api_request = APIRequest('ModifyAccountDescription', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "AccountDescription": account_description}
        return self._handle_request(api_request).result

    def migrate_to_other_zone(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            zone_id_slave1=None,
            zone_id_slave2=None,
            owner_id=None,
            vswitch_id=None,
            effective_time=None,
            vpc_id=None,
            zone_id=None,
            db_instance_id=None,
            category=None):
        api_request = APIRequest('MigrateToOtherZone', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "ZoneIdSlave1": zone_id_slave1,
            "ZoneIdSlave2": zone_id_slave2,
            "OwnerId": owner_id,
            "VSwitchId": vswitch_id,
            "EffectiveTime": effective_time,
            "VPCId": vpc_id,
            "ZoneId": zone_id,
            "DBInstanceId": db_instance_id,
            "Category": category}
        return self._handle_request(api_request).result

    def import_data_for_sql_server(
            self,
            resource_owner_id=None,
            file_name=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ImportDataForSQLServer', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "FileName": file_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def import_database_between_instances(
            self,
            resource_owner_id=None,
            source_db_instance_id=None,
            resource_owner_account=None,
            db_info=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ImportDatabaseBetweenInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourceDBInstanceId": source_db_instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "DBInfo": db_info,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def grant_account_privilege(
            self,
            resource_owner_id=None,
            account_name=None,
            db_name=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            account_privilege=None):
        api_request = APIRequest('GrantAccountPrivilege', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "AccountPrivilege": account_privilege}
        return self._handle_request(api_request).result

    def describe_tasks(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            page_size=None,
            db_instance_id=None,
            task_action=None,
            status=None):
        api_request = APIRequest('DescribeTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "TaskAction": task_action,
            "Status": status}
        return self._handle_request(api_request).result

    def describe_sql_log_reports(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeSQLLogReports', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_sql_log_records(
            self,
            sql_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            query_keywords=None,
            page_number=None,
            database=None,
            form=None,
            page_size=None,
            db_instance_id=None,
            user=None):
        api_request = APIRequest('DescribeSQLLogRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SQLId": sql_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "QueryKeywords": query_keywords,
            "PageNumber": page_number,
            "Database": database,
            "Form": form,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "User": user}
        return self._handle_request(api_request).result

    def describe_slow_logs(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            sort_key=None,
            db_name=None,
            page_size=None,
            db_instance_id=None):
        api_request = APIRequest('DescribeSlowLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "SortKey": sort_key,
            "DBName": db_name,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def describe_slow_log_records(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            db_name=None,
            page_size=None,
            db_instance_id=None,
            sqlhash=None):
        api_request = APIRequest('DescribeSlowLogRecords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "DBName": db_name,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "SQLHASH": sqlhash}
        return self._handle_request(api_request).result

    def describe_resource_usage(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeResourceUsage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_regions(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_parameter_templates(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            engine=None,
            owner_account=None,
            engine_version=None,
            owner_id=None,
            category=None):
        api_request = APIRequest('DescribeParameterTemplates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Engine": engine,
            "OwnerAccount": owner_account,
            "EngineVersion": engine_version,
            "OwnerId": owner_id,
            "Category": category}
        return self._handle_request(api_request).result

    def describe_parameters(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeParameters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_modify_parameter_log(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeModifyParameterLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_error_logs(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeErrorLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_db_instance_performance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            owner_id=None,
            key=None):
        api_request = APIRequest('DescribeDBInstancePerformance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "Key": key}
        return self._handle_request(api_request).result

    def describe_databases(
            self,
            resource_owner_id=None,
            db_name=None,
            resource_owner_account=None,
            db_status=None,
            owner_account=None,
            page_size=None,
            db_instance_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeDatabases', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "DBStatus": db_status,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_binlog_files(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            end_time=None,
            db_instance_id=None,
            start_time=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeBinlogFiles', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "EndTime": end_time,
            "DBInstanceId": db_instance_id,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_backup_tasks(
            self,
            backup_job_id=None,
            resource_owner_id=None,
            flag=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            backup_mode=None,
            owner_id=None,
            backup_job_status=None):
        api_request = APIRequest('DescribeBackupTasks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BackupJobId": backup_job_id,
            "ResourceOwnerId": resource_owner_id,
            "Flag": flag,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "BackupMode": backup_mode,
            "OwnerId": owner_id,
            "BackupJobStatus": backup_job_status}
        return self._handle_request(api_request).result

    def describe_backups(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            backup_id=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            backup_status=None,
            backup_location=None,
            page_size=None,
            db_instance_id=None,
            backup_mode=None):
        api_request = APIRequest('DescribeBackups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "BackupId": backup_id,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "BackupStatus": backup_status,
            "BackupLocation": backup_location,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "BackupMode": backup_mode}
        return self._handle_request(api_request).result

    def describe_backup_policy(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            compress_type=None,
            db_instance_id=None,
            owner_id=None,
            backup_policy_mode=None):
        api_request = APIRequest('DescribeBackupPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "CompressType": compress_type,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "BackupPolicyMode": backup_policy_mode}
        return self._handle_request(api_request).result

    def describe_accounts(
            self,
            resource_owner_id=None,
            account_name=None,
            resource_owner_account=None,
            owner_account=None,
            page_size=None,
            db_instance_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeAccounts', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def descibe_imports_from_database(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            page_number=None,
            import_id=None,
            engine=None,
            page_size=None,
            db_instance_id=None):
        api_request = APIRequest('DescibeImportsFromDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "ImportId": import_id,
            "Engine": engine,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id}
        return self._handle_request(api_request).result

    def delete_db_instance(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_database(
            self,
            resource_owner_id=None,
            db_name=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_account(
            self,
            resource_owner_id=None,
            account_name=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_temp_db_instance(
            self,
            resource_owner_id=None,
            restore_time=None,
            resource_owner_account=None,
            backup_id=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('CreateTempDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "RestoreTime": restore_time,
            "ResourceOwnerAccount": resource_owner_account,
            "BackupId": backup_id,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_database(
            self,
            resource_owner_id=None,
            db_name=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            db_description=None,
            owner_id=None,
            character_set_name=None):
        api_request = APIRequest('CreateDatabase', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "DBDescription": db_description,
            "OwnerId": owner_id,
            "CharacterSetName": character_set_name}
        return self._handle_request(api_request).result

    def create_backup(
            self,
            backup_method=None,
            resource_owner_id=None,
            backup_strategy=None,
            db_name=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            backup_type=None):
        api_request = APIRequest('CreateBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "BackupMethod": backup_method,
            "ResourceOwnerId": resource_owner_id,
            "BackupStrategy": backup_strategy,
            "DBName": db_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "BackupType": backup_type}
        return self._handle_request(api_request).result

    def create_account(
            self,
            resource_owner_id=None,
            account_password=None,
            account_name=None,
            resource_owner_account=None,
            owner_account=None,
            account_type=None,
            db_instance_id=None,
            owner_id=None,
            account_description=None):
        api_request = APIRequest('CreateAccount', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountPassword": account_password,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AccountType": account_type,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "AccountDescription": account_description}
        return self._handle_request(api_request).result

    def check_account_name_available(
            self,
            resource_owner_id=None,
            account_name=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('CheckAccountNameAvailable', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AccountName": account_name,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def cancel_import(
            self,
            resource_owner_id=None,
            import_id=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('CancelImport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ImportId": import_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_tags_to_resource(
            self,
            tag4value=None,
            resource_owner_id=None,
            tag2key=None,
            tag5key=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            tag3key=None,
            owner_id=None,
            tag5value=None,
            tags=None,
            tag1key=None,
            tag1value=None,
            region_id=None,
            tag2value=None,
            tag4key=None,
            db_instance_id=None,
            tag3value=None,
            proxy_id=None):
        api_request = APIRequest('AddTagsToResource', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Tag.4.value": tag4value,
            "ResourceOwnerId": resource_owner_id,
            "Tag.2.key": tag2key,
            "Tag.5.key": tag5key,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "Tag.3.key": tag3key,
            "OwnerId": owner_id,
            "Tag.5.value": tag5value,
            "Tags": tags,
            "Tag.1.key": tag1key,
            "Tag.1.value": tag1value,
            "RegionId": region_id,
            "Tag.2.value": tag2value,
            "Tag.4.key": tag4key,
            "DBInstanceId": db_instance_id,
            "Tag.3.value": tag3value,
            "proxyId": proxy_id}
        return self._handle_request(api_request).result

    def switch_db_instance_net_type(
            self,
            resource_owner_id=None,
            connection_string_prefix=None,
            connection_string_type=None,
            resource_owner_account=None,
            client_token=None,
            port=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('SwitchDBInstanceNetType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ConnectionStringPrefix": connection_string_prefix,
            "ConnectionStringType": connection_string_type,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "Port": port,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def release_instance_public_connection(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            current_connection_string=None):
        api_request = APIRequest('ReleaseInstancePublicConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "CurrentConnectionString": current_connection_string}
        return self._handle_request(api_request).result

    def modify_db_instance_network_type(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            vswitch_id=None,
            private_ip_address=None,
            retain_classic=None,
            classic_expired_days=None,
            vpc_id=None,
            db_instance_id=None,
            read_write_splitting_private_ip_address=None,
            instance_network_type=None,
            read_write_splitting_classic_expired_days=None):
        api_request = APIRequest('ModifyDBInstanceNetworkType', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "RetainClassic": retain_classic,
            "ClassicExpiredDays": classic_expired_days,
            "VPCId": vpc_id,
            "DBInstanceId": db_instance_id,
            "ReadWriteSplittingPrivateIpAddress": read_write_splitting_private_ip_address,
            "InstanceNetworkType": instance_network_type,
            "ReadWriteSplittingClassicExpiredDays": read_write_splitting_classic_expired_days}
        return self._handle_request(api_request).result

    def modify_db_instance_connection_string(
            self,
            resource_owner_id=None,
            connection_string_prefix=None,
            resource_owner_account=None,
            port=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None,
            current_connection_string=None):
        api_request = APIRequest('ModifyDBInstanceConnectionString', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ConnectionStringPrefix": connection_string_prefix,
            "ResourceOwnerAccount": resource_owner_account,
            "Port": port,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id,
            "CurrentConnectionString": current_connection_string}
        return self._handle_request(api_request).result

    def modify_db_instance_connection_mode(
            self,
            connection_mode=None,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('ModifyDBInstanceConnectionMode', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ConnectionMode": connection_mode,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_instance_net_info(
            self,
            resource_owner_id=None,
            flag=None,
            db_instance_net_rw_split_type=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceNetInfo', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Flag": flag,
            "DBInstanceNetRWSplitType": db_instance_net_rw_split_type,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_read_only_db_instance(
            self,
            resource_owner_id=None,
            db_instance_storage=None,
            resource_owner_account=None,
            client_token=None,
            owner_account=None,
            engine_version=None,
            owner_id=None,
            db_instance_class=None,
            vswitch_id=None,
            private_ip_address=None,
            resource_group_id=None,
            region_id=None,
            vpc_id=None,
            zone_id=None,
            db_instance_id=None,
            db_instance_description=None,
            db_instance_storage_type=None,
            category=None,
            pay_type=None,
            instance_network_type=None):
        api_request = APIRequest('CreateReadOnlyDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "ResourceOwnerAccount": resource_owner_account,
            "ClientToken": client_token,
            "OwnerAccount": owner_account,
            "EngineVersion": engine_version,
            "OwnerId": owner_id,
            "DBInstanceClass": db_instance_class,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "VPCId": vpc_id,
            "ZoneId": zone_id,
            "DBInstanceId": db_instance_id,
            "DBInstanceDescription": db_instance_description,
            "DBInstanceStorageType": db_instance_storage_type,
            "Category": category,
            "PayType": pay_type,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def create_db_instance(
            self,
            connection_mode=None,
            resource_owner_id=None,
            db_instance_storage=None,
            system_db_charset=None,
            client_token=None,
            zone_id_slave1=None,
            zone_id_slave2=None,
            engine_version=None,
            resource_group_id=None,
            region_id=None,
            engine=None,
            db_instance_description=None,
            db_instance_storage_type=None,
            business_info=None,
            db_instance_net_type=None,
            period=None,
            resource_owner_account=None,
            owner_account=None,
            encryption_key=None,
            owner_id=None,
            used_time=None,
            db_instance_class=None,
            security_ip_list=None,
            vswitch_id=None,
            private_ip_address=None,
            auto_renew=None,
            role_arn=None,
            vpc_id=None,
            tunnel_id=None,
            zone_id=None,
            category=None,
            pay_type=None,
            instance_network_type=None):
        api_request = APIRequest('CreateDBInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ConnectionMode": connection_mode,
            "ResourceOwnerId": resource_owner_id,
            "DBInstanceStorage": db_instance_storage,
            "SystemDBCharset": system_db_charset,
            "ClientToken": client_token,
            "ZoneIdSlave1": zone_id_slave1,
            "ZoneIdSlave2": zone_id_slave2,
            "EngineVersion": engine_version,
            "ResourceGroupId": resource_group_id,
            "RegionId": region_id,
            "Engine": engine,
            "DBInstanceDescription": db_instance_description,
            "DBInstanceStorageType": db_instance_storage_type,
            "BusinessInfo": business_info,
            "DBInstanceNetType": db_instance_net_type,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EncryptionKey": encryption_key,
            "OwnerId": owner_id,
            "UsedTime": used_time,
            "DBInstanceClass": db_instance_class,
            "SecurityIPList": security_ip_list,
            "VSwitchId": vswitch_id,
            "PrivateIpAddress": private_ip_address,
            "AutoRenew": auto_renew,
            "RoleARN": role_arn,
            "VPCId": vpc_id,
            "TunnelId": tunnel_id,
            "ZoneId": zone_id,
            "Category": category,
            "PayType": pay_type,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def allocate_instance_public_connection(
            self,
            resource_owner_id=None,
            connection_string_prefix=None,
            resource_owner_account=None,
            port=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('AllocateInstancePublicConnection', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ConnectionStringPrefix": connection_string_prefix,
            "ResourceOwnerAccount": resource_owner_account,
            "Port": port,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_db_instances_by_performance(
            self,
            tag4value=None,
            resource_owner_id=None,
            tag2key=None,
            client_token=None,
            tag3key=None,
            page_number=None,
            tag1value=None,
            sort_key=None,
            region_id=None,
            page_size=None,
            db_instance_id=None,
            tag3value=None,
            proxy_id=None,
            tag5key=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            tag5value=None,
            tags=None,
            tag1key=None,
            sort_method=None,
            tag2value=None,
            tag4key=None):
        api_request = APIRequest('DescribeDBInstancesByPerformance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Tag.4.value": tag4value,
            "ResourceOwnerId": resource_owner_id,
            "Tag.2.key": tag2key,
            "ClientToken": client_token,
            "Tag.3.key": tag3key,
            "PageNumber": page_number,
            "Tag.1.value": tag1value,
            "SortKey": sort_key,
            "RegionId": region_id,
            "PageSize": page_size,
            "DBInstanceId": db_instance_id,
            "Tag.3.value": tag3value,
            "proxyId": proxy_id,
            "Tag.5.key": tag5key,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tag.5.value": tag5value,
            "Tags": tags,
            "Tag.1.key": tag1key,
            "SortMethod": sort_method,
            "Tag.2.value": tag2value,
            "Tag.4.key": tag4key}
        return self._handle_request(api_request).result

    def describe_db_instances_by_expire_time(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            page_number=None,
            tags=None,
            expired=None,
            region_id=None,
            page_size=None,
            expire_period=None,
            proxy_id=None):
        api_request = APIRequest('DescribeDBInstancesByExpireTime', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "Tags": tags,
            "Expired": expired,
            "RegionId": region_id,
            "PageSize": page_size,
            "ExpirePeriod": expire_period,
            "proxyId": proxy_id}
        return self._handle_request(api_request).result

    def describe_db_instances(
            self,
            connection_mode=None,
            tag4value=None,
            resource_owner_id=None,
            tag2key=None,
            client_token=None,
            search_key=None,
            tag3key=None,
            engine_version=None,
            page_number=None,
            tag1value=None,
            resource_group_id=None,
            expired=None,
            engine=None,
            region_id=None,
            page_size=None,
            db_instance_status=None,
            db_instance_id=None,
            tag3value=None,
            proxy_id=None,
            tag5key=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            tag5value=None,
            db_instance_type=None,
            db_instance_class=None,
            tags=None,
            vswitch_id=None,
            tag1key=None,
            vpc_id=None,
            tag2value=None,
            zone_id=None,
            tag4key=None,
            pay_type=None,
            instance_network_type=None):
        api_request = APIRequest('DescribeDBInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ConnectionMode": connection_mode,
            "Tag.4.value": tag4value,
            "ResourceOwnerId": resource_owner_id,
            "Tag.2.key": tag2key,
            "ClientToken": client_token,
            "SearchKey": search_key,
            "Tag.3.key": tag3key,
            "EngineVersion": engine_version,
            "PageNumber": page_number,
            "Tag.1.value": tag1value,
            "ResourceGroupId": resource_group_id,
            "Expired": expired,
            "Engine": engine,
            "RegionId": region_id,
            "PageSize": page_size,
            "DBInstanceStatus": db_instance_status,
            "DBInstanceId": db_instance_id,
            "Tag.3.value": tag3value,
            "proxyId": proxy_id,
            "Tag.5.key": tag5key,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Tag.5.value": tag5value,
            "DBInstanceType": db_instance_type,
            "DBInstanceClass": db_instance_class,
            "Tags": tags,
            "VSwitchId": vswitch_id,
            "Tag.1.key": tag1key,
            "VpcId": vpc_id,
            "Tag.2.value": tag2value,
            "ZoneId": zone_id,
            "Tag.4.key": tag4key,
            "PayType": pay_type,
            "InstanceNetworkType": instance_network_type}
        return self._handle_request(api_request).result

    def describe_db_instance_attribute(
            self,
            resource_group_id=None,
            resource_owner_id=None,
            expired=None,
            resource_owner_account=None,
            owner_account=None,
            db_instance_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeDBInstanceAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceGroupId": resource_group_id,
            "ResourceOwnerId": resource_owner_id,
            "Expired": expired,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "DBInstanceId": db_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result
