# -*- coding: utf-8 -*-
import urllib2
import requests
import re
import time

def getHtml(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0')
    req.add_header('Host', '10.10.4.132')
    req.add_header('Cookie', 'csrftoken=8kgouCYk63PMm8XNgiK8RkWtPDZVp892; sessionid=6qryn7w6nsmkf5frv6jqzpqlo0ek9eg1')
    res = urllib2.urlopen(req)
    body = res.read()
    # name = re.compile('<h3 id="vul_name">(.*?)</h3>')
    return body

# def saveHtml(file_name,file_content):
# #    注意windows文件命名的禁用符，比如 /
#     with open (file_name.replace('/','_')+".html","wb") as f:
# #   写文件用bytes而不是str，所以要转码
#         f.write( file_content )

for i in range(1,2300,1):
    url = ("http://10.10.4.132/help/vuldetail/?id=%d&height=540&width=720"%i)
    time.sleep(2)
    try:
        body = getHtml(url)
        title = re.findall('<h3 id="vul_name">(.*?)</h3>',body)
        f =open(title[0].decode('utf-8'),'w')
        f.write(body)
        print ("%d"%i)
        b = "%d"%i
        f =open("ok.txt",'ab')
        f.write(b+'\r\n')
    except:
        print ("%d--error"%i)
        a = "%d"%i
        f =open("error.txt",'ab')
        f.write(a+'\r\n')


# print body
# saveHtml("text3",body)