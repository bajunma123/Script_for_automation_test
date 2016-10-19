#! /usr/bin/python3

from subprocess import *

# print the output including the error output
# when plug off and plug in the canister frequently, the canister number may change.
# so I need to try all the decvice and get their results. 

# get the results
we = []
for i in range(6):
    proc = Popen(['sg_ses', '/dev/sg{}'.format(i)], stdout=PIPE, stderr=PIPE)
    output, errs = proc.communicate()
    we.append((output+errs).decode('utf-8'))

# write the results into file
with open('222222.txt', 'w') as f:
    for m in we:
        f.write('[root]wer\n')
        f.write(m)
        
# print the results to the screen 
file_content = open('222222.txt', 'r').read()
print(file_content)
