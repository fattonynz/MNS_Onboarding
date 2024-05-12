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
        '/pm/config/adom/{adom}/pkg/{pkg}/firewall/policy'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/pkg/{pkg}/firewall/policy/{policy}'
    ]

    url_params = ['adom', 'pkg']
    module_primary_key = '_policy_block'  
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
        'state': {
            'type': 'str',
            'required': True,
            'choices': [
                'present',
                'absent'
            ]
        },
        'adom': {
            'required': True,
            'type': 'str'
        },
        'pkg': {
            'required': True,
            'type': 'str'
        },
        'pm_config_adom_pkg_firewall_policy_block': {
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
                '_policy_block': {
                    'required': True,
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
                    'type': 'str'
                }
            }
        },     
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'pm_config_adom_pkg_firewall_policy_block'),
                           supports_check_mode=False)

    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        connection.set_option('enable_log', module.params['enable_log'] if 'enable_log' in module.params else False)
        fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
        if module.params['state'] == 'present':
            fmgr.validate_parameters(params_validation_blob)
            fmgr.process_curd(argument_specs=module_arg_spec)
        else:
            #Deconstructed process_fact function in napi.py
            #get policyide based on polic_block name
            api_params = [{'url': f'/pm/config/adom/{module.params["adom"]}/pkg/{module.params["pkg"]}/firewall/policy'}]
            response = fmgr.conn.send_request('get', api_params)
            try:
                policyid = 0
                policyblock = module.params['pm_config_adom_pkg_firewall_policy_block']['_policy_block']
                for policy in response[1]['data']:
                    if policy['_policy_block'] == policyblock:
                        policyid = policy['policyid']
                        break
                if policyid > 0:
                    # Run standard delete policy via process_curd using policyid
                    fmgr.module_primary_key = 'policyid'
                    module.params['pm_config_adom_pkg_firewall_policy_block']['policyid'] = policyid
                    fmgr.validate_parameters(params_validation_blob)
                    fmgr.process_curd(argument_specs=module_arg_spec)
                else:
                    module.exit_json(myres=f'Could not find policy id for block {policyblock}')
            except Exception as e:
                module.fail_json(msg='Error during delete. Error = ' + str(e))        
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
