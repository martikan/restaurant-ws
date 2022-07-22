from pydantic import BaseModel

class Ingredient(BaseModel):
    id: int(64)
    name: str