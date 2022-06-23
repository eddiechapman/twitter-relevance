import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)

env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
app.config["UPLOADS"].mkdir(exist_ok=True)

db = SQLAlchemy(app)

from app import routes, models

try:
    db.create_all()
except sqlalchemy.exc.OperationalError as e:
    db.session.rollback()
else:
    db.session.commit()
