# -*- coding: utf-8 -*-
import hashlib
def test():
    count=0
    md5='38e4c352809e150186920aac37190cbc'
    str='flag{www_shiyanbar_com_is_very_good_'
    while count==0:
        for i in range(32,127):
            a=chr(i)
            for i in range(32,127):
                b=chr(i)
                for i in range(32,127):
                    c=chr(i)
                    for i in range(32,127):
                        d=chr(i)
                    test=str+a+b+c+d+'}'
                    m=hashlib.md5()
                    m.update(test)
                    m=m.hexdigest()
                    if(cmp(m,md5)==0):
                               count=1
                               print 'ok'
                               print test

if __name__ == '__main__':
    test()
    pass