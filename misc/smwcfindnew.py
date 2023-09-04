import os
import sys
import json
import time
from os.path import exists
#4959:31956

fr = open('hacklist.json')
hacklist  = json.load(fr)

untried = []

for x in hacklist :
    if exists("hacks/" + str(x["id"])):
        continue
    if exists("tried/" + str(x["id"])):
        continue
    print('python3 runid.py ' + str(x["id"]))
    os.system('python3 runid.py ' + str(x["id"]))
    time.sleep(5)


#

