# encoding:utf-8
import sys
import threading
from base import SDKTestBase, MyServer

# the version under py3 use the different package
if sys.version_info[0] == 3:
    from http.server import SimpleHTTPRequestHandler
    from http.server import HTTPServer
else:
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer

from alibabacloud.client import ClientConfig
from alibabacloud.clients.ecs_20140526 import EcsClient


# class MyServer:
#     _headers = {}
#     _url = ''
#
#     def __enter__(self):
#         class ServerHandler(SimpleHTTPRequestHandler):
#
#             def do_GET(_self):
#                 _self.protocol_version = 'HTTP/1.1'
#                 self._headers = _self.headers
#                 self._url = _self.path
#                 _self.send_response(200)
#                 _self.send_header("Content-type", "application/json")
#                 _self.end_headers()
#                 _self.wfile.write(b"{}")
#
#         self.server = HTTPServer(("", 51352), ServerHandler)
#
#         def thread_func():
#             self.server.serve_forever()
#
#         thread = threading.Thread(target=thread_func)
#         thread.start()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.server:
#             self.server.shutdown()
#             self.server = None
#
#     @property
#     def headers(self):
#         return self._headers
#
#     @property
#     def url(self):
#         return self._url
#
#     @property
#     def content(self):
#         class Response:
#             def __init__(self, headers):
#                 self.headers = headers
#         response = Response(self._headers)
#         return response


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
        client = EcsClient(client_config)
        with MyServer() as s:
            client.describe_instances()
            user_agent = s.headers.get('User-Agent')
        self.assertEqual(self.joint_default_user_agent(), user_agent)

    def test_append_user_agent(self):
        client_config = self.init_temp_client_config()
        client_config.user_agent = 'alibabacloudpythonsdk'
        client = EcsClient(client_config)
        with MyServer() as s:
            client.describe_instances()
            user_agent = s.headers.get('User-Agent')
        self.assertEqual(self.joint_default_user_agent() + ' alibabacloudpythonsdk', user_agent)
