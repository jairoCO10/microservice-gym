from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from infrastructure.models.UsersModels import User as ORMUser

import bcrypt


class UserRepository:
    def __init__(self, db: Session):
        self.db = db


    async def create_user(self, email: str, username: str, password: str, firstname: str, 
                          lastname: str, birthday: str, cellphone: str) -> ORMUser:
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = ORMUser(email=email, username=username, password=hash_password,
                    firstname=firstname, lastname=lastname, birthday=birthday,
                    cellphone=cellphone)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    async def get_user(self, user_id: int) -> ORMUser:
        result = self.db.execute(select(ORMUser).filter(ORMUser.id == user_id))
        return result.scalars().first()

    async def get_users(self,) -> List[ORMUser]:
        result = self.db.execute(select(ORMUser))
        return result.scalars().all()

    async def update_user(self, user_id: int, username: str, email: str) -> ORMUser:
        user = await self.get_user(user_id)
        if user:
            user.username = username
            user.email = email
            self.db.commit()
            self.db.refresh(user)
        return user

    async def delete_user(self, user_id: int) -> ORMUser:
        user = await self.get_user(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
        return user
    