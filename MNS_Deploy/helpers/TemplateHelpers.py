## Template Helpers - Allows you to create custom python scripts to be run along with template 

import random
import string
import os,sys

import json
import inspect
import re
import traceback
import time
import ipaddress
from ipaddress import IPv4Address
from ipaddress import IPv4Network
import collections
from collections import *
import collections.abc
class TemplateHelpers:

    def __init__(self,workflow):
        self.workflow=workflow

    
    def templatehelpers_varfile_fmg_add_interface_vlans(self,**args):
      try:
        if "var_default_mdrfmgdict" in self.workflow.site_config_dict:
           self.workflow.site_config_dict['var_default_mdrfmgdict']=""
        task=args['task'] if "task" in args else "Updating Var Files "  
        customer_name=self.workflow.site_config_dict['var_customer_code']        
        key_output_var=self.workflow.find_function("find_key_by_value",{"value":args['var_file']})
        mdrfmg_varfile= OrderedDict(self.workflow.site_config_dict[key_output_var])       
        vlans=args['vlans']
        for vlan in vlans:
           print(vlan)
           
        new_dict={}
        print(new_dict)
        if "save_path" in args:
           self.workflow.find_function("yamltools_save_yaml",{"save_path":args['save_path'],"content":new_dict})
      except:
        self.workflow.add_output_row(task=task,status="Error",details="",key=args['key'])  
        traceback.print_exc()
         

    def templatehelpers_varfile_add_l2vlans(self,**args):  
      try:
        if "var_default_mdrclfdict" in self.workflow.site_config_dict:
           self.workflow.site_config_dict['var_default_mdrclfdict']=""
        task=args['task'] if "task" in args else "Updating Var Files "  
        customer_name=self.workflow.site_config_dict['var_customer_code']        
        key_output_var=self.workflow.find_function("find_key_by_value",{"value":args['var_file']})
        mdrclf_varfile= self.workflow.site_config_dict[key_output_var]
        #print(self.workflow.site_config_dict[key_output_var])
        vlan_info={}
        vlan_id=args['vlanid']
        service_name=args['service_name']
        subnet=args['subnet']
        mask=args['mask']
        data=args['data'] if "data" in args else {}
        vlan_info['name']=f"{customer_name}_{service_name}_{subnet}/{mask}"
        for x,y in data.items():
          vlan_info[x]=y
        mdrclf_varfile['tenants'][customer_name]['l2vlans'][vlan_id]=vlan_info
        self.workflow.add_output_row(task=task,status="OK",details="Updated",key=args['key'])
        self.workflow.site_config_dict[key_output_var]=mdrclf_varfile
        if "save_path" in args:
           self.workflow.find_function("yamltools_save_yaml",{"save_path":args['save_path'],"content":mdrclf_varfile})
      except:
        self.workflow.add_output_row(task=task,status="Error",details="",key=args['key'])  
        traceback.print_exc()
         
        


    def templatehelpers_generate_default_mdrclf(self,**args):
        mdrclf = {
             'tenants': {
                self.workflow.site_config_dict['var_customer_code']: {
                   'mac_vrf_vni_base': 0,
                   'vlan_aware_bundle_number_base': 0,
                   'enable_mlag_ibgp_peering_vrfs': False,
                   'l2vlans': {}
                   }
                   }
                   }
        out_var=args['out_var'] if "out_var" in args else "var_default_mdrclfdict" 
        self.workflow.site_config_dict[out_var]=mdrclf
        