from typing import List
from sqlalchemy.orm import Session
from core.entities.UserEntities import CreateUser, Users
from infrastructure.repositories.UsersRepositories import UserRepository






class UserGateway:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.repository = UserRepository(self.db_session)

        
    async def create_user(self,  email: str, username: str, password: str, firstname: str, 
                          lastname: str, birthday: str, cellphone: str) -> CreateUser:
        orm_user = await self.repository.create_user( email, username, password, firstname, 
                          lastname, birthday, cellphone)
        return CreateUser(email=orm_user.email, username=orm_user.username, password=orm_user.password,
                        firstname=orm_user.firstname, lastname=orm_user.lastname, birthday=orm_user.birthday,
                        cellphone=orm_user.cellphone)
    

    async def get_users(self) -> List[Users]:
        orm_users = await self.repository.get_users()
        users = []
        for orm_user in orm_users:
            users.append(Users(id=orm_user.id, 
                         username= orm_user.username,
                         email=orm_user.email,
                         password= orm_user.password,
                         firstname= orm_user.firstname,
                         lastname= orm_user.lastname,
                         age = orm_user.age,
                         weight= orm_user.weight,
                         height = orm_user.height,
                         has_conditions= orm_user.has_conditions,
                         limitations = orm_user.limitations,
                         is_admin = orm_user.is_admin,
                         is_staff = orm_user.is_staff,
                         cellphone = orm_user.cellphone,
                         birthday = orm_user.birthday,))
        return users
    
    async def get_user(self, user_id: int) -> Users:
        orm_user = await self.repository.get_user(user_id)
        if orm_user:
            return Users(id=orm_user.id, 
                         username= orm_user.username,
                         email=orm_user.email,
                         password= orm_user.password,
                         firstname= orm_user.firstname,
                         lastname= orm_user.lastname,
                         age = orm_user.age,
                         weight= orm_user.weight,
                         height = orm_user.height,
                         has_conditions= orm_user.has_conditions,
                         limitations = orm_user.limitations,
                         is_admin = orm_user.is_admin,
                         is_staff = orm_user.is_staff,
                         cellphone = orm_user.cellphone,
                         birthday = orm_user.birthday,
                         )
        return None
    