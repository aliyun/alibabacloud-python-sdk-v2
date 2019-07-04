管理用户凭证
============

``credentials_provider`` 是 ``Alibaba Cloud Python SDK``
提供的新特性。它是阿里云的访问凭证（ ``credentials`` ）的提供者，通过\ ``credentials_provider``\ 的\ ``provider``\ 接口可以获取真实的访问凭证
``credentials``\ 。


默认的 ``credentials_provider``
-------------------------------

``Alibaba Cloud Python SDK`` 提供3种类型的 ``credentials_provider``\ 。

.. module:: alibabacloud

.. autoclass:: alibabacloud.credentials.provider.PredefinedChainCredentialsProvider
.. autoclass:: alibabacloud.credentials.provider.EnvCredentialsProvider
.. autoclass:: alibabacloud.credentials.provider.ProfileCredentialsProvider
.. autoclass:: alibabacloud.credentials.provider.InstanceProfileCredentialsProvider


用户自定义的 ``credentials_provider``
-------------------------------------

``Alibaba Cloud Python SDK`` 支持用户使用自定义的
``credentials_provider`` ,但是该 ``credentials_provider`` 必须实现一个
``provide`` 返回最终的 ``credentials`` .

例如，您想自定义一个名为 ``CustomCredentialsProvider`` 的 ``credentials_provider`` ，可以参照以下代码：

.. code:: python

   class CustomCredentialsProvider(object):
       def __init__(self):
           pass

       def provide(self, retry_policy_context):
   	  # 返回 credentials
           pass


使用用户自定义的 ``credentials_provider``
-----------------------------------------

例如， 您自定义了一个名为 ``CustomCredentialsProvider`` 的 ``credentials_provider`` ，您可以使用以下方式引用它，替代我们默认的 ``credentials_provider``。

.. code:: python

   from alibabacloud import get_client, ClientConfig

   client_config = ClientConfig(connection_timeout=10, read_timeout=20)
   ecs_client = get_client('ecs', access_key_id=access_key_id,
                           access_key_secret=access_key_secret,
                           region_id='cn-hangzhou', config=client_config,
                           credentials_provider=CustomCredentialsProvider())
   response = ecs_client.describe_regions()
   print(response)
