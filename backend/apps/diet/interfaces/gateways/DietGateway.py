from typing import List
from sqlalchemy.orm import Session
from core.entities.DietEntities import MealCreate, MealReader
from infrastructure.repositories.DietRepository import DietRepository



class DietGateway:
    def __init__(self, db_session:Session):
        self.db_session = db_session
        self.repository = DietRepository(self.db_session)
    

    async def create_diet(self, name: str, calories: int, protein: float, carbs: float, 
                          fats: float, ):
        orm_meal = await self.repository.create_meal(name, calories, protein, carbs, fats)

        return MealCreate(name=orm_meal.name, calories=orm_meal.calories,
                          protein=orm_meal.protein, carbs=orm_meal.carbs, fats=orm_meal.fats)
    

    async def get_diets(self)->List[MealReader]:
        orm_meals = await self.repository.get_diets()
        meals = []
        for orm_meal in orm_meals:
            meals.append(MealReader(id=orm_meal.id,
                                    name=orm_meal.name,
                                    calories=orm_meal.calories,
                                    protein=orm_meal.protein,
                                    carbs=orm_meal.carbs,
                                    fats=orm_meal.fats))
        return meals
    

    async def get_diet(self, diet_id:int)->MealReader:
        orm_meal = await self.repository.get_diet(diet_id)
        if orm_meal:
            return MealReader(id=orm_meal.id,
                            name=orm_meal.name,
                            calories=orm_meal.calories,
                            protein=orm_meal.protein,
                            carbs=orm_meal.carbs,
                            fats=orm_meal.fats)
        return None

