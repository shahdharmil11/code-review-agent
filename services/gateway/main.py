from fastapi import FastAPI

from models import Settings

settings = Settings()
app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}
