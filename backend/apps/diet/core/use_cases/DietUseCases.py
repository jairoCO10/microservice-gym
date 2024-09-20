# app/core/usecases/user_usecase.py
from typing import List
from core.entities.DietEntities import MealCreate, MealReader
from interfaces.gateways.DietGateway import DietGateway

class DietUseCase:
    def __init__(self, diet_gateway: DietGateway):
        self.diet_gateway = diet_gateway

    async def create_diet(self, name: str, calories: int, protein: float, carbs: float, 
                          fats: float, ) -> MealCreate:
        return await self.diet_gateway.create_diet(name=name, calories=calories, protein=protein,
                                                   carbs=carbs, fats=fats)

    async def get_diet(self, diet_id: int) -> MealReader:
        return await self.diet_gateway.get_diet(diet_id)
    
    async def get_diets(self,) -> MealReader:
        return await self.diet_gateway.get_diets()

    # async def update_diet(self, diet_id: int, name: str, email: str) -> MealReader:
    #     return await self.diet_gateway.update_user(diet_id, name, email)

    # async def delete_diet(self, diet_id: int) -> MealReader:
    #     return await self.diet_gateway.delete_user(diet_id)
    