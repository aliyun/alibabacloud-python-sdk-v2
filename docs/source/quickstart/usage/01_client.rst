Client 使用
------------

`alibabacloud` 创建的client是基于产品的。

::

    import alibabacloud
    # 创建一个基于ECS产品的client
    ecs_client = alibabacloud.client(service_name='Ecs')

创建基于产品的客户端后，该产品提供的每一个操作都将能够被直接调用，并获取到字典类型的返回结果

::

    result = ecs_client.describe_regions()
    print(result.get("RequestId"))
    print(result.get("Regions"))  # 获取alibabacloud全球19个region