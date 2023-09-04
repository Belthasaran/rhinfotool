#!/usr/bin/python3

import json
import re
#import jinja2
import datetime
#from jinja2 import Environment, FileSystemLoader, select_autoescape
import requests
import os
import sys


def fetch_download_function(data1):
    if type(data1)==list:
        data = data1
    else:
        data = [data1]

    user_agent = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    requests_debug = {'verbose': sys.stderr}
    
    url = 'http:' + data[0]["name_href"]
    #url = 'http:' + data[0]["download_href"]
    print('Requests.get ' + url +   "for hack id " + str(data[0]["id"]))
    req = requests.get(url, headers = user_agent)
    
    f = open("temp/in.zip.new", "wb")
    f.write(req.content)
    f.close()
    os.rename("temp/in.zip.new", "temp/in.zip")
    
    f = open("zips/" + data[0]["id"] +".zip.new", "wb")
    f.write(req.content)
    f.close()
    os.rename("zips/" + data[0]["id"]  + ".zip.new", "zips/" + data[0]["id"] +".zip")
    
if __name__ == '__main__':
    pass
    #fetch_download_function()
    
