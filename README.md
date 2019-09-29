# Alibaba Cloud Python SDK 2.0

[![PyPI Release](https://img.shields.io/pypi/v/alibaba-cloud-python-sdk-v2.svg?style=flat)](https://pypi.org/project/alibaba-cloud-python-sdk-v2)
[![Build Status](https://api.travis-ci.org/aliyun/alibabacloud-python-sdk-v2.svg?branch=master)](https://travis-ci.org/aliyun/alibabacloud-python-sdk-v2)
[![Code Coverage](https://codecov.io/gh/aliyun/alibabacloud-python-sdk-v2/branch/master/graph/badge.svg)](https://codecov.io/gh/aliyun/alibabacloud-python-sdk-v2)

```Alibaba Cloud Python SDK 2.0``` is aimed to provide a Pythonic, object-oriented interface of Alibaba
Cloud APIs. By
using it, developers can make use of Alibaba Cloud APIs to manage resources including instances, 
with a
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

# Create your credentials settings

```Alibaba Cloud Python SDK 2.0``` accepts multiple forms of credentials.
As a quick start, a simple INI file can be placed at ```~/.alibabacloud/credentials.ini```:*

```ini
[default]
type = access_key
access_key_id = YOUR_ACCESS_KEY_ID
access_key_secret = YOUR_ACCESS_KEY_SECRET
```

# Getting started with ECS Instance resource

1, Initialize a ECS resource

```python
import alibabacloud

ecs = alibabacloud.get_resource('ecs', region_id="Your Region ID")
```

*Note: To make it work you need to create a credentials file first at 
```~/.alibabacloud/credentials.ini```, or you can define your credentials like this:*

```python
import alibabacloud

ecs = alibabacloud.get_resource(
    'ecs', 
    region_id="Your Region ID",
    access_key_id="Your Access Key ID",
    access_key_secret="Your Access Key Secret")
```


2, Create an ECS instance, and start, stop it.

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

3, Get all instances attributes

```python
# Assume you already have a ECS resource name 'ecs'
for instance in ecs.instances.all():
    print(instance.instance_id)
    print(instance.instance_type)
    print(instance.status)
```

4, Find all instances which status is running, and let PageNumber of DescribeInstances API to be 
100, and limit results number to 100.
```python
# Assume you already have a ECS resource name 'ecs'
for instance in ecs.instances.filter(Status='Running').page_size(100).limit(200):
    print(instance.instance_id)
    print(instance.instance_type)
    print(instance.status)
```

# More Resources

In ```Alibaba Cloud Python SDK 2.0```, there are a lot resource interfaces available from 
services including ECS, RDS, SLB, VPC, CDN, RAM, etc. Each type of resource has a set of methods 
and users can call APIs via these methods. For example, calling for ```instance.start()``` will emit
an API call of ```StartInstance```. There are 2 level of resource, namely service-level resource and
entity-level resource. You can obtain a service-level resource like this:

```python
import alibabacloud

ecs = alibabacloud.get_resource('ecs')
rds = alibabacloud.get_resource('rds')
slb = alibabacloud.get_resource('slb')
vpc = alibabacloud.get_resource('vpc')
cdn = alibabacloud.get_resource('cdn')
ram = alibabacloud.get_resource('ram')

# Currently you need to specify a region ID.

```

Or an entity-level resource like this:
```python
import alibabacloud
instance = alibabacloud.get_resource('ecs.instance', resource_id='Your Instance ID')

instance.start()
instance.stop()
```

In the above code sample, 'ecs.instance' is the resource name, and you need to provide an 
instance ID for resource id. 

Here is a name list of available entity-level resources:

```
cdn.cdn_domain
cdn.fc_trigger
cdn.user_usage_data_export_task
ecs.access_point
ecs.auto_provisioning_group
ecs.auto_snapshot_policy
ecs.bandwidth_package
ecs.cluster
ecs.command
ecs.dedicated_host
ecs.deployment_set
ecs.disk
ecs.eip_address
ecs.fleet
ecs.ha_vip
ecs.hpc_cluster
ecs.image
ecs.instance
ecs.instance_type
ecs.key_pair
ecs.launch_template
ecs.nat_gateway
ecs.network_interface
ecs.network_interface_permission
ecs.physical_connection
ecs.region
ecs.reserved_instance
ecs.router_interface
ecs.route_table
ecs.security_group
ecs.snapshot
ecs.snapshot_link
ecs.storage_set
ecs.system_event
ecs.task
ecs.virtual_border_router
ecs.vpc
ecs.vrouter
ecs.vswitch
ecs.zone
ens.ens_region
ens.image
ens.instance
ens.instance_type
ram.group
ram.policy
ram.role
ram.user
ram.virtual_mfa_device
rds.account
rds.backup
rds.db
rds.db_instance
rds.diagnostic_report
rds.migrate_task
rds.parameter
rds.region
rds.slow_log
rds.task
rds.temp_db_instance
slb.access_control_list
slb.ca_certificate
slb.domain_extension
slb.load_balancer
slb.master_slave_server_group
slb.master_slave_vserver_group
slb.region
slb.rule
slb.server_certificate
slb.vserver_group
slb.zone
vpc.access_point
vpc.bandwidth_package
vpc.bgp_group
vpc.bgp_peer
vpc.customer_gateway
vpc.eip_address
vpc.express_cloud_connection
vpc.flow_log
vpc.global_acceleration_instance
vpc.ha_vip
vpc.ipv6_address
vpc.ipv6_egress_only_rule
vpc.ipv6_gateway
vpc.ipv6_translator
vpc.ipv6_translator_acl_list
vpc.ipv6_translator_acl_list_entry
vpc.ipv6_translator_entry
vpc.nat_gateway
vpc.network_acl
vpc.physical_connection
vpc.region
vpc.router_interface
vpc.route_table
vpc.ssl_vpn_client_cert
vpc.ssl_vpn_server
vpc.virtual_border_router
vpc.vpc
vpc.vpn_connection
vpc.vpn_gateway
vpc.vpn_pbr_route_entry
vpc.vrouter
vpc.vswitch
vpc.zone
```

# Collections

The Collection is one of the new features in ```Alibaba Cloud Python SDK 2.0```. With collections, 
you can easily iterate resources with filters, and operate each resource coming from collections.

For example, to iterate all ECS instances:
```python
import alibabacloud

ecs = alibabacloud.get_resource('ecs', region_id="Your Region ID")

# ecs.instances is a collection for ECS Instance
# All calls to ecs.instances will translate API calls to DescribeInstances

# Iterate all instances
for instance in ecs.instances.all():
    print(instance.instance_id)
    print(instance.instance_type)
    print(instance.status)
    instance.start()
    instance.stop()
    instance.delete()
    
# Limit instance number to 200:
for instance in ecs.instances.limit(200):
    pass
    
# Filter instances with Status=Stopped. Status is a parameter passing to DescribeInstance API.
for instance in ecs.instances.filter(Status="Stopped"):
    pass
```

All other collections have interfaces including all(), limit(), filter(). Here is a list of all
available collections:

1, ECS collections:
```
ecs.access_points
ecs.auto_provisioning_groups
ecs.bandwidth_packages
ecs.clusters
ecs.commands
ecs.dedicated_hosts
ecs.deployment_sets
ecs.disks
ecs.eip_addresses
ecs.fleets
ecs.ha_vips
ecs.hpc_clusters
ecs.images
ecs.instances
ecs.instance_types
ecs.key_pairs
ecs.launch_templates
ecs.network_interfaces
ecs.network_interface_permissions
ecs.physical_connections
ecs.regions
ecs.reserved_instances
ecs.route_tables
ecs.router_interfaces
ecs.security_groups
ecs.snapshots
ecs.snapshot_links
ecs.storage_sets
ecs.system_events
ecs.tasks
ecs.vrouters
ecs.vswitches
ecs.virtual_border_routers
ecs.vpcs
ecs.zones
```

2, RDS collections
```
rds.db_instances
rds.migrate_tasks
rds.parameters
rds.regions
rds.slow_logs
rds.tasks
rds.accounts
rds.backups
rds.dbs
```

3, SLB collections
```
slb.access_control_lists
slb.ca_certificates
slb.domain_extensions
slb.load_balancers
slb.master_slave_server_groups
slb.master_slave_vserver_groups
slb.regions
slb.rules
slb.server_certificates
slb.vserver_groups
slb.zones
```
4, VPC collections
```
vpc.access_points
vpc.bandwidth_packages
vpc.bgp_groups
vpc.bgp_peers
vpc.eip_addresses
vpc.flow_logs
vpc.global_acceleration_instances
vpc.ha_vips
vpc.ipv6_translators
vpc.ipv6_translator_acl_lists
vpc.ipv6_translator_entries
vpc.ipv6_addresses
vpc.ipv6_egress_only_rules
vpc.network_acls
vpc.physical_connections
vpc.regions
vpc.route_tables
vpc.router_interfaces
vpc.ssl_vpn_client_certs
vpc.ssl_vpn_servers
vpc.vrouters
vpc.vswitches
vpc.virtual_border_routers
vpc.vpcs
vpc.vpn_connections
vpc.vpn_pbr_route_entries
vpc.zones
```
5, CDN collections
```
cdn.fc_triggers
```
6, RAM collections
```
ram.groups
ram.policies
ram.roles
ram.users
```

# Getting Help

```Alibaba Cloud Python SDK 2.0``` is still under development. If you have suggestions or find a 
bug, please [open an issue](https://github.com/aliyun/alibabacloud-python-sdk-v2/issues/new).
