# -*- coding: utf-8 -*-
import urllib2
import re
for page in range(1,45):
    url="http://www.wooyun.org/corps/page/%d" % page   
    resp=urllib2.urlopen(url)
    html=resp.read()
    #print html

    m=re.compile('<td width="370"><a href="/corps/.*?">(.*?)<.*?"_blank">(.*?)<',re.S)

    for match in re.finditer(m,html):
        name = match.group(1)
        print match.group(2)
        link=match.group(2)
        link=link.replace("http：","")
        link=link.replace("/","")
        name = name.decode("utf-8").encode("gbk")
        print "%-40s%-40s" %(link,name)
    
    
