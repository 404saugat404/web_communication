from fastapi import FastAPI

print("successful running after uv")



app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}
