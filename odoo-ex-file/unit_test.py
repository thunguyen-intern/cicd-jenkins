import os, ast
import sys
# from test_base_utils.__manifest__ import manifest

class CodeGenerator:
    def __init__(self):
        # self.src = "test_base_utils/tests/test_utils.py"
        self.dest = "test_utils.sh"
        self.bin_path = "/opt/odoo/odoo-bin"
        self.conf_path = "/etc/odoo.conf"
        self.mod_path = "modules.txt"
    
    def check_path(self, fpath):
        return os.path.isfile(fpath)
    
    def run(self):
        f = open(self.dest, "w")
        code = self.genCode()
        f.write(code)
        f.close()

    # def find_tagged(self, fpath):
    #     with open(fpath, "r") as f:
    #         for line in f:
    #             stripped_line = line.strip()
    #             if stripped_line.startswith('@tagged'):
    #                 args_line = stripped_line.replace('@tagged', '').strip()
    #                 args_list = ast.literal_eval(args_line)
    #                 return args_list
    
    def check_module(self, fpath):
        with open(fpath, "r") as f:
            return [modules.strip() for modules in f]

    def genCode(self):
        modules_list = self.check_module(self.mod_path)
        code = "#!/bin/bash \n \n" + self.bin_path + " -c " + self.conf_path
        # First argument from input: database name
        code += " -d " + "abc"
        # Modules
        if len(modules_list) > 0:
            code += " -i "
            code += ','.join(modules_list)

        code += " --stop-after-init"
        return code
    
if __name__ == "__main__":
    code = CodeGenerator()
    code.run()
