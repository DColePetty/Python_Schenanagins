# written for windows 10

import time
import subprocess
import random
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
num_spaces = 40
break_char = " "
additional_meow = "\tmeow"
while(num_spaces != 0):
    for i in range(0, len(splits)):
        rng_val = random.randint(0, 20)
        if(rng_val == 20):
            splits[i]  += additional_meow
        print(str(splits[i]))
        splits[i] = break_char + str(splits[i])
    num_spaces -= 1
    time.sleep(0.03)
    subprocess.call(["clear"])
