"""create_meals_and_migrations

Revision ID: 8123ce807797
Revises: 
Create Date: 2022-07-24 12:50:44.618807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8123ce807797'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    conn = op.get_bind()
    
    """
    Create INGREDIENTS table.
    """
    conn.execute(
        "CREATE TABLE IF NOT EXISTS ingredients ( " +
        "id serial PRIMARY KEY, " +
        "name varchar(50) UNIQUE NOT NULL " +
        ");"
    )
    
    """
    Create MEALS table.
    """
    conn.execute(
        "CREATE TABLE IF NOT EXISTS meals ( " +
        "id serial PRIMARY KEY, " +
        "name varchar(100) UNIQUE NOT NULL, " +
        "price real NOT NULL, " +
        "spicy smallint NOT NULL, " +
        "vegan boolean NOT NULL, " +
        "gluten_free boolean NOT NULL, " +
        "kcal smallint NOT NULL " +
        ");"
    )
    
    """
    Create Assoc. table for meals & ingredients tables.
    """
    conn.execute(
        "CREATE TABLE IF NOT EXISTS meals_ingredients ( " +
        "meal_id integer NOT NULL, " +
        "ingredient_id integer NOT NULL, " +
        "PRIMARY KEY (meal_id, ingredient_id), " +
        "CONSTRAINT FK_MEALS_INGREDIENTS_MEAL FOREIGN KEY (meal_id) REFERENCES meals(id), " +
        "CONSTRAINT FK_MEALS_INGREDIENTS_INGREDIENT FOREIGN KEY (ingredient_id) REFERENCES ingredients(id) " +
        ");"
    )
    


def downgrade():
    conn = op.get_bind()
    
    """
    Drop meals_ingredients table.
    """
    conn.execute("DROP TABLE IF EXISTS meals_ingredients;")
    
    """
    Drop ingredients table.
    """
    conn.execute("DROP TABLE IF EXISTS ingredients;")

    """
    Drop meals table.
    """
    conn.execute("DROP TABLE IF EXISTS meals;")
