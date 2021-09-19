from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,SelectField
from wtforms import ValidationError
from wtforms.validators import Required


class Pitchform(FlaskForm):
    title = StringField('Pitch Title')
    category = SelectField('Category', choices=[('Technology','Technology'), ('Sports', 'Sports'), ('Motivation', 'Motivation')])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')