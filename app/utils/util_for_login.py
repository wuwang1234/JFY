# coding=utf-8
def get_login_info(Nmodel, Oquery_result=None):
    '''

    :param Nmodel: 数据库模型名称
    :param username: 登录用户名
    :return:返回查找的结果
    '''
    Ins = genera_object(Nmodel)
    Oquery = Oquery_result
    # print(Ins.to_dict())
    for att in Ins.to_dict():
        setattr(Ins, att, Oquery[att])
        # print(Ins.to_dict())
    return Ins.to_dict


def juage_login_passwd(Nmodel, passwd, Oquery_result=None):
    Ins = genera_object(Nmodel)
    Oquery = Oquery_result
    if Oquery is None:
        return False
    print(Ins.to_dict())
    for att in Ins.to_dict():
        # 根据数据库查询的结果重新构造返回的实例
        # print(Oquery[att])
        value = getattr(Oquery, att)
        setattr(Ins, att, value)
        # print(Ins.to_dict())
    return Ins.verify_password(passwd)


def genera_object(Nmodel):
    '''
    反射机制，利用字符串获取对象。获取实例对象
    :param Nmodel:实例模型名称
    :return:返回对象实例
    '''
    import importlib
    a = importlib.import_module('app.zhdb.Omodel.%s' % Nmodel)
    Ins = getattr(a, Nmodel)()
    return Ins
