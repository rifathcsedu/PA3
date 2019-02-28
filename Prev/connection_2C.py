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
    cmd="./out/Default/quic_client --host=54.174.77.168 --port=6121 --disable-certificate-verification https://www.bestbuy.com/ &"
    Popen(cmd, shell=True)
    cmd="./out/Default/quic_client --host=34.238.241.175 --port=6121 --disable-certificate-verification https://www.bestbuy.com/ &"
    Popen(cmd, shell=True)
    cmd="./out/Default/quic_client --host=3.92.181.73 --port=6121 --disable-certificate-verification https://www.bestbuy.com/ &"
    Popen(cmd, shell=True)
    time.sleep(10)
    cmd="sudo killall tshark"
    Popen(cmd, shell=True)
    time.sleep(2)
    cmd="sudo tshark -r /tmp/test.pcap -Y 'gquic.tag == \"CHLO\" && ip.addr==54.174.77.168'"
    result=subprocess.check_output(cmd, shell=True)
    #print("CHLO: ")
    #print(result)
    result=result.split()
    start1=float(result[1])
    cmd="sudo tshark -r /tmp/test.pcap -Y 'gquic.tag == \"REJ\" && ip.addr==54.174.77.168'"
    result1=subprocess.check_output(cmd, shell=True)
    #print(result1)
    result1=result1.split()
    end1=float(result1[1])
    #print(start)
    #print(end)
    #print(end-start)
    cmd="sudo tshark -r /tmp/test.pcap -Y 'gquic.tag == \"CHLO\" && ip.addr==34.238.241.175'"
    result=subprocess.check_output(cmd, shell=True)
    #print("CHLO: ")
    #print(result)
    result=result.split()
    start2=float(result[1])
    cmd="sudo tshark -r /tmp/test.pcap -Y 'gquic.tag == \"REJ\" && ip.addr==34.238.241.175'"
    result1=subprocess.check_output(cmd, shell=True)
    #print(result1)
    result1=result1.split()
    end2=float(result1[1])
    cmd="sudo tshark -r /tmp/test.pcap -Y 'gquic.tag == \"CHLO\" && ip.addr==3.92.181.73'"
    result=subprocess.check_output(cmd, shell=True)
    #print("CHLO: ")
    #print(result)
    result=result.split()
    start3=float(result[1])
    cmd="sudo tshark -r /tmp/test.pcap -Y 'gquic.tag == \"REJ\" && ip.addr==3.92.181.73'"
    result1=subprocess.check_output(cmd, shell=True)
    #print(result1)
    result1=result1.split()
    end3=float(result1[1])
    timelist.append((max(end1,end2,end3)-min(start1,start2,start3))*1000)

mini=min(timelist)
maxi=max(timelist)
avg=sum(timelist)*1.0/len(timelist)
print(mini)
print(maxi)
print(avg)
