import os
import subprocess
import json
from datetime import datetime
from upload import *
from S3_file_management import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('img',help='inference image path')
parser.add_argument('config',help='checkpoint file path')
args = parser.parse_args()

# 경로바꾸시려면 download_file에서 세번째 파라미터에서 조정하시면 됩니다!
download_file('smartfarmtv', "mixed_real_test.png", './mixed_real_test.png')


subprocess.call([f"python ../mmdetection/tools/dataset_converters/images2coco.py {args.img} ../mmdetection/label.txt result.json"],shell=True)
subprocess.call([f"python ../mmdetection/tools/test2.py ../mmdetection/configs/cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_1x_coco.py {args.config} --format-only --option 'jsonfile_prefix=./result'"],shell=True)

image_files = []
with open ("../mmdetection/annotations/result.json",'r') as f:
    ann_file = json.loads(f.read())

for i in ann_file['images']:
    image_files.append(i['file_name'])


with open("./result.bbox.json",'r') as j:
    result_list = json.loads(j.read())


tmp = dict()
for result in result_list:
    if tmp.get(result['image_id']):
        score = tmp[result['image_id']][1]

        if score < result['score']:
            tmp[result['image_id']] = [result['category_id'],result['score']]


    else:
        tmp[result['image_id']] = [result['category_id'],result['score']]

result_list = tmp






file_num = 0
now_time = datetime.now().strftime('%Y-%m-%d_%H:%M')
now_hour = str((int(now_time[11:13]) + 9) % 24)
now_time = now_time.replace(now_time[11:13],now_hour)

file_name_list = []
file_path_name_list = []




for name,pred in zip(image_files,list(result_list.values())):
    
    pred = pred[0]
    ext = name[name.find('.'):]
    fname = name
    if pred == 0:
        new_fname = os.path.join(image_path,str(file_num)+"_Bug_정상_"+str(now_time)+ext)
        os.rename(fname,new_fname)
        file_path_name_list.append(new_fname)
            
            
    elif pred == 1:
        new_fname = os.path.join(image_path,str(file_num)+"_Bug_배추좀나방_"+str(now_time)+ext)
        os.rename(fname,new_fname)
        file_path_name_list.append(new_fname)
        file_name_list.append(str(file_num)+"_Bug_배추좀나방_"+str(now_time)+ext)

    elif pred == 2:
        new_fname = os.path.join(image_path,str(file_num)+"_Bug_배추흰나비_"+str(now_time)+ext)
        os.rename(fname,new_fname)
        file_path_name_list.append(new_fname)
        file_name_list.append(str(file_num)+"_Bug_배추흰나비_"+str(now_time)+ext)
    elif pred == 3:
        new_fname = os.path.join(image_path,str(file_num)+"_Bug_벼룩잎벌레_"+str(now_time)+ext)
        os.rename(fname,new_fname)
        file_path_name_list.append(new_fname)
        file_name_list.append(str(file_num)+"_Bug_벼룩잎벌레_"+str(now_time)+ext)

    else :
        new_fname = os.path.join(image_path,str(file_num)+"_Bug_비단노린재_"+str(now_time)+ext)
        os.rename(fname,new_fname)
        file_path_name_list.append(new_fname)
        file_name_list.append(str(file_num)+"_Bug_비단노린재_"+str(now_time)+ext)


    file_num += 1






for file in file_name_list:
    upload_file("../image/" + file , 'smartfarmtv')


for file in file_path_name_list:
    os.remove(file)

