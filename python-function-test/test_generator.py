# from alibabacloud.clients.eci_20180808 import EciClient
from alibabacloud.clients.ecs_20140526 import EcsClient
from alibabacloud.clients.edas_20170801 import EdasClient
from alibabacloud.clients.linkwan_20181230 import LinkWANClient
from alibabacloud.exceptions import ServerException, HttpErrorException, ParamValidationException
from alibabacloud.vendored import six
from base import SDKTestBase
from utils import crClient, CSBClient, OpenanalyticsClient


class GenTestBase(SDKTestBase):

    def test_rpc_query_list(self):
        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())
        tag = [
            {"xxx": 123,
             "aaaa": 456,
             },
            {"Key": 234,
             "qqq": 345,
             },
        ]
        try:
            context = ecs_client.add_tags(list_of_tag=tag, resource_type="instance",
                                          resource_id="i-bp13ozj6v9ckzcq8sjxw")
            assert False
        except ServerException as e:
            self.assertEqual(e.http_status, 400)
            self.assertEqual(e.endpoint, 'ecs-cn-hangzhou.aliyuncs.com')
            self.assertEqual(e.error_code, 'InvalidTagValue.Malformed')
            self.assertEqual(e.error_message, 'The specified Tag.n.Value is not valid.')

    def test_rpc_query_get(self):
        # TODO
        ecs_client = EcsClient(self.client_config, self.init_credentials_provider())
        tag = "hi"
        try:
            context = ecs_client.add_tags(list_of_tag=tag, resource_type="instance",
                                          resource_id="i-bp13ozj6v9ckzcq8sjxw")
            assert False
        except ParamValidationException as e:
            if six.PY2:
                self.assertEqual(e.error_message,
                                 "Parameter validation failed: Invalid type for parameter Tag, value: hi, type: <type 'str'>, valid types: <type 'list'>")
            else:
                self.assertEqual(e.error_message,
                                 "Parameter validation failed: Invalid type for parameter Tag, value: hi, type: <class 'str'>, valid types: <class 'list'>")

    def test_rpc_body_get(self):

        open_client = OpenanalyticsClient(self.client_config, self.init_credentials_provider())
        try:
            context = open_client.get_region_status()
            assert False
        except ServerException as e:
            self.assertEqual(e.http_status, 400)
            self.assertEqual(e.error_code, 'InvalidVersion')
            self.assertEqual(e.error_message, 'Specified parameter Version is not valid.')

    def test_rpc_body_get1(self):
        link_client = LinkWANClient(self.client_config, self.init_credentials_provider())
        try:
            context = link_client.describe_regions()
            assert False
        except HttpErrorException as e:
            self.assertEqual(e.error_message,
                             "HTTPSConnectionPool(host='linkwan.cn-hangzhou.aliyuncs.com', port=443): Read timed out. (read timeout=10)")
        except ServerException as e:
            self.assertEqual(e.http_status, 503)
            self.assertEqual(e.error_code, 'ServiceUnavailable')
            self.assertEqual(e.error_message,
                             'The request has failed due to a temporary failure of the server.')

    def test_rpc_body_post(self):
        csb_client = CSBClient(self.client_config, self.init_credentials_provider())
        try:
            context = csb_client.approve_order_list()
            assert False
        except ServerException as e:
            self.assertEqual(e.http_status, 404)
            self.assertEqual(e.error_code, "InvalidApi.NotFound")
            self.assertEqual(e.error_message,
                             "Specified api is not found, please check your url and method.")

    def test_rpc_body_https(self):
        # TODO
        link_client = LinkWANClient(self.client_config, self.init_credentials_provider())
        try:
            context = link_client.list_gateway_tuple_orders(offset="123", limit="12")
            assert False
        except ServerException as e:
            self.assertEqual(e.http_status, 503)
            self.assertEqual(e.error_code, "ServiceUnavailable")
            self.assertEqual(e.error_message,
                             "The request has failed due to a temporary failure of the server.")

    def test_roa_path(self):
        cr_client = crClient(self.client_config, self.init_credentials_provider())
        try:
            context = cr_client.get_namespace_authorization_list(namespace="123")
            assert False
        except ServerException as e:
            self.assertEqual(e.http_status, 500)
            self.assertEqual(e.error_code, 'SDK.UnknownServerError')
            self.assertTrue('rpc_invalid_arg' in e.error_message)

    def test_roa_query_get_post_delete_put(self):
        self.client_config.endpoint = "edas.cn-hangzhou.aliyuncs.com"
        edas_client = EdasClient(self.client_config, self.init_credentials_provider())
        result = edas_client.list_application()
        self.assertEqual(result.get('Message'), 'success')
        self.assertEqual(result.get('Code'), 200)

        result = edas_client.list_slb()
        self.assertEqual(result.get('Message'), 'success')
        self.assertEqual(result.get('Code'), 200)

        try:
            context = edas_client.disable_degrade_control(app_id='123', rule_id=[{"name": 123}])
            assert False
        except ServerException as e:

            self.assertEqual(e.http_status, 400)
            self.assertEqual(e.error_code, 'MissingRuleId')
            self.assertEqual(e.error_message, 'RuleId is mandatory for this action.')

        result = edas_client.delete_application(app_id="123")
        self.assertEqual(result.get('Message'), 'No permissions')
        self.assertEqual(result.get('Code'), 500)
