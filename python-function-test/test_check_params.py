import os

from alibabacloud.client import ClientConfig
from alibabacloud.clients.eci_20180808 import EciClient
from alibabacloud.clients.ecs_20140526 import EcsClient
from alibabacloud.exceptions import ServerException, ParamValidationException
from alibabacloud.vendored import six
from base import SDKTestBase


class GenTestCheckParams(SDKTestBase):

    def test_rpc_query_list(self):
        # check one
        ecs_client = EcsClient(self.client_config)
        tag = 'hi'
        try:
            context = ecs_client.describe_tags(tag=tag)
            assert False
        except ParamValidationException as e:
            if six.PY2:
                self.assertEqual(e.error_message,
                                 "Parameter validation failed: Invalid type for parameter Tag, value: hi, type: <type 'str'>, valid types: <type 'list'>")
            else:
                self.assertEqual(e.error_message,
                                 "Parameter validation failed: Invalid type for parameter Tag, value: hi, type: <class 'str'>, valid types: <class 'list'>")

    def test_rpc_query_list1(self):
        # check two
        ecs_client = EcsClient(self.client_config)
        tag = [
            'hi'
        ]
        try:
            context = ecs_client.describe_tags(tag=tag)
            assert False
        except ParamValidationException as e:
            if six.PY2:
                self.assertEqual(e.error_message,
                                 "Parameter validation failed: Invalid type for parameter Tag.0.Tag, value: hi, type: <type 'str'>, valid types: <type 'dict'>")

            else:
                self.assertEqual(e.error_message,
                                 "Parameter validation failed: Invalid type for parameter Tag.0.Tag, value: hi, type: <class 'str'>, valid types: <class 'dict'>")

    def test_rpc_query_list2(self):
        # tree layer check
        eci_client = EciClient(self.client_config)
        container = [{
            "Port": {
                "Protocol": 'https',
                "Port": '80'
            }

        },
        ]
        try:
            context = eci_client.update_container_group(container=container)
            assert False
        except ParamValidationException as e:
            if six.PY2:
                self.assertEqual(e.error_message,
                                 "Parameter validation failed: Invalid type for parameter Container.0.Container.Port, value: {'Protocol': 'https', 'Port': '80'}, type: <type 'dict'>, valid types: <type 'list'>")
            else:
                self.assertEqual(e.error_message,
                                 "Parameter validation failed: Invalid type for parameter Container.0.Container.Port, value: {'Protocol': 'https', 'Port': '80'}, type: <class 'dict'>, valid types: <class 'list'>")

    def test_rpc_query_list3(self):
        # tree layer check
        eci_client = EciClient(self.client_config)
        container = [{
            "Port": [{
                "Protocol": 'https',
                "Port": '80'
            }, ],
        },
        ]
        try:
            context = eci_client.update_container_group(container=container)
            assert False
        except ServerException as e:
            self.assertEqual(e.http_status, 400)
            self.assertEqual(e.error_code, "MissingContainerGroupId")
            self.assertEqual(e.error_message, "ContainerGroupId is mandatory for this action.")

    def test_rpc_query_with_extra_params(self):
        # tree layer check
        eci_client = EciClient(self.client_config)
        container = [{
            "Port": [{
                "Protocol": 'https',
                "Port": '80'
            }, ],
            "xxx": "error"
        },
        ]
        try:
            context = eci_client.update_container_group(container=container)
            assert False
        except ServerException as e:
            self.assertEqual(e.http_status, 400)
            self.assertEqual(e.error_code, "MissingContainerGroupId")
            self.assertEqual(e.error_message, "ContainerGroupId is mandatory for this action.")
