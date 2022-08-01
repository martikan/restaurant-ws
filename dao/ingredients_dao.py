"""Data access layer for ingredients.
"""

from re import A
from typing import List
from models.ingredient import Ingredient, CreateUpdateIngredient
from db.db import engine
from db.ingredients_meals import ingredients, meals, meals_ingredients
from sqlalchemy import text as query

async def find_all() -> List[Ingredient]:
    """Find all ingredients.
    @return: Ingredient
    """
    
    stmt = query("SELECT id, name FROM ingredients")
    async with engine.connect() as conn:
        result = await conn.execute(stmt)
        ingredients = result.fetchall()
        result.close()

    return ingredients

async def find_by_id(id: int) -> Ingredient:
    """Find an ingredient by id.
    @param id: id of the ingredient
    @return: Ingredient
    """
    
    stmt = query(f"SELECT id, name FROM ingredients WHERE id = {id}")
    async with engine.connect() as conn:
        result = await conn.execute(stmt)
        ingredient = result.fetchone()
        result.close()
    
    return ingredient

async def save(payload: CreateUpdateIngredient) -> Ingredient:
    """Save an ingredient.
    @param payload: payload of the ingredient
    @return: Ingredient
    """
    
    stmt = query(f"INSERT INTO ingredients(name) VALUES('{payload.name}') RETURNING id")
    async with engine.connect() as conn:
        result = await conn.execute(stmt, (payload.name,))
        ingredient_id = result.fetchone()[0]
        await conn.commit()
        result.close()
    
    return {"id": ingredient_id, **payload.dict()}

# async def update(id: int, payload: IngredientCreate):
#     """Service to update an ingredient by id.
#     returns an ingredient.
#     """
    
#     query = ingredients.update().where(ingredients.c.id==id).values(**payload.dict())
#     await database.execute(query)
#     return {"id": id, **payload.dict()}
    

# async def delete_all():
#     """Service to delete all ingredients.
#     Returns STATUS 404 if it's not exist.
#     Else return STATUS 200 with DELETED message.
#     fe.: {"status_code": 200, "message": "DELETED"}
#     """

#     # Check foreign keys.
#     query = meals_ingredients.select().where(meals_ingredients.c.ingredient_id)

#     # Delete all ingredients.
#     query = ingredients.delete()
#     await database.execute(query)

# async def delete_by_id(id: int):
#     """Service to delete an ingredient by id.
#     """
    
#     query = ingredients.delete().where(ingredients.c.id==id)
#     await database.execute(query)