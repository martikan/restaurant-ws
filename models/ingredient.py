""" Model for ingredients.
"""
from pydantic import BaseModel

""" IngredientCreate
Model for create new ingredients.
"""
class IngredientCreate(BaseModel):
    name: str

""" IngredientAll
Model which contains all ingredient fields.
"""
class IngredientAll(BaseModel):
    id: int
    name: str