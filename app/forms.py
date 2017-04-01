from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import Required, Length


class LoginForm(FlaskForm):
    openid = StringField('openid')
    remember_me = BooleanField('remember_me', default=False)


class EditForm(FlaskForm):
    nickname = StringField('nickname')
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

