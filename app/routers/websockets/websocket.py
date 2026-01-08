# app/routers/websocket.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json

from app.services.connection_manager.connection_manager import ConnectionManager

router = APIRouter()
manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        # Step 1: receive join message
        join_data = await websocket.receive_text()
        join_msg = json.loads(join_data)

        if join_msg.get("type") != "join":
            await websocket.close()
            return

        username = join_msg["username"]
        manager.register(websocket, username)

        await manager.broadcast(f"🟢 {username} joined the chat")

        # Step 2: normal chat loop
        while True:
            message = await websocket.receive_text()
            await manager.broadcast(f"[{username}]: {message}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"🔴 {username} left the chat")
