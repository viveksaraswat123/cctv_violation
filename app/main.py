from fastapi import FastAPI
from app.routers import detect

app = FastAPI(
    title="CCTV Violation Detection API",
    description="Backend for AI-powered traffic violation detection.",
    version="1.0.0"
)

# include routers
app.include_router(detect.router)

@app.get("/")
def root():
    return {"message": "CCTV Violation API Running"}
