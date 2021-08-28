import subprocess
import re 
import os 
data = open("/var/log/auth.log", "r")
exp = re.compile("authentication failure")
result = ""  
for line in data:
    if re.search(exp, str(line)):
        result += (str(line))
result_list = result.split("\n")
if (os.path.exists("/home/security/Destop/auth_failures.txt")):
    for line in open("/home/security/Destop/auth_failures.txt", 'r'):
        result_list.append(str(line))
after_sort = result_list.sort()
after_sort = list(set(result_list))
after_uniq = "\n".join(result_list)
print(after_uniq)
output_file = open("/home/security/Desktop/auth_failures.txt", 'w+')
for i in after_uniq.split("\n"):
    output_file.write(str(i) + "\n")
