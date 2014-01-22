Benchmark Report
================

Benchmark urllib2
-----------------

                   name | rank | runs |   mean |       sd | timesBaseline
------------------------|------|------|--------|----------|--------------
urllib3 connection pool |    1 |   10 | 0.1156 | 0.006399 |           1.0
          urllib3 basic |    2 |   10 | 0.1184 | 0.006743 | 1.02462916467
                urllib2 |    3 |   10 | 0.1803 |  0.00766 | 1.56019867567
       requests session |    4 |   10 | 0.2182 |  0.02923 | 1.88860321873
               requests |    5 |   10 |  0.331 |  0.04303 | 2.86456249653

Each of the above 50 runs were run in random, non-consecutive order by
`benchmark` v0.1.5 (http://jspi.es/benchmark) with Python 2.7.3
Linux-3.2.0-39-generic-x86_64 on 2014-01-22 10:20:29.


Environment
================

Testing Server is Nginx with HttpEchoModule.
