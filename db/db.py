""" Manage database connection.
"""

from sqlalchemy import (create_engine)
from databases import Database

from configs import settings

datasource_url = settings.get_datasource_url()

database = Database(datasource_url)

engine = create_engine(datasource_url)