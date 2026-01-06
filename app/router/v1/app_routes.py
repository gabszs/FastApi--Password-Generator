from fastapi import APIRouter
from fastapi import Request

from app.core.telemetry import logger

router = APIRouter(tags=["Password-Generator"])


@router.get("/health")
async def health():
    logger.info("Service is healthy and running.")
    return {"status": "alive"}


@router.get("/debug")
async def debug(request: Request):
    return {
        "headers": dict(request.headers),
        "geo": {
            "country": request.headers.get("cf-ipcountry"),
            "city": request.headers.get("cf-ipcity"),
            "isp": request.headers.get("cf-ipasnorganization"),
        },
    }
