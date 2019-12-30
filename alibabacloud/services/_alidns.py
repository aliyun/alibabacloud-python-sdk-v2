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
from alibabacloud.resources.collection import _create_resource_collection, \
    _create_special_resource_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _ALIDNSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'alidns', _client=_client)
        self.domains = _create_resource_collection(
            _ALIDNSDomainResource, _client, _client.describe_domains,
            'Domains.Domain', 'DomainName',
        )
        self.domain_groups = _create_resource_collection(
            _ALIDNSDomainGroupResource, _client, _client.describe_domain_groups,
            'DomainGroups.DomainGroup', 'GroupId',
        )
        self.domain_records = _create_resource_collection(
            _ALIDNSDomainRecordResource, _client, _client.describe_domain_records,
            'DomainRecords.Record', 'RecordId',
        )
        self.gtm_access_strategies = _create_special_resource_collection(
            _ALIDNSGtmAccessStrategyResource, _client, _client.describe_gtm_access_strategies,
            'Strategies.Strategy', 'StrategyId',
        )
        self.gtm_recovery_plans = _create_special_resource_collection(
            _ALIDNSGtmRecoveryPlanResource, _client, _client.describe_gtm_recovery_plans,
            'RecoveryPlans.RecoveryPlan', 'RecoveryPlanId',
        )

    def add_domain(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_domain(**_params)
        domain_name = _new_get_key_in_response(response, 'DomainName')
        return _ALIDNSDomainResource(domain_name, _client=self._client)

    def delete_domain(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_domain(**_params)
        domain_name = _new_get_key_in_response(response, 'DomainName')
        return _ALIDNSDomainResource(domain_name, _client=self._client)

    def add_domain_group(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_domain_group(**_params)
        group_id = _new_get_key_in_response(response, 'GroupId')
        return _ALIDNSDomainGroupResource(group_id, _client=self._client)

    def add_domain_record(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_domain_record(**_params)
        record_id = _new_get_key_in_response(response, 'RecordId')
        return _ALIDNSDomainRecordResource(record_id, _client=self._client)

    def delete_domain_record(self, **params):
        _params = _transfer_params(params)
        response = self._client.delete_domain_record(**_params)
        record_id = _new_get_key_in_response(response, 'RecordId')
        return _ALIDNSDomainRecordResource(record_id, _client=self._client)

    def update_domain_record(self, **params):
        _params = _transfer_params(params)
        response = self._client.update_domain_record(**_params)
        record_id = _new_get_key_in_response(response, 'RecordId')
        return _ALIDNSDomainRecordResource(record_id, _client=self._client)

    def add_gtm_access_strategy(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_gtm_access_strategy(**_params)
        strategy_id = _new_get_key_in_response(response, 'StrategyId')
        return _ALIDNSGtmAccessStrategyResource(strategy_id, _client=self._client)

    def add_gtm_address_pool(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_gtm_address_pool(**_params)
        addr_pool_id = _new_get_key_in_response(response, 'AddrPoolId')
        return _ALIDNSGtmAddressPoolResource(addr_pool_id, _client=self._client)

    def add_gtm_monitor(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_gtm_monitor(**_params)
        monitor_config_id = _new_get_key_in_response(response, 'MonitorConfigId')
        return _ALIDNSGtmMonitorResource(monitor_config_id, _client=self._client)

    def add_gtm_recovery_plan(self, **params):
        _params = _transfer_params(params)
        response = self._client.add_gtm_recovery_plan(**_params)
        recovery_plan_id = _new_get_key_in_response(response, 'RecoveryPlanId')
        return _ALIDNSGtmRecoveryPlanResource(recovery_plan_id, _client=self._client)

    def create_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_instance(**_params)
        instance_id = _new_get_key_in_response(response, 'InstanceId')
        return _ALIDNSInstanceResource(instance_id, _client=self._client)


class _ALIDNSDomainResource(ServiceResource):

    def __init__(self, domain_name, _client=None):
        ServiceResource.__init__(self, "alidns.domain", _client=_client)
        self.domain_name = domain_name

        self.ali_domain = None
        self.dns_servers = None
        self.domain_id = None
        self.group_id = None
        self.group_name = None
        self.instance_end_time = None
        self.instance_expired = None
        self.instance_id = None
        self.puny_code = None
        self.record_count = None
        self.registrant_email = None
        self.remark = None
        self.version_code = None
        self.version_name = None

    def change_domain_group(self, **params):
        _params = _transfer_params(params)
        return self._client.change_domain_group(domain_name=self.domain_name, **_params)

    def check_domain_record(self, **params):
        _params = _transfer_params(params)
        return self._client.check_domain_record(domain_name=self.domain_name, **_params)

    def delete_sub_domain_records(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_sub_domain_records(domain_name=self.domain_name, **_params)

    def describe_dnsslb_sub(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dnsslb_sub_domains(domain_name=self.domain_name, **_params)

    def describe_domain_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_domain_info(domain_name=self.domain_name, **_params)

    def describe_domain_ns(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_domain_ns(domain_name=self.domain_name, **_params)

    def describe_domain_statistics(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_domain_statistics(domain_name=self.domain_name, **_params)

    def describe_record_logs(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_record_logs(domain_name=self.domain_name, **_params)

    def describe_record_statistics(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_record_statistics(domain_name=self.domain_name, **_params)

    def describe_record_statistics_summary(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_record_statistics_summary(domain_name=self.domain_name,
                                                               **_params)

    def modify_hichina_domain_dns(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_hichina_domain_dns(domain_name=self.domain_name, **_params)


class _ALIDNSDomainGroupResource(ServiceResource):

    def __init__(self, group_id, _client=None):
        ServiceResource.__init__(self, "alidns.domain_group", _client=_client)
        self.group_id = group_id

        self.domain_count = None
        self.group_name = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_domain_group(group_id=self.group_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_domain_group(group_id=self.group_id, **_params)


class _ALIDNSDomainRecordResource(ServiceResource):

    def __init__(self, record_id, _client=None):
        ServiceResource.__init__(self, "alidns.domain_record", _client=_client)
        self.record_id = record_id

        self.domain_name = None
        self.line = None
        self.locked = None
        self.priority = None
        self.rr = None
        self.remark = None
        self.status = None
        self.ttl = None
        self.type_ = None
        self.value = None
        self.weight = None

    def describe_domain_record_info(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_domain_record_info(record_id=self.record_id, **_params)

    def set_domain_record_status(self, **params):
        _params = _transfer_params(params)
        return self._client.set_domain_record_status(record_id=self.record_id, **_params)

    def update_dnsslb_weight(self, **params):
        _params = _transfer_params(params)
        return self._client.update_dnsslb_weight(record_id=self.record_id, **_params)


class _ALIDNSGtmAccessStrategyResource(ServiceResource):

    def __init__(self, strategy_id, _client=None):
        ServiceResource.__init__(self, "alidns.gtm_access_strategy", _client=_client)
        self.strategy_id = strategy_id

        self.access_mode = None
        self.access_status = None
        self.create_time = None
        self.create_timestamp = None
        self.default_addr_pool_id = None
        self.default_addr_pool_monitor_status = None
        self.default_addr_pool_name = None
        self.default_addr_pool_status = None
        self.failover_addr_pool_id = None
        self.failover_addr_pool_monitor_status = None
        self.failover_addr_pool_name = None
        self.failover_addr_pool_status = None
        self.instance_id = None
        self.lines = None
        self.strategy_mode = None
        self.strategy_name = None

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_gtm_access_strategy(strategy_id=self.strategy_id, **_params)

    def set_gtm_access_mode(self, **params):
        _params = _transfer_params(params)
        return self._client.set_gtm_access_mode(strategy_id=self.strategy_id, **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_gtm_access_strategy(strategy_id=self.strategy_id, **_params)


class _ALIDNSGtmAddressPoolResource(ServiceResource):

    def __init__(self, addr_pool_id, _client=None):
        ServiceResource.__init__(self, "alidns.gtm_address_pool", _client=_client)
        self.addr_pool_id = addr_pool_id

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_gtm_address_pool(addr_pool_id=self.addr_pool_id, **_params)

    def describe_gtm_instance_address_pool(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_gtm_instance_address_pool(addr_pool_id=self.addr_pool_id,
                                                               **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_gtm_address_pool(addr_pool_id=self.addr_pool_id, **_params)


class _ALIDNSGtmMonitorResource(ServiceResource):

    def __init__(self, monitor_config_id, _client=None):
        ServiceResource.__init__(self, "alidns.gtm_monitor", _client=_client)
        self.monitor_config_id = monitor_config_id

    def describe_gtm_monitor_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_gtm_monitor_config(monitor_config_id=self.monitor_config_id,
                                                        **_params)

    def set_gtm_monitor_status(self, **params):
        _params = _transfer_params(params)
        return self._client.set_gtm_monitor_status(monitor_config_id=self.monitor_config_id,
                                                   **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_gtm_monitor(monitor_config_id=self.monitor_config_id, **_params)


class _ALIDNSGtmRecoveryPlanResource(ServiceResource):

    def __init__(self, recovery_plan_id, _client=None):
        ServiceResource.__init__(self, "alidns.gtm_recovery_plan", _client=_client)
        self.recovery_plan_id = recovery_plan_id

        self.create_time = None
        self.create_timestamp = None
        self.fault_addr_pool_num = None
        self.last_execute_time = None
        self.last_execute_timestamp = None
        self.last_rollback_time = None
        self.last_rollback_timestamp = None
        self.name = None
        self.remark = None
        self.status = None
        self.update_time = None
        self.update_timestamp = None

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_gtm_recovery_plan(recovery_plan_id=self.recovery_plan_id,
                                                     **_params)

    def describe(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_gtm_recovery_plan(recovery_plan_id=self.recovery_plan_id,
                                                       **_params)

    def execute(self, **params):
        _params = _transfer_params(params)
        return self._client.execute_gtm_recovery_plan(recovery_plan_id=self.recovery_plan_id,
                                                      **_params)

    def preview(self, **params):
        _params = _transfer_params(params)
        return self._client.preview_gtm_recovery_plan(recovery_plan_id=self.recovery_plan_id,
                                                      **_params)

    def rollback(self, **params):
        _params = _transfer_params(params)
        return self._client.rollback_gtm_recovery_plan(recovery_plan_id=self.recovery_plan_id,
                                                       **_params)

    def update(self, **params):
        _params = _transfer_params(params)
        return self._client.update_gtm_recovery_plan(recovery_plan_id=self.recovery_plan_id,
                                                     **_params)


class _ALIDNSInstanceResource(ServiceResource):

    def __init__(self, instance_id, _client=None):
        ServiceResource.__init__(self, "alidns.instance", _client=_client)
        self.instance_id = instance_id

    def change_domain_of_dns_product(self, **params):
        _params = _transfer_params(params)
        return self._client.change_domain_of_dns_product(instance_id=self.instance_id, **_params)

    def describe_dns_product(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_dns_product_instance(instance_id=self.instance_id, **_params)

    def describe_gtm(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_gtm_instance(instance_id=self.instance_id, **_params)

    def describe_gtm_access_strategy_available_config(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_gtm_access_strategy_available_config(
            instance_id=self.instance_id, **_params)

    def describe_gtm_instance_address_pools(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_gtm_instance_address_pools(instance_id=self.instance_id,
                                                                **_params)

    def describe_gtm_instance_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_gtm_instance_status(instance_id=self.instance_id, **_params)

    def describe_gtm_instance_system_cname(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_gtm_instance_system_cname(instance_id=self.instance_id,
                                                               **_params)

    def update_gtm_instance_global_config(self, **params):
        _params = _transfer_params(params)
        return self._client.update_gtm_instance_global_config(instance_id=self.instance_id,
                                                              **_params)
