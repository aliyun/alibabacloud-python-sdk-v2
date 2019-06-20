Client 或者Config文件配置
---------------------------

使用Client配置
~~~~~~~~~~~~~~~

:: 

    import alibabacloud

    client = alibabacloud.client(service_name='Ecs',
                                access_key_id=access_key_id,
                                access_key_secret=access_key_secret,
                                region_id="cn-hangzhou")

使用Config文件配置
~~~~~~~~~~~~~~~~~~

`alibabacloud` 还可以从 `~/alibabacloud/.config` 加载凭据。

您可以通过设置 `ALIBABA_CLOUD_CONFIG_FILE` 环境变量来更改此默认位置。

配置文件是INI格式， `配置文件格式 <https://yuque.antfin-inc.com/wb-yxy487231/agm6gg/tob9nt>`_ 。