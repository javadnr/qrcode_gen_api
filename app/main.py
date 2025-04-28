from fastapi import FastAPI
from app.api.v1.endpoints import generate
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(generate.router, prefix="/api/v1/qrcode", tags=["QRCode"])
