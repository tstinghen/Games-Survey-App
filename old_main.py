import webapp2
import time
import os 
from jinja2 import Environment, PackageLoader
#import jinja2

#jinja environment info from lectures week2 

# JINJA_ENVIRONMENT = Environment(
	# Loader=FileSystemLoader(os.path.dirname(__file__) + '/templates'),
	# extensions=['ext.autoescape'], 
	# autoescape=True
	# )
	
#from jinja2 documentation
@webapp2.cached_property 
env = Environment(loader=PackageLoader('main', 'templates'))

class MainPage(webapp2.RequestHandler):
	template_variables = {}  
    
	def get(self): 
			template = env.get_template('week2.html')
			self.response.write(template.render())
			
	def post(self):
		self.template_variables['form_content'] = {}
		template = env.get_template('week2.html')
		for i in self.request.arguments(): 
			self.template_variables['form_content'][i] = self.request.get(i)
		self.response.write(template.render(self.template_variables))
		
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
 
