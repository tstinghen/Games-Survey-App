import webapp2
import time
import os 
import db_defs
from google.appengine.ext import ndb
from jinja2 import Environment, PackageLoader
#from django.http import HttpResponse
#import jinja2
#code adapted from CS496 week 2 lectures 
	
#from jinja2 documentation
env = Environment(loader=PackageLoader('main', 'templates'))

template_variables = {}  

def render(self, template, template_variables={}):
		template = env.get_template(template)
		self.response.write(template.render(template_variables))

def set_temp_vals(self):
	template_variables['responders'] = [{'name': x.name, 'key': x.key.urlsafe()} for x in db_defs.Results.query().fetch()]
	return template_variables 
	
class MainPage(webapp2.RequestHandler):
	template_variables = {}  
   
	
	def get(self): 
		template_variables = set_temp_vals(self)
		render(self, 'survey.html', template_variables)
			
	def post(self):
	
		action = self.request.get('action')
		if action == 'add_results' : 
			k = ndb.Key(db_defs.Results, 'results_group')
			res = db_defs.Results(parent=k)
			res.name = self.request.get('name')
			res.fav_game = self.request.get('fav_game')
			res.num_track = self.request.get('num_track')
			res.resource = self.request.get('resource')
			res.meeple = self.request.get('meeple')
			res.residents = self.request.get_all('residents[]')#[ndb.Key(urlsafe=x) for x in self.request.get_all('residents[]')] # self.request.post.getlist('residents[]')
			res.put() 
			#render(self, 'survey.html')
			render(self, 'success.html', {'message': 'Success: Saved results for ' + res.name + ' to the database'})
		
		if action == 'edit_results' : 
			res = self.request.get('key')
			res.name = self.request.get('name')
			res.fav_game = self.request.get('fav_game')
			res.num_track = self.request.get('num_track')
			res.resource = self.request.get('resource')
			res.meeple = self.request.get('meeple')
			res.residents = self.request.get('residents')
			res.put() 
			#render(self, 'survey.html')
			render(self, 'success.html', {'message': 'Success: Updated results for ' + res.name + ' in the database'})
		
		#else: 
		#	render(self, 'survey.html', {'message': 'Error: Action ' + action + ' is unknown'})
		
		#self.template_variables['form_content'] = {}
		#template = env.get_template('survey.html')
		#for i in self.request.arguments(): 
		#	self.template_variables['form_content'][i] = self.request.get(i)
		#self.response.write(template.render(self.template_variables))
		
# application = webapp2.WSGIApplication([
    # ('/view*', ViewPage),
	# ('/', MainPage),
	
	
# ], debug=True)
 