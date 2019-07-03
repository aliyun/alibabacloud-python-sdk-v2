配置
-------------

在开始使用 `alibabacloud` 之前，您需要设置身份验证凭据。您可以在控制台中找到您的阿里云账户的凭据，也可以在秘钥管理页面生成新的秘钥。

您可以在默认凭据文件中配置凭据，其位置默认为 `~/.alibabacloud/credentials` 。

::

    [default]
    access_key_id = YOUR ACCESS KEY ID
    access_key_secret = YOUR ACCESS KEY SECRET


此外，您还必须配置 `region` ，这是您创建连接时的默认区域。
您可以在配置文件中设置 `region` 。默认情况下，其位置为 `~/.alibabacloud/config` 。

::

    [default]
    region_id= cn-hangzhou

或者，您可以在创建客户端和资源时传递 `region_id` 。


有关配置的深入使用，请参考
