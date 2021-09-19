from flask import render_template,redirect,url_for,request
# from app import app
from .forms import Pitchform,CommentForm
from . import main

#Views
@main.route('/')
def index():
    '''
    View root page function that returns index page and it's data
    '''
   
    # mesaage = "Welcome to Pitch App!"
    # title = 'Pitch-app'
    # technology = Pitches.query.filter_by(category = 'Technology').all()
    # now_showing_movie = get_movies('now_playing')

    # return render_template('index.html', message = message, title = title, technology = technology)
