from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField, TextAreaField
from wtforms.validators import Required


class LoginForm(Form):
    username = StringField(validators=[Required()])
    passwd = PasswordField(validators=[Required()])
    submit = SubmitField()


class RegistrationForm(Form):
    username = StringField(validators=[Required()])
    passwd = PasswordField(validators=[Required()])
    number = IntegerField(validators=[Required()])
    email = StringField(validators=[Required()])
    submit = SubmitField()


class ArticleForm(Form):
    classify = StringField()
    title = StringField(validators=[Required()])
    text = TextAreaField(validators=[Required()])
    submit = SubmitField()
