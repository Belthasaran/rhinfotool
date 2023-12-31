import os
import json
import random
import sys
import re

import repatch
typenames = {}

listfile = open('hacklist.json', 'r')
hacklist = json.load(listfile)
argvstr =  ' '.join(sys.argv[1:])
selection = []
hackdata = {}

for x in hacklist:
     if re.search(argvstr.lower(), x["name"].lower(), re.I):
         selection = selection + [x["id"]]
         hackdata[ str(x["id"]) ] = x
         continue
     if re.search(argvstr.lower(), x["authors"].lower(), re.I):
         selection = selection + [x["id"]]
         hackdata[ str(x["id"]) ] = x
         continue
     if re.search(argvstr.lower(), x["type"].lower(), re.I):
         selection = selection + [x["id"]]
         hackdata[ str(x["id"]) ] = x
         continue

for u in selection:
    chosen = u
    chosenrecord = hackdata[str(chosen)]
    print(str(chosen)  +  '  -  '  + chosenrecord["name"]   + "  - " + chosenrecord["authors"] +  "  - " + chosenrecord["type"]  + " - "   )
#    print(json.dumps(chosenrecord, indent=4, sort_keys=True))

