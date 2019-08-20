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


class SmartagClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Smartag'
        self.api_version = '2018-03-13'
        self.location_service_code = 'smartag'
        self.location_endpoint_type = 'openAPI'

    def describe_bindable_smart_access_gateways(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            cross_account=None,
            owner_account=None,
            ccn_id=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeBindableSmartAccessGateways',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "CrossAccount": cross_account,
            "OwnerAccount": owner_account,
            "CcnId": ccn_id,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_unbind_flow_log_sags(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeUnbindFlowLogSags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_sag_remote_access(
            self,
            resource_owner_id=None,
            serial_number=None,
            resource_owner_account=None,
            owner_account=None,
            remote_access_ip=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('ModifySagRemoteAccess', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SerialNumber": serial_number,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "RemoteAccessIp": remote_access_ip,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def associate_qos(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            qos_id=None):
        api_request = APIRequest('AssociateQos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "QosId": qos_id}
        return self._handle_request(api_request).result

    def disassociate_qos(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            qos_id=None):
        api_request = APIRequest('DisassociateQos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "QosId": qos_id}
        return self._handle_request(api_request).result

    def modify_smart_access_gateway_up_bandwidth(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            up_bandwidth4_g=None,
            smart_ag_id=None,
            up_bandwidth_wan=None,
            owner_id=None):
        api_request = APIRequest('ModifySmartAccessGatewayUpBandwidth',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "UpBandwidth4G": up_bandwidth4_g,
            "SmartAGId": smart_ag_id,
            "UpBandwidthWan": up_bandwidth_wan,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def deactive_flow_log(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            flow_log_id=None):
        api_request = APIRequest('DeactiveFlowLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id}
        return self._handle_request(api_request).result

    def associate_flow_log(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            flow_log_id=None):
        api_request = APIRequest('AssociateFlowLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id}
        return self._handle_request(api_request).result

    def describe_flow_log_sags(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            flow_log_id=None,
            page_number=None):
        api_request = APIRequest('DescribeFlowLogSags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def active_flow_log(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            flow_log_id=None):
        api_request = APIRequest('ActiveFlowLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id}
        return self._handle_request(api_request).result

    def delete_flow_log(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            flow_log_id=None):
        api_request = APIRequest('DeleteFlowLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id}
        return self._handle_request(api_request).result

    def describe_flow_logs(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            description=None,
            owner_id=None,
            page_number=None,
            region_id=None,
            page_size=None,
            output_type=None,
            flow_log_id=None,
            flow_log_name=None,
            status=None):
        api_request = APIRequest('DescribeFlowLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "RegionId": region_id,
            "PageSize": page_size,
            "OutputType": output_type,
            "FlowLogId": flow_log_id,
            "FlowLogName": flow_log_name,
            "Status": status}
        return self._handle_request(api_request).result

    def modify_flow_log_attribute(
            self,
            resource_owner_id=None,
            project_name=None,
            logstore_name=None,
            resource_owner_account=None,
            owner_account=None,
            netflow_server_port=None,
            netflow_version=None,
            description=None,
            owner_id=None,
            inactive_aging=None,
            netflow_server_ip=None,
            region_id=None,
            name=None,
            sls_region_id=None,
            active_aging=None,
            output_type=None,
            flow_log_id=None):
        api_request = APIRequest('ModifyFlowLogAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ProjectName": project_name,
            "LogstoreName": logstore_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "NetflowServerPort": netflow_server_port,
            "NetflowVersion": netflow_version,
            "Description": description,
            "OwnerId": owner_id,
            "InactiveAging": inactive_aging,
            "NetflowServerIp": netflow_server_ip,
            "RegionId": region_id,
            "Name": name,
            "SlsRegionId": sls_region_id,
            "ActiveAging": active_aging,
            "OutputType": output_type,
            "FlowLogId": flow_log_id}
        return self._handle_request(api_request).result

    def create_flow_log(
            self,
            resource_owner_id=None,
            project_name=None,
            logstore_name=None,
            resource_owner_account=None,
            owner_account=None,
            netflow_server_port=None,
            netflow_version=None,
            description=None,
            owner_id=None,
            inactive_aging=None,
            netflow_server_ip=None,
            region_id=None,
            name=None,
            sls_region_id=None,
            active_aging=None,
            output_type=None):
        api_request = APIRequest('CreateFlowLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ProjectName": project_name,
            "LogstoreName": logstore_name,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "NetflowServerPort": netflow_server_port,
            "NetflowVersion": netflow_version,
            "Description": description,
            "OwnerId": owner_id,
            "InactiveAging": inactive_aging,
            "NetflowServerIp": netflow_server_ip,
            "RegionId": region_id,
            "Name": name,
            "SlsRegionId": sls_region_id,
            "ActiveAging": active_aging,
            "OutputType": output_type}
        return self._handle_request(api_request).result

    def disassociate_flow_log(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            flow_log_id=None):
        api_request = APIRequest('DisassociateFlowLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "FlowLogId": flow_log_id}
        return self._handle_request(api_request).result

    def describe_grant_sag_rules(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            smart_ag_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeGrantSagRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def grant_sag_instance_to_ccn(
            self,
            resource_owner_id=None,
            ccn_uid=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            ccn_instance_id=None,
            owner_id=None):
        api_request = APIRequest('GrantSagInstanceToCcn', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "CcnUid": ccn_uid,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "CcnInstanceId": ccn_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def revoke_sag_instance_from_ccn(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            ccn_instance_id=None,
            owner_id=None):
        api_request = APIRequest('RevokeSagInstanceFromCcn', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "CcnInstanceId": ccn_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_smart_access_gateway_attribute(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeSmartAccessGatewayAttribute',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_qoses(
            self,
            resource_owner_id=None,
            qos_name=None,
            resource_owner_account=None,
            region_id=None,
            qos_ids=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeQoses', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "QosName": qos_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "QosIds": qos_ids,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_qos(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            qos_id=None):
        api_request = APIRequest('DeleteQos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "QosId": qos_id}
        return self._handle_request(api_request).result

    def create_qos(
            self,
            resource_owner_id=None,
            qos_name=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CreateQos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "QosName": qos_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_qos(
            self,
            resource_owner_id=None,
            qos_name=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            qos_id=None):
        api_request = APIRequest('ModifyQos', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "QosName": qos_name,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "QosId": qos_id}
        return self._handle_request(api_request).result

    def create_qos_policy(
            self,
            resource_owner_id=None,
            source_port_range=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            source_cidr=None,
            description=None,
            end_time=None,
            start_time=None,
            owner_id=None,
            priority=None,
            dest_cidr=None,
            dest_port_range=None,
            region_id=None,
            qos_id=None):
        api_request = APIRequest('CreateQosPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourcePortRange": source_port_range,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "SourceCidr": source_cidr,
            "Description": description,
            "EndTime": end_time,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "Priority": priority,
            "DestCidr": dest_cidr,
            "DestPortRange": dest_port_range,
            "RegionId": region_id,
            "QosId": qos_id}
        return self._handle_request(api_request).result

    def delete_qos_policy(
            self,
            resource_owner_id=None,
            qos_policy_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            qos_id=None):
        api_request = APIRequest('DeleteQosPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "QosPolicyId": qos_policy_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "QosId": qos_id}
        return self._handle_request(api_request).result

    def modify_qos_policy(
            self,
            resource_owner_id=None,
            source_port_range=None,
            qos_policy_id=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            source_cidr=None,
            end_time=None,
            description=None,
            start_time=None,
            owner_id=None,
            priority=None,
            dest_cidr=None,
            dest_port_range=None,
            region_id=None,
            qos_id=None):
        api_request = APIRequest('ModifyQosPolicy', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SourcePortRange": source_port_range,
            "QosPolicyId": qos_policy_id,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "SourceCidr": source_cidr,
            "EndTime": end_time,
            "Description": description,
            "StartTime": start_time,
            "OwnerId": owner_id,
            "Priority": priority,
            "DestCidr": dest_cidr,
            "DestPortRange": dest_port_range,
            "RegionId": region_id,
            "QosId": qos_id}
        return self._handle_request(api_request).result

    def modify_qos_car(
            self,
            max_bandwidth_abs=None,
            resource_owner_id=None,
            resource_owner_account=None,
            min_bandwidth_abs=None,
            max_bandwidth_percent=None,
            owner_account=None,
            description=None,
            owner_id=None,
            qos_car_id=None,
            priority=None,
            min_bandwidth_percent=None,
            limit_type=None,
            region_id=None,
            percent_source_type=None,
            qos_id=None):
        api_request = APIRequest('ModifyQosCar', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MaxBandwidthAbs": max_bandwidth_abs,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "MinBandwidthAbs": min_bandwidth_abs,
            "MaxBandwidthPercent": max_bandwidth_percent,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "QosCarId": qos_car_id,
            "Priority": priority,
            "MinBandwidthPercent": min_bandwidth_percent,
            "LimitType": limit_type,
            "RegionId": region_id,
            "PercentSourceType": percent_source_type,
            "QosId": qos_id}
        return self._handle_request(api_request).result

    def delete_qos_car(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            qos_id=None,
            qos_car_id=None):
        api_request = APIRequest('DeleteQosCar', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "QosId": qos_id,
            "QosCarId": qos_car_id}
        return self._handle_request(api_request).result

    def create_qos_car(
            self,
            max_bandwidth_abs=None,
            resource_owner_id=None,
            resource_owner_account=None,
            min_bandwidth_abs=None,
            max_bandwidth_percent=None,
            owner_account=None,
            description=None,
            owner_id=None,
            priority=None,
            min_bandwidth_percent=None,
            limit_type=None,
            region_id=None,
            percent_source_type=None,
            qos_id=None):
        api_request = APIRequest('CreateQosCar', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MaxBandwidthAbs": max_bandwidth_abs,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "MinBandwidthAbs": min_bandwidth_abs,
            "MaxBandwidthPercent": max_bandwidth_percent,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "Priority": priority,
            "MinBandwidthPercent": min_bandwidth_percent,
            "LimitType": limit_type,
            "RegionId": region_id,
            "PercentSourceType": percent_source_type,
            "QosId": qos_id}
        return self._handle_request(api_request).result

    def describe_qos_policies(
            self,
            resource_owner_id=None,
            qos_policy_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            description=None,
            owner_id=None,
            qos_id=None,
            page_number=None,
            order=None):
        api_request = APIRequest('DescribeQosPolicies', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "QosPolicyId": qos_policy_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "Description": description,
            "OwnerId": owner_id,
            "QosId": qos_id,
            "PageNumber": page_number,
            "Order": order}
        return self._handle_request(api_request).result

    def describe_qos_cars(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            description=None,
            owner_id=None,
            qos_id=None,
            qos_car_id=None,
            page_number=None,
            order=None):
        api_request = APIRequest('DescribeQosCars', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "Description": description,
            "OwnerId": owner_id,
            "QosId": qos_id,
            "QosCarId": qos_car_id,
            "PageNumber": page_number,
            "Order": order}
        return self._handle_request(api_request).result

    def describe_smart_access_gateway_routes(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            smart_ag_id=None,
            owner_id=None,
            page_nubmer=None):
        api_request = APIRequest('DescribeSmartAccessGatewayRoutes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "PageNubmer": page_nubmer}
        return self._handle_request(api_request).result

    def describe_snat_entries(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            smart_ag_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeSnatEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_snat_entry(
            self,
            resource_owner_id=None,
            instance_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteSnatEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "InstanceId": instance_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_snat_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            cidr_block=None,
            smart_ag_id=None,
            owner_id=None,
            snat_ip=None):
        api_request = APIRequest('AddSnatEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "CidrBlock": cidr_block,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "SnatIp": snat_ip}
        return self._handle_request(api_request).result

    def delete_dnat_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            sag_id=None,
            owner_account=None,
            owner_id=None,
            dnat_entry_id=None):
        api_request = APIRequest('DeleteDnatEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "SagId": sag_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "DnatEntryId": dnat_entry_id}
        return self._handle_request(api_request).result

    def add_dnat_entry(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            owner_id=None,
            type_=None,
            internal_ip=None,
            region_id=None,
            sag_id=None,
            internal_port=None,
            external_ip=None,
            external_port=None):
        api_request = APIRequest('AddDnatEntry', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Type": type_,
            "InternalIp": internal_ip,
            "RegionId": region_id,
            "SagId": sag_id,
            "InternalPort": internal_port,
            "ExternalIp": external_ip,
            "ExternalPort": external_port}
        return self._handle_request(api_request).result

    def describe_dnat_entries(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            sag_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            type_=None,
            page_number=None):
        api_request = APIRequest('DescribeDnatEntries', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "SagId": sag_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "Type": type_,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def bind_vbr(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            vbr_id=None,
            vbr_region_id=None):
        api_request = APIRequest('BindVbr', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "VbrId": vbr_id,
            "VbrRegionId": vbr_region_id}
        return self._handle_request(api_request).result

    def unbind_vbr(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            vbr_id=None,
            vbr_region_id=None):
        api_request = APIRequest('UnbindVbr', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "VbrId": vbr_id,
            "VbrRegionId": vbr_region_id}
        return self._handle_request(api_request).result

    def enable_smart_access_gateway_user(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            user_name=None):
        api_request = APIRequest('EnableSmartAccessGatewayUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def disable_smart_access_gateway_user(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            user_name=None):
        api_request = APIRequest('DisableSmartAccessGatewayUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def create_smart_access_gateway_software(
            self,
            resource_owner_id=None,
            period=None,
            auto_pay=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            user_count=None,
            charge_type=None,
            owner_id=None,
            data_plan=None):
        api_request = APIRequest('CreateSmartAccessGatewaySoftware', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Period": period,
            "AutoPay": auto_pay,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "UserCount": user_count,
            "ChargeType": charge_type,
            "OwnerId": owner_id,
            "DataPlan": data_plan}
        return self._handle_request(api_request).result

    def describe_network_optimizations(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            network_opt_id=None,
            owner_account=None,
            ccn_id=None,
            name=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeNetworkOptimizations', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NetworkOptId": network_opt_id,
            "OwnerAccount": owner_account,
            "CcnId": ccn_id,
            "Name": name,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def add_network_optimization_setting(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            network_opt_id=None,
            owner_account=None,
            domain=None,
            owner_id=None,
            type_=None):
        api_request = APIRequest('AddNetworkOptimizationSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NetworkOptId": network_opt_id,
            "OwnerAccount": owner_account,
            "Domain": domain,
            "OwnerId": owner_id,
            "Type": type_}
        return self._handle_request(api_request).result

    def attach_network_optimization_sags(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            network_opt_id=None,
            owner_account=None,
            list_of_smart_ag_ids=None,
            owner_id=None):
        api_request = APIRequest('AttachNetworkOptimizationSags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NetworkOptId": network_opt_id,
            "OwnerAccount": owner_account,
            "SmartAGIds": list_of_smart_ag_ids,
            "OwnerId": owner_id}
        repeat_info = {"SmartAGIds": ('SmartAGIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_network_optimization_setting(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            network_opt_id=None,
            owner_account=None,
            domain=None,
            owner_id=None,
            type_=None):
        api_request = APIRequest('DeleteNetworkOptimizationSetting', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NetworkOptId": network_opt_id,
            "OwnerAccount": owner_account,
            "Domain": domain,
            "OwnerId": owner_id,
            "Type": type_}
        return self._handle_request(api_request).result

    def describe_network_optimization_sags(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            network_opt_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeNetworkOptimizationSags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NetworkOptId": network_opt_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def detach_network_optimization_sags(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            network_opt_id=None,
            owner_account=None,
            list_of_smart_ag_ids=None,
            owner_id=None):
        api_request = APIRequest('DetachNetworkOptimizationSags', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NetworkOptId": network_opt_id,
            "OwnerAccount": owner_account,
            "SmartAGIds": list_of_smart_ag_ids,
            "OwnerId": owner_id}
        repeat_info = {"SmartAGIds": ('SmartAGIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def modify_network_optimization(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            network_opt_id=None,
            owner_account=None,
            name=None,
            owner_id=None):
        api_request = APIRequest('ModifyNetworkOptimization', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NetworkOptId": network_opt_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_network_optimization_settings(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            network_opt_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeNetworkOptimizationSettings',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NetworkOptId": network_opt_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_network_optimization(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            network_opt_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteNetworkOptimization', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "NetworkOptId": network_opt_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def kick_out_clients(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            username=None):
        api_request = APIRequest('KickOutClients', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "Username": username}
        return self._handle_request(api_request).result

    def set_sag_routeable_address(
            self,
            access_key_id=None,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            sag_id=None,
            owner_account=None,
            owner_id=None,
            routeable_address=None):
        api_request = APIRequest('SetSagRouteableAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "SagId": sag_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "RouteableAddress": routeable_address}
        return self._handle_request(api_request).result

    def clear_sag_routeable_address(
            self,
            access_key_id=None,
            resource_owner_id=None,
            region_id=None,
            resource_owner_account=None,
            sag_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ClearSagRouteableAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "access_key_id": access_key_id,
            "ResourceOwnerId": resource_owner_id,
            "RegionId": region_id,
            "ResourceOwnerAccount": resource_owner_account,
            "SagId": sag_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_sag_routeable_address(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            sag_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeSagRouteableAddress', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "SagId": sag_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_network_optimization(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            ccn_id=None,
            owner_id=None):
        api_request = APIRequest('CreateNetworkOptimization', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "CcnId": ccn_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_smart_access_gateway_client_user(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            user_name=None):
        api_request = APIRequest('DeleteSmartAccessGatewayClientUser',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def reset_smart_access_gateway_client_user_password(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            user_name=None):
        api_request = APIRequest(
            'ResetSmartAccessGatewayClientUserPassword',
            'GET',
            'http',
            'RPC',
            'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def describe_user_flow_statistics(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            statistics_date=None,
            list_of_user_names=None,
            owner_id=None):
        api_request = APIRequest('DescribeUserFlowStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "StatisticsDate": statistics_date,
            "UserNames": list_of_user_names,
            "OwnerId": owner_id}
        repeat_info = {"UserNames": ('UserNames', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_user_online_clients(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            user_name=None):
        api_request = APIRequest('DescribeUserOnlineClients', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def describe_user_online_client_statistics(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            list_of_user_names=None,
            owner_id=None):
        api_request = APIRequest('DescribeUserOnlineClientStatistics',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "UserNames": list_of_user_names,
            "OwnerId": owner_id}
        repeat_info = {"UserNames": ('UserNames', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_sag_online_client_statistics(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            list_of_smart_ag_ids=None,
            owner_id=None):
        api_request = APIRequest('DescribeSagOnlineClientStatistics', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGIds": list_of_smart_ag_ids,
            "OwnerId": owner_id}
        repeat_info = {"SmartAGIds": ('SmartAGIds', 'list', 'str', None),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_smart_access_gateway_client_users(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            smart_ag_id=None,
            owner_id=None,
            page_number=None,
            user_name=None):
        api_request = APIRequest('DescribeSmartAccessGatewayClientUsers',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def modify_smart_access_gateway_client_user(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            bandwidth=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            user_name=None):
        api_request = APIRequest('ModifySmartAccessGatewayClientUser',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def create_smart_access_gateway_client_user(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            bandwidth=None,
            owner_account=None,
            client_ip=None,
            smart_ag_id=None,
            user_mail=None,
            owner_id=None,
            user_name=None):
        api_request = APIRequest('CreateSmartAccessGatewayClientUser',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "Bandwidth": bandwidth,
            "OwnerAccount": owner_account,
            "ClientIp": client_ip,
            "SmartAGId": smart_ag_id,
            "UserMail": user_mail,
            "OwnerId": owner_id,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def modify_serial_number(
            self,
            resource_owner_id=None,
            serial_number=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('ModifySerialNumber', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SerialNumber": serial_number,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_acl(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            owner_id=None):
        api_request = APIRequest('CreateACL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_ac_ls(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            acl_ids=None,
            owner_account=None,
            name=None,
            page_size=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeACLs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "AclIds": acl_ids,
            "OwnerAccount": owner_account,
            "Name": name,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def associate_acl(
            self,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('AssociateACL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def add_acl_rule(
            self,
            acl_id=None,
            resource_owner_id=None,
            source_port_range=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            source_cidr=None,
            description=None,
            owner_id=None,
            priority=None,
            type_=None,
            dest_cidr=None,
            dest_port_range=None,
            region_id=None,
            direction=None,
            policy=None):
        api_request = APIRequest('AddACLRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "SourcePortRange": source_port_range,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "SourceCidr": source_cidr,
            "Description": description,
            "OwnerId": owner_id,
            "Priority": priority,
            "Type": type_,
            "DestCidr": dest_cidr,
            "DestPortRange": dest_port_range,
            "RegionId": region_id,
            "Direction": direction,
            "Policy": policy}
        return self._handle_request(api_request).result

    def disassociate_acl(
            self,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('DisassociateACL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_acl_rule(
            self,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None,
            acr_id=None):
        api_request = APIRequest('DeleteACLRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "AcrId": acr_id}
        return self._handle_request(api_request).result

    def modify_acl_rule(
            self,
            acl_id=None,
            resource_owner_id=None,
            source_port_range=None,
            resource_owner_account=None,
            ip_protocol=None,
            owner_account=None,
            source_cidr=None,
            description=None,
            owner_id=None,
            priority=None,
            type_=None,
            acr_id=None,
            dest_cidr=None,
            dest_port_range=None,
            region_id=None,
            direction=None,
            policy=None):
        api_request = APIRequest('ModifyACLRule', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "SourcePortRange": source_port_range,
            "ResourceOwnerAccount": resource_owner_account,
            "IpProtocol": ip_protocol,
            "OwnerAccount": owner_account,
            "SourceCidr": source_cidr,
            "Description": description,
            "OwnerId": owner_id,
            "Priority": priority,
            "Type": type_,
            "AcrId": acr_id,
            "DestCidr": dest_cidr,
            "DestPortRange": dest_port_range,
            "RegionId": region_id,
            "Direction": direction,
            "Policy": policy}
        return self._handle_request(api_request).result

    def describe_acl_attribute(
            self,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            owner_id=None,
            page_number=None,
            direction=None,
            order=None):
        api_request = APIRequest('DescribeACLAttribute', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "OwnerId": owner_id,
            "PageNumber": page_number,
            "Direction": direction,
            "Order": order}
        return self._handle_request(api_request).result

    def delete_acl(
            self,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteACL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_acl(
            self,
            acl_id=None,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            owner_id=None):
        api_request = APIRequest('ModifyACL', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AclId": acl_id,
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def unicom_order_confirm(
            self,
            tms_code=None,
            resource_owner_id=None,
            list_of_order_item=None,
            owner_user_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            order_post_fee=None,
            owner_id=None,
            tms_order_code=None,
            trade_id=None):
        api_request = APIRequest('UnicomOrderConfirm', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TmsCode": tms_code,
            "ResourceOwnerId": resource_owner_id,
            "OrderItem": list_of_order_item,
            "OwnerUserId": owner_user_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OrderPostFee": order_post_fee,
            "OwnerId": owner_id,
            "TmsOrderCode": tms_order_code,
            "TradeId": trade_id}
        repeat_info = {"OrderItem": ('OrderItem',
                                     'list',
                                     'dict',
                                     [('ScItemName',
                                       'str',
                                       None,
                                       None),
                                      ('ItemAmount',
                                       'str',
                                       None,
                                       None),
                                         ('SnList',
                                          'list',
                                          'str',
                                          None),
                                         ('OrderItemId',
                                          'str',
                                          None,
                                          None),
                                         ('ScItemCode',
                                          'str',
                                          None,
                                          None),
                                         ('ItemQuantity',
                                          'str',
                                          None,
                                          None),
                                         ('TradeId',
                                          'str',
                                          None,
                                          None),
                                         ('TradeItemId',
                                          'str',
                                          None,
                                          None),
                                      ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def unicom_sign_confirm(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            list_of_tms_order=None,
            owner_id=None):
        api_request = APIRequest('UnicomSignConfirm', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "TmsOrder": list_of_tms_order,
            "OwnerId": owner_id}
        repeat_info = {"TmsOrder": ('TmsOrder',
                                    'list',
                                    'dict',
                                    [('TmsCode',
                                      'str',
                                      None,
                                      None),
                                     ('SigningTime',
                                      'str',
                                      None,
                                      None),
                                        ('TmsOrderCode',
                                         'str',
                                         None,
                                         None),
                                        ('TradeId',
                                         'str',
                                         None,
                                         None),
                                     ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def downgrade_smart_access_gateway(
            self,
            resource_owner_id=None,
            auto_pay=None,
            band_width_spec=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            user_count=None,
            smart_ag_id=None,
            owner_id=None,
            data_plan=None):
        api_request = APIRequest('DowngradeSmartAccessGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "BandWidthSpec": band_width_spec,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "UserCount": user_count,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "DataPlan": data_plan}
        return self._handle_request(api_request).result

    def upgrade_smart_access_gateway(
            self,
            resource_owner_id=None,
            auto_pay=None,
            band_width_spec=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            user_count=None,
            smart_ag_id=None,
            owner_id=None,
            data_plan=None):
        api_request = APIRequest('UpgradeSmartAccessGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "AutoPay": auto_pay,
            "BandWidthSpec": band_width_spec,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "UserCount": user_count,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "DataPlan": data_plan}
        return self._handle_request(api_request).result

    def describe_grant_rules(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            page_size=None,
            associated_ccn_id=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeGrantRules', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "PageSize": page_size,
            "AssociatedCcnId": associated_ccn_id,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def grant_instance_to_cbn(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            cen_uid=None,
            cen_instance_id=None,
            owner_account=None,
            ccn_instance_id=None,
            owner_id=None):
        api_request = APIRequest('GrantInstanceToCbn', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "CenUid": cen_uid,
            "CenInstanceId": cen_instance_id,
            "OwnerAccount": owner_account,
            "CcnInstanceId": ccn_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def revoke_instance_from_cbn(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            cen_instance_id=None,
            owner_account=None,
            ccn_instance_id=None,
            owner_id=None):
        api_request = APIRequest('RevokeInstanceFromCbn', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "CenInstanceId": cen_instance_id,
            "OwnerAccount": owner_account,
            "CcnInstanceId": ccn_instance_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_sag_link_level_ha(
            self,
            resource_owner_id=None,
            backup_link_id=None,
            resource_owner_account=None,
            ha_type=None,
            owner_account=None,
            main_link_region_id=None,
            smart_ag_id=None,
            owner_id=None,
            main_link_id=None,
            backup_link_region_id=None):
        api_request = APIRequest('CreateSAGLinkLevelHa', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "BackupLinkId": backup_link_id,
            "ResourceOwnerAccount": resource_owner_account,
            "HaType": ha_type,
            "OwnerAccount": owner_account,
            "MainLinkRegionId": main_link_region_id,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "MainLinkId": main_link_id,
            "BackupLinkRegionId": backup_link_region_id}
        return self._handle_request(api_request).result

    def switch_sag_ha_state(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            ha_type=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('SwitchSAGHaState', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "HaType": ha_type,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_sag_link_level_ha(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            ha_type=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteSAGLinkLevelHa', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "HaType": ha_type,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_dedicated_line_backup(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteDedicatedLineBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_dedicated_line_backup(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            vbr_id=None,
            vbr_region_id=None):
        api_request = APIRequest('CreateDedicatedLineBackup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "VbrId": vbr_id,
            "VbrRegionId": vbr_region_id}
        return self._handle_request(api_request).result

    def describe_smart_access_gateway_ha(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeSmartAccessGatewayHa', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def switch_cloud_box_ha_state(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('SwitchCloudBoxHaState', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def reboot_smart_access_gateway(
            self,
            resource_owner_id=None,
            serial_number=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('RebootSmartAccessGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SerialNumber": serial_number,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_smart_access_gateway(
            self,
            max_band_width=None,
            resource_owner_id=None,
            description=None,
            receiver_town=None,
            receiver_district=None,
            region_id=None,
            user_count=None,
            receiver_address=None,
            instance_type=None,
            buyer_message=None,
            hard_ware_spec=None,
            receiver_email=None,
            receiver_state=None,
            receiver_city=None,
            period=None,
            auto_pay=None,
            receiver_mobile=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            receiver_phone=None,
            receiver_name=None,
            ha_type=None,
            name=None,
            receiver_country=None,
            charge_type=None,
            data_plan=None,
            receiver_zip=None):
        api_request = APIRequest('CreateSmartAccessGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "MaxBandWidth": max_band_width,
            "ResourceOwnerId": resource_owner_id,
            "Description": description,
            "ReceiverTown": receiver_town,
            "ReceiverDistrict": receiver_district,
            "RegionId": region_id,
            "UserCount": user_count,
            "ReceiverAddress": receiver_address,
            "InstanceType": instance_type,
            "BuyerMessage": buyer_message,
            "HardWareSpec": hard_ware_spec,
            "ReceiverEmail": receiver_email,
            "ReceiverState": receiver_state,
            "ReceiverCity": receiver_city,
            "Period": period,
            "AutoPay": auto_pay,
            "ReceiverMobile": receiver_mobile,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "ReceiverPhone": receiver_phone,
            "ReceiverName": receiver_name,
            "HaType": ha_type,
            "Name": name,
            "ReceiverCountry": receiver_country,
            "ChargeType": charge_type,
            "DataPlan": data_plan,
            "ReceiverZip": receiver_zip}
        return self._handle_request(api_request).result

    def activate_smart_access_gateway(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('ActivateSmartAccessGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def unlock_smart_access_gateway(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('UnlockSmartAccessGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def bind_smart_access_gateway(
            self,
            resource_owner_id=None,
            smart_ag_uid=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            ccn_id=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('BindSmartAccessGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SmartAGUid": smart_ag_uid,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "CcnId": ccn_id,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_cloud_connect_network(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            cidr_block=None,
            description=None,
            snat_cidr_block=None,
            is_default=None,
            owner_id=None):
        api_request = APIRequest('CreateCloudConnectNetwork', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "CidrBlock": cidr_block,
            "Description": description,
            "SnatCidrBlock": snat_cidr_block,
            "IsDefault": is_default,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def delete_cloud_connect_network(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            ccn_id=None,
            owner_id=None):
        api_request = APIRequest('DeleteCloudConnectNetwork', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "CcnId": ccn_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_cloud_connect_networks(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            name=None,
            ccn_id=None,
            page_size=None,
            list_of_tag=None,
            owner_id=None,
            page_number=None):
        api_request = APIRequest('DescribeCloudConnectNetworks', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "Name": name,
            "CcnId": ccn_id,
            "PageSize": page_size,
            "Tag": list_of_tag,
            "OwnerId": owner_id,
            "PageNumber": page_number}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Value', 'str', None, None),
                                                       ('Key', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_regions(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            owner_account=None,
            accept_language=None,
            owner_id=None):
        api_request = APIRequest('DescribeRegions', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "AcceptLanguage": accept_language,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_smart_access_gateways(
            self,
            resource_owner_id=None,
            serial_number=None,
            resource_owner_account=None,
            acl_ids=None,
            owner_account=None,
            associated_ccn_id=None,
            owner_id=None,
            unbound_acl_ids=None,
            page_number=None,
            region_id=None,
            name=None,
            page_size=None,
            smart_ag_id=None,
            instance_type=None,
            status=None):
        api_request = APIRequest('DescribeSmartAccessGateways', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SerialNumber": serial_number,
            "ResourceOwnerAccount": resource_owner_account,
            "AclIds": acl_ids,
            "OwnerAccount": owner_account,
            "AssociatedCcnId": associated_ccn_id,
            "OwnerId": owner_id,
            "UnboundAclIds": unbound_acl_ids,
            "PageNumber": page_number,
            "RegionId": region_id,
            "Name": name,
            "PageSize": page_size,
            "SmartAGId": smart_ag_id,
            "InstanceType": instance_type,
            "Status": status}
        return self._handle_request(api_request).result

    def get_cloud_connect_network_use_limit(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('GetCloudConnectNetworkUseLimit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def get_smart_access_gateway_use_limit(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('GetSmartAccessGatewayUseLimit', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def modify_cloud_connect_network(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            ccn_id=None,
            name=None,
            cidr_block=None,
            description=None,
            owner_id=None,
            interworking_status=None):
        api_request = APIRequest('ModifyCloudConnectNetwork', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "CcnId": ccn_id,
            "Name": name,
            "CidrBlock": cidr_block,
            "Description": description,
            "OwnerId": owner_id,
            "InterworkingStatus": interworking_status}
        return self._handle_request(api_request).result

    def modify_smart_access_gateway(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            city=None,
            owner_account=None,
            description=None,
            owner_id=None,
            security_lock_threshold=None,
            routing_strategy=None,
            region_id=None,
            name=None,
            cidr_block=None,
            smart_ag_id=None):
        api_request = APIRequest('ModifySmartAccessGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "City": city,
            "OwnerAccount": owner_account,
            "Description": description,
            "OwnerId": owner_id,
            "SecurityLockThreshold": security_lock_threshold,
            "RoutingStrategy": routing_strategy,
            "RegionId": region_id,
            "Name": name,
            "CidrBlock": cidr_block,
            "SmartAGId": smart_ag_id}
        return self._handle_request(api_request).result

    def unbind_smart_access_gateway(
            self,
            resource_owner_id=None,
            smart_ag_uid=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            ccn_id=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('UnbindSmartAccessGateway', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SmartAGUid": smart_ag_uid,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "CcnId": ccn_id,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_smart_access_gateway_version(
            self,
            resource_owner_id=None,
            serial_number=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None,
            version_code=None):
        api_request = APIRequest('UpdateSmartAccessGatewayVersion', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "SerialNumber": serial_number,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id,
            "VersionCode": version_code}
        return self._handle_request(api_request).result

    def describe_smart_access_gateway_versions(
            self,
            resource_owner_id=None,
            resource_owner_account=None,
            region_id=None,
            owner_account=None,
            smart_ag_id=None,
            owner_id=None):
        api_request = APIRequest('DescribeSmartAccessGatewayVersions',
                                 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ResourceOwnerAccount": resource_owner_account,
            "RegionId": region_id,
            "OwnerAccount": owner_account,
            "SmartAGId": smart_ag_id,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result
