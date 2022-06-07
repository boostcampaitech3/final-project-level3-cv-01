import boto3
import csv
import datetime
from .cls_kind import *
from .weather import *

def get_all_objects(s3, **base_kwargs):
    continuation_token = None
    while True:
        list_kwargs = dict(MaxKeys=1000, **base_kwargs)
        if continuation_token:
            list_kwargs['ContinuationToken'] = continuation_token
        response = s3.list_objects_v2(**list_kwargs)
        yield from response.get('Contents', [])
        if not response.get('IsTruncated'):  
            break
        continuation_token = response.get('NextContinuationToken')

def make_objects_list(BucketName):
    """
    bucket에 존재하는 객체들을 리스트로 return
    """
    with open("output.txt", "w") as f:
        for file in get_all_objects(boto3.client('s3'), Bucket=BucketName):
            f.write(file['Key']+'\n')

    with open('./output.txt', 'r') as f:
        objects_list = f.readlines()
        for idx, obj in enumerate(objects_list):
            objects_list[idx] = obj.strip()
    return objects_list

def make_object(bucketname, objectname):
    """
    S3의 원하는 bucket에서 원하는 객체의 정보를 받아옴
    """
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucketname)
    return bucket.Object(objectname)


def get_image_type(object):
    """
    s3에 올리기위한 이미지 확장자를 리턴
    url, 저장형식을 위함
    """
    return object.get()['ContentType'][6:]

def get_image_date(object):
    """
    해당 이미지의 생성 날짜를 return
    """


    month_list = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12} 

    # 한국 시간으로 변경
    KST = datetime.timedelta(hours=9)

    obj = object.get()['LastModified']
    korea_time = str(obj + KST).split()

    date, time = korea_time[0], korea_time[1][:5]
    return date, time



def get_image_url(object):
    """
    bucket : Model Input Image, Inference Image 분류해서 두 개로 만들어야 할듯?
    filename : s3에 저장된 파일 명
    """
    filename = object.key
    bucketname = object.bucket_name
    s3_client = boto3.client('s3')
    location = s3_client.get_bucket_location(Bucket=bucketname)["LocationConstraint"]
    

    return f"https://{bucketname}.s3.{location}.amazonaws.com/{filename}"


def get_standard_data():
    objects_list = make_objects_list('smartfarmtv')[:-1]
    Bug_list = []
    Disease_list = []

    for data in objects_list:
        if data[2] == 'D':
            Disease_list.append(data)
        else:
            Bug_list.append(data)

    Bug_data_list = [make_object('smartfarmtv', obj) for obj in Bug_list]
    Disease_data_list = [make_object('smartfarmtv', obj) for obj in Disease_list]

    Bug_kind_list = [get_cls_kind(obj) for obj in Bug_list]
    Disease_kind_list = [get_cls_kind(obj) for obj in Disease_list]

    Bug_date_list = [get_image_date(data) for data in Bug_data_list]
    Disease_date_list = [get_image_date(data) for data in Disease_data_list]

    weather_list = [today_weather(date[0], date[1], 60, 120) for date in Disease_date_list]

    Bug_url_list = [get_image_url(data) for data in Bug_data_list]
    Disease_url_list = [get_image_url(data) for data in Disease_data_list]

    Bug_time_list = [{'datetime' : date[1], 'image_url' : url} for date, url in zip(Bug_date_list, Bug_url_list)]
    Disease_time_list = [{'datetime' : date[1], 'image_url' : url} for date, url in zip(Disease_date_list, Disease_url_list)]

    responese = []
    for idx, value in enumerate(Disease_kind_list):
        category, kind = value[0], value[1]
        if idx >= 1 and Disease_kind_list[idx] == Disease_kind_list[idx-1]:
            continue
        responese.append({
                "category": category, 
                "kind": kind, 
                "date": Disease_date_list[0][0],
                "datetime": Disease_time_list, 
                "weather": [{
                    'state' : weather_list[0]['state'], 
                    'temperature' : weather_list[0]['temperature'], 
                    'precipitation' : weather_list[0]['precipitation']
                    }],  
                "image_url": Disease_url_list[0], 
                'dbmemo' : ''
                })

    for idx, value in enumerate(Bug_kind_list):
        category, kind = value[0], value[1]
        if idx >= 1 and Bug_kind_list[idx] == Bug_kind_list[idx-1]:
            continue
        responese.append({
                "category": category, 
                "kind": kind, 
                "date": Bug_date_list[0][0],
                "datetime": Bug_time_list, 
                "weather": [{
                    'state' : weather_list[0]['state'], 
                    'temperature' : weather_list[0]['temperature'], 
                    'precipitation' : weather_list[0]['precipitation']
                    }], 
                "image_url": Bug_url_list[0], 
                'dbmemo' : ''
                })
    return responese


