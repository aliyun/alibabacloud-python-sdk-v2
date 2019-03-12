# Copyright 2019 Alibaba Cloud Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tests.base import SDKTestBase


class MockResponseTest(SDKTestBase):

    def test_ecs_disk(self):
        # Create Disk
        ecs = self._get_resource("ecs")
        disk = ecs.create_disk()

        # Attach Disk to an Instance
        # Delete Disk
        disk.delete()

        # Create 2 Disks
        # get 2 disks and check attributes
        pass

    def test_ecs_images(self):
        # create image
        # delete image
        # create 2 images
        # get 2 images and check attributes
        pass

    def test_vpc_eip_address(self):
        # create vpc EIP address
        # associate EIP to an ECS instance
        # unassociate eip address
        # delete eip address
        # create 2 EIP addresses
        # get 2 eip addresses and check attributes
        pass

    def test_slb_load_balancer(self):
        # create 1 load balancer
        # rename load balancers and refresh() and check the name
        # delete load balancer
        # create 2 load balancers
        # get 2 load balancers and check attributes
        pass


