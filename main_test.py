#! /usr/bin/python

import time
from subprocess import Popen, PIPE
from glob import glob

def test_function():
    print('this is the main.py for automation test')

device_list = glob('/dev/sg*')
enclosure_list = []

for device in device_list: 
    try:
        result = Popen('sg_ses %s' % device, stdout=PIPE, stderr=PIPE, shell=True)
        output, errors = result.communicate()
        if 'CELESTIC' in output:
            enclosure_list.append(device)
    except OSError:
        pass

## get the result
#    def get_information(sg_ses='sg_ses', page='', index='', set='') 
#        test_result = []
#        for enclosure in enclosure_list: 
#            cmd_output = '[root@localhost wgz]# sg_ses {} {} {} {}\n'.format(page, index, set, enclosure)
#            test_result.append(cmd_output)
#            proc = Popen('sg_ses {} {} {} {}'.format, stdout=PIPE, stderr=PIPE)
#            output, errors = proc.communicate() 
#            test_result.append((output + errors).decode('utf-8'))
#        return test_result.append(('-' * 80 + '\n'))

# get the result
test_result = []
def get_information(sg_ses='sg_ses', **cmd): 
    print('load get_information file')
    for enclosure in enclosure_list: 
        if cmd:
            cmd_string = ' '.join(list(cmd.values()))
            cmd_output = '[root@localhost wgz]# sg_ses %s\n' % cmd_string
            test_result.append(cmd_output)
            proc = Popen(['sg_ses']+list(cmd.values()), stdout=PIPE, stderr=PIPE)
            output, errors = proc.communicate() 
            test_result.append((output + errors).decode('utf-8'))
            return test_result.append(('-' * 80 + '\n'))
        
# write and select the related result info file and output it into the screen
def write_into_file(test_id):
    with open(test_id, 'w') as f:
        for content in test_result:
                f.write(content)
                f.write(('-'* 80 + '\n'))
    print(test_id)
    file_content = open(test_id).read()
    print(file_content)

# get the cli result
def cli_cmd(cmd=''):
    for enclosure in enclosure_list: 
        expre = '[root@localhost wgz]# ../cls_latest_version/cls_cli_tool -d /dev/sg{} -c {}\n'.format(enclosure, cmd)
        test_result.append(expre)
        proc = Popen(['../cls_latest_version/cls_cli_tool', '-d', '/dev/sg{}'.format(enclosure), '-c', '{}'.format(cmd)], stdout=PIPE, stderr=PIPE)
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


