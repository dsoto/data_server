import cgi
from wsgiref.simple_server import make_server
import twiggy as tw

# example of post code at
# http://webpython.codepoint.net/wsgi_request_parsing_post


tw.quickSetup(file='log_simple_server.log')
tw.log.info('staring simlpe_server.py')

def app(environ, start_response):
    for key in environ.keys():
        print key, environ[key]
    #print environ['QUERY_STRING']
        
    tw.log.info(environ['QUERY_STRING'])
    qs = environ['QUERY_STRING']
    qlist = qs.split('&')
    for q in qlist:
        kv = q.split('=')
        tw.log.info('key ' + kv[0] + '  value ' + kv[1])
    #qs = cgi.parse_qs(environ['QUERY_STRING'])

    start_response('200 OK', [('Content-type', 'text/plain')])
    return ['%s' % qs]  # something that you can iter

httpd = make_server('50.56.226.226', 8000, app)
print "Serving on port 8000..."
httpd.serve_forever()
