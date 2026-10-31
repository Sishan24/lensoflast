from typing import Literal
from pydantic import BaseModel


DateType = Literal[
    "MFD", "EXP", "BEST_BEFORE", "USE_BY", "SHELF_LIFE", "BATCH_CODE", "UNKNOWN"
]


class HealthResponse(BaseModel):
    status: str
    app: str


class ScanAcceptedResponse(BaseModel):
    status: str
    message: str
    filename: str
    analysis_implemented: bool = False
