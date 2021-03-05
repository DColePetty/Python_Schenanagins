import os
import subprocess

VERBOSE = False

net = "129.82.250."
hosts = []
for i in range(1, 255):
    hosts.append(i)
print(str(hosts))

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
