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
		
class EditPage(webapp2.RequestHandler):
	
	def get(self): 
		template_variables = {}
		if self.request.get('type') == 'responders': 
			urlsafekey = urlsafe=self.request.get('key')
			resp_key = ndb.Key(urlsafe=self.request.get('key'))
			responder = resp_key.get() 
			template_variables = {'urlsafe_key': urlsafekey, 'key': resp_key, 'name': responder.name, 'fav_game': responder.fav_game, 'num_track': responder.num_track, 'resource': responder.resource, 'meeple': responder.meeple, 'residents': responder.residents}
			render(self, 'edit.html', template_variables)
			
			
	def post(self):
		action = self.request.get('action')
		if action == 'edit_results' : 
			resp_key = ndb.Key(urlsafe=self.request.get('key'))
			res = resp_key.get()
			res.name = self.request.get('name')
			res.fav_game = self.request.get('fav_game')
			res.num_track = self.request.get('num_track')
			res.resource = self.request.get('resource')
			res.meeple = self.request.get('meeple')
			res.residents = self.request.get_all('residents[]')
			res.put() 
			# render(self, 'survey.html')
			render(self, 'success.html', {'message': 'Success: Updated results for ' +res.name+ ' in the database'})
		else: 
			render(self, 'success.html', {'message': 'Error: Action ' + action + ' is unknown'})
		
		
		
		# action = self.request.get('action')
		# if action == 'edit_results' : 
			# resp_key = ndb.Key(urlsafe=self.request.get('key'))
			# res = resp_key.get()
			# res.name = self.request.get('name')
			# res.fav_game = self.request.get('fav_game')
			# res.num_track = self.request.get('num_track')
			# res.resource = self.request.get('resource')
			# res.meeple = self.request.get('meeple')
			# res.residents = self.request.get('residents')
			# res.put() 
			# render(self, 'survey.html')
			# render(self, 'success.html', {'message': 'Success: Updated survey answers for ' + res.name + ' in the database'})
		# else: 
			# render(self, 'success.html', {'message': 'Error: Action ' + action + ' is unknown'})
		
			
	
			