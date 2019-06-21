from alibabacloud.clients.ecs_20140526 import EcsClient
from base import SDKTestBase, MyServer


class UserAgentTest(SDKTestBase):

    @staticmethod
    def joint_default_user_agent():
        import platform
        base = '%s (%s %s;%s) Python/%s Alibabacloud/%s python-requests/%s' \
               % ('AlibabaCloud',
                  platform.system(),
                  platform.release(),
                  platform.machine(),
                  platform.python_version(),
                  __import__('alibabacloud').__version__,
                  __import__(
                      'alibabacloud.vendored.requests.__version__', globals(), locals(),
                      ['vendored', 'requests', '__version__'], 0).__version__)
        return base

    def init_temp_client_config(self):
        client_config = self.client_config
        client_config.http_port = 51352
        client_config.endpoint = "localhost"
        return client_config

    def test_default_user_agent(self):
        client_config = self.init_temp_client_config()
        client = EcsClient(client_config, self.init_credentials_provider())
        with MyServer() as s:
            client.describe_instances()
            user_agent = s.headers.get('User-Agent')
        self.assertEqual(self.joint_default_user_agent(), user_agent)

    def test_append_user_agent(self):
        client_config = self.init_temp_client_config()
        client_config.user_agent = 'alibabacloudpythonsdk'
        client = EcsClient(client_config, self.init_credentials_provider())
        with MyServer() as s:
            client.describe_instances()
            user_agent = s.headers.get('User-Agent')
        self.assertEqual(self.joint_default_user_agent() + ' alibabacloudpythonsdk', user_agent)
