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
NTest=10
timelist=[]
NODE=sys.argv[1]

for i in range(NTest):
	 time.sleep(3)
	 start=datetime.datetime.utcnow().timestamp()
	 print(start)
	 i=0
	 while(i<int(NODE)):
	 	cmd="python SendMessage.py S &"
	 	result=subprocess.check_output(cmd, shell=True)
	 	print(result)
	 	i+=1
	 time.sleep(3)
	 timelist.append((start))
    
print(timelist)
