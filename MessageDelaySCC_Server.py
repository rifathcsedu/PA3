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
NODE=sys.argv[1]

for i in range(NTest):
	time.sleep(3)
	i=0
	while(i<int(NODE)):
		cmd="python ReceiveMessage.py S"
		result=subprocess.check_output(cmd, shell=True)
		print(result)
		i+=1
	start=datetime.datetime.utcnow().timestamp()
	print(start)
	timelist.append((start))
    
print(timelist)
