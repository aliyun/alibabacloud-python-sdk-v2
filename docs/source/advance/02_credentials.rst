.. _credentials-config:

使用Alibaba Cloud Python SDK 凭证
====================================

``Alibaba Cloud Python SDK``
有两种类型的凭证数据：凭证提供者（\ ``credentials_provider``\ ）和凭证（\ ``credentials``
）。

**凭证提供者（ credentials_provider ）:** ``credentials_ovider``
是您存放凭证相关信息的位置，\ ``Alibaba Cloud Python SDK`` 寻址
``credentials_provider`` 链，获取凭证（ ``credentials`` ）后立即停止。

**凭证（ credentials ）:** ``credentials`` 是 ``client``
发送API请求必须携带的凭证，\ ``Alibaba Cloud``
以此验证您是否是阿里云的合法用户。 凭证包含\ ``access_key_id`` ,
``access_key_secret``\ ，\ ``security_token`` 以及 ``bearer_token``
等3种凭证。

``Alibaba Cloud Python SDK`` 搜索 ``credentials_provider`` 链 的顺序是：

.. toctree::
    :maxdepth: 2

    credentials/01_func
    credentials/02_env
    credentials/03_file
    credentials/04_instance
