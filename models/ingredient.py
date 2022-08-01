""" Model for ingredients.
"""

from pydantic import BaseModel

class Ingredient(BaseModel):
    """
    Model which contains all ingredient fields.
    """
    
    id: int
    name: str

class CreateUpdateIngredient(BaseModel):
    """
    Model for create or update ingredients.
    """
    
    name: str