from flask import render_template, session, redirect, url_for
from . import main
# add in other key modules for views such as: Forms required, functional modules, DB models, etc.


@main.route('/')
@main.route('/index')
def index():
    return render_template("index.html")

