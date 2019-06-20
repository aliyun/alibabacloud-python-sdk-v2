from alibabacloud import AccessKeyCredentials, StaticCredentialsProvider
from alibabacloud.client import AlibabaCloudClient
from alibabacloud.request import APIRequest


class RamClient(AlibabaCloudClient):

    def __init__(self, client_config, credentials_provider=None, custom_retry_policy=None,
                 custom_endpoint_resolver=None):
        AlibabaCloudClient.__init__(self, client_config,
                                    credentials_provider=credentials_provider,
                                    custom_retry_policy=custom_retry_policy,
                                    custom_endpoint_resolver=custom_endpoint_resolver)
        self.product_code = 'Ram'
        self.api_version = '2015-05-01'
        self.location_service_code = 'ram'
        self.location_endpoint_type = 'openAPI'

    def create_access_key(self, user_name=None):
        api_request = APIRequest('CreateAccessKey', 'GET', 'https', 'RPC', 'query')
        api_request._params = {"UserName": user_name}
        return self._handle_request(api_request).result


class STSTokenProvider(object):
    def __init__(self,client_config, access_key_id, access_key_secret, user_name):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.user_name = user_name
        self.client_config = client_config

    def get_sub_credentials(self):
        credentials = AccessKeyCredentials(self.access_key_id, self.access_key_secret)
        credentials_provider = StaticCredentialsProvider(credentials)
        ram_client = RamClient(client_config=self.client_config,credentials_provider=credentials_provider)
        # 0，必须是主账号，使用已有角色处理已有user
        response = ram_client.create_access_key(user_name=self.user_name)
        credential = response.get('AccessKey')
        return credential
