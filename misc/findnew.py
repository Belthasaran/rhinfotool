#!/usr/bin/python

import os
import json
import smwcprep
import time

oldf = open('smwclist_old.json', 'r')
newf = open('smwclist_new.json', 'r')
nhl = open('smwclist_addlist.txt', 'w')


ohacks = json.loads(oldf.read())
nhacks = json.loads(newf.read())
newlist = []

hackids = {}

for u in ohacks:
    hackids[ u["id"] ] = 1

for hentry in nhacks:
    if not(hentry["id"] in hackids):
         newlist = newlist + [hentry]

#####
for hentry in newlist:
    nhl.write(hentry["id"] + "\n")
    if not(os.path.exists("zips/" + hentry["id"] + ".zip")):
       print(str(hentry["id"]))
       os.system("python3 runid.py " + hentry["id"])
       #smwcprep.fetch_download_function(hentry)
       time.sleep(3) #break
       #print(str(hentry["id"]))
    pass
    f2 = open("hacks/" + hentry["id"], "r")
    hackmeta = json.load(f2)
    f2.close()
    if "patchblob1_name" in hackmeta : 
        print("Hack already mkblob: " + hackmeta["id"])
    else:
        os.system("python3 mkblob.py " + hackmeta["id"])
    #print(str(hackmeta["patchblob1_name"]))
pass
nhl.close()

