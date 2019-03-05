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
    cmd="sudo tshark -i eno1 -w /tmp/test.pcap -F libpcap &"
    Popen(cmd, shell=True)
    time.sleep(3)
    cmd="python SendMessage.py S &"
    Popen(cmd, shell=True)
    time.sleep(10)
    cmd="sudo killall tshark"
    Popen(cmd, shell=True)
    time.sleep(2)
    cmd="sudo tshark -r /tmp/test.pcap -Y 'dns.qry.name == \"queue.amazonaws.com\"' -T fields  -e 'dns.a'" # tracing SYN
    result=subprocess.check_output(cmd, shell=True)
    result=result.split()
    Qadd=""    
    for j in result:
    	if(j!=""):
    		Qadd=j
    		break
    cmd="sudo tshark -r /tmp/test.pcap -Y 'ip.addr=="+Qadd+"' -T fields  -e 'ssl.record.length'" # tracing ACK
    result1=subprocess.check_output(cmd, shell=True)
    result1=result1.split()
    SSLNum=0
    for j in result1:
    	if(j.isdigit()):
    		print(j)
    		SSLNum+=int(j)
    cmd="sudo tshark -r /tmp/test.pcap -Y 'ip.addr=="+Qadd+"' -T fields  -e 'frame.len'" # tracing ACK
    result1=subprocess.check_output(cmd, shell=True)
    result1=result1.split()
    FrmNum=0
    for j in result1:
    	if(j.isdigit()):
    		#print(j)
    		FrmNum+=int(j)
    timelist.append(FrmNum-SSLNum)
print(timelist)
mini=min(timelist)
maxi=max(timelist)
avg=sum(timelist)*1.0/len(timelist)
print(mini)
print(maxi)
print(avg)