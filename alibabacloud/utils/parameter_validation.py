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
import six
from alibabacloud.exceptions import ParamValidationException

MetaParams = namedtuple('MetaParams', 'sname, stype, ctype, cparams')


def verify_params(params, shape):
    validator = ParamValidator()
    report = validator.validate(params, shape)
    if report.has_errors():
        raise ParamValidationException(report=report.generate_report())


def type_check(valid_types):
    def _create_type_check_guard(func):
        def _on_passes_type_check(self, param, shape, errors, name):
            if _type_check(param, errors, name):
                return func(self, param, shape, errors, name)

        def _type_check(param, errors, name):
            if not isinstance(param, valid_types):
                valid_type_names = [six.text_type(t) for t in valid_types]
                errors.report(name, 'invalid type', param=param,
                              valid_types=valid_type_names)
                return False
            return True

        return _on_passes_type_check

    return _create_type_check_guard


class ValidationErrors(object):
    def __init__(self):
        self._errors = []

    def has_errors(self):
        if self._errors:
            return True
        return False

    def generate_report(self):
        error_messages = []
        for error in self._errors:
            error_messages.append(self._format_error(error))
        return '\n'.join(error_messages)

    def _format_error(self, error):
        error_type, name, additional = error
        name = self._get_name(name)
        if error_type == 'missing required field':
            return 'Missing required parameter in %s: "%s"' % (
                name, additional['required_name'])
        elif error_type == 'unknown field':
            return 'Unknown parameter in %s: "%s", must be one of: %s' % (
                name, additional['unknown_param'],
                ', '.join(additional['valid_names']))
        elif error_type == 'invalid type':
            return 'Invalid type for parameter %s, value: %s, type: %s, ' \
                   'valid types: %s' % (name, additional['param'],
                                        str(type(additional['param'])),
                                        ', '.join(additional['valid_types']))
        elif error_type == 'invalid range':
            min_allowed = additional['valid_range'][0]
            max_allowed = additional['valid_range'][1]
            return ('Invalid range for parameter %s, value: %s, valid range: '
                    '%s-%s' % (name, additional['param'],
                               min_allowed, max_allowed))
        elif error_type == 'invalid length':
            min_allowed = additional['valid_range'][0]
            max_allowed = additional['valid_range'][1]
            return ('Invalid length for parameter %s, value: %s, valid range: '
                    '%s-%s' % (name, additional['param'],
                               min_allowed, max_allowed))
        elif error_type == 'unable to encode to json':
            return 'Invalid parameter %s must be json serializable: %s' \
                   % (name, additional['type_error'])

    def _get_name(self, name):
        if not name:
            return 'input'
        elif name.startswith('.'):
            return name[1:]
        else:
            return name

    def report(self, name, reason, **kwargs):
        self._errors.append((reason, name, kwargs))


class ParamValidator(object):

    def validate(self, api_params, repeat_info):
        errors = ValidationErrors()
        for name, value in repeat_info.items():
            actual_param = api_params.get(name)
            if actual_param is not None:
                meta_params = MetaParams._make(list(value))
                self._validate_list(actual_param, meta_params, errors, name=meta_params.sname)
        return errors

    @type_check(valid_types=(list,))
    def _validate_list(self, param, shape, errors, name):
        """
        :param param: [{'Port': {'Protocol': 'https', 'Port': '80'}}]
        :param shape:
        :param errors:
        :param name:
        :return:
        """
        member_shape = shape.cparams
        for i, item in enumerate(param):
            if member_shape is not None:
                self._validate_dict(item, member_shape, errors,
                                    '.'.join([name, str(i), shape.sname]))

    @type_check(valid_types=(dict,))
    def _validate_dict(self, param, shape, errors, name):
        """
        :param param: {'Port': {'Protocol': 'https', 'Port': '80'}}
        :param shape:
                   ('Port', 'list', 'dict', [('Protocol', 'str', None, None),
                                     ('Port', 'str', None, None),],),
        :param errors:
        :param name:
        :return:
        """
        for item in shape:
            meta_params = MetaParams._make(list(item))
            if meta_params.stype == 'list':
                if param.get(meta_params.sname) is not None:
                    self._validate_list(param.get(meta_params.sname), meta_params, errors,
                                        '.'.join([name, meta_params.sname]))
