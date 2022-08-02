"""Data access layer for ingredients.
"""

from ast import stmt
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
        result = await conn.execute(stmt)
        ingredient_id = result.fetchone()[0]
        await conn.commit()
        result.close()
    
    return {"id": ingredient_id, **payload.dict()}

async def update(id: int, payload: CreateUpdateIngredient) -> Ingredient:
    """Update an ingredient by id.
    @param payload: payload of the ingredient
    @return: Ingredient
    """
    
    stmt = query(f"UPDATE ingredients SET name='{payload.name}' WHERE id = {id} RETURNING id")
    async with engine.connect() as conn:
        result = await conn.execute(stmt)
        ingredient_id = result.fetchone()[0]
        await conn.commit()
        result.close()
    
    return {"id": ingredient_id, **payload.dict()}

async def delete_all_removable() -> None:
    """Delete all ingredients which ones haven't got any relationship.
    """

    stmt = query("DELETE FROM ingredients t WHERE NOT EXISTS (SELECT ingredients_id FROM meals_ingredients WHERE ingredients_id = t.id)")
    async with engine.connect() as conn:
        result = await conn.execute(stmt)
        await conn.commit()
        result.close()

async def delete_by_id(id: int) -> None:
    """Delete an ingredient by id.
    """
    
    stmt = query(f"DELETE FROM ingredients WHERE id = {id}")
    async with engine.connect() as conn:
        result = await conn.execute(stmt)
        await conn.commit()
        result.close()
