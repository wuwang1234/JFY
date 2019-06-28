from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from config import config
import importlib
from app.utils.get_db_type import get_db_type as dbtype


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = None
if dbtype() == 'mongo':

    flask_mon_db = importlib.import_module('flask_mongoengine')
    db = flask_mon_db.MongoEngine()
else:
    flask_sql_db = importlib.import_module('flask_sqlalchemy')
    db = flask_sql_db.SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name]) # 可以直接把对象里面的配置数据转换到app.config里面
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app


