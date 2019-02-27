# Alibaba Cloud Python SDK 2.0

[![PyPI Release](https://img.shields.io/pypi/v/alibaba-cloud-python-sdk-v2.svg?style=flat)](https://pypi.org/project/alibaba-cloud-python-sdk-v2)
[![Build Status](https://api.travis-ci.org/aliyun/alibabacloud-python-sdk-v2.svg?branch=master)](https://travis-ci.org/aliyun/alibabacloud-python-sdk-v2)
[![Code Coverage](https://codecov.io/gh/aliyun/alibabacloud-python-sdk-v2/branch/master/graph/badge.svg)](https://codecov.io/gh/aliyun/alibabacloud-python-sdk-v2)

Alibaba Cloud Python SDK 2.0 is aimed to provide a Pythonic, object-oriented interface of Alibaba
Cloud APIs. Now it's still under development, with a few ECS functions and resources available. By
using it, developers can make use of ECS APIs to manage resources including instances, with a
much better programming experience than the current
[aliyun-openapi-python-sdk](https://github.com/aliyun/aliyun-openapi-python-sdk).


# Installation

Install the SDK from PYPI:
```bash
pip install alibaba-cloud-python-sdk-v2
```

If you prefer installing the SDK from source:

```bash
git clone git://github.com/aliyun/alibabacloud-python-sdk-v2.git
cd alibabacloud-python-sdk-v2
python setup.py install
```

# Usage

1. Initialize a ECS resource

```python
import alibabacloud

ecs = alibabacloud.get_resource(
    'ecs',
    access_key_id="your Access Key ID",
    access_key_secret="your Access Key Secret",
    region_id="your Region ID",
)
```

*Note: Credentials information will be moved to configuration files in the future versions.*

2. Create an ECS instance, and start, stop it.

```python
from alibabacloud.services.ecs import ECSInstanceResource

# Assume you already have a ECS resource name 'ecs'

instance = ecs.create_instance(
    ImageId="coreos_1745_7_0_64_30G_alibase_20180705.vhd",
    InstanceType="ecs.n2.small",
)

print(instance.instance_id)

instance.start()
instance.wait_until(ECSInstanceResource.STATUS_RUNNING)

instance.stop()
instance.wait_until(ECSInstanceResource.STATUS_STOPPED)
```

3. Get all instances attributes

```python
# Assume you already have a ECS resource name 'ecs'
for instance in ecs.instances.all():
    print(instance.instance_id)
    print(instance.instance_type)
    print(instance.status)
```

4. Find all instances which status is running, and let PageNumber of DescribeInstances API to be 
100, and limit results number to 100.
```python
# Assume you already have a ECS resource name 'ecs'
for instance in ecs.instances.filter(Status='Running').page_size(100).limit(200):
    print(instance.instance_id)
    print(instance.instance_type)
    print(instance.status)
```

# Getting Help

```Alibaba Cloud Python SDK 2.0``` is still under development. If you have suggestions or find a 
bug, please [open an issue](https://github.com/aliyun/alibabacloud-python-sdk-v2/issues/new).
