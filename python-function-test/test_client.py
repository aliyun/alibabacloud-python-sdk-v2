import os
# from base import TestCase
from unittest import TestCase

import alibabacloud
from alibabacloud.clients.ecs_20140526 import EcsClient
from alibabacloud.exceptions import ServiceNameInvalidException, ApiVersionInvalidException


class AlibabaClientTest(TestCase):

    def setUp(self):
        self.access_key_id = os.environ.get("ACCESS_KEY_ID")
        self.access_key_secret = os.environ.get("ACCESS_KEY_SECRET")
        self.region_id = os.environ.get("REGION_ID")

    def test_ecs_client(self):
        client = alibabacloud.get_client(service_name='Ecs', api_version='2014-05-26',
                                         access_key_id=self.access_key_id,
                                         access_key_secret=self.access_key_secret,
                                         region_id=self.region_id)
        self.assertTrue(isinstance(client, EcsClient))
        result = client.describe_regions()
        self.assertTrue(result.get('Regions'))

    def test_not_support_client(self):
        try:
            client = alibabacloud.get_client(service_name='Ems', api_version='2014-05-26',
                                             access_key_id=self.access_key_id,
                                             access_key_secret=self.access_key_secret,
                                             region_id=self.region_id)
            assert False
        except ServiceNameInvalidException as e:
            self.assertTrue(e.error_message, 'No such service_name Ems')

    def test_not_support_version(self):
        try:
            client = alibabacloud.get_client(service_name='ECS', api_version='2015-05-26',
                                             access_key_id=self.access_key_id,
                                             access_key_secret=self.access_key_secret,
                                             region_id=self.region_id)
            assert False
        except ApiVersionInvalidException as e:
            self.assertTrue(e.error_message,
                            "ECS no such api_version '2015-05-26'. Please check your API Version.\n"
                            "We now support api_version: 2014-05-26")
