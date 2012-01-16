this repo is a very simple datalogging server.

data is posted by POST to port 8000
tag - data label
value - data value
time_stamp - local time of sensor report

data will be fetched by GET
(not implemented yet 16 jan 2012)

server.py - server running on rackspace

client_get.py - posts a sawtooth timeseries to server via GET

client_post.py - posts a sawtooth timeseries to server via POST

