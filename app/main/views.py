from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, request
from . import main
from .forms import LoginForm, RegistrationForm, ArticleForm
from app.zhdb.zh_db_interface import *
import sys
from app.utils import contants, deal_form_data, util_for_login


@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        # ...
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())


@main.route('/home', methods=['GET', 'POST'])
@main.route('/home/?<string:username>', methods=['GET', 'POST'])
def home(username=None):
    if username is None:
        return render_template('home.html')
    else:
        return render_template('home.html', username=username, current_time=datetime.utcnow())


@main.route('/userLogin', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 从表单数据获取查询条件
        user = request.form.get('username')
        passwd = request.form.get('passwd')
        print(user)
        filter_data = {'username': user}
        # 获取数据库模型和实例模型
        fname = sys._getframe().f_code.co_name
        data_model = contants.DB_Enum[fname]
        # 根据查询条件从获取数据库得到的数据
        # Oquery = QueryObject(data_model, condiction)
        # Oquery = OperaInter(data_model, condition=condiction)
        # Oquery.get_all_items()
        # Oresult = Oquery.get_one_items()
        ks = {'condition': filter_data}
        Oresult = OperaInter().query_one(data_model, **ks)
        # 根据查询结果得到返回的实例模型
        # login_info = util_for_login.get_login_info(data_model, Oresult)
        login_flag = util_for_login.juage_login_passwd(data_model, passwd, Oresult)
        print(login_flag)
        if login_flag:
            return redirect(url_for('main.home', username=user))
        else:
            return redirect(url_for('main.login'))
    return render_template('user_login.html', Flag=True,
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())


@main.route('/userRegistor', methods=['GET', 'POST'])
def registor():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        flash("Logged in successfully.")
        # 获取表单数据
        form_dict = request.form.to_dict()
        # 获取数据库表模型
        # python中将一个字符串转为类名，可以通过ORM方式进行数据库数据查询
        fname = sys._getframe().f_code.co_name
        data_model = contants.DB_Enum[fname]
        # 处理数据
        DBdata_dict = deal_form_data.deal_data(form_dict, data_model)
        # 调用公共接口存储数据，传入要存储的数据和表模型
        kwargs = {'form': DBdata_dict}
        OperaInter().add(data_model, **kwargs)
        # add = ModelInter(DBdata_dict, data_model)
        # add.save()
        # user.save()
        # form.populate_obj(user)
        # print(user)
        # db.session.add(user)  # 使用SqlAlchemy保存
        # db.session.commit()
        # login_user(user)
        # user.save()
        return redirect(url_for('main.home', username=form_dict['username']))
    return render_template('user_registor.html', Flag=False,
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())


@main.route('/arctile_edit', methods=['GET', 'POST'])
def arctile_edit():
    form = ArticleForm(request.form)
    if form.validate_on_submit():
        form_dict = request.form.to_dict()
        fname = sys._getframe().f_code.co_name
        data_model = contants.DB_Enum[fname]
        DBdata_dict = deal_form_data.deal_data(form_dict, data_model)
        kwargs = {'form': DBdata_dict}
        OperaInter().add(data_model, **kwargs)
        return redirect(url_for('main.home', username=form_dict['username']))
    return render_template('arctile_edit.html', form=form,
                           known=session.get('known', False),
                           current_time=datetime.utcnow())


@main.route('/test')
def test():
    return redirect(url_for('main.home'))
