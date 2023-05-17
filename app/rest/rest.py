from typing import Union
from fastapi import FastAPI
from generator import get_password

app = FastAPI()

@app.get('/password')
def getpassword(length: int = 12, hasPunctuation: bool = True):
    password = get_password(length, hasPunctuation)
    return {'password': password}