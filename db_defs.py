from google.appengine.ext import ndb 

class Results(ndb.Model):
	name = ndb.StringProperty(required=True)
	fav_game = ndb.StringProperty(required=True)
	num_track = ndb.StringProperty(required=True)
	resource = ndb.StringProperty(required=True)
	meeple = ndb.StringProperty(required=True)
	residents =ndb.StringProperty(repeated=True)