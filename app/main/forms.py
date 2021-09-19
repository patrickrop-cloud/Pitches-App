from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,SelectField
from wtforms import ValidationError
from wtforms.validators import Required,Email,EqualTo


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    title = StringField('Pitch Title')
    category = SelectField('Category', choices=["  ",'Production', 'Advertising', 'Interview', 'Sport', 'Technology'])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')    

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')