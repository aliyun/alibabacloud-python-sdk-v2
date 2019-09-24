代理
----------

``Alibaba Cloud Python SDK`` 支持用户使用网络代理。代理分为HTTP代理（
``http_proxy`` ）和HTTPS代理（ ``https_proxy``
）。如果您想使用代理，参照以下的使用方式

config接口显式传递
^^^^^^^^^^^^^^^^^^^

.. code:: python

   from alibabacloud import get_client, ClientConfig


   client_config = ClientConfig(http_proxy="http://...",https_proxy="https://...")
   ecs_client = get_client('ecs', access_key_id=access_key_id,
                           access_key_secret=access_key_secret,
                           region_id='cn-hangzhou',
                           config=client_config)
   response = ecs_client.describe_regions()
   print(response)

我们提供多种方式配置代理，参照 ::ref:`handle-client` 


配置文件
^^^^^^^^^^^^^^^^^^^

您也可以在配置文件进行配置环境变量，参照 ::ref:`handle-client` 


环境变量
^^^^^^^^^^^^^^^^^^^

阿里云 Python SDK支持从环境变量读取代理相关的配置： 

`HTTP_PROXY`: HTTP代理

`HTTPS_PROXY`： HTTPS代理 

以Linux为例，配置方式:

.. code:: 

   $ export ALIBABA_CLOUD_ACCESS_KEY_ID=<AccessKeyId>
   $ export ALIBABA_CLOUD_ACCESS_KEY_SECRET=<AccessKeySecret>
