# coding=utf-8
from app.zhdb.Omodel import *


def deal_data(form_data, model):
    form_data.pop('submit')
    form_data.pop('csrf_token')
    print(model)
    import importlib
    a = importlib.import_module('app.zhdb.Omodel.%s' % model)
    password = None
    pa_flag = False
    for key in form_data.keys():
        if 'passwd' == key:
            pa_flag = True
            # 如果有密码需要进行加密处理
            password = form_data['passwd']
            form_data.pop('passwd')
            break
    Omodel = getattr(a, model)(**form_data)
    if pa_flag:
        Omodel.password = password
    form_data = Omodel.to_dict()
    print(form_data)
    return form_data
