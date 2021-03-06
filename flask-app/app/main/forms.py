from ..models import Role, User
from flask_wtf import FlaskForm
#from flask.ext.admin.form import DateTimeField
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField,\
    SubmitField, DateTimeField, DateField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp

class NameForm(FlaskForm):
	name = StringField('What is your name?', validators=[DataRequired()])
	submit = SubmitField('Submit')

class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


