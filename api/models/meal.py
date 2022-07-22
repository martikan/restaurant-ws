from typing import List
from pydantic import BaseModel

from api.models.ingredient import Ingredient

class Meal(BaseModel):
    id: int(64)
    name: str
    price: float
    spicy: int
    vegan: bool
    gluten_free: bool
    kcal: int
    ingredients: List[Ingredient]