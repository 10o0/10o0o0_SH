# -*- coding: utf-8 -*-
url = 'http://www.nwccw.gov.cn/'

from lxml import html
def geturltitle(url):
    doc = html.parse(url)
    title = doc.find('.//title').text
    return title
print geturltitle(url)

import requests
def getStatusCode(url):
    r = requests.get(url, allow_redirects = False)
    return r.status_code
print getStatusCode(url)

import socket
import urlparse
def host_to_ip(host):
    try:
        family, socktype, proto, canonname, sockaddr = socket.getaddrinfo(
            host, 0, socket.AF_UNSPEC, socket.SOCK_STREAM)[0]

        if family == socket.AF_INET:
            ip, port = sockaddr
        elif family == socket.AF_INET6:
            ip, port, flow_info, scope_id = sockaddr

    except Exception:
        ip = None
    return ip
print host_to_ip(urlparse.urlsplit(url)[1].split(':')[0])