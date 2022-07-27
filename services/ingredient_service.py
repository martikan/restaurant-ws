"""Service layer for ingredient model.
"""

from models.ingredient import IngredientCreate
from db.db import database
from db.ingredients_meals import ingredients, meals, meals_ingredients

async def find_all():
    """Service to find all ingredients.
    returns a list of ingredients.
    """
    
    query = ingredients.select()
    return await database.fetch_all(query)

async def find_by_id(id: int):
    """Service to find ingredient by id.
    returns an ingredient.
    """
    
    query = ingredients.select().where(ingredients.c.id==id)
    return await database.fetch_one(query)

async def save(payload: IngredientCreate):
    """Service to save an ingredient.
    returns an ingredient.
    """
    
    query = ingredients.insert().values(name=payload.name)
    id = await database.execute(query)
    return {"id": id, **payload.dict()}

async def update(id: int, payload: IngredientCreate):
    """Service to update an ingredient by id.
    returns an ingredient.
    """
    
    query = ingredients.update().where(ingredients.c.id==id).values(**payload.dict())
    await database.execute(query)
    return {"id": id, **payload.dict()}
    

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

async def delete_by_id(id: int):
    """Service to delete an ingredient by id.
    """
    
    query = ingredients.delete().where(ingredients.c.id==id)
    await database.execute(query)