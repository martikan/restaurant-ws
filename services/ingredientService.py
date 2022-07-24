"""Service layer for ingredient model.
"""

from models.ingredient import IngredientAll, IngredientCreate
from db import database, ingredients

"""save
Service for save an ingredient.
@return ingredient
"""
async def save(payload: IngredientCreate):
    query = ingredients.insert().values(name=payload.name)
    id = await database.execute(query)
    
    return {"id": id, **payload.dict()}

"""find_all
Service for find all ingredients.
@return list of ingredients
"""
async def find_all():
    query = ingredients.select()
    return await database.fetch_all(query)