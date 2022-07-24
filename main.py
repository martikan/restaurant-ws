""" Main
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import ingredients
from db import database

API_PREFIX = "/api/v1"

app = FastAPI()

"""
Manage db connection.
"""
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

"""
Set-up API routers.
"""
app.include_router(ingredients.router, prefix=API_PREFIX)
# app.include_router(meals.router)

"""
Only for testing purposes.
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
