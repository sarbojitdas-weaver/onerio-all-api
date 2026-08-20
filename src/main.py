from fastapi import FastAPI
from src.apps.api.v1_router import api_router

app = FastAPI(
    title="Oneiro Backend",
    version="1.0.0",
)

# Include API Router
app.include_router(api_router, prefix="/api/v1")

@app.get("/healthcheck", tags=["System"])
async def healthcheck():
    return {"status": "ok", "service": "Oneiro Backend Engine"}