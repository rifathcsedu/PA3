import csv
import re
import sys
import os
import subprocess
import time
import threading
from subprocess import Popen
NTest=10
timelist=[]
for i in range(NTest):
    time.sleep(3)  
    #start=time.time()
    #print(start)
    cmd="python ReceiveMessage.py S"
    result=subprocess.check_output(cmd, shell=True)
    print(result)
    start=time.time()
    print(start)
    time.sleep(10)
    timelist.append((start))
    
print(timelist)
with open('time.csv', 'a') as csvfile:
    fieldnames = ['Domain']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#    if(flag==0):
#       writer.writeheader()
    writer.writerow({'Domain': timelist})
'''
mini=min(timelist)
maxi=max(timelist)
avg=sum(timelist)*1.0/len(timelist)
print(mini)
print(maxi)
print(avg)
'''
