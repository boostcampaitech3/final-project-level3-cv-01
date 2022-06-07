## SmartfarmTV


### **Product Flow**

![image-20220607165040960](https://raw.githubusercontent.com/variety82/imgForTypora/forUpload/img/image-20220607165040960.png)

### Service Architecture

![image-20220607165105401](https://raw.githubusercontent.com/variety82/imgForTypora/forUpload/img/image-20220607165105401.png)

### Directory

```
Backend/
├── main.py
├── requirements.txt
├── database.csv
└── utils
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
