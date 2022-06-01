import csv
from urllib import response
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
    date: str
    datetime: str
    crop: str
    bug: str
    weather: dict
    memo: str

@app.post('/api/v1/login')
async def login(user: user):
    if user.id == "admin" and user.password == "1234":
        return {"Authorization" : True}
    else:
        return {"Authorization" : False}

objects_list = make_objects_list('smartfarmtv')
data_list = [make_object('smartfarmtv', obj) for idx, obj in enumerate(objects_list)]
date_list = [get_image_date(data) for data in data_list]
weather_list = [weather.today_weather(str(date[0]), str(date[1]), 60, 120) for date in date_list]
url_list = [get_image_url(data) for data in data_list]
    
@app.post('/api/v1/postDisease')
async def postDisease():
    response = [{
        "category": "disease", 
        "kind": "병", 
        "date": date_list[-1][0], 
        "datetime": date_list[-1][1], 
        "weather": [{
            'state' : weather_list[-1]['state'], 
            'temperature' : weather_list[-1]['temperature'], 
            'precipitation' : weather_list[-1]['precipitation']
            }], 
        "image_url": url_list[-1], 
        'dbmemo' : ''
        }]
    f = open('database.csv', 'r', encoding="utf-8")
    rd = csv.reader(f)
    for line in rd:
        if line[0] == date_list[-1][0]:  # db에 해당 날씨 정보가 있을 때 일지 추가
            response[0]['dbmemo'] = line[-1]
        else: continue
    f.close()

    return {
        "diseases": response
    }

@app.post('/api/v1/postWeather')
async def postWeather():
    response = {'date' : weather_list[-1]['date'], 'temperature': weather_list[-1]['temperature'], 'state': weather_list[-1]['state'], 'precipitation': weather_list[-1]['precipitation']}
    return {
        "weather": response
    }

@app.post('/api/v1/postMemo')
async def postMemo(memo: memo):
    print(memo)
    fr = open('database.csv', 'r', encoding="utf-8")  # read
    fw = open('database.csv', 'w', newline='', encoding="utf-8")  # write
    
    rd = csv.reader(fr)
    wr = csv.writer(fw)
    
    for line in rd:
        if memo.date == line[0]:
            line[-1] = memo.memo
        else:
            continue
    wr.writerow([memo.date, memo.datetime, memo.crop, memo.bug, memo.weather, memo.memo])
    fw.close()
    fr.close()

    return {'response': "access"}