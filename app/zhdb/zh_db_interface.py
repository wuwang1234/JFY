# coding=utf-8
from app.zhdb import dbtype, DbClient


class ModelInter(object):

    def __init__(self, app=None):
        self.db_model = None
        self.db = None
        self.app = app
        self.model = None

    def set_db_name_and_model(self):
        app = self.app
        if dbtype == 'mongo':
            from flask_mongoengine import MongoEngine
            from app.zhdb.mongodb_models import gmodel
            self.db = MongoEngine(app)
            self.db_model = MongoEngine(app).Document
            self.model = gmodel
        else:
            from flask_sqlalchemy import SQLAlchemy
            from app.zhdb.mysql_models import ymodel
            self.db = SQLAlchemy(self.app)
            self.db_model = SQLAlchemy(app).Model
            self.model = ymodel

    def get_db_name(self):
        return self.db

    def get_db_model(self):
        return self.db_model

    def get_model(self):
        return self.model


class OperaInter(object):

    def __init__(self):
        self.AddObject = None
        self.DeleteObject = None
        self.QueryObject = None
        self.UpdateObject = None

    def add(self, *args, **kwargs):
        self.AddObject = DbClient.AddOneItem(*args, **kwargs)
        self.AddObject.save()

    def delete(self, *args, **kwargs):
        self.DeleteObject = DbClient.DeleteAllItems(self, *args, **kwargs)
        self.DeleteObject.delete()

    def update(self, *args, **kwargs):
        self.UpdateObject = DbClient.UpdateAllItems(self, *args, **kwargs)
        self.UpdateObject.update()

    def query_one(self, *args, **kwargs):
        # self.QueryObject = QueryOneItem(self,*args, **kwargs)
        # 如果传入了self，接受参数的时候self是args的第一个参数
        self.QueryObject = DbClient.QueryOneItem(*args, **kwargs)
        return self.QueryObject.get_one_items()

    def query_all(self, *args, **kwargs):
        # self.QueryObject = QueryOneItem(self,*args, **kwargs)
        # 如果传入了self，接受参数的时候self是args的第一个参数
        self.QueryObject = DbClient.QueryAllItems(*args, **kwargs)
        return self.QueryObject.get_all_items()
