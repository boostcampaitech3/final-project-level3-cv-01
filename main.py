from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

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

@app.get('/api/v1/getDisease')
async def get():
    response = [{"id": 1, "image_url": "https://picsum.photos/200", "time_stamp": datetime.date(2022,5,10), "species": "배추", "category": "disease", "kind": "병"}, {"id": 2, "image_url": "https://picsum.photos/300","time_stamp": datetime.date(2022,5,14), "species": "배추", "category": "bug", "kind": "벌레"}]
    return {
        "diseases": response
    }