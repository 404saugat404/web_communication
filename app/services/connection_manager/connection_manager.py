

from typing import List
from fastapi import WebSocket
from typing import Dict


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[WebSocket, str] = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()

    def register(self, websocket: WebSocket, username: str):
        self.active_connections[websocket] = username
        print(f"🟢 {username} joined ({len(self.active_connections)} users)")

    def disconnect(self, websocket: WebSocket):
        username = self.active_connections.get(websocket, "Unknown")
        self.active_connections.pop(websocket, None)
        print(f"🔴 {username} left ({len(self.active_connections)} users)")

    async def broadcast(self, message: str):
        for ws in self.active_connections:
            await ws.send_text(message)
