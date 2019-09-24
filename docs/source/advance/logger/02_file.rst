生成文件日志
---------------


Client 创建文件日志
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用 ``Alibaba Cloud Python SDK`` 创建的 Client 在当前目录下创建一个名为
``ecs.log`` 的日志文件

.. code:: python

   from alibabacloud import get_client
   client = get_client('ecs', access_key_id=access_key_id,
                               access_key_secret=access_key_secret,
                               region_id='cn-hangzhou')
   ecs_client.add_rotating_file_log_handler(path="ecs.log")


Resource 创建文件日志
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

使用 ``Alibaba Cloud Python SDK`` 创建的 Resource
在当前目录下创建一个名为 ``ecs.log`` 的日志文件

.. code:: python

   from alibabacloud import get_resource

   ecs_resource = get_resource('ecs', access_key_id=access_key_id,
                               access_key_secret=access_key_secret,
                               region_id='cn-hangzhou', enable_file_logger=True,
                               file_logger_path="ecs.log")

当然，您还可以选择可选配置参数，修改输出日志的格式：
file\ *log*\ level：Logging level, 比如： ``logging.INFO``
file\ *log*\ name：日志名称 file\ *logger*\ path：文件日志位置
file\ *maxBytes：文件最大字节数，默认10485760字节
file*\ backupCount：最多保存的文件个数，默认5个文件
file\ *logger*\ format_string：日志信息输出格式
