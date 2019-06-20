API文档
==========

.. module:: alibabacloud

获取Client
--------------

.. autofunction:: alibabacloud.get_client

获取Resource
---------------
.. autofunction:: alibabacloud.get_resource

Client 基类
-------------------
.. autoclass:: alibabacloud.client.AlibabaCloudClient

Config 类
-------------------
.. autoclass:: alibabacloud.client.ClientConfig

CredentialsProvider
--------------------
.. autoclass:: alibabacloud.credentials.provider.PredefinedChainCredentialsProvider
.. autoclass:: alibabacloud.credentials.provider.EnvCredentialsProvider
.. autoclass:: alibabacloud.credentials.provider.ProfileCredentialsProvider
.. autoclass:: alibabacloud.credentials.provider.InstanceProfileCredentialsProvider

Endpoint解析类
--------------------
.. autoclass:: alibabacloud.endpoint.default_endpoint_resolver.DefaultEndpointResolver