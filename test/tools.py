# -*- coding: utf-8 -*-
import urllib2
import re
for i in xrange(0,10000):
    url = ("https://www.t00ls.net/members-profile-%d.html"%i)
    res = urllib2.urlopen(url)
    body = res.read()
    try:
        name = re.compile('<h2 class="user-nicename">@(.*?)</h2>').findall(body)[0]
        print name
        f =open("ok.txt",'ab')
        f.write(name+'\r\n')
    except:
        continue