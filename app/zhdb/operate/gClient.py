from app.utils import get_db_type
from app.zhdb.mongodb_models import gmodel


class AddOneItem(object):
    def __init__(self, model, form=None):
        self.dbtype = get_db_type.get_db_type()
        self.sql = None
        self.form_data = form
        self.data_model = model
        self.sql_data = None

    def transfer(self):
        if self.dbtype == 'mongo':
            self.sql_data = self.form_data
        else:
            self.sql_data = self.form_data  # self.deal_data(self.form_data)
        return self.sql_data

    # def deal_data(self, form_data):
    #     return form_data

    def save(self):
        save_data = self.transfer()
        print(save_data)
        Omodel_cls = getattr(gmodel, self.data_model)
        Omodel = Omodel_cls(**save_data)
        Omodel.save()


class DeleteAllItems(object):
    def __init__(self, model, condition=None):
        self.dbtype = get_db_type.get_db_type()
        self.data_model = model
        self.condition = condition
        self.model_object = None

    def set_model_object(self):
        if self.dbtype == 'mongo':
            self.model_object = getattr(gmodel, self.data_model)
        else:
            pass
        return self.model_object

    def delete(self):
        self.set_model_object().objects.filter(**self.condition).delete()


class QueryOneItem(object):
    def __init__(self, *args, **kwargs):
        # print(condition)
        print(args)
        print(kwargs)
        self.dbtype = get_db_type.get_db_type()
        self.data_model = args[0]
        self.condition = kwargs['condition']
        self.model_object = None

    def set_model_object(self):
        if self.dbtype == 'mongo':
            self.model_object = getattr(gmodel, self.data_model)
        else:
            pass
        return self.model_object

    def get_all_items(self):
        Omodel = self.set_model_object()
        for O in Omodel.objects.all():
            print(O.username)
        return Omodel.objects

    def get_one_items(self):
        o_model = self.set_model_object().objects.filter(**self.condition).first()
        # print(o_model.number)
        print(o_model)
        return o_model


class UpdateAllItems(object):
    def __init__(self, model, condition=None, update_info=None):
        self.dbtype = get_db_type.get_db_type()
        self.data_model = model
        self.condition = condition
        self.model_object = None
        self.update_info = update_info

    def set_model_object(self):
        if self.dbtype == 'mongo':
            self.model_object = getattr(gmodel, self.data_model)
        else:
            pass
        return self.model_object

    def update(self):
        self.set_model_object().objects.filter(**self.condition).update(**self.update_info)
