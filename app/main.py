from fastapi import FastAPI, WebSocket, WebSocketDisconnect

print("successful running after uv")
from app.services.connection_manager.connection_manager import ConnectionManager

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# import asyncio

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     print("🟢 WebSocket connected")

#     async def server_sender():
#         """Server-initiated messages"""
#         while True:
#             await asyncio.sleep(3)
#             await websocket.send_text("📡 Server: ping")

#     sender_task = asyncio.create_task(server_sender())

#     try:
#         while True:
#             message = await websocket.receive_text()
#             print(f"📩 From browser: {message}")

#             await websocket.send_text(f"🧑 Browser said: {message}")

#     except WebSocketDisconnect:
#         print("🔴 WebSocket disconnected")

#     finally:
#         sender_task.cancel()


from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()
manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            print(f"📩 Received: {message}")

            await manager.broadcast(f"💬 {message}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)