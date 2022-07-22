# meals.py

from typing import List
from fastapi import APIRouter
from pydantic import BaseModel

from api.models.ingredient import Ingredient

router = APIRouter(
    prefix="/meals",
    tags=["meals"],
    responses={404: {"message": "Meal has not found"}}
)

class MealDTO(BaseModel):
    id: int(64)
    name: str
    price: float
    spicy: int
    vegan: bool
    gluten_free: bool
    kcal: int
    ingredients: List[Ingredient]

@router.get("/")
async def get_meals():
    return [{"name": "Meal"}]

@router.post("/")
async def create_meal(meal: MealDTO):
    return meal

@router.get("/{id}")
async def get_meal_by_id(id: int(64)):
    return id

@router.put("/{id}")
async def update_meal(id: int, meal: MealDTO):
    return {"id": id, "meal": meal}