#! /usr/bin/python

import time
from subprocess import Popen, PIPE
import os
from glob import glob

expander_list = glob('/dev/bsg/expander*') 
def get_information(cmd=''):
    for expander in expander_list:   
        expre = '[root@localhost wgz]# {} {}\n'.format(cmd, expander)
        test_result.append(expre)
        proc = Popen(['{}'.format(cmd), '{}'.format(expander)], stdout=PIPE, stderr=PIPE)
        output, errors = proc.communicate() 
        test_result.append((output + errors).decode('utf-8'))
#    return test_result.append(('-' * 80 + '\n'))
    
def write_into_file(test_id):
    with open(test_id, 'w') as f:
        for content in test_result:
                f.write(content)
                f.write(('-'* 80 + '\n'))
    print(test_id)
    file_content = open(test_id).read()
    print(file_content)

test_result = []
command_list = ['smp_rep_general', 'smp_rep_manufacturer', 'smp_read_gpio', 'smp_rep_self_conf_stat', 'smp_rep_zone_perm_tbl', 'smp_rep_zone_man_pass', 'smp_rep_broadcast'
                , 'smp_discover', 'smp_rep_phy_err_log', 'smp_rep_phy_sata', 'smp_rep_route_info', 'smp_rep_phy_event', 'smp_discover_list', 'smp_rep_phy_event_list',
                'smp_rep_exp_route_tbl']
for command in command_list:              
    get_information(command)
write_into_file('SES-5-1.txt')


