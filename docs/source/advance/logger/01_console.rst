生成控制台日志
---------------------

日志文件，我们使用logging模块下的 ``RotatingFileHandler`` , 单文件最大字节为 10M ，备份文件为 5 个。
因此，使用我们默认的日志文件配置，请确保磁盘最低有 60M 可用空间。

client创建控制台日志
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用 ``Alibaba Cloud Python SDK`` 创建的 Client 创建控制台日志

.. code:: python

   from alibabacloud import get_client
   client = get_client('ecs', access_key_id=access_key_id,
                               access_key_secret=access_key_secret,
                               region_id='cn-hangzhou')
   client.add_stream_log_handler()

resource创建控制台日志
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用 ``Alibaba Cloud Python SDK`` 创建的 Resource 创建控制台日志

.. code:: python

   from alibabacloud import get_resource

   ecs_resource = get_resource('ecs', access_key_id=access_key_id,
                               access_key_secret=access_key_secret,
                               region_id='cn-hangzhou', enable_stream_logger=True)

当然，您还可以选择可选配置参数，修改输出日志的格式：
stream\ *log*\ level：Logging level, 比如： ``logging.INFO``
stream\ *log*\ name：日志名字 stream=None,
stream\ *format*\ string：日志信息输出格式
