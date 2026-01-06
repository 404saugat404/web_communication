from fastapi import FastAPI, WebSocket, WebSocketDisconnect

print("successful running after uv")



app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     print("🟢 WebSocket connected")

#     try:
#         while True:
#             message = await websocket.receive_text()
#             print(f"📩 Received: {message}")

#             if message == "bye":
#                 await websocket.send_text("Closing connection from server")
#                 await websocket.close()
#                 break  # 🔴 VERY IMPORTANT

#             await websocket.send_text(f"Echo: {message}")

#     except WebSocketDisconnect:
#         print("🔴 WebSocket disconnected")

import asyncio

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("🟢 WebSocket connected")

    async def server_sender():
        """Server-initiated messages"""
        while True:
            await asyncio.sleep(3)
            await websocket.send_text("📡 Server: ping")

    sender_task = asyncio.create_task(server_sender())

    try:
        while True:
            message = await websocket.receive_text()
            print(f"📩 From browser: {message}")

            await websocket.send_text(f"🧑 Browser said: {message}")

    except WebSocketDisconnect:
        print("🔴 WebSocket disconnected")

    finally:
        sender_task.cancel()
