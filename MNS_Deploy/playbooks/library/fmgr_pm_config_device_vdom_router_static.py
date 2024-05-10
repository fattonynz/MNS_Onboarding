#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2021 Fortinet, Inc.
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
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_galaxy_version
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_parameter_bypass


def main():
    jrpc_urls = [
        'pm/config/device/{device}/vdom/{vdom}/router/static'
    ]

    perobject_jrpc_urls = [
        'pm/config/device/{device}/vdom/{vdom}/router/static/{static}'
    ]

    url_params = ['device', 'vdom']
    module_primary_key = 'seq-num'
    module_arg_spec = {
        'enable_log': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'proposed_method': {
            'type': 'str',
            'required': False,
            'choices': [
                'set',
                'update',
                'add'
            ]
        },
        'bypass_validation': {
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
        'device': {
            'required': True,
            'type': 'str'
        },
        'state': {
            'type': 'str',
            'required': True,
            'choices': [
                'present',
                'absent'
            ]
        },
        'vdom': {
            'required': True,
            'type': 'str'
        },        
        'pm_config_device_vdom_router_static': {
            'required': False,
            'type': 'dict',
            'revision': {
                '6.0.0': True,
                '6.2.1': True,
                '6.2.3': True,
                '6.2.5': True,
                '6.4.0': True,
                '6.4.2': True,
                '6.4.5': True,
                '7.0.0': True
            },
            'options': {
                "seq-num": {
                    'required': False,
                    'type': 'int'
                },
                "status": {
                    'required': False,
                    'choices': [
                        'enable',
                        'disable'
                    ],
                    'type': 'str'                    
                },
                "dst": {
                    'required': True,
                    'type': 'str'
                },
                "src": {
                    'required': False,
                    'type': 'str'
                },
                "gateway": {
                    'required': True,
                    'type': 'str'
                },                           
                "distance": {
                    'required': False,
                    'type': 'int'
                },
                "weight": {
                    'required': False,
                    'type': 'int'
                },
                "priority": {
                    'required': False,
                    'type': 'int'
                },
                "device": {
                    'required': True,
                    'type': 'str'
                },
                "comment": {
                    'required': False,
                    'type': 'str'
                },
                "blackhole": {
                    'required': False,
                    'choices': [
                        'enable',
                        'disable'
                    ],
                    'type': 'str'                    
                },
                "dynamic-gateway": {
                    'required': False,
                    'choices': [
                        'enable',
                        'disable'
                    ],
                    'type': 'str'                    
                },
                "sdwan": {
                    'required': False,
                    'choices': [
                        'enable',
                        'disable'
                    ],
                    'type': 'str'                    
                },
                "dstaddr": {
                    'required': False,
                    'type': 'str'
                },
                "internet-service": {
                    'required': False,
                    'type': 'int'
                },
                "internet-service-custom": {
                    'required': False,
                    'type': 'str'
                },                
                "link-monitor-exempt": {
                    'required': False,
                    'choices': [
                        'enable',
                        'disable'
                    ],
                    'type': 'str'                    
                },
                "vrf": {
                    'required': False,
                    'type': 'int'
                },
                "bfd": {
                    'required': False,
                    'choices': [
                        'enable',
                        'disable'
                    ],
                    'type': 'str'                    
                }
            }
        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'pm_config_device_vdom_router_static'),
                           supports_check_mode=False)

    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        connection.set_option('enable_log', module.params['enable_log'] if 'enable_log' in module.params else False)
        fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
        fmgr.validate_parameters(params_validation_blob)
        fmgr.process_curd(argument_specs=module_arg_spec)
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()