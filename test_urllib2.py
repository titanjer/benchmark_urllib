import urllib2

params = [] 

#handler = urllib2.HTTPHandler(debuglevel=1)
#params.append(handler)

proxy = urllib2.ProxyHandler({'http': 'user-02703:2a6e7aga@31.220.11.117:1212'})
params.append(proxy)
auth = urllib2.HTTPBasicAuthHandler()
params.append(auth)

opener = urllib2.build_opener(*params)
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib2.install_opener(opener)
return_str = urllib2.urlopen('http://www.google.com/search?q=innovotech').read()

#print len(return_str)
print return_str

