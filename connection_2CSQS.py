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
    cmd="sudo tshark -i eth0 -w /tmp/test.pcap -F libpcap &"
    Popen(cmd, shell=True)
    time.sleep(3)
    cmd="python SendMessage.py &"
    Popen(cmd, shell=True)
    time.sleep(10)
    cmd="sudo killall tshark"
    Popen(cmd, shell=True)
    time.sleep(2)
    cmd="sudo tshark -r /tmp/test.pcap -Y 'tcp.flags == 0x010 && ip.addr==3.82.28.86'" # tracing SYN
    result=subprocess.check_output(cmd, shell=True)
    result=result.split()
    end=result[1]
    print(result)
    cmd="sudo tshark -r /tmp/test.pcap -Y 'tcp.flags == 0x002 && ip.addr==3.82.28.86'" # tracing ACK
    result1=subprocess.check_output(cmd, shell=True)
    result1=result1.split()
    start=result1[1]
    timelist.append((end-start)*1000)

mini=min(timelist)
maxi=max(timelist)
avg=sum(timelist)*1.0/len(timelist)
print(mini)
print(maxi)
print(avg)