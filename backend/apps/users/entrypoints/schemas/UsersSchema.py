# app/entrypoints/api/schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime,date


class UserBase(BaseModel):
    username: str
    email: str
    firstname: str
    lastname:str
    birthday:date
    cellphone:str

class UserCreate(UserBase):
    password: str

class Login(BaseModel):
    username:str
    password:str

class UserReader(BaseModel):
    username:str
    email:str
    firstname:str
    lastname:str
    # age:int
    # weight:float
    # height:float
    # is_admin:bool
    cellphone:str
    birthday:date




