from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

app = Flask(__name__)
    
app.config.from_object(Config)

db = SQLAlchemy(app=app)

bootstrap = Bootstrap5(app=app)

from app import models
