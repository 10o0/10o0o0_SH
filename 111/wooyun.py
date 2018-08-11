#coding:utf-8
import re
import requests
from urlparse import urlparse
headers = {
    'Host':'www.wooyun.org',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate',
    'Referer':'http://www.wooyun.org',
    'Content-Type':'application/x-www-form-urlencoded',
    'Connection':'keep-alive'
    }

def catch_url(url):
  r=requests.get(url,headers=headers)
  url=r.url
  for i in range(len(url)-1,0,-1):
    if url[i]=='/':
      break
  url_dir=url[:i+1]
  url_root=url[:url_dir.find('/',10)]

  urls={}
  urls[url]=True

  p=re.compile(r'(?<=href=[\"|\']).*?(?=[\"|\'])')
  for link in p.findall(r.content):
    try:
      if link.find('javascript:')==-1:
        link=link.strip().encode('utf-8')
        new_url=''
        if link=='':
          new_url=url
        elif link.startswith('/'):
          new_url=url_root+link
        elif link.startswith('http'):
          new_url=link
        else:
          new_url=url_dir+link
        urls[new_url]=True
    except:
      pass
  p=re.compile(r'(?<=action=[\"|\']).*?(?=[\"|\'])')
  for link in p.findall(r.content):
    try:
      if link.find('javascript:')==-1:
        link=link.strip().encode('utf-8')
        new_url=''
        if link=='':
          new_url=url
        elif link.startswith('/'):
          new_url=url_root+link
        elif link.startswith('http'):
          new_url=link
        else:
          new_url=url_dir+link
        urls[new_url]=True
    except:
      pass    
  return urls

def main():
  urls={}
  for i in range(1,44,1):
    for url in catch_url('http://wooyun.org/corps/page/%d'%i):
      urls[url]=True
    
  out={}
  for url in urls:
    out[urlparse(url).hostname]=True

  fd=open('wooyun.txt','w')
  for url in out:
    try:
      fd.write(url+'\n')
    except:
      pass
  fd.close()

if __name__ == '__main__':
  main()