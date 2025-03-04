from flask import Blueprint

bl = Blueprint('blog', __name__)

from app.blog import handlers