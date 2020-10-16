import os
beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
beep(5)
# found this code on stack overflow, not really sure why it works but is fun!
