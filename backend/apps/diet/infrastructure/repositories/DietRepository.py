from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from infrastructure.models.DietModels import Diet as ORMDiet



class DietRepository:
    def __init__(self, db:Session) -> None:
        self.db = db
    
    async def create_meal(self, name: str, calories: int, protein: float, carbs: float, 
                          fats: float):
        meal = ORMDiet(name = name, calories=calories, protein=protein, carbs=carbs, fats=fats)
        self.db.add(meal)
        self.db.commit()
        self.db.refresh(meal)
        return meal
    

    async def get_diet(self, diet_id: int) -> ORMDiet:
        result = self.db.execute(select(ORMDiet).filter(ORMDiet.id == diet_id))
        return result.scalars().first()

    async def get_diets(self,) -> List[ORMDiet]:
        result = self.db.execute(select(ORMDiet))
        return result.scalars().all()
