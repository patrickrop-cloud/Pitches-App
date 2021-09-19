from flask import render_template,redirect,url_for,request
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns index page and it's data
    '''
    return render_template('index.html')
