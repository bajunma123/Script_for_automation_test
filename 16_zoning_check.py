#! /usr/bin/python

import time
from subprocess import Popen, PIPE 
from glob import glob
import os


# get the test result
def get_information(cmd=''):
    expander_list = glob('/dev/bsg/expander*') 
    for expander in expander_list:   
        expre = '[root@localhost wgz] {} {}\n'.format(cmd, expander)
        test_result.append(expre)
        proc = Popen(['{} {}'.format(cmd, expander)], stdout=PIPE, stderr=PIPE, shell=True)
        output, errors = proc.communicate() 
        test_result.append((output + errors).decode('utf-8'))
    return test_result.append(('-' * 80 + '\n'))
    
# get the enclosure device and execute the CLI 'reset 1' command
def reset_cmd():
    dev_list = glob('/dev/sg*')
    encl = []
    for i in dev_list:
        try:
            proc = Popen('sg_ses %s' %i, shell=True, stdout=PIPE, stderr=PIPE)
            output, error = proc.communicate()
            if 'CELESTIC' in output.decode('utf-8'):
                encl.append(i)
        except OSError:
            pass

    for enclosure in encl:
        print(enclosure)
        os.popen("../cls_latest_version/cls_cli_tool -d {} -c 'reset 1'".format(enclosure))
        time.sleep(30)

# commands that need to repeat
def cycle():
    get_information('smp_zone_lock')
    get_information('smp_ena_dis_zoning -e 2')
    get_information('smp_zone_activate')
    get_information('smp_discover_list')
    for i in ['3', '4', '5', '6', '9']:
        get_information('smp_discover -p {}'.format(i))
    get_information('smp_zone_unlock')

# write the test result to file and print them to terminal
def write_into_file(test_id):
    with open(test_id, 'w') as f:
        for content in test_result:
                f.write(content)
                f.write(('-'* 80 + '\n'))
    print(test_id)
    file_content = open(test_id).read()
    print(file_content)

#########################################################################################

test_result = []

get_information('smp_rep_general')
get_information('smp_zone_lock')
get_information('smp_ena_dis_zoning -e 2')
get_information('smp_zone_activate')
get_information('smp_discover_list')
for i in ['3', '4', '5', '6', '9']:
    get_information('smp_discover -p {}'.format(i))
get_information('smp_conf_zone_phy_info -p phyinfo.txt')
time.sleep(5)
get_information('smp_zone_activate')
get_information('smp_ena_dis_zoning -e 1')
get_information('smp_zone_activate')
get_information('smp_zone_unlock')

time.sleep(10)
cycle()

print('reset the canister')
reset_cmd()
cycle()

write_into_file('SES16-2--SES001001.txt')

#########################################################################################

test_result = []

get_information('smp_rep_general')
get_information('smp_zone_lock')
get_information('smp_ena_dis_zoning -e 2')
get_information('smp_zone_activate')
get_information('smp_discover_list')
for i in ['3', '4', '5', '6', '9']:
    get_information('smp_discover -p {}'.format(i))
get_information('smp_conf_zone_phy_info -p phyinfo.txt -S 1')
time.sleep(5)
get_information('smp_zone_activate')
get_information('smp_ena_dis_zoning -e 1')
get_information('smp_zone_activate')
get_information('smp_zone_unlock')

time.sleep(10)
cycle()

print('reset the canister')
reset_cmd()

cycle()

write_into_file('SES16-2--SES001002.txt')

#########################################################################################

test_result = []

get_information('smp_rep_general')
get_information('smp_zone_lock')
get_information('smp_ena_dis_zoning -e 2')
get_information('smp_zone_activate')
get_information('smp_discover_list')
for i in ['3', '4', '5', '6', '9']:
    get_information('smp_discover -p {}'.format(i))
get_information('smp_conf_zone_phy_info -p phyinfo.txt -S 2')
time.sleep(5)
get_information('smp_zone_activate')
get_information('smp_ena_dis_zoning -e 1')
get_information('smp_zone_activate')
get_information('smp_zone_unlock')

time.sleep(10)
cycle()

print('reset the canister')
reset_cmd()
cycle()

write_into_file('SES16-2--SES001003.txt')

#########################################################################################

test_result = []

get_information('smp_rep_general')
get_information('smp_zone_lock')
get_information('smp_ena_dis_zoning -e 2')
get_information('smp_zone_activate')
get_information('smp_discover_list')
for i in ['3', '4', '5', '6', '9']:
    get_information('smp_discover -p {}'.format(i))
get_information('smp_conf_zone_phy_info -p phyinfo.txt -S 3')
time.sleep(5)
get_information('smp_zone_activate')
get_information('smp_ena_dis_zoning -e 1')
get_information('smp_zone_activate')
get_information('smp_zone_unlock')

time.sleep(10)
cycle()

# reset the canister
print('reset the canister')
reset_cmd()
cycle()

write_into_file('SES16-2--SES001004.txt')

