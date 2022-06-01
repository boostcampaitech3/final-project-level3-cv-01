import csv
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
import os
import datetime
import weather
from upload import *
from getS3contents import *
from collections import deque

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class user(BaseModel):
    id: str
    password: str
    
class memo(BaseModel):
    idx: int
    crop: str
    bug: str
    weather: dict
    memo: str
    datetime: dict

@app.post('/api/v1/login')
async def login(user: user):
    if user.id == "admin" and user.password == "1234":
        return {"Authorization" : True}
    else:
        return {"Authorization" : False}


objects_list = make_objects_list('smartfarmtv')
data_list = [make_object('smartfarmtv', obj) for idx, obj in enumerate(objects_list)]
date_list = [get_image_date(data) for data in data_list]
tw = weather.today_weather(date_list[-1][0], date_list[-1][1], 60, 120) # 날짜, 시간, 위치, 경도
time_list = [{'datetime' : get_image_date(data)[1]} for data in data_list]
url_list = [get_image_url(data) for data in data_list]


@app.post('/api/v1/postDisease')
async def postDisease():
    id = 0
    category = "disease"
    # 모델에서 나온 결과에 따라 category 판별 일단 test용으로 disease로 설정

    response_disease = [
        {"idx": 1, "category": "disease", "date": date_list[0][0], "kind": "병", "datetime": time_list, "weather": [tw['state'], tw['temperature']], "image_url": url_list[0]}
        ]
    response_bug = [
        {"idx": 2, "category": "bug", "date": date_list[0][0], "kind": "해충", "datetime": time_list, "weather": [tw['state'], tw['temperature']], "image_url": url_list[0]},
        ]
        

    return {"diseases": response_disease} if category == "disease" else {"diseases" : response_bug}
    


@app.post('/api/v1/postWeather')
async def postWeather():
    response = {'date' : tw['date'], 'temperature': tw['temperature'], 'state': tw['state'], 'precipitation': tw['precipitation']}
    return {
        "weather": response
    }

@app.post('/api/v1/postMemo')
async def postMemo(memo: memo):
    print(memo)
    f = open('database.csv', 'a', newline='', encoding="utf-8")
    wr = csv.writer(f)
    
    print(memo.datetime)
    idx = str(memo.idx) + '_' + str(memo.datetime["id"])
    wr.writerow([idx, memo.crop, memo.bug, memo.weather, memo.memo])
    f.close()
    

    return {'response': "access"}

