from pathlib import Path
from fastapi import APIRouter, File, HTTPException, UploadFile
from backend.app.core.config import settings
from backend.app.schemas.scan import ScanAcceptedResponse

router = APIRouter()

ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_BYTES = settings.max_upload_mb * 1024 * 1024


@router.post("/scan", response_model=ScanAcceptedResponse)
async def scan_product(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=415, detail="Upload a JPEG, PNG or WEBP image.")

    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="The uploaded file is empty.")
    if len(content) > MAX_BYTES:
        raise HTTPException(status_code=413, detail=f"Image exceeds {settings.max_upload_mb} MB.")

    # TODO: decode and validate image bytes, then call the trained inference pipeline.
    # Do not save untrusted uploads using the original filename.
    safe_name = Path(file.filename or "upload").name
    return ScanAcceptedResponse(
        status="accepted",
        message="Upload received. Deep Learning inference is not connected yet.",
        filename=safe_name,
        analysis_implemented=False,
    )
