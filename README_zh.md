```Alibaba Cloud Python SDK 2.0``` 旨在提供阿里云API的Pythonic，面向对象的接口。现在它仍在开发中，有一些包含ECS、RDS、SLB、RAM、VPC、CDN等功能和资源可用。通过使用它，开发人员可以更便捷的管理其相应资源，并且比当前的aliyun-openapi-python-sdk具有更好的编程体验 。


# 安装
```Alibaba Cloud Python SDK 2.0``` 目前暂没有发布pypi版本，只能通过源代码安装SDK：
```
git clone https://github.com/aliyun/alibabacloud-python-sdk-v2.git
cd alibabacloud-python-sdk-v2
python setup.py install
```


# 配置

在开始使用 `alibabacloud` 之前，您需要设置身份验证凭据。
您可以在控制台中找到您的阿里云账户的凭据，也可以在秘钥管理页面生成新的秘钥。

您可以在默认凭据文件中配置凭据，其位置默认为 `~/.alibabacloud/credentials` 。
```
[default]
access_key_id = YOUR ACCESS KEY ID
access_key_secret = YOUR ACCESS KEY SECRET
```
此外，您还必须配置 `region` ，这是您创建连接时的默认区域。
您可以在配置文件中设置 `region` 。默认情况下，其位置为 `~/.alibabacloud/config` 。
```
[default]
region_id= cn-hangzhou
```
或者，您可以在创建客户端和资源时传递 `region_id` 。

# 快速开始

`alibabacloud` 创建client是基于产品的client。
```python
import alibabacloud
# 创建一个基于ECS产品的client
ecs_client = alibabacloud.client(service_name='Ecs')
```
创建基于产品的客户端后，该产品提供的每一个操作都将能够被直接调用，获取到字典类型的返回结果
```python
result = ecs_client.describe_regions()
print(result.get("RequestId"))
print(result.get("Regions"))  # 获取alibabacloud全球19个region
```
```Alibaba Cloud Python SDK 2.0``` 仍在开发中。如果您有任何建议或发现错误，请 [打开一个Issue](https://github.com/aliyun/alibabacloud-python-sdk-v2/issues/new) 。
