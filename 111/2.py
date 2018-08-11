import urllib2
response = urllib2.urlopen('http://www.pc28.am/')
html = response.read()
print html