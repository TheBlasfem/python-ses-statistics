import boto.ses
import cherrypy
import json
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

conn = boto.ses.connect_to_region(
        'us-east-1',
        aws_access_key_id='your-access-key',
        aws_secret_access_key='your-secret-access')

#conn.verify_email_address('ljuliom@gmail.com')

filedb = open( "db.txt", "r" )
linesd = filedb.readlines()

for i, line in enumerate(linesd):
	conn.send_email(
	        'your-from-email',
	        'More demos Amazon SES',
	        'Probando Envio de mensajes',
	        [linesd[i]])
filedb.close()

statistics = conn.get_send_statistics()

class Root(object):
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render(statistic=statistics.GetSendStatisticsResponse.GetSendStatisticsResult.SendDataPoints[0])
    index.exposed = True

cherrypy.quickstart(Root())