# app/main.py
from fastapi import FastAPI

from app.routers.router_check import health
from app.routers.websockets import websocket

app = FastAPI()

app.include_router(health.router)
app.include_router(websocket.router)
