"""Service layer for ingredients.
"""

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
    
    return await dao.find_by_id(id)

async def save(payload: CreateUpdateIngredient) -> Ingredient:
    """Service to save ingredient
    @param payload: payload of the ingredient
    @return: Ingredient
    """
    
    return await dao.save(payload)