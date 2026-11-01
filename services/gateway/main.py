import hashlib
import hmac

from fastapi import FastAPI, HTTPException, Request

from models import Settings

settings = Settings()
app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/webhook/github")
async def github_webhook(request: Request):
    body = await request.body()
    signature_header = request.headers.get("X-Hub-Signature-256", "")

    expected = (
        "sha256="
        + hmac.new(
            settings.github_webhook_secret.encode(),
            body,
            hashlib.sha256,
        ).hexdigest()
    )

    if not hmac.compare_digest(expected, signature_header):
        raise HTTPException(status_code=401, detail="Invalid signature")

    return {"status": "ok"}
