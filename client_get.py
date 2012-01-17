'''
this is a client application that posts data to the
data server
'''

import datetime as dt
import requests
import time

ip_address = '50.56.226.226'
port = '8000'
#ip_address = '127.0.0.1'
tag = 'sawtooth'


date_end = dt.datetime.now()
date_start = date_end - dt.timedelta(days=1)

request_string = 'http://%s:%s/?tag=%s&date_start=%s&date_end=%s'
request_string = request_string % (ip_address,
                                   port,
                                   tag,
                                   date_start.isoformat(),
                                   date_end.isoformat())

#print request_string


r = requests.get(request_string)

print r.content