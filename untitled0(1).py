# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 22:21:51 2017

@author: lenovo
"""
import requests
import hashlib  
import time
import json
#print(nameBytes)
  
def md5Encode(str):  
    m = hashlib.md5()  
    m.update(str)  
    return m.hexdigest()  

timestamp = str(int(round(time.time() * 1000)))
name = 'Dstv.10-28'+timestamp+'Dstv.10-28'
nameBytes = name.encode('gbk')   # 字节

sign = md5Encode(nameBytes)

#print timestamp,sign

def open(url):
    headers = {
    'Host':'api.eatlm.com:8080',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0',
    #'Referer':'http://api.eatlm.com:8080/Box/stream/1510158915/8501',
    'Content-Type':'application/x-www-form-urlencoded',
    'timestamp':timestamp,
    'sign':sign
    }
    r=requests.get(url,headers=headers)

    return r.text
url1 = "http://api.eatlm.com:8080/Box/stream/"
dataa = json.loads(open(url1))
for i in range(1,20):
    cid = dataa['data'][i]['cid']
# for i in dataa:
#     print dataa['data'][0]['cid']
# print "CID:"
# cid = raw_input()
    url2 = url1 + cid  # CID
    dataa1 = json.loads(open(url2))
    print dataa1
#
#
# print "ROOMID"
# roomid = raw_input()
# url3 = url2 + "/" + roomid   # ROOMID
# open(url3)


#date = r.headers["Date"]
#print timestamp,sign