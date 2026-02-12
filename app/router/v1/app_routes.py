from datetime import datetime
from datetime import timezone

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.telemetry import logger

router = APIRouter(tags=["Password-Generator"])


@router.get("/health")
async def health():
    logger.info("Service is healthy and running.")
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/debug")
async def debug(request: Request):
    logger.info(f"Request headers: {request.headers}")
    return JSONResponse(
        content={
            "headers": dict(request.headers),
            "geo": {
                "country": request.headers.get("cf-ipcountry"),
                "city": request.headers.get("cf-ipcity"),
                "isp": request.headers.get("cf-ipasnorganization"),
            },
        },
        media_type="application/json; charset=utf-8",
    )
