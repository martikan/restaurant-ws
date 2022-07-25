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

@router.post("/", response_model=IngredientAll)
async def create_ingredient(payload: IngredientCreate):
    return await ingredientService.save(payload)

@router.get("/{id}", response_model=IngredientAll)
async def get_ingredient_by_id(id: int):
    return await ingredientService.find_by_id(id)

@router.put("/{id}", response_model=IngredientAll)
async def update_ingredients(id: int, payload: IngredientCreate):
    return await ingredientService.update(id, payload)

@router.delete("/{id}")
async def delete_ingredient_by_id(id: int):
    await ingredientService.delete_by_id(id)
    return 