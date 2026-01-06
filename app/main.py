from fastapi import FastAPI, WebSocket, WebSocketDisconnect

print("successful running after uv")



app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("🟢 WebSocket connected")

    try:
        while True:
            message = await websocket.receive_text()
            print(f"📩 Received: {message}")

            await websocket.send_text(f"Echo: {message} , this is me")

    except WebSocketDisconnect:
        print("🔴 WebSocket disconnected")