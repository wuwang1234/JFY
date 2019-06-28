# coding=utf-8
import os

basedir = os.path.abspath(os.path.dirname(__file__))
username = 'root'
password = 'Huawei@123'
hostname = 'localhost'
database = 'jfy'
# MYSQL_URL = 'mysql+pymysql://%s:%s@%s:3306/%s' %\
#             (username, password, hostname, database)
MYSQL_URL = 'mysql+pymysql://{}:{}@{}:3306/{}'.format(username, password, hostname, database)
print(MYSQL_URL)
MONGO_URL = 'mongodb://localhost:27017/flask'

# D:\JustForYou
print(basedir)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
         pass


class DevelopmentConfig(Config):# 开发环境mongodb
    print('use development environment')
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('DEV_DATABASE_URL') or MONGO_URL


class TestingConfig(Config): #测试环境
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config): #生产环境mysql
    print('use production environment')
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 588
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or MYSQL_URL
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}