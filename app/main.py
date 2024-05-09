from fastapi import FastAPI
from app.routes.category_routes import router as category_routes


app = FastAPI(title="Project 2")
app.include_router(router=category_routes, tags=["categories"])
