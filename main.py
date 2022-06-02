import csv
from time import time
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
    datetime: list
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
weather_list = [weather.today_weather(date[0], date[1], 60, 120) for date in date_list]
time_list = [{'datetime' : get_image_date(data)[1]} for data in data_list]
url_list = [get_image_url(data) for data in data_list]
    
@app.post('/api/v1/postDisease')
async def postDisease():
    response = [{
        "category": "disease", 
        "kind": "병", 
        "date": date_list[0][0],
        "datetime": time_list, 
        "weather": [{
            'state' : weather_list[0]['state'], 
            'temperature' : weather_list[0]['temperature'], 
            'precipitation' : weather_list[0]['precipitation']
            }], 
        "image_url": url_list[0], 
        'dbmemo' : ''
        }]
    f = open('database.csv', 'r', encoding="utf-8")
    rd = csv.reader(f)
    for line in rd:
        if line[0] == date_list[0][0]:  # db에 해당 날씨 정보가 있을 때 일지 추가
            response[0]['dbmemo'] = line[-1]
        else: continue
    f.close()

    return {
        "diseases": response
    }

@app.post('/api/v1/postWeather')
async def postWeather():
    current_time = str(datetime.datetime.now()).split()
    date, time = current_time[0], current_time[1][:5]
    current_tw = weather.today_weather(date, time, 60, 120)
    response = {'date' : current_tw['date'], 'temperature': current_tw['temperature'], 'state': current_tw['state'], 'precipitation': current_tw['precipitation']}
    return {
        "weather": response
    }

@app.post('/api/v1/postMemo')
async def postMemo(memo: memo):
    fr = open('database.csv', 'r', encoding="utf-8")  # read
    rd = csv.reader(fr)

    temp = []
    for line in rd:
        if memo.date == line[0]:
            line[-1] = memo.memo
        temp.append(line)
    fr.close()

    fw = open('database.csv', 'w', newline='', encoding="utf-8")  # write   
    wr = csv.writer(fw)
    for t in temp:
        wr.writerow(t)

    fw.close()

    return {'response': "access"}