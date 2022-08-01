"""Domain layer for meals and ingredients tables.
"""

from sqlalchemy import Table, Column, Integer, String, Float, Boolean, ForeignKey

from db.db import metadata

# Assoc. table for meals & ingredients.
meals_ingredients = Table(
    "meals_ingredients",
    metadata,
    Column("meal_id", ForeignKey("meals.id"), primary_key=True),
    Column("ingredient_id", ForeignKey("ingredients.id"), primary_key=True),
)

# Ingredients table.
ingredients = Table(
    "ingredients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), unique=True, nullable=False),
)

# Meals table.
meals = Table(
    "meals",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), unique=True, nullable=False),
    Column("price", Float, nullable=False),
    Column("spicy", Integer, nullable=False),
    Column("vegan", Boolean, nullable=False),
    Column("gluten_free", Boolean, nullable=False),
    Column("kcal", Integer, nullable=False),
)