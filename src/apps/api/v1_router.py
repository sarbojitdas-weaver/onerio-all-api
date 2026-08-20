from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/ping")
async def ping():
    return {"message": "v1 router is active"}