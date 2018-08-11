# -*- coding: utf-8 -*-
#author:pcat
#http://pcat.cnblogs.com
import base64

def foo():
	f=open('pic_png.txt').read()
	fsave=open('pic.png','wb')
	#添加的png头部
	addHeader="89 50 4E 47 0D 0A 1A 0A".replace(' ','').decode('hex')
	fsave.write(addHeader)
	fsave.write(base64.b64decode(f))
	fsave.close()
	pass

if __name__ == '__main__':
	foo()
	print 'ok'
	pass