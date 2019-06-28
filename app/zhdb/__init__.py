from app.utils.get_db_type import get_db_type
import importlib
db = None
dbtype = get_db_type()
DbClient = None
if dbtype == 'mongo':
    flask_mon_db = importlib.import_module('flask_mongoengine')
    db = flask_mon_db.MongoEngine()
    DbClient = importlib.import_module('app.zhdb.operate.gClient')
else:
    flask_sql_db = importlib.import_module('flask_sqlalchemy')
    db = flask_sql_db.SQLAlchemy()
    DbClient = importlib.import_module('app.zhdb.operate.yClient')

