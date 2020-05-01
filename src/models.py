from datetime import datetime
from flask_mongoengine import MongoEngine

db = MongoEngine()

class SearchMovie(db.Document):
    
    time = db.DateTimeField(default=datetime.utcnow)
    movie_name = db.StringField()
    rec_success = db.BooleanField(default=False)
    rec_movies = db.ListField(db.StringField())
    ipp_address = db.StringField()
