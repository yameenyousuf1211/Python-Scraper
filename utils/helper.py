from fastapi.responses import JSONResponse
from typing import Any, Dict

def generateResponse(message: str, data: Dict[str, Any] = None, statusCode: int = 200) -> JSONResponse:
    responseContent = {
        "message": message,
        "data": data
    }
    return JSONResponse(content=responseContent, status_code=statusCode)