from fastapi import FastAPI

app = FastAPI()

from API.auth_routes import auth_router
from API.order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

#Pra rodar a API, colocar no terminal: uvicorn API.api:app --reload