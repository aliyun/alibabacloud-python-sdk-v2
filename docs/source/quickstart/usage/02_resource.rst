资源使用
--------------

资源（ ``resource`` ） 代表 ``Alibaba Cloud Python SDK``
面向对象的接口，提供比 ``client`` 进行的原始低级调用更高级别的抽象接口。

创建服务资源
^^^^^^^^^^^^^^^^^^^

要访问 ``Alibaba Cloud Python SDK`` 的资源，您需要创建该资源对象（
``resource``
）。创建的时候，您需要指定 访问凭证 以及地域和可用区（
``region_id``\ ） 以及即将访问的 resource。

**访问凭证：**
访问凭证相当于您在阿里云的身份标识。为了您的账号安全，我们强烈建议您使用 ::ref:`instance-credentials` 。
当然，您也可以使用其他凭证，详情参考 ::ref:`credentials-config` 

**region_id：** region_id
是您创建资源的所在区域，查找参考: \ `地域和可用区 <https://help.aliyun.com/document/detail/40654.html>`_

**resource：** resource
是您即将访问的资源，可用资源参照 ::ref:`usage-resources` 

.. code:: python

   import alibabacloud
   # 创建ecs资源
   ecs_resource = alibabacloud.get_resource('ecs', access_key_id=access_key_id,
                                            access_key_secret=access_key_secret,
                                            region_id=region_id)

创建 ``resource`` 后，您可以通过该 ``resource`` 操作其对应服务：

.. code:: python

   for instance in ecs_resource.instances.all():
       print(instance.instance_id)
