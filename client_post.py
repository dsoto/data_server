'''
this is a client application that posts data to the
data server
'''

import datetime
import requests
import time
from config import host_ip


ip_address = host_ip
port = '8000'

url = 'http://' + ip_address + ':' + port

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

    r = requests.post(url, data=data)

    time.sleep(60 * 20)

