import benchmark
import os

from random import randint

from urllib2 import Request, urlopen
from cookielib import LWPCookieJar

import requests

class Benchmark_urllib2(benchmark.Benchmark):

    each = 1

    def setUp(self):
        self.size = 50
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'
        self.prefix_url = 'http://www.google.com/search?q='
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
            pass
        # }}}

        # make google to cache this query?
        # {{{
        for n in self.numbers:
            c = requests.get(self.prefix_url+n).content
        # }}}

        print 'benchmarking...'

#    def test_urllib2(self):
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
    def test_requests(self):
        ''' ''' # {{{
        for n in self.numbers:
            c = requests.get(self.prefix_url+n).content
        # }}}
        
#    def test_requests_proxy(self):
#        ''' ''' # {{{
#        for n in self.numbers:
#            c = requests.get(self.prefix_url+n, proxies={'http': self.proxy}).content
#        # }}}
#        
    def test_requests_stream(self):
        ''' ''' # {{{
        for n in self.numbers:
            c = requests.get(self.prefix_url+n, stream=True).content
        # }}}
        


if __name__ == '__main__':
    benchmark.main(format="markdown", numberFormat="%.4g")
