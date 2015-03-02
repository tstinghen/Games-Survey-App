import webapp2
import time
import os 
import db_defs
from google.appengine.ext import ndb
from jinja2 import Environment, PackageLoader
#####REPEATED CODE FROM SURVEY.PY#####
env = Environment(loader=PackageLoader('main', 'templates'))

template_variables = {}  

def render(self, template, template_variables={}):
		template = env.get_template(template)
		self.response.write(template.render(template_variables))
######END REPEATED SECTION#####	
		
class ViewPage(webapp2.RequestHandler):

    def get(self):
		template_variables = {}
		if self.request.get('type') == 'responders': 
			urlsafekey = urlsafe=self.request.get('key')
			resp_key = ndb.Key(urlsafe=self.request.get('key'))
			responder = resp_key.get() 
			template_variables = {'urlsafe_key': urlsafekey, 'name': responder.name, 'fav_game': responder.fav_game, 'num_track': responder.num_track, 'resource': responder.resource, 'meeple': responder.meeple, 'residents': responder.residents}
			render(self, 'view.html', template_variables)
			
			
			
			# self.response.headers['Content-Type'] = 'text/plain'
			# self.response.write("Hey check this out...\n")
			# self.response.write(time.strftime("\n\n%a, %b %d %Y \n%H:%M %p\n\n", time.localtime()))
			# self.response.write("That's your local time, right? \nMaybe? \n\nWell it's somebody's local time anyway. \nPretty dynamic, right??")
			
			
			