from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
import os
import datetime

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
    
@app.post('/api/v1/login')
async def login(user: user):
    if user.id == "admin" and user.password == "1234":
        return {"Authorization" : True}
    else:
        return {"Authorization" : False}

@app.post('/api/v1/postDisease')
async def postDisease():
    response = [{"idx": 1, "category": "disease", "date": "2022-05-30", "kind": "병", "datetime": [{'id': '1', 'datetime': '05:26'}], "weather": "흐림", "image_url": "./image2.jpg"}]
    return {
        "diseases": response
    }