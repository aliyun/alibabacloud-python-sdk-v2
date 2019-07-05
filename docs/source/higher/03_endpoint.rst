.. _handle-endpoint:

管理 Endpoint
===============

Endpoint 是您使用 ``Alibaba Cloud SDK`` 访问某个产品或者服务的访问域名。
``Alibaba Cloud Python SDK``\ 内部封装 ``Endpoint`` 寻址流程，获取 ``Endpoint`` 。您也可以通过直接指定 ``Endpoint`` 的方式省略寻址。


默认Endpoint寻址流程
--------------------

.. autoclass:: alibabacloud.endpoint.default_endpoint_resolver.DefaultEndpointResolver


用户自定义Endpoint寻址
----------------------

您的 ``Endpoint`` 解析需要实现一个 ``resolve`` 的接口，返回一个可用的 ``endpoint``

例如，您想自定义一个名为 ``CustomEndpointResolve`` 的 ``Endpoint`` 管理工具 ，可以参照以下代码：

.. code:: python

   class CustomEndpointResolve(object):
       def __init__(self):
           pass

       def resolve(self, retry_policy_context):
   	  # 返回一个可用的endpoint
           pass


使用用户自定义的寻址
------------------------

例如， 您自定义了一个名为 ``CustomEndpointResolve`` 的  ``Endpoint`` 管理工具 ，您可以使用以下方式引用它，替代我们默认的 ``Endpoint`` 寻址。

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
