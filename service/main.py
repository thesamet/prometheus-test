from prometheus_client import start_http_server, Counter, Histogram
import random
import time
import sys

start_http_server(int(sys.argv[1]))

r = Counter('requests', 'HTTP Failures')
e = Counter('errors', 'HTTP Failures')
h = Histogram('latency', 'HTTP Latency')

while True:
    success_count = max(0, int(random.gauss(8, 5)))
    error_count = max(0, int(random.gauss(8, 5)))
    r.inc(success_count + error_count)
    e.inc(error_count)
    for x in xrange(success_count + error_count):
        h.observe(random.gauss(0.07, 0.05))
    time.sleep(1)
    print "Tick"

