# Copyright 2018 Alibaba Cloud Inc. All rights reserved.
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
# -*- coding: utf-8 -*-
import time

from alibabacloud import get_resource
from alibabacloud.exceptions import ServerException
from tests.base import SDKTestBase


class EcsResourceTest(SDKTestBase):
    def __init__(self, *args, **kwargs):
        SDKTestBase.__init__(self, *args, **kwargs)

    def get_resource(self, service, **kwargs):
        return self._get_resource(service, **kwargs)

    def test_cdn_resource(self):
        # TODO 没有fc_triggers的接口
        cdn_resource = self.get_resource("cdn")
        try:
            for _ in cdn_resource.fc_triggers.all(): pass
            assert False
        except ServerException as e:
            self.assertTrue(e.http_status, 400)
            self.assertTrue(e.endpoint, "cdn.aliyuncs.com")
            self.assertTrue(e.error_code, "MissingEventMetaName")
            self.assertTrue(e.error_message, "EventMetaName is mandatory for this action.")

    def test_ens_resource(self):
        # ens, all
        #  TODO  filter 为什么不是1
        ens_resource = self.get_resource("ens")
        self.assertTrue(len(list(ens_resource.images.all())) > 0)
        self.assertTrue(
            len(list(ens_resource.images.filter(image_id="m-2Q3022yr24iUy5yQipMTd8"))) >= 1)

    def test_ram_resource(self):
        # ram, collection, create, method, refresh, username
        # filter ,不能filter
        ram_resource = self.get_resource("ram")
        for user in ram_resource.users.all():
            if user.user_name.startswith("yan"):
                user.delete()
        ram_user = ram_resource.create_user(user_name="yan", email="123@163.com")
        ram_user.refresh()
        ram_user.create_login_profile(password="123yan123")
        login_profile = ram_user.get_login_profile()

        self.assertTrue(login_profile.get("LoginProfile"))
        ram_user.delete_login_profile()
        ram_user.delete()

    def test_rds_resource(self):
        rds_resource = self.get_resource("rds")
        for db_instance in rds_resource.db_instances.all():
            db_instance.delete()
        rds_instance = rds_resource.create_db_instance(Engine="MySQL", EngineVersion="5.6",
                                                       DBInstanceClass="rds.mysql.s1.small",
                                                       DBInstanceStorage=20,
                                                       DBInstanceNetType="Internet",
                                                       PayType="Postpaid",
                                                       SecurityIPList="10.23.12.27/24")
        self.assertEqual(len(list(rds_resource.db_instances.all())), 1)

        time.sleep(60)
        # 子资源database
        self.assertEqual(len(list(rds_instance.dbs.all())), 0)

        rds_database = rds_instance.create_database(DBName="rds_mysql", CharacterSetName="gbk",
                                                    DBDescription="just-test")
        self.assertEqual(len(list(rds_instance.dbs.all())), 1)
        for data_base in rds_instance.dbs.all():
            data_base.delete()

        self.assertEqual(len(list(rds_instance.accounts.all())), 0)
        rds_account = rds_instance.create_account(AccountName="test1", AccountPassword="Test123456",
                                                  AccountDescription="aliyunsdk")
        self.assertEqual(len(list(rds_instance.accounts.all())), 1)
        rds_account.refresh()
        self.assertEqual(rds_account.account_description, "aliyunsdk")
        rds_account.modify_description(AccountDescription="just a test")
        rds_account.refresh()
        self.assertEqual(rds_account.account_description, "just a test")
        rds_account.delete()

        # 子资源 backups
        self.assertEqual(len(list(rds_instance.backups.all())), 0)
        rds_backup = rds_instance.create_backup(BackupMethod="Physical", BackupStrategy="db",
                                                DBName="rds_mysql")
        # TODO bug, 待青塘解决

        # rds_backup.refresh()
        # rds_backup.delete()
        # self.assertEqual(len(list(rds_instance.backups.all())), 1)
