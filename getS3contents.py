import boto3
import datetime

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
    obj = object.get()['ResponseMetadata']['HTTPHeaders']['date']
    date_info = obj.split()

    month_list = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12} 

    year, day, hour, minute = int(date_info[3]), int(date_info[1]), int(date_info[4][:2]), int(date_info[4][3:5])
    month = month_list[date_info[2]]
    KST = datetime.timezone(datetime.timedelta(hours=9))

    korea_time = str(datetime.datetime(year, month, day, hour, minute, 0, tzinfo=KST)).split()

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
    
    # if get_image_type(object) == 'jpg':
    #     imageType = 'jpg'
    # elif get_image_type(object) == 'jpeg':
    #     imageType = 'jpeg'

    return f"https://{bucketname}.s3.{location}.amazonaws.com/{filename}"



# objects_list = make_objects_list('smartfarmtv')
# tiger = make_object('smartfarmtv', objects_list[-1])


# date, datetime = get_image_date(tiger)
# print(date, datetime)


