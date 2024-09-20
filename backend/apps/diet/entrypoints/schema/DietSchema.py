from pydantic import BaseModel
from typing import Optional, List


class Meal(BaseModel):
    name: str
    calories: int
    protein: float
    carbs: float
    fats: float

class DietPlan(BaseModel):
    user_id: int
    date: str  # en formato YYYY-MM-DD
    meals: List[Meal]
