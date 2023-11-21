### RUN PYTHON SEO TOOL MULTIPLE TIMES

### PYTHON MODULES
import os

### GLOBALS
MAXCOUNT = 5000 ## 1 - MAXCOUNT


##### EXECUTION LOOP
for i in range(0, MAXCOUNT):
    i += 1
    print("[+] Launching Script %s of %s Times" % (i, MAXCOUNT))
    os.system("python SageChrome.py")
else:
    print("[+] Sage Has Finished it's Rotation")

