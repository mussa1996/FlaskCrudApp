
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
import os
db = SQLAlchemy()
migrate = Migrate()
cors=CORS()
def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret-key'
    app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:mussa@localhost/leapture"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    return app
