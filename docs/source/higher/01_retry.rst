.. _handle-retry:

管理重试策略
===============

``Alibaba Cloud Python SDK`` 提供默认的重试和退避策略，由
``Alibaba Cloud`` 定义为可重试 API，\ ``Alibaba Cloud Python SDK``
才允许重试，重试当前仅支持 ECS 产品。\ **除 ECS 外的其他产品，当前均不支持重试。**


默认重试策略
-------------------------------

（API文档）


用户自定义重试策略
-------------------------------

您自定义的重试策略需要实现一个 ``should_retry`` 的接口。

例如，您想自定义一个名为 ``CustomRetryPolicy`` 的重试策略，可以参照以下代码：

.. code:: python

       class CustomRetryPolicy(object):
         def __init__(self):
             pass

         def should_retry(self, retry_policy_context):
             pass


使用用户自定义的重试策略
-------------------------------
例如， 您自定义了一个名为 ``CustomRetryPolicy`` 的重试策略，您可以使用以下方式引用它，替代我们默认的重试策略。

.. code:: python

   from alibabacloud import get_client, ClientConfig

   client_config = ClientConfig(connection_timeout=10, read_timeout=20)
   ecs_client = get_client('ecs', access_key_id=access_key_id,
                           access_key_secret=access_key_secret,
                           region_id='cn-hangzhou', config=client_config,
                           retry_policy=CustomRetryPolicy())
   response = ecs_client.describe_regions()
   print(response)
