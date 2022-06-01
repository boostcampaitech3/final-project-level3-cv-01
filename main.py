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

# 테스트 부분
# upload_file('./호랑이.jpeg', 'smartfarmtv')
objects_list = make_objects_list('smartfarmtv')
tiger = make_object('smartfarmtv', objects_list[-1])
date, input_datetime = get_image_date(tiger)
img_url = get_image_url(tiger)

tw = weather.today_weather(date, input_datetime, 60, 120)  # 날짜, 시간, 위치, 경도

@app.post('/api/v1/postDisease')
async def postDisease():
    response = [{"idx": 1, "category": "disease", "date": date, "kind": "병", "datetime": [{'id': '1', 'datetime': input_datetime}], "weather": [{'state' : tw['state'], 'temperature' : tw['temperature'], "precipitation": tw["precipitation"]}], "image_url": img_url}]
    return {
        "diseases": response
    }

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

