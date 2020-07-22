#!/usr/bin/python3.8
import subprocess
from threading import Thread

netId = input("please enter yor net ID")
netMask = input("please enter your Subnet Mask")

### Getting how many bits are netID
count = 0
nMask = netMask.split('.')
for i in nMask:
    if (int(i) == 255):
        count+=1

### Getting network address
netAddress = ''
nId = netId.split('.')
for i in range(0,count):
    netAddress = netAddress + nId[i] + '.'

ips = []
def check_ip(ip_2_check):

    try:
        response = subprocess.check_output(
            ['ping', '-c', '3', ip_2_check],
            stderr=subprocess.STDOUT,  # get all output
            universal_newlines=True  # return string not bytes
            
        )
        ips.append(ip_2_check)
    except subprocess.CalledProcessError:
        response = None

threads = []
x = False
y = False
if (count == 1):
    for a in range(0,256):
        if a == 0:
            x = True
            y = False
        elif a == 255:
            x = False
            y = True
        else:
            x = False
            y = False
        for b in range(0,256):
            if b == 0:
                x = True
                y = False
            elif b == 255:
                x = False
                y = True
            else:
                x = False
                y = False
            for c in range(0,256):
                if (x == False and y == False):
                    threads.append(Thread(target = check_ip, args =(netAddress + str(a) + '.' + str(b) + '.' + str(c),))) # registering threads
if (count == 2):
    for b in range(0,256):
        if b == 0:
            x = True
            y = False
        elif b == 255:
            x = False
            y = True
        else:
            x = False
            y = False
        for c in range(0,256):
            if (x == False and y == False):
                threads.append(Thread(target = check_ip, args =(netAddress + str(b) + '.' + str(c),))) # registering threads

if (count == 3):
    for c in range(1,255):
        threads.append(Thread(target = check_ip, args =(netAddress + str(c),))) # registering threads

    
for thread in threads:   # starting the ping test
    thread.start()

for thread in threads:   # waiting for pings to finish
    thread.join()

print('Finished, These ips are available in Network')
print(ips)
    
