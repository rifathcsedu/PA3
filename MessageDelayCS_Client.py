import csv
import re
import sys
import os
import subprocess
import time
import threading
from subprocess import Popen
NTest=1
timelist=[]
for i in range(NTest):
    start=time.time()
    print(start)
    cmd="python SendMessage.py"
    Popen(cmd, shell=True)
    time.sleep(10)    
    timelist.append((start))
    
print(timelist)
'''
mini=min(timelist)
maxi=max(timelist)
avg=sum(timelist)*1.0/len(timelist)
print(mini)
print(maxi)
print(avg)
'''