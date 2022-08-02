"""Router for ingredients model.
"""

from typing import List
from fastapi import APIRouter

from models.ingredient import Ingredient, CreateUpdateIngredient
from services import ingredients_service

router = APIRouter(
    prefix="/v1/ingredients",
    tags=["ingredients"]
)

@router.get("", response_model=List[Ingredient])
async def get_ingredients():
    """Controller to get all ingredients.
    """
    
    return await ingredients_service.find_all()

@router.post("", response_model=Ingredient, status_code=201)
async def create_ingredient(payload: CreateUpdateIngredient):
    """Controller to create a new ingredient.
    """
    
    return await ingredients_service.save(payload)

@router.get("/{id}", response_model=Ingredient)
async def get_ingredient_by_id(id: int):
    """Controller to get an ingredient by id.
    """
    
    return await ingredients_service.find_by_id(id)

@router.put("/{id}", response_model=Ingredient)
async def update_ingredients(id: int, payload: CreateUpdateIngredient):
    """Controller to update an ingredient by id.
    """
    
    return await ingredients_service.update(id, payload)

@router.delete("/delete-all-removable")
async def delete_all_ingredients() -> None:
    """Controller to delete all removable ingredients.
    """

    await ingredients_service.delete_all_removable()

@router.delete("/{id}")
async def delete_ingredient_by_id(id: int) -> None:
    """Controller to delete an ingredient by id.
    """
    
    await ingredients_service.delete_by_id(id)