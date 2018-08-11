# -*- coding: utf-8 -*-
import urllib
import time
import os
while(os.system('ping -c 1 -w 137.0.0.1')==0):
    print 'ooo'
    res = urllib.urlopen("http://127.0.0.1")
    status = res.getcode()
    print status
    time.sleep(5)
