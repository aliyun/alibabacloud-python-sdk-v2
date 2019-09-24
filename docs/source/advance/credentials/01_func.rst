方法参数显示传递
-----------------

显式传递方式存在硬编码以及安全问题，请您慎重使用，并保管好自己的
AccessKey

get_client方法显式传递凭证信息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

即 ``access_key_id`` 和 ``access_key_secret``

.. code:: python

   import alibabacloud
   client = alibabacloud.get_client(service_name='Ecs',
                                access_key_id=access_key_id,
                                access_key_secret=access_key_secret,
                                region_id="cn-hangzhou")

get_resource方法显式传递凭证信息
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

即 ``access_key_id`` 和 ``access_key_secret``

.. code:: python

   import alibabacloud
   resource = alibabacloud.get_resource(service_name='Ecs',
                                access_key_id=access_key_id,
                                access_key_secret=access_key_secret,
                                region_id="cn-hangzhou")
