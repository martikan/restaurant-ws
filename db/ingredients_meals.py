""" Domain layer for meals and ingredients tables.
"""

from sqlalchemy import Table, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.db import Metadata

# Assoc. table for meals & ingredients.
meals_ingredients = Table(
    "meals_ingredients",
    
    Metadata,
    Column("meal_id", ForeignKey("meals.id"), primary_key=True),
    Column("meal_id", ForeignKey("ingredients.id"), primary_key=True),
)

# Ingredients table.
ingredients = Table(
    "ingredients",
    Metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), unique=True, nullable=False),
)

# Meals table.
meals = Table(
    "meals",
    Metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), unique=True, nullable=False),
    Column("price", Float, nullable=False),
    Column("spicy", Integer, nullable=False),
    Column("vegan", Boolean, nullable=False),
    Column("gluten_free", Boolean, nullable=False),
    Column("kcal", Integer, nullable=False),
)