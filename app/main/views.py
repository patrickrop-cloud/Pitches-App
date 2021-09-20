from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from ..models import  Comments, User,Pitches
from .forms import PitchForm,CommentForm,UpdateProfile
from .. import db, photos
from . import main

@main.route('/')
def index():
    message= "Welcome to Pitch Application!!"
    title= 'Pitches App'
    sport= Pitches.query.filter_by(category = 'Sports').all()
    technology= Pitches.query.filter_by(category = 'Technology').all()
    advertising = Pitches.query.filter_by(category = 'Advertising').all()
    interview= Pitches.query.filter_by(category = 'Interview').all()
    production=Pitches.query.filter_by(category = 'Production').all()

    return render_template('index.html', message=message,sport=sport,technology=technology,title=title,advertising=advertising,interview=interview,production=production)

@main.route('/pitch/', methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        pitch= form.pitch.data
        user_id = current_user

        # Updated pitchinstance
        new_pitch = Pitches(title=title,category= category,pitch= pitch,user_id=current_user.id)

        title='New Pitch'

        new_pitch.save_pitch()

        return redirect(url_for('main.index'))

    return render_template('pitch.html',form= form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user == None: 
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['POST','GET'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user == None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.author))

    return render_template('profile/update.html',form =form)
 

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile',uname=uname))   


@main.route('/categories/<cate>')
def category(cate):
    '''
    function to return the pitches by category
    '''
    category = Pitches.get_pitches(cate)
    # print(category)
    title = f'{cate}'
    return render_template('categories.html',title = title, category = category)

@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitches.query.get(pitch_id)
    all_comments = Comments.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comments(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)