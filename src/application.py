from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_admin import Admin 
from flask_admin.contrib.mongoengine import ModelView
from resources import Recommend
from models import db, SearchMovie
import config

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'seeecccreet'
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER


#db
app.config['MONGODB_HOST'] = 'mongodbhost'
app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_DB'] = 'admin'
app.config['MONGODB_USERNAME'] = 'root'
app.config['MONGODB_PASSWORD'] = 'rootpassword'

db.init_app(app)
app.session_interface = MongoEngineSessionInterface(db)


# admin
admin = Admin(app)
admin.add_view(ModelView(SearchMovie))


#endpoints
api.add_resource(Recommend, '/recommend')

if __name__=="__main__":
    app.run(host=config.HOST,
            port=config.HOST,
            debug= config.DEBUG)
