重试
---------

``Alibaba Cloud Python SDK`` 对当前仅对 ECS 产品的API
设置了默认重试。但是您可以在配置当中关闭默认重试或者定制自己的重试策略。

**max\ retry\ times**\ ：单个请求的最大重试次数。默认为3次。
**enable_retry**\ ：是否重试的开关，默认True开启。一旦关闭，则该 client
下所有请求不重试，\ ``max_retry_times`` 配置将不启用。

例如，您想自定义是否重试，请使用以下代码。

.. code:: python

   from alibabacloud import get_client, ClientConfig
    # 您也可以配置enable_retry=false，关闭默认的重试
   client_config = ClientConfig(max_retry_times=5) 
   # 创建ecs client
   ecs_client = get_client('ecs', access_key_id=access_key_id,
                           access_key_secret=access_key_secret,
                           region_id='cn-hangzhou',
                           config=client_config)
   response = ecs_client.describe_regions()
   print(response)

当然，您也可以使用其他方式配置重试，参照 ::ref:`handle-retry` 
