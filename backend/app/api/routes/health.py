from fastapi import APIRouter
from backend.app.core.config import settings
from backend.app.schemas.scan import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(status="ok", app=settings.app_name)
