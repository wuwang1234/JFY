# coding=utf-8
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import uuid


class User(UserMixin):
    def __init__(self, username=None, number=None, email=None):
        self.username = username
        self.number = number
        self.email = email
        self.passwd = None  # 存入数据库的密码，password是传入的参数，没有加密前的密码

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.passwd = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.passwd, password)

    def to_dict(self):
        # self.__dict__.pop('password')
        return self.__dict__

    def get_id(self):
        if self.username is not None:
            return self.username
        else:
            return uuid.uuid4()


if __name__ == '__main__':
    user = User()
    print(user)
    print(dir(user))
    print(user.__dict__)
