from fastapi import FastAPI
from app.routes.category_routes import router as category_routes
from app.routes.category_routes import router as category_routes
from app.routes.product_routes import router as product_routes
from app.routes.user_routes import router as user_routes
from app.routes.poc_routes import router as poc_routes


app = FastAPI(title="Project 2")

app.include_router(router=category_routes, tags=["categories"])
app.include_router(router=product_routes, tags=["products"])
app.include_router(router=user_routes, tags=["users"])
app.include_router(router=poc_routes, tags=["pocs"])
