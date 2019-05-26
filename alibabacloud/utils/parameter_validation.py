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
# See the License for the specific hierarchiclanguage governing permissions and
# limitations under the License.
from collections import namedtuple

from alibabacloud.exceptions import ParamTypeInvalidException, MaximumRecursionException

MetaParams = namedtuple('MetaParams', 'sname, stype, ctype, cparams')

DEPTH = 0


def verify_hierarchic(cparams, aparams):
    """
    :param cparams:list
    :param aparams:dict
    :return:
    """
    global DEPTH
    DEPTH += 1
    if DEPTH >= 5:
        raise MaximumRecursionException()
    for item in cparams:
        meta_params = MetaParams._make(list(item))
        if meta_params.stype == list:
            if aparams.get(meta_params.sname) is not None:
                if not isinstance(aparams.get(meta_params.sname), meta_params.stype):
                    raise ParamTypeInvalidException(param=meta_params.sname,
                                                    param_type='list')
                if meta_params.ctype == dict:
                    for sub_item in aparams.get(meta_params.sname):
                        if not isinstance(sub_item, dict):
                            raise ParamTypeInvalidException(param=sub_item,
                                                            param_type='dict')
                        verify_hierarchic(meta_params.cparams, sub_item)


def verify_params(api_params, repeat_info):
    """
    api_params
    repeat_info = {'Tag': ('Tag', list, str, None,), }
    repeat_info = {'Tag': ('Tag', list, dict, [
                        ('Key', str, None, None),
                        ('Value', str, None, None),],), }
    """
    global DEPTH
    DEPTH = 0
    for name, value in repeat_info.items():
        formal_param = value
        actual_param = api_params.get(name)
        if actual_param is not None:
            meta_params = MetaParams._make(list(formal_param))
            if not isinstance(actual_param, list):
                raise ParamTypeInvalidException(param=meta_params.sname,
                                                param_type='list')

            if meta_params.ctype == dict:
                for item in actual_param:
                    if not isinstance(item, meta_params.ctype):
                        raise ParamTypeInvalidException(param=item,
                                                        param_type='dict')
                    verify_hierarchic(meta_params.cparams, item)
