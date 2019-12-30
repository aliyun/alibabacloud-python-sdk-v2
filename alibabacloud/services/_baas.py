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

from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_special_resource_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _BAASResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'baas', _client=_client)
        self.consortiums = _create_special_resource_collection(
            _BAASConsortiumResource, _client, _client.describe_consortiums,
            'Result.Result', 'ConsortiumId',
        )
        self.organizations = _create_special_resource_collection(
            _BAASOrganizationResource, _client, _client.describe_organizations,
            'Result.Result', 'OrganizationId',
        )
        self.regions = _create_special_resource_collection(
            _BAASRegionResource, _client, _client.describe_regions,
            'Result.Result', 'RegionId',
        )
        self.tasks = _create_special_resource_collection(
            _BAASTaskResource, _client, _client.describe_tasks,
            'Result.Task', 'TaskId',
        )

    def create_ant_chain(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ant_chain(**_params)
        ant_chain_id = _new_get_key_in_response(response, 'AntChainId')
        return _BAASAntChainResource(ant_chain_id, _client=self._client)

    def create_ant_chain_contract_content(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ant_chain_contract_content(**_params)
        content_id = _new_get_key_in_response(response, 'ContentId')
        return _BAASAntChainContractContentResource(content_id, _client=self._client)

    def create_ant_chain_contract_project(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_ant_chain_contract_project(**_params)
        project_id = _new_get_key_in_response(response, 'ProjectId')
        return _BAASAntChainContractProjectResource(project_id, _client=self._client)

    def create_channel(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_channel(**_params)
        channel_id = _new_get_key_in_response(response, 'ChannelId')
        return _BAASChannelResource(channel_id, _client=self._client)

    def create_consortium(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_consortium(**_params)
        consortium_id = _new_get_key_in_response(response, 'ConsortiumId')
        return _BAASConsortiumResource(consortium_id, _client=self._client)

    def destroy_consortium(self, **params):
        _params = _transfer_params(params)
        response = self._client.destroy_consortium(**_params)
        consortium_id = _new_get_key_in_response(response, 'ConsortiumId')
        return _BAASConsortiumResource(consortium_id, _client=self._client)

    def create_organization(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_organization(**_params)
        organization_id = _new_get_key_in_response(response, 'OrganizationId')
        return _BAASOrganizationResource(organization_id, _client=self._client)

    def destroy_organization(self, **params):
        _params = _transfer_params(params)
        response = self._client.destroy_organization(**_params)
        organization_id = _new_get_key_in_response(response, 'OrganizationId')
        return _BAASOrganizationResource(organization_id, _client=self._client)

    def create_smart_contract_job(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_smart_contract_job(**_params)
        access_id = _new_get_key_in_response(response, 'AccessId')
        return _BAASSmartContractJobResource(access_id, _client=self._client)

    def invite_user(self, **params):
        _params = _transfer_params(params)
        response = self._client.invite_user(**_params)
        user_id = _new_get_key_in_response(response, 'UserId')
        return _BAASUserResource(user_id, _client=self._client)


class _BAASAntChainResource(ServiceResource):

    def __init__(self, ant_chain_id, _client=None):
        ServiceResource.__init__(self, "baas.ant_chain", _client=_client)
        self.ant_chain_id = ant_chain_id

    def apply_ant_chain_certificate(self, **params):
        _params = _transfer_params(params)
        return self._client.apply_ant_chain_certificate(ant_chain_id=self.ant_chain_id, **_params)

    def describe_ant_chain_accounts(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chain_accounts(ant_chain_id=self.ant_chain_id, **_params)

    def describe_ant_chain_block(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chain_block(ant_chain_id=self.ant_chain_id, **_params)

    def describe_ant_chain_certificate_applications(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chain_certificate_applications(
            ant_chain_id=self.ant_chain_id, **_params)

    def describe_ant_chain_download_paths(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chain_download_paths(ant_chain_id=self.ant_chain_id,
                                                              **_params)

    def describe_ant_chain_information(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chain_information(ant_chain_id=self.ant_chain_id,
                                                           **_params)

    def describe_ant_chain_latest_blocks(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chain_latest_blocks(ant_chain_id=self.ant_chain_id,
                                                             **_params)

    def describe_ant_chain_latest_transaction_digests(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chain_latest_transaction_digests(
            ant_chain_id=self.ant_chain_id, **_params)

    def describe_ant_chain_transaction(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chain_transaction(ant_chain_id=self.ant_chain_id,
                                                           **_params)

    def describe_ant_chain_transaction_statistics(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chain_transaction_statistics(
            ant_chain_id=self.ant_chain_id, **_params)

    def freeze_ant_chain_account(self, **params):
        _params = _transfer_params(params)
        return self._client.freeze_ant_chain_account(ant_chain_id=self.ant_chain_id, **_params)

    def process_cloud_ide_contract_transaction(self, **params):
        _params = _transfer_params(params)
        return self._client.process_cloud_ide_contract_transaction(ant_chain_id=self.ant_chain_id,
                                                                   **_params)

    def reset_ant_chain_certificate(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_ant_chain_certificate(ant_chain_id=self.ant_chain_id, **_params)

    def reset_ant_chain_user_certificate(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_ant_chain_user_certificate(ant_chain_id=self.ant_chain_id,
                                                             **_params)

    def unfreeze_ant_chain_account(self, **params):
        _params = _transfer_params(params)
        return self._client.unfreeze_ant_chain_account(ant_chain_id=self.ant_chain_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_ant_chain(ant_chain_id=self.ant_chain_id, **_params)

    def apply_ant_chain_certificate_with_key_auto_creation(self, **params):
        _params = _transfer_params(params)
        return self._client.apply_ant_chain_certificate_with_key_auto_creation(
            ant_chain_id=self.ant_chain_id, **_params)

    def apply_ant_chain_with_key_auto_creation(self, **params):
        _params = _transfer_params(params)
        return self._client.apply_ant_chain_with_key_auto_creation(ant_chain_id=self.ant_chain_id,
                                                                   **_params)


class _BAASAntChainContractContentResource(ServiceResource):

    def __init__(self, content_id, _client=None):
        ServiceResource.__init__(self, "baas.ant_chain_contract_content", _client=_client)
        self.content_id = content_id

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_ant_chain_contract_content(content_id=self.content_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_ant_chain_contract_content(content_id=self.content_id, **_params)


class _BAASAntChainContractProjectResource(ServiceResource):

    def __init__(self, project_id, _client=None):
        ServiceResource.__init__(self, "baas.ant_chain_contract_project", _client=_client)
        self.project_id = project_id

    def copy(self, **params):
        _params = _transfer_params(params)
        return self._client.copy_ant_chain_contract_project(project_id=self.project_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_ant_chain_contract_project(project_id=self.project_id, **_params)

    def describe_ant_chain_contract_project_content_tree(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chain_contract_project_content_tree(
            project_id=self.project_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_ant_chain_contract_project(project_id=self.project_id, **_params)


class _BAASChannelResource(ServiceResource):

    def __init__(self, channel_id, _client=None):
        ServiceResource.__init__(self, "baas.channel", _client=_client)
        self.channel_id = channel_id

    def create_channel_member(self, **params):
        _params = _transfer_params(params)
        return self._client.create_channel_member(channel_id=self.channel_id, **_params)

    def describe_channel_members(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_channel_members(channel_id=self.channel_id, **_params)

    def join(self, **params):
        _params = _transfer_params(params)
        return self._client.join_channel(channel_id=self.channel_id, **_params)

    def update_channel_config(self, **params):
        _params = _transfer_params(params)
        return self._client.update_channel_config(channel_id=self.channel_id, **_params)


class _BAASConsortiumResource(ServiceResource):

    def __init__(self, consortium_id, _client=None):
        ServiceResource.__init__(self, "baas.consortium", _client=_client)
        self.consortium_id = consortium_id

        self.ca_name = None
        self.ca_url = None
        self.channel_count = None
        self.channel_policy = None
        self.code_name = None
        self.create_time = None
        self.domain = None
        self.expired_time = None
        self.hybrid = None
        self.msp = None
        self.name = None
        self.orderer_count = None
        self.organization_count = None
        self.owner_bid = None
        self.owner_name = None
        self.owner_uid = None
        self.region_id = None
        self.request_id = None
        self.spec_name = None
        self.state = None
        self.support_channel_config = None

    def confirm_consortium_member(self, **params):
        _params = _transfer_params(params)
        return self._client.confirm_consortium_member(consortium_id=self.consortium_id, **_params)

    def create_consortium_member(self, **params):
        _params = _transfer_params(params)
        return self._client.create_consortium_member(consortium_id=self.consortium_id, **_params)

    def delete_ant_chain(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_ant_chain_consortium(consortium_id=self.consortium_id, **_params)

    def describe_ant_chain_contract_projects(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chain_contract_projects(consortium_id=self.consortium_id,
                                                                 **_params)

    def describe_ant_chain_members(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chain_members(consortium_id=self.consortium_id, **_params)

    def describe_ant_chains(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_ant_chains(consortium_id=self.consortium_id, **_params)

    def describe_consortium_chaincodes(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_consortium_chaincodes(consortium_id=self.consortium_id,
                                                           **_params)

    def describe_consortium_channels(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_consortium_channels(consortium_id=self.consortium_id,
                                                         **_params)

    def describe_consortium_deletable(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_consortium_deletable(consortium_id=self.consortium_id,
                                                          **_params)

    def describe_consortium_member_approval(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_consortium_member_approval(consortium_id=self.consortium_id,
                                                                **_params)

    def describe_consortium_members(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_consortium_members(consortium_id=self.consortium_id, **_params)

    def describe_consortium_orderers(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_consortium_orderers(consortium_id=self.consortium_id,
                                                         **_params)

    def describe_invitation_code(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_invitation_code(consortium_id=self.consortium_id, **_params)

    def describe_invitation_list(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_invitation_list(consortium_id=self.consortium_id, **_params)

    def describe_orderer_logs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_orderer_logs(consortium_id=self.consortium_id, **_params)

    def query_consortium_deletable(self, **params):
        _params = _transfer_params(params)
        return self._client.query_consortium_deletable(consortium_id=self.consortium_id, **_params)

    def update_ant_chain(self, **params):
        _params = _transfer_params(params)
        return self._client.update_ant_chain_consortium(consortium_id=self.consortium_id, **_params)

    def update_ant_chain_member(self, **params):
        _params = _transfer_params(params)
        return self._client.update_ant_chain_member(consortium_id=self.consortium_id, **_params)


class _BAASOrganizationResource(ServiceResource):

    def __init__(self, organization_id, _client=None):
        ServiceResource.__init__(self, "baas.organization", _client=_client)
        self.organization_id = organization_id

        self.code_name = None
        self.consortium_count = None
        self.create_time = None
        self.description = None
        self.domain = None
        self.expired_time = None
        self.hybrid = None
        self.name = None
        self.owner_bid = None
        self.owner_name = None
        self.owner_uid = None
        self.peer_count = None
        self.region_id = None
        self.request_id = None
        self.spec_name = None
        self.state = None
        self.user_count = None
        self.zone_id = None

    def create_organization_user(self, **params):
        _params = _transfer_params(params)
        return self._client.create_organization_user(organization_id=self.organization_id,
                                                     **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_organization(organization_id=self.organization_id, **_params)

    def describe_chaincode_upload_policy(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_chaincode_upload_policy(organization_id=self.organization_id,
                                                             **_params)

    def describe_explorer(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_explorer(organization_id=self.organization_id, **_params)

    def describe_organization_chaincodes(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_organization_chaincodes(organization_id=self.organization_id,
                                                             **_params)

    def describe_organization_channels(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_organization_channels(organization_id=self.organization_id,
                                                           **_params)

    def describe_organization_deletable(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_organization_deletable(organization_id=self.organization_id,
                                                            **_params)

    def describe_organization_members(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_organization_members(organization_id=self.organization_id,
                                                          **_params)

    def describe_organization_peers(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_organization_peers(organization_id=self.organization_id,
                                                        **_params)

    def describe_organization_user_certs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_organization_user_certs(organization_id=self.organization_id,
                                                             **_params)

    def describe_organization_users(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_organization_users(organization_id=self.organization_id,
                                                        **_params)

    def describe_orgnaization_chaincodes(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_orgnaization_chaincodes(organization_id=self.organization_id,
                                                             **_params)

    def describe_peer_logs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_peer_logs(organization_id=self.organization_id, **_params)

    def download_organization_sdk(self, **params):
        _params = _transfer_params(params)
        return self._client.download_organization_sdk(organization_id=self.organization_id,
                                                      **_params)

    def query_organization_deletable(self, **params):
        _params = _transfer_params(params)
        return self._client.query_organization_deletable(organization_id=self.organization_id,
                                                         **_params)

    def reset_organization_user_password(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_organization_user_password(organization_id=self.organization_id,
                                                             **_params)

    def create_chaincode(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_chaincode(organization_id=self.organization_id, **_params)
        chaincode_id = _new_get_key_in_response(response, 'ChaincodeId')
        return _BAASChaincodeResource(chaincode_id, self.organization_id, _client=self._client)


class _BAASChaincodeResource(ServiceResource):

    def __init__(self, chaincode_id, organization_id, _client=None):
        ServiceResource.__init__(self, "baas.chaincode", _client=_client)
        self.chaincode_id = chaincode_id
        self.organization_id = organization_id

    def describe_chaincode_collection_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_chaincode_collection_config(chaincode_id=self.chaincode_id,
                                                                 organization_id=self.organization_id,
                                                                 **_params)

    def install(self, **params):
        _params = _transfer_params(params)
        return self._client.install_chaincode(chaincode_id=self.chaincode_id,
                                              organization_id=self.organization_id, **_params)

    def instantiate(self, **params):
        _params = _transfer_params(params)
        return self._client.instantiate_chaincode(chaincode_id=self.chaincode_id,
                                                  organization_id=self.organization_id, **_params)

    def synchronize(self, **params):
        _params = _transfer_params(params)
        return self._client.synchronize_chaincode(chaincode_id=self.chaincode_id,
                                                  organization_id=self.organization_id, **_params)

    def upgrade(self, **params):
        _params = _transfer_params(params)
        return self._client.upgrade_chaincode(chaincode_id=self.chaincode_id,
                                              organization_id=self.organization_id, **_params)


class _BAASRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "baas.region", _client=_client)
        self.region_id = region_id

        self.id_ = None
        self.online = None
        self.title = None


class _BAASSmartContractJobResource(ServiceResource):

    def __init__(self, access_id, _client=None):
        ServiceResource.__init__(self, "baas.smart_contract_job", _client=_client)
        self.access_id = access_id


class _BAASTaskResource(ServiceResource):

    def __init__(self, task_id, _client=None):
        ServiceResource.__init__(self, "baas.task", _client=_client)
        self.task_id = task_id

        self.action = None
        self.handled = None
        self.operation_type = None
        self.request_time = None
        self.response_time = None
        self.result = None
        self.sender = None
        self.target = None


class _BAASUserResource(ServiceResource):

    def __init__(self, user_id, _client=None):
        ServiceResource.__init__(self, "baas.user", _client=_client)
        self.user_id = user_id
