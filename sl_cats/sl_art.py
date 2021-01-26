# written for windows 10

import time
import subprocess
cat = '''
 ,_     _
 |\\\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'   meow
 \  _T_/-._( (
 /         `. \\
|         _  \ |
 \ \ ,  /      |                    meow
  || |-_\__   /
 ((_/`(____,-'

'''
cat_url = "https://www.asciiart.eu/animals/cats"

# moving code
splits = cat.split("\n")
num_spaces = 30
break_char = " "
while(num_spaces != 0):
    for i in range(0, len(splits)):
        print(str(splits[i]))
        splits[i] = break_char + str(splits[i])
    num_spaces -= 1
    time.sleep(0.033)
    subprocess.call(["cl.bat"])
