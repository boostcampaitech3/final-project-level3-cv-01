## SmartfarmTV

### 등장 배경  OR Why?

한국에서 배추는 1인당 연간 소비량이 47.5kg에 달할정도로 소비가 많은 작물입니다. 그러나 매년 병충해 피해로 생산량이 감소하고 가격이 오르는 등 농가와 소비자에게 큰 피해가 있는 상황입니다.

따라서, 저희는 Computer Vision 기술을 활용해 실시간으로 농작물을 관찰하여 해충 및 질병피해가 발견된 경우 사용자에게 알려주어 농가의 피해감소, 노동력 절감 및 농가 경제 경쟁력을 향상시킬 수 있는 시스템을 개발하고자 하였습니다.

### 문제 정의

농작물에서 병해충을 Detection 해주는 모델을 사용해서, 농작물을 관찰하다 해충 및 질병피해가 발견된 경우 사용자에게 알려주어 사용자가 조치를 취할 수 있도록 도와준다.

### **Product Flow**

![image-20220607165040960](https://raw.githubusercontent.com/variety82/imgForTypora/forUpload/img/image-20220607165040960.png)

### Service Architecture

![image-20220607165105401](https://raw.githubusercontent.com/variety82/imgForTypora/forUpload/img/image-20220607165105401.png)

### Directory

```
app
├── main.py
├── requirements.txt
├── S3_file_management.py
├── cls_kind.py
├── database.csv
├── getS3contents.py
└── weather.py
```

### Files

- `main.py` : FastAPI app root
- `cls_kind.py` : 해당 데이터의 category, kind, date, time을 가져오는 Component
- `getS3contents.py` : S3에 있는 이미지의 정보를 반환하는 Component(날짜, 시간, 이미지 url 등)
- `S3_file_management.py` : 연결된 S3 Bucket에 이미지를 업로드, 다운로드하는 Component
- `weather.py` : 기상청 API를 사용해 입력한 시간의 날씨를 크롤링해오는 Component

## Prerequisite

```
$ pip install -r requirements.txt
```

### **Run**

```
uvicorn main:app --reload --host={your_host} --port={your_port}
```

### 데모 영상

![시연영상](https://raw.githubusercontent.com/variety82/imgForTypora/forUpload/img/%EC%8B%9C%EC%97%B0%EC%98%81%EC%83%81.gif)
