from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from resources import Recommend
from models import db
import config

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER


app.config['MONGODB_HOST'] = 'mongodbhost'
app.config['MONGODB_PORT'] = 27017
app.config['MONGODB_DB'] = 'admin'
app.config['MONGODB_USERNAME'] = 'root'
app.config['MONGODB_PASSWORD'] = 'rootpassword'

# app.config['MONGO_HOST'] = 'db'
# app.config['MONGO_PORT'] = '27017'
# app.config['MONGO_DBNAME'] = 'admin'
# app.config['MONGO_USERNAME'] = 'root'
# app.config['MONGO_PASSWORD'] = 'rootpassword'
# app.config['MONGO_AUTH_SOURCE'] = 'admin'

db.init_app(app)
app.session_interface = MongoEngineSessionInterface(db)

api.add_resource(Recommend, '/recommend')
if __name__=="__main__":
    app.run(host=config.HOST,
            port=config.HOST,
            debug= config.DEBUG)
