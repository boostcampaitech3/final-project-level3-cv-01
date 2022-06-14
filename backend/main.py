import csv
from time import time
from urllib import response
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import datetime
import schema
from utills.memo import *
from utills.weather import *
from utills.S3_file_management import *
from utills.getS3contents import *
from utills.cls_kind import *


app = FastAPI()


origins = [
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


@app.post('/api/v1/login')
async def login(user: schema.user):
    if user.id == "admin" and user.password == "1234":
        return {"Authorization" : True}
    else:
        return {"Authorization" : False}


responese = get_standard_data()


@app.post('/api/v1/postDisease')
def postDisease():
    update_memo(responese)
    return {
        "diseases": responese
    }


@app.post('/api/v1/postWeather')
def postWeather():
    current_time = str(datetime.datetime.now()).split()
    date, time = current_time[0], current_time[1][:5]
    current_tw = today_weather(date, time, 60, 120)
    response = {'date' : current_tw['date'], 'temperature': current_tw['temperature'], 'state': current_tw['state'], 'precipitation': current_tw['precipitation']}
    return {
        "weather": response
    }

@app.post('/api/v1/postMemo')
def postMemo(memo: schema.memo):
    save_memo(memo)
    return {
        "response": "access"
    }