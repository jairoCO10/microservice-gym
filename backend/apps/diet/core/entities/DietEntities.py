from dataclasses import dataclass
from datetime import date

@dataclass
class MealReader:
    id:int
    name: str
    calories: int
    protein: float
    carbs: float
    fats: float

@dataclass
class MealCreate:
    name: str
    calories: int
    protein: float
    carbs: float
    fats: float
