from fastapi import APIRouter
from utils.helper import generateResponse

router = APIRouter(prefix="/api", tags=["default"])


@router.get("/")
async def root_api():
    return generateResponse("Health Check Passed")