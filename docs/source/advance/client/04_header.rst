自定制请求头
-------------

``Alibaba Cloud Python SDK``
为客户端发送的每一个请求自定义请求头 `User-Agent` 。默认的 `User-Agent`
包含您的Python版本以及 ``Alibaba Cloud Python SDK`` 的版本信息。
我们同样支持您 **追加** 自己的 `User-Agent` 信息。

例如，淘宝公司想定制自己的 `User-Agent` ，请使用以下代码，\ *当前仅支持追加*\ 。

.. code:: python

   from alibabacloud import get_client, ClientConfig

   client_config = ClientConfig(user_agent="taobao/1.3.2")

   ecs_client = get_client('ecs', access_key_id=access_key_id,
                           access_key_secret=access_key_secret,
   						region_id='cn-hangzhou',
                           config=client_config)
   response = ecs_client.describe_regions()
   # 请求User-Agent 为：AlibabaCloud (Windows 10;AMD64) Python/3.7.2 Alibabacloud/0.4.4 python-requests/2.18.3 taobao/1.3.2

追加 `User-Agent` 的配置方式有多种，参照 ::ref:`handle-client` 
