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


CLIENT_SUPPORT = {
    # product: name version
    'ecs':('EcsClient', ['2014-05-26',]),
    'ram': ('RamClient', ['2015-05-01', ]),
    'rds': ('RdsClient', ['2014-08-15', ]),
    'slb': ('SlbClient', ['2014-05-15', ]),
    'vpc': ('VpcClient', ['2016-04-28', ]),
    'cdn':('CdnClient', ['2014-11-11', '2018-05-10',]),
    'eci':('EciClient', ['2018-08-08',]),
    'edas':('EdasClient', ['2017-08-01',]),
    'linkwan':('LinkWANClient', ['2018-12-30',]),
}
