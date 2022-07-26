""" Model for ingredients.
"""

from pydantic import BaseModel

class IngredientCreate(BaseModel):
    """
    Model for create new ingredients.
    """
    
    name: str

class IngredientAll(BaseModel):
    """
    Model which contains all ingredient fields.
    """
    
    id: int
    name: str