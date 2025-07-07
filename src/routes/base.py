from fastapi import APIRouter, FastAPI

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}