Config 文件配置
-----------------

`alibabacloud` 可以多种方式管理您发送请求时候的配置。\
一般，我们遵循这样的方法：尝试各种位置，直到找到值。

`alibabacloud` 使用以下源进行配置

    * 创建客户端时候显式传递为config参数
    * 环境变量
    * 在 `~/.alibabacloud/config` 文件
    * 默认配置

创建客户端时候显式传递为config参数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    import alibabacloud

    client = alibabacloud.client(service_name='Ecs',
                                region_id='cn-hangzhou',
                                access_key_id=access_key_id,
                                access_key_secret=access_key_secret)
    client.add_rotating_file_log_handler(path="ecs.log")
    result = client.describe_regions()
    print(result.get("RequestId"))
    print(result.get("Regions"))  # 获取alibabacloud全球19个region

环境变量配置
~~~~~~~~~~~~~~

::

    ALIBABA_CLOUD_ACCESS_KEY_ID：您的阿里云账户访问id

    ALIBABA_CLOUD_ACCESS_KEY_SECRET：您的阿里云账户访问秘钥

    ALIBABA_CLOUD_CONFIG_FILE

    ALIBABA_CLOUD_CREDENTIALS_FILE
    
    ALIBABA_CLOUD_ROLE_NAME


配置文件
~~~~~~~~~~~~
在查找配置值时，alibabacloud还将搜索 `~/.alibabacloud/config` 文件。
您还可以设置 `ALIBABA_CLOUD_CONFIG_FILE` 值来更改此文件的位置
此文件是INI格式文件，我们支持多个section配置，但是目前，我们默认只读取default
以下是 `~/.alibabacloud/config` 支持的所有的配置变量：

* **region_id**：要使用的默认区域
* access_key_id：阿里云账户ID
* access_key_secret：阿里云账户秘钥
* max_retry_times：单个请求的最大重试次数
* endpoint：默认的endpoint
* user_agent：用户自定义的user_gent
* http_port：HTTP代理服务器
* https_port：HTTPS代理服务器
* connection_timeout：尝试建立连接时，抛出超时异常的时间，单位为秒。默认5秒
* read_timeout：尝试从连接读取时抛出超时异常的时间，单位为秒。默认10秒


