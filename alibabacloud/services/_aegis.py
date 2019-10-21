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


class _AEGISResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'aegis', _client=_client)
        self.check_warnings = _create_special_resource_collection(
            _AEGISCheckWarningResource, _client, _client.describe_check_warnings,
            'CheckWarnings.CheckWarning', 'CheckWarningId', 
        )
        self.data_sources = _create_special_resource_collection(
            _AEGISDataSourceResource, _client, _client.describe_data_source,
            'MetaDatas.Data', 'DataSourceId', 
        )
        self.risks = _create_special_resource_collection(
            _AEGISRiskResource, _client, _client.describe_risks,
            'Risks.Risk', 'RiskId', 
        )
    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _AEGISInstanceResource(instance_id, _client=self._client)

    def create_suspicious_export(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_suspicious_export(**_params)
        file_name = _new_get_key_in_response(response, 'FileName')
        return _AEGISSuspiciousExportResource(file_name, _client=self._client)

class _AEGISCheckWarningResource(ServiceResource):

    def __init__(self, check_warning_id, _client=None):
        ServiceResource.__init__(self, "aegis.check_warning", _client=_client)
        self.check_warning_id = check_warning_id
        
        self.check_id = None
        self.item = None
        self.level = None
        self.reason = None
        self.status = None
        self.type_ = None
        self.uuid = None

    def describe_check_warning_detail(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_check_warning_detail(check_warning_id=self.check_warning_id, **_params)

class _AEGISDataSourceResource(ServiceResource):

    def __init__(self, data_source_id, _client=None):
        ServiceResource.__init__(self, "aegis.data_source", _client=_client)
        self.data_source_id = data_source_id
        
        self.data_source_name = None
        self.date_source_name = None
        self.description = None
        self.meta_data_fields = None

class _AEGISInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "aegis.instance", _client=_client)
        self.instance_id = instance_id
        

    def release(self, **params):
        _params = _transfer_params(params)
        return self._client.release_instance(instance_id=self.instance_id, **_params)

    def renew(self, **params):
        _params = _transfer_params(params)
        return self._client.renew_instance(instance_id=self.instance_id, **_params)

    def upgrade(self, **params):
        _params = _transfer_params(params)
        return self._client.upgrade_instance(instance_id=self.instance_id, **_params)

class _AEGISRiskResource(ServiceResource):

    def __init__(self, risk_id, _client=None):
        ServiceResource.__init__(self, "aegis.risk", _client=_client)
        self.risk_id = risk_id
        
        self.risk_detail = None
        self.risk_name = None
        self.risk_type = None
        self.sub_risk_type = None
        self.sub_type_alias = None
        self.type_alias = None

    def validate_hc_warnings(self, **params):
        _params = _transfer_params(params)
        return self._client.validate_hc_warnings(risk_id=self.risk_id, **_params)

    def describe_warning_machines(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_warning_machines(risk_id=self.risk_id, **_params)

    def ignore_hc_check_warnings(self, **params):
        _params = _transfer_params(params)
        return self._client.ignore_hc_check_warnings(risk_id=self.risk_id, **_params)

class _AEGISSuspiciousExportResource(ServiceResource):

    def __init__(self, file_name, _client=None):
        ServiceResource.__init__(self, "aegis.suspicious_export", _client=_client)
        self.file_name = file_name
        
