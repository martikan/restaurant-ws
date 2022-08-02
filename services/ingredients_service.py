"""Service layer for ingredients.
"""

from fastapi import HTTPException
from typing import List
from dao import ingredients_dao as dao
from models.ingredient import Ingredient, CreateUpdateIngredient

async def find_all() -> List[Ingredient]:
    """Service to find all ingredients.
    @return: List of ingredients
    """
    
    return await dao.find_all()

async def find_by_id(id: int) -> Ingredient:
    """Service to find an ingredient by id.
    @param id: id of the ingredient
    @return: Ingredient
    """
    
    ingredient = await dao.find_by_id(id)
    if ingredient is None:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    
    return 

async def save(payload: CreateUpdateIngredient) -> Ingredient:
    """Service to save ingredient
    @param payload: payload of the ingredient
    @return: Ingredient
    """
    
    return await dao.save(payload)

async def update(id: int, payload: CreateUpdateIngredient) -> Ingredient:
    """Service to update ingredient if exist.
    @param payload: payload of the ingredient
    @return: Ingredient
    """
    
    await find_by_id(id)
    return await dao.update(id, payload)

async def delete_all_removable() -> None:
    """Service to delete all removable ingredients.
    """
    
    return await dao.delete_all_removable()

async def delete_by_id(id: int) -> None:
    """Service to delete ingredient by id.
    """
    
    await find_by_id(id)
    return await dao.delete_by_id(id)