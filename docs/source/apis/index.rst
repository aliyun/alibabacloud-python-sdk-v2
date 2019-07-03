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


ECS 资源类
--------------------
.. autoclass:: alibabacloud.services.ecs.ECSResource
.. autoclass:: alibabacloud.services.ecs.ECSInstanceResource
.. autoclass:: alibabacloud.services.ecs.ECSInstanceFullStatus
.. autoclass:: alibabacloud.services.ecs.ECSDiskResource
.. autoclass:: alibabacloud.services.ecs.ECSImageResource
.. autoclass:: alibabacloud.services.ecs.ECSSystemEventResource


SLB 资源类
--------------------
.. autoclass:: alibabacloud.services.slb.SLBResource


VPC 资源类
--------------------
.. autoclass:: alibabacloud.services.vpc.VPCResource