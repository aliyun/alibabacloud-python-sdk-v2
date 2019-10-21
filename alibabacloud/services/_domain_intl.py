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


class _DOMAIN_INTLResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'domain-intl', _client=_client)
        self.registrant_profiles = _create_special_resource_collection(
            _DOMAIN_INTLRegistrantProfileResource, _client, _client.query_registrant_profiles,
            'RegistrantProfiles.RegistrantProfile', 'RegistrantProfileId', 
        )
    def check_domain(self, **params):
        _params = _transfer_params(params)
        response = self._client.check_domain(**_params)
        domain_name = _new_get_key_in_response(response, 'DomainName')
        return _DOMAIN_INTLDomainResource(domain_name, _client=self._client)

    def save_registrant_profile(self, **params):
        _params = _transfer_params(params)
        response = self._client.save_registrant_profile(**_params)
        registrant_profile_id = _new_get_key_in_response(response, 'RegistrantProfileId')
        return _DOMAIN_INTLRegistrantProfileResource(registrant_profile_id, _client=self._client)

class _DOMAIN_INTLDomainResource(ServiceResource):

    def __init__(self, domain_name, _client=None):
        ServiceResource.__init__(self, "domain-intl.domain", _client=_client)
        self.domain_name = domain_name
        

    def confirm_transfer_in_email(self, **params):
        _params = _transfer_params(params)
        return self._client.confirm_transfer_in_email(domain_name=self.domain_name, **_params)

    def save_batch_task_for_domain_name_proxy_service(self, **params):
        _params = _transfer_params(params)
        return self._client.save_batch_task_for_domain_name_proxy_service(domain_name=self.domain_name, **_params)

    def save_batch_task_for_modifying_domain_dns(self, **params):
        _params = _transfer_params(params)
        return self._client.save_batch_task_for_modifying_domain_dns(domain_name=self.domain_name, **_params)

    def save_batch_task_for_transfer_prohibition_lock(self, **params):
        _params = _transfer_params(params)
        return self._client.save_batch_task_for_transfer_prohibition_lock(domain_name=self.domain_name, **_params)

    def save_batch_task_for_update_prohibition_lock(self, **params):
        _params = _transfer_params(params)
        return self._client.save_batch_task_for_update_prohibition_lock(domain_name=self.domain_name, **_params)

    def save_batch_task_for_updating_contact_info_by_new_contact(self, **params):
        _params = _transfer_params(params)
        return self._client.save_batch_task_for_updating_contact_info_by_new_contact(domain_name=self.domain_name, **_params)

    def save_task_for_submitting_domain_real_name_verification_by_identity_credential(self, **params):
        _params = _transfer_params(params)
        return self._client.save_task_for_submitting_domain_real_name_verification_by_identity_credential(domain_name=self.domain_name, **_params)

    def save_task_for_updating_registrant_info_by_identity_credential(self, **params):
        _params = _transfer_params(params)
        return self._client.save_task_for_updating_registrant_info_by_identity_credential(domain_name=self.domain_name, **_params)

    def check_domain_sunrise_claim(self, **params):
        _params = _transfer_params(params)
        return self._client.check_domain_sunrise_claim(domain_name=self.domain_name, **_params)

    def check_transfer_in_feasibility(self, **params):
        _params = _transfer_params(params)
        return self._client.check_transfer_in_feasibility(domain_name=self.domain_name, **_params)

    def query_art_extension(self, **params):
        _params = _transfer_params(params)
        return self._client.query_art_extension(domain_name=self.domain_name, **_params)

    def query_contact_info(self, **params):
        _params = _transfer_params(params)
        return self._client.query_contact_info(domain_name=self.domain_name, **_params)

    def query_ds_record(self, **params):
        _params = _transfer_params(params)
        return self._client.query_ds_record(domain_name=self.domain_name, **_params)

    def query_domain_by_domain_name(self, **params):
        _params = _transfer_params(params)
        return self._client.query_domain_by_domain_name(domain_name=self.domain_name, **_params)

    def query_domain_real_name_verification_info(self, **params):
        _params = _transfer_params(params)
        return self._client.query_domain_real_name_verification_info(domain_name=self.domain_name, **_params)

    def query_ens_association(self, **params):
        _params = _transfer_params(params)
        return self._client.query_ens_association(domain_name=self.domain_name, **_params)

    def query_fail_reason_for_domain_real_name_verification(self, **params):
        _params = _transfer_params(params)
        return self._client.query_fail_reason_for_domain_real_name_verification(domain_name=self.domain_name, **_params)

    def query_local_ens_association(self, **params):
        _params = _transfer_params(params)
        return self._client.query_local_ens_association(domain_name=self.domain_name, **_params)

    def query_transfer_out_info(self, **params):
        _params = _transfer_params(params)
        return self._client.query_transfer_out_info(domain_name=self.domain_name, **_params)

    def save_single_task_for_adding_ds_record(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_adding_ds_record(domain_name=self.domain_name, **_params)

    def save_single_task_for_approving_transfer_out(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_approving_transfer_out(domain_name=self.domain_name, **_params)

    def save_single_task_for_associating_ens(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_associating_ens(domain_name=self.domain_name, **_params)

    def save_single_task_for_canceling_transfer_in(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_canceling_transfer_in(domain_name=self.domain_name, **_params)

    def save_single_task_for_canceling_transfer_out(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_canceling_transfer_out(domain_name=self.domain_name, **_params)

    def save_single_task_for_creating_order_activate(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_creating_order_activate(domain_name=self.domain_name, **_params)

    def save_single_task_for_creating_order_redeem(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_creating_order_redeem(domain_name=self.domain_name, **_params)

    def save_single_task_for_creating_order_renew(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_creating_order_renew(domain_name=self.domain_name, **_params)

    def save_single_task_for_creating_order_transfer(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_creating_order_transfer(domain_name=self.domain_name, **_params)

    def save_single_task_for_deleting_ds_record(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_deleting_ds_record(domain_name=self.domain_name, **_params)

    def save_single_task_for_disassociating_ens(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_disassociating_ens(domain_name=self.domain_name, **_params)

    def save_single_task_for_domain_name_proxy_service(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_domain_name_proxy_service(domain_name=self.domain_name, **_params)

    def save_single_task_for_modifying_ds_record(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_modifying_ds_record(domain_name=self.domain_name, **_params)

    def save_single_task_for_querying_transfer_authorization_code(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_querying_transfer_authorization_code(domain_name=self.domain_name, **_params)

    def save_single_task_for_save_art_extension(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_save_art_extension(domain_name=self.domain_name, **_params)

    def save_single_task_for_synchronizing_ds_record(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_synchronizing_ds_record(domain_name=self.domain_name, **_params)

    def save_single_task_for_transfer_prohibition_lock(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_transfer_prohibition_lock(domain_name=self.domain_name, **_params)

    def save_single_task_for_update_prohibition_lock(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_update_prohibition_lock(domain_name=self.domain_name, **_params)

    def save_single_task_for_updating_contact_info(self, **params):
        _params = _transfer_params(params)
        return self._client.save_single_task_for_updating_contact_info(domain_name=self.domain_name, **_params)

    def save_task_for_submitting_domain_real_name_verification_by_registrant_profile_id(self, **params):
        _params = _transfer_params(params)
        return self._client.save_task_for_submitting_domain_real_name_verification_by_registrant_profile_id(domain_name=self.domain_name, **_params)

    def transfer_in_reenter_transfer_authorization_code(self, **params):
        _params = _transfer_params(params)
        return self._client.transfer_in_reenter_transfer_authorization_code(domain_name=self.domain_name, **_params)

    def transfer_in_refetch_whois_email(self, **params):
        _params = _transfer_params(params)
        return self._client.transfer_in_refetch_whois_email(domain_name=self.domain_name, **_params)

    def transfer_in_resend_mail_token(self, **params):
        _params = _transfer_params(params)
        return self._client.transfer_in_resend_mail_token(domain_name=self.domain_name, **_params)

class _DOMAIN_INTLRegistrantProfileResource(ServiceResource):

    def __init__(self, registrant_profile_id, _client=None):
        ServiceResource.__init__(self, "domain-intl.registrant_profile", _client=_client)
        self.registrant_profile_id = registrant_profile_id
        
        self.address = None
        self.city = None
        self.country = None
        self.create_time = None
        self.default_registrant_profile = None
        self.email = None
        self.email_verification_status = None
        self.postal_code = None
        self.province = None
        self.real_name_status = None
        self.registrant_name = None
        self.registrant_organization = None
        self.registrant_profile_type = None
        self.registrant_type = None
        self.tel_area = None
        self.tel_ext = None
        self.telephone = None
        self.update_time = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_registrant_profile(registrant_profile_id=self.registrant_profile_id, **_params)

    def query_registrant_profile_real_name_verification_info(self, **params):
        _params = _transfer_params(params)
        return self._client.query_registrant_profile_real_name_verification_info(registrant_profile_id=self.registrant_profile_id, **_params)

    def save_batch_task_for_updating_contact_info(self, **params):
        _params = _transfer_params(params)
        return self._client.save_batch_task_for_updating_contact_info(registrant_profile_id=self.registrant_profile_id, **_params)

    def save_task_for_updating_registrant_info_by_registrant_profile_id(self, **params):
        _params = _transfer_params(params)
        return self._client.save_task_for_updating_registrant_info_by_registrant_profile_id(registrant_profile_id=self.registrant_profile_id, **_params)
