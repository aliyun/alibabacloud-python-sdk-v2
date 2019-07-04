客户端使用
-----------

客户端（ ``client`` ）是 ``Alibaba Cloud Python SDK``
比较底层的实现，您构造的所有的API请求或者服务都通过 ``client`` 来实现。


创建服务客户端
^^^^^^^^^^^^^^^^^

要访问 ``Alibaba Cloud Python SDK`` 的服务或资源，您需要创建一个客户端（
``client``）。创建的时候，您需要指定 访问凭证
、地域和可用区（``region_id`` ）以及即将访问的 service 。

**访问凭证：**
访问凭证相当于您在阿里云的身份标识。为了您的账号安全，我们强烈建议您使用 ::ref:`instance-credentials` 。
当然，您也可以使用其他凭证，详情参考 ::ref:`credentials-config` 

**region_id：** region_id
是您创建资源的所在区域，查找参考 \ `地域和可用区 <https://help.aliyun.com/document/detail/40654.html>`_

**service：** service
是您即将访问的服务，可用服务参照 ::ref:`usage-client`

.. code:: python

   from alibabacloud import get_client
   # 创建一个ecs client
   ecs_client = get_client('ecs', access_key_id=your_access_key_id,
                            access_key_secret=your_access_key_secret,
                            region_id=your_region_id)

创建 ``client`` 后，您可以通过该 ``client`` 调用其提供的API：

.. code:: python

   result = ecs_client.describe_regions()
   print(result.get("Regions"))  # 获取alibabacloud全球19个region
