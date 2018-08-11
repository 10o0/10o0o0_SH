# -*- coding: utf-8 -*-
import urllib2,json,sys,smtplib
from email.mime.text import MIMEText
reload(sys)
sys.setdefaultencoding('utf-8')#避免中文编码问题
appkey = "e2376cfbe3b27dff923ed61698839a67"
url = 'http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?page=1'#API地址
req = urllib2.Request(url) #初始化请求
req.add_header("apikey", appkey) #添加 http请求的header
resp = urllib2.urlopen(req) #发起请求
content = resp.read()#获得返回内容，json格式字符串
if(content):
    json_result = json.loads(content) #转换为字典对象
    content_list = json_result['showapi_res_body']['contentlist']
    first_title = content_list[1]['title'].encode('utf8')
    first_text = content_list[1]['text'].encode('utf8')
    print '标题：'+first_title
    print '内容：'+first_text
else:
    print (content)
