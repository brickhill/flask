from flask import Flask, Blueprint
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models

from app.blog import bl as app_blog
app.register_blueprint(app_blog, url_prefix='/blog')
