import csv
import re
import sys
import os
import subprocess
import time
import threading
from subprocess import Popen
NTest=30
timelist=[]
for i in range(NTest):
    time.sleep(2)
    start=int(round(time.time() * 1000))
    cmd="./out/Default/quic_client --host=54.174.77.168 --port=6121 --disable-certificate-verification https://www.example.org/"
    result=subprocess.check_output(cmd, shell=True)
    #cmd="./out/Default/quic_client --host=34.238.241.175 --port=6121 --disable-certificate-verification https://www.bestbuy.com/"
    #Popen(cmd, shell=True)
    end=int(round(time.time() * 1000))
    timelist.append((end-start))
mini=min(timelist)
maxi=max(timelist)
avg=sum(timelist)*1.0/len(timelist)
print(mini)
print(maxi)
print(avg)
