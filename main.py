"""
Main
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import ingredients_router_v1
from db.db import database

from configs import settings

API_PREFIX = "/api"

app = FastAPI()

@app.on_event("startup")
async def startup():
    """
    Startup event.
    * Connect to database.
    """
    
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    """
    Shut-down event.
    * Disconnect from database.
    """
    await database.disconnect()

################################
##### Set-up API routers. ######
################################
app.include_router(ingredients_router_v1.router, prefix=API_PREFIX)
# app.include_router(meals_router_v1.router)


if (settings.is_development()):
    """If it's in development mode, then allow all origins.
    """
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
