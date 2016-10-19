#! /usr/bin/python3

import time
from subprocess import Popen, PIPE

# get the result
def get_information(sg_ses='sg_ses', page=None, index=None):
    for device_number in range(14):
        expre = '[root@localhost wgz]# sg_ses {} {} /dev/sg{}\n'.format(page, index, device_number)
        test_result.append(expre)
        proc = Popen([sg_ses, page, index, '/dev/sg{}'.format(device_number)], stdout=PIPE, stderr=PIPE)
        output, errors = proc.communicate() 
        test_result.append((output + errors).decode('utf-8'))
    return test_result.append(('-' * 80 + '\n'))

# write and select the related result info file and output it into the screen
def write_into_file(test_id):
    with open(test_id, 'w') as f:
        for num, content in result.items():
            if 'CELESTIC' in content:
                f.write(result[num-1])
                f.write(content)
                f.write(('-'* 80 + '\n'))
    print(test_id)
    file_content = open(test_id).read()
    print(file_content)

# get the cli result
def cli_cmd(cmd=None):
    for device_number in range(14):
        expre = '[root@localhost wgz]# ../cls_latest_version/cls_cli_tool -d /dev/sg{} -c {}'.format(device_numver, cmd)
        test_result.append(expre)
        proc = Popen(['../cls_latest_version/cls_cli_tool', '-d', '/dev/sg{}'.format(device_number), '-c', {}.format(cmd)], stdout=PIPE, stderr=PIPE)
        output, errors = proc.communicate() 
        test_result.append((output + errors).decode('utf-8'))
    return test_result.append(('-' * 80 + '\n'))
    
# write and select the related cli result info file and output it into the screen
def write_cli_into_file(test_id):
    with open(test_id, 'w') as f:
        for num, content in result.items():
            if 'cli_cmd' in content:
                f.write(result[num-1])
                f.write(content)
                f.write(('-'*80+'\n'))
    print(test_id)
    file_content = open(test_id).read()
    print(file_content)


###############################################################################
# Canister hot plug check 
###############################################################################

# Canister Hot Plug 
# Check SES Page 02h  

test_result =  []
get_information(page='--page=0x02', index='--index=esc,0')
print('Remove Canister A')
time.sleep(30)
get_information(page='--page=0x02', index='--index=esc,0')
print('Insert Canister A')
time.sleep(30)
get_information(page='--page=0x02', index='--index=esc,1')
print('Remove Canister B')
time.sleep(30)
get_information(page='--page=0x02', index='--index=esc,1')
print('Insert Canister B')
time.sleep(30)

result = dict(enumerate(test_result))
# print(result)
write_into_file('SES-13-2--SES001001.txt')


###############################################################

# Canister Hot Plug 
# Check SES Page 07h  

test_result =  []
get_information(page='--page=0x07', index='--index=esc,0')
print('Remove Canister A')
time.sleep(30)
get_information(page='--page=0x07', index='--index=esc,0')
print('Insert Canister A')
time.sleep(30)
get_information(page='--page=0x07', index='--index=esc,1')
print('Remove Canister B')
time.sleep(30)
get_information(page='--page=0x07', index='--index=esc,1')
print('Insert Canister B')
time.sleep(30)

result = dict(enumerate(test_result))
# print(result)
write_into_file('SES-13-2--SES001002.txt')


###############################################################

# Canister Hot Plug 
# Check SES Page 0ah  

test_result =  []
get_information(page='--page=0x0a', index='--index=esc,0')
print('Remove Canister A')
time.sleep(30)
get_information(page='--page=0x0a', index='--index=esc,0')
print('Insert Canister A')
time.sleep(30)
get_information(page='--page=0x0a', index='--index=esc,1')
print('Remove Canister B')
time.sleep(30)
get_information(page='--page=0x0a', index='--index=esc,1')
print('Insert Canister B')
time.sleep(30)

result = dict(enumerate(test_result))
# print(result)
write_into_file('SES-13-2--SES001003.txt')


###############################################################

# Canister Hot Plug 
# CLI Check 

test_result =  []
cli_cmd(cmd='fru get')
cli_cmd(cmd='port get')
print('Remove Canister A')
time.sleep(30)
cli_cmd(cmd='fru get')
cli_cmd(cmd='port get')
print('Insert Canister A')
time.sleep(30)
cli_cmd(cmd='fru get')
cli_cmd(cmd='port get')
print('Remove Canister B')
time.sleep(30)
cli_cmd(cmd='fru get')
cli_cmd(cmd='port get')
print('Insert Canister B')
time.sleep(30)

result = dict(enumerate(test_result))
# print(result)
write_cli_into_file('SES-13-2--SES001004.txt')


###############################################################

# Canister Hot Plug 
# LED Check 

test_result =  []
cli_cmd(cmd='led get')
print('Remove Canister A')
time.sleep(30)
cli_cmd(cmd='led get')
print('Insert Canister A')
time.sleep(30)
cli_cmd(cmd='led get')
print('Remove Canister B')
time.sleep(30)
cli_cmd(cmd='led get')
print('Insert Canister B')
time.sleep(30)

result = dict(enumerate(test_result))
# print(result)
write_cli_into_file('SES-13-2--SES001005.txt')


###############################################################

# Canister Hot Plug 
# LED Check 

test_result =  []
cli_cmd(cmd='log clear')
print('Remove Canister A')
time.sleep(30)
cli_cmd(cmd='log get')
print('Insert Canister A')
time.sleep(30)
cli_cmd(cmd='log get')
print('Remove Canister B')
time.sleep(30)
cli_cmd(cmd='log get')
print('Insert Canister B')
time.sleep(30)

result = dict(enumerate(test_result))
# print(result)
write_cli_into_file('SES-13-2--SES001006.txt')

