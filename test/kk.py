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
var = 1
def md5Encode(str):  
    m = hashlib.md5()  
    m.update(str)  
    return m.hexdigest()  

timestamp = str(int(round(time.time() * 1000)))
name = 'Dstv.10-28'+timestamp+'Dstv.10-28'
nameBytes = name.encode('gbk')   # 字节

sign = md5Encode(nameBytes)

#print timestamp,sign

url = "http://api.eatlm.com:8080/Box/stream/1510157508/"
#url = "http://api.eatlm.com:8080/Box/stream/1506683912"  # CID
#url = "http://api.eatlm.com:8080/Box/stream/1506683912/105"   # ROOMID
headers = {
    'Host':'api.eatlm.com:8080',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0',
    #'Referer':'http://api.eatlm.com:8080/Box/stream/1510158915/8501',
    'Content-Type':'application/x-www-form-urlencoded',
    'timestamp':timestamp,
    'sign':sign
    }
r=requests.get(url,headers=headers)
data1 = json.loads(r.text)
for record1 in data1["data"]:
    roomid = str(record1['roomid'])
    print record1['roomid']
while var == 1:
      room = raw_input()
      url2 = url + room
      r2=requests.get(url2,headers=headers)
      data2 = json.loads(r2.text)
      print data2['data']['playu_rtmp']
#print r.text

#
#print dataa['data']['playu_rtmp']
#date = r.headers["Date"]
#print timestamp,sign