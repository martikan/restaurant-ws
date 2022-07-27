"""Router for ingredients model.
"""

from typing import List
from fastapi import APIRouter

from models.ingredient import IngredientAll, IngredientCreate
from services import ingredient_service

router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"]
)

@router.get("/", response_model=List[IngredientAll])
async def get_ingredients():
    """Controller to get all ingredients.
    """
    
    return await ingredient_service.find_all()

@router.post("/", response_model=IngredientAll, status_code=201)
async def create_ingredient(payload: IngredientCreate):
    """Controller to create a new ingredient.
    """
    
    return await ingredient_service.save(payload)

@router.get("/{id}", response_model=IngredientAll)
async def get_ingredient_by_id(id: int):
    """Controller to get an ingredient by id.
    """
    
    return await ingredient_service.find_by_id(id)

@router.put("/{id}", response_model=IngredientAll)
async def update_ingredients(id: int, payload: IngredientCreate):
    """Controller to update an ingredient by id.
    """
    
    return await ingredient_service.update(id, payload)

async def delete_all_ingredients():
    """Controller to delete all ingredients.
    """

    #TODO: add service for it.

@router.delete("/{id}")
async def delete_ingredient_by_id(id: int):
    """Controller to delete an ingredient by id.
    """
    
    await ingredient_service.delete_by_id(id)
    return 