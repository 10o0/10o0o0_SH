import urllib2
url = "http://www.keen8.com"


response = urllib2.urlopen(url)
print response.getcode()
print len(response.read())


request = urllib2.Request(url)
request.add_header('User-Agent','Mozilla/5.0')
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())
