import webapp2


application = webapp2.WSGIApplication([
	('/view', 'view.ViewPage'),
	('/edit', 'edit.EditPage'),
	('/', 'survey.MainPage'),
], debug=True)
 
