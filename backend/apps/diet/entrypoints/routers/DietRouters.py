
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from interfaces.gateways.DietGateway import DietGateway
from core.use_cases.DietUseCases import DietUseCase
from entrypoints.schema.DietSchema import  Meal, DietPlan
from infrastructure.database import Connect
# from interfaces.dependencies import get_current_user


router = APIRouter()




@router.post("/register/", response_model=Meal)
async def create_meal(meal:Meal, db:Session = Depends(Connect.get_db)):
    meal_gateway = DietGateway(db)
    meal_usecase = DietUseCase(meal_gateway)
    return await meal_usecase.create_diet(meal.name, meal.calories, meal.protein, meal.carbs, meal.fats)


@router.get("/diet/{meal_id}")
async def get_meal(meal_id:int, db:Session = Depends(Connect.get_db)):
    meal_gateway = DietGateway(db)
    meal_usecase = DietUseCase(meal_gateway)
    return await meal_usecase.get_diet(meal_id)



@router.get("/diets")
async def get_diets(db: Session = Depends(Connect.get_db)):
    meal_gateway = DietGateway(db)
    meal_usecase = DietUseCase(meal_gateway)
    return await meal_usecase.get_diets()
