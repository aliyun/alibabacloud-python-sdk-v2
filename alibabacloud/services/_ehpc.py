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

import json
import time

from alibabacloud.exceptions import ClientException
from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, _create_special_resource_collection
from alibabacloud.resources.collection import _create_default_resource_collection
from alibabacloud.resources.collection import _create_sub_resource_with_page_collection
from alibabacloud.resources.collection import _create_sub_resource_without_page_collection
from alibabacloud.utils.utils import _assert_is_not_none, _new_get_key_in_response, _transfer_params


class _EHPCResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'ehpc', _client=_client)
        self.commands = _create_resource_collection(
            _EHPCCommandResource, _client, _client.list_commands,
            'Commands.Command', 'CommandId', 
        )
        self.gws_instances = _create_resource_collection(
            _EHPCGWSInstanceResource, _client, _client.describe_gws_instances,
            'Instances.InstanceInfo', 'InstanceId', 
        )
        self.regions = _create_special_resource_collection(
            _EHPCRegionResource, _client, _client.list_regions,
            'Regions.RegionInfo', 'RegionId', 
        )
        self.volumes = _create_resource_collection(
            _EHPCVolumeResource, _client, _client.list_volumes,
            'Volumes.VolumeInfo', 'VolumeId', 
        )
    def create_cluster(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_cluster(**_params)
        cluster_id = _new_get_key_in_response(response, 'ClusterId')
        return _EHPCClusterResource(cluster_id, _client=self._client)

    def add_container_app(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_container_app(**_params)
        container_ids = _new_get_key_in_response(response, 'ContainerId.ContainerId')
        container_apps = []
        for container_id in container_ids:
            container_app = _EHPCContainerAppResource(container_id, _client=self._client)
            container_apps.append(container_app)
        return container_apps

    def create_gws_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_gws_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _EHPCGWSInstanceResource(instance_id, _client=self._client)

    def create_job_file(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_job_file(**_params)
        template_id = _new_get_key_in_response(response, 'TemplateId')
        return _EHPCJobFileResource(template_id, _client=self._client)

class _EHPCClusterResource(ServiceResource):

    def __init__(self, cluster_id, _client=None):
        ServiceResource.__init__(self, "ehpc.cluster", _client=_client)
        self.cluster_id = cluster_id
        

        self.queues = _create_sub_resource_without_page_collection(
            _EHPCQueueResource, _client, _client.list_queues,
            'Queues.QueueInfo', 'QueueName', parent_identifier="ClusterId",parent_identifier_value=self.cluster_id
        )
    def add_local_nodes(self, **params):
        _params = _transfer_params(params)
        return self._client.add_local_nodes(cluster_id=self.cluster_id, **_params)

    def add_nodes(self, **params):
        _params = _transfer_params(params)
        return self._client.add_nodes(cluster_id=self.cluster_id, **_params)

    def add_users(self, **params):
        _params = _transfer_params(params)
        return self._client.add_users(cluster_id=self.cluster_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_cluster(cluster_id=self.cluster_id, **_params)

    def delete_gws(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_gws_cluster(cluster_id=self.cluster_id, **_params)

    def delete_image(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_image(cluster_id=self.cluster_id, **_params)

    def delete_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_jobs(cluster_id=self.cluster_id, **_params)

    def delete_nodes(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_nodes(cluster_id=self.cluster_id, **_params)

    def delete_users(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_users(cluster_id=self.cluster_id, **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_cluster(cluster_id=self.cluster_id, **_params)

    def describe_auto_scale_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_auto_scale_config(cluster_id=self.cluster_id, **_params)

    def describe_image(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_image(cluster_id=self.cluster_id, **_params)

    def describe_image_gateway_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_image_gateway_config(cluster_id=self.cluster_id, **_params)

    def get_accounting_report(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_accounting_report(cluster_id=self.cluster_id, **_params)
        return response

    def get_auto_scale_config(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_auto_scale_config(cluster_id=self.cluster_id, **_params)
        return response

    def get_cloud_metric_logs(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_cloud_metric_logs(cluster_id=self.cluster_id, **_params)
        return response

    def get_cloud_metric_profiling(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_cloud_metric_profiling(cluster_id=self.cluster_id, **_params)
        return response

    def get_cluster_volumes(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_cluster_volumes(cluster_id=self.cluster_id, **_params)
        return response

    def get_hybrid_cluster_config(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_hybrid_cluster_config(cluster_id=self.cluster_id, **_params)
        return response

    def get_visual_service_status(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_visual_service_status(cluster_id=self.cluster_id, **_params)
        return response

    def install_software(self, **params):
        _params = _transfer_params(params)
        return self._client.install_software(cluster_id=self.cluster_id, **_params)

    def invoke_shell_command(self, **params):
        _params = _transfer_params(params)
        return self._client.invoke_shell_command(cluster_id=self.cluster_id, **_params)

    def list_cloud_metric_profilings(self, **params):
        _params = _transfer_params(params)
        return self._client.list_cloud_metric_profilings(cluster_id=self.cluster_id, **_params)

    def list_cluster_logs(self, **params):
        _params = _transfer_params(params)
        return self._client.list_cluster_logs(cluster_id=self.cluster_id, **_params)

    def list_container_images(self, **params):
        _params = _transfer_params(params)
        return self._client.list_container_images(cluster_id=self.cluster_id, **_params)

    def list_installed_software(self, **params):
        _params = _transfer_params(params)
        return self._client.list_installed_software(cluster_id=self.cluster_id, **_params)

    def list_invocation_results(self, **params):
        _params = _transfer_params(params)
        return self._client.list_invocation_results(cluster_id=self.cluster_id, **_params)

    def list_invocation_status(self, **params):
        _params = _transfer_params(params)
        return self._client.list_invocation_status(cluster_id=self.cluster_id, **_params)

    def list_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.list_jobs(cluster_id=self.cluster_id, **_params)

    def list_nodes(self, **params):
        _params = _transfer_params(params)
        return self._client.list_nodes(cluster_id=self.cluster_id, **_params)

    def list_nodes_no_paging(self, **params):
        _params = _transfer_params(params)
        return self._client.list_nodes_no_paging(cluster_id=self.cluster_id, **_params)

    def list_users(self, **params):
        _params = _transfer_params(params)
        return self._client.list_users(cluster_id=self.cluster_id, **_params)

    def modify_attributes(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_cluster_attributes(cluster_id=self.cluster_id, **_params)

    def modify_image_gateway_config(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_image_gateway_config(cluster_id=self.cluster_id, **_params)

    def modify_user_groups(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_user_groups(cluster_id=self.cluster_id, **_params)

    def modify_user_passwords(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_user_passwords(cluster_id=self.cluster_id, **_params)

    def modify_visual_service_passwd(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_visual_service_passwd(cluster_id=self.cluster_id, **_params)

    def pull_image(self, **params):
        _params = _transfer_params(params)
        return self._client.pull_image(cluster_id=self.cluster_id, **_params)

    def recover(self, **params):
        _params = _transfer_params(params)
        return self._client.recover_cluster(cluster_id=self.cluster_id, **_params)

    def rerun_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.rerun_jobs(cluster_id=self.cluster_id, **_params)

    def reset_nodes(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_nodes(cluster_id=self.cluster_id, **_params)

    def run_cloud_metric_profiling(self, **params):
        _params = _transfer_params(params)
        return self._client.run_cloud_metric_profiling(cluster_id=self.cluster_id, **_params)

    def set_auto_scale_config(self, **params):
        _params = _transfer_params(params)
        return self._client.set_auto_scale_config(cluster_id=self.cluster_id, **_params)

    def set_job_user(self, **params):
        _params = _transfer_params(params)
        return self._client.set_job_user(cluster_id=self.cluster_id, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        return self._client.start_cluster(cluster_id=self.cluster_id, **_params)

    def start_nodes(self, **params):
        _params = _transfer_params(params)
        return self._client.start_nodes(cluster_id=self.cluster_id, **_params)

    def start_visual_service(self, **params):
        _params = _transfer_params(params)
        return self._client.start_visual_service(cluster_id=self.cluster_id, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_cluster(cluster_id=self.cluster_id, **_params)

    def stop_jobs(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_jobs(cluster_id=self.cluster_id, **_params)

    def stop_nodes(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_nodes(cluster_id=self.cluster_id, **_params)

    def stop_visual_service(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_visual_service(cluster_id=self.cluster_id, **_params)

    def uninstall_software(self, **params):
        _params = _transfer_params(params)
        return self._client.uninstall_software(cluster_id=self.cluster_id, **_params)

    def update_cluster_volumes(self, **params):
        _params = _transfer_params(params)
        return self._client.update_cluster_volumes(cluster_id=self.cluster_id, **_params)

    def upgrade_client(self, **params):
        _params = _transfer_params(params)
        return self._client.upgrade_client(cluster_id=self.cluster_id, **_params)

    def submit_job(self, **params):
        _params = _transfer_params(params)
        response = self._client.submit_job(cluster_id=self.cluster_id,**_params)
        job_id = _new_get_key_in_response(response, 'JobId')
        return _EHPCJobResource(job_id,self.cluster_id, _client=self._client)

    def add_queue(self, **params):
        _params = _transfer_params(params)
        self._client.add_queue(cluster_id=self.cluster_id,**_params)
        queue_name = _params.get("queue_name")
        return _EHPCQueueResource(queue_name,self.cluster_id, _client=self._client)

class _EHPCJobResource(ServiceResource):

    def __init__(self, job_id,cluster_id, _client=None):
        ServiceResource.__init__(self, "ehpc.job", _client=_client)
        self.job_id = job_id
        self.cluster_id = cluster_id

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_job(job_id=self.job_id,cluster_id=self.cluster_id, **_params)

class _EHPCQueueResource(ServiceResource):

    def __init__(self, queue_name,cluster_id, _client=None):
        ServiceResource.__init__(self, "ehpc.queue", _client=_client)
        self.queue_name = queue_name
        self.cluster_id = cluster_id
        self.compute_instance_type = None
        self.resource_group_id = None
        self.type_ = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_queue(queue_name=self.queue_name,cluster_id=self.cluster_id, **_params)

    def list_nodes_by(self, **params):
        _params = _transfer_params(params)
        return self._client.list_nodes_by_queue(queue_name=self.queue_name,cluster_id=self.cluster_id, **_params)

    def set(self, **params):
        _params = _transfer_params(params)
        return self._client.set_queue(queue_name=self.queue_name,cluster_id=self.cluster_id, **_params)

    def update_queue_config(self, **params):
        _params = _transfer_params(params)
        return self._client.update_queue_config(queue_name=self.queue_name,cluster_id=self.cluster_id, **_params)

class _EHPCCommandResource(ServiceResource):

    def __init__(self, command_id, _client=None):
        ServiceResource.__init__(self, "ehpc.command", _client=_client)
        self.command_id = command_id
        
        self.command_content = None
        self.timeout = None
        self.working_dir = None

class _EHPCContainerAppResource(ServiceResource):

    def __init__(self, container_id, _client=None):
        ServiceResource.__init__(self, "ehpc.container_app", _client=_client)
        self.container_id = container_id
        

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_container_app(container_id=self.container_id, **_params)

    def modify_attributes(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_container_app_attributes(container_id=self.container_id, **_params)

class _EHPCGWSInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "ehpc.gws_instance", _client=_client)
        self.instance_id = instance_id
        
        self.app_list = None
        self.cluster_id = None
        self.create_time = None
        self.expire_time = None
        self.instance_type = None
        self.name = None
        self.status = None
        self.user_name = None
        self.work_mode = None

    def create_gws_image(self, **params):
        _params = _transfer_params(params)
        return self._client.create_gws_image(instance_id=self.instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_gws_instance(instance_id=self.instance_id, **_params)

    def describe_nfs_client_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_nfs_client_status(instance_id=self.instance_id, **_params)

    def get_gws_connect_ticket(self, **params):
        _params = _transfer_params(params)
        response = self._client.get_gws_connect_ticket(instance_id=self.instance_id, **_params)
        return response

    def install_nfs_client(self, **params):
        _params = _transfer_params(params)
        return self._client.install_nfs_client(instance_id=self.instance_id, **_params)

    def mount_nfs(self, **params):
        _params = _transfer_params(params)
        return self._client.mount_nfs(instance_id=self.instance_id, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        return self._client.start_gws_instance(instance_id=self.instance_id, **_params)

    def stop(self, **params):
        _params = _transfer_params(params)
        return self._client.stop_gws_instance(instance_id=self.instance_id, **_params)

    def set_gws_instance_user(self, **params):
        _params = _transfer_params(params)
        return self._client.set_gws_instance_user(instance_id=self.instance_id, **_params)

class _EHPCJobFileResource(ServiceResource):

    def __init__(self, template_id, _client=None):
        ServiceResource.__init__(self, "ehpc.job_file", _client=_client)
        self.template_id = template_id
        

    def edit_job_template(self, **params):
        _params = _transfer_params(params)
        return self._client.edit_job_template(template_id=self.template_id, **_params)

class _EHPCRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "ehpc.region", _client=_client)
        self.region_id = region_id
        
        self.local_name = None

class _EHPCVolumeResource(ServiceResource):

    def __init__(self, volume_id, _client=None):
        ServiceResource.__init__(self, "ehpc.volume", _client=_client)
        self.volume_id = volume_id
        
        self.additional_volumes = None
        self.cluster_id = None
        self.cluster_name = None
        self.region_id = None
        self.remote_directory = None
        self.volume_mountpoint = None
        self.volume_protocol = None
        self.volume_type = None
