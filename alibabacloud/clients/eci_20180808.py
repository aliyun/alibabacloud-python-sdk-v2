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


class EciClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None):
        AlibabaCloudClient.__init__(self, client_config, credentials_provider)
        self.product_code = 'Eci'
        self.api_version = '2018-08-08'
        self.location_service_code = 'eci'
        self.location_endpoint_type = 'openAPI'

    def describe_multi_container_group_metric(
            self,
            resource_owner_id=None,
            container_group_ids=None,
            resource_group_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeMultiContainerGroupMetric', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ContainerGroupIds": container_group_ids,
            "ResourceGroupId": resource_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def describe_container_group_metric(
            self,
            resource_owner_id=None,
            start_time=None,
            container_group_id=None,
            period=None,
            resource_owner_account=None,
            owner_account=None,
            end_time=None,
            owner_id=None):
        api_request = APIRequest('DescribeContainerGroupMetric', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "StartTime": start_time,
            "ContainerGroupId": container_group_id,
            "Period": period,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "EndTime": end_time,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_container_group_by_template(
            self,
            template=None,
            resource_owner_id=None,
            client_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('UpdateContainerGroupByTemplate', 'POST', 'http', 'RPC', 'body')
        api_request._params = {
            "Template": template,
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_container_group_from_template(
            self,
            template=None,
            resource_owner_id=None,
            client_token=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('CreateContainerGroupFromTemplate', 'POST', 'http', 'RPC', 'body')
        api_request._params = {
            "Template": template,
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def export_container_group_template(
            self,
            resource_owner_id=None,
            container_group_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('ExportContainerGroupTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ContainerGroupId": container_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def restart_container_group(
            self,
            resource_owner_id=None,
            client_token=None,
            container_group_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('RestartContainerGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "ContainerGroupId": container_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def update_container_group(
            self,
            container=None,
            resource_owner_id=None,
            memory=None,
            client_token=None,
            init_container=None,
            image_registry_credential=None,
            tag=None,
            container_group_id=None,
            dns_config_name_server=None,
            resource_owner_account=None,
            restart_policy=None,
            owner_account=None,
            dns_config_option=None,
            cpu=None,
            dns_config_search=None,
            owner_id=None,
            volume=None):
        api_request = APIRequest('UpdateContainerGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Container": container,
            "ResourceOwnerId": resource_owner_id,
            "Memory": memory,
            "ClientToken": client_token,
            "InitContainer": init_container,
            "ImageRegistryCredential": image_registry_credential,
            "Tag": tag,
            "ContainerGroupId": container_group_id,
            "DnsConfig.NameServer": dns_config_name_server,
            "ResourceOwnerAccount": resource_owner_account,
            "RestartPolicy": restart_policy,
            "OwnerAccount": owner_account,
            "DnsConfig.Option": dns_config_option,
            "Cpu": cpu,
            "DnsConfig.Search": dns_config_search,
            "OwnerId": owner_id,
            "Volume": volume}
        repeat_info = {"Container": ('Container', 'list', 'dict', [('Name', 'str', None, None),
                                                                   ('Image', 'str', None, None),
                                                                   ('Cpu', 'str', None, None),
                                                                   ('Memory', 'str', None, None),
                                                                   ('WorkingDir', 'str', None, None),
                                                                   ('ImagePullPolicy', 'str', None, None),
                                                                   ('Stdin', 'str', None, None),
                                                                   ('StdinOnce', 'str', None, None),
                                                                   ('Tty', 'str', None, None),
                                                                   ('Command', 'list', 'str', None),
                                                                   ('Arg', 'list', 'str', None),
                                                                   ('EnvironmentVar', 'list', 'dict', [('Key', 'str', None, None),
                                                                                                       ('Value', 'str', None, None),
                                                                                                       ],),('Port', 'list', 'dict', [('Protocol', 'str', None, None),
                                                                                                                                     ('Port', 'str', None, None),
                                                                                                                                     ],),('VolumeMount', 'list', 'dict', [('Name', 'str', None, None),
                                                                                                                                                                          ('MountPath', 'str', None, None),
                                                                                                                                                                          ('SubPath', 'str', None, None),
                                                                                                                                                                          ('ReadOnly', 'str', None, None),
                                                                                                                                                                          ],),('ReadinessProbe.TcpSocket.Port', 'str', None, None),
                                                                   ('ReadinessProbe.Exec.Command', 'list', 'str', None),
                                                                   ('ReadinessProbe.HttpGet.Path', 'str', None, None),
                                                                   ('ReadinessProbe.HttpGet.Port', 'str', None, None),
                                                                   ('ReadinessProbe.HttpGet.Scheme', 'str', None, None),
                                                                   ('ReadinessProbe.InitialDelaySeconds', 'str', None, None),
                                                                   ('ReadinessProbe.PeriodSeconds', 'str', None, None),
                                                                   ('ReadinessProbe.SuccessThreshold', 'str', None, None),
                                                                   ('ReadinessProbe.FailureThreshold', 'str', None, None),
                                                                   ('ReadinessProbe.TimeoutSeconds', 'str', None, None),
                                                                   ('LivenessProbe.TcpSocket.Port', 'str', None, None),
                                                                   ('LivenessProbe.Exec.Command', 'list', 'str', None),
                                                                   ('LivenessProbe.HttpGet.Path', 'str', None, None),
                                                                   ('LivenessProbe.HttpGet.Port', 'str', None, None),
                                                                   ('LivenessProbe.HttpGet.Scheme', 'str', None, None),
                                                                   ('LivenessProbe.InitialDelaySeconds', 'str', None, None),
                                                                   ('LivenessProbe.PeriodSeconds', 'str', None, None),
                                                                   ('LivenessProbe.SuccessThreshold', 'str', None, None),
                                                                   ('LivenessProbe.FailureThreshold', 'str', None, None),
                                                                   ('LivenessProbe.TimeoutSeconds', 'str', None, None),
                                                                   ('SecurityContext.ReadOnlyRootFilesystem', 'str', None, None),
                                                                   ('SecurityContext.RunAsUser', 'str', None, None),
                                                                   ('SecurityContext.Capability.Add', 'list', 'str', None),
                                                                   ('Gpu', 'str', None, None),
                                                                   ]),
                       "InitContainer": ('InitContainer', 'list', 'dict', [('Name', 'str', None, None),
                                                                           ('Image', 'str', None, None),
                                                                           ('Cpu', 'str', None, None),
                                                                           ('Memory', 'str', None, None),
                                                                           ('WorkingDir', 'str', None, None),
                                                                           ('ImagePullPolicy', 'str', None, None),
                                                                           ('Stdin', 'str', None, None),
                                                                           ('StdinOnce', 'str', None, None),
                                                                           ('Tty', 'str', None, None),
                                                                           ('Command', 'list', 'str', None),
                                                                           ('Arg', 'list', 'str', None),
                                                                           ('EnvironmentVar', 'list', 'dict', [('Key', 'str', None, None),
                                                                                                               ('Value', 'str', None, None),
                                                                                                               ],),('Port', 'list', 'dict', [('Port', 'str', None, None),
                                                                                                                                             ('Protocol', 'str', None, None),
                                                                                                                                             ],),('VolumeMount', 'list', 'dict', [('Name', 'str', None, None),
                                                                                                                                                                                  ('MountPath', 'str', None, None),
                                                                                                                                                                                  ('SubPath', 'str', None, None),
                                                                                                                                                                                  ('ReadOnly', 'str', None, None),
                                                                                                                                                                                  ],),('SecurityContext.ReadOnlyRootFilesystem', 'str', None, None),
                                                                           ('SecurityContext.RunAsUser', 'str', None, None),
                                                                           ('SecurityContext.Capability.Add', 'list', 'str', None),
                                                                           ('Gpu', 'str', None, None),
                                                                           ]),
                       "ImageRegistryCredential": ('ImageRegistryCredential', 'list', 'dict', [('Server', 'str', None, None),
                                                                                               ('UserName', 'str', None, None),
                                                                                               ('Password', 'str', None, None),
                                                                                               ]),
                       "Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       "DnsConfig.NameServer": ('DnsConfig.NameServer', 'list', 'str', None),
                       "DnsConfig.Option": ('DnsConfig.Option', 'list', 'dict', [('Name', 'str', None, None),
                                                                                 ('Value', 'str', None, None),
                                                                                 ]),
                       "DnsConfig.Search": ('DnsConfig.Search', 'list', 'str', None),
                       "Volume": ('Volume', 'list', 'dict', [('Name', 'str', None, None),
                                                             ('Type', 'str', None, None),
                                                             ('NFSVolume.Server', 'str', None, None),
                                                             ('NFSVolume.Path', 'str', None, None),
                                                             ('NFSVolume.ReadOnly', 'str', None, None),
                                                             ('ConfigFileVolume.ConfigFileToPath', 'list', 'dict', [('Content', 'str', None, None),
                                                                                                                    ('Path', 'str', None, None),
                                                                                                                    ],),('EmptyDirVolume.Medium', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_container_group_price(
            self,
            resource_owner_id=None,
            memory=None,
            resource_owner_account=None,
            owner_account=None,
            cpu=None,
            owner_id=None):
        api_request = APIRequest('DescribeContainerGroupPrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "Memory": memory,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "Cpu": cpu,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def exec_container_command(
            self,
            resource_owner_id=None,
            container_name=None,
            container_group_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            command=None):
        api_request = APIRequest('ExecContainerCommand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ContainerName": container_name,
            "ContainerGroupId": container_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "Command": command}
        return self._handle_request(api_request).result

    def describe_container_log(
            self,
            resource_owner_id=None,
            container_name=None,
            start_time=None,
            container_group_id=None,
            resource_owner_account=None,
            tail=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DescribeContainerLog', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ContainerName": container_name,
            "StartTime": start_time,
            "ContainerGroupId": container_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "Tail": tail,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result

    def create_container_group(
            self,
            container=None,
            resource_owner_id=None,
            memory=None,
            client_token=None,
            security_group_id=None,
            dns_policy=None,
            resource_group_id=None,
            host_aliase=None,
            init_container=None,
            instance_type=None,
            image_registry_credential=None,
            tag=None,
            eip_instance_id=None,
            arn=None,
            dns_config_name_server=None,
            security_context_sysctl=None,
            resource_owner_account=None,
            restart_policy=None,
            owner_account=None,
            dns_config_option=None,
            cpu=None,
            dns_config_search=None,
            owner_id=None,
            v_switch_id=None,
            volume=None,
            container_group_name=None,
            zone_id=None):
        api_request = APIRequest('CreateContainerGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Container": container,
            "ResourceOwnerId": resource_owner_id,
            "Memory": memory,
            "ClientToken": client_token,
            "SecurityGroupId": security_group_id,
            "DnsPolicy": dns_policy,
            "ResourceGroupId": resource_group_id,
            "HostAliase": host_aliase,
            "InitContainer": init_container,
            "InstanceType": instance_type,
            "ImageRegistryCredential": image_registry_credential,
            "Tag": tag,
            "EipInstanceId": eip_instance_id,
            "Arn": arn,
            "DnsConfig.NameServer": dns_config_name_server,
            "SecurityContext.Sysctl": security_context_sysctl,
            "ResourceOwnerAccount": resource_owner_account,
            "RestartPolicy": restart_policy,
            "OwnerAccount": owner_account,
            "DnsConfig.Option": dns_config_option,
            "Cpu": cpu,
            "DnsConfig.Search": dns_config_search,
            "OwnerId": owner_id,
            "VSwitchId": v_switch_id,
            "Volume": volume,
            "ContainerGroupName": container_group_name,
            "ZoneId": zone_id}
        repeat_info = {"Container": ('Container', 'list', 'dict', [('Image', 'str', None, None),
                                                                   ('Name', 'str', None, None),
                                                                   ('Cpu', 'str', None, None),
                                                                   ('Memory', 'str', None, None),
                                                                   ('WorkingDir', 'str', None, None),
                                                                   ('ImagePullPolicy', 'str', None, None),
                                                                   ('Command', 'list', 'str', None),
                                                                   ('Arg', 'list', 'str', None),
                                                                   ('VolumeMount', 'list', 'dict', [('MountPath', 'str', None, None),
                                                                                                    ('ReadOnly', 'str', None, None),
                                                                                                    ('Name', 'str', None, None),
                                                                                                    ('SubPath', 'str', None, None),
                                                                                                    ],),('Port', 'list', 'dict', [('Protocol', 'str', None, None),
                                                                                                                                  ('Port', 'str', None, None),
                                                                                                                                  ],),('EnvironmentVar', 'list', 'dict', [('Key', 'str', None, None),
                                                                                                                                                                          ('Value', 'str', None, None),
                                                                                                                                                                          ],),('ReadinessProbe.HttpGet.Path', 'str', None, None),
                                                                   ('ReadinessProbe.HttpGet.Port', 'str', None, None),
                                                                   ('ReadinessProbe.HttpGet.Scheme', 'str', None, None),
                                                                   ('ReadinessProbe.InitialDelaySeconds', 'str', None, None),
                                                                   ('ReadinessProbe.PeriodSeconds', 'str', None, None),
                                                                   ('ReadinessProbe.SuccessThreshold', 'str', None, None),
                                                                   ('ReadinessProbe.FailureThreshold', 'str', None, None),
                                                                   ('ReadinessProbe.TimeoutSeconds', 'str', None, None),
                                                                   ('ReadinessProbe.Exec.Command', 'list', 'str', None),
                                                                   ('LivenessProbe.HttpGet.Path', 'str', None, None),
                                                                   ('LivenessProbe.HttpGet.Port', 'str', None, None),
                                                                   ('LivenessProbe.HttpGet.Scheme', 'str', None, None),
                                                                   ('LivenessProbe.InitialDelaySeconds', 'str', None, None),
                                                                   ('LivenessProbe.PeriodSeconds', 'str', None, None),
                                                                   ('LivenessProbe.SuccessThreshold', 'str', None, None),
                                                                   ('LivenessProbe.FailureThreshold', 'str', None, None),
                                                                   ('LivenessProbe.TimeoutSeconds', 'str', None, None),
                                                                   ('LivenessProbe.Exec.Command', 'list', 'str', None),
                                                                   ('SecurityContext.Capability.Add', 'list', 'str', None),
                                                                   ('SecurityContext.ReadOnlyRootFilesystem', 'str', None, None),
                                                                   ('SecurityContext.RunAsUser', 'str', None, None),
                                                                   ('ReadinessProbe.TcpSocket.Port', 'str', None, None),
                                                                   ('LivenessProbe.TcpSocket.Port', 'str', None, None),
                                                                   ('Stdin', 'str', None, None),
                                                                   ('StdinOnce', 'str', None, None),
                                                                   ('Tty', 'str', None, None),
                                                                   ('Gpu', 'str', None, None),
                                                                   ]),
                       "HostAliase": ('HostAliase', 'list', 'dict', [('Ip', 'str', None, None),
                                                                     ('Hostname', 'list', 'str', None),
                                                                     ]),
                       "InitContainer": ('InitContainer', 'list', 'dict', [('Name', 'str', None, None),
                                                                           ('Image', 'str', None, None),
                                                                           ('Cpu', 'str', None, None),
                                                                           ('Memory', 'str', None, None),
                                                                           ('WorkingDir', 'str', None, None),
                                                                           ('ImagePullPolicy', 'str', None, None),
                                                                           ('Command', 'list', 'str', None),
                                                                           ('Arg', 'list', 'str', None),
                                                                           ('VolumeMount', 'list', 'dict', [('MountPath', 'str', None, None),
                                                                                                            ('ReadOnly', 'str', None, None),
                                                                                                            ('Name', 'str', None, None),
                                                                                                            ('SubPath', 'str', None, None),
                                                                                                            ],),('Port', 'list', 'dict', [('Protocol', 'str', None, None),
                                                                                                                                          ('Port', 'str', None, None),
                                                                                                                                          ],),('EnvironmentVar', 'list', 'dict', [('Key', 'str', None, None),
                                                                                                                                                                                  ('Value', 'str', None, None),
                                                                                                                                                                                  ],),('SecurityContext.Capability.Add', 'list', 'str', None),
                                                                           ('SecurityContext.ReadOnlyRootFilesystem', 'str', None, None),
                                                                           ('SecurityContext.RunAsUser', 'str', None, None),
                                                                           ('Gpu', 'str', None, None),
                                                                           ]),
                       "ImageRegistryCredential": ('ImageRegistryCredential', 'list', 'dict', [('Server', 'str', None, None),
                                                                                               ('UserName', 'str', None, None),
                                                                                               ('Password', 'str', None, None),
                                                                                               ]),
                       "Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       "Arn": ('Arn', 'list', 'dict', [('RoleArn', 'str', None, None),
                                                       ('RoleType', 'str', None, None),
                                                       ('AssumeRoleFor', 'str', None, None),
                                                       ]),
                       "DnsConfig.NameServer": ('DnsConfig.NameServer', 'list', 'str', None),
                       "SecurityContext.Sysctl": ('SecurityContext.Sysctl', 'list', 'dict', [('Name', 'str', None, None),
                                                                                             ('Value', 'str', None, None),
                                                                                             ]),
                       "DnsConfig.Option": ('DnsConfig.Option', 'list', 'dict', [('Name', 'str', None, None),
                                                                                 ('Value', 'str', None, None),
                                                                                 ]),
                       "DnsConfig.Search": ('DnsConfig.Search', 'list', 'str', None),
                       "Volume": ('Volume', 'list', 'dict', [('Name', 'str', None, None),
                                                             ('NFSVolume.Server', 'str', None, None),
                                                             ('NFSVolume.Path', 'str', None, None),
                                                             ('NFSVolume.ReadOnly', 'str', None, None),
                                                             ('ConfigFileVolume.ConfigFileToPath', 'list', 'dict', [('Content', 'str', None, None),
                                                                                                                    ('Path', 'str', None, None),
                                                                                                                    ('Mode', 'str', None, None),
                                                                                                                    ],),('Type', 'str', None, None),
                                                             ('EmptyDirVolume.Medium', 'str', None, None),
                                                             ('ConfigFileVolume.DefaultModel', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_container_groups(
            self,
            resource_owner_id=None,
            container_group_ids=None,
            next_token=None,
            limit=None,
            tag=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None,
            v_switch_id=None,
            container_group_name=None,
            zone_id=None,
            status=None):
        api_request = APIRequest('DescribeContainerGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ContainerGroupIds": container_group_ids,
            "NextToken": next_token,
            "Limit": limit,
            "Tag": tag,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id,
            "VSwitchId": v_switch_id,
            "ContainerGroupName": container_group_name,
            "ZoneId": zone_id,
            "Status": status}
        repeat_info = {"Tag": ('Tag', 'list', 'dict', [('Key', 'str', None, None),
                                                       ('Value', 'str', None, None),
                                                       ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_container_group(
            self,
            resource_owner_id=None,
            client_token=None,
            container_group_id=None,
            resource_owner_account=None,
            owner_account=None,
            owner_id=None):
        api_request = APIRequest('DeleteContainerGroup', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ResourceOwnerId": resource_owner_id,
            "ClientToken": client_token,
            "ContainerGroupId": container_group_id,
            "ResourceOwnerAccount": resource_owner_account,
            "OwnerAccount": owner_account,
            "OwnerId": owner_id}
        return self._handle_request(api_request).result
