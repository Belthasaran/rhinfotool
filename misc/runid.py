import os
import json
from os.path import exists
import sys

runid = sys.argv[1]

os.system('scrapy runspider smwcrandhack.py  -O rand.json -s USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" -a start_url="https://www.smwcentral.net/?p=section&a=details&id="' + runid)


f = open("rand.json", "r")
data = json.load(f)

idx = str(data[0]["id"])
if exists("hacks/" + idx):
   print("Already exist: hacks/"+idx)
   exit(0)

if data[0] and data[0]["name_href"]  :
   try: 
       os.remove("temp/in.zip")
   except:
        pass
   try:
       os.remove("temp/result")
   except:
       pass
   os.system("python3 smwcfetchrand.py")
   os.system("python3 extractpatch.py")

