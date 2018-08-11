#coding:utf-8
import requests
from bs4 import BeautifulSoup as bs
import os
import re
import thread
import socket

i=1
socket.setdefaulttimeout(5)
def get_soup(url):
    html=requests.get(url).content
    soup=bs(html,"html.parser")
    return soup

def get_tags_box(url,soup):#获取导航框中每个tags目录如http://www.symmz.com/xiezhen
    div=soup.find(class_="tags-box")
    tags=div.find_all(name="a")
    tag_dirs={} #目录用字典，url用列表
    for tag in tags[1:]:
        k=tag.string
        t=str(tag['href']).split('.')[0]
        tag_dirs[k]=url+t
    return tag_dirs

def get_tag_page(tag_dir):#根据tag_dir获取该tag下的导航栏每个page的url如http://www.symmz.com/xiezhen/1.html
    tag_url=tag_dir+'.html'
    soup=get_soup(tag_url)
    page=soup.find(class_="page")
    link=page.find(name="a",text="尾页")#直接找到尾页对应的url，不用弄两个for循环来找
    page_urls=[]
    if link==None:
        a=2
    else :
        a=str(link['href']).split('/')[-1].split('.')[0]
        a=int(a)+1
    for i in range(1,a):
        page_url=tag_dir+'/'+str(i)+'.html'
        page_urls.append(page_url)
    return page_urls

def get_img_box(page_url,url):#根据page_url找到该page下每个相册的目录img_dir如http://www.symmz.com/xiezhen/25122-1.html
    soup=get_soup(page_url)
    img_dirs={}
    divs=soup.find_all(class_="colum")
    for div in divs:
        link=div.find(name="a")
        k=link['title']
        t=str(link['href'])
        img_dirs[k]=url+t

    return img_dirs


def get_img_page(img_dir,tag_dir):#
    soup=get_soup(img_dir)
    img_urls=[]
    div=soup.find(class_="page")
    s=div.find(name="a").string
    n=re.findall(r'\d/(\d+)',s.encode('utf-8',"replace"),re.S)#找导航栏的又一种方法，直接找第一个1/25匹配出页数
    num=int(n[0])+1
    for i in range(1,num):
        t=str(img_dir).split('/')[-1]
        tmp=t.split('-')[0]
        img_url=tag_dir+'/'+tmp+'-'+str(i)+'.html'
        img_urls.append(img_url)
    #print img_urls
    return img_urls

def download_img_page(img_url,tag_name,dir_name):#下载每个img_page下的图片
    soup=get_soup(img_url)
    lazys=soup.find(id="srcPic").find_all(name="img")
    for lazy in lazys:
        lazy_src=lazy['src']
        filename=str(lazy_src).split('/')[-1]
        try:
            img=requests.get(lazy_src,timeout=5).content
        except requests.exceptions.ConnectionError as e:
            print 'requests'
            print e
            continue
        except socket.timeout as e:
            print 'socket.timeout'
            print e
            continue
        book='f:/Img/'
        if not os.path.exists(book):
            print '开始创建 '+book+' 目录'
            os.mkdir(book)

        photo=book+tag_name+'/'+dir_name+'/'

        if not os.path.exists(photo):
            print '开始创建相册'
            os.makedirs(photo)
        filename=photo+filename
        global i
        print '开始下载第 '+str(i)+' 张图片...'
        with open(filename,"wb") as f:
            f.write(img)

        i=i+1

if __name__=='__main__':
    url='http://www.symmz.com'
    soup=get_soup(url)
    tag_dirs=get_tags_box(url,soup)
    for tag_name in tag_dirs:
        #print tag_name,tag_dirs[tag_name]
        tag_dir=tag_dirs[tag_name]
        page_urls=get_tag_page(tag_dir)
        for page_url in page_urls:
            img_dirs=get_img_box(page_url,url)
            for dir_name in img_dirs:
                img_dir=img_dirs[dir_name]
                img_urls=get_img_page(img_dir,tag_dir,)
                for img_url in img_urls:
                    download_img_page(img_url,tag_name,dir_name)



