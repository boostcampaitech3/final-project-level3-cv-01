from xml.dom.expatbuilder import parseString
import subprocess
import json
import os
from datetime import datetime
from S3_file_management import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('img',help='inference image path')
parser.add_argument('config',help='checkpoint file path')
args = parser.parse_args()


image_path = arg.img


subprocess.call([f"python ../mmclassification/tools/test.py ../mmclassification/configs/1.MyConfig/resnext/my_resnext152-32x4d_8xb32_in1k.py {args.configs} --out ./results.json --out-items all"],shell=True)



with open("./results.json",'r') as j:
    dic = json.loads(j.read())

with open("./file_name.json",'r') as k:
    image_files = json.loads(k.read())



file_num = 0
now_time = datetime.now().strftime('%Y-%m-%d_%H:%M')
now_hour = str((int(now_time[11:13]) + 9) % 24)
now_time = now_time.replace(now_time[11:13],now_hour)

file_name_list = []
file_path_name_list = []



for name,pred in zip(image_files,dic['pred_class']):

    
    ext = name[name.find('.'):]

    
    fname = name
    
    if pred == 'Normal':
        new_fname = os.path.join(image_path,str(file_num)+"_Disease_정상_"+str(now_time)+ext)
        os.rename(fname,new_fname)
        file_path_name_list.append(new_fname)
        
        

    elif pred == 'Black rot':
        new_fname = os.path.join(image_path,str(file_num)+"_Disease_배추검음썩음병_"+str(now_time)+ext)
        os.rename(fname,new_fname)
        file_path_name_list.append(new_fname)
        file_name_list.append(str(file_num)+"_Disease_배추검음썩음병_"+str(now_time)+ext)

    else :
        new_fname = os.path.join(image_path,str(file_num)+"_Disease_배추노균병_"+str(now_time)+ext)
        os.rename(fname,new_fname)
        file_path_name_list.append(new_fname)
        file_name_list.append(str(file_num)+"_Disease_배추노균병_"+str(now_time)+ext)


    file_num += 1






for file in file_name_list:
    upload_file(image_path+'/' + file , 'smartfarmtv')


for file in file_path_name_list:
    os.remove(file)
    

    














