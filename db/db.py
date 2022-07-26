""" Manage database connection.
"""

from sqlalchemy import (create_engine)
from databases import Database
from sqlalchemy.ext.declarative import declarative_base

from configs import settings

datasource_url = settings.get_datasource_url()

database = Database(datasource_url)

Base = declarative_base()

Metadata = Base.metadata

engine = create_engine(datasource_url)