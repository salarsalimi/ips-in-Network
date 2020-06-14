#!/usr/bin/python3.8
import subprocess
from threading import Thread

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
for i in range(1,255):
    threads.append(Thread(target = check_ip, args =('192.168.1.'+str(i),))) # registering threads

for thread in threads:   # starting the ping test
    thread.start()

for thread in threads:   # waiting for pings to finish
    thread.join()

print('Finished, These ips are available in Network')
print(ips)
    
