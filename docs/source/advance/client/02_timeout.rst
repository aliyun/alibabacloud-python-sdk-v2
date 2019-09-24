超时
-----

``Alibaba Cloud Python SDK`` 超时分为连接超时（ ``connection_timeout``
）和读超时（ ``read_timeout`` ）。

**connection_timeout：**
连接超时。TCP建立连接的时间阈值，单位为秒。默认5秒 

**read_timeout :**
读超时。 客户端接收到服务端响应的时间阈值，单位为秒。默认10秒

例如，您想自定义超时时间，请使用以下代码。

.. code:: python

   from alibabacloud import get_client, ClientConfig

   client_config = ClientConfig(connection_timeout=10, read_timeout=20)
   # 创建ecs client
   ecs_client = get_client('ecs', access_key_id=access_key_id,
                           access_key_secret=access_key_secret,
                           region_id='cn-hangzhou',
                           config=client_config)
   response = ecs_client.describe_regions()
   print(response)

我们提供了多种方式的配置超时，参照 ::ref:`handle-client` 
