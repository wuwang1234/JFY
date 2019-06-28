from app.zhdb.mongodb_models import *


class User(db.Document):
    meta = {'allow_inheritance': True}
    username = db.StringField(required=True, max_length=50)
    number = db.StringField(required=True)
    email = db.StringField(required=True)
    passwd = db.StringField(required=True)


class Role(db.Document):
    meta = {'allow_inheritance': True}
    name = db.StringField(max_length=50)
