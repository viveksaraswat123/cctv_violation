from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse

from app.routers import detect

app = FastAPI(
    title="CCTV Violation Detection API",
    description="Backend service for AI-powered traffic violation detection using CCTV camera streams.",
    version="1.1.0",
    contact={"name": "Traffic AI System", "email": "support@trafficai.com"},
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(detect.router, prefix="/detect", tags=["Violation Detection"])

@app.get("/", tags=["Root"])
async def root():
    return {"message": "🚦 CCTV Violation Detection API is Running!"}

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "ok", "service": "violation detection"}

@app.exception_handler(StarletteHTTPException)
async def custom_http_error_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "status": exc.status_code},
    )

@app.exception_handler(Exception)
async def global_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "details": str(exc)},
    )
