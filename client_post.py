'''
this is a client application that posts data to the
data server
'''

import datetime
import requests
import time

ip_address = '50.56.226.226'
port = '8000'
ip_address = 'http://127.0.0.1:8000'
tag = 'sawtooth_post'
value = 0

while 1:
    time_stamp = datetime.datetime.now().isoformat()
    print time_stamp
    data = {'tag': tag,
            'time_stamp': time_stamp,
            'value': value}

    #print request_string
    value += 0.1
    if value > 20:
        value = 0

    r = requests.post(ip_address, data=data)

    time.sleep(10)

