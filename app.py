from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_login import UserMixin
from app import login


app = Flask(__name__)
db = MongoEngine()
db.init_app(app)
login_manager = LoginManager()



app.config['SECRET_KEY'] = 'asdfg'
app.config["MONGODB_SETTINGS"] = {
    "db": "user_data",
    "host" : "localhost",
    "port" : 27017
}




