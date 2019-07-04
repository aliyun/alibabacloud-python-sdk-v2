.. _handle-client:

管理客户端配置
===============

``Alibaba Cloud Python SDK`` 提供多种方式管理您发送请求时候的 ``Config``
，一般，我们遵循这样的方法：\ **尝试各种位置，直到找到值**\ 。
``Alibaba Cloud Python SDK`` 使用以下方式查找您的配置：

-  创建客户端时显式传递为参数

-  环境变量

-  文件

-  默认配置


创建客户端时显式传递参数
-------------------------------


方式一：get_client接口显式传递
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``get_client`` 接口递仅仅支持 ``region_id`` 以及 ``endpoint``
显式传递。此处指定的 ``region_id`` 和 ``endpoint``
优先级高于任何其他的链式 ``Config`` 指定。

**endpoint:**
Endpoint是阿里云服务的API服务端地址。针对不同的地域，单个服务可能有不同的Endpoint。例如，云服务器（ECS）在华东1（杭州）地域的Endpoint是
ecs-cn-hangzhou.aliyuncs.com，
而在日本（东京）地域的Endpoint是ecs.ap-northeast-1.aliyuncs.com。
如果您不显式指定endpoint，阿里云SDK内置了
Endpoint寻址模块，当您调用SDK对一个服务发起请求时，SDK会自动根据您在创建SDK
Client时指定的地域ID（Region ID）和产品ID来找到Endpoint。

.. code:: python

   from alibabacloud import get_client

   ecs_client = get_client('ecs', access_key_id=access_key_id,
                           access_key_secret=access_key_secret,
                           region_id='cn-hangzhou', endpoint='ecs-cn-hangzhou.aliyuncs.com')
   response = ecs_client.describe_tags(page_size=100)
   ret = response.get('Tags')
   print(ret)


方式二：get_client接口通过config传递
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``get_client`` 接口 支持用户显式传递 ``ClientConfig`` 对象。

.. code:: python

   from alibabacloud import get_client, ClientConfig

   client_config = ClientConfig(region_id='cn-hangzhou', endpoint='ecs-cn-hangzhou.aliyuncs.com')

   ecs_client = get_client('ecs', access_key_id=access_key_id,
                           access_key_secret=access_key_secret,
                           config=client_config)
   response = ecs_client.describe_tags(page_size=100)
   ret = response.get('Tags')
   print(ret)


环境变量配置
-------------------------------

``Alibaba Cloud Python SDK`` 支持从环境变量读取部分 ``config`` 相关配置

**HTTPS_PROXY**：HTTPS代理

**HTTP_PROXY**：HTTP代理


文件
-------------------------------

在查找配置值时，\ ``Alibaba Cloud Python SDK``\ 还将搜索\ ``~/.alibabacloud/config``\ 文件。您可以设置环境变量\ ``ALIBABA_CLOUD_CONFIG_FILE``\ 值来更改此文件的位置。
此文件是INI格式文件，我们支持多个section配置，但是目前，我们默认只读取default

以下是\ ``~/.alibabacloud/config``\ 支持的所有的配置变量：

-  region_id：要使用的默认地域，参考 `地域与可用区 <https://help.aliyun.com/document_detail/40654.html>`__

-  endpoint：默认的endpoint,即服务请求地址

-  max_retry_times：单个请求的最大重试次数

-  http_port：HTTP代理服务器

-  https_port：HTTPS代理服务器

-  connection_timeout：尝试建立连接时，抛出超时异常的时间，单位为秒。默认5秒

-  read_timeout：尝试从连接读取时抛出超时异常的时间，单位为秒。默认10秒

-  http_proxy：http代理

-  https_proxy：HTTPS代理

-  user_agent：用户自定义的user_gent

**注意：**
目前文件暂不支持开关类接口配置。开关类接口在文件中一经配置，默认为开启

-  enable_retry：是否使用使用重试

-  enable_https：使用HTTPS


默认配置
-------------------------------

``Alibaba Cloud Python SDK``
提供一些默认的配置，保障API请求或者服务的通路。您可以通过上边的方式进行修改。

**max_retry_times**：最大重试次数，默认3次

**enable_retry**：是否重试，默认True 

**enable_https**：是否使用ssl，默认True 

**http_port**:HTTP请求 端口，默认80 

**https_port**：HTTPS请求端口，默认443
