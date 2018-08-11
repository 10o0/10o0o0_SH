# -*- coding: utf-8 -*-
import urllib2
import re
from lxml import etree

target_url = 'http://139.199.200.138:8081/999/one.asp?curpage='
for i in xrange(0,1):
    url = target_url + str(i)
    req = urllib2.Request(url=url)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11')
    req.add_header('Host', '139.199.200.138:8081')
    req.add_header('Cookie', 'WBKWXLTTEIITHZXPHWFC=ZOUVGVJIJXWYOVPYGDSFGIWDHRCCBBEOCHUJMPYV; TSCvalue=gb')
    res = urllib2.urlopen(req)
    body = res.read()
    selector = etree.HTML(body)
    data = selector.xpath("//table")
    info = data[0].xpath('string(.)').extract()[0]
    print info