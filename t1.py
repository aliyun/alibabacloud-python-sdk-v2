import os

import alibabacloud

with open(os.path.join(os.path.expanduser("~"), "aliyun_sdk_config.json")) as fp:
    res = fp.read()

print(res)

ecs = alibabacloud.get_resource("ecs")
for event in ecs.system_events.all():
    print(event.event_id)

image_id = "coreos_1745_7_0_64_30G_alibase_20180705.vhd"
instance_type = "ecs.n4.large"
# classics_instance = ecs.create_instance(ImageId=image_id,
#                                         InstanceType=instance_type,
#                                         InnerIpAddress="10.0.0.0")
# print(classics_instance)
for item in ecs.instances.all():
    print(item.instance_id)
    print(item.inner_ip_address)


