# coding=utf-8
import json
from app.utils.data_transfer import time_transfer
from app.utils.contants import classify


def to_json(data_model, Oresult):
    import importlib
    a = importlib.import_module('app.zhdb.Omodel.%s' % data_model)
    result = []
    for o in Oresult:
        temp = {}
        for i in getattr(a, data_model)().to_dict():
            temp[i] = o[i]
        result.append(temp)
    # 根据业务对结果进行进一步处理
    for i in result:
        if 'classify' in i.keys():
            i['classify'] = classify[i['classify']]
        if 'date' in i.keys():
            i['date'] = time_transfer(i['date'])
    return json.dumps(result)
