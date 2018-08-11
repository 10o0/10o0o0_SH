# -*- coding: utf-8 -*-
import re
f = open("temp.txt", "r")
line = f.readline()
pattern = re.compile(ur'(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)')
str = u'1.2.3.234..324.3.4.3.4.3.3...44.4.4'
print(pattern.search(str))
f.close()