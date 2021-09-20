from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField,PasswordField,BooleanField,SubmitField,TextAreaField,SelectField
from wtforms import ValidationError
from wtforms.validators import Required,Email,EqualTo


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Save')


class PitchForm(FlaskForm):
    title = StringField('Pitch Title')
    category = SelectField('Category', choices=["  ",'Production', 'Advertising', 'Interview', 'Sport','Society', 'Technology'])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')    

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment',validators=[Required()])
    submit = SubmitField('Post Comments')