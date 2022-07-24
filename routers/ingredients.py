"""Router for ingredients model.
"""
from typing import List
from fastapi import APIRouter

from models.ingredient import IngredientAll, IngredientCreate
from services import ingredientService

router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
    responses={404: {"message": "Ingredient has not found"}}
)

@router.get("/", response_model=List[IngredientAll])
async def get_ingredients():
    return ingredientService.find_all()

@router.post("/")
async def create_ingredient(payload: IngredientCreate):
    return await ingredientService.save(payload)

# @router.get("/{id}")
# async def get_ingredient_by_id(id: int(64)):
#     return id

# @router.put("/{id}")
# async def update_ingredients(id: int, payload: MealDTO):
#     return {"id": id, "meal": meal}