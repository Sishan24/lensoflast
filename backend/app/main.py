from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.core.config import settings
from backend.app.api.routes import health, scans

app = FastAPI(title=settings.app_name, version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix=settings.api_v1_prefix, tags=["system"])
app.include_router(scans.router, prefix=settings.api_v1_prefix, tags=["scans"])


@app.get("/")
def root():
    return {"app": settings.app_name, "docs": "/docs"}
