#import pytz
import calendar
import csv
import re
import sys
import os
import subprocess
import time
import threading
from subprocess import Popen
import datetime
NTest=1
timelist=[]
Trans=sys.argv[1]
for i in range(NTest):
    start=datetime.datetime.utcnow().timestamp()
    print(start)
    timeStartLoop=time.time()
    j=0
    while(True):
    	if(timeStartLoop+1<time.time() || j==int(Trans)):
    		break
    	cmd="python SendMessage.py S &"
    	result=subprocess.check_output(cmd, shell=True)
    	print(result)
    	j+=1
    time.sleep(10)
    timelist.append((start))
    
print(timelist)
