from pydantic import BaseModel
from typing import List, Optional

class Box(BaseModel):
    class_name: str
    confidence: float
    bbox: List[float]

class DetectionResponse(BaseModel):
    violations: List[str]
    detections: List[Box]
    message: Optional[str] = None
