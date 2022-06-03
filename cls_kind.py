from getS3contents import *

def get_cls_kind(data):
    data = data.split('_')
    category, kind = data[1], data[2]
    return category, kind

def get_date(data):
    data = data.split('_')
    date, time = data[3], data[4][:5]
    return date, time

