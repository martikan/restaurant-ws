# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from  api.routers import meals

app = FastAPI()
app.include_router(meals.router)

# Only for testing purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)