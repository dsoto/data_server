from wsgiref.simple_server import make_server
import twiggy as tw
import sqlite3
from config import host_ip

server_ip = host_ip

# example of post code at
# http://webpython.codepoint.net/wsgi_request_parsing_post

db_connection = sqlite3.connect('./database.db')
db_cursor = db_connection.cursor()


tw.quickSetup(file='log_simple_server.log')
tw.log.info('starting simple_server.py')

def app(environ, start_response):

    '''
    for key in environ.keys():
        print key, environ[key]
    '''

    if environ.get('REQUEST_METHOD') == 'POST':
        tw.log.info('POST received')
        # if post, parse and insert into database
        body = ''
        try:
            length = int(environ.get('CONTENT_LENGTH', '0'))
        except ValueError:
            length = 0
        if length != 0:
            body = environ['wsgi.input'].read(length)

        # deal with escaped colon
        body = body.replace('%3A', ':')

        data = body.split('&')
        dd = {}
        for d in data:
            kv = d.split('=')
            key = kv[0]
            value = kv[1]
            dd[key] = value

        query_string = 'insert into logs (tag, time_stamp, value) values (?,?,?)'
        db_cursor.execute(query_string, (dd['tag'], dd['time_stamp'], dd['value']))
        db_connection.commit()

        start_response('200 OK', [('Content-type', 'text/plain')])
        return['%s' % dd]

    # if get,
    # todo : return json blob of data with tag and daterange
    if environ.get('REQUEST_METHOD') == 'GET':
        tw.log.info(environ['QUERY_STRING'])
        qs = environ['QUERY_STRING']
        qlist = qs.split('&')
        dd = {}
        for q in qlist:
            kv = q.split('=')
            key = kv[0]
            value = kv[1]
            dd[key] = value

        print dd

        query_string = 'select * from logs where tag=? and time_stamp>? and time_stamp<?'
        result = db_cursor.execute(query_string, (dd['tag'], dd['date_start'], dd['date_end']))

        response = '['
        for r in result:
            response += '{"time_stamp":"' + str(r[0]) + '","value":' + str(r[1]) + '},'
        response = response[:-1] + ']'


        print response
        start_response('200 OK', [('Content-type', 'text/plain'),('Access-Control-Allow-Origin','*')])
        return [response]  # something that you can iter

httpd = make_server(server_ip, 8000, app)
print "Serving on port 8000..."
httpd.serve_forever()
