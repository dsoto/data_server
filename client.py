import datetime
import requests
import time

ip_address = '50.56.226.226'
port = '8000'
tag = 'sawtooth'
value = 0

while 1:
    time_stamp = datetime.datetime.now().isoformat()

    request_string = 'http://%s:%s/?tag=%s&value=%s&time_stamp=%s'
    request_string = request_string % (ip_address,
                                       port,
                                       tag,
                                       value,
                                       time_stamp)

    print request_string
    value += 0.1
    if value > 20:
        value = 0

    r = requests.get(request_string)

    time.sleep(15 * 60)

