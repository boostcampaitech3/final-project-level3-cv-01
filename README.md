# 👩‍🌾SmartfarmTV👨‍🌾



### 등장 배경

한국에서 배추는 1인당 연간 소비량이 47.5kg에 달할정도로 소비가 많은 작물입니다. 그러나 매년 병충해 피해로 생산량이 감소하고 가격이 오르는 등 농가와 소비자에게 큰 피해가 있는 상황입니다.

따라서, 저희는 Computer Vision 기술을 활용해 실시간으로 농작물을 관찰하여 해충 및 질병피해가 발견된 경우 사용자에게 알려주어 농가의 피해감소, 노동력 절감 및 농가 경제 경쟁력을 향상시킬 수 있는 시스템을 개발하고자 하였습니다.


### 문제 정의

농작물에서 병해충을 Detection 해주는 모델을 사용해서, 농작물을 관찰하다 해충 및 질병피해가 발견된 경우 사용자에게 알려주어 사용자가 조치를 취할 수 있도록합니다.

# Environment



- OS : Linux Ubuntu 18.04.5

- GPU : Tesla V100 (32GB)

# Prerequisite

- react v18.1.0
- Node.js v16.15.0
- npm v8.5.5
- npx v8.5.5
- Package : package.json 참고

# Usage
## git clone
```
npm init # npm 초기화
git clone https://github.com/boostcampaitech3/final-project-level3-cv-01.git
```
## react start
```
cd app # 폴더 진입
npm install 
npm start
```



# Directory 구조



```bash
app
├── public
│   ├── index.html
│   └── manifest.json
├── src
│   ├── components
│   │    ├── Home
│   │    │    └── Home.jsx
│   │    ├── Log
│   │    │    ├── Log.jsx
│   │    │    ├── LogBox.jsx
│   │    │    └── LogDateBox.jsx
│   │    ├── LogDetail
│   │    │    └── LogDetail.jsx
│   │    ├── Login
│   │    │    └── Login.jsx
│   │    └── Navigator
│   │    │    └── Navigator.jsx
│   ├── App.js
│   ├── index.css
│   └── index.js
├── package.json
├── package-lock.json
└── README.md
```



# 🎞프로토타입



![시연영상](https://raw.githubusercontent.com/variety82/imgForTypora/forUpload/img/%EC%8B%9C%EC%97%B0%EC%98%81%EC%83%81.gif)



### Product Flow
___


![image-20220607165040960](https://raw.githubusercontent.com/variety82/imgForTypora/forUpload/img/image-20220607165040960.png)

### Service Architecture
___

![image-20220607165105401](https://raw.githubusercontent.com/variety82/imgForTypora/forUpload/img/image-20220607165105401.png)

# Dataset


### **AIHub 개방 데이터셋**

![image-20220607185039043](https://raw.githubusercontent.com/variety82/imgForTypora/forUpload/img/image-20220607185039043.png)

### 1. 노지 작물 질병 진단 이미지

주요 노지 작물 질병 데이터 중 배추 관련 데이터

전체 이미지 개수 : 12959장 ( Train : 10578 장 , Validation : 2378 장 )

3 class : 정상, 배추검음썩음병, 배추노균병

### 2. 노지 작물 해충 진단 이미지

주요 노지 작물 해충 데이터 중 배추 관련 데이터

전체 이미지 개수 : 114637장 ( Train : 109945 장 , Validation : 4692 장 )

4 class : 배추좀나방, 배추흰나비, 벼룩잎벌레, 비단노린재



# Model Pipeline



![image-20220607185059077](https://raw.githubusercontent.com/variety82/imgForTypora/forUpload/img/image-20220607185059077.png)

# Experiments



![image-20220607185115207](https://raw.githubusercontent.com/variety82/imgForTypora/forUpload/img/image-20220607185115207.png)

### ↘️ **배추 Detection**

**Task** : 배추 이미지에서 배춧잎 하나 detection

**Metric** : mAP50

| Model       | Backbone    | mAP50      |
| ----------- | ----------- | ---------- |
| RetinaNet   | Swin        | 0.7680     |
| SSD         | MobileNetV2 | 0.6130     |
| CascadeRCNN | ResNeXt     | 0.801      |
| CascadeRCNN | Swin        | 0.808      |
| CascadeRCNN | SwinL       | 0.739      |
| CascadeRCNN | Swin        | 0.827(Aug) |

**최종 모델 : CascadeRCNN + Swin Transformer**

### ↘️ **질병 Classification**

**Task** : Cropping 된 배춧잎에서 질병 Classification

**Metric** : Accuracy

| Model          | Accuracy |
| -------------- | -------- |
| Resnext152     | 0.93     |
| Resnet101      | 0.87     |
| Resnext101     | 0.89     |
| Swin Tiny      | 0.93     |
| Convnext Small | 0.88     |

**최종 모델 : Resnext101**

### ↘️ **해충 Detection**

**Task** : Cropping 된 배춧잎에서 해충 Detection

**Metric** : mAP50

| Model       | Backbone   | mAP50  |
| ----------- | ---------- | ------ |
| CascadeRCNN | Resnext101 | 0.8712 |

**최종 모델 : CascadeRCNN + Resnext101**
