from flask import render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_required, current_user, login_user
from app.blog import bl
from app import app, db
import sqlalchemy as sa
from app.models import User
from .forms import LoginForm

# @app.route('/index')
@app.route('/blog/xxx')
@login_required
def blog_index():
    return render_template('blog/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('blog/login.html', title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
