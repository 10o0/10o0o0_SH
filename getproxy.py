"""
由Lz1y修改：
1.由Python2修改为Python3
2.将ip写入txt文件中，并且去重复了
3.退出程序时更加优雅

请用python3执行
"""
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import signal
import sys
import os
import time
from datetime import datetime, timedelta, timezone


def handler(signal_num,frame):
	Goduplicate()
	sys.exit(signal_num)


def proxy_spider():
	headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",}
	for i in range(1,50):		
		url='http://www.kuaidaili.com/free/outtr/'+str(i)
		r=requests.get(url=url,headers=headers)
		html = r.text
		print(r.status_code)
		if "-10" not in html :
			if (r.status_code == 200):
				soup= BeautifulSoup(html, "html.parser")
				datas=soup.find_all('tr')
				for data in datas[1:-1]:
#					soup_proxy= BeautifulSoup(data , "html.parser")	
#					print(data)
					proxy_contents=data.find_all(name = 'td')
					ip_org=proxy_contents[0].string
					ip="http://"+ip_org
					port=proxy_contents[1].string
					protocol=proxy_contents[3].string
					print("[*] ip :"+ip + ':' + port )
#					proxy_check(ip,port,protocol)
					with open("proxy_ip.txt",'a',encoding="utf-8") as ip:
							ip.write(ip_org+':'+port + '\n')
			time.sleep(2)
		else:
			time.sleep(2)
			continue
"""
def proxy_check(ip,port,protocol):
	proxy={}
	proxy[protocol.lower()]='%s:%s'%(ip,port)
	#print proxy
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	try:
		r=requests.get(url='https://www.google.com.hk',headers=headers,proxies=proxy,timeout=5) #
#		ip_available=re.findall(r'\[(.*?)\]',r.text)[0]
#		ip_availables="http://"+ip_available
		if r.status_code == 200:
			print ("[+]"+str(ip)+'  is ok')
			with open("proxy_ip.txt",'a',encoding="utf-8") as ip:
				ip.write(ip_available+':'+port + '\n')			
	except Exception as e:
		print("[-]sorry :"+ip + ':' + port + ' is defeated')
		#print e
		pass
	"""	
def Goduplicate():
	now = datetime.now()
	os.remove("proxy_ips.txt")
	with open("proxy_ips.txt",'a',encoding = 'gbk') as edu:
		edu.write("#Author: Lz1y \n")
		edu.write("#此页为采集可用翻墙http代理，使用教程: \n               http://www.lz1y.cn/wordpress/?p=515\n\n\n")
		edu.write("更新时间为:"+str(now)+"\n\n\n\n\n")
	with open("proxy_ip.txt",encoding = 'utf-8') as urls:
		url = urls.readlines()	
	news_url = []
	for id in url:
		if id not in news_url:
			news_url.append(id)
	for i in range(len(news_url)):
		with open("proxy_ips.txt",'a') as edu:
			edu.write(news_url[i])
	os.remove("proxy_ip.txt")
	print ("\nDone,the available ip have been put in 'proxy_ips.txt'...")
	print ("\nSucceed to exit.")
		
		
if __name__ == '__main__':
	signal.signal(signal.SIGINT, handler)
	proxy_spider()
	Goduplicate()
