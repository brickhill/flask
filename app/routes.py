from app import app
from flask import render_template
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import db
from app.models import User
from flask_login import login_required

@app.route('/')
@app.route('/index')
# @login_required
def index():
    user = {'username': 'Peter'}
    return render_template('index.html', title='Home', user=user)

