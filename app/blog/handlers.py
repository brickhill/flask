from flask import render_template, request
from app.blog import bl
from app import app

# @app.route('/index')
@app.route('/blog/xxx')
def blog_index():
    return render_template('blog/index.html')

