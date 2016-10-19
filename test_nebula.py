#! /usr/bin/env python


from subprocess import Popen, PIPE
from functools import partial


class Nebulaapp:
    def __init__(self):
        self.i = 0

    def __call__(self):
        self.i += 1
        return self.i

    def execute_cmd(self, subcmd, *opt):
        cmdline = ['nebulaapp'] + [subcmd] + ' '.join(opt).split()
        #print(cmdline)
        proc = Popen(cmdline, stdout=PIPE, stderr=PIPE)
        output, error = proc.communicate()
        #return (output+error).decode('utf-8') # for python 3
        return (output+error), cmdline

    def proc_logfilename(self, subcmd):
        pass

    def log_file(self, subcmd, *opt):
        i = self.__call__()
        content, cmdline= self.execute_cmd(subcmd, *opt)
        #print(content)
        filename = subcmd + '_%.2d.log' % i
        with open(filename, 'w') as f:
            f.write('root@diag-PowerEdge-R720:~# '+' '.join(cmdline))
            f.write('\n%s' % content)

        file_content = open(filename).read()
        print(file_content)



if __name__ == '__main__':
    link_status = Nebulaapp()
    #link_status.log_file('lnksta', '-a')

################################################################################     
# p2pbinding
################################################################################     
    p2p = Nebulaapp()
    p2p_cmd_list = partial(p2p.log_file, 'p2p', '/dev/pmc_psx')
    cmd_list = ['--partitioninfo --partition=0',
                '--bind --port=0 --partition=1',
                '--unbind --port=0',
                '--portinfo --port=0',
               ]
    for cmd in cmd_list:
        p2p_cmd_list(cmd)
                           
