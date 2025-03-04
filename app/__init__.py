from flask import Flask, Blueprint
app = Flask(__name__)
from app import routes

from app.blog import bl as app_blog
app.register_blueprint(app_blog, url_prefix='/blog')

