"""Service layer for ingredient model.
"""
from models.ingredient import IngredientCreate
from db import database, ingredients

"""find_all
Service to find all ingredients.
@return list of ingredients
"""
async def find_all():
    query = ingredients.select()
    return await database.fetch_all(query)

"""find_by_id
Service to find ingredient by id.
@return ingredient
"""
async def find_by_id(id: int):
    query = ingredients.select().where(ingredients.c.id==id)
    return await database.fetch_one(query)

"""save
Service to save an ingredient.
@return ingredient
"""
async def save(payload: IngredientCreate):
    query = ingredients.insert().values(name=payload.name)
    id = await database.execute(query)
    return {"id": id, **payload.dict()}

"""update
Service to update an ingredient.
@return ingredient
"""
async def update(id: int, payload: IngredientCreate):
    query = ingredients.update().where(ingredients.c.id==id).values(**payload.dict())
    await database.execute(query)
    return {"id": id, **payload.dict()}
    

"""delete
Service to delete an ingredient by id.
"""
async def delete_by_id(id: int):
    query = ingredients.delete().where(ingredients.c.id==id)
    await database.execute(query)