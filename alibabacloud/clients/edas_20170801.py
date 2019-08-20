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


class EdasClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, retry_policy=None,
                 endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    retry_policy=retry_policy,
                                    endpoint_resolver=endpoint_resolver)
        self.product_code = 'Edas'
        self.api_version = '2017-08-01'
        self.location_service_code = 'edas'
        self.location_endpoint_type = 'openAPI'

    def get_scaling_rules(self, mode=None, app_id=None, group_id=None):
        api_request = APIRequest('GetScalingRules', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/scalingRules'
        api_request._params = {"Mode": mode, "AppId": app_id, "GroupId": group_id}
        return self._handle_request(api_request).result

    def modify_scaling_rule(
            self,
            in_step=None,
            out_instance_num=None,
            out_rt=None,
            in_instance_num=None,
            vswitch_ids=None,
            template_instance_id=None,
            accept_eula=None,
            out_step=None,
            out_cpu=None,
            key_pair_name=None,
            password=None,
            template_version=None,
            in_condition=None,
            in_rt=None,
            in_cpu=None,
            out_duration=None,
            multi_az_policy=None,
            out_load=None,
            in_load=None,
            group_id=None,
            resource_from=None,
            out_enable=None,
            template_id=None,
            scaling_policy=None,
            out_condition=None,
            in_duration=None,
            in_enable=None,
            app_id=None,
            vpc_id=None,
            template_instance_name=None):
        api_request = APIRequest('ModifyScalingRule', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/scaling_rules2'
        api_request._params = {
            "InStep": in_step,
            "OutInstanceNum": out_instance_num,
            "OutRT": out_rt,
            "InInstanceNum": in_instance_num,
            "VSwitchIds": vswitch_ids,
            "TemplateInstanceId": template_instance_id,
            "AcceptEULA": accept_eula,
            "OutStep": out_step,
            "OutCPU": out_cpu,
            "KeyPairName": key_pair_name,
            "Password": password,
            "TemplateVersion": template_version,
            "InCondition": in_condition,
            "InRT": in_rt,
            "InCpu": in_cpu,
            "OutDuration": out_duration,
            "MultiAzPolicy": multi_az_policy,
            "OutLoad": out_load,
            "InLoad": in_load,
            "GroupId": group_id,
            "ResourceFrom": resource_from,
            "OutEnable": out_enable,
            "TemplateId": template_id,
            "ScalingPolicy": scaling_policy,
            "OutCondition": out_condition,
            "InDuration": in_duration,
            "InEnable": in_enable,
            "AppId": app_id,
            "VpcId": vpc_id,
            "TemplateInstanceName": template_instance_name}
        return self._handle_request(api_request).result

    def list_methods(self, app_id=None, service_name=None):
        api_request = APIRequest('ListMethods', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/service/list_methods'
        api_request._params = {"AppId": app_id, "ServiceName": service_name}
        return self._handle_request(api_request).result

    def get_k8s_application(self, app_id=None, from_=None):
        api_request = APIRequest('GetK8sApplication', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/co_application'
        api_request._params = {"AppId": app_id, "From": from_}
        return self._handle_request(api_request).result

    def query_ecc_info(self, ecc_id=None):
        api_request = APIRequest('QueryEccInfo', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/ecc'
        api_request._params = {"EccId": ecc_id}
        return self._handle_request(api_request).result

    def continue_pipeline(self, confirm=None, pipeline_id=None):
        api_request = APIRequest('ContinuePipeline', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/pipeline_batch_confirm'
        api_request._params = {"Confirm": confirm, "PipelineId": pipeline_id}
        return self._handle_request(api_request).result

    def change_deploy_group(self, force_status=None, app_id=None, ecc_info=None, group_name=None):
        api_request = APIRequest('ChangeDeployGroup', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/co_change_group'
        api_request._params = {
            "ForceStatus": force_status,
            "AppId": app_id,
            "EccInfo": ecc_info,
            "GroupName": group_name}
        return self._handle_request(api_request).result

    def get_cluster(self, cluster_id=None):
        api_request = APIRequest('GetCluster', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/cluster'
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def query_region_config(self,):
        api_request = APIRequest('QueryRegionConfig', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/region_config'

        return self._handle_request(api_request).result

    def synchronize_resource(self, type_=None):
        api_request = APIRequest('SynchronizeResource', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/pop_sync_resource'
        api_request._params = {"Type": type_}
        return self._handle_request(api_request).result

    def create_serverless_application(
            self,
            web_container=None,
            jar_start_args=None,
            memory=None,
            command_args=None,
            replicas=None,
            readiness=None,
            liveness=None,
            cpu=None,
            envs=None,
            package_version=None,
            command=None,
            custom_host_alias=None,
            deploy=None,
            vswitch_id=None,
            jdk=None,
            app_description=None,
            jar_start_options=None,
            edas_container_version=None,
            app_name=None,
            namespace_id=None,
            package_url=None,
            vpc_id=None,
            image_url=None,
            package_type=None):
        api_request = APIRequest('CreateServerlessApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/pop/pop_serverless_app_create_without_deploy'
        api_request._params = {
            "WebContainer": web_container,
            "JarStartArgs": jar_start_args,
            "Memory": memory,
            "CommandArgs": command_args,
            "Replicas": replicas,
            "Readiness": readiness,
            "Liveness": liveness,
            "Cpu": cpu,
            "Envs": envs,
            "PackageVersion": package_version,
            "Command": command,
            "CustomHostAlias": custom_host_alias,
            "Deploy": deploy,
            "VSwitchId": vswitch_id,
            "Jdk": jdk,
            "AppDescription": app_description,
            "JarStartOptions": jar_start_options,
            "EdasContainerVersion": edas_container_version,
            "AppName": app_name,
            "NamespaceId": namespace_id,
            "PackageUrl": package_url,
            "VpcId": vpc_id,
            "ImageUrl": image_url,
            "PackageType": package_type}
        return self._handle_request(api_request).result

    def deploy_serverless_application(
            self,
            web_container=None,
            jar_start_args=None,
            command_args=None,
            readiness=None,
            batch_wait_time=None,
            liveness=None,
            envs=None,
            package_version=None,
            command=None,
            custom_host_alias=None,
            jdk=None,
            jar_start_options=None,
            min_ready_instances=None,
            edas_container_version=None,
            package_url=None,
            app_id=None,
            image_url=None):
        api_request = APIRequest('DeployServerlessApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/pop/pop_serverless_app_deploy'
        api_request._params = {
            "WebContainer": web_container,
            "JarStartArgs": jar_start_args,
            "CommandArgs": command_args,
            "Readiness": readiness,
            "BatchWaitTime": batch_wait_time,
            "Liveness": liveness,
            "Envs": envs,
            "PackageVersion": package_version,
            "Command": command,
            "CustomHostAlias": custom_host_alias,
            "Jdk": jdk,
            "JarStartOptions": jar_start_options,
            "MinReadyInstances": min_ready_instances,
            "EdasContainerVersion": edas_container_version,
            "PackageUrl": package_url,
            "AppId": app_id,
            "ImageUrl": image_url}
        return self._handle_request(api_request).result

    def get_serverless_app_config_detail(self, app_id=None):
        api_request = APIRequest('GetServerlessAppConfigDetail', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/pop/pop_serverless_app_config_detail'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def insert_serverless_application(
            self,
            web_container=None,
            jar_start_args=None,
            memory=None,
            build_pack_id=None,
            command_args=None,
            replicas=None,
            readiness=None,
            liveness=None,
            cpu=None,
            envs=None,
            package_version=None,
            command=None,
            custom_host_alias=None,
            deploy=None,
            vswitch_id=None,
            jdk=None,
            app_description=None,
            jar_start_options=None,
            app_name=None,
            namespace_id=None,
            package_url=None,
            vpc_id=None,
            image_url=None,
            package_type=None):
        api_request = APIRequest('InsertServerlessApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/pop/pop_serverless_app_create_without_deploy'
        api_request._params = {
            "WebContainer": web_container,
            "JarStartArgs": jar_start_args,
            "Memory": memory,
            "BuildPackId": build_pack_id,
            "CommandArgs": command_args,
            "Replicas": replicas,
            "Readiness": readiness,
            "Liveness": liveness,
            "Cpu": cpu,
            "Envs": envs,
            "PackageVersion": package_version,
            "Command": command,
            "CustomHostAlias": custom_host_alias,
            "Deploy": deploy,
            "VSwitchId": vswitch_id,
            "Jdk": jdk,
            "AppDescription": app_description,
            "JarStartOptions": jar_start_options,
            "AppName": app_name,
            "NamespaceId": namespace_id,
            "PackageUrl": package_url,
            "VpcId": vpc_id,
            "ImageUrl": image_url,
            "PackageType": package_type}
        return self._handle_request(api_request).result

    def scale_serverless_application(self, replicas=None, app_id=None):
        api_request = APIRequest('ScaleServerlessApplication', 'PUT', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/pop/pop_serverless_app_rescale'
        api_request._params = {"Replicas": replicas, "AppId": app_id}
        return self._handle_request(api_request).result

    def unbind_serverless_slb(self, intranet=None, app_id=None, internet=None):
        api_request = APIRequest('UnbindServerlessSlb', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/acs/serverless_slb_binding'
        api_request._params = {"Intranet": intranet, "AppId": app_id, "Internet": internet}
        return self._handle_request(api_request).result

    def delete_serverless_application(self, act=None, app_id=None):
        api_request = APIRequest('DeleteServerlessApplication', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/pop/pop_serverless_app_delete'
        api_request._params = {"Act": act, "AppId": app_id}
        return self._handle_request(api_request).result

    def bind_serverless_slb(self, intranet=None, app_id=None, internet=None):
        api_request = APIRequest('BindServerlessSlb', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/acs/serverless_slb_binding'
        api_request._params = {"Intranet": intranet, "AppId": app_id, "Internet": internet}
        return self._handle_request(api_request).result

    def install_agent(self, instance_ids=None, do_async=None, cluster_id=None):
        api_request = APIRequest('InstallAgent', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/ecss/install_agent'
        api_request._params = {
            "InstanceIds": instance_ids,
            "DoAsync": do_async,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_components(self,):
        api_request = APIRequest('ListComponents', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/resource/components'

        return self._handle_request(api_request).result

    def get_package_storage_credential(self,):
        api_request = APIRequest('GetPackageStorageCredential', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/package_storage_credential'

        return self._handle_request(api_request).result

    def list_ecs_not_in_cluster(self, vpc_id=None, network_mode=None):
        api_request = APIRequest('ListEcsNotInCluster', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/ecs_not_in_cluster'
        api_request._params = {"VpcId": vpc_id, "NetworkMode": network_mode}
        return self._handle_request(api_request).result

    def insert_k8s_application(
            self,
            nas_id=None,
            repo_id=None,
            internet_target_port=None,
            web_container=None,
            intranet_slb_id=None,
            command_args=None,
            readiness=None,
            liveness=None,
            internet_slb_port=None,
            envs=None,
            requests_mem=None,
            package_version=None,
            storage_type=None,
            limit_mem=None,
            edas_container_version=None,
            app_name=None,
            internet_slb_id=None,
            logical_region_id=None,
            package_url=None,
            internet_slb_protocol=None,
            intranet_slb_port=None,
            pre_stop=None,
            mount_descs=None,
            replicas=None,
            limit_cpu=None,
            cluster_id=None,
            intranet_target_port=None,
            local_volume=None,
            command=None,
            jdk=None,
            intranet_slb_protocol=None,
            image_url=None,
            namespace=None,
            application_description=None,
            package_type=None,
            requests_cpu=None,
            post_start=None):
        api_request = APIRequest('InsertK8sApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/acs/create_k8s_app'
        api_request._params = {
            "NasId": nas_id,
            "RepoId": repo_id,
            "InternetTargetPort": internet_target_port,
            "WebContainer": web_container,
            "IntranetSlbId": intranet_slb_id,
            "CommandArgs": command_args,
            "Readiness": readiness,
            "Liveness": liveness,
            "InternetSlbPort": internet_slb_port,
            "Envs": envs,
            "RequestsMem": requests_mem,
            "PackageVersion": package_version,
            "StorageType": storage_type,
            "LimitMem": limit_mem,
            "EdasContainerVersion": edas_container_version,
            "AppName": app_name,
            "InternetSlbId": internet_slb_id,
            "LogicalRegionId": logical_region_id,
            "PackageUrl": package_url,
            "InternetSlbProtocol": internet_slb_protocol,
            "IntranetSlbPort": intranet_slb_port,
            "PreStop": pre_stop,
            "MountDescs": mount_descs,
            "Replicas": replicas,
            "LimitCpu": limit_cpu,
            "ClusterId": cluster_id,
            "IntranetTargetPort": intranet_target_port,
            "LocalVolume": local_volume,
            "Command": command,
            "JDK": jdk,
            "IntranetSlbProtocol": intranet_slb_protocol,
            "ImageUrl": image_url,
            "Namespace": namespace,
            "ApplicationDescription": application_description,
            "PackageType": package_type,
            "RequestsCpu": requests_cpu,
            "PostStart": post_start}
        return self._handle_request(api_request).result

    def import_k8s_cluster(self, namespace_id=None, cluster_id=None):
        api_request = APIRequest('ImportK8sCluster', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/import_k8s_cluster'
        api_request._params = {"NamespaceId": namespace_id, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def update_k8s_application_config(
            self,
            app_id=None,
            memory_limit=None,
            cluster_id=None,
            cpu_limit=None):
        api_request = APIRequest('UpdateK8sApplicationConfig', 'PUT', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/acs/k8s_app_configuration'
        api_request._params = {
            "AppId": app_id,
            "MemoryLimit": memory_limit,
            "ClusterId": cluster_id,
            "CpuLimit": cpu_limit}
        return self._handle_request(api_request).result

    def deploy_k8s_application(
            self,
            nas_id=None,
            web_container=None,
            readiness=None,
            batch_wait_time=None,
            liveness=None,
            envs=None,
            cpu_limit=None,
            package_version=None,
            storage_type=None,
            edas_container_version=None,
            package_url=None,
            memory_limit=None,
            image_tag=None,
            memory_request=None,
            image=None,
            pre_stop=None,
            mount_descs=None,
            replicas=None,
            cpu_request=None,
            local_volume=None,
            command=None,
            args=None,
            jdk=None,
            app_id=None,
            post_start=None):
        api_request = APIRequest('DeployK8sApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/acs/k8s_apps'
        api_request._params = {
            "NasId": nas_id,
            "WebContainer": web_container,
            "Readiness": readiness,
            "BatchWaitTime": batch_wait_time,
            "Liveness": liveness,
            "Envs": envs,
            "CpuLimit": cpu_limit,
            "PackageVersion": package_version,
            "StorageType": storage_type,
            "EdasContainerVersion": edas_container_version,
            "PackageUrl": package_url,
            "MemoryLimit": memory_limit,
            "ImageTag": image_tag,
            "MemoryRequest": memory_request,
            "Image": image,
            "PreStop": pre_stop,
            "MountDescs": mount_descs,
            "Replicas": replicas,
            "CpuRequest": cpu_request,
            "LocalVolume": local_volume,
            "Command": command,
            "Args": args,
            "JDK": jdk,
            "AppId": app_id,
            "PostStart": post_start}
        return self._handle_request(api_request).result

    def scale_k8s_application(self, replicas=None, app_id=None):
        api_request = APIRequest('ScaleK8sApplication', 'PUT', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/acs/k8s_apps'
        api_request._params = {"Replicas": replicas, "AppId": app_id}
        return self._handle_request(api_request).result

    def delete_k8s_application(self, app_id=None):
        api_request = APIRequest('DeleteK8sApplication', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/acs/k8s_apps'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def unbind_k8s_slb(self, app_id=None, cluster_id=None, type_=None):
        api_request = APIRequest('UnbindK8sSlb', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/acs/k8s_slb_binding'
        api_request._params = {"AppId": app_id, "ClusterId": cluster_id, "Type": type_}
        return self._handle_request(api_request).result

    def bind_k8s_slb(
            self,
            slb_id=None,
            slb_protocol=None,
            port=None,
            app_id=None,
            cluster_id=None,
            type_=None,
            target_port=None):
        api_request = APIRequest('BindK8sSlb', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/acs/k8s_slb_binding'
        api_request._params = {
            "SlbId": slb_id,
            "SlbProtocol": slb_protocol,
            "Port": port,
            "AppId": app_id,
            "ClusterId": cluster_id,
            "Type": type_,
            "TargetPort": target_port}
        return self._handle_request(api_request).result

    def update_k8s_slb(
            self,
            slb_protocol=None,
            port=None,
            app_id=None,
            cluster_id=None,
            type_=None,
            target_port=None):
        api_request = APIRequest('UpdateK8sSlb', 'PUT', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/k8s/acs/k8s_slb_binding'
        api_request._params = {
            "SlbProtocol": slb_protocol,
            "Port": port,
            "AppId": app_id,
            "ClusterId": cluster_id,
            "Type": type_,
            "TargetPort": target_port}
        return self._handle_request(api_request).result

    def get_secure_token(self, namespace_id=None):
        api_request = APIRequest('GetSecureToken', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/secure_token'
        api_request._params = {"NamespaceId": namespace_id}
        return self._handle_request(api_request).result

    def transform_cluster_member(self, password=None, instance_ids=None, target_cluster_id=None):
        api_request = APIRequest('TransformClusterMember', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/transform_cluster_member'
        api_request._params = {
            "Password": password,
            "InstanceIds": instance_ids,
            "TargetClusterId": target_cluster_id}
        return self._handle_request(api_request).result

    def list_convertable_ecu(self, cluster_id=None):
        api_request = APIRequest('ListConvertableEcu', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/convertable_ecu_list'
        api_request._params = {"clusterId": cluster_id}
        return self._handle_request(api_request).result

    def insert_cluster_member(self, password=None, instance_ids=None, cluster_id=None):
        api_request = APIRequest('InsertClusterMember', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/cluster_member'
        api_request._params = {
            "password": password,
            "instanceIds": instance_ids,
            "clusterId": cluster_id}
        return self._handle_request(api_request).result

    def update_role(self, role_id=None, action_data=None):
        api_request = APIRequest('UpdateRole', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/account/edit_role'
        api_request._params = {"RoleId": role_id, "ActionData": action_data}
        return self._handle_request(api_request).result

    def update_jvm_configuration(
            self,
            min_heap_size=None,
            app_id=None,
            group_id=None,
            options=None,
            max_perm_size=None,
            max_heap_size=None):
        api_request = APIRequest('UpdateJvmConfiguration', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/app_jvm_config'
        api_request._params = {
            "MinHeapSize": min_heap_size,
            "AppId": app_id,
            "GroupId": group_id,
            "Options": options,
            "MaxPermSize": max_perm_size,
            "MaxHeapSize": max_heap_size}
        return self._handle_request(api_request).result

    def update_health_check_url(self, app_id=None, hc_url=None):
        api_request = APIRequest('UpdateHealthCheckUrl', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/modify_hc_url'
        api_request._params = {"AppId": app_id, "hcURL": hc_url}
        return self._handle_request(api_request).result

    def update_flow_control(
            self,
            consumer_app_id=None,
            granularity=None,
            rule_type=None,
            app_id=None,
            url_var=None,
            service_name=None,
            threshold=None,
            rule_id=None,
            strategy=None,
            method_name=None):
        api_request = APIRequest('UpdateFlowControl', 'PUT', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/flowControl'
        api_request._params = {
            "ConsumerAppId": consumer_app_id,
            "Granularity": granularity,
            "RuleType": rule_type,
            "AppId": app_id,
            "UrlVar": url_var,
            "ServiceName": service_name,
            "Threshold": threshold,
            "RuleId": rule_id,
            "Strategy": strategy,
            "MethodName": method_name}
        return self._handle_request(api_request).result

    def update_degrade_control(
            self,
            duration=None,
            rule_type=None,
            app_id=None,
            url_var=None,
            rt_threshold=None,
            service_name=None,
            rule_id=None,
            method_name=None):
        api_request = APIRequest('UpdateDegradeControl', 'PUT', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/degradeControl'
        api_request._params = {
            "Duration": duration,
            "RuleType": rule_type,
            "AppId": app_id,
            "UrlVar": url_var,
            "RtThreshold": rt_threshold,
            "ServiceName": service_name,
            "RuleId": rule_id,
            "MethodName": method_name}
        return self._handle_request(api_request).result

    def update_container_configuration(
            self,
            use_body_encoding=None,
            max_threads=None,
            uri_encoding=None,
            app_id=None,
            group_id=None,
            http_port=None,
            context_path=None):
        api_request = APIRequest('UpdateContainerConfiguration', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/container_config'
        api_request._params = {
            "UseBodyEncoding": use_body_encoding,
            "MaxThreads": max_threads,
            "URIEncoding": uri_encoding,
            "AppId": app_id,
            "GroupId": group_id,
            "HttpPort": http_port,
            "ContextPath": context_path}
        return self._handle_request(api_request).result

    def update_application_base_info(self, app_name=None, app_id=None, desc=None):
        api_request = APIRequest('UpdateApplicationBaseInfo', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/update_app_info'
        api_request._params = {"AppName": app_name, "AppId": app_id, "desc": desc}
        return self._handle_request(api_request).result

    def update_account_info(self, name=None, telephone=None, email=None):
        api_request = APIRequest('UpdateAccountInfo', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/account/edit_account_info'
        api_request._params = {"Name": name, "Telephone": telephone, "Email": email}
        return self._handle_request(api_request).result

    def unbind_slb(self, slb_id=None, app_id=None, type_=None):
        api_request = APIRequest('UnbindSlb', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/app/unbind_slb_json'
        api_request._params = {"SlbId": slb_id, "AppId": app_id, "Type": type_}
        return self._handle_request(api_request).result

    def rollback_application(
            self,
            app_id=None,
            group_id=None,
            batch_wait_time=None,
            batch=None,
            history_version=None):
        api_request = APIRequest('RollbackApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/co_rollback'
        api_request._params = {
            "AppId": app_id,
            "GroupId": group_id,
            "BatchWaitTime": batch_wait_time,
            "Batch": batch,
            "HistoryVersion": history_version}
        return self._handle_request(api_request).result

    def query_monitor_info(
            self,
            metric=None,
            aggregator=None,
            start=None,
            end=None,
            interval=None,
            tags=None):
        api_request = APIRequest('QueryMonitorInfo', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/monitor/queryMonitorInfo'
        api_request._params = {
            "Metric": metric,
            "Aggregator": aggregator,
            "Start": start,
            "End": end,
            "Interval": interval,
            "Tags": tags}
        return self._handle_request(api_request).result

    def query_migrate_region_list(self, logical_region_id=None):
        api_request = APIRequest('QueryMigrateRegionList', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/migrate_region_select'
        api_request._params = {"LogicalRegionId": logical_region_id}
        return self._handle_request(api_request).result

    def query_migrate_ecu_list(self, logical_region_id=None):
        api_request = APIRequest('QueryMigrateEcuList', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/migrate_ecu_list'
        api_request._params = {"LogicalRegionId": logical_region_id}
        return self._handle_request(api_request).result

    def query_config_center(self, data_id=None, logical_region_id=None, group=None):
        api_request = APIRequest('QueryConfigCenter', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/configCenter'
        api_request._params = {
            "DataId": data_id,
            "LogicalRegionId": logical_region_id,
            "Group": group}
        return self._handle_request(api_request).result

    def query_application_status(self, app_id=None):
        api_request = APIRequest('QueryApplicationStatus', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/app_status'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def migrate_ecu(self, instance_ids=None, logical_region_id=None):
        api_request = APIRequest('MigrateEcu', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/migrate_ecu'
        api_request._params = {"InstanceIds": instance_ids, "LogicalRegionId": logical_region_id}
        return self._handle_request(api_request).result

    def list_user_define_region(self, debug_enable=None):
        api_request = APIRequest('ListUserDefineRegion', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/user_region_defs'
        api_request._params = {"DebugEnable": debug_enable}
        return self._handle_request(api_request).result

    def list_sub_account(self,):
        api_request = APIRequest('ListSubAccount', 'POST', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/account/sub_account_list'

        return self._handle_request(api_request).result

    def list_slb(self,):
        api_request = APIRequest('ListSlb', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/slb_list'

        return self._handle_request(api_request).result

    def list_service_groups(self,):
        api_request = APIRequest('ListServiceGroups', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/service/serviceGroups'

        return self._handle_request(api_request).result

    def list_scale_out_ecu(
            self,
            mem=None,
            logical_region_id=None,
            app_id=None,
            group_id=None,
            instance_num=None,
            cpu=None,
            cluster_id=None):
        api_request = APIRequest('ListScaleOutEcu', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/scale_out_ecu_list'
        api_request._params = {
            "Mem": mem,
            "LogicalRegionId": logical_region_id,
            "AppId": app_id,
            "GroupId": group_id,
            "InstanceNum": instance_num,
            "Cpu": cpu,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_role(self,):
        api_request = APIRequest('ListRole', 'POST', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/account/role_list'

        return self._handle_request(api_request).result

    def list_resource_group(self,):
        api_request = APIRequest('ListResourceGroup', 'POST', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/resource/reg_group_list'

        return self._handle_request(api_request).result

    def list_recent_change_order(self, app_id=None):
        api_request = APIRequest('ListRecentChangeOrder', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/change_order_list'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def list_published_services(self, app_id=None):
        api_request = APIRequest('ListPublishedServices', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/service/listPublishedServices'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def list_history_deploy_version(self, app_id=None):
        api_request = APIRequest('ListHistoryDeployVersion', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/deploy_history_version_list'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def list_flow_controls(self, app_id=None):
        api_request = APIRequest('ListFlowControls', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/flowControls'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def list_ecu_by_region(self, act=None, logical_region_id=None):
        api_request = APIRequest('ListEcuByRegion', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/ecu_list'
        api_request._params = {"Act": act, "LogicalRegionId": logical_region_id}
        return self._handle_request(api_request).result

    def list_degrade_controls(self, app_id=None):
        api_request = APIRequest('ListDegradeControls', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/degradeControls'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def list_consumed_services(self, app_id=None):
        api_request = APIRequest('ListConsumedServices', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/service/listConsumedServices'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def list_config_centers(
            self,
            app_name=None,
            logical_region_id=None,
            data_id_pattern=None,
            group=None):
        api_request = APIRequest('ListConfigCenters', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/configCenters'
        api_request._params = {
            "AppName": app_name,
            "LogicalRegionId": logical_region_id,
            "DataIdPattern": data_id_pattern,
            "Group": group}
        return self._handle_request(api_request).result

    def list_cluster_members(self, page_size=None, current_page=None, cluster_id=None):
        api_request = APIRequest('ListClusterMembers', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/cluster_member_list'
        api_request._params = {
            "PageSize": page_size,
            "CurrentPage": current_page,
            "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def list_authority(self,):
        api_request = APIRequest('ListAuthority', 'POST', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/account/authority_list'

        return self._handle_request(api_request).result

    def list_aliyun_region(self,):
        api_request = APIRequest('ListAliyunRegion', 'POST', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/resource/region_list'

        return self._handle_request(api_request).result

    def insert_service_group(self, group_name=None):
        api_request = APIRequest('InsertServiceGroup', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/service/serviceGroups'
        api_request._params = {"GroupName": group_name}
        return self._handle_request(api_request).result

    def insert_role(self, role_name=None, action_data=None):
        api_request = APIRequest('InsertRole', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/account/create_role'
        api_request._params = {"RoleName": role_name, "ActionData": action_data}
        return self._handle_request(api_request).result

    def insert_or_update_region(
            self,
            debug_enable=None,
            region_tag=None,
            region_name=None,
            description=None,
            id_=None):
        api_request = APIRequest('InsertOrUpdateRegion', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/user_region_def'
        api_request._params = {
            "DebugEnable": debug_enable,
            "RegionTag": region_tag,
            "RegionName": region_name,
            "Description": description,
            "Id": id_}
        return self._handle_request(api_request).result

    def insert_config_center(
            self,
            data_id=None,
            data=None,
            app_name=None,
            logical_region_id=None,
            group=None):
        api_request = APIRequest('InsertConfigCenter', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/configCenter'
        api_request._params = {
            "DataId": data_id,
            "Data": data,
            "AppName": app_name,
            "LogicalRegionId": logical_region_id,
            "Group": group}
        return self._handle_request(api_request).result

    def insert_flow_control(
            self,
            consumer_app_id=None,
            granularity=None,
            rule_type=None,
            app_id=None,
            url_var=None,
            service_name=None,
            threshold=None,
            strategy=None,
            method_name=None):
        api_request = APIRequest('InsertFlowControl', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/flowControl'
        api_request._params = {
            "ConsumerAppId": consumer_app_id,
            "Granularity": granularity,
            "RuleType": rule_type,
            "AppId": app_id,
            "UrlVar": url_var,
            "ServiceName": service_name,
            "Threshold": threshold,
            "Strategy": strategy,
            "MethodName": method_name}
        return self._handle_request(api_request).result

    def insert_deploy_group(self, app_id=None, group_name=None):
        api_request = APIRequest('InsertDeployGroup', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/deploy_group'
        api_request._params = {"AppId": app_id, "GroupName": group_name}
        return self._handle_request(api_request).result

    def insert_degrade_control(
            self,
            duration=None,
            rule_type=None,
            app_id=None,
            url_var=None,
            rt_threshold=None,
            service_name=None,
            method_name=None):
        api_request = APIRequest('InsertDegradeControl', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/degradeControl'
        api_request._params = {
            "Duration": duration,
            "RuleType": rule_type,
            "AppId": app_id,
            "UrlVar": url_var,
            "RtThreshold": rt_threshold,
            "ServiceName": service_name,
            "MethodName": method_name}
        return self._handle_request(api_request).result

    def insert_cluster(
            self,
            cluster_type=None,
            iaas_provider=None,
            logical_region_id=None,
            cluster_name=None,
            vpc_id=None,
            network_mode=None,
            oversold_factor=None):
        api_request = APIRequest('InsertCluster', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/cluster'
        api_request._params = {
            "ClusterType": cluster_type,
            "IaasProvider": iaas_provider,
            "LogicalRegionId": logical_region_id,
            "ClusterName": cluster_name,
            "VpcId": vpc_id,
            "NetworkMode": network_mode,
            "OversoldFactor": oversold_factor}
        return self._handle_request(api_request).result

    def get_jvm_configuration(self, app_id=None, group_id=None):
        api_request = APIRequest('GetJvmConfiguration', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/app_jvm_config'
        api_request._params = {"AppId": app_id, "GroupId": group_id}
        return self._handle_request(api_request).result

    def get_container_configuration(self, app_id=None, group_id=None):
        api_request = APIRequest('GetContainerConfiguration', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/container_config'
        api_request._params = {"AppId": app_id, "GroupId": group_id}
        return self._handle_request(api_request).result

    def get_application(self, app_id=None):
        api_request = APIRequest('GetApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/app_info'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def enable_flow_control(self, app_id=None, rule_id=None):
        api_request = APIRequest('EnableFlowControl', 'PUT', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/flowcontrol/enable'
        api_request._params = {"AppId": app_id, "RuleId": rule_id}
        return self._handle_request(api_request).result

    def enable_degrade_control(self, app_id=None, rule_id=None):
        api_request = APIRequest('EnableDegradeControl', 'PUT', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/degradecontrol/enable'
        api_request._params = {"AppId": app_id, "RuleId": rule_id}
        return self._handle_request(api_request).result

    def disable_flow_control(self, app_id=None, rule_id=None):
        api_request = APIRequest('DisableFlowControl', 'PUT', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/flowcontrol/disable'
        api_request._params = {"AppId": app_id, "RuleId": rule_id}
        return self._handle_request(api_request).result

    def disable_degrade_control(self, app_id=None, rule_id=None):
        api_request = APIRequest('DisableDegradeControl', 'PUT', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/degradecontrol/disable'
        api_request._params = {"AppId": app_id, "RuleId": rule_id}
        return self._handle_request(api_request).result

    def delete_user_define_region(self, region_tag=None, id_=None):
        api_request = APIRequest('DeleteUserDefineRegion', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/user_region_def'
        api_request._params = {"RegionTag": region_tag, "Id": id_}
        return self._handle_request(api_request).result

    def delete_service_group(self, group_id=None):
        api_request = APIRequest('DeleteServiceGroup', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/service/serviceGroups'
        api_request._params = {"GroupId": group_id}
        return self._handle_request(api_request).result

    def delete_role(self, role_id=None):
        api_request = APIRequest('DeleteRole', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/account/delete_role'
        api_request._params = {"RoleId": role_id}
        return self._handle_request(api_request).result

    def delete_flow_control(self, app_id=None, rule_id=None):
        api_request = APIRequest('DeleteFlowControl', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/flowControl'
        api_request._params = {"AppId": app_id, "RuleId": rule_id}
        return self._handle_request(api_request).result

    def delete_ecu(self, ecu_id=None):
        api_request = APIRequest('DeleteEcu', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/delete_ecu'
        api_request._params = {"EcuId": ecu_id}
        return self._handle_request(api_request).result

    def delete_deploy_group(self, app_id=None, group_name=None):
        api_request = APIRequest('DeleteDeployGroup', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/deploy_group'
        api_request._params = {"AppId": app_id, "GroupName": group_name}
        return self._handle_request(api_request).result

    def delete_degrade_control(self, app_id=None, rule_id=None):
        api_request = APIRequest('DeleteDegradeControl', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/degradeControl'
        api_request._params = {"AppId": app_id, "RuleId": rule_id}
        return self._handle_request(api_request).result

    def delete_config_center(self, data_id=None, logical_region_id=None, group=None):
        api_request = APIRequest('DeleteConfigCenter', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/configCenter'
        api_request._params = {
            "DataId": data_id,
            "LogicalRegionId": logical_region_id,
            "Group": group}
        return self._handle_request(api_request).result

    def delete_cluster_member(self, cluster_member_id=None, cluster_id=None):
        api_request = APIRequest('DeleteClusterMember', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/cluster_member'
        api_request._params = {"ClusterMemberId": cluster_member_id, "ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def delete_cluster(self, cluster_id=None):
        api_request = APIRequest('DeleteCluster', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/cluster'
        api_request._params = {"ClusterId": cluster_id}
        return self._handle_request(api_request).result

    def bind_slb(
            self,
            vserver_group_id=None,
            listener_port=None,
            slb_id=None,
            app_id=None,
            slb_ip=None,
            type_=None):
        api_request = APIRequest('BindSlb', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/app/bind_slb_json'
        api_request._params = {
            "VServerGroupId": vserver_group_id,
            "ListenerPort": listener_port,
            "SlbId": slb_id,
            "AppId": app_id,
            "SlbIp": slb_ip,
            "Type": type_}
        return self._handle_request(api_request).result

    def authorize_role(self, role_ids=None, target_user_id=None):
        api_request = APIRequest('AuthorizeRole', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/account/authorize_role'
        api_request._params = {"RoleIds": role_ids, "TargetUserId": target_user_id}
        return self._handle_request(api_request).result

    def authorize_resource_group(self, resource_group_ids=None, target_user_id=None):
        api_request = APIRequest('AuthorizeResourceGroup', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/account/authorize_res_group'
        api_request._params = {
            "ResourceGroupIds": resource_group_ids,
            "TargetUserId": target_user_id}
        return self._handle_request(api_request).result

    def authorize_application(self, app_ids=None, target_user_id=None):
        api_request = APIRequest('AuthorizeApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/account/authorize_app'
        api_request._params = {"AppIds": app_ids, "TargetUserId": target_user_id}
        return self._handle_request(api_request).result

    def list_vpc(self,):
        api_request = APIRequest('ListVpc', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/vpc_list'

        return self._handle_request(api_request).result

    def scale_out_application(self, ecu_info=None, deploy_group=None, app_id=None):
        api_request = APIRequest('ScaleOutApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/co_scale_out'
        api_request._params = {"EcuInfo": ecu_info, "DeployGroup": deploy_group, "AppId": app_id}
        return self._handle_request(api_request).result

    def scale_in_application(self, force_status=None, app_id=None, ecc_info=None):
        api_request = APIRequest('ScaleInApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/co_scale_in'
        api_request._params = {"ForceStatus": force_status, "AppId": app_id, "EccInfo": ecc_info}
        return self._handle_request(api_request).result

    def deploy_application(
            self,
            build_pack_id=None,
            component_ids=None,
            group_id=None,
            batch_wait_time=None,
            release_type=None,
            batch=None,
            app_env=None,
            package_version=None,
            app_id=None,
            image_url=None,
            war_url=None,
            desc=None,
            deploy_type=None):
        api_request = APIRequest('DeployApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/co_deploy'
        api_request._params = {
            "BuildPackId": build_pack_id,
            "ComponentIds": component_ids,
            "GroupId": group_id,
            "BatchWaitTime": batch_wait_time,
            "ReleaseType": release_type,
            "Batch": batch,
            "AppEnv": app_env,
            "PackageVersion": package_version,
            "AppId": app_id,
            "ImageUrl": image_url,
            "WarUrl": war_url,
            "Desc": desc,
            "DeployType": deploy_type}
        return self._handle_request(api_request).result

    def insert_application(
            self,
            web_container=None,
            ecu_info=None,
            build_pack_id=None,
            health_check_url=None,
            reserved_port_str=None,
            description=None,
            cpu=None,
            cluster_id=None,
            application_name=None,
            jdk=None,
            mem=None,
            logical_region_id=None,
            package_type=None):
        api_request = APIRequest('InsertApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/co_create_app'
        api_request._params = {
            "WebContainer": web_container,
            "EcuInfo": ecu_info,
            "BuildPackId": build_pack_id,
            "HealthCheckURL": health_check_url,
            "ReservedPortStr": reserved_port_str,
            "Description": description,
            "Cpu": cpu,
            "ClusterId": cluster_id,
            "ApplicationName": application_name,
            "Jdk": jdk,
            "Mem": mem,
            "LogicalRegionId": logical_region_id,
            "PackageType": package_type}
        return self._handle_request(api_request).result

    def delete_application(self, app_id=None):
        api_request = APIRequest('DeleteApplication', 'DELETE', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/co_delete_app'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def update_container(self, build_pack_id=None, app_id=None):
        api_request = APIRequest('UpdateContainer', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/co_update_container'
        api_request._params = {"BuildPackId": build_pack_id, "AppId": app_id}
        return self._handle_request(api_request).result

    def stop_application(self, app_id=None, ecc_info=None):
        api_request = APIRequest('StopApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/co_stop'
        api_request._params = {"AppId": app_id, "EccInfo": ecc_info}
        return self._handle_request(api_request).result

    def start_application(self, app_id=None, ecc_info=None):
        api_request = APIRequest('StartApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/co_start'
        api_request._params = {"AppId": app_id, "EccInfo": ecc_info}
        return self._handle_request(api_request).result

    def reset_application(self, app_id=None, ecc_info=None):
        api_request = APIRequest('ResetApplication', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/co_reset'
        api_request._params = {"AppId": app_id, "EccInfo": ecc_info}
        return self._handle_request(api_request).result

    def list_deploy_group(self, app_id=None):
        api_request = APIRequest('ListDeployGroup', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/app/deploy_group_list'
        api_request._params = {"AppId": app_id}
        return self._handle_request(api_request).result

    def list_build_pack(self,):
        api_request = APIRequest('ListBuildPack', 'POST', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/app/build_pack_list'

        return self._handle_request(api_request).result

    def list_application_ecu(self,):
        api_request = APIRequest('ListApplicationEcu', 'POST', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/resource/ecu_list'

        return self._handle_request(api_request).result

    def get_change_order_info(self, change_order_id=None):
        api_request = APIRequest('GetChangeOrderInfo', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/changeorder/change_order_info'
        api_request._params = {"ChangeOrderId": change_order_id}
        return self._handle_request(api_request).result

    def list_cluster(self, logical_region_id=None):
        api_request = APIRequest('ListCluster', 'POST', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/pop/v5/resource/cluster_list'
        api_request._params = {"LogicalRegionId": logical_region_id}
        return self._handle_request(api_request).result

    def list_application(self,):
        api_request = APIRequest('ListApplication', 'POST', 'http', 'ROA', '')
        api_request.uri_pattern = '/pop/v5/app/app_list'

        return self._handle_request(api_request).result
