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
    #start=datetime.datetime.utcnow().timestamp()
    #print(start)
    timeStartLoop=time.time()
    j=0
    while(True):
    	if(j==int(Trans)):
    		break
    	
    	cmd="timeout 2 python ReceiveMessage.py S"
    	
    	result=subprocess.call(cmd, shell=True)
    	print(str(result))
    	if(str(result)=="124"):
    		break
    	#print("hehe")
    	#print(result)
    	cmd="python SendMessage.py 2 &"
    	result=subprocess.check_output(cmd, shell=True)
    	
    	j+=1
    #time.sleep(10)
    #timelist.append((start))
print(j)
print(timelist)
