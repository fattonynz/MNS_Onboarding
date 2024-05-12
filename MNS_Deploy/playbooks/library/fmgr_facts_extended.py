#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2020-2021 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import NAPIManager


def main():
    facts_metadata = {
        'device_interfaces': {
            'params': [
                'device'
            ],
            'urls': [
                'pm/config/device/{device}/global/system/interface',
            ],
            'revision': {
                '6.0.0': True,
                '6.2.1': True,
                '6.2.3': True,
                '6.2.5': True,
                '6.4.0': True,
                '6.4.2': True,
                '6.4.5': True,
                '7.0.0': True
            }            
        },
        'device_static_routes': {
            'params': [
                'device',
                'vdom'
            ],
            'urls': [
                'pm/config/device/{device}/vdom/{vdom}/router/static'
            ],
            'revision': {
                '6.0.0': True,
                '6.2.1': True,
                '6.2.3': True,
                '6.2.5': True,
                '6.4.0': True,
                '6.4.2': True,
                '6.4.5': True,
                '7.0.0': True
            }            
        },
        'device_system_zones': {
            'params': [
                'device',
                'vdom'
            ],
            'urls': [
                'pm/config/device/{device}/vdom/{vdom}/system/zone'
            ],
            'revision': {
                '6.0.0': True,
                '6.2.1': True,
                '6.2.3': True,
                '6.2.5': True,
                '6.4.0': True,
                '6.4.2': True,
                '6.4.5': True,
                '7.0.0': True
            }            
        }        
    }

    module_arg_spec = {
        'enable_log': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'rc_succeeded': {
            'required': False,
            'type': 'list'
        },
        'rc_failed': {
            'required': False,
            'type': 'list'
        },
        'facts': {
            'required': True,
            'type': 'dict',
            'options': {
                'selector': {
                    'required': True,
                    'type': 'str',
                    'choices': [
                        'device_interfaces',
                        'device_static_routes',
                        'device_system_zones'
                    ]
                },
                'params': {
                    'required': False,
                    'type': 'dict'
                },
                'filter': {
                    'required': False,
                    'type': 'list'
                },
                'sortings': {
                    'required': False,
                    'type': 'list'
                },
                'fields': {
                    'required': False,
                    'type': 'list'
                },
                'option': {
                    'required': False,
                    'type': 'list'
                }
            }
        }
    }
    module = AnsibleModule(argument_spec=module_arg_spec,
                           supports_check_mode=False)
    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        connection.set_option('enable_log', module.params['enable_log'] if 'enable_log' in module.params else False)
        fmgr = NAPIManager(None, None, None, None, module, connection)
        fmgr.process_fact(facts_metadata)
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
