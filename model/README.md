## :bulb: Model Installation Guide

### Git Clone
```bash
#Pytorch 설치 필요
git clone https://github.com/boostcampaitech3/final-project-level3-cv-01.git
cd model
```

### 1. MMDetection 
```bash
pip install -U openmim
mim install mmcv-full
cd mmdetection
pip install -v -e 
```

### 2. MMClassfication
```bash
#"1" 의 openmim, mmcv-full 설치필요
cd mmclassification
pip install -v -e 
```

### 3. Crontab 을 이용한 Batch Inference 설정
```bash
crontab -e

# Crontab 에 아래 내용 추가 후 저장 (경로설정 필수)
*/15 * * * * python {crontab_classification.py path} {img path} {checkpoint pth path}

* * * * * python {crontab_bug_detection.py path} {img path} {checkpoint pth path}

#:wq 로 저장
```

<br>
<br>


## :file_folder: Checkpoint Download


1. [배추 Detection pth](https://drive.google.com/file/d/1I50u2QwuEDl7U2lL5DaIBYNFNqKFLQMN/view?usp=sharing)
2. [해충 Detection pth](https://drive.google.com/file/d/1vVC38mZDHUqYGZEhVeYePIpCbWcwn3Rl/view?usp=sharing)
3. [질병 Classification pth](https://drive.google.com/file/d/1tRxeN1ahd5aGez7EDBYGYN3QykBbXMgy/view?usp=sharing)




<br>
<br>

## :notebook: Train Usage

### 배추 Detection Model
```bash
#mywork/_base_/datasets/coco_detection.py 에서 train_pipeline 수정필요
cd mmdetection
python tools/train.py configs/../mywork/cascade_rcnn/swin_cascade_rcnn_x101_64x4d_fpn_20e_coco.py
```


### 해충 Detection Model
```bash
#config/1.MyConfig/datasets/custom.py 에서 train_pipeline 수정필요
cd mmdetection
python tools/train.py configs/cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_1x_coco.py

```

### 질병 Classification Model
```bash
#config/1.MyConfig/datasets/custom.py 에서 train_pipeline 수정필요 
cd mmclassification 
python tools/train.py configs/1.MyConfig/resnext/my_resnext152-32x4d_8xb32_in1k.py

```


<br>
<br>


## :notebook: Inference Usage

### 배추 Detection Model
```bash
#pth file 다운 및 mywork/_base_/datasets/coco_detection.py 에서 test_pipeline 수정필요
cd mmdetection
python tools/cabbage_detection.py {img path} {config file path} {checkpoint pth path} {save dir path}
```


### 해충 Detection Model
```bash
#pth file 다운 및 config/1.MyConfig/datasets/custom.py 에서 test_pipeline 수정필요
cd mmdetection
python tools/test.py configs/cascade_rcnn/cascade_rcnn_x101_64x4d_fpn_1x_coco.py \
{pth_path} --options "jsonfile_prefix={output filename}"
```

### 질병 Classification Model
```bash
#pth file 다운 및 config/1.MyConfig/datasets/custom.py 에서 test_pipeline 수정필요 
cd mmclassification
python tools/test.py configs/1.MyConfig/resnext/my_resnext152-32x4d_8xb32_in1k.py \
{pth_path} --out {output filename} --out-itmes all
```