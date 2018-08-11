# -*- coding: utf8 -*-
#author:woniu
import binascii
file=open('bin.txt','rb')
t=''
for line in file.readlines():
    t+=chr(int(line,2))
print t