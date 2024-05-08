from classes.workflow import *
class Run:

    def __init__(self,automation):
        
        self.automation=automation
    
    def run(self,**args):
        self.gather_facts()
        self.init_workbook()
    
    def gather_facts(self):

        ## check template exists
        if "template" in self.automation.site_config_dict:
            pass
        else:
           template=self.automation.site_config_dict['template']
           if "TEMPLATE_SUFFIX" in self.automation.site_config_dict:
             template=template+"_"+self.automation.site_config_dict['TEMPLATE_SUFFIX']
           self.automation.site_config_dict['template']=template
                

    def init_workbook(self,**args):
        self.workflow=Workflow(self.automation.site_config_dict,debug=1,fmg_version=721,useroutput=self.automation.useroutput,outputexcel=self.automation.outputexcel,memory=self.automation.memory)
        self.convert_yaml()
    def convert_yaml(self):
        self.workflow.yaml_convert()
        self.workbook_run()

    def workbook_run(self):
        self.workflow.run()
    

