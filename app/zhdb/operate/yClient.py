from app.zhdb.mysql_models import ymodel
from app import db


class AddOneItem(object):
    def __init__(self, model, form=None):
        self.form_data = form
        self.data_model = model
        self.add_object = None

    def save(self):
        self.add_object = getattr(ymodel, self.data_model)(**self.form_data)
        print(db)
        db.create_all()
        db.session.add(self.add_object)  # 使用SqlAlchemy保存
        db.session.commit()


class DeleteAllItems(object):
    def __init__(self, model, condition=None):
        self.data_model = model
        self.condition = condition
        self.delete_object = None

    def delete(self):
        self.delete_object = \
            QueryOneItem(self.data_model, condition=self.condition).get_one_items()
        db.session.delete(self.delete_object)  # 使用SqlAlchemy保存
        db.session.commit()


class QueryOneItem(object):
    # def __init__(self, *args, **kwargs):
    def __init__(self, model, condition=None):
        # self.data_model = args[0]
        # self.condition = kwargs['condition']
        self.data_model = model
        self.condition = condition
        self.model_object = getattr(ymodel, self.data_model)

    def get_all_items(self):
        Omodel = self.model_object
        for O in Omodel.query.filter_by().all():
            print(O.username)
        return Omodel.query.filter_by().all()

    def get_one_items(self):
        o_model = self.model_object.query.filter_by(**self.condition).first()
        print(o_model.number)
        return o_model


class UpdateAllItems(object):
    def __init__(self, model, condition=None, update_info=None):
        self.data_model = model
        self.condition = condition
        self.update_object = None
        self.update_info = update_info

    def update(self):
        self.update_object = \
            QueryOneItem(self.data_model, condition=self.condition).get_one_items()
        for attr, value in self.update_info.items():
            self.update_object.attr = value
        db.session.add(self.update_object)  # 使用SqlAlchemy保存
        db.session.commit()
