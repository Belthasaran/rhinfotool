from zipfile import ZipFile
import re
import hashlib
import base64
import os
import json
import sys

def extract_function(args):    
    filename = "temp/in.zip"
    
    fr = open('rand.json')
    hackinfo = json.load(fr)
    
      
    with ZipFile(filename, 'r') as zip:
        found = False
        for info in zip.infolist():
            if re.match('Espa', info.filename) :
                continue
            if re.match('.*\.bps', info.filename) :
                print(info.filename)
                data = zip.read(info)
                shake1 = (base64.b64encode(hashlib.shake_128(data).digest(24), b"_-")).decode('latin1')
                sha1 = (hashlib.sha1(data).hexdigest())
                xsha224 = hashlib.sha224(data).hexdigest()
    
                f1 = open("temp/" + xsha224 + ".new" , "wb")
                f1.write(data)
                f1.close()
                os.rename("temp/" + xsha224 + ".new", "patch/" + shake1)
                hackinfo[0]["patch"] = "patch/" + shake1
                os.system("./flips --apply patch/" + shake1 +"  smw.sfc temp/result")
                #data = bytearray()
                #with open("temp/result", "rb") as patched:
                #    data += patched.read(1)
                data = open("temp/result", "rb").read()
    
                shake1_patched = (base64.b64encode(hashlib.shake_128(data).digest(24), b"_-")).decode('latin1')
                sha1_patched = (hashlib.sha1(data).hexdigest())
                xsha224_patched = hashlib.sha224(data).hexdigest()
    
                f0 = open("rom/" + shake1_patched + ".new", "wb")
                f0.write(data)
                f0.close()
                os.rename("rom/" + shake1_patched + ".new", "rom/" + shake1_patched)
    
                hackinfo[0]["pat_sha224"] = xsha224
                hackinfo[0]["pat_sha1"] = sha1
                hackinfo[0]["pat_shake_128"] = shake1
                hackinfo[0]["result_sha224"] = xsha224_patched
                hackinfo[0]["result_sha1"] = sha1_patched
                hackinfo[0]["result_shake1"] = shake1_patched
                hackinfo[0]["rom"] = "rom/" + shake1_patched
                f2 = open("meta/" + shake1 + ".new", "w")
                f2.write( json.dumps(hackinfo[0]) + "\n" )
                f2.close()
                os.rename("meta/" + shake1 + ".new", "meta/" + shake1 + "")
    
                f2 = open("hacks/" + hackinfo[0]["id"]  + ".new", "w")
                f2.write( json.dumps(hackinfo[0]) + "\n" )
                f2.close()
                os.rename("hacks/" + hackinfo[0]["id"]  + ".new", "hacks/" + hackinfo[0]["id"]  + "")
                found = True
                break
        #
        if found == False:
            print('ERROR: No BPS found')
    


if __name__ == '__main__':
    extract_function(sys.argv)
    


    #zip.printdir()
  
