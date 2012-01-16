'''
this is a client application that posts data to the
data server
'''

import datetime as dt
import requests
import time

#ip_address = '50.56.226.226'
port = '8000'
ip_address = '127.0.0.1'
tag = 'sawtooth_post'
value = 0


while 1:
    date_end = dt.datetime.now()
    date_start = date_end - dt.timedelta(days=1)

    request_string = 'http://%s:%s/?tag=%s&date_start=%s&date_end=%s'
    request_string = request_string % (ip_address,
                                       port,
                                       tag,
                                       date_start.isoformat(),
                                       date_end.isoformat())

    print request_string

    #print request_string
    value += 0.1
    if value > 20:
        value = 0

    r = requests.get(request_string)

    time.sleep(10 * 60)

