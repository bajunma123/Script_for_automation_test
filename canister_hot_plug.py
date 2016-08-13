#! /usr/bin/python3

import time
from subprocess import *


###############################################################################
# Canister hot plug check 
###############################################################################

# print the output including the error output
# when plug off and plug in the canister frequently, the canister number may change.
# so I need to try all the decvice and get their results. 

# Canister Hot Plug 
# Check SES Page 02h  

def get_information(sg_ses='sg_ses', page=None, index=None):
    for device_number in range(14):
        expre = '[root@localhost wgz]# sg_ses {} {} /dev/sg{}\n'.format(page, index, device_number)
        test_result.append(expre)
        proc = Popen([sg_ses, page, index, '/dev/sg{}'.format(device_number)], stdout=PIPE, stderr=PIPE)
        output, errors = proc.communicate() 
        test_result.append((output+errors).decode('utf-8'))
    return test_result.append(('-' * 80 + '\n'))

print('SES-13-2--SES001001.txt')

test_result =  []

get_information(page='--page=0x02', index='--index=esc,0')

print('Remove Canister A')
time.sleep(5)

get_information(page='--page=0x02', index='--index=esc,0')

print('Insert Canister A')
time.sleep(5)

with open('SES-13-2--SES001001.txt', 'w') as f:
    for content in test_result:
        f.write(content)

# judge and scan the results

file_content = open('SES-13-2--SES001001.txt').read()
print(file_content)


###############################################################

# Canister Hot Plug 
# Check SES Page 02h  

print('SES-13-2--SES001002.txt')

test_result =  []

get_information(page='--page=0x07', index='--index=esc,1')

print('Remove Canister B')
time.sleep(5)

get_information(page='--page=0x07', index='--index=esc,1')

with open('SES-13-2--SES001002.txt', 'w') as f:
    for content in test_result:
        f.write(content)

# judge and scan the results

file_content = open('SES-13-2--SES001002.txt').read()
print(file_content)
