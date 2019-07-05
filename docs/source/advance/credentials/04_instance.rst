.. _instance-credentials:

实例凭证配置
--------------

使用实例凭证，该实例必须是\ **专有网络**\ 下配置了\ **RAMRole**\ 的ECS实例，配置方式参照：\ `使用
RAM 对云服务器 ECS
进行权限管理 <https://help.aliyun.com/knowledge_detail/58900.html>`__

在该实例的环境变量配置 ``ALIBABA_CLOUD_ROLE_NAME``
,即可通过该实例实现无AK访问阿里云的资源和服务。

环境变量配置以 Linux 为例：

.. code:: 

   export ALIBABA_CLOUD_ROLE_NAME= YourRamRoleName
