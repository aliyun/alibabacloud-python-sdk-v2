import os
import shutil
import tempfile

from alibabacloud import get_client, ClientConfig
from base import SDKTestBase


class VerifyTest(SDKTestBase):

    def test_response_set_path(self):
        client_config = self.client_config
        self.assertEqual(client_config.verify, True)

    def write_config(self, credential):
        with open(self.credentials_file, 'w') as f:
            f.write(credential)

    def test_file_ca(self):
        self.tempdir = tempfile.mkdtemp()
        self.credentials_file = os.path.join(self.tempdir, 'config')
        os.environ['ALIBABA_CLOUD_CONFIG_FILE'] = self.credentials_file

        config_file = (
            '[default]\n'
            'region_id = us-west-1\n'
            'endpoint = somewhere.you.will.never.get\n'
            'verify = /path/cacerts.pem\n'
        )
        self.write_config(config_file)
        client = get_client('ecs', access_key_id=self.access_key_id,
                            access_key_secret=self.access_key_secret,
                            region_id='hangzhou', endpoint='123')
        self.assertEqual(client.config.verify, "/path/cacerts.pem")

        shutil.rmtree(self.tempdir)
        os.environ.pop('ALIBABA_CLOUD_CONFIG_FILE')

    def test_file_env_ca(self):
        self.tempdir = tempfile.mkdtemp()
        self.credentials_file = os.path.join(self.tempdir, 'config')
        os.environ['ALIBABA_CLOUD_CONFIG_FILE'] = self.credentials_file
        os.environ['ALIBABA_CLOUD_CA_BUNDLE'] = "/path/cacerts.pem"

        config_file = (
            '[default]\n'
            'region_id = us-west-1\n'
            'endpoint = somewhere.you.will.never.get\n'
            'verify = 11111111111\n'
        )
        self.write_config(config_file)
        client = get_client('ecs', access_key_id=self.access_key_id,
                            access_key_secret=self.access_key_secret,
                            region_id='hangzhou', endpoint='123')
        self.assertEqual(client.config.verify, "/path/cacerts.pem")

        shutil.rmtree(self.tempdir)
        os.environ.pop('ALIBABA_CLOUD_CONFIG_FILE')
        os.environ.pop('ALIBABA_CLOUD_CA_BUNDLE')

    def test_client_file_env_ca(self):
        self.tempdir = tempfile.mkdtemp()
        self.credentials_file = os.path.join(self.tempdir, 'config')
        os.environ['ALIBABA_CLOUD_CONFIG_FILE'] = self.credentials_file
        os.environ['ALIBABA_CLOUD_CA_BUNDLE'] = "/path/cacerts.pem"

        config_file = (
            '[default]\n'
            'region_id = us-west-1\n'
            'endpoint = somewhere.you.will.never.get\n'
            'verify = 11111111111\n'
        )
        self.write_config(config_file, )
        config = ClientConfig(region_id='hangzhou', endpoint='123', verify="client/config.pem")
        client = get_client('ecs', access_key_id=self.access_key_id,
                            access_key_secret=self.access_key_secret,
                            config=config)
        self.assertEqual(client.config.verify, "client/config.pem")

        shutil.rmtree(self.tempdir)
        os.environ.pop('ALIBABA_CLOUD_CONFIG_FILE')
        os.environ.pop('ALIBABA_CLOUD_CA_BUNDLE')
