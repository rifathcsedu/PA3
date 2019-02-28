import csv
import re
import sys
import os
import subprocess
import time
import threading
from subprocess import Popen
NTest=1

arr=[]
arr2=[]
for i in range(NTest):
    cmd="sudo tshark -i eth0 -w /tmp/test.pcap -F libpcap &" # t-shark tracks all incoming outgoing data transfer
    Popen(cmd, shell=True)
    time.sleep(4)
    cmd="./out/Default/quic_client --host=35.174.174.103 --port=6121 --disable-certificate-verification https://www.example.org/ " # client connecting to server
    a=subprocess.check_output(cmd, shell=True)
    print(a)
    #cmd="./out/Default/quic_client --host=34.238.241.175 --port=6121 --disable-certificate-verification https://www.example.org/ &" # client connecting to server
    #b=subprocess.check_output(cmd, shell=True)
    #cmd="./out/Default/quic_client --host=3.92.181.73 --port=6121 --disable-certificate-verification https://www.example.org/ &" # client connecting to server
    #c=subprocess.check_output(cmd, shell=True)
    #cmd="hyper --h2 GET http://3.90.15.222:8080/ &" # client connecting to server
    #Popen(cmd, shell=True)
    #end=int(round(time.time() * 1000))
    time.sleep(8)
    cmd="sudo killall tshark"
    subprocess.check_output(cmd, shell=True)
    time.sleep(3)
    
    print("Server 1")
    cmd="sudo tshark -r /tmp/test.pcap -Y 'gquic'"# tracing SYN
    result=subprocess.check_output(cmd, shell=True)
    print(result)
    result=result.split()
    #start=float(result[0])
    #end=float(result[len(result)-1])
    #print("SYN")
    #print(result)
    #print(start)
    #print(result[len(result)-1])
    #arr.append(end-start)
    #cmd="sudo rm /tmp/test.pcap"
    #result=subprocess.check_output(cmd, shell=True)
'''
print(arr)
avg=sum(arr)/len(arr)
avg=avg*1000
mini=min(arr)*1000
maxi=max(arr)*1000
print("min time= ",mini)
print("max time= ",maxi)
print("avg time= ",avg)
'''
