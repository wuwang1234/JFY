import os
import configparser


def get_db_type():
    dirname = os.path.abspath(os.path.dirname(__file__))
    basedir = os.path.dirname(dirname)
    filename = ''
    if os.name == 'posix':
        filename = basedir + '/etc/zhdb.cfg'
    elif os.name == 'nt':
        filename = basedir + '\etc\zhdb.cfg'
    else:
        pass
    cf = configparser.ConfigParser()
    print(filename)
    cf.read(filename, encoding='utf-8')
    print(cf.sections())
    for sec in cf.sections():
        print(cf.options(sec))
    mongo_flag = True if cf.get('DEFAULT', 'use_pymongo') == 'True' else False
    mysql_flag = True if cf.get('DEFAULT', 'use_pymysql') == 'True' else False
    if mongo_flag:
        return 'mongo'
    elif mysql_flag:
        return 'mysql'
    else:
        return 'sqlite'
