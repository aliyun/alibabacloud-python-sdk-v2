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


class EHPCClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'EHPC'
        self.api_version = '2018-04-12'
        self.location_service_code = 'ehs'
        self.location_endpoint_type = 'openAPI'

    def set_gws_instance_user(self, instance_id=None, user_uid=None, user_name=None):
        api_request = APIRequest('SetGWSInstanceUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "UserUid": user_uid,
            "UserName": user_name}
        return self._handle_request(api_request).result

    def update_queue_config(
            self,
            queue_name=None,
            resource_group_id=None,
            cluster_id=None,
            compute_instance_type=None):
        api_request = APIRequest('UpdateQueueConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "QueueName": queue_name,
            "ResourceGroupId": resource_group_id,
            "ClusterId": cluster_id,
            "ComputeInstanceType": compute_instance_type}
        return self._handle_request(api_request).result

    def mount_nfs(self, instance_id=None, nfs_dir=None, mount_dir=None):
        api_request = APIRequest('MountNFS', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "NfsDir": nfs_dir, "MountDir": mount_dir}
        return self._handle_request(api_request).result

    def install_nfs_client(self, instance_id=None):
        api_request = APIRequest('InstallNFSClient', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def describe_nfs_client_status(self, instance_id=None):
        api_request = APIRequest('DescribeNFSClientStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def describe_gws_clusters(self, page_size=None, cluster_id=None, page_number=None):
        api_request = APIRequest('DescribeGWSClusters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def describe_gws_instances(
            self,
            instance_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('DescribeGWSInstances', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "InstanceId": instance_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_gws_connect_ticket(self, instance_id=None, app_name=None):
        api_request = APIRequest('GetGWSConnectTicket', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "AppName": app_name}
        return self._handle_request(api_request).result

    def create_gws_instance(
            self,
            period=None,
            image_id=None,
            allocate_public_address=None,
            app_list=None,
            internet_max_bandwidth_out=None,
            cluster_id=None,
            work_mode=None,
            period_unit=None,
            auto_renew=None,
            system_disk_category=None,
            internet_charge_type=None,
            system_disk_size=None,
            name=None,
            instance_type=None,
            instance_charge_type=None,
            internet_max_bandwidth_in=None):
        api_request = APIRequest('CreateGWSInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "ImageId": image_id,
            "AllocatePublicAddress": allocate_public_address,
            "AppList": app_list,
            "InternetMaxBandwidthOut": internet_max_bandwidth_out,
            "ClusterId": cluster_id,
            "WorkMode": work_mode,
            "PeriodUnit": period_unit,
            "AutoRenew": auto_renew,
            "SystemDiskCategory": system_disk_category,
            "InternetChargeType": internet_charge_type,
            "SystemDiskSize": system_disk_size,
            "Name": name,
            "InstanceType": instance_type,
            "InstanceChargeType": instance_charge_type,
            "InternetMaxBandwidthIn": internet_max_bandwidth_in}
        return self._handle_request(api_request).result

    def describe_gws_images(self, page_size=None, page_number=None):
        api_request = APIRequest('DescribeGWSImages', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_gws_instance(self, instance_id=None):
        api_request = APIRequest('DeleteGWSInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def delete_gws_cluster(self, cluster_id=None):
        api_request = APIRequest('DeleteGWSCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def create_gws_cluster(self, cluster_type=None, vpc_id=None, name=None):
        api_request = APIRequest('CreateGWSCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterType": cluster_type, "VpcId": vpc_id, "Name": name}
        return self._handle_request(api_request).result

    def create_gws_image(self, instance_id=None, name=None):
        api_request = APIRequest('CreateGWSImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id, "Name": name}
        return self._handle_request(api_request).result

    def start_gws_instance(self, instance_id=None):
        api_request = APIRequest('StartGWSInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def stop_gws_instance(self, instance_id=None):
        api_request = APIRequest('StopGWSInstance', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"InstanceId": instance_id}
        return self._handle_request(api_request).result

    def query_service_pack_and_price(self,):
        api_request = APIRequest('QueryServicePackAndPrice', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def update_cluster_volumes(self, list_of_additional_volumes=None, cluster_id=None):
        api_request = APIRequest('UpdateClusterVolumes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AdditionalVolumes": list_of_additional_volumes,
            "ClusterId": cluster_id}
        repeat_info = {"AdditionalVolumes": ('AdditionalVolumes',
                                             'list',
                                             'dict',
                                             [('VolumeType',
                                               'str',
                                               None,
                                               None),
                                              ('VolumeProtocol',
                                               'str',
                                               None,
                                               None),
                                                 ('LocalDirectory',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('RemoteDirectory',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('Roles',
                                                  'list',
                                                  'dict',
                                                  [('Name',
                                                    'str',
                                                    None,
                                                    None),
                                                   ],
                                                  ),
                                                 ('VolumeId',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('VolumeMountpoint',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('Location',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('JobQueue',
                                                  'str',
                                                  None,
                                                  None),
                                              ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_cluster_volumes(self, cluster_id=None):
        api_request = APIRequest('GetClusterVolumes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_job(self, job_id=None, cluster_id=None):
        api_request = APIRequest('DescribeJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"JobId": job_id, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def install_software(self, application=None, cluster_id=None):
        api_request = APIRequest('InstallSoftware', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Application": application, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def get_accounting_report(
            self,
            report_type=None,
            end_time=None,
            cluster_id=None,
            start_time=None):
        api_request = APIRequest('GetAccountingReport', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ReportType": report_type,
            "EndTime": end_time,
            "ClusterId": cluster_id,
            "StartTime": start_time}
        return self._handle_request(api_request).result

    def uninstall_software(self, application=None, cluster_id=None):
        api_request = APIRequest('UninstallSoftware', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Application": application, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_installed_software(self, cluster_id=None):
        api_request = APIRequest('ListInstalledSoftware', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def add_queue(self, queue_name=None, cluster_id=None):
        api_request = APIRequest('AddQueue', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"QueueName": queue_name, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def delete_queue(self, queue_name=None, cluster_id=None):
        api_request = APIRequest('DeleteQueue', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"QueueName": queue_name, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def set_queue(self, queue_name=None, list_of_node=None, cluster_id=None):
        api_request = APIRequest('SetQueue', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "QueueName": queue_name,
            "Node": list_of_node,
            "ClusterId": cluster_id}
        repeat_info = {"Node": ('Node', 'list', 'dict', [('Name', 'str', None, None),
                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_nodes_by_queue(
            self,
            queue_name=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('ListNodesByQueue', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "QueueName": queue_name,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def stop_visual_service(self, port=None, cluster_id=None, cidr_ip=None):
        api_request = APIRequest('StopVisualService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Port": port, "ClusterId": cluster_id, "CidrIp": cidr_ip}
        return self._handle_request(api_request).result

    def list_cpfs_file_systems(self, page_size=None, page_number=None, file_system_id=None):
        api_request = APIRequest('ListCpfsFileSystems', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "PageNumber": page_number,
            "FileSystemId": file_system_id}
        return self._handle_request(api_request).result

    def list_available_file_system_types(self,):
        api_request = APIRequest('ListAvailableFileSystemTypes', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def start_visual_service(self, port=None, cluster_id=None, cidr_ip=None):
        api_request = APIRequest('StartVisualService', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Port": port, "ClusterId": cluster_id, "CidrIp": cidr_ip}
        return self._handle_request(api_request).result

    def get_visual_service_status(self, cluster_id=None):
        api_request = APIRequest('GetVisualServiceStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def modify_visual_service_passwd(
            self,
            passwd=None,
            runas_user_password=None,
            runas_user=None,
            cluster_id=None):
        api_request = APIRequest('ModifyVisualServicePasswd', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Passwd": passwd,
            "RunasUserPassword": runas_user_password,
            "RunasUser": runas_user,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_clusters_meta(self, page_size=None, page_number=None):
        api_request = APIRequest('ListClustersMeta', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "PageNumber": page_number}
        return self._handle_request(api_request).result

    def create_job_file(
            self,
            target_file=None,
            runas_user_password=None,
            runas_user=None,
            cluster_id=None,
            content=None):
        api_request = APIRequest('CreateJobFile', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "TargetFile": target_file,
            "RunasUserPassword": runas_user_password,
            "RunasUser": runas_user,
            "ClusterId": cluster_id,
            "Content": content}
        return self._handle_request(api_request).result

    def list_file_system_with_mount_targets(self, page_size=None, page_number=None):
        api_request = APIRequest('ListFileSystemWithMountTargets', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_available_ecs_types(
            self,
            spot_strategy=None,
            zone_id=None,
            show_sold_out=None,
            instance_charge_type=None):
        api_request = APIRequest('ListAvailableEcsTypes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SpotStrategy": spot_strategy,
            "ZoneId": zone_id,
            "ShowSoldOut": show_sold_out,
            "InstanceChargeType": instance_charge_type}
        return self._handle_request(api_request).result

    def list_queues(self, cluster_id=None):
        api_request = APIRequest('ListQueues', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_price(
            self,
            price_unit=None,
            list_of_commodities=None,
            charge_type=None,
            order_type=None):
        api_request = APIRequest('DescribePrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PriceUnit": price_unit,
            "Commodities": list_of_commodities,
            "ChargeType": charge_type,
            "OrderType": order_type}
        repeat_info = {"Commodities": ('Commodities',
                                       'list',
                                       'dict',
                                       [('Amount',
                                         'str',
                                         None,
                                         None),
                                        ('Period',
                                         'str',
                                         None,
                                         None),
                                           ('NodeType',
                                            'str',
                                            None,
                                            None),
                                           ('SystemDiskCategory',
                                            'str',
                                            None,
                                            None),
                                           ('SystemDiskSize',
                                            'str',
                                            None,
                                            None),
                                           ('InstanceType',
                                            'str',
                                            None,
                                            None),
                                           ('NetworkType',
                                            'str',
                                            None,
                                            None),
                                        ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_image_price(
            self,
            period=None,
            amount=None,
            image_id=None,
            price_unit=None,
            sku_code=None,
            order_type=None):
        api_request = APIRequest('DescribeImagePrice', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Period": period,
            "Amount": amount,
            "ImageId": image_id,
            "PriceUnit": price_unit,
            "SkuCode": sku_code,
            "OrderType": order_type}
        return self._handle_request(api_request).result

    def get_cloud_metric_profiling(self, region_id=None, profiling_id=None, cluster_id=None):
        api_request = APIRequest('GetCloudMetricProfiling', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "ProfilingId": profiling_id,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def run_cloud_metric_profiling(
            self,
            duration=None,
            host_name=None,
            region_id=None,
            process_id=None,
            freq=None,
            cluster_id=None):
        api_request = APIRequest('RunCloudMetricProfiling', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Duration": duration,
            "HostName": host_name,
            "RegionId": region_id,
            "ProcessId": process_id,
            "Freq": freq,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_cloud_metric_profilings(
            self,
            region_id=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('ListCloudMetricProfilings', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RegionId": region_id,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_image(self, container_type=None, cluster_id=None, repository=None, image_tag=None):
        api_request = APIRequest('DeleteImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContainerType": container_type,
            "ClusterId": cluster_id,
            "Repository": repository,
            "ImageTag": image_tag}
        return self._handle_request(api_request).result

    def describe_image(self, container_type=None, cluster_id=None, repository=None, image_tag=None):
        api_request = APIRequest('DescribeImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContainerType": container_type,
            "ClusterId": cluster_id,
            "Repository": repository,
            "ImageTag": image_tag}
        return self._handle_request(api_request).result

    def modify_image_gateway_config(
            self,
            default_repo_location=None,
            db_password=None,
            list_of_repo=None,
            db_type=None,
            db_username=None,
            db_server_info=None,
            pull_update_timeout=None,
            cluster_id=None,
            image_expiration_timeout=None):
        api_request = APIRequest('ModifyImageGatewayConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "DefaultRepoLocation": default_repo_location,
            "DBPassword": db_password,
            "Repo": list_of_repo,
            "DBType": db_type,
            "DBUsername": db_username,
            "DBServerInfo": db_server_info,
            "PullUpdateTimeout": pull_update_timeout,
            "ClusterId": cluster_id,
            "ImageExpirationTimeout": image_expiration_timeout}
        repeat_info = {"Repo": ('Repo', 'list', 'dict', [('Auth', 'str', None, None),
                                                         ('Location', 'str', None, None),
                                                         ('URL', 'str', None, None),
                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def add_local_nodes(self, nodes=None, cluster_id=None):
        api_request = APIRequest('AddLocalNodes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Nodes": nodes, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def get_cloud_metric_logs(
            self,
            aggregation_type=None,
            filter_=None,
            metric_categories=None,
            metric_scope=None,
            from_=None,
            cluster_id=None,
            to=None,
            aggregation_interval=None,
            reverse=None):
        api_request = APIRequest('GetCloudMetricLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AggregationType": aggregation_type,
            "Filter": filter_,
            "MetricCategories": metric_categories,
            "MetricScope": metric_scope,
            "From": from_,
            "ClusterId": cluster_id,
            "To": to,
            "AggregationInterval": aggregation_interval,
            "Reverse": reverse}
        return self._handle_request(api_request).result

    def describe_image_gateway_config(self, cluster_id=None):
        api_request = APIRequest('DescribeImageGatewayConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def pull_image(self, container_type=None, cluster_id=None, repository=None, image_tag=None):
        api_request = APIRequest('PullImage', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContainerType": container_type,
            "ClusterId": cluster_id,
            "Repository": repository,
            "ImageTag": image_tag}
        return self._handle_request(api_request).result

    def list_container_images(
            self,
            container_type=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('ListContainerImages', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContainerType": container_type,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_container_app_attributes(self, description=None, container_id=None):
        api_request = APIRequest('ModifyContainerAppAttributes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Description": description, "ContainerId": container_id}
        return self._handle_request(api_request).result

    def list_container_apps(self, page_size=None, page_number=None):
        api_request = APIRequest('ListContainerApps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "PageNumber": page_number}
        return self._handle_request(api_request).result

    def get_hybrid_cluster_config(self, node=None, cluster_id=None):
        api_request = APIRequest('GetHybridClusterConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Node": node, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def describe_container_app(self, container_id=None):
        api_request = APIRequest('DescribeContainerApp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ContainerId": container_id}
        return self._handle_request(api_request).result

    def delete_container_apps(self, list_of_container_app=None):
        api_request = APIRequest('DeleteContainerApps', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ContainerApp": list_of_container_app}
        repeat_info = {"ContainerApp": ('ContainerApp', 'list', 'dict', [('Id', 'str', None, None),
                                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def create_hybrid_cluster(
            self,
            ehpc_version=None,
            security_group_id=None,
            description=None,
            key_pair_name=None,
            security_group_name=None,
            ecs_order_compute_instance_type=None,
            on_premise_volume_remote_path=None,
            job_queue=None,
            volume_type=None,
            resource_group_id=None,
            password=None,
            on_premise_volume_mount_point=None,
            on_premise_volume_protocol=None,
            volume_protocol=None,
            on_premise_volume_local_path=None,
            client_version=None,
            os_tag=None,
            remote_directory=None,
            list_of_post_install_script=None,
            vswitch_id=None,
            list_of_nodes=None,
            list_of_application=None,
            domain=None,
            vpc_id=None,
            name=None,
            volume_id=None,
            volume_mountpoint=None,
            zone_id=None,
            scheduler_pre_install=None,
            location=None):
        api_request = APIRequest('CreateHybridCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "EhpcVersion": ehpc_version,
            "SecurityGroupId": security_group_id,
            "Description": description,
            "KeyPairName": key_pair_name,
            "SecurityGroupName": security_group_name,
            "EcsOrder.Compute.InstanceType": ecs_order_compute_instance_type,
            "OnPremiseVolumeRemotePath": on_premise_volume_remote_path,
            "JobQueue": job_queue,
            "VolumeType": volume_type,
            "ResourceGroupId": resource_group_id,
            "Password": password,
            "OnPremiseVolumeMountPoint": on_premise_volume_mount_point,
            "OnPremiseVolumeProtocol": on_premise_volume_protocol,
            "VolumeProtocol": volume_protocol,
            "OnPremiseVolumeLocalPath": on_premise_volume_local_path,
            "ClientVersion": client_version,
            "OsTag": os_tag,
            "RemoteDirectory": remote_directory,
            "PostInstallScript": list_of_post_install_script,
            "VSwitchId": vswitch_id,
            "Nodes": list_of_nodes,
            "Application": list_of_application,
            "Domain": domain,
            "VpcId": vpc_id,
            "Name": name,
            "VolumeId": volume_id,
            "VolumeMountpoint": volume_mountpoint,
            "ZoneId": zone_id,
            "SchedulerPreInstall": scheduler_pre_install,
            "Location": location}
        repeat_info = {"PostInstallScript": ('PostInstallScript',
                                             'list',
                                             'dict',
                                             [('Args',
                                               'str',
                                               None,
                                               None),
                                              ('Url',
                                               'str',
                                               None,
                                               None),
                                              ]),
                       "Nodes": ('Nodes',
                                 'list',
                                 'dict',
                                 [('IpAddress',
                                   'str',
                                   None,
                                   None),
                                  ('HostName',
                                     'str',
                                     None,
                                     None),
                                     ('Role',
                                      'str',
                                      None,
                                      None),
                                     ('AccountType',
                                      'str',
                                      None,
                                      None),
                                     ('SchedulerType',
                                      'str',
                                      None,
                                      None),
                                  ]),
                       "Application": ('Application',
                                       'list',
                                       'dict',
                                       [('Tag',
                                         'str',
                                         None,
                                         None),
                                        ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def add_container_app(
            self,
            container_type=None,
            name=None,
            description=None,
            repository=None,
            image_tag=None):
        api_request = APIRequest('AddContainerApp', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ContainerType": container_type,
            "Name": name,
            "Description": description,
            "Repository": repository,
            "ImageTag": image_tag}
        return self._handle_request(api_request).result

    def list_commands(self, page_size=None, cluster_id=None, command_id=None, page_number=None):
        api_request = APIRequest('ListCommands', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "CommandId": command_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_invocation_status(self, cluster_id=None, command_id=None):
        api_request = APIRequest('ListInvocationStatus', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id, "CommandId": command_id}
        return self._handle_request(api_request).result

    def list_invocation_results(
            self,
            list_of_instance=None,
            invoke_record_status=None,
            page_size=None,
            cluster_id=None,
            command_id=None,
            page_number=None):
        api_request = APIRequest('ListInvocationResults', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Instance": list_of_instance,
            "InvokeRecordStatus": invoke_record_status,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "CommandId": command_id,
            "PageNumber": page_number}
        repeat_info = {"Instance": ('Instance', 'list', 'dict', [('Id', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def invoke_shell_command(
            self,
            list_of_instance=None,
            working_dir=None,
            cluster_id=None,
            command=None,
            timeout=None):
        api_request = APIRequest('InvokeShellCommand', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Instance": list_of_instance,
            "WorkingDir": working_dir,
            "ClusterId": cluster_id,
            "Command": command,
            "Timeout": timeout}
        repeat_info = {"Instance": ('Instance', 'list', 'dict', [('Id', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def describe_auto_scale_config(self, cluster_id=None):
        api_request = APIRequest('DescribeAutoScaleConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def stop_cluster(self, cluster_id=None):
        api_request = APIRequest('StopCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def start_nodes(self, role=None, list_of_instance=None, cluster_id=None):
        api_request = APIRequest('StartNodes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Role": role, "Instance": list_of_instance, "ClusterId": cluster_id}
        repeat_info = {"Instance": ('Instance', 'list', 'dict', [('Id', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def start_cluster(self, cluster_id=None):
        api_request = APIRequest('StartCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def stop_nodes(self, role=None, list_of_instance=None, cluster_id=None):
        api_request = APIRequest('StopNodes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Role": role, "Instance": list_of_instance, "ClusterId": cluster_id}
        repeat_info = {"Instance": ('Instance', 'list', 'dict', [('Id', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def recover_cluster(
            self,
            image_id=None,
            os_tag=None,
            client_version=None,
            account_type=None,
            scheduler_type=None,
            cluster_id=None,
            image_owner_alias=None):
        api_request = APIRequest('RecoverCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ImageId": image_id,
            "OsTag": os_tag,
            "ClientVersion": client_version,
            "AccountType": account_type,
            "SchedulerType": scheduler_type,
            "ClusterId": cluster_id,
            "ImageOwnerAlias": image_owner_alias}
        return self._handle_request(api_request).result

    def stop_jobs(self, jobs=None, cluster_id=None):
        api_request = APIRequest('StopJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Jobs": jobs, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_nodes_no_paging(self, host_name=None, role=None, cluster_id=None, only_detached=None):
        api_request = APIRequest('ListNodesNoPaging', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HostName": host_name,
            "Role": role,
            "ClusterId": cluster_id,
            "OnlyDetached": only_detached}
        return self._handle_request(api_request).result

    def list_regions(self,):
        api_request = APIRequest('ListRegions', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def list_clusters(self, page_size=None, page_number=None):
        api_request = APIRequest('ListClusters', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_user_passwords(self, cluster_id=None, list_of_user=None):
        api_request = APIRequest('ModifyUserPasswords', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id, "User": list_of_user}
        repeat_info = {"User": ('User', 'list', 'dict', [('Password', 'str', None, None),
                                                         ('Name', 'str', None, None),
                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_jobs(
            self,
            owner=None,
            page_size=None,
            cluster_id=None,
            state=None,
            rerunable=None,
            page_number=None):
        api_request = APIRequest('ListJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "Owner": owner,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "State": state,
            "Rerunable": rerunable,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def modify_user_groups(self, cluster_id=None, list_of_user=None):
        api_request = APIRequest('ModifyUserGroups', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id, "User": list_of_user}
        repeat_info = {"User": ('User', 'list', 'dict', [('Name', 'str', None, None),
                                                         ('Group', 'str', None, None),
                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def get_auto_scale_config(self, cluster_id=None):
        api_request = APIRequest('GetAutoScaleConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_preferred_ecs_types(self, spot_strategy=None, zone_id=None, instance_charge_type=None):
        api_request = APIRequest('ListPreferredEcsTypes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SpotStrategy": spot_strategy,
            "ZoneId": zone_id,
            "InstanceChargeType": instance_charge_type}
        return self._handle_request(api_request).result

    def add_nodes(
            self,
            auto_renew_period=None,
            period=None,
            image_id=None,
            count=None,
            cluster_id=None,
            compute_spot_strategy=None,
            job_queue=None,
            image_owner_alias=None,
            system_disk_type=None,
            vswitch_id=None,
            period_unit=None,
            auto_renew=None,
            ecs_charge_type=None,
            create_mode=None,
            system_disk_size=None,
            instance_type=None,
            zone_id=None,
            compute_spot_price_limit=None):
        api_request = APIRequest('AddNodes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "AutoRenewPeriod": auto_renew_period,
            "Period": period,
            "ImageId": image_id,
            "Count": count,
            "ClusterId": cluster_id,
            "ComputeSpotStrategy": compute_spot_strategy,
            "JobQueue": job_queue,
            "ImageOwnerAlias": image_owner_alias,
            "SystemDiskType": system_disk_type,
            "VSwitchId": vswitch_id,
            "PeriodUnit": period_unit,
            "AutoRenew": auto_renew,
            "EcsChargeType": ecs_charge_type,
            "CreateMode": create_mode,
            "SystemDiskSize": system_disk_size,
            "InstanceType": instance_type,
            "ZoneId": zone_id,
            "ComputeSpotPriceLimit": compute_spot_price_limit}
        return self._handle_request(api_request).result

    def edit_job_template(
            self,
            stderr_redirect_path=None,
            variables=None,
            runas_user=None,
            re_runable=None,
            template_id=None,
            priority=None,
            command_line=None,
            array_request=None,
            package_path=None,
            name=None,
            stdout_redirect_path=None):
        api_request = APIRequest('EditJobTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StderrRedirectPath": stderr_redirect_path,
            "Variables": variables,
            "RunasUser": runas_user,
            "ReRunable": re_runable,
            "TemplateId": template_id,
            "Priority": priority,
            "CommandLine": command_line,
            "ArrayRequest": array_request,
            "PackagePath": package_path,
            "Name": name,
            "StdoutRedirectPath": stdout_redirect_path}
        return self._handle_request(api_request).result

    def set_auto_scale_config(
            self,
            shrink_idle_times=None,
            grow_timeout_in_minutes=None,
            cluster_id=None,
            enable_auto_grow=None,
            spot_price_limit=None,
            enable_auto_shrink=None,
            spot_strategy=None,
            max_nodes_in_cluster=None,
            exclude_nodes=None,
            shrink_interval_in_minutes=None,
            list_of_queues=None,
            extra_nodes_grow_ratio=None,
            grow_interval_in_minutes=None,
            grow_ratio=None):
        api_request = APIRequest('SetAutoScaleConfig', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ShrinkIdleTimes": shrink_idle_times,
            "GrowTimeoutInMinutes": grow_timeout_in_minutes,
            "ClusterId": cluster_id,
            "EnableAutoGrow": enable_auto_grow,
            "SpotPriceLimit": spot_price_limit,
            "EnableAutoShrink": enable_auto_shrink,
            "SpotStrategy": spot_strategy,
            "MaxNodesInCluster": max_nodes_in_cluster,
            "ExcludeNodes": exclude_nodes,
            "ShrinkIntervalInMinutes": shrink_interval_in_minutes,
            "Queues": list_of_queues,
            "ExtraNodesGrowRatio": extra_nodes_grow_ratio,
            "GrowIntervalInMinutes": grow_interval_in_minutes,
            "GrowRatio": grow_ratio}
        repeat_info = {"Queues": ('Queues', 'list', 'dict', [('SpotStrategy', 'str', None, None),
                                                             ('QueueName', 'str', None, None),
                                                             ('InstanceTypes', 'list', 'dict', [('SpotStrategy', 'str', None, None),
                                                                                                ('VSwitchId', 'str', None, None),
                                                                                                ('InstanceType', 'str', None, None),
                                                                                                ('ZoneId', 'str', None, None),
                                                                                                ('SpotPriceLimit', 'str', None, None),
                                                                                                ],),('InstanceType', 'str', None, None),
                                                             ('EnableAutoGrow', 'str', None, None),
                                                             ('SpotPriceLimit', 'str', None, None),
                                                             ('EnableAutoShrink', 'str', None, None),
                                                             ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_nodes(self, release_instance=None, list_of_instance=None, cluster_id=None):
        api_request = APIRequest('DeleteNodes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "ReleaseInstance": release_instance,
            "Instance": list_of_instance,
            "ClusterId": cluster_id}
        repeat_info = {"Instance": ('Instance', 'list', 'dict', [('Id', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def delete_jobs(self, jobs=None, cluster_id=None):
        api_request = APIRequest('DeleteJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Jobs": jobs, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_images(self,):
        api_request = APIRequest('ListImages', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def delete_users(self, cluster_id=None, list_of_user=None):
        api_request = APIRequest('DeleteUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id, "User": list_of_user}
        repeat_info = {"User": ('User', 'list', 'dict', [('Name', 'str', None, None),
                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def set_job_user(self, runas_user_password=None, runas_user=None, cluster_id=None):
        api_request = APIRequest('SetJobUser', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "RunasUserPassword": runas_user_password,
            "RunasUser": runas_user,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def reset_nodes(self, list_of_instance=None, cluster_id=None):
        api_request = APIRequest('ResetNodes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Instance": list_of_instance, "ClusterId": cluster_id}
        repeat_info = {"Instance": ('Instance', 'list', 'dict', [('Id', 'str', None, None),
                                                                 ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_custom_images(self, base_os_tag=None, image_owner_alias=None):
        api_request = APIRequest('ListCustomImages', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"BaseOsTag": base_os_tag, "ImageOwnerAlias": image_owner_alias}
        return self._handle_request(api_request).result

    def add_users(self, cluster_id=None, list_of_user=None):
        api_request = APIRequest('AddUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id, "User": list_of_user}
        repeat_info = {"User": ('User', 'list', 'dict', [('Password', 'str', None, None),
                                                         ('Name', 'str', None, None),
                                                         ('Group', 'str', None, None),
                                                         ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def list_softwares(self, ehpc_version=None):
        api_request = APIRequest('ListSoftwares', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"EhpcVersion": ehpc_version}
        return self._handle_request(api_request).result

    def list_job_templates(self, name=None, page_size=None, page_number=None):
        api_request = APIRequest('ListJobTemplates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name, "PageSize": page_size, "PageNumber": page_number}
        return self._handle_request(api_request).result

    def submit_job(
            self,
            stderr_redirect_path=None,
            variables=None,
            runas_user_password=None,
            post_cmd_line=None,
            runas_user=None,
            cluster_id=None,
            re_runable=None,
            priority=None,
            command_line=None,
            job_queue=None,
            array_request=None,
            unzip_cmd=None,
            package_path=None,
            input_file_url=None,
            name=None,
            stdout_redirect_path=None,
            container_id=None):
        api_request = APIRequest('SubmitJob', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StderrRedirectPath": stderr_redirect_path,
            "Variables": variables,
            "RunasUserPassword": runas_user_password,
            "PostCmdLine": post_cmd_line,
            "RunasUser": runas_user,
            "ClusterId": cluster_id,
            "ReRunable": re_runable,
            "Priority": priority,
            "CommandLine": command_line,
            "JobQueue": job_queue,
            "ArrayRequest": array_request,
            "UnzipCmd": unzip_cmd,
            "PackagePath": package_path,
            "InputFileUrl": input_file_url,
            "Name": name,
            "StdoutRedirectPath": stdout_redirect_path,
            "ContainerId": container_id}
        return self._handle_request(api_request).result

    def list_current_client_version(self,):
        api_request = APIRequest('ListCurrentClientVersion', 'GET', 'http', 'RPC', '')

        return self._handle_request(api_request).result

    def describe_cluster(self, cluster_id=None):
        api_request = APIRequest('DescribeCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_nodes(
            self,
            host_name=None,
            role=None,
            page_size=None,
            cluster_id=None,
            page_number=None):
        api_request = APIRequest('ListNodes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "HostName": host_name,
            "Role": role,
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def list_volumes(self, page_size=None, page_number=None):
        api_request = APIRequest('ListVolumes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"PageSize": page_size, "PageNumber": page_number}
        return self._handle_request(api_request).result

    def create_job_template(
            self,
            stderr_redirect_path=None,
            array_request=None,
            package_path=None,
            variables=None,
            name=None,
            runas_user=None,
            stdout_redirect_path=None,
            re_runable=None,
            priority=None,
            command_line=None):
        api_request = APIRequest('CreateJobTemplate', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "StderrRedirectPath": stderr_redirect_path,
            "ArrayRequest": array_request,
            "PackagePath": package_path,
            "Variables": variables,
            "Name": name,
            "RunasUser": runas_user,
            "StdoutRedirectPath": stdout_redirect_path,
            "ReRunable": re_runable,
            "Priority": priority,
            "CommandLine": command_line}
        return self._handle_request(api_request).result

    def modify_cluster_attributes(self, name=None, description=None, cluster_id=None):
        api_request = APIRequest('ModifyClusterAttributes', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Name": name, "Description": description, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def upgrade_client(self, client_version=None, cluster_id=None):
        api_request = APIRequest('UpgradeClient', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ClientVersion": client_version, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_users(self, page_size=None, cluster_id=None, page_number=None):
        api_request = APIRequest('ListUsers', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result

    def delete_cluster(self, release_instance=None, cluster_id=None):
        api_request = APIRequest('DeleteCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"ReleaseInstance": release_instance, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def create_cluster(
            self,
            scc_cluster_id=None,
            image_id=None,
            list_of_additional_volumes=None,
            ecs_order_manager_instance_type=None,
            ehpc_version=None,
            account_type=None,
            security_group_id=None,
            description=None,
            key_pair_name=None,
            security_group_name=None,
            ecs_order_compute_instance_type=None,
            job_queue=None,
            image_owner_alias=None,
            volume_type=None,
            deploy_mode=None,
            system_disk_type=None,
            ecs_order_manager_count=None,
            resource_group_id=None,
            password=None,
            ecs_order_login_count=None,
            remote_vis_enable=None,
            system_disk_size=None,
            compute_spot_price_limit=None,
            auto_renew_period=None,
            period=None,
            volume_protocol=None,
            client_version=None,
            os_tag=None,
            remote_directory=None,
            ecs_order_compute_count=None,
            compute_spot_strategy=None,
            list_of_post_install_script=None,
            vswitch_id=None,
            period_unit=None,
            list_of_application=None,
            auto_renew=None,
            ecs_charge_type=None,
            input_file_url=None,
            vpc_id=None,
            ha_enable=None,
            name=None,
            scheduler_type=None,
            volume_id=None,
            volume_mountpoint=None,
            ecs_order_login_instance_type=None,
            zone_id=None):
        api_request = APIRequest('CreateCluster', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "SccClusterId": scc_cluster_id,
            "ImageId": image_id,
            "AdditionalVolumes": list_of_additional_volumes,
            "EcsOrder.Manager.InstanceType": ecs_order_manager_instance_type,
            "EhpcVersion": ehpc_version,
            "AccountType": account_type,
            "SecurityGroupId": security_group_id,
            "Description": description,
            "KeyPairName": key_pair_name,
            "SecurityGroupName": security_group_name,
            "EcsOrder.Compute.InstanceType": ecs_order_compute_instance_type,
            "JobQueue": job_queue,
            "ImageOwnerAlias": image_owner_alias,
            "VolumeType": volume_type,
            "DeployMode": deploy_mode,
            "SystemDiskType": system_disk_type,
            "EcsOrder.Manager.Count": ecs_order_manager_count,
            "ResourceGroupId": resource_group_id,
            "Password": password,
            "EcsOrder.Login.Count": ecs_order_login_count,
            "RemoteVisEnable": remote_vis_enable,
            "SystemDiskSize": system_disk_size,
            "ComputeSpotPriceLimit": compute_spot_price_limit,
            "AutoRenewPeriod": auto_renew_period,
            "Period": period,
            "VolumeProtocol": volume_protocol,
            "ClientVersion": client_version,
            "OsTag": os_tag,
            "RemoteDirectory": remote_directory,
            "EcsOrder.Compute.Count": ecs_order_compute_count,
            "ComputeSpotStrategy": compute_spot_strategy,
            "PostInstallScript": list_of_post_install_script,
            "VSwitchId": vswitch_id,
            "PeriodUnit": period_unit,
            "Application": list_of_application,
            "AutoRenew": auto_renew,
            "EcsChargeType": ecs_charge_type,
            "InputFileUrl": input_file_url,
            "VpcId": vpc_id,
            "HaEnable": ha_enable,
            "Name": name,
            "SchedulerType": scheduler_type,
            "VolumeId": volume_id,
            "VolumeMountpoint": volume_mountpoint,
            "EcsOrder.Login.InstanceType": ecs_order_login_instance_type,
            "ZoneId": zone_id}
        repeat_info = {"AdditionalVolumes": ('AdditionalVolumes',
                                             'list',
                                             'dict',
                                             [('VolumeType',
                                               'str',
                                               None,
                                               None),
                                              ('VolumeProtocol',
                                               'str',
                                               None,
                                               None),
                                                 ('LocalDirectory',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('RemoteDirectory',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('Roles',
                                                  'list',
                                                  'dict',
                                                  [('Name',
                                                    'str',
                                                    None,
                                                    None),
                                                   ],
                                                  ),
                                                 ('VolumeId',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('VolumeMountpoint',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('Location',
                                                  'str',
                                                  None,
                                                  None),
                                                 ('JobQueue',
                                                  'str',
                                                  None,
                                                  None),
                                              ]),
                       "PostInstallScript": ('PostInstallScript',
                                             'list',
                                             'dict',
                                             [('Args',
                                               'str',
                                               None,
                                               None),
                                              ('Url',
                                                 'str',
                                                 None,
                                                 None),
                                              ]),
                       "Application": ('Application',
                                       'list',
                                       'dict',
                                       [('Tag',
                                         'str',
                                         None,
                                         None),
                                        ]),
                       }
        verify_params(api_request._params, repeat_info)
        return self._handle_request(api_request).result

    def rerun_jobs(self, jobs=None, cluster_id=None):
        api_request = APIRequest('RerunJobs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Jobs": jobs, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def delete_job_templates(self, templates=None):
        api_request = APIRequest('DeleteJobTemplates', 'GET', 'http', 'RPC', 'query')
        api_request._params = {"Templates": templates}
        return self._handle_request(api_request).result

    def list_cluster_logs(self, page_size=None, cluster_id=None, page_number=None):
        api_request = APIRequest('ListClusterLogs', 'GET', 'http', 'RPC', 'query')
        api_request._params = {
            "PageSize": page_size,
            "ClusterId": cluster_id,
            "PageNumber": page_number}
        return self._handle_request(api_request).result
