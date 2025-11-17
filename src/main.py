"""
AgroCare API
"""
from fastapi import FastAPI
from src.config.database import Base, engine
from src.routes.user_routes import user_router


app = FastAPI()
app.title = "AgroCare API"


Base.metadata.create_all(bind=engine)

app.include_router(prefix='/user', router=user_router, tags=['user'])
