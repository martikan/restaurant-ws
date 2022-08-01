""" Manage database connection.
"""

from sqlalchemy import MetaData
from databases import Database
from sqlalchemy.ext import asyncio

from configs import settings

datasource_url = settings.get_datasource_url()

database = Database(datasource_url)

metadata = MetaData()

engine = asyncio.create_async_engine(datasource_url,
                                     echo = True if settings.is_development() else False,
                                     future = True)