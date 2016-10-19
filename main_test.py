#! /usr/bin/python

import time
from subprocess import Popen, PIPE
from glob import glob

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

# get the result
def get_information(scsi_cmd, *opt): 
    global test_result
    test_result = []
    for enclosure in enclosure_list: 
        if opt:
            opt_string = ' '.join(list(opt))
            opt_output = '[root@localhost wgz]# %s %s %s\n' % (scsi_cmd, opt_string, enclosure)
            test_result.append(opt_output)
            proc = Popen(['{}'.format(scsi_cmd)]+list(opt), stdout=PIPE, stderr=PIPE)
            output, errors = proc.communicate() 
            test_result.append((output + errors).decode('utf-8'))
            test_result.append(('-' * 80 + '\n'))
        
# write and select the related result info file and output it into the screen
def write_into_file(test_id):
    with open(test_id, 'w') as f:
        for content in test_result:
                f.write(content)
    print(test_id)
    file_content = open(test_id).read()
    print(file_content)

# get the cli result
tool_path =''.join(glob('**/cls_cli_tool', recursive=True))
def cli_cmd(cmd=''):
    for enclosure in enclosure_list: 
        expre = '[root@localhost wgz]# {} -d /dev/sg{} -c {}\n'.format(tool_path, enclosure, cmd)
        test_result.append(expre)
        proc = Popen(['{}'.format(tool_path), '-d', '{}'.format(enclosure), '-c', '{}'.format(cmd)], stdout=PIPE, stderr=PIPE)
        output, errors = proc.communicate() 
        test_result.append((output + errors).decode('utf-8'))
        test_result.append(('-' * 80 + '\n'))
    
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


