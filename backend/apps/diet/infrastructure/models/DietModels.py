from sqlalchemy import Column, Integer, String, Boolean, Date, Float, Text
from infrastructure.database import Connection


class Diet(Connection.Base):
    __tablename__ = "diets"

    id =  Column(Integer, primary_key=True, index=True)
    name  = Column(String(100))
    calories =  Column(Integer)
    protein  =  Column(Float)
    carbs =  Column(Float)
    fats  =  Column(Float)