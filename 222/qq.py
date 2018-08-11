# -*- coding: utf-8 -*-
import urllib2
import re

target_url = 'http://139.199.200.138:8081/999/one.asp?curpage='
for i in xrange(0,50):
    url = target_url + str(i)
    req = urllib2.Request(url=url)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11')
    req.add_header('Host', '139.199.200.138:8081')
    req.add_header('Cookie', 'WBKWXLTTEIITHZXPHWFC=ZOUVGVJIJXWYOVPYGDSFGIWDHRCCBBEOCHUJMPYV; TSCvalue=gb')
    res = urllib2.urlopen(req)
    body = res.read()
    qq = re.compile('<td align="left" class="bx" width="36%">(.*?)<span class=ckzz_superqq></td>')
    mima = re.compile('<td align="left" class="by1" width="63%">(.*?)</td>')
    qq_list = qq.findall(body)
    mima_list = mima.findall(body)
    for i in xrange(0,10):
        try:
            print qq_list[i],mima_list[i]
        except:
            break
