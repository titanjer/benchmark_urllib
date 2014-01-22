import benchmark
import os, time

from random import randint

from urllib2 import Request, urlopen
from cookielib import LWPCookieJar
from urllib3 import PoolManager, HTTPConnectionPool 
import requests

class Benchmark_urllib2(benchmark.Benchmark):

    each = 10

    def setUp(self):
        ''' ''' # {{{
        self.size = 100
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'
        #self.prefix_url = 'http://www.google.com/search?q='
        self.server_ip = '192.168.1.100'
        self.server_port = '8011'
        self.server_path = 'hello?q='
        self.prefix_url = 'http://%s:%s/%s' % (self.server_ip, self.server_port, self.server_path)
        self.proxy = 'http://user-02703:2a6e7aga@31.220.11.117:1212'

        self.numbers = ['09%08d' % randint(10000001, 89000000) for i in xrange(self.size)]

        # Cookie jar
        # {{{
        home_folder = os.getenv('HOME')
        if not home_folder:
            home_folder = os.getenv('USERHOME')
            if not home_folder:
                home_folder = '.'   # Use the current folder on error.
        self.cookie_jar = LWPCookieJar(os.path.join(home_folder, '.google-cookie'))
        try:
            self.cookie_jar.load()
        except Exception:
            print '> cookie_jar failed'
            pass
        # }}}

        # make google to cache this query?
        # {{{
        for n in self.numbers:
            c = requests.get(self.prefix_url+n).content
        # }}}

        print 'benchmarking...'
        # }}}

    def eachTearDown(self):
        ''' ''' # {{{
        t = randint(1, 2)
        print 'sleep %d secs...' % t,
        time.sleep(t)
        print 'Wake up'
        # }}}

    def test_urllib2(self):
        ''' ''' # {{{
        for n in self.numbers:
            response = urlopen(self.prefix_url+n)
            l = len(response.read())
        # }}}

#    def test_urllib2_cookie(self):
#        ''' ''' # {{{
#        for n in self.numbers:
#            request = Request(self.prefix_url+n)
#            request.add_header('User-Agent', self.user_agent)
#            self.cookie_jar.add_cookie_header(request)
#            response = urlopen(request)
#            self.cookie_jar.extract_cookies(response, request)
#            html = response.read()
#            self.cookie_jar.save()
#        # }}}
#
#    def test_urllib2_proxy(self):
#        ''' ''' # {{{
#        proxy = urllib2.ProxyHandler({'http': self.proxy})
#        auth = urllib2.HTTPBasicAuthHandler()
#        opener = urllib2.build_opener(proxy, auth)
#        opener.addheaders = [('User-agent', self.user_agent)]
#        urllib2.install_opener(opener)
#
#        for n in self.numbers:
#            r = urllib2.urlopen(self.prefix_url+n).read()
#        # }}}
#
    def test_urllib3_basic(self):
        ''' Basic ''' # {{{
        http = PoolManager()
        for n in self.numbers:
            r = http.request('GET', self.prefix_url+n)
            l = len(r.data)
        # }}}

    def test_urllib3_connection_pool(self):
        ''' ''' # {{{
        http_pool = HTTPConnectionPool(self.server_ip, self.server_port)
        for n in self.numbers:
            r = http_pool.urlopen('GET', "/hello?q=%s" % n)
            l = len(r.data)
        # }}}
    
    def test_requests(self):
        ''' ''' # {{{
        for n in self.numbers:
            r = requests.get(self.prefix_url+n)
            l = len(r.content)
        # }}}
        
#    def test_requests_proxy(self):
#        ''' ''' # {{{
#        for n in self.numbers:
#            c = requests.get(self.prefix_url+n, proxies={'http': self.proxy}).content
#        # }}}
#        
#    def test_requests_stream(self):
#        ''' ''' # {{{
#        for n in self.numbers:
#            r = requests.get(self.prefix_url+n, stream=True)
#            l = len(r.content)
#        # }}}
#        

    def test_requests_session(self):
        ''' ''' # {{{
        s = requests.Session()
        for n in self.numbers:
            r = s.get(self.prefix_url+n)
            l = len(r.content)
        # }}}
        

if __name__ == '__main__':
    benchmark.main(format="markdown", numberFormat="%.4g")
