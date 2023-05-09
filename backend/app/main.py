import jwt
import uvicorn

from app import controller, models
from fastapi.middleware.cors import CORSMiddleware
from .database import engine

from datetime import datetime, timedelta
from typing import Union, Any
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

from app.security import validate_token, reusable_oauth2

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'

app.include_router(controller.router, tags=['Calculator Salary'], prefix='/api')

def generate_token(username: Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds=60 * 60 * 24 * 3  # Expired after 3 days
    )
    to_encode = {
        "exp": expire, "username": username
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    return encoded_jwt

class LoginRequest(BaseModel):
    username: str
    password: str

def verify_password(username, password):
    if username == 'admin' and password == 'admin':
        return True
    return False

@app.post('/login')
def login(request_data: LoginRequest):
    print(f'[x] request_data: {request_data.__dict__}')
    if verify_password(username=request_data.username, password=request_data.password):
        token = generate_token(request_data.username)
        return {
            'token': token
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")
    

