import json
from datetime import datetime
from datetime import timezone

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse
from typing import Any

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


def _debug_response(request: Request, body: Any = None) -> JSONResponse:
    return JSONResponse(
        content={
            "headers": dict(request.headers),
            "geo": {
                "country": request.headers.get("cf-ipcountry"),
                "city": request.headers.get("cf-ipcity"),
                "isp": request.headers.get("cf-ipasnorganization"),
            },
            "body": body,
        },
        media_type="application/json; charset=utf-8",
    )

@router.post("/debug")
async def debug_post(request: Request):
    logger.info(f"Debug POST received. Request headers: {request.headers}")

    raw_body = await request.body()
    parsed_body: Any = None

    if raw_body:
        decoded_body = raw_body.decode("utf-8", errors="replace")
        try:
            parsed_body = json.loads(decoded_body)
        except json.JSONDecodeError:
            parsed_body = decoded_body

    return _debug_response(request=request, body=parsed_body)
