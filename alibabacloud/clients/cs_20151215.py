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


class CSClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None):
        AlibabaCloudClient.__init__(self, client_config, credentials_provider)
        self.product_code = 'CS'
        self.product_version = '2015-12-15'
        self.location_service_code = 'cs'
        self.location_endpoint_type = 'openAPI'

    def scale_out_cluster(self, cluster_id=None,):
        api_request = APIRequest(
            'ScaleOutCluster', 'POST', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/api/v2/clusters/[ClusterId]'
        api_request._params = {"ClusterId": cluster_id, }
        return self._handle_request(api_request).result

    def get_cluster_cert_info(self, cluster_id=None,):
        api_request = APIRequest(
            'GetClusterCertInfo',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/clusters/[ClusterId]/hosts/certs'
        api_request._params = {"ClusterId": cluster_id, }
        return self._handle_request(api_request).result

    def create_trigger_hook(self,):
        api_request = APIRequest('CreateTriggerHook', 'PUT', 'http', 'ROA', '')
        api_request.uri_pattern = '/hook/trigger'

        return self._handle_request(api_request).result

    def create_cluster_by_resources_group(self, resource_group_id=None,):
        api_request = APIRequest(
            'CreateClusterByResourcesGroup',
            'POST',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/resource_groups/[ResourceGroupId]/clusters'
        api_request._params = {"ResourceGroupId": resource_group_id, }
        return self._handle_request(api_request).result

    def pre_check_for_create_cluster(self,):
        api_request = APIRequest(
            'PreCheckForCreateCluster',
            'POST',
            'http',
            'ROA',
            '')
        api_request.uri_pattern = '/api/v1/ess/precheck'

        return self._handle_request(api_request).result

    def describe_kubernetes_version_metadata(
        self,
        cluster_type=None,
        multi_az=None,
        kubernetes_version=None,
        region=None,
    ):
        api_request = APIRequest(
            'DescribeKubernetesVersionMetadata',
            'GET',
            'http',
            'ROA',
            'query')
        api_request.uri_pattern = '/api/v1/metadata/versions'
        api_request._params = {
            "ClusterType": cluster_type,
            "MultiAZ": multi_az,
            "KubernetesVersion": kubernetes_version,
            "Region": region,
        }
        return self._handle_request(api_request).result

    def upgrade_cluster_addons(self, cluster_id=None,):
        api_request = APIRequest(
            'UpgradeClusterAddons',
            'POST',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/clusters/[ClusterId]/components/upgrade'
        api_request._params = {"ClusterId": cluster_id, }
        return self._handle_request(api_request).result

    def describe_cluster_addons_version(self, cluster_id=None,):
        api_request = APIRequest(
            'DescribeClusterAddonsVersion',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/clusters/[ClusterId]/components/version'
        api_request._params = {"ClusterId": cluster_id, }
        return self._handle_request(api_request).result

    def describe_edge_cluster_attach_scripts(
            self, cluster_id=None, name_prefix=None,):
        api_request = APIRequest(
            'DescribeEdgeClusterAttachScripts',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/clusters/[ClusterId]/attachscript'
        api_request._params = {
            "ClusterId": cluster_id,
            "NamePrefix": name_prefix,
        }
        return self._handle_request(api_request).result

    def delete_cluster_nodes(self, cluster_id=None,):
        api_request = APIRequest(
            'DeleteClusterNodes',
            'POST|DELETE',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/clusters/[ClusterId]/nodes'
        api_request._params = {"ClusterId": cluster_id, }
        return self._handle_request(api_request).result

    def describe_cluster_user_kubeconfig(
            self, private_ip_address=None, cluster_id=None,):
        api_request = APIRequest(
            'DescribeClusterUserKubeconfig',
            'GET',
            'http',
            'ROA',
            'query')
        api_request.uri_pattern = '/k8s/[ClusterId]/user_config'
        api_request._params = {
            "PrivateIpAddress": private_ip_address,
            "ClusterId": cluster_id,
        }
        return self._handle_request(api_request).result

    def describe_cluster_endpoints(self, cluster_id=None,):
        api_request = APIRequest(
            'DescribeClusterEndpoints',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/clusters/[ClusterId]/endpoints'
        api_request._params = {"ClusterId": cluster_id, }
        return self._handle_request(api_request).result

    def upgrade_cluster_components(self, component_id=None, cluster_id=None,):
        api_request = APIRequest(
            'UpgradeClusterComponents',
            'POST',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/clusters/[ClusterId]/components/[ComponentId]/upgrade'
        api_request._params = {
            "ComponentId": component_id,
            "ClusterId": cluster_id,
        }
        return self._handle_request(api_request).result

    def describe_cluster_nodes(
        self,
        page_size=None,
        cluster_id=None,
        page_number=None,
    ):
        api_request = APIRequest(
            'DescribeClusterNodes',
            'GET',
            'http',
            'ROA',
            'query')
        api_request.uri_pattern = '/clusters/[ClusterId]/nodes'
        api_request._params = {
            "pageSize": page_size,
            "ClusterId": cluster_id,
            "pageNumber": page_number,
        }
        return self._handle_request(api_request).result

    def describe_cluster_logs(self, cluster_id=None,):
        api_request = APIRequest(
            'DescribeClusterLogs',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/clusters/[ClusterId]/logs'
        api_request._params = {"ClusterId": cluster_id, }
        return self._handle_request(api_request).result

    def check_aliyun_cs_service_role(self,):
        api_request = APIRequest(
            'CheckAliyunCSServiceRole', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/aliyuncsrole/status'

        return self._handle_request(api_request).result

    def reset_cluster_node(self, instance_id=None, cluster_id=None,):
        api_request = APIRequest(
            'ResetClusterNode', 'POST', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/clusters/[ClusterId]/instances/[InstanceId]/reset'
        api_request._params = {
            "InstanceId": instance_id,
            "ClusterId": cluster_id,
        }
        return self._handle_request(api_request).result

    def delete_cluster_node(
        self,
        release_instance=None,
        ip=None,
        force=None,
        cluster_id=None,
    ):
        api_request = APIRequest(
            'DeleteClusterNode',
            'DELETE',
            'http',
            'ROA',
            'query')
        api_request.uri_pattern = '/clusters/[ClusterId]/ip/[Ip]'
        api_request._params = {
            "releaseInstance": release_instance,
            "Ip": ip,
            "force": force,
            "ClusterId": cluster_id,
        }
        return self._handle_request(api_request).result

    def revoke_cluster_token(self, token=None,):
        api_request = APIRequest(
            'RevokeClusterToken',
            'DELETE',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/token/[Token]/revoke'
        api_request._params = {"Token": token, }
        return self._handle_request(api_request).result

    def download_cluster_node_certs(self, node_id=None, token=None,):
        api_request = APIRequest(
            'DownloadClusterNodeCerts',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/token/[Token]/nodes/[NodeId]/certs'
        api_request._params = {"NodeId": node_id, "Token": token, }
        return self._handle_request(api_request).result

    def attach_instances(self, cluster_id=None,):
        api_request = APIRequest(
            'AttachInstances', 'POST', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/clusters/[ClusterId]/attach'
        api_request._params = {"ClusterId": cluster_id, }
        return self._handle_request(api_request).result

    def create_cluster(self,):
        api_request = APIRequest('CreateCluster', 'POST', 'http', 'ROA', '')
        api_request.uri_pattern = '/clusters'

        return self._handle_request(api_request).result

    def scale_cluster(self, cluster_id=None,):
        api_request = APIRequest('ScaleCluster', 'PUT', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/clusters/[ClusterId]'
        api_request._params = {"ClusterId": cluster_id, }
        return self._handle_request(api_request).result

    def describe_clusters(self, cluster_type=None, name=None,):
        api_request = APIRequest(
            'DescribeClusters', 'GET', 'http', 'ROA', 'query')
        api_request.uri_pattern = '/clusters'
        api_request._params = {"clusterType": cluster_type, "Name": name, }
        return self._handle_request(api_request).result

    def describe_cluster_detail(self, cluster_id=None,):
        api_request = APIRequest(
            'DescribeClusterDetail',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/clusters/[ClusterId]'
        api_request._params = {"ClusterId": cluster_id, }
        return self._handle_request(api_request).result

    def describe_cluster_certs(self, cluster_id=None,):
        api_request = APIRequest(
            'DescribeClusterCerts',
            'GET',
            'http',
            'ROA',
            'path')
        api_request.uri_pattern = '/clusters/[ClusterId]/certs'
        api_request._params = {"ClusterId": cluster_id, }
        return self._handle_request(api_request).result

    def delete_cluster(self, cluster_id=None,):
        api_request = APIRequest(
            'DeleteCluster', 'DELETE', 'http', 'ROA', 'path')
        api_request.uri_pattern = '/clusters/[ClusterId]'
        api_request._params = {"ClusterId": cluster_id, }
        return self._handle_request(api_request).result

    def describe_api_version(self,):
        api_request = APIRequest(
            'DescribeApiVersion', 'GET', 'http', 'ROA', '')
        api_request.uri_pattern = '/version'

        return self._handle_request(api_request).result
