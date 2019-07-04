地域配置
----------------

使用地域可以访问实际位于特定地理区域的 阿里云 服务。

选择地域
^^^^^^^^^^^^

您可以指定地域名称，\ ``Alibaba Cloud Python SDK`` 内置了访问域名（
``Endpoint`` ）寻址模块，当您调用 ``Alibaba Cloud Python SDK``
对一个阿里云服务发起请求时，\ ``Alibaba Cloud Python SDK``
会自动根据您在创建 ``Client`` 时指定的地域ID（Region ID）和产品ID来找到
``Endpoint`` 。

有关所有 阿里云 服务的区域最新列表，请参阅
`地域与可用区 <https://help.aliyun.com/document_detail/40654.html>`__

例如，要将 ECS 客户端配置为使用 中国（杭州）区域，请使用以下代码。

.. code:: python

   from alibabacloud import get_client
   # 创建一个ecs client
   ecs_client = get_client('ecs', access_key_id=your_access_key_id,
                            access_key_secret=your_access_key_secret,
                            region_id='cn-hangzhou')

注意：如果要为同一项服务使用多个区域，请创建多个客户端 —
即每个区域一个客户端。

使用特定访问域名
^^^^^^^^^^^^^^^^^^^^^^^^

您也可以使用 ``Endpoint`` 配置，为各个 ``Alibaba Cloud Python SDK``
客户端配置使用一个区域内的特定访问域名。

例如，要将 ECS 客户端配置为使用
中国（杭州）的特定访问域名，请使用以下代码。

.. code:: python

   from alibabacloud import get_client
   # 创建一个ecs client
   ecs_client = get_client('ecs', access_key_id=your_access_key_id,
                            access_key_secret=your_access_key_secret,
                            endpoint="ecs-cn-hangzhou.aliyuncs.com)

如果您存在多个 ``Endpoint`` 的配置，您可以参照 ::ref:`handle-client` 

地域以及访问域名更多配置参照 ::ref:`handle-endpoint` 
