# coding=utf-8
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, IntegerField, TextAreaField, SelectField
from wtforms.validators import Required,DataRequired


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
    # classify = StringField()
    # 后续优化改为从数据库查询
    module_list = [(1,'日记随笔'), (2,'学习笔记'),(3, '童年记忆'), (4,'兴趣爱好')]
    classify = SelectField(label='类别',validators=[DataRequired('请选择标签')],choices=module_list,default=1,coerce=int)
    title = StringField(validators=[Required()])
    text = TextAreaField(validators=[Required()])
    submit = SubmitField()
