""" Database connections and database tables.
"""
from sqlalchemy import (MetaData, create_engine)
from databases import Database

from configs import settings

datasource_url = settings.get_datasource_url()

metadata = MetaData()

from sqlalchemy import (Column, Integer, Float, String, Table, ForeignKey, Boolean, MetaData)

metadata = MetaData()

database = Database(datasource_url)

"""
Ingredients table.
"""
ingredients = Table(
    "ingredients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), unique=True, nullable=False),
)

"""
Meals table.
"""
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

"""
Assoc. table for meals & ingredients.
"""
meals_ingredients = Table(
    "meals_ingredients",
    metadata,
    Column("meal_id", ForeignKey("meals.id"), primary_key=True),
    Column("meal_id", ForeignKey("ingredients.id"), primary_key=True),
)

engine = create_engine(datasource_url)