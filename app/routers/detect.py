from fastapi import APIRouter, UploadFile, File
from app.schemas.detect import DetectionResponse

router = APIRouter(
    prefix="/detect",
    tags=["Detection"]
)

@router.post("/", response_model=DetectionResponse)
async def detect_violation(file: UploadFile = File(...)):
    """
    This endpoint will:
    - Read uploaded image
    - Pass it to YOLO model (later)
    - Return detection + violation results
    """
    
    # TEMP LOGIC (you will replace this with ML inference)
    image_bytes = await file.read()

    return {
        "violations": [],
        "detections": [],
        "message": "ML model not added yet"
    }
