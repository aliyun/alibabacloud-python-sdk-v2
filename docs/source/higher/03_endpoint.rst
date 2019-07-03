.. _handle-endpoint:

管理endpoint
============

Endpoint是您使用Alibaba Cloud 访问某个产品或者服务的访问域名。
``Alibaba Cloud Python SDK``\ 内部封装Endpoint寻址流程，获取Endpoint。您也可以通过直接指定endpoint的方式省略寻址。

.. _header-n3:

默认endpoint寻址流程
--------------------

.. autoclass:: alibabacloud.endpoint.default_endpoint_resolver.DefaultEndpointResolver

.. _header-n5:

用户自定义endpoint寻址
----------------------

您的endpoint解析需要实现一个resolve的接口，返回一个endpoint

.. _header-n8:

使用用户自定义的重试策略
------------------------

例如，您定一个CustomEndpointResolve的重试策略，您可以参照以下代码：

.. code:: python

   from alibabacloud import get_client, ClientConfig


   class CustomEndpointResolve(object):
       def __init__(self):
           pass

       def resolve(self, retry_policy_context):
   	  # 返回一个可用的endpoint
           pass

   client_config = ClientConfig(connection_timeout=10, read_timeout=20)
   ecs_client = get_client('ecs', access_key_id=access_key_id,
                           access_key_secret=access_key_secret,
                           region_id='cn-hangzhou', config=client_config,
                           endpoint_resolver=CustomEndpointResolve())
   response = ecs_client.describe_regions()
   print(response)
