import os
import json
import random
import sys
import re
import loadsmwrh

import pb_repatch
typenames = {}

hacklist = loadsmwrh.get_hacklist_data()
argvstr =  ' '.join(sys.argv[1:])
selection = []
hackdata = {}

#print(str(hacklist[0]))

for x in hacklist:
     if not('id' in x):
         continue
     if x["id"] == argvstr:
         selection = selection + [x["id"]]
         hackdata[ str(x["id"]) ] = x
         continue
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
    flag1 = loadsmwrh.has_pnum(chosen)
    if flag1 :
       flag1s = '+'
    else:
       flag1s = '-'
    print(flag1s + ' ' + str(chosen)  +  '  -  '  + chosenrecord["name"]   + "  - " + chosenrecord["authors"] +  "  - " + chosenrecord["type"] + " - " )

#
#for u in selection:
#    data1 = loadsmwrh.get_patch_blob(u)
#    print("Len:" + str(len(data1)))
#    pass
#    print(json.dumps(chosenrecord, indent=4, sort_keys=True))

