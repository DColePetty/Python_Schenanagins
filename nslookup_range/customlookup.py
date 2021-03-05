import os
import subprocess

# PYTHON 3.6 +
# first three octets plus a dot
net = "192.168.0."
hosts = []
# this range here will be the range for the second octet, currently 1-255 (ik)
for i in range(1, 255):
    hosts.append(i)
print(str(hosts)) # prints the fourth octet values to be tried

# todo tranform this this to a method that can be multithreaded
# todo add some pretty default output for resolved and unresolved hosts. 
for i in hosts:
    out1 = subprocess.call(["nslookup", str(net) + str(i)])
    if out1 != 0:
        continue
        #print(str(out1))
    else:
        out = subprocess.check_output(["nslookup", str(net) + str(i)]).decode("utf-8")
        if "** server can't find" in out:
            continue
        else:
            print(str(out))
