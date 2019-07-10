# coding=utf-8
import json


def to_json(data_model, Oresult):
    import importlib
    a = importlib.import_module('app.zhdb.Omodel.%s' % data_model)
    result = []
    for o in Oresult:
        temp = {}
        for i in getattr(a, data_model)().__dict__:
            temp[i] = o[i]
        result.append(temp)
    return json.dumps(result)
