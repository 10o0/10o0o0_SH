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
    all = json.loads(r.text)
    return all

url1 = "http://api.eatlm.com:8080/Box/stream/"
data1 = open(url1)
for record1 in data1["data"]:
    cid = str(record1['cid'])


    url2 = url1 + cid  # CID
    data2 = open(url2)
    for record2 in data2["data"]:
        roomid = str(record2['roomid'])
        print record1['name'],record1['cid'],record2['nick'],record2['roomid']
#
#        url3 = url2 + "/" + roomid   # ROOMID
#        data3 = open(url3)
#        try:
#            print data3['data']['playu_hls']
#            print data3['data']['playu_flv']
#            print data3['data']['playu_url']
#            print data3['data']['playu_rtmp']
#            print data3['data']['playu_mp4']
#            print "****************************"
#        except:
#            continue
#            try:
##                print data3['data']['playu_hls']
#                print data3['data']['playu_flv']
##                print data3['data']['playu_url']
#                print data3['data']['playu_rtmp']
##                print data3['data']['playu_mp4']
#            except:
#                continue
#        date = r.headers["Date"]
#print timestamp,sign