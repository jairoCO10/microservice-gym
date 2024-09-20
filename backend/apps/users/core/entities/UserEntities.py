from dataclasses import dataclass
from datetime import date

@dataclass
class Users:
    id: int
    username: str
    email: str
    password: str
    firstname:str
    lastname:str
    age:int
    weight:float
    height:float
    has_conditions:str
    limitations:str
    is_admin:bool
    is_staff:bool
    cellphone:str
    birthday:date


@dataclass
class CreateUser:
    username: str
    email: str
    password: str
    firstname:str
    lastname:str
    cellphone:str
    birthday:date



@dataclass
class AuthToken:
    access_token: str
    token_type: str

