#! /usr/bin/python3

import time
from subprocess import Popen, PIPE


###############################################################################
# Canister hot plug check 
###############################################################################

# print the output including the error output
# when plug off and plug in the canister frequently, the canister number may change.
# so I need to try all the decvice and get their results. 

# Canister Hot Plug 
# Check SES Page 02h  

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
def write_info_file(test_id):
    with open(test_id, 'w') as f:
        for num, content in result.items():
            if 'enclosure' in content:
                f.write(result[num-1])
                f.write(content)
                f.write(('-'*80+'\n'))
    print(test_id)
    file_content = open(test_id).read()
    print(file_content)

###############################################################

test_result =  []
get_information(page='--page=0x02', index='--index=esc,0')
print('Remove Canister A')
time.sleep(2)
get_information(page='--page=0x02', index='--index=esc,0')
print('Insert Canister A')
time.sleep(2)

result = dict(enumerate(test_result))
# print(result)
write_info_file('SES-13-2--SES001001.txt')



###############################################################

# Canister Hot Plug 
# Check SES Page 07h  


test_result =  []
get_information(page='--page=0x07', index='--index=esc,1')
print('Remove Canister B')
time.sleep(5)
get_information(page='--page=0x07', index='--index=esc,1')

result = dict(enumerate(test_result))
# print(result)
write_info_file('SES-13-2--SES001002.txt')


