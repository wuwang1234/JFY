from app.zhdb.mysql_models import *


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    number = db.Column(db.String(64))
    email = db.Column(db.String(64))
    passwd = db.Column(db.String(100))

    def __repr__(self):
        return '<User %r>' % self.username
