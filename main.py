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
from S3_file_management import *
from getS3contents import *
from cls_kind import *
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


response = get_standard_data()

@app.post('/api/v1/postDisease')
async def postDisease():
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
    flag = True
    for line in rd:
        if memo.date == line[0]:
            line[-1] = memo.memo
            flag = False
        temp.append(line)
    fr.close()
    if flag:
        temp.append([memo.date, memo.datetime, memo.crop, memo.bug, memo.weather, memo.memo])
    fw = open('database.csv', 'w', newline='', encoding="utf-8")  # write   
    wr = csv.writer(fw)
    for t in temp:
        wr.writerow(t)

    fw.close()

    return {'response': "access"}