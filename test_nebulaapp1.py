#! /usr/bin/env python3

import time

from subprocess import Popen, PIPE

class Nebulaapp:
    def __init__(self):
        self.time = time.strftime('%Y%m%d-%H:%M')

    def execute_command(self):
        cmdline = self.get_command()
        proc = Popen(cmdline, stdout=PIPE, stderr=PIPE)
        output, error = proc.commucate()
        output = (output+error).decode('utf-8')
        return output

    def get_command(self, command_name, *opt):
        cmdline = [command_name] + list(opt)
        return comdline

    def command_log(self, command_name, log_name):
        outputdir = command_name + '_log'
        os.mkdir(outputdir)
        log_name = log_name + '-' + self.time
        log_file = os.path.join(outputdir, logname)
        with open(log_file, 'w') as f:
            command_output = self.execute_command()
            f.write(command_output)
            f.wirte('\n')

    def find_expander(self):
        expander_list = glob.glob('/dev/pmc*')
        return expander_list
