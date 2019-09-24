# from alibabacloud.clients.eci_20180808 import EciClient
from alibabacloud.clients.ecs_20140526 import EcsClient
from alibabacloud.exceptions import ParamValidationException
from alibabacloud.vendored import six
from base import SDKTestBase


class GenTestCheckParams(SDKTestBase):

    def test_rpc_query_list(self):
        # check one
        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())
        tag = 'hi'
        try:
            context = ecs_client.describe_tags(list_of_tag=tag)
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
        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())
        tag = [
            'hi'
        ]
        try:
            context = ecs_client.describe_tags(list_of_tag=tag)
            assert False
        except ParamValidationException as e:
            if six.PY2:
                self.assertEqual(e.error_message,
                                 "Parameter validation failed: Invalid type for parameter Tag.0.Tag, value: hi, type: <type 'str'>, valid types: <type 'dict'>")

            else:
                self.assertEqual(e.error_message,
                                 "Parameter validation failed: Invalid type for parameter Tag.0.Tag, value: hi, type: <class 'str'>, valid types: <class 'dict'>")
