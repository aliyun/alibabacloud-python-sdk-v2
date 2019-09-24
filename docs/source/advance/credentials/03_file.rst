凭证文件配置
----------------

``Alibaba Cloud Python SDK``
凭证文件的默认位置为：\ ``~/.alibabacloud/credentials`` 。
您可以通过环境变量 ``ALIBABA_CLOUD_CREDENTIALS_FILE``
来更改此默认位置。配置文件是 INI 格式。 您可以在配置文件中设置以下 ``type``
的 ``Credentials``


基于 AccessKey 的凭证配置
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AccessKey 可以是主账号或者子账号，为了安全考虑，建议您使用子账号进行
AccessKey 的凭证配置

.. code:: 

   [default]
   type = access_key
   access_key_id = YOUR_ACCESS_KEY_ID
   access_key_secret = YOUR_ACCESS_KEY_SECRET

基于 RAM 子用户的凭证配置
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

创建RAM子账号流程，参照
`准备RAM子账号 <https://help.aliyun.com/knowledge_detail/56143.html>`__

.. code:: 

   [default]
   type = ram_role_arn
   access_key_id = YOUR_ACCESS_KEY_ID
   access_key_secret = YOUR_ACCESS_KEY_SECRET
   role_arn = YOUR_ROLE_ARN
   role_session_name = YOUR_ROLE_SESSION_NAME


基于实例 ECS 实例的凭证配置
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

阿里云 SDK 支持通过实例元数据服务来获取 ECS RAM
角色的授权信息来访问阿里云资源和服务。使用这种方式，您部署在 ECS
上的应用程序，无需在 SDK 上配置授权信息即可访问阿里云API（即不需要配置
AccessKey ）。通过这种方式授权的 SDK ，可以拥有这个 ECS RAM 角色的权限。

.. code:: 

   [default]
   type = ecs_ram_role
   role_name = YOUR_ROLE_NAME

注意：确保 ECS 实例已经配置了 RAM 角色。


基于 BearerToken 的凭证配置
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

BearerToken 当前仅支持 CCC (云呼叫中心)产品的加密，请**慎重使用**

.. code:: 

   [default]
   type = bearer_token
   bearer_token = YOUR BEAR TOKEN

基于 STS Token 的凭证配置
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

参照 `配置STS
Token <https://help.aliyun.com/document_detail/67118.html>`__

.. code:: 

   [default]
   type = sts_token
   type = ram_role_arn
   access_key_id = YOUR_ACCESS_KEY_ID
   access_key_secret = YOUR_ACCESS_KEY_SECRET
   user_name = YOUR_USER_NAME
   role_arn = YOUR_ROLE_ARN
   role_session_name = YOUR_ROLE_SESSION_NAME

您可以配置多个客户端凭证，但是我们目前仅支持读取 section 为 default
的凭证。
