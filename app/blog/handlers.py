from flask import render_template, request, flash, redirect, url_for
from app.blog import bl
from app import app
from .forms import LoginForm

# @app.route('/index')
@app.route('/blog/xxx')
def blog_index():
    return render_template('blog/index.html')

@app.route('/blog/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {} remember me = {}".
        format(form.username.data, form.remember_me.data))
        return redirect(url_for('blog_index'))
    return render_template('blog/login.html', title="Sign in", form=form)
