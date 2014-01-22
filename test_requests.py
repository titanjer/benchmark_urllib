import requests

#print len(requests.get('http://www.google.com/search?q=whoscall', ).content)
#print len(requests.get('http://www.google.com/search?q=whoscall', proxies={'http': 'http://user-02703:2a6e7aga@31.220.11.117:1212'}).content)
#print requests.get('http://www.google.com/search?q=whoscall', ).content
print requests.get('http://www.google.com/search?q=whoscall', proxies={'http': 'http://user-02703:2a6e7aga@31.220.11.117:1212'}).content

