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


class _DTSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'dts', _client=_client)
        self.consumer_groups = _create_special_resource_collection(
            _DTSConsumerGroupResource, _client, _client.describe_consumer_group,
            'ConsumerChannels.DescribeConsumerChannel', 'ConsumerGroupName', 
        )
        self.synchronization_jobs = _create_special_resource_collection(
            _DTSSynchronizationJobResource, _client, _client.describe_synchronization_jobs,
            'SynchronizationInstances.SynchronizationInstance', 'SynchronizationJobId', 
        )
    def create_consumer_group(self, **params):
        _params = _transfer_params(params)
        self._client.create_consumer_group(**_params)
        consumer_group_name = _params.get("consumer_group_name")
        return _DTSConsumerGroupResource(consumer_group_name, _client=self._client)

    def create_subscription_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_subscription_instance(**_params)
        subscription_instance_id = _new_get_key_in_response(response, 'SubscriptionInstanceId')
        return _DTSSubscriptionInstanceResource(subscription_instance_id, _client=self._client)

    def create_synchronization_job(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_synchronization_job(**_params)
        synchronization_job_id = _new_get_key_in_response(response, 'SynchronizationJobId')
        return _DTSSynchronizationJobResource(synchronization_job_id, _client=self._client)

class _DTSConsumerGroupResource(ServiceResource):

    def __init__(self, consumer_group_name, _client=None):
        ServiceResource.__init__(self, "dts.consumer_group", _client=_client)
        self.consumer_group_name = consumer_group_name
        
        self.consumer_group_id = None
        self.consumer_group_user_name = None
        self.consumption_checkpoint = None
        self.message_delay = None
        self.unconsumed_data = None

class _DTSSubscriptionInstanceResource(ServiceResource):

    def __init__(self, subscription_instance_id, _client=None):
        ServiceResource.__init__(self, "dts.subscription_instance", _client=_client)
        self.subscription_instance_id = subscription_instance_id
        

    def configure(self, **params):
        _params = _transfer_params(params)
        return self._client.configure_subscription_instance(subscription_instance_id=self.subscription_instance_id, **_params)

    def configure_subscription_instance_alert(self, **params):
        _params = _transfer_params(params)
        return self._client.configure_subscription_instance_alert(subscription_instance_id=self.subscription_instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_subscription_instance(subscription_instance_id=self.subscription_instance_id, **_params)

    def delete_consumer_group(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_consumer_group(subscription_instance_id=self.subscription_instance_id, **_params)

    def describe_subscription_instance_alert(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_subscription_instance_alert(subscription_instance_id=self.subscription_instance_id, **_params)

    def describe_subscription_instance_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_subscription_instance_status(subscription_instance_id=self.subscription_instance_id, **_params)

    def describe_subscription_object_modify_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_subscription_object_modify_status(subscription_instance_id=self.subscription_instance_id, **_params)

    def modify_consumer_group_password(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_consumer_group_password(subscription_instance_id=self.subscription_instance_id, **_params)

    def modify_consumption_timestamp(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_consumption_timestamp(subscription_instance_id=self.subscription_instance_id, **_params)

    def modify_subscription_object(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_subscription_object(subscription_instance_id=self.subscription_instance_id, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        return self._client.start_subscription_instance(subscription_instance_id=self.subscription_instance_id, **_params)

class _DTSSynchronizationJobResource(ServiceResource):

    def __init__(self, synchronization_job_id, _client=None):
        ServiceResource.__init__(self, "dts.synchronization_job", _client=_client)
        self.synchronization_job_id = synchronization_job_id
        
        self.data_initialization = None
        self.data_initialization_status = None
        self.data_synchronization_status = None
        self.delay = None
        self.destination_endpoint = None
        self.error_message = None
        self.expire_time = None
        self.pay_type = None
        self.performance = None
        self.precheck_status = None
        self.source_endpoint = None
        self.status = None
        self.structure_initialization = None
        self.structure_initialization_status = None
        self.synchronization_direction = None
        self.synchronization_job_class = None
        self.synchronization_job_name = None
        self.synchronization_objects = None

    def configure(self, **params):
        _params = _transfer_params(params)
        return self._client.configure_synchronization_job(synchronization_job_id=self.synchronization_job_id, **_params)

    def configure_synchronization_job_alert(self, **params):
        _params = _transfer_params(params)
        return self._client.configure_synchronization_job_alert(synchronization_job_id=self.synchronization_job_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        return self._client.delete_synchronization_job(synchronization_job_id=self.synchronization_job_id, **_params)

    def describe_initialization_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_initialization_status(synchronization_job_id=self.synchronization_job_id, **_params)

    def describe_synchronization_job_alert(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_synchronization_job_alert(synchronization_job_id=self.synchronization_job_id, **_params)

    def describe_synchronization_job_status(self, **params):
        _params = _transfer_params(params)
        return self._client.describe_synchronization_job_status(synchronization_job_id=self.synchronization_job_id, **_params)

    def modify_synchronization_object(self, **params):
        _params = _transfer_params(params)
        return self._client.modify_synchronization_object(synchronization_job_id=self.synchronization_job_id, **_params)

    def reset(self, **params):
        _params = _transfer_params(params)
        return self._client.reset_synchronization_job(synchronization_job_id=self.synchronization_job_id, **_params)

    def start(self, **params):
        _params = _transfer_params(params)
        return self._client.start_synchronization_job(synchronization_job_id=self.synchronization_job_id, **_params)

    def suspend(self, **params):
        _params = _transfer_params(params)
        return self._client.suspend_synchronization_job(synchronization_job_id=self.synchronization_job_id, **_params)

    def switch_synchronization_endpoint(self, **params):
        _params = _transfer_params(params)
        return self._client.switch_synchronization_endpoint(synchronization_job_id=self.synchronization_job_id, **_params)
