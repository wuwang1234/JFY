from flask import Flask
from app.zhdb.zh_db_interface import ModelInter

app = Flask(__name__)
Imodel = ModelInter(app)
Imodel.set_db_name_and_model()
Model = Imodel.get_model()


class Role(Model.Role):
    pass


class User(Model.User):
    pass
