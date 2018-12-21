import json
import os

import alibabacloud


sdk_config_path = os.path.join(os.path.expanduser("~"), "aliyun_sdk_config.json")
with open(sdk_config_path) as fp:
    config = json.loads(fp.read())
    access_key_id = config['access_key_id']
    access_key_secret = config['access_key_secret']
    region_id = config['region_id']

resource = alibabacloud.get_resource('ecs', ak=access_key_id, secret=access_key_secret, region_id=region_id)
# print(resource.instances.all())


# for instance in resource.instances.all():
    # print(instance.instance_id)
    # instance.start()


# ecs_objs = resource.instances.filter('i-bp162a07bhoj5skna4zj')
# print(ecs_objs)
# for item in ecs_objs:
#     item.start()


# request.set_ImageId('coreos_1745_7_0_64_30G_alibase_20180705.vhd')
# request.set_SecurityGroupId('sg-bp12zdiq3r9dqbaaq717')
# request.set_InstanceType('ecs.n2.small')
# request.set_IoOptimized('optimized')
# request.set_SystemDiskCategory('cloud_ssd')

# response = resource.create_instance(
#     ImageId='coreos_1745_7_0_64_30G_alibase_20180705.vhd',InstanceType='ecs.n2.small')
# print(response)

# obj = resource.instances.get('i-bp1bclwh3i4nbzlfsycm')
# obj.stop()
# obj.delete()


# 批量创建instance
# response = resource.run_instances(
#     ImageId='coreos_1745_7_0_64_30G_alibase_20180705.vhd', InstanceType='ecs.n2.small', SecurityGroupId='sg-bp12zdiq3r9dqbaaq717')
# print(response)

objs = resource.instances.limit(1)
print('hi', objs)
# for obj in objs:
    # print(obj.instance_id)
    # obj.stop()

# obj = resource.instances.get('i-bp162a07bhoj5skna4zj')
# # obj.start()
# obj.reactivate(Period=1)


