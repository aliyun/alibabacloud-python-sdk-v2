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


class _CASResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'cas', _client=_client)
    def create_order_audit(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_order_audit(**_params)
        check_name = _new_get_key_in_response(response, 'CheckName')
        return _CASOrderAuditResource(check_name, _client=self._client)

    def create_signature(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_signature(**_params)
        transaction_id = _new_get_key_in_response(response, 'TransactionId')
        return _CASSignatureResource(transaction_id, _client=self._client)

    def create_signature_document(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_signature_document(**_params)
        doc_id = _new_get_key_in_response(response, 'DocId')
        return _CASSignatureDocumentResource(doc_id, _client=self._client)

    def create_signature_people_certificate(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_signature_people_certificate(**_params)
        people_id = _new_get_key_in_response(response, 'PeopleId')
        return _CASSignaturePeopleCertificateResource(people_id, _client=self._client)

class _CASOrderAuditResource(ServiceResource):

    def __init__(self, check_name, _client=None):
        ServiceResource.__init__(self, "cas.order_audit", _client=_client)
        self.check_name = check_name
        

class _CASSignatureResource(ServiceResource):

    def __init__(self, transaction_id, _client=None):
        ServiceResource.__init__(self, "cas.signature", _client=_client)
        self.transaction_id = transaction_id
        

    def describe_signature_trade_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_signature_trade_detail(transaction_id=self.transaction_id, **_params)

class _CASSignatureDocumentResource(ServiceResource):

    def __init__(self, doc_id, _client=None):
        ServiceResource.__init__(self, "cas.signature_document", _client=_client)
        self.doc_id = doc_id
        

    def create_filing(self, **params):
        _params = _transfer_params(params)
        return self._client.create_filing_signature_document(doc_id=self.doc_id, **_params)

    def create_web_signature(self, **params):
        _params = _transfer_params(params)
        return self._client.create_web_signature(doc_id=self.doc_id, **_params)

class _CASSignaturePeopleCertificateResource(ServiceResource):

    def __init__(self, people_id, _client=None):
        ServiceResource.__init__(self, "cas.signature_people_certificate", _client=_client)
        self.people_id = people_id
        
