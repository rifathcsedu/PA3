import calendar
#import pytz
import csv
import re
import sys
import os
import subprocess
import time
import datetime;
import threading
from subprocess import Popen
NTest=10
timelist=[]
for i in range(NTest):
    #start=time.time()
    #print(start)
    cmd="python ReceiveMessage.py 2"
    result=subprocess.check_output(cmd, shell=True)
    print(result)
    start=datetime.datetime.utcnow().timestamp()
    #start=calendar.timegm(start.utctimetuple())
    print(start)
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
