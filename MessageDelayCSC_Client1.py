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
for i in range(NTest):
    start=datetime.datetime.utcnow().timestamp()
    #start=calendar.timegm(start.utctimetuple())
    print(start)
    cmd="python SendMessage.py S"
    result=subprocess.check_output(cmd, shell=True)
    print(result)
    time.sleep(10)
    timelist.append((start))
    
print(timelist)
