from typing import List
from pydantic import BaseModel


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