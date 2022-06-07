import os
import json
import pandas as pd
ann_folder = '/opt/ml/input/Project/data/Training/label'
ann_files = os.listdir(ann_folder)
image_folder = '/opt/ml/input/Project/data/Training/image'
label_data = []


for file in ann_files:
    with open(os.path.join(ann_folder,file)) as f:
        json_object = json.load(f)
    
    fname = json_object['description']['image']
    disease = json_object['annotations']['disease']
    risk = json_object['annotations']['risk']
    
    label = 0 

    if disease == 0: # 정상
        label = 0

    elif disease == 5: # 배추검음썩음병
    
        if risk == 1:  # 초기
            label = 1

        elif risk == 2: # 중기
            #label = 2
            label = 1

        else : # 말기
            #label =3
            label = 1
    
    else: # 배추노균병

        if risk == 1:   # 초기
            #label = 4
            label = 2

        elif risk == 2: # 중기
            #label = 5
            label = 2

        else :  # 말기
           # label = 6
            label = 2 

    label_data.append([os.path.join(image_folder,fname),label])

df = pd.DataFrame(label_data,
                        columns = ['path','label'])

df.to_csv('./train_3label.csv',sep=',',columns=['path','label'],index=False)
    